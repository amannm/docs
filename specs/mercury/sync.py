#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
from __future__ import annotations

import argparse
import os
import re
import sys
import time
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen


DOCS_ORIGIN = "https://docs.mercury.com"
DEFAULT_REFERENCE_ROOT = "/reference"
DEFAULT_SEED_PATH = "/reference/getaccount"
SITEMAP_URL = f"{DOCS_ORIGIN}/sitemap.xml"
SITEMAP_NAMESPACE = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
REQUEST_HEADERS = {
    "User-Agent": "MercuryDocSync/1.0 (+https://docs.mercury.com/reference/getaccount)",
}
REFERENCE_ATTR_PATTERN = re.compile(r'(?:href|data-url)="([^"#?]+)"')
ABSOLUTE_LINK_PATTERN = re.compile(
    r"\((https://docs\.mercury\.com(?P<path>/[^)#>\s]+)(?P<anchor>#[^)]+)?)\)"
)
RELATIVE_LINK_PATTERN = re.compile(r"\(((?P<path>/[^)#>\s]+)(?P<anchor>#[^)]+)?)\)")
AUTOLINK_PATTERN = re.compile(
    r"<https://docs\.mercury\.com(?P<path>/[^>#\s]+)(?P<anchor>#[^>]+)?>"
)


@dataclass(slots=True)
class FetchResult:
    text: str
    final_url: str
    content_type: str


@dataclass(slots=True)
class SyncResult:
    reference_path: str
    output_path: Path
    url: str
    error: str | None = None

    @property
    def ok(self) -> bool:
        return self.error is None


def fetch(url: str, timeout: float, retries: int, retry_delay: float) -> FetchResult:
    last_error: Exception | None = None
    for attempt in range(1, retries + 1):
        request = Request(url, headers=REQUEST_HEADERS)
        try:
            with urlopen(request, timeout=timeout) as response:
                body = response.read().decode("utf-8")
                return FetchResult(
                    text=body,
                    final_url=response.geturl(),
                    content_type=response.headers.get_content_type(),
                )
        except HTTPError as exc:
            last_error = exc
            if exc.code in {404, 410}:
                raise
        except URLError as exc:
            last_error = exc

        if attempt < retries:
            time.sleep(retry_delay * attempt)

    assert last_error is not None
    raise last_error


def normalize_reference_root(candidate: str) -> str | None:
    parsed = urlparse(candidate)
    if parsed.scheme and parsed.netloc and parsed.netloc != "docs.mercury.com":
        return None

    path = parsed.path.rstrip("/") or "/"
    if path == "/reference":
        return path

    match = re.fullmatch(r"/([^/]+)/reference", path)
    if match:
        return path

    return None


def reference_root_for(path: str) -> str | None:
    normalized = path.rstrip("/") or "/"
    if normalized == "/reference" or normalized.startswith("/reference/"):
        return "/reference"

    match = re.fullmatch(r"/([^/]+)/reference(?:/.*)?", normalized)
    if match:
        return f"/{match.group(1)}/reference"

    return None


def normalize_reference_path(candidate: str, allowed_roots: set[str] | None = None) -> str | None:
    parsed = urlparse(candidate)
    if parsed.scheme and parsed.netloc and parsed.netloc != "docs.mercury.com":
        return None

    path = parsed.path.rstrip("/") or "/"
    if path.endswith(".md"):
        path = path.removesuffix(".md")

    root = reference_root_for(path)
    if root is None:
        return None
    if allowed_roots is not None and root not in allowed_roots:
        return None
    return path


def output_path_for(reference_path: str, output_dir: Path) -> Path:
    parts = [part for part in reference_path.split("/") if part]
    if not parts:
        raise ValueError(f"Unsupported reference path: {reference_path}")

    if parts[0] == "reference":
        relative_parts = parts[1:]
    elif len(parts) >= 2 and parts[1] == "reference":
        relative_parts = [parts[0], *parts[2:]]
    else:
        raise ValueError(f"Unsupported reference path: {reference_path}")

    if not relative_parts:
        raise ValueError(f"No markdown export is available for root path {reference_path}")

    return output_dir.joinpath(*relative_parts).with_suffix(".md")


def markdown_url_for(reference_path: str) -> str:
    return f"{DOCS_ORIGIN}{reference_path}.md"


def extract_reference_paths_from_markup(markup: str, allowed_roots: set[str] | None = None) -> set[str]:
    paths: set[str] = set()
    for candidate in REFERENCE_ATTR_PATTERN.findall(markup):
        normalized = normalize_reference_path(candidate, allowed_roots=allowed_roots)
        if normalized:
            paths.add(normalized)
    return paths


def discover_reference_roots(timeout: float, retries: int, retry_delay: float, include_public_versions: bool) -> list[str]:
    roots = {DEFAULT_REFERENCE_ROOT}
    if not include_public_versions:
        return [DEFAULT_REFERENCE_ROOT]

    seed_html = fetch(f"{DOCS_ORIGIN}{DEFAULT_SEED_PATH}", timeout, retries, retry_delay).text
    for path in extract_reference_paths_from_markup(seed_html):
        root = reference_root_for(path)
        if root:
            roots.add(root)

    ordered = [DEFAULT_REFERENCE_ROOT]
    ordered.extend(sorted(root for root in roots if root != DEFAULT_REFERENCE_ROOT))
    return ordered


def discover_reference_paths_from_sitemap(
    allowed_roots: set[str],
    timeout: float,
    retries: int,
    retry_delay: float,
) -> set[str]:
    sitemap_xml = fetch(SITEMAP_URL, timeout, retries, retry_delay).text
    root = ET.fromstring(sitemap_xml)

    paths: set[str] = set()
    for loc in root.findall("sm:url/sm:loc", SITEMAP_NAMESPACE):
        if not loc.text:
            continue
        normalized = normalize_reference_path(loc.text, allowed_roots=allowed_roots)
        if normalized:
            paths.add(normalized)
    return paths


def discover_reference_paths_from_html(
    reference_root: str,
    timeout: float,
    retries: int,
    retry_delay: float,
    crawl: bool,
) -> set[str]:
    allowed_roots = {reference_root}
    discovered: set[str] = set()
    pending = [reference_root]
    fetched: set[str] = set()

    while pending:
        path = pending.pop()
        if path in fetched:
            continue
        fetched.add(path)

        html = fetch(f"{DOCS_ORIGIN}{path}", timeout, retries, retry_delay).text
        candidates = extract_reference_paths_from_markup(html, allowed_roots=allowed_roots)
        new_paths = candidates - discovered
        discovered.update(new_paths)

        if crawl:
            pending.extend(sorted(new_paths - fetched))

    return discovered


def discover_reference_paths(
    roots: Iterable[str],
    timeout: float,
    retries: int,
    retry_delay: float,
) -> list[str]:
    root_list = list(dict.fromkeys(roots))
    allowed_roots = set(root_list)
    sitemap_paths = discover_reference_paths_from_sitemap(
        allowed_roots=allowed_roots,
        timeout=timeout,
        retries=retries,
        retry_delay=retry_delay,
    )
    roots_with_sitemap = {reference_root_for(path) for path in sitemap_paths}

    all_paths = set(sitemap_paths)
    for root in root_list:
        html_paths = discover_reference_paths_from_html(
            root,
            timeout=timeout,
            retries=retries,
            retry_delay=retry_delay,
            crawl=root not in roots_with_sitemap,
        )
        all_paths.update(html_paths)

    root_set = set(root_list)
    return sorted(path for path in all_paths if path not in root_set)


def rewrite_internal_links(content: str, current_path: str, known_paths: set[str], output_dir: Path) -> str:
    current_output = output_path_for(current_path, output_dir)
    current_dir = current_output.parent

    def to_relative(reference_path: str, anchor: str | None) -> str | None:
        normalized = normalize_reference_path(reference_path)
        if not normalized or normalized not in known_paths:
            return None

        target = output_path_for(normalized, output_dir)
        relative = os.path.relpath(target, current_dir).replace(os.sep, "/")
        return f"{relative}{anchor or ''}"

    def replace_link(match: re.Match[str]) -> str:
        rewritten = to_relative(match.group("path"), match.groupdict().get("anchor"))
        if not rewritten:
            return match.group(0)
        return f"({rewritten})"

    def replace_autolink(match: re.Match[str]) -> str:
        rewritten = to_relative(match.group("path"), match.groupdict().get("anchor"))
        if not rewritten:
            return match.group(0)
        return f"<{rewritten}>"

    content = ABSOLUTE_LINK_PATTERN.sub(replace_link, content)
    content = RELATIVE_LINK_PATTERN.sub(replace_link, content)
    content = AUTOLINK_PATTERN.sub(replace_autolink, content)
    return content


def sync_one(
    reference_path: str,
    output_dir: Path,
    known_paths: set[str],
    timeout: float,
    retries: int,
    retry_delay: float,
) -> SyncResult:
    destination = output_path_for(reference_path, output_dir)
    url = markdown_url_for(reference_path)
    try:
        response = fetch(url, timeout=timeout, retries=retries, retry_delay=retry_delay)
        if response.content_type == "text/html" and response.text.lstrip().startswith("<!DOCTYPE html"):
            raise ValueError(f"{url} returned HTML instead of markdown")

        content = rewrite_internal_links(response.text, reference_path, known_paths, output_dir)
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(content, encoding="utf-8")
        return SyncResult(reference_path=reference_path, output_path=destination, url=url)
    except Exception as exc:  # noqa: BLE001
        return SyncResult(
            reference_path=reference_path,
            output_path=destination,
            url=url,
            error=str(exc),
        )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Sync Mercury API Markdown docs into the local specs/mercury tree."
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).resolve().parent,
        help="Directory that receives the generated Markdown files.",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=12,
        help="Number of concurrent markdown downloads.",
    )
    parser.add_argument(
        "--roots",
        nargs="+",
        help="Explicit reference roots to sync, for example /reference or /v2/reference.",
    )
    parser.add_argument(
        "--no-public-versions",
        action="store_true",
        help="Only sync the default /reference tree.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        help="Only sync the first N discovered pages. Useful for smoke tests.",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=30.0,
        help="Per-request timeout in seconds.",
    )
    parser.add_argument(
        "--retries",
        type=int,
        default=3,
        help="Number of attempts for each request.",
    )
    parser.add_argument(
        "--retry-delay",
        type=float,
        default=0.5,
        help="Base delay in seconds between retry attempts.",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print every file as it is written.",
    )
    return parser.parse_args()


def resolve_roots(args: argparse.Namespace) -> list[str]:
    if not args.roots:
        return discover_reference_roots(
            timeout=args.timeout,
            retries=args.retries,
            retry_delay=args.retry_delay,
            include_public_versions=not args.no_public_versions,
        )

    resolved: list[str] = []
    for raw_root in args.roots:
        normalized = normalize_reference_root(raw_root)
        if not normalized:
            raise ValueError(f"Unsupported Mercury reference root: {raw_root}")
        resolved.append(normalized)
    return list(dict.fromkeys(resolved))


def main() -> int:
    args = parse_args()
    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    roots = resolve_roots(args)
    print(f"Reference roots: {', '.join(roots)}", file=sys.stderr)

    paths = discover_reference_paths(
        roots=roots,
        timeout=args.timeout,
        retries=args.retries,
        retry_delay=args.retry_delay,
    )

    if args.limit is not None:
        paths = paths[: args.limit]

    known_paths = set(paths)
    print(f"Discovered {len(paths)} Mercury markdown page(s)", file=sys.stderr)

    failures: list[SyncResult] = []
    completed = 0
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
        futures = {
            executor.submit(
                sync_one,
                reference_path,
                output_dir,
                known_paths,
                args.timeout,
                args.retries,
                args.retry_delay,
            ): reference_path
            for reference_path in paths
        }

        for future in as_completed(futures):
            result = future.result()
            completed += 1
            if result.ok:
                if args.verbose:
                    print(
                        f"[{completed}/{len(paths)}] wrote {result.output_path.relative_to(output_dir)}",
                        file=sys.stderr,
                    )
                elif completed % 25 == 0 or completed == len(paths):
                    print(f"[{completed}/{len(paths)}] synced", file=sys.stderr)
            else:
                failures.append(result)
                print(
                    f"[{completed}/{len(paths)}] failed {result.reference_path}: {result.error}",
                    file=sys.stderr,
                )

    if failures:
        print("", file=sys.stderr)
        print(f"{len(failures)} download(s) failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure.reference_path} -> {failure.error}", file=sys.stderr)
        return 1

    print("Sync complete", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

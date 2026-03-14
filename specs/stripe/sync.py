#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen


DOCS_ORIGIN = "https://docs.stripe.com"
API_INDEX_URL = f"{DOCS_ORIGIN}/api"
STATE_MARKER = "window.__INITIAL_STATE__ = "
REQUEST_HEADERS = {
    "User-Agent": "StripeDocSync/1.0 (+https://docs.stripe.com/api)",
}


def fetch_text(url: str, timeout: float, retries: int, retry_delay: float) -> str:
    last_error: Exception | None = None
    for attempt in range(1, retries + 1):
        request = Request(url, headers=REQUEST_HEADERS)
        try:
            with urlopen(request, timeout=timeout) as response:
                return response.read().decode("utf-8")
        except HTTPError as exc:
            if exc.code in {404, 410}:
                raise
            last_error = exc
        except URLError as exc:
            last_error = exc

        if attempt < retries:
            time.sleep(retry_delay * attempt)

    assert last_error is not None
    raise last_error


def extract_initial_state(html: str) -> dict[str, Any]:
    marker_index = html.find(STATE_MARKER)
    if marker_index == -1:
        raise ValueError("Could not find window.__INITIAL_STATE__ in Stripe docs HTML")

    payload = html[marker_index + len(STATE_MARKER):]
    state, _ = json.JSONDecoder().raw_decode(payload)
    if not isinstance(state, dict):
        raise ValueError("Stripe initial state did not decode to an object")
    return state


def normalize_api_path(href: str | None) -> str | None:
    if not href:
        return None

    parsed = urlparse(href)
    if parsed.scheme and parsed.netloc and parsed.netloc != "docs.stripe.com":
        return None

    path = parsed.path.rstrip("/") or "/"
    if path == "/api" or path.startswith("/api/"):
        return path
    return None


def collect_api_paths(node: Any) -> set[str]:
    paths: set[str] = set()

    def walk(value: Any) -> None:
        if isinstance(value, dict):
            for key in ("href", "route"):
                normalized = normalize_api_path(value.get(key))
                if normalized:
                    paths.add(normalized)

            for child in value.values():
                walk(child)
            return

        if isinstance(value, list):
            for item in value:
                walk(item)

    walk(node)
    return paths


def output_path_for(api_path: str, output_dir: Path) -> Path:
    if api_path == "/api":
        return output_dir / "index.md"
    relative = api_path.removeprefix("/api/")
    return output_dir / f"{relative}.md"


def markdown_url_for(api_path: str) -> str:
    return f"{DOCS_ORIGIN}{api_path}.md"


def rewrite_internal_links(content: str, current_path: str, known_paths: set[str], output_dir: Path) -> str:
    current_output = output_path_for(current_path, output_dir)
    current_dir = current_output.parent

    absolute_pattern = re.compile(r"\((https://docs\.stripe\.com(?P<path>/api(?:/[^)#?\s]*)?)\.md(?P<anchor>#[^)]+)?)\)")
    autolink_pattern = re.compile(r"<https://docs\.stripe\.com(?P<path>/api(?:/[^>#?\s]*)?)\.md(?P<anchor>#[^>]+)?>")

    def to_relative(api_path: str, anchor: str | None) -> str | None:
        normalized = normalize_api_path(api_path)
        if not normalized or normalized not in known_paths:
            return None
        target = output_path_for(normalized, output_dir)
        relative = os.path.relpath(target, current_dir).replace(os.sep, "/")
        return f"{relative}{anchor or ''}"

    def replace_absolute(match: re.Match[str]) -> str:
        rewritten = to_relative(match.group("path"), match.group("anchor"))
        if not rewritten:
            return match.group(0)
        return f"({rewritten})"

    def replace_autolink(match: re.Match[str]) -> str:
        rewritten = to_relative(match.group("path"), match.group("anchor"))
        if not rewritten:
            return match.group(0)
        return f"<{rewritten}>"

    content = absolute_pattern.sub(replace_absolute, content)
    content = autolink_pattern.sub(replace_autolink, content)
    return content


def extract_internal_api_paths_from_markdown(content: str) -> set[str]:
    matches = set(
        re.findall(
            r"https://docs\.stripe\.com(?P<path>/api(?:/[^)#>\s]*)?)\.md(?:#[^) >\s]+)?",
            content,
        )
    )
    normalized = {normalize_api_path(match) for match in matches}
    return {path for path in normalized if path}


@dataclass(slots=True)
class SyncResult:
    api_path: str
    output_path: Path
    url: str
    error: str | None = None
    missing: bool = False

    @property
    def ok(self) -> bool:
        return self.error is None and not self.missing


def sync_one(
    api_path: str,
    output_dir: Path,
    known_paths: set[str],
    timeout: float,
    retries: int,
    retry_delay: float,
) -> SyncResult:
    url = markdown_url_for(api_path)
    destination = output_path_for(api_path, output_dir)
    try:
        content = fetch_text(url, timeout=timeout, retries=retries, retry_delay=retry_delay)
        content = rewrite_internal_links(content, api_path, known_paths, output_dir)
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(content, encoding="utf-8")
        return SyncResult(api_path=api_path, output_path=destination, url=url)
    except HTTPError as exc:
        if exc.code in {404, 410}:
            return SyncResult(
                api_path=api_path,
                output_path=destination,
                url=url,
                error=f"HTTP Error {exc.code}: Not Found",
                missing=True,
            )
        return SyncResult(api_path=api_path, output_path=destination, url=url, error=str(exc))
    except Exception as exc:  # noqa: BLE001
        return SyncResult(api_path=api_path, output_path=destination, url=url, error=str(exc))


def discover_api_paths(timeout: float, retries: int, retry_delay: float) -> list[str]:
    html = fetch_text(API_INDEX_URL, timeout=timeout, retries=retries, retry_delay=retry_delay)
    state = extract_initial_state(html)
    navigation = state.get("navigation", {}).get("products", [])
    paths = collect_api_paths(navigation)
    if not paths:
        raise ValueError("No /api paths were discovered in Stripe navigation")
    return sorted(paths)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Sync Stripe API Markdown docs into the local specs/stripe tree."
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
        default=16,
        help="Number of concurrent markdown downloads.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        help="Only sync the first N discovered API pages. Useful for smoke tests.",
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


def main() -> int:
    args = parse_args()
    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    paths = discover_api_paths(timeout=args.timeout, retries=args.retries, retry_delay=args.retry_delay)
    if args.limit is not None:
        paths = paths[: args.limit]

    known_paths = set(paths)
    print(f"Discovered {len(paths)} Stripe API Markdown page(s) from navigation", file=sys.stderr)

    pending = list(paths)
    synced_paths: set[str] = set()
    failures: list[SyncResult] = []
    missing: list[SyncResult] = []

    while pending:
        completed = 0
        synced_this_round: set[str] = set()
        missing_this_round: set[str] = set()

        with ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
            futures = {
                executor.submit(
                    sync_one,
                    api_path,
                    output_dir,
                    known_paths,
                    args.timeout,
                    args.retries,
                    args.retry_delay,
                ): api_path
                for api_path in pending
            }

            for future in as_completed(futures):
                result = future.result()
                completed += 1
                if result.ok:
                    synced_paths.add(result.api_path)
                    synced_this_round.add(result.api_path)
                    if args.verbose:
                        print(
                            f"[{completed}/{len(pending)}] wrote {result.output_path.relative_to(output_dir)}",
                            file=sys.stderr,
                        )
                    elif completed % 50 == 0 or completed == len(pending):
                        print(f"[{completed}/{len(pending)}] synced", file=sys.stderr)
                elif result.missing:
                    missing.append(result)
                    missing_this_round.add(result.api_path)
                    print(
                        f"[{completed}/{len(pending)}] skipped unavailable {result.api_path}",
                        file=sys.stderr,
                    )
                else:
                    failures.append(result)
                    print(
                        f"[{completed}/{len(pending)}] failed {result.api_path}: {result.error}",
                        file=sys.stderr,
                    )

        if failures:
            print("", file=sys.stderr)
            print(f"{len(failures)} download(s) failed:", file=sys.stderr)
            for failure in failures:
                print(f"- {failure.api_path} -> {failure.error}", file=sys.stderr)
            return 1

        if missing_this_round:
            known_paths.difference_update(missing_this_round)

        if args.limit is not None:
            break

        discovered_from_content: set[str] = set()
        for api_path in synced_this_round:
            content = output_path_for(api_path, output_dir).read_text(encoding="utf-8")
            discovered_from_content.update(extract_internal_api_paths_from_markdown(content))

        extra_paths = sorted(discovered_from_content - known_paths)
        if not extra_paths:
            break

        known_paths.update(extra_paths)
        pending = extra_paths
        print(
            f"Discovered {len(extra_paths)} additional API Markdown page(s) from internal links",
            file=sys.stderr,
        )
    else:
        pending = []

    for api_path in sorted(synced_paths):
        destination = output_path_for(api_path, output_dir)
        content = destination.read_text(encoding="utf-8")
        rewritten = rewrite_internal_links(content, api_path, known_paths, output_dir)
        if rewritten != content:
            destination.write_text(rewritten, encoding="utf-8")

    if missing:
        print(f"Skipped {len(missing)} unavailable page(s):", file=sys.stderr)
        for result in missing:
            print(f"- {result.api_path}", file=sys.stderr)

    print("Sync complete", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

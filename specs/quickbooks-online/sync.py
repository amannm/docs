#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = ["beautifulsoup4", "html5lib"]
# ///
from __future__ import annotations

import argparse
import gzip
import html
import json
import os
import re
import sys
import time
from pathlib import Path
from typing import Any, Iterable
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup, NavigableString, Tag


BASE_DOCS_URL = "https://developer.intuit.com/app/developer/qbo/docs/api"
STATIC_BASE_URL = "https://static.developer.intuit.com/JSONObjects"
DOC_ROUTE_PREFIX = "/app/developer/qbo/docs/api/"
REQUEST_HEADERS = {
    "User-Agent": "QuickBooksOnlineDocSync/1.0 (+https://developer.intuit.com/app/developer/qbo/docs/api)",
    "Accept-Encoding": "gzip",
}

BLOCK_TAGS = {
    "article",
    "aside",
    "blockquote",
    "details",
    "div",
    "dl",
    "figure",
    "footer",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
    "header",
    "hr",
    "li",
    "main",
    "nav",
    "ol",
    "p",
    "section",
    "table",
    "tbody",
    "td",
    "th",
    "thead",
    "tr",
    "ul",
}

KNOWN_HTML_TAGS = {
    "a",
    "article",
    "aside",
    "b",
    "blockquote",
    "br",
    "code",
    "dd",
    "details",
    "div",
    "dl",
    "dt",
    "em",
    "figure",
    "footer",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
    "header",
    "hr",
    "i",
    "kbd",
    "li",
    "main",
    "nav",
    "ol",
    "p",
    "pre",
    "section",
    "span",
    "strong",
    "sub",
    "sup",
    "table",
    "tbody",
    "td",
    "th",
    "thead",
    "tr",
    "ul",
}

HEADING_LEVEL_BY_DEPTH = {
    0: "#",
    1: "##",
    2: "###",
    3: "####",
    4: "#####",
    5: "######",
}


def fetch_bytes(url: str, timeout: float, retries: int, retry_delay: float) -> bytes:
    last_error: Exception | None = None
    for attempt in range(1, retries + 1):
        request = Request(url, headers=REQUEST_HEADERS)
        try:
            with urlopen(request, timeout=timeout) as response:
                payload = response.read()
                if response.headers.get("Content-Encoding") == "gzip" or payload[:2] == b"\x1f\x8b":
                    payload = gzip.decompress(payload)
                return payload
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


def fetch_json(url: str, timeout: float, retries: int, retry_delay: float) -> Any:
    return json.loads(fetch_bytes(url, timeout=timeout, retries=retries, retry_delay=retry_delay))


def fetch_text(url: str, timeout: float, retries: int, retry_delay: float) -> str:
    return fetch_bytes(url, timeout=timeout, retries=retries, retry_delay=retry_delay).decode("utf-8", errors="replace")


def normalize_lookup_key(name: str | None) -> list[str]:
    if not name:
        return []

    candidates = [name]
    lower = name.lower()
    title_lower = name[:1].upper() + name[1:].lower()
    if lower not in candidates:
        candidates.append(lower)
    if title_lower not in candidates:
        candidates.append(title_lower)
    return candidates


def resolve_mapping_key(mapping: dict[str, Any], name: str | None) -> str | None:
    for candidate in normalize_lookup_key(name):
        if candidate in mapping:
            return candidate
    return None


def normalize_heading_text(value: str) -> str:
    value = value.replace("-", " ").replace("_", " ").strip()
    if not value:
        return value
    if value.lower() == value:
        return value.title()
    return value


def markdown_heading(level: int, title: str) -> str:
    return f"{HEADING_LEVEL_BY_DEPTH[min(level, max(HEADING_LEVEL_BY_DEPTH))]} {title}"


def leaf_output_path(route: tuple[str, ...], output_dir: Path) -> Path:
    if not route:
        return output_dir / "index.md"
    return output_dir.joinpath(*route[:-1], f"{route[-1]}.md")


def index_output_path(route: tuple[str, ...], output_dir: Path) -> Path:
    if not route:
        return output_dir / "index.md"
    return output_dir.joinpath(*route, "index.md")


def docs_url_for(route: tuple[str, ...]) -> str:
    if not route:
        return BASE_DOCS_URL
    return f"{BASE_DOCS_URL}/{'/'.join(route)}"


def relative_link(from_path: Path, to_path: Path) -> str:
    relative = os.path.relpath(to_path, from_path.parent)
    return relative.replace(os.sep, "/")


def format_breadcrumbs(
    route: tuple[str, ...],
    current_output: Path,
    route_lookup: dict[tuple[str, ...], Path],
    title_lookup: dict[tuple[str, ...], str],
) -> str:
    parts = [f"[QuickBooks Online API]({relative_link(current_output, route_lookup[()])})"]
    for depth in range(1, len(route)):
        prefix = route[:depth]
        target = route_lookup.get(prefix)
        label = title_lookup[prefix]
        if target is None:
            parts.append(label)
        else:
            parts.append(f"[{label}]({relative_link(current_output, target)})")
    parts.append(title_lookup[route])
    return " / ".join(parts)


def collect_leaf_pages(node: dict[str, Any], prefix: tuple[str, ...] = ()) -> list[tuple[tuple[str, ...], str]]:
    pages: list[tuple[tuple[str, ...], str]] = []
    for slug, child in node.get("childAttributes", {}).items():
        route = prefix + (slug,)
        if isinstance(child, dict) and child.get("childAttributes"):
            pages.extend(collect_leaf_pages(child, route))
        else:
            pages.append((route, str(child)))
    return pages


def collect_index_nodes(node: dict[str, Any], prefix: tuple[str, ...] = ()) -> list[tuple[tuple[str, ...], dict[str, Any]]]:
    nodes = [(prefix, node)]
    for slug, child in node.get("childAttributes", {}).items():
        if isinstance(child, dict) and child.get("childAttributes"):
            nodes.extend(collect_index_nodes(child, prefix + (slug,)))
    return nodes


def build_title_lookup(root: dict[str, Any]) -> dict[tuple[str, ...], str]:
    titles: dict[tuple[str, ...], str] = {(): "QuickBooks Online API"}

    def walk(node: dict[str, Any], prefix: tuple[str, ...]) -> None:
        for slug, child in node.get("childAttributes", {}).items():
            route = prefix + (slug,)
            if isinstance(child, dict) and child.get("childAttributes"):
                raw_name = str(child.get("name") or slug)
                titles[route] = normalize_heading_text(raw_name)
                walk(child, route)
            else:
                titles[route] = str(child).strip()

    walk(root, ())
    return titles


def escape_table_cell(text: str) -> str:
    return text.replace("|", r"\|").replace("\n", "<br>").strip()


def clean_markdown(text: str) -> str:
    lines = [line.rstrip() for line in text.splitlines()]
    cleaned: list[str] = []
    blank_run = 0
    for line in lines:
        if not line.strip():
            blank_run += 1
            if blank_run <= 1:
                cleaned.append("")
            continue
        blank_run = 0
        cleaned.append(line)
    return "\n".join(cleaned).strip() + "\n"


def preprocess_fragment(fragment: str) -> str:
    fragment = fragment.replace("\r\n", "\n")
    fragment = fragment.replace("\xa0", " ")
    fragment = fragment.replace('\\"', '"')
    fragment = fragment.replace("<./li>", "</li>")
    fragment = re.sub(
        r"</?([A-Za-z][A-Za-z0-9:-]*)(\s+[^<>]*?)?\s*/?>",
        escape_unknown_tag_like_markup,
        fragment,
    )
    return fragment.strip()


def escape_unknown_tag_like_markup(match: re.Match[str]) -> str:
    raw = match.group(0)
    tag_name = match.group(1).lower()
    if tag_name in KNOWN_HTML_TAGS:
        return raw
    return f"<code>{html.escape(raw)}</code>"


def normalize_inline_text(text: str) -> str:
    text = html.unescape(text.replace("\xa0", " "))
    text = re.sub(r"\s+", " ", text)
    return text


def has_block_children(tag: Tag) -> bool:
    return any(isinstance(child, Tag) and child.name in BLOCK_TAGS for child in tag.children)


def rewrite_href(
    href: str | None,
    current_output: Path,
    route_lookup: dict[tuple[str, ...], Path],
) -> str | None:
    if not href:
        return href

    parsed = urlparse(href)
    if parsed.scheme and parsed.netloc and parsed.netloc != "developer.intuit.com":
        return href

    path = parsed.path or ""
    if not path:
        return href

    if path.rstrip("/") == DOC_ROUTE_PREFIX.rstrip("/"):
        target = route_lookup[()]
        rewritten = relative_link(current_output, target)
    elif path.startswith(DOC_ROUTE_PREFIX):
        relative = tuple(part for part in path.removeprefix(DOC_ROUTE_PREFIX).split("/") if part)
        target = route_lookup.get(relative)
        if target is None:
            return href
        rewritten = relative_link(current_output, target)
    else:
        return href

    if parsed.fragment:
        return f"{rewritten}#{parsed.fragment}"
    return rewritten


def render_inline(
    node: Any,
    current_output: Path,
    route_lookup: dict[tuple[str, ...], Path],
    preserve_breaks: bool = False,
) -> str:
    if isinstance(node, NavigableString):
        return normalize_inline_text(str(node))

    if not isinstance(node, Tag):
        return ""

    if node.name == "br":
        return "<br>" if preserve_breaks else "\n"

    if node.name in {"span", "code"} and "literal" in node.get("class", []):
        content = render_inline_children(node, current_output, route_lookup, preserve_breaks=preserve_breaks).strip()
        return f"`{content}`" if content else ""

    if node.name in {"code", "kbd"}:
        content = render_inline_children(node, current_output, route_lookup, preserve_breaks=preserve_breaks).strip()
        return f"`{content}`" if content else ""

    if node.name in {"strong", "b"}:
        content = render_inline_children(node, current_output, route_lookup, preserve_breaks=preserve_breaks).strip()
        return f"**{content}**" if content else ""

    if node.name in {"em", "i"}:
        content = render_inline_children(node, current_output, route_lookup, preserve_breaks=preserve_breaks).strip()
        return f"*{content}*" if content else ""

    if node.name == "a":
        label = render_inline_children(node, current_output, route_lookup, preserve_breaks=preserve_breaks).strip()
        href = rewrite_href(node.get("href"), current_output, route_lookup)
        if not href:
            return label
        return f"[{label or href}]({href})"

    if node.name in {"p", "div", "li", "ul", "ol"} and not preserve_breaks:
        return render_inline_children(node, current_output, route_lookup, preserve_breaks=preserve_breaks)

    return render_inline_children(node, current_output, route_lookup, preserve_breaks=preserve_breaks)


def render_inline_children(
    node: Tag,
    current_output: Path,
    route_lookup: dict[tuple[str, ...], Path],
    preserve_breaks: bool = False,
) -> str:
    pieces = [render_inline(child, current_output, route_lookup, preserve_breaks=preserve_breaks) for child in node.children]
    text = "".join(pieces)
    if preserve_breaks:
        text = re.sub(r"[ \t]+\n", "\n", text)
        text = re.sub(r"\n[ \t]+", "\n", text)
    else:
        text = re.sub(r"\s+\n", "\n", text)
        text = re.sub(r"\n\s+", "\n", text)
    return text.strip()


def render_html_table(
    table: Tag,
    current_output: Path,
    route_lookup: dict[tuple[str, ...], Path],
) -> list[str]:
    rows: list[list[str]] = []
    for tr in table.find_all("tr"):
        cells = tr.find_all(["th", "td"])
        if not cells:
            continue
        rows.append(
            [
                escape_table_cell(render_inline_children(cell, current_output, route_lookup, preserve_breaks=True))
                for cell in cells
            ]
        )

    if not rows:
        return []

    header = rows[0]
    data_rows = rows[1:] or [[]]
    lines = [
        f"| {' | '.join(header)} |",
        f"| {' | '.join(['---'] * len(header))} |",
    ]
    for row in data_rows:
        padded = row + [""] * (len(header) - len(row))
        lines.append(f"| {' | '.join(padded[: len(header)])} |")
    lines.append("")
    return lines


def render_attribute_group(
    group: Tag,
    current_output: Path,
    route_lookup: dict[tuple[str, ...], Path],
) -> list[str]:
    sections: list[tuple[str | None, list[tuple[str, str]]]] = []
    current_title: str | None = None
    current_rows: list[tuple[str, str]] = []

    def flush() -> None:
        nonlocal current_rows
        if current_rows:
            sections.append((current_title, current_rows))
            current_rows = []

    for child in group.children:
        if not isinstance(child, Tag):
            continue
        classes = child.get("class", [])
        if child.name == "div" and "attributes-list-table-title" in classes:
            flush()
            current_title = render_inline_children(child, current_output, route_lookup)
            continue
        if child.name == "li" and "attribute-list-item" in classes:
            name_tag = child.select_one(".attribute-name")
            description_tag = child.select_one(".attribute-description") or child.select_one(".attribute-info")
            name = render_inline_children(name_tag or child, current_output, route_lookup, preserve_breaks=True)
            description = render_inline_children(description_tag or child, current_output, route_lookup, preserve_breaks=True)
            current_rows.append((name, description))
    flush()

    lines: list[str] = []
    for title, rows in sections:
        if title:
            lines.append(f"#### {title}")
            lines.append("")
        lines.append("| Name | Description |")
        lines.append("| --- | --- |")
        for name, description in rows:
            lines.append(f"| {escape_table_cell(name)} | {escape_table_cell(description)} |")
        lines.append("")
    return lines


def render_block(
    node: Any,
    current_output: Path,
    route_lookup: dict[tuple[str, ...], Path],
    list_depth: int = 0,
) -> list[str]:
    if isinstance(node, NavigableString):
        text = normalize_inline_text(str(node))
        return [text, ""] if text else []

    if not isinstance(node, Tag):
        return []

    if node.name in {"script", "style"}:
        return []

    if "attributes-list-group" in node.get("class", []):
        return render_attribute_group(node, current_output, route_lookup)

    if node.name in {"p"}:
        text = render_inline_children(node, current_output, route_lookup)
        return [text, ""] if text else []

    if node.name in {"h1", "h2", "h3", "h4", "h5", "h6"}:
        level = int(node.name[1])
        text = render_inline_children(node, current_output, route_lookup)
        return [markdown_heading(level - 1, text), ""] if text else []

    if node.name in {"ul", "ol"}:
        lines: list[str] = []
        ordered = node.name == "ol"
        item_number = 1
        for item in node.find_all("li", recursive=False):
            prefix = f"{item_number}. " if ordered else "- "
            inline_parts: list[str] = []
            nested_lines: list[str] = []
            for child in item.children:
                if isinstance(child, Tag) and child.name in {"ul", "ol"}:
                    nested_lines.extend(render_block(child, current_output, route_lookup, list_depth + 1))
                    continue
                if isinstance(child, Tag) and child.name in BLOCK_TAGS and child.name not in {"span", "strong", "em", "a", "code", "br"}:
                    nested_lines.extend(render_block(child, current_output, route_lookup, list_depth + 1))
                    continue
                inline_parts.append(render_inline(child, current_output, route_lookup))

            text = re.sub(r"\s+", " ", "".join(inline_parts)).strip()
            if text:
                lines.append(f"{'  ' * list_depth}{prefix}{text}")
            elif nested_lines:
                lines.append(f"{'  ' * list_depth}{prefix}".rstrip())

            for nested in nested_lines:
                if not nested:
                    lines.append("")
                else:
                    lines.append(f"{'  ' * (list_depth + 1)}{nested}")

            item_number += 1
        lines.append("")
        return lines

    if node.name == "table":
        return render_html_table(node, current_output, route_lookup)

    if node.name == "div" and "attributes-list-table-title" in node.get("class", []):
        title = render_inline_children(node, current_output, route_lookup)
        return [f"#### {title}", ""] if title else []

    if has_block_children(node):
        lines: list[str] = []
        for child in node.children:
            lines.extend(render_block(child, current_output, route_lookup, list_depth=list_depth))
        return lines

    text = render_inline_children(node, current_output, route_lookup)
    return [text, ""] if text else []


def render_html_fragment(
    fragment: str | None,
    current_output: Path,
    route_lookup: dict[tuple[str, ...], Path],
) -> str:
    if not fragment:
        return ""

    prepared = preprocess_fragment(fragment)
    if not prepared:
        return ""

    soup = BeautifulSoup(f"<div>{prepared}</div>", "html5lib")
    root = soup.body.div
    lines: list[str] = []
    inline_buffer: list[Any] = []

    def flush_inline_buffer() -> None:
        nonlocal inline_buffer
        if not inline_buffer:
            return
        text = "".join(render_inline(node, current_output, route_lookup) for node in inline_buffer).strip()
        inline_buffer = []
        if text:
            lines.append(text)
            lines.append("")

    for child in root.children:
        if isinstance(child, NavigableString) or (isinstance(child, Tag) and child.name not in BLOCK_TAGS):
            inline_buffer.append(child)
            continue

        flush_inline_buffer()
        lines.extend(render_block(child, current_output, route_lookup))

    flush_inline_buffer()
    return clean_markdown("\n".join(lines)).strip()


def ordered_model_properties(model: dict[str, Any]) -> list[tuple[str, dict[str, Any]]]:
    properties = model.get("properties", {})
    if not isinstance(properties, dict):
        return []

    ordered_names: list[str] = []
    for key in ("ShowFirst", "Required", "RequiredForUpdate", "ConditionallyRequired", "Default", "Optional"):
        for name in model.get(key, []):
            if name in properties and name not in ordered_names:
                ordered_names.append(name)

    for name in properties:
        if name not in ordered_names:
            ordered_names.append(name)

    return [(name, properties[name]) for name in ordered_names]


def extract_refs(property_data: dict[str, Any]) -> list[str]:
    refs = property_data.get("$ref")
    if isinstance(refs, str):
        return [refs]
    if isinstance(refs, list):
        extracted: list[str] = []
        for item in refs:
            if isinstance(item, dict):
                extracted.extend(str(value) for value in item.values())
        return extracted
    return []


def format_property_metadata(property_data: dict[str, Any]) -> list[str]:
    lines: list[str] = []
    required_flag = property_data.get("requiredFlag")
    if required_flag:
        lines.append(f"Required: {required_flag}")

    property_type = property_data.get("type")
    if property_type:
        lines.append(f"Type: `{property_type}`")

    traits: list[str] = []
    if property_data.get("readOnly"):
        traits.append("read only")
    if property_data.get("systemDefined"):
        traits.append("system defined")
    if property_data.get("filterable"):
        traits.append("filterable")
    if property_data.get("sortable"):
        traits.append("sortable")
    if property_data.get("deprecated"):
        traits.append("deprecated")
    if traits:
        lines.append(f"Traits: {', '.join(traits)}")

    if property_data.get("maxLen"):
        lines.append(f"Max length: {property_data['maxLen']}")
    if property_data.get("default"):
        lines.append(f"Default: {property_data['default']}")
    if property_data.get("minorVersion"):
        lines.append(f"Minor version: {property_data['minorVersion']}")
    if property_data.get("locales"):
        lines.append(f"Locales: {', '.join(property_data['locales'])}")

    return lines


def render_auxiliary_sections(
    auxiliary_refs: dict[str, Any] | None,
    current_output: Path,
    route_lookup: dict[tuple[str, ...], Path],
    auxiliary_cache: dict[str, str],
    timeout: float,
    retries: int,
    retry_delay: float,
) -> list[str]:
    lines: list[str] = []
    if not auxiliary_refs:
        return lines

    for name, labels in auxiliary_refs.items():
        if name not in auxiliary_cache:
            url = f"{STATIC_BASE_URL}/{name}.html"
            auxiliary_cache[name] = fetch_text(url, timeout=timeout, retries=retries, retry_delay=retry_delay)
        rendered = render_html_fragment(auxiliary_cache[name], current_output, route_lookup)
        if not rendered:
            continue

        summary = name
        if isinstance(labels, list) and labels:
            summary = str(labels[0]).strip()
        elif isinstance(labels, str):
            summary = labels.strip()

        lines.append("<details>")
        lines.append(f"<summary>{summary}</summary>")
        lines.append("")
        lines.extend(rendered.splitlines())
        lines.append("")
        lines.append("</details>")
        lines.append("")

    return lines


def render_model(
    model_ref: str,
    models: dict[str, Any],
    current_output: Path,
    route_lookup: dict[tuple[str, ...], Path],
    auxiliary_cache: dict[str, str],
    timeout: float,
    retries: int,
    retry_delay: float,
    heading_level: int,
    seen: set[str] | None = None,
    title_override: str | None = None,
) -> list[str]:
    seen = set() if seen is None else set(seen)
    model_key = resolve_mapping_key(models, model_ref)
    if model_key is None:
        return [f"_Unresolved model reference: `{model_ref}`._", ""]

    if model_key in seen:
        return [f"_Circular model reference to `{model_key}` omitted._", ""]

    seen.add(model_key)
    model = models[model_key]
    title = title_override or model_key
    lines = [markdown_heading(heading_level, title), ""]

    model_type = model.get("type")
    if model_type:
        lines.append(f"Model type: `{model_type}`")
        lines.append("")

    properties = ordered_model_properties(model)
    if not properties:
        lines.append("_No documented properties._")
        lines.append("")
        return lines

    for property_name, property_data in properties:
        lines.append(markdown_heading(heading_level + 1, f"`{property_name}`"))
        lines.append("")
        metadata_lines = format_property_metadata(property_data)
        lines.extend(metadata_lines)
        if metadata_lines:
            lines.append("")

        description = render_html_fragment(property_data.get("description"), current_output, route_lookup)
        if description:
            lines.extend(description.splitlines())
            lines.append("")

        lines.extend(
            render_auxiliary_sections(
                property_data.get("table"),
                current_output,
                route_lookup,
                auxiliary_cache,
                timeout=timeout,
                retries=retries,
                retry_delay=retry_delay,
            )
        )

        refs = extract_refs(property_data)
        if refs:
            lines.append("<details>")
            lines.append(f"<summary>Child attributes for `{property_name}`</summary>")
            lines.append("")
            for ref in refs:
                lines.extend(
                    render_model(
                        ref,
                        models=models,
                        current_output=current_output,
                        route_lookup=route_lookup,
                        auxiliary_cache=auxiliary_cache,
                        timeout=timeout,
                        retries=retries,
                        retry_delay=retry_delay,
                        heading_level=min(heading_level + 2, 5),
                        seen=seen,
                    )
                )
            lines.append("</details>")
            lines.append("")

    return lines


def code_language(text: str) -> str:
    stripped = text.lstrip("\ufeff").strip()
    bare = stripped[1:-1].strip() if stripped.startswith('"') and stripped.endswith('"') else stripped
    lowered = bare.lower()
    if stripped.startswith("{") or stripped.startswith("["):
        return "json"
    if stripped.startswith("<") and not stripped.startswith("<!doctype"):
        return "xml"
    if lowered.startswith("select "):
        return "sql"
    if stripped.startswith("%PDF-"):
        return "text"
    return "text"


def is_binary_like(text: str) -> bool:
    if text.startswith("%PDF-"):
        return True
    control_count = sum(1 for char in text if ord(char) < 32 and char not in "\n\r\t")
    return control_count > 0


def render_code_examples(
    code_bundle: dict[str, str] | None,
    code_name: str | None,
) -> list[str]:
    if not code_bundle or not code_name:
        return []

    lines: list[str] = []
    for label, suffix in (("Example", ""), ("XML example", "-xml")):
        content = code_bundle.get(f"{code_name}{suffix}")
        if not content:
            continue
        content = content.lstrip("\ufeff")
        lines.append(f"#### {label}")
        lines.append("")
        if is_binary_like(content):
            lines.append("_Binary response body omitted in the source payload._")
            lines.append("")
            continue
        lines.append(f"```{code_language(content)}")
        lines.extend(content.rstrip().splitlines())
        lines.append("```")
        lines.append("")

    return lines


def render_titled_fragment(
    value: Any,
    current_output: Path,
    route_lookup: dict[tuple[str, ...], Path],
    heading_level: int = 2,
) -> list[str]:
    if value is None:
        return []

    if isinstance(value, str):
        rendered = render_html_fragment(value, current_output, route_lookup)
        return rendered.splitlines() + [""] if rendered else []

    if isinstance(value, dict):
        heading = str(value.get("heading") or "").strip()
        description = render_html_fragment(value.get("description"), current_output, route_lookup)
        lines: list[str] = []
        if heading:
            lines.append(markdown_heading(heading_level, heading))
            lines.append("")
        if description:
            lines.extend(description.splitlines())
            lines.append("")
        return lines

    return []


def render_definition(definition: dict[str, Any] | None) -> list[str]:
    if not definition:
        return []

    lines = ["### Definition", ""]
    for key, value in definition.items():
        lines.append(f"- **{key}:** `{value}`")
    lines.append("")
    return lines


def render_operation_section(
    operation: dict[str, Any],
    top_level_model_key: str | None,
    code_bundle: dict[str, str] | None,
    models: dict[str, Any],
    current_output: Path,
    route_lookup: dict[tuple[str, ...], Path],
    auxiliary_cache: dict[str, str],
    timeout: float,
    retries: int,
    retry_delay: float,
) -> list[str]:
    title = str(operation.get("name") or "Operation").strip()
    lines = [f"## {title}", ""]

    lines.extend(render_definition(operation.get("definition")))

    description = render_html_fragment(operation.get("description"), current_output, route_lookup)
    if description:
        lines.extend(description.splitlines())
        lines.append("")

    for section in operation.get("sections", []):
        section_name = str(section.get("name") or "Section").strip()
        lines.append(f"### {section_name}")
        lines.append("")

        section_description = render_html_fragment(section.get("description"), current_output, route_lookup)
        if section_description:
            lines.extend(section_description.splitlines())
            lines.append("")

        section_model_ref = section.get("model", {}).get("$ref") if isinstance(section.get("model"), dict) else None
        section_model_key = resolve_mapping_key(models, section_model_ref) if section_model_ref else None
        if section_model_ref:
            lines.append(f"Schema: `{section_model_key or section_model_ref}`")
            lines.append("")
            if section_model_key == top_level_model_key:
                lines.append("_Matches the top-level sample object schema._")
                lines.append("")
            else:
                lines.append("<details>")
                lines.append(f"<summary>Show schema for `{section_model_key or section_model_ref}`</summary>")
                lines.append("")
                lines.extend(
                    render_model(
                        section_model_ref,
                        models=models,
                        current_output=current_output,
                        route_lookup=route_lookup,
                        auxiliary_cache=auxiliary_cache,
                        timeout=timeout,
                        retries=retries,
                        retry_delay=retry_delay,
                        heading_level=3,
                    )
                )
                lines.append("</details>")
                lines.append("")

        lines.extend(render_code_examples(code_bundle, section.get("code")))

    return lines


def render_leaf_page(
    route: tuple[str, ...],
    entity_name: str,
    entity: dict[str, Any],
    code_bundle: dict[str, str] | None,
    models: dict[str, Any],
    route_lookup: dict[tuple[str, ...], Path],
    title_lookup: dict[tuple[str, ...], str],
    auxiliary_cache: dict[str, str],
    timeout: float,
    retries: int,
    retry_delay: float,
    output_dir: Path,
) -> str:
    output_path = leaf_output_path(route, output_dir)
    title = title_lookup[route]
    top_model_ref = entity.get("model", {}).get("$ref") if isinstance(entity.get("model"), dict) else None
    top_model_key = resolve_mapping_key(models, top_model_ref) if top_model_ref else None

    lines = [
        f"# {title}",
        "",
        f"> Source: {docs_url_for(route)}",
        f"> Breadcrumbs: {format_breadcrumbs(route, output_path, route_lookup, title_lookup)}",
        f"> Canonical entity: `{entity_name}`",
        "",
    ]

    description = render_html_fragment(entity.get("description"), output_path, route_lookup)
    if description:
        lines.extend(description.splitlines())
        lines.append("")

    lines.extend(render_titled_fragment(entity.get("optional-description"), output_path, route_lookup))

    lines.extend(
        render_auxiliary_sections(
            entity.get("table"),
            output_path,
            route_lookup,
            auxiliary_cache,
            timeout=timeout,
            retries=retries,
            retry_delay=retry_delay,
        )
    )

    model_header = str(entity.get("model-header") or "").strip()
    if top_model_ref and top_model_key:
        lines.append(f"## {model_header or 'Sample object'}")
        lines.append("")
        model_description = render_html_fragment(entity.get("model-description"), output_path, route_lookup)
        if model_description:
            lines.extend(model_description.splitlines())
            lines.append("")

        lines.extend(
            render_model(
                top_model_ref,
                models=models,
                current_output=output_path,
                route_lookup=route_lookup,
                auxiliary_cache=auxiliary_cache,
                timeout=timeout,
                retries=retries,
                retry_delay=retry_delay,
                heading_level=2,
            )
        )

        lines.extend(render_code_examples(code_bundle, entity.get("code")))

    operations = entity.get("operations", {})
    for operation_group in operations.values():
        for operation in operation_group:
            lines.extend(
                render_operation_section(
                    operation,
                    top_level_model_key=top_model_key,
                    code_bundle=code_bundle,
                    models=models,
                    current_output=output_path,
                    route_lookup=route_lookup,
                    auxiliary_cache=auxiliary_cache,
                    timeout=timeout,
                    retries=retries,
                    retry_delay=retry_delay,
                )
            )

    return clean_markdown("\n".join(lines))


def render_index_page(
    route: tuple[str, ...],
    node: dict[str, Any],
    route_lookup: dict[tuple[str, ...], Path],
    title_lookup: dict[tuple[str, ...], str],
    output_dir: Path,
) -> str:
    output_path = index_output_path(route, output_dir)
    title = title_lookup[route]

    lines = [f"# {title}", ""]
    if route:
        lines.extend(
            [
                f"> Source: {docs_url_for(route)}",
                f"> Breadcrumbs: {format_breadcrumbs(route, output_path, route_lookup, title_lookup)}",
                "",
            ]
        )
    else:
        lines.extend(
            [
                f"> Source: {BASE_DOCS_URL}",
                "",
            ]
        )

    if route == ():
        lines.append("Generated from the official QuickBooks Online API docs JSON assets used by the public documentation site.")
        lines.append("")

    for slug, child in node.get("childAttributes", {}).items():
        child_route = route + (slug,)
        if child_route not in route_lookup:
            continue
        if isinstance(child, dict) and child.get("childAttributes"):
            label = title_lookup[child_route]
            target = route_lookup[child_route]
        else:
            label = title_lookup[child_route]
            target = route_lookup[child_route]
        lines.append(f"- [{label}]({relative_link(output_path, target)})")

    lines.append("")
    return clean_markdown("\n".join(lines))


def safe_write(path: Path, content: str, verbose: bool) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    if verbose:
        print(path)


def remove_stale_markdown(output_dir: Path, keep: set[Path]) -> None:
    for path in output_dir.rglob("*.md"):
        if path in keep:
            continue
        if path.name == "TODO.md":
            continue
        path.unlink()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Sync the QuickBooks Online API docs into Markdown under specs/quickbooks-online."
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).resolve().parent,
        help="Directory that receives the generated Markdown files.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        help="Only render the first N leaf routes. Useful for smoke tests.",
    )
    parser.add_argument(
        "--route",
        action="append",
        help="Render only the specified route, for example accounting/all-entities/account.",
    )
    parser.add_argument(
        "--clean",
        action="store_true",
        help="Delete previously generated Markdown files that are not written during this run.",
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
        help="Number of fetch attempts per resource.",
    )
    parser.add_argument(
        "--retry-delay",
        type=float,
        default=0.5,
        help="Base delay in seconds between retries.",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print each file path as it is written.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    toc = fetch_json(f"{STATIC_BASE_URL}/TocJsonObject_v1.json", args.timeout, args.retries, args.retry_delay)["qbo"]
    entities = fetch_json(f"{STATIC_BASE_URL}/EntityJsonObject_v1.json", args.timeout, args.retries, args.retry_delay)["entities"]["qbo"]
    codes_models = fetch_json(
        f"{STATIC_BASE_URL}/CodesModelsJsonObjects_v2.json",
        args.timeout,
        args.retries,
        args.retry_delay,
    )
    models = codes_models["models"]["qbo"]
    codes = codes_models["codes"]["qbo"]

    title_lookup = build_title_lookup(toc)
    leaves = collect_leaf_pages(toc)
    index_nodes = collect_index_nodes(toc)

    if args.route:
        wanted_routes = {tuple(route.strip("/").split("/")) for route in args.route}
        leaves = [(route, name) for route, name in leaves if route in wanted_routes]
        index_nodes = [(route, node) for route, node in index_nodes if route in {(), *{tuple(route[:depth]) for route in wanted_routes for depth in range(len(route))}}]

    if args.limit is not None:
        leaves = leaves[: args.limit]

    route_lookup: dict[tuple[str, ...], Path] = {(): index_output_path((), output_dir)}
    for route, _ in index_nodes:
        route_lookup[route] = index_output_path(route, output_dir)
    for route, _ in leaves:
        route_lookup[route] = leaf_output_path(route, output_dir)

    auxiliary_cache: dict[str, str] = {}
    written_paths: set[Path] = set()

    for route, node in index_nodes:
        content = render_index_page(
            route=route,
            node=node,
            route_lookup=route_lookup,
            title_lookup=title_lookup,
            output_dir=output_dir,
        )
        path = index_output_path(route, output_dir)
        safe_write(path, content, args.verbose)
        written_paths.add(path)

    for route, entity_name in leaves:
        entity = entities[entity_name]
        code_bundle_key = resolve_mapping_key(codes, entity_name)
        code_bundle = codes.get(code_bundle_key) if code_bundle_key else None
        content = render_leaf_page(
            route=route,
            entity_name=entity_name,
            entity=entity,
            code_bundle=code_bundle,
            models=models,
            route_lookup=route_lookup,
            title_lookup=title_lookup,
            auxiliary_cache=auxiliary_cache,
            timeout=args.timeout,
            retries=args.retries,
            retry_delay=args.retry_delay,
            output_dir=output_dir,
        )
        path = leaf_output_path(route, output_dir)
        safe_write(path, content, args.verbose)
        written_paths.add(path)

    if args.clean:
        remove_stale_markdown(output_dir, written_paths)

    print(f"Rendered {len(leaves)} leaf page(s) and {len(index_nodes)} index page(s).", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

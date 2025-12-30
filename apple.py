#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
import argparse
import json
import os
import re
import sys
import time
from urllib.parse import urlparse
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE_URL = "https://developer.apple.com/tutorials/data"

class LinkResolver:
    def __init__(self, known_paths=None, current_path=None):
        self.known_paths = known_paths or set()
        self.current_path = current_path

    def resolve(self, url):
        if not url:
            return url

        doc_path = None
        if url.startswith("/documentation/"):
            doc_path = url[len("/documentation/"):]
        elif url.startswith("https://developer.apple.com/documentation/"):
            doc_path = url[len("https://developer.apple.com/documentation/"):]

        if doc_path:
            clean_path = doc_path.split("?")[0].split("#")[0]
            if clean_path in self.known_paths:
                return self._relative_path(clean_path)

        if url.startswith("/"):
            return f"https://developer.apple.com{url}"
        return url

    def _relative_path(self, target_path):
        target_file = url_to_filepath(target_path)
        if not self.current_path:
            return target_file

        current_file = url_to_filepath(self.current_path)
        current_dir = os.path.dirname(current_file)

        if current_dir:
            rel = os.path.relpath(target_file, current_dir)
        else:
            rel = target_file

        return rel

def fetch_json(doc_path, language="objc"):
    url = f"{BASE_URL}/documentation/{doc_path}.json?language={language}"
    req = Request(url, headers={"User-Agent": "AppleDocFetcher/1.0"})
    try:
        with urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except HTTPError as e:
        print(f"HTTP Error {e.code}: {url}", file=sys.stderr)
        return None
    except URLError as e:
        print(f"URL Error: {e.reason}", file=sys.stderr)
        return None

def parse_doc_url(url):
    parsed = urlparse(url)
    path = parsed.path
    if path.startswith("/documentation/"):
        path = path[len("/documentation/"):]
    path = path.rstrip("/")
    params = dict(p.split("=") for p in parsed.query.split("&") if "=" in p)
    lang = params.get("language", "objc")
    return path, lang

def render_inline_content(items, refs, resolver=None):
    if resolver is None:
        resolver = LinkResolver()
    result = []
    for item in items:
        t = item.get("type", "")
        if t == "text":
            result.append(item.get("text", ""))
        elif t == "codeVoice":
            result.append(f"`{item.get('code', '')}`")
        elif t == "emphasis":
            inner = render_inline_content(item.get("inlineContent", []), refs, resolver)
            result.append(f"*{inner}*")
        elif t == "strong":
            inner = render_inline_content(item.get("inlineContent", []), refs, resolver)
            result.append(f"**{inner}**")
        elif t == "reference":
            ref_id = item.get("identifier", "")
            ref = refs.get(ref_id, {})
            title = ref.get("title", ref_id.split("/")[-1])
            ref_url = ref.get("url", "")
            ref_url = resolver.resolve(ref_url)
            if ref_url:
                result.append(f"[{title}]({ref_url})")
            else:
                result.append(title)
        elif t == "link":
            title = item.get("title", "")
            dest = item.get("destination", "")
            dest = resolver.resolve(dest)
            result.append(f"[{title}]({dest})")
        elif t == "inlineHead":
            inner = render_inline_content(item.get("inlineContent", []), refs, resolver)
            result.append(f"**{inner}**")
        elif t == "newTerm":
            inner = render_inline_content(item.get("inlineContent", []), refs, resolver)
            result.append(f"*{inner}*")
        elif t == "superscript":
            inner = render_inline_content(item.get("inlineContent", []), refs, resolver)
            result.append(f"^{inner}^")
        elif t == "subscript":
            inner = render_inline_content(item.get("inlineContent", []), refs, resolver)
            result.append(f"~{inner}~")
        elif t == "image":
            ident = item.get("identifier", "")
            ref = refs.get(ident, {})
            alt = ref.get("alt", "image")
            variants = ref.get("variants", [])
            img_url = variants[0].get("url", "") if variants else ""
            if img_url and not img_url.startswith("http"):
                img_url = f"https://developer.apple.com{img_url}"
            result.append(f"![{alt}]({img_url})")
        else:
            inner = item.get("inlineContent", [])
            if inner:
                result.append(render_inline_content(inner, refs, resolver))
    return "".join(result)

def render_content_block(block, refs, indent=0, resolver=None):
    if resolver is None:
        resolver = LinkResolver()
    lines = []
    prefix = "  " * indent
    t = block.get("type", "")

    if t == "paragraph":
        text = render_inline_content(block.get("inlineContent", []), refs, resolver)
        if text.strip():
            lines.append(f"{prefix}{text}")
            lines.append("")
    elif t == "heading":
        level = block.get("level", 2)
        anchor = block.get("anchor", "")
        text = render_inline_content(block.get("inlineContent", []), refs, resolver)
        if text.strip():
            hashes = "#" * level
            lines.append(f"{prefix}{hashes} {text}")
            lines.append("")
    elif t == "codeListing":
        lang = block.get("syntax", "")
        code_lines = block.get("code", [])
        lines.append(f"{prefix}```{lang}")
        for cl in code_lines:
            lines.append(f"{prefix}{cl}")
        lines.append(f"{prefix}```")
        lines.append("")
    elif t == "unorderedList":
        for item in block.get("items", []):
            content = item.get("content", [])
            for i, c in enumerate(content):
                if c.get("type") == "paragraph":
                    text = render_inline_content(c.get("inlineContent", []), refs, resolver)
                    if i == 0:
                        lines.append(f"{prefix}- {text}")
                    else:
                        lines.append(f"{prefix}  {text}")
                else:
                    sub = render_content_block(c, refs, indent + 1, resolver)
                    lines.append(sub)
        lines.append("")
    elif t == "orderedList":
        for idx, item in enumerate(block.get("items", []), 1):
            content = item.get("content", [])
            for i, c in enumerate(content):
                if c.get("type") == "paragraph":
                    text = render_inline_content(c.get("inlineContent", []), refs, resolver)
                    if i == 0:
                        lines.append(f"{prefix}{idx}. {text}")
                    else:
                        lines.append(f"{prefix}   {text}")
                else:
                    sub = render_content_block(c, refs, indent + 1, resolver)
                    lines.append(sub)
        lines.append("")
    elif t == "termList":
        for item in block.get("items", []):
            term = item.get("term", {})
            term_text = render_inline_content(term.get("inlineContent", []), refs, resolver)
            lines.append(f"{prefix}**{term_text}**")
            definition = item.get("definition", {})
            for c in definition.get("content", []):
                sub = render_content_block(c, refs, indent, resolver)
                lines.append(sub)
        lines.append("")
    elif t == "aside":
        style = block.get("style", "note")
        name = block.get("name", style.capitalize())
        lines.append(f"{prefix}> **{name}**")
        for c in block.get("content", []):
            sub = render_content_block(c, refs, indent, resolver)
            for sl in sub.split("\n"):
                if sl.strip():
                    lines.append(f"{prefix}> {sl}")
        lines.append("")
    elif t == "table":
        header = block.get("header", "row")
        rows = block.get("rows", [])
        if rows:
            first_row = rows[0]
            header_cells = []
            for cell in first_row:
                cell_content = []
                for c in cell:
                    if c.get("type") == "paragraph":
                        cell_content.append(render_inline_content(c.get("inlineContent", []), refs, resolver))
                header_cells.append(" ".join(cell_content))
            lines.append(f"{prefix}| " + " | ".join(header_cells) + " |")
            lines.append(f"{prefix}| " + " | ".join(["---"] * len(header_cells)) + " |")
            for row in rows[1:]:
                row_cells = []
                for cell in row:
                    cell_content = []
                    for c in cell:
                        if c.get("type") == "paragraph":
                            cell_content.append(render_inline_content(c.get("inlineContent", []), refs, resolver))
                    row_cells.append(" ".join(cell_content))
                lines.append(f"{prefix}| " + " | ".join(row_cells) + " |")
        lines.append("")
    else:
        content = block.get("content", [])
        if content:
            for c in content:
                sub = render_content_block(c, refs, indent, resolver)
                lines.append(sub)

    return "\n".join(lines)

def render_declaration(decl, refs):
    lines = []
    for d in decl.get("declarations", []):
        platforms = d.get("platforms", [])
        tokens = d.get("tokens", [])
        code_parts = []
        for tok in tokens:
            kind = tok.get("kind", "")
            text = tok.get("text", "")
            code_parts.append(text)
        code = "".join(code_parts)
        if platforms:
            lines.append(f"**Platforms:** {', '.join(platforms)}")
            lines.append("")
        lines.append("```objc")
        lines.append(code)
        lines.append("```")
        lines.append("")
    return "\n".join(lines)

def render_parameters(params_section, refs, resolver=None):
    if resolver is None:
        resolver = LinkResolver()
    lines = []
    lines.append("### Parameters")
    lines.append("")
    for param in params_section.get("parameters", []):
        name = param.get("name", "")
        content = param.get("content", [])
        lines.append(f"- **`{name}`**")
        for c in content:
            text = render_content_block(c, refs, 1, resolver)
            lines.append(text)
    return "\n".join(lines)

def render_return_value(rv_section, refs, resolver=None):
    if resolver is None:
        resolver = LinkResolver()
    lines = []
    lines.append("### Return Value")
    lines.append("")
    for c in rv_section.get("content", []):
        text = render_content_block(c, refs, 0, resolver)
        lines.append(text)
    return "\n".join(lines)

def render_discussion(disc_section, refs, resolver=None):
    if resolver is None:
        resolver = LinkResolver()
    lines = []
    lines.append("### Discussion")
    lines.append("")
    for c in disc_section.get("content", []):
        text = render_content_block(c, refs, 0, resolver)
        lines.append(text)
    return "\n".join(lines)

def render_content_section(section, refs, resolver=None):
    if resolver is None:
        resolver = LinkResolver()
    lines = []
    for c in section.get("content", []):
        text = render_content_block(c, refs, 0, resolver)
        lines.append(text)
    return "\n".join(lines)

def render_topic_section(topic, refs, resolver=None):
    if resolver is None:
        resolver = LinkResolver()
    lines = []
    title = topic.get("title", "")
    lines.append(f"### {title}")
    lines.append("")
    abstract = topic.get("abstract", [])
    if abstract:
        text = render_inline_content(abstract, refs, resolver)
        lines.append(text)
        lines.append("")
    for ident in topic.get("identifiers", []):
        ref = refs.get(ident, {})
        title = ref.get("title", ident.split("/")[-1])
        ref_url = ref.get("url", "")
        abstract_items = ref.get("abstract", [])
        abstract_text = render_inline_content(abstract_items, refs, resolver) if abstract_items else ""
        ref_url = resolver.resolve(ref_url)
        if ref_url:
            lines.append(f"- [{title}]({ref_url})")
        else:
            lines.append(f"- {title}")
        if abstract_text:
            lines.append(f"  {abstract_text}")
        lines.append("")
    return "\n".join(lines)

def doc_to_markdown(data, resolver=None):
    if resolver is None:
        resolver = LinkResolver()
    refs = data.get("references", {})
    metadata = data.get("metadata", {})
    lines = []

    title = metadata.get("title", "Untitled")
    role_heading = metadata.get("roleHeading", "")
    modules = metadata.get("modules", [])
    platforms = metadata.get("platforms", [])

    lines.append(f"# {title}")
    lines.append("")

    if role_heading:
        lines.append(f"**{role_heading}**")
        lines.append("")

    if modules:
        mod_names = [m.get("name", "") for m in modules]
        lines.append(f"**Framework:** {', '.join(mod_names)}")
        lines.append("")

    if platforms:
        plat_info = []
        for p in platforms:
            name = p.get("name", "")
            intro = p.get("introducedAt", "")
            if name and intro:
                plat_info.append(f"{name} {intro}+")
            elif name:
                plat_info.append(name)
        if plat_info:
            lines.append(f"**Availability:** {', '.join(plat_info)}")
            lines.append("")

    hierarchy = data.get("hierarchy", {})
    paths = hierarchy.get("paths", [])
    if paths:
        path = paths[0]
        breadcrumb = []
        for pid in path:
            ref = refs.get(pid, {})
            t = ref.get("title", pid.split("/")[-1])
            u = ref.get("url", "")
            u = resolver.resolve(u)
            if u:
                breadcrumb.append(f"[{t}]({u})")
            else:
                breadcrumb.append(t)
        if breadcrumb:
            lines.append(" > ".join(breadcrumb))
            lines.append("")

    lines.append("---")
    lines.append("")

    abstract = data.get("abstract", [])
    if abstract:
        text = render_inline_content(abstract, refs, resolver)
        lines.append(text)
        lines.append("")

    primary = data.get("primaryContentSections", [])
    has_overview = False
    for section in primary:
        kind = section.get("kind", "")
        if kind == "declarations":
            lines.append("## Declaration")
            lines.append("")
            lines.append(render_declaration(section, refs))
        elif kind == "parameters":
            lines.append(render_parameters(section, refs, resolver))
        elif kind == "possibleValues":
            lines.append("### Possible Values")
            lines.append("")
            for val in section.get("values", []):
                name = val.get("name", "")
                content = val.get("content", [])
                lines.append(f"- **`{name}`**")
                for c in content:
                    text = render_content_block(c, refs, 1, resolver)
                    lines.append(text)
            lines.append("")
        elif kind == "content":
            content_text = render_content_section(section, refs, resolver).strip()
            if content_text:
                if not has_overview:
                    lines.append("## Overview")
                    lines.append("")
                    has_overview = True
                lines.append(content_text)
                lines.append("")
        elif kind == "restEndpoint":
            endpoint = section.get("endpoint", {})
            method = endpoint.get("method", "GET")
            path = endpoint.get("path", "")
            lines.append("## Endpoint")
            lines.append("")
            lines.append(f"```")
            lines.append(f"{method} {path}")
            lines.append(f"```")
            lines.append("")
        else:
            content = section.get("content", [])
            content_text = "\n".join(render_content_block(c, refs, 0, resolver) for c in content).strip()
            if content_text:
                lines.append(f"## {kind.capitalize()}")
                lines.append("")
                lines.append(content_text)
                lines.append("")

    topics = data.get("topicSections", [])
    if topics:
        lines.append("## Topics")
        lines.append("")
        for topic in topics:
            lines.append(render_topic_section(topic, refs, resolver))

    see_also = data.get("seeAlsoSections", [])
    if see_also:
        lines.append("## See Also")
        lines.append("")
        for section in see_also:
            title = section.get("title", "")
            if title:
                lines.append(f"### {title}")
                lines.append("")
            for ident in section.get("identifiers", []):
                ref = refs.get(ident, {})
                t = ref.get("title", ident.split("/")[-1])
                u = ref.get("url", "")
                abs_items = ref.get("abstract", [])
                abs_text = render_inline_content(abs_items, refs, resolver) if abs_items else ""
                u = resolver.resolve(u)
                if u:
                    lines.append(f"- [{t}]({u})")
                else:
                    lines.append(f"- {t}")
                if abs_text:
                    lines.append(f"  {abs_text}")
                lines.append("")
            for ref_info in section.get("generated", False) and [] or section.get("reference", []):
                pass

    legal = data.get("legalNotices", {})
    copyright_text = legal.get("copyright", "")
    if copyright_text:
        lines.append("---")
        lines.append("")
        lines.append(f"*{copyright_text}*")
        lines.append("")

    return "\n".join(lines)

def extract_child_paths(data):
    paths = []
    refs = data.get("references", {})
    for topic in data.get("topicSections", []):
        for ident in topic.get("identifiers", []):
            ref = refs.get(ident, {})
            url = ref.get("url", "")
            if url and url.startswith("/documentation/"):
                path = url[len("/documentation/"):]
                paths.append(path)
    return paths

def strip_numeric_prefix(name):
    match = re.match(r'^\d+-(.+)$', name)
    if match:
        return match.group(1)
    return name

def url_to_filepath(doc_path):
    parts = doc_path.split("/")
    cleaned = [strip_numeric_prefix(p) for p in parts]
    if len(cleaned) == 1:
        return cleaned[0] + ".md"
    return os.path.join(*cleaned[:-1], cleaned[-1] + ".md")

def url_to_dirname(doc_path):
    parts = doc_path.split("/")
    cleaned = [strip_numeric_prefix(p) for p in parts]
    return os.path.join(*cleaned)

def fetch_hierarchy(root_path, language, output_dir, max_depth=None, delay=0.1, verbose=False):
    visited = set()
    queue = [(root_path, 0)]
    fetched = []

    while queue:
        doc_path, depth = queue.pop(0)

        if doc_path in visited:
            continue
        if max_depth is not None and depth > max_depth:
            continue

        visited.add(doc_path)

        if verbose:
            print(f"[{len(visited)}] Fetching: {doc_path}", file=sys.stderr)

        data = fetch_json(doc_path, language)
        if not data:
            continue

        title = data.get("metadata", {}).get("title", doc_path.split("/")[-1])

        fetched.append({
            "path": doc_path,
            "title": title,
            "depth": depth,
            "data": data
        })

        child_paths = extract_child_paths(data)
        for child_path in child_paths:
            if child_path not in visited:
                queue.append((child_path, depth + 1))

        if delay > 0:
            time.sleep(delay)

    known_paths = set(f["path"] for f in fetched)

    if verbose:
        print(f"\nRendering {len(fetched)} documents with internal links...", file=sys.stderr)

    results = []
    for item in fetched:
        resolver = LinkResolver(known_paths=known_paths, current_path=item["path"])
        markdown = doc_to_markdown(item["data"], resolver)
        results.append({
            "path": item["path"],
            "title": item["title"],
            "depth": item["depth"],
            "markdown": markdown,
            "data": item["data"]
        })

    return results

def write_hierarchy(results, output_dir, verbose=False):
    os.makedirs(output_dir, exist_ok=True)

    for result in results:
        doc_path = result["path"]
        markdown = result["markdown"]

        filepath = os.path.join(output_dir, url_to_filepath(doc_path))
        filedir = os.path.dirname(filepath)

        if filedir:
            os.makedirs(filedir, exist_ok=True)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(markdown)

        if verbose:
            print(f"  Written: {filepath}", file=sys.stderr)

    return len(results)

def print_hierarchy_tree(results):
    by_depth = {}
    for r in results:
        d = r["depth"]
        if d not in by_depth:
            by_depth[d] = []
        by_depth[d].append(r)

    for depth in sorted(by_depth.keys()):
        items = by_depth[depth]
        indent = "  " * depth
        for item in items:
            print(f"{indent}- {item['title']} ({item['path']})")

def main():
    parser = argparse.ArgumentParser(
        description="Fetch Apple Developer documentation and convert to Markdown",
        epilog="""Examples:
  %(prog)s https://developer.apple.com/documentation/coreservices/apple_events?language=objc
  %(prog)s --hierarchy -o ./docs https://developer.apple.com/documentation/coreservices/apple_events
  %(prog)s --hierarchy --tree https://developer.apple.com/documentation/coreservices/apple_events"""
    )
    parser.add_argument("url", help="Apple Developer documentation URL")
    parser.add_argument("-o", "--output", help="Output file or directory (for --hierarchy)")
    parser.add_argument("-l", "--language", default=None,
                        help="Language override (objc or swift)")
    parser.add_argument("--json", action="store_true",
                        help="Output raw JSON instead of Markdown")
    parser.add_argument("--hierarchy", action="store_true",
                        help="Fetch entire hierarchy recursively")
    parser.add_argument("--tree", action="store_true",
                        help="Print hierarchy tree structure (with --hierarchy)")
    parser.add_argument("--max-depth", type=int, default=None,
                        help="Maximum depth to fetch (with --hierarchy)")
    parser.add_argument("--delay", type=float, default=0.1,
                        help="Delay between requests in seconds (default: 0.1)")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="Verbose output")
    args = parser.parse_args()

    doc_path, lang = parse_doc_url(args.url)
    if args.language:
        lang = args.language

    if args.hierarchy:
        output_dir = args.output or "apple_docs"
        print(f"Fetching hierarchy from: {doc_path}", file=sys.stderr)
        print(f"Output directory: {output_dir}", file=sys.stderr)

        results = fetch_hierarchy(
            doc_path, lang, output_dir,
            max_depth=args.max_depth,
            delay=args.delay,
            verbose=args.verbose
        )

        if args.tree:
            print("\nHierarchy structure:", file=sys.stderr)
            print_hierarchy_tree(results)

        count = write_hierarchy(results, output_dir, verbose=args.verbose)
        print(f"\nFetched {count} documents to {output_dir}/", file=sys.stderr)
    else:
        data = fetch_json(doc_path, lang)
        if not data:
            sys.exit(1)

        if args.json:
            output = json.dumps(data, indent=2)
        else:
            output = doc_to_markdown(data)

        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(output)
            print(f"Written to {args.output}", file=sys.stderr)
        else:
            print(output)

if __name__ == "__main__":
    main()

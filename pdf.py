#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = ["pymupdf"]
# ///
import argparse
import os
import re
import sys
import urllib.request
from urllib.parse import urlparse, unquote


# for Yamaha MusicCast spec:
# Basic: https://community.symcon.de/uploads/short-url/7r8QTdkYFNfJVJmKbtqvdleuzKt.pdf
# Advanced: https://community.symcon.de/uploads/short-url/vRXaJXAn6vI2DSQYMHF0aqLbdir.pdf

def download_pdf(url: str) -> tuple[str, bytes]:
    """Download PDF from URL, following redirects. Returns (filename, content)."""
    req = urllib.request.Request(url, headers={"User-Agent": "PDFSplitter/1.0"})
    with urllib.request.urlopen(req) as response:
        content = response.read()

        # Try to get filename from Content-Disposition header
        content_disp = response.headers.get("Content-Disposition", "")
        filename = None
        if "filename=" in content_disp:
            match = re.search(r'filename[*]?=["\']?([^"\';]+)["\']?', content_disp)
            if match:
                filename = match.group(1)
                # Handle RFC 5987 encoded filenames (e.g., filename*=UTF-8''name.pdf)
                if filename.startswith("UTF-8''") or filename.startswith("utf-8''"):
                    filename = unquote(filename.split("''", 1)[1])

        # Fall back to URL path
        if not filename:
            parsed = urlparse(response.url)
            filename = os.path.basename(parsed.path)

        # Ensure .pdf extension
        if not filename.lower().endswith(".pdf"):
            filename += ".pdf"

        return filename, content


def sanitize_filename(name: str) -> str:
    """Sanitize a string for use in a filename."""
    # Replace spaces with hyphens
    name = name.replace(" ", "-")
    # Remove or replace problematic characters
    name = re.sub(r'[<>:"/\\|?*]', "-", name)
    # Collapse multiple hyphens
    name = re.sub(r'-+', "-", name)
    # Strip leading/trailing hyphens
    name = name.strip("-")
    return name


def get_outline_titles(doc) -> dict[int, str]:
    """Extract PDF outline/bookmarks and map page numbers to their titles."""
    page_titles = {}
    toc = doc.get_toc()  # Returns list of [level, title, page_number]

    for level, title, page_num in toc:
        # page_num is 1-indexed in TOC, convert to 0-indexed
        page_idx = page_num - 1
        if page_idx >= 0 and page_idx not in page_titles:
            page_titles[page_idx] = title

    return page_titles


def split_pdf(pdf_content: bytes, output_dir: str) -> int:
    """Split PDF into individual pages. Returns number of pages created."""
    import fitz  # PyMuPDF

    os.makedirs(output_dir, exist_ok=True)

    doc = fitz.open(stream=pdf_content, filetype="pdf")
    num_pages = len(doc)

    # Determine zero-padding width based on total page count
    width = len(str(num_pages))

    # Get outline titles mapped to page indices
    page_titles = get_outline_titles(doc)

    for page_idx in range(num_pages):
        # Create new single-page PDF
        new_doc = fitz.open()
        new_doc.insert_pdf(doc, from_page=page_idx, to_page=page_idx)

        # Build filename
        page_num_str = str(page_idx + 1).zfill(width)

        if page_idx in page_titles:
            title = sanitize_filename(page_titles[page_idx])
            filename = f"{page_num_str}-{title}.pdf"
        else:
            filename = f"{page_num_str}.pdf"

        output_path = os.path.join(output_dir, filename)
        new_doc.save(output_path)
        new_doc.close()

        print(f"  {filename}", file=sys.stderr)

    doc.close()
    return num_pages


def main():
    parser = argparse.ArgumentParser(
        description="Download a PDF and split it into individual pages",
        epilog="""Examples:
  %(prog)s https://example.com/userguide.pdf
  %(prog)s -o ./output https://example.com/manual.pdf"""
    )
    parser.add_argument("url", help="URL of the PDF to download")
    parser.add_argument("-o", "--output", help="Output directory (default: derived from PDF filename)")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")
    args = parser.parse_args()

    # Download PDF
    print(f"Downloading: {args.url}", file=sys.stderr)
    filename, content = download_pdf(args.url)
    print(f"Downloaded: {filename} ({len(content)} bytes)", file=sys.stderr)

    # Determine output directory
    if args.output:
        output_dir = args.output
    else:
        # Remove .pdf extension for directory name
        output_dir = re.sub(r'\.pdf$', '', filename, flags=re.IGNORECASE)

    # Split PDF
    print(f"Splitting into: {output_dir}/", file=sys.stderr)
    num_pages = split_pdf(content, output_dir)
    print(f"Created {num_pages} page(s)", file=sys.stderr)


if __name__ == "__main__":
    main()

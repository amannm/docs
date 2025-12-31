#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = ["pymupdf"]
# ///
import argparse
import os
import re
import sys


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
        description="Split a local PDF into individual pages",
        epilog="""Examples:
  %(prog)s ./userguide.pdf
  %(prog)s -o ./output ./manual.pdf"""
    )
    parser.add_argument("pdf_path", help="Path to a local PDF file")
    parser.add_argument("-o", "--output", help="Output directory (default: derived from PDF filename)")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")
    args = parser.parse_args()

    pdf_path = os.path.abspath(args.pdf_path)
    if not os.path.isfile(pdf_path):
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    if not pdf_path.lower().endswith(".pdf"):
        raise ValueError(f"Not a .pdf file: {pdf_path}")

    filename = os.path.basename(pdf_path)
    with open(pdf_path, "rb") as handle:
        content = handle.read()

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

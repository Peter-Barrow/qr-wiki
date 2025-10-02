#!/usr/bin/env python3
"""
Generate QR codes for all markdown files in the wiki.
Each QR code points to the corresponding page on the deployed site.
"""

import os
import qrcode
from pathlib import Path
from typing import Dict, List


# SITE_URL = os.environ.get('SITE_URL', 'http://localhost:8000')
# DOCS_DIR = Path('docs')
# QR_OUTPUT_DIR = Path('qr-codes')
# QR_DOCS_DIR = DOCS_DIR / 'qr-codes'

SITE_URL = os.environ.get("SITE_URL", "http://localhost:8000")
DOCS_DIR = Path("docs")
QR_OUTPUT_DIR = Path("docs/qr-codes")  # Changed: now inside docs/
QR_DOCS_DIR = DOCS_DIR / "qr-codes"


def get_page_url(md_file: Path) -> str:
    """Convert a markdown file path to its corresponding URL."""
    rel_path = md_file.relative_to(DOCS_DIR)
    url_path = str(rel_path).replace(".md", "").replace(os.sep, "/")

    if url_path == "index":
        return SITE_URL
    else:
        return f"{SITE_URL}/{url_path}/"


def get_page_title(md_file: Path) -> str:
    """Extract the title from the markdown file (first # heading)."""
    try:
        with open(md_file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("# "):
                    return line[2:].strip()
    except Exception:
        pass

    # Fallback to filename
    return md_file.stem.replace("-", " ").title()


def generate_qr_code(url: str, output_path: Path) -> None:
    """Generate a QR code for the given URL and save it."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    img.save(output_path)


def generate_all_qr_codes() -> Dict[str, Dict[str, str]]:
    """Generate QR codes for all markdown files and return metadata."""
    QR_OUTPUT_DIR.mkdir(exist_ok=True)

    pages_data = {}

    # Find all markdown files except special ones
    for md_file in DOCS_DIR.rglob("*.md"):
        # Skip the qr-codes listing page itself
        if md_file.name == "qr-codes.md":
            continue

        rel_path = md_file.relative_to(DOCS_DIR)
        url = get_page_url(md_file)
        title = get_page_title(md_file)

        # Generate QR code
        qr_filename = rel_path.with_suffix(".png")
        qr_output_path = QR_OUTPUT_DIR / qr_filename

        generate_qr_code(url, qr_output_path)

        # Store metadata
        pages_data[str(rel_path)] = {
            "title": title,
            "url": url,
            "qr_path": str(qr_filename),
        }

        print(f"✓ Generated QR code for '{title}' -> {qr_output_path}")

    return pages_data


def generate_qr_codes_page(pages_data: Dict[str, Dict[str, str]]) -> None:
    """Generate a markdown page listing all QR codes."""
    qr_page_path = DOCS_DIR / "qr-codes.md"

    with open(qr_page_path, "w", encoding="utf-8") as f:
        f.write("# QR Codes for All Pages\n\n")
        f.write(
            "Print these QR codes and attach them to physical equipment or locations.\n\n"
        )
        f.write("!!! tip\n")
        f.write(
            "    Download the QR codes from the `qr-codes/` directory in the repository.\n\n"
        )

        # Group by directory
        grouped: Dict[str, List[tuple]] = {}
        for md_path, data in sorted(pages_data.items()):
            directory = str(Path(md_path).parent)
            if directory == ".":
                directory = "Home"
            else:
                directory = directory.replace(os.sep, " / ").title()

            if directory not in grouped:
                grouped[directory] = []
            grouped[directory].append((md_path, data))

        # Write grouped QR codes
        for directory, items in sorted(grouped.items()):
            f.write(f"## {directory}\n\n")

            for md_path, data in items:
                f.write(f"### {data['title']}\n\n")
                f.write(f"**URL:** [{data['url']}]({data['url']})\n\n")
                # f.write(
                #     f'![QR Code for {data["title"]}](../{data["qr_path"]}){{ width="300" }}\n\n'
                # )
                # f.write(f"[Download QR Code](../{data['qr_path']}){{ .md-button }}\n\n")
                f.write(
                    f'![QR Code for {data["title"]}](qr-codes/{Path(data["qr_path"]).name}){{ width="300" }}\n\n'
                )
                f.write(
                    f"[Download QR Code](qr-codes/{Path(data['qr_path']).name}){{ .md-button }}\n\n"
                )
                f.write("---\n\n")

    print(f"✓ Generated QR codes listing page -> {qr_page_path}")


def main():
    """Main entry point."""
    print(f"Generating QR codes for site: {SITE_URL}")
    print(f"Scanning docs directory: {DOCS_DIR}\n")

    pages_data = generate_all_qr_codes()
    generate_qr_codes_page(pages_data)

    print(f"\n✓ Successfully generated {len(pages_data)} QR codes")
    print(f"QR codes saved to: {QR_OUTPUT_DIR}/")


if __name__ == "__main__":
    main()

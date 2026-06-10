"""
Update image URLs in HTML files by replacing local image paths with CDN URLs.

This script processes HTML files and replaces relative image paths (images/*.jpg)
with absolute CDN URLs (*.webp format). The updated file is saved with "_updated"
suffix in the same directory as the input file.

To use this tool with pipx and the package installed as "gg-tools", run the following command in your terminal:
    update-image-urls path/to/your/email_template.html
"""

from pathlib import Path
import re
import sys

BASE_URL = "https://www.gracedandgolden.com/mail-images/"


def main():
    if len(sys.argv) != 2:
        print("Usage: update-image-urls <html-file>")
        sys.exit(1)

    # Read the input HTML file
    html_file = Path(sys.argv[1])
    html = html_file.read_text(encoding="utf-8")

    # Replace image paths: images/filename.jpg -> {BASE_URL}filename.webp
    updated_html = re.sub(r"images/([A-Za-z0-9_-]+)\.jpg", rf"{BASE_URL}\1.webp", html)

    # Create output file with "_updated" suffix in the same directory
    output_file = html_file.with_name(f"{html_file.stem}_updated.html")
    output_file.write_text(updated_html, encoding="utf-8")

    print(f"Updated {html_file} -> {output_file}")


if __name__ == "__main__":
    main()

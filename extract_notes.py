"""
Pulls plain text out of raw meeting-notes .docx files (Step 1 of the
bd-market-memo pipeline) so it can be fed to the skill for research +
drafting. Uses only the standard library (zipfile) -- no pandoc/python-docx
dependency needed just to read text back out.

Usage:
    python3 extract_notes.py path/to/meeting_notes.docx [more.docx ...]
"""
import zipfile
import re
import html
import sys


def extract_text(docx_path: str) -> str:
    with zipfile.ZipFile(docx_path) as z:
        xml = z.read("word/document.xml").decode("utf-8")
    xml = xml.replace("</w:p>", "</w:p>\n")
    xml = re.sub(r"<w:tab/>", "\t", xml)
    text = re.sub(r"<[^>]+>", "", xml)
    text = html.unescape(text)
    lines = [line.strip() for line in text.split("\n")]
    return "\n".join(line for line in lines if line)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"===== {path} =====")
        print(extract_text(path))
        print()

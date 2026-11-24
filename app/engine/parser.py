"""Turn a contract (DOCX or plain text) into a list of numbered clauses.

Standard library only: a .docx file is a zip archive with word/document.xml inside.
"""
import io
import re
import zipfile
from xml.etree import ElementTree

W_NS = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"

# "1. Purpose", "12) Term", "§ 3 Kara umowna", "§3."
HEADING_RE = re.compile(r"^\s*(?:§\s*(\d+)\.?|(\d+)[.)])\s+(.{1,120})$")


def docx_to_text(data: bytes) -> str:
    """Extract paragraphs from a .docx file as plain text, one paragraph per line."""
    with zipfile.ZipFile(io.BytesIO(data)) as zf:
        xml = zf.read("word/document.xml")
    root = ElementTree.fromstring(xml)
    lines = []
    for para in root.iter(W_NS + "p"):
        text = "".join(node.text or "" for node in para.iter(W_NS + "t"))
        lines.append(text)
    return "\n".join(lines)


def split_clauses(text: str):
    """Split text into clauses by top-level numbering.

    Returns a list of dicts: {"ref": "5", "heading": "Contractual penalty", "text": "..."}.
    Text before the first numbered heading becomes the "preamble" clause.
    Without any numbering, paragraphs (blank-line separated) become clauses.
    """
    clauses = []
    current = {"ref": "preamble", "heading": "Preamble", "lines": []}
    found_heading = False
    for line in text.splitlines():
        m = HEADING_RE.match(line)
        # A heading is short and does not end like a sentence.
        if m and len(m.group(3)) <= 80 and not m.group(3).rstrip().endswith((".", ";", ",")):
            found_heading = True
            if current["lines"] or current["ref"] != "preamble":
                clauses.append(current)
            ref = m.group(1) or m.group(2)
            current = {"ref": ref, "heading": m.group(3).strip(), "lines": []}
        else:
            current["lines"].append(line)
    clauses.append(current)

    if not found_heading:
        paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
        return [
            {"ref": str(i + 1), "heading": p.split("\n")[0][:60], "text": p}
            for i, p in enumerate(paragraphs)
        ]

    result = []
    for c in clauses:
        body = "\n".join(c["lines"]).strip()
        if c["ref"] == "preamble" and not body:
            continue
        result.append({"ref": c["ref"], "heading": c["heading"], "text": body})
    return result

"""Mask personal and company identifiers before text leaves the server (e.g. to an LLM).

Pattern-based and deliberately conservative: it catches typical Polish identifiers,
but names of people are NOT detected yet (see docs/05_legal_compliance.md, open questions).
"""
import re

PATTERNS = [
    ("EMAIL", re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")),
    ("IBAN", re.compile(r"\bPL\s?\d{2}(?:\s?\d{4}){6}\b")),
    ("PHONE", re.compile(r"(?<!\d)(?:\+48[\s-]?)?\d{3}[\s-]\d{3}[\s-]\d{3}(?!\d)")),
    ("KRS", re.compile(r"\bKRS[:\s]*\d{10}\b")),
    ("NIP", re.compile(r"\b(?:NIP[:\s]*)?\d{3}-\d{3}-\d{2}-\d{2}\b|\bNIP[:\s]*\d{10}\b")),
    ("PESEL", re.compile(r"(?<!\d)\d{11}(?!\d)")),
]


def mask(text: str):
    """Return (masked_text, counts) where counts = {"EMAIL": 2, ...}."""
    counts = {}
    for label, pattern in PATTERNS:
        n = 0

        def repl(_m, label=label):
            nonlocal n
            n += 1
            return "[{}_{}]".format(label, n)

        text = pattern.sub(repl, text)
        if n:
            counts[label] = n
    return text, counts

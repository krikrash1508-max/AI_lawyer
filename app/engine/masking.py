"""Mask personal and company identifiers before text leaves the server (e.g. to an LLM).

Pattern-based and deliberately conservative: it catches typical Polish identifiers and
names of people that follow a cue ("represented by", "reprezentowana przez", "Pan", …).
Names without a cue (e.g. a bare signature line) are NOT detected yet — that needs a
proper name recogniser before a pilot (see docs/05_legal_compliance.md).
"""
import re

UPPER = "A-ZĄĆĘŁŃÓŚŹŻ"
LOWER = "a-ząćęłńóśźż"
NAME_WORD = "[{U}][{L}]+(?:-[{U}][{L}]+)?".format(U=UPPER, L=LOWER)
NAME_CUE = (
    r"represented by|signed by|on behalf of whom|contact person|attn\.?|attention:?|"
    r"reprezentowan[aey]+ przez|w imieniu której działa|osoba kontaktowa|"
    r"Mr\.?|Mrs\.?|Ms\.?|Pan|Pani|Panem|Panią"
)

PATTERNS = [
    ("EMAIL", re.compile(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+")),
    ("IBAN", re.compile(r"\bPL\s?\d{2}(?:\s?\d{4}){6}\b")),
    ("PHONE", re.compile(r"(?<!\d)(?:\+48[\s-]?)?\d{3}[\s-]\d{3}[\s-]\d{3}(?!\d)")),
    ("KRS", re.compile(r"\bKRS[:\s]*\d{10}\b")),
    ("NIP", re.compile(r"\b(?:NIP[:\s]*)?\d{3}-\d{3}-\d{2}-\d{2}\b|\bNIP[:\s]*\d{10}\b")),
    ("PESEL", re.compile(r"(?<!\d)\d{11}(?!\d)")),
]
# Names: two or three capitalised words after a cue; the cue stays, only the name is replaced.
NAME_RE = re.compile(r"(\b(?i:{cue})\s+)({w}(?:\s+{w}){{1,2}})".format(cue=NAME_CUE, w=NAME_WORD))


def _mask_names(text, counts):
    n = 0

    def repl(m):
        nonlocal n
        n += 1
        return "{}[NAME_{}]".format(m.group(1), n)

    text = NAME_RE.sub(repl, text)
    if n:
        counts["NAME"] = n
    return text


def mask(text: str):
    """Return (masked_text, counts) where counts = {"EMAIL": 2, "NAME": 1, ...}."""
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
    text = _mask_names(text, counts)
    return text, counts

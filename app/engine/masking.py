"""Mask personal and company identifiers before text leaves the server (e.g. to an LLM).

Pattern-based, standard library only (ADR-0004). Identifiers (email, phone, PESEL, NIP,
KRS, IBAN) are masked by their format. Names of people are found in three layers:

1. after a cue: "represented by", "reprezentowana przez", "Pan", "Name:", "Imię i nazwisko:";
2. in the signature block ("Signatures", "Podpisy", "For and on behalf of", "Za … sp. z o.o.")
   and next to a job title ("Prezes Zarządu", "Managing Director", "Prokurent" …);
3. every later mention of a person found once — with or without the first name, as an
   initial ("J. Kowalski") or in another grammatical case ("Kowalskiego") — gets the same label.

Not covered yet: a name with no cue, no title and outside the signature block; addresses.
"""
import re

UPPER = "A-ZĄĆĘŁŃÓŚŹŻ"
LOWER = "a-ząćęłńóśźż"
NAME_WORD = "[{U}][{L}]+(?:-[{U}][{L}]+)?".format(U=UPPER, L=LOWER)
# 2–3 capitalised words on one line (no line breaks inside a name)
NAME = r"{w}(?:[ \t]+{w}){{1,2}}".format(w=NAME_WORD)

NAME_CUE = (
    r"represented by|signed by|on behalf of whom|contact person|attn\.?|attention:?|"
    r"reprezentowan[aey]+ przez|w imieniu której działa|osoba kontaktowa|"
    r"Mr\.?|Mrs\.?|Ms\.?|Pan|Pani|Panem|Panią|"
    r"name[ \t]*:|full name[ \t]*:|imię i nazwisko[ \t]*:|by[ \t]*:"
)
TITLE = (
    r"(?:Wice)?[Pp]rezes(?:a)? Zarządu|Członek Zarządu|Członkini Zarządu|Prokurent(?:ka)?|"
    r"Pełnomocnik|Dyrektor(?:ka)?(?: [A-ZĄĆĘŁŃÓŚŹŻa-ząćęłńóśźż]+)?|Radca prawny|Adwokat|"
    r"President of the Management Board|(?:Vice-)?President|Member of the Management Board|"
    r"Board Member|Managing Director|Director|CEO|CFO|COO|General Counsel|Head of Legal|"
    r"Attorney-in-fact|Proxy|Authorised Signatory|Authorized Signatory"
)
COMPANY_SUFFIX = re.compile(
    r"^[ \t,]*(?:sp\. z o\.o\.|spółka|S\.A\.|sp\. ?k\.|sp\. ?j\.|Ltd|Limited|GmbH|Inc|LLC|plc|B\.V\.|AG)\b", re.I)
# Words that start with a capital in contracts but are never part of a person's name
STOP_WORDS = {
    "Agreement", "Party", "Parties", "Receiving", "Disclosing", "Confidential", "Information",
    "Purpose", "Company", "Signature", "Signatures", "Date", "Place", "Name", "Title", "Position",
    "Umowa", "Strona", "Strony", "Podpis", "Podpisy", "Data", "Miejsce", "Spółka", "Spółki",
    "Prezes", "Wiceprezes", "Zarządu", "Członek", "Członkini", "Prokurent", "Pełnomocnik",
    "Dyrektor", "Radca", "Adwokat", "President", "Member", "Management", "Board", "Managing",
    "Director", "General", "Counsel", "Head", "Legal", "Proxy", "Authorised", "Authorized",
    "Signatory", "For", "On", "Behalf", "Za", "In", "Witness", "Whereof", "The", "Warsaw",
    "Warszawa", "Kraków", "Poland", "Polska", "Republic", "Rzeczypospolitej", "Polskiej",
}

PATTERNS = [
    ("EMAIL", re.compile(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+")),
    ("IBAN", re.compile(r"\bPL\s?\d{2}(?:\s?\d{4}){6}\b")),
    ("PHONE", re.compile(r"(?<!\d)(?:\+48[\s-]?)?\d{3}[\s-]\d{3}[\s-]\d{3}(?!\d)")),
    ("KRS", re.compile(r"\bKRS[:\s]*\d{10}\b")),
    ("NIP", re.compile(r"\b(?:NIP[:\s]*)?\d{3}-\d{3}-\d{2}-\d{2}\b|\bNIP[:\s]*\d{10}\b")),
    ("PESEL", re.compile(r"(?<!\d)\d{11}(?!\d)")),
]

# Layer 1: a cue, then the name (the cue itself stays in the text)
CUE_RE = re.compile(r"\b(?i:{cue})[ \t]+({name})".format(cue=NAME_CUE, name=NAME))
# Layer 2: name next to a job title — "Jan Kowalski, Prezes Zarządu" / "Jan Kowalski\nCEO" /
# "Prezes Zarządu Jan Kowalski" / "Director: Jan Kowalski"
NAME_TITLE_RE = re.compile(r"({name})[ \t]*(?:,|–|-|\(|\n)[ \t]*(?:{title})\b".format(name=NAME, title=TITLE))
TITLE_NAME_RE = re.compile(r"\b(?:{title})[ \t]*[:,–-]?[ \t]+({name})".format(title=TITLE, name=NAME))
# Layer 2: the signature block starts at one of these lines and runs to the end of the text
SIGNATURE_START_RE = re.compile(
    r"^[ \t]*(?:signatures?\b|podpisy\b|in witness whereof|for and on behalf of|on behalf of\b|"
    r"w imieniu\b|za[ \t]+[^\n]{0,60}?(?:sp\. z o\.o\.|S\.A\.|spółk|Ltd|GmbH))",
    re.I | re.M)
# A line that is only a name, maybe after a signature mark like "/-/" or "(signed)"
SIGNATURE_LINE_RE = re.compile(r"^[ \t]*(?:/-/|\(signed\)|\(podpis\)|_+)?[ \t]*({name})[ \t]*$".format(name=NAME), re.M)


def _defined_terms(text):
    """Short names the contract defines in quotes, e.g. ("Alfa"): never a person."""
    return {w for t in re.findall(r"[(\[]\s*[\"“„']([^\"”']{1,40})[\"”']", text) for w in t.split()}


def _is_person(candidate, text_after, stop):
    words = re.split(r"[ \t]+", candidate.strip())
    if len(words) < 2 or any(w in stop for w in words):
        return False
    return not COMPANY_SUFFIX.match(text_after)


def _stem(word):
    """Crude Polish stem for declension: Kowalski/Kowalskiego/Kowalskim → Kowalsk."""
    stem = re.sub(r"[aąeęioóuy]+$", "", word)
    return stem if len(stem) >= 3 else word


def _find_people(text):
    stop = STOP_WORDS | _defined_terms(text)
    found = []

    def add(m, group=1):
        cand = m.group(group)
        if _is_person(cand, text[m.end(group):m.end(group) + 20], stop):
            found.append((m.start(group), cand))

    for m in CUE_RE.finditer(text):
        add(m)
    for m in NAME_TITLE_RE.finditer(text):
        add(m)
    for m in TITLE_NAME_RE.finditer(text):
        add(m)
    start = SIGNATURE_START_RE.search(text)
    if start:
        for m in SIGNATURE_LINE_RE.finditer(text, start.start()):
            add(m)
    found.sort()
    return [name for _, name in found]


def _mask_names(text, counts):
    """Give each person one label and replace every mention of them."""
    people = {}  # surname stem -> (label number, first-name stems)
    for name in _find_people(text):
        words = re.split(r"[ \t]+", name)
        key = _stem(words[-1])
        num, firsts = people.get(key, (len(people) + 1, set()))
        firsts.update(_stem(w) for w in words[:-1])
        people[key] = (num, firsts)
    for key, (num, firsts) in sorted(people.items(), key=lambda kv: -len(kv[0])):
        first = "|".join(re.escape(f) for f in sorted(firsts, key=len, reverse=True))
        first_part = r"(?:{f})[{L}]{{0,4}}[ \t]+|".format(f=first, L=LOWER) if first else ""
        pattern = re.compile(
            r"(?<![{L}{U}])(?:{first_part}[{U}]\.[ \t]*)?{surname}[{L}]{{0,4}}(?![{L}{U}])".format(
                first_part=first_part, surname=re.escape(key), L=LOWER, U=UPPER))
        text = pattern.sub("[NAME_{}]".format(num), text)
    if people:
        counts["NAME"] = len(people)  # number of people, not of mentions
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

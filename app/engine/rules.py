"""Rule-based playbook check ("demo mode").

Works offline and deterministically, so the prototype can be shown and tested without
an API key. Each rule in playbooks/nda_pl.json has an evaluator below. The LLM mode
(engine/llm.py) uses the same playbook and returns findings in the same shape.

Finding shape:
  {rule_id, topic, level: "risk"|"review"|"ok", missing: bool,
   clause_ref, quote, explanation, suggested_edit, standard}
"""
import re

FOREIGN_LAW = re.compile(
    r"laws? of (England|Wales|Germany|France|Switzerland|the State of \w+|New York|Delaware|Ireland|"
    r"the Netherlands|Cyprus|Luxembourg|Austria)|English law|German law|Swiss law",
    re.I,
)
POLISH = re.compile(r"Poland|Polish|polsk|Rzeczypospolitej", re.I)
FOREIGN_COURT = re.compile(r"courts? of (London|England|Berlin|Paris|Zurich|New York|Dublin|Vienna)|LCIA|ICC arbitration|Swiss Chambers", re.I)
NUM_WORDS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
             "eight": 8, "nine": 9, "ten": 10, "fifteen": 15, "twenty": 20}


def _sentence(text, pattern):
    """Return the sentence of `text` that matches `pattern` (for quoting)."""
    for s in re.split(r"(?<=[.;])\s+", text):
        if re.search(pattern, s, re.I):
            return s.strip()
    return text.strip()[:240]


def _find(clauses, pattern):
    """First clause whose heading or text matches pattern."""
    for c in clauses:
        if re.search(pattern, c["heading"] + "\n" + c["text"], re.I):
            return c
    return None


def _finding(rule, level, clause=None, quote="", explanation="", missing=False):
    return {
        "rule_id": rule["id"],
        "topic": rule["topic"],
        "level": level,
        "missing": missing,
        "clause_ref": clause["ref"] if clause else None,
        "clause_heading": clause["heading"] if clause else None,
        "quote": quote,
        "explanation": explanation,
        "standard": rule["standard"],
        "suggested_edit": "" if level == "ok" else rule["suggested_edit"],
    }


def _governing_law(rule, clauses):
    pat = r"governed by|governing law|prawo właściwe|podlega prawu"
    c = _find(clauses, pat)
    if not c:
        return _finding(rule, "review", missing=True, explanation="No governing law clause found.")
    q = _sentence(c["text"], pat)
    if FOREIGN_LAW.search(q):
        return _finding(rule, "risk", c, q, "Foreign law chosen; playbook requires Polish law.")
    if POLISH.search(q):
        return _finding(rule, "ok", c, q, "Polish law — matches the playbook.")
    return _finding(rule, "review", c, q, "Governing law is unclear — check manually.")


def _jurisdiction(rule, clauses):
    pat = r"courts?|arbitration|sąd"
    c = _find(clauses, r"dispute|court|arbitration|sąd")
    if not c:
        return _finding(rule, "review", missing=True, explanation="No dispute resolution clause found.")
    q = _sentence(c["text"], pat)
    if FOREIGN_COURT.search(q):
        return _finding(rule, "risk", c, q, "Disputes go to a foreign forum — costly for us.")
    if POLISH.search(q) or re.search(r"registered seat|common court|Warsaw|Warszaw", q, re.I):
        return _finding(rule, "ok", c, q, "Polish court — matches the playbook.")
    return _finding(rule, "review", c, q, "Forum is unclear — check manually.")


def _duration(rule, clauses):
    pat = r"indefinite|perpetual|in perpetuity|without time limit|bezterminow|survive|remain in force|years?|lat\b"
    c = _find(clauses, r"confidentiality shall|obligations of confidentiality|indefinite|perpetu|survive")
    if not c:
        return _finding(rule, "review", missing=True, explanation="Duration of the confidentiality obligation not found.")
    q = _sentence(c["text"], pat)
    if re.search(r"indefinite|perpetu|without time limit|bezterminow", q, re.I):
        return _finding(rule, "risk", c, q, "Obligation never ends — playbook allows 2–5 years.")
    m = re.search(r"\((\d+)\)\s*years|(\d+)\s*years|\b(" + "|".join(NUM_WORDS) + r")\b\s*(?:\(\d+\)\s*)?years", q, re.I)
    if m:
        years = int(m.group(1) or m.group(2) or NUM_WORDS[m.group(3).lower()])
        if 2 <= years <= 5:
            return _finding(rule, "ok", c, q, "{} years — within the 2–5 year standard.".format(years))
        if years > 10:
            return _finding(rule, "risk", c, q, "{} years — far above the standard.".format(years))
        return _finding(rule, "review", c, q, "{} years — outside the 2–5 year standard.".format(years))
    return _finding(rule, "review", c, q, "Duration could not be read — check manually.")


def _exclusions(rule, clauses):
    c = _find(clauses, r"shall not include|does not include|exclusions|nie obejmuj|shall not apply to")
    if not c:
        return _finding(rule, "risk", missing=True, explanation="No exclusions from Confidential Information.")
    q = _sentence(c["text"], r"shall not include|does not include|exclusions|nie obejmuj|shall not apply")
    checks = {
        "public domain": r"public",
        "already known": r"known to|in (its|the) possession|prior to disclosure|before disclosure",
        "independently developed": r"independently developed",
        "received from a third party": r"third party",
    }
    present = [k for k, p in checks.items() if re.search(p, c["text"], re.I)]
    absent = [k for k in checks if k not in present]
    if len(present) >= 4:
        return _finding(rule, "ok", c, q, "All standard exclusions present.")
    level = "risk" if len(present) <= 1 else "review"
    return _finding(rule, level, c, q, "Missing exclusions: " + ", ".join(absent) + ".")


def _required_by_law(rule, clauses):
    pat = r"required by (law|a court|any authority)|court order|competent (court|authority)|wymaga(ją)? przepisy"
    c = _find(clauses, pat)
    if not c:
        return _finding(rule, "review", missing=True, explanation="No exception for disclosure required by law.")
    return _finding(rule, "ok", c, _sentence(c["text"], pat), "Exception for legally required disclosure is present.")


def _penalty(rule, clauses):
    pat = r"contractual penalty|kar[aęy] umown|liquidated damages"
    c = _find(clauses, pat)
    if not c:
        return _finding(rule, "ok", explanation="No contractual penalty — acceptable.")
    q = _sentence(c["text"], pat)
    amount = None
    m = re.search(r"(?:PLN|zł)\s*(\d[\d\s,.]*)|(\d[\d\s,.]*)\s*(?:PLN|zł)", q, re.I)
    if m:
        digits = re.sub(r"[^\d]", "", m.group(1) or m.group(2))
        amount = int(digits) if digits else None
    one_sided = not re.search(r"breaching Party|each Party|either Party|the other Party", q, re.I)
    problems = []
    if amount and amount > 100000:
        problems.append("PLN {:,} exceeds the PLN 100,000 limit".format(amount))
    if one_sided:
        problems.append("penalty binds only one Party")
    if problems:
        text = "; ".join(problems)
        return _finding(rule, "risk", c, q, text[0].upper() + text[1:] + ".")
    return _finding(rule, "review", c, q, "Mutual penalty within limit — confirm the amount with the business.")


def _liability(rule, clauses):
    pat = r"indemnif|unlimited liability|all losses|indirect loss|lost profits|consequential"
    c = _find(clauses, pat)
    if not c:
        return _finding(rule, "ok", explanation="No indemnity or extended liability — general Civil Code rules apply.")
    q = _sentence(c["text"], pat)
    return _finding(rule, "risk", c, q, "Indemnity / liability beyond the Civil Code standard.")


def _non_solicit(rule, clauses):
    pat = r"solicit|non-compete|not compete|employ any employee|zakaz konkurencji"
    c = _find(clauses, pat)
    if not c:
        return _finding(rule, "ok", explanation="No non-solicitation or non-compete.")
    return _finding(rule, "risk", c, _sentence(c["text"], pat), "Restriction outside the scope of an NDA.")


def _return(rule, clauses):
    pat = r"return or destroy|destroy|zwr[oó]c|zniszcz"
    c = _find(clauses, pat)
    if not c:
        return _finding(rule, "review", missing=True, explanation="No obligation to return or destroy information.")
    return _finding(rule, "ok", c, _sentence(c["text"], pat), "Return / destruction clause present.")


def _gdpr(rule, clauses):
    pat = r"personal data|GDPR|RODO|2016/679|dane osobowe"
    c = _find(clauses, pat)
    if not c:
        return _finding(rule, "review", missing=True, explanation="No personal data (GDPR) clause.")
    return _finding(rule, "ok", c, _sentence(c["text"], pat), "Personal data clause present.")


EVALUATORS = {
    "NDA-01": _governing_law,
    "NDA-02": _jurisdiction,
    "NDA-03": _duration,
    "NDA-04": _exclusions,
    "NDA-05": _required_by_law,
    "NDA-06": _penalty,
    "NDA-07": _liability,
    "NDA-08": _non_solicit,
    "NDA-09": _return,
    "NDA-10": _gdpr,
}

LEVEL_ORDER = {"risk": 0, "review": 1, "ok": 2}


def check(clauses, playbook):
    findings = [EVALUATORS[r["id"]](r, clauses) for r in playbook["rules"] if r["id"] in EVALUATORS]
    findings.sort(key=lambda f: (LEVEL_ORDER[f["level"]], f["rule_id"]))
    return findings

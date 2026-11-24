"""Klauzula AI review engine (TO-BE process, docs/03_architecture.md):

mask identifiers → check against the playbook and Polish law references → report for the lawyer.
A new version from the counterparty is a new round: it is checked the same way and compared
with the previous round (what changed, which risks appeared or went away).
"""
import json
import time
from pathlib import Path

from . import compare, llm, masking, parser, rules

PLAYBOOK_DIR = Path(__file__).resolve().parents[1] / "playbooks"


def load_playbook(playbook_id="nda_pl"):
    return json.loads((PLAYBOOK_DIR / (playbook_id + ".json")).read_text(encoding="utf-8"))


def review(text, filename="", playbook_id="nda_pl", use_claude=None, previous=None):
    """Check one version of a contract.

    previous: optional {"round": 1, "clauses": [...], "findings": [...]} from the previous
    round (already masked). Then the result also says what changed since that round.
    """
    started = time.time()
    playbook = load_playbook(playbook_id)
    masked_text, mask_counts = masking.mask(text)
    clauses = parser.split_clauses(masked_text)

    mode, note = "rules", ""
    if use_claude is None:
        use_claude = llm.available()
    findings = None
    if use_claude:
        try:
            findings = llm.check(clauses, playbook)
            mode = "claude"
        except Exception as exc:  # keep the demo usable if the API is unavailable
            note = "Claude mode failed ({}); used the rule-based check.".format(type(exc).__name__)
    if findings is None:
        findings = rules.check(clauses, playbook)

    # Polish law: every finding carries the legal basis of its playbook rule.
    basis = {r["id"]: r.get("legal_basis", "") for r in playbook["rules"]}
    for f in findings:
        f["legal_basis"] = basis.get(f["rule_id"], "")

    counts = {lvl: sum(1 for f in findings if f["level"] == lvl) for lvl in ("risk", "review", "ok")}
    result = {
        "filename": filename,
        "round": 1,
        "mode": mode,
        "note": note,
        "playbook": {k: playbook[k] for k in ("id", "title", "version", "status")},
        "masked": mask_counts,
        "clauses": clauses,
        "findings": findings,
        "counts": counts,
        "red_flags": counts["risk"],
        "seconds": round(time.time() - started, 2),
    }
    if previous:
        result["round"] = int(previous.get("round", 1)) + 1
        result.update(compare.compare(previous["clauses"], clauses, previous["findings"], findings))
    return result

"""Klauzula review engine: parse → mask → check against playbook → compare → export."""
import json
import time
from pathlib import Path

from . import llm, masking, parser, rules

PLAYBOOK_DIR = Path(__file__).resolve().parents[1] / "playbooks"


def load_playbook(playbook_id="nda_pl"):
    return json.loads((PLAYBOOK_DIR / (playbook_id + ".json")).read_text(encoding="utf-8"))


def review(text, filename="", playbook_id="nda_pl", use_claude=None):
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

    counts = {lvl: sum(1 for f in findings if f["level"] == lvl) for lvl in ("risk", "review", "ok")}
    return {
        "filename": filename,
        "mode": mode,
        "note": note,
        "playbook": {k: playbook[k] for k in ("id", "title", "version", "status")},
        "masked": mask_counts,
        "clauses": clauses,
        "findings": findings,
        "counts": counts,
        "seconds": round(time.time() - started, 2),
    }

"""Compare two versions of a contract clause by clause."""
import difflib
import re

from . import rules


def _word_diff(a: str, b: str):
    """List of [op, text] where op is "=", "-" or "+"."""
    ta, tb = re.findall(r"\S+|\s+", a), re.findall(r"\S+|\s+", b)
    out = []
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, ta, tb, autojunk=False).get_opcodes():
        if tag == "equal":
            out.append(["=", "".join(ta[i1:i2])])
        else:
            if i2 > i1:
                out.append(["-", "".join(ta[i1:i2])])
            if j2 > j1:
                out.append(["+", "".join(tb[j1:j2])])
    return out


def compare(old_clauses, new_clauses, playbook):
    old_by_ref = {c["ref"]: c for c in old_clauses}
    new_by_ref = {c["ref"]: c for c in new_clauses}
    refs = list(old_by_ref)
    refs += [r for r in new_by_ref if r not in old_by_ref]

    changes = []
    for ref in refs:
        o, n = old_by_ref.get(ref), new_by_ref.get(ref)
        if o and not n:
            status, diff = "removed", [["-", o["text"]]]
        elif n and not o:
            status, diff = "added", [["+", n["text"]]]
        elif o["text"] == n["text"]:
            status, diff = "unchanged", [["=", n["text"]]]
        else:
            status, diff = "modified", _word_diff(o["text"], n["text"])
        changes.append({
            "ref": ref,
            "heading": (n or o)["heading"],
            "status": status,
            "diff": diff,
        })

    old_f = {f["rule_id"]: f for f in rules.check(old_clauses, playbook)}
    new_f = {f["rule_id"]: f for f in rules.check(new_clauses, playbook)}
    risk_changes = []
    for rid, nf in new_f.items():
        of = old_f[rid]
        if of["level"] != nf["level"]:
            better = rules.LEVEL_ORDER[nf["level"]] > rules.LEVEL_ORDER[of["level"]]
            risk_changes.append({
                "rule_id": rid,
                "topic": nf["topic"],
                "before": of["level"],
                "after": nf["level"],
                "direction": "resolved" if better else "new_risk",
                "explanation": nf["explanation"],
            })
    risk_changes.sort(key=lambda r: (r["direction"] != "new_risk", r["rule_id"]))
    return {"changes": changes, "risk_changes": risk_changes, "findings_new": list(new_f.values())}

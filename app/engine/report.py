"""Export a review with the lawyer's decisions as a Word-compatible file or Markdown."""
import html
from datetime import date

LEVEL_LABEL = {"risk": "Red flag", "review": "Review", "ok": "OK"}
DECISION_LABEL = {"accepted": "Edit accepted", "rejected": "Edit rejected", "": "No decision"}


VERDICT_LABEL = {
    "sign": "Ready for signing — no edits to send",
    "edits": "Edits to send to the counterparty (via sales / purchasing)",
    "": "Not decided yet",
}


def to_markdown(review, decisions, verdict=""):
    accepted = [f for f in review["findings"]
                if f["level"] != "ok" and decisions.get(f["rule_id"], {}).get("decision") == "accepted"]
    lines = [
        "# Contract review report — {}".format(review.get("filename") or "contract"),
        "",
        "Date: {} · Round {} · Playbook: {} v{} · Mode: {}".format(
            date.today().isoformat(), review.get("round", 1), review["playbook"]["title"],
            review["playbook"]["version"], review["mode"]),
        "",
        "> Prepared with Klauzula AI as a working aid for the lawyer. It is not legal advice; "
        "the lawyer reviews and decides on every point.",
        "",
        "Lawyer's decision: {}".format(VERDICT_LABEL.get(verdict, VERDICT_LABEL[""])),
        "",
        "Red flags: {} · Review: {} · OK: {}".format(
            review["counts"]["risk"], review["counts"]["review"], review["counts"]["ok"]),
        "",
    ]
    if review.get("risk_changes"):
        lines += ["## Since the previous round", ""]
        for x in review["risk_changes"]:
            lines.append("- {}: {} — {} → {}".format(
                "New risk" if x["direction"] == "new_risk" else "Improved", x["topic"],
                LEVEL_LABEL[x["before"]], LEVEL_LABEL[x["after"]]))
        lines.append("")
    if verdict == "edits" and accepted:
        lines += ["## Edits to send to the counterparty", ""]
        for f in accepted:
            where = "§ " + f["clause_ref"] if f.get("clause_ref") else "new clause"
            lines += ["- {} ({}): {}".format(f["topic"], where, decisions[f["rule_id"]].get("edit") or f["suggested_edit"])]
        lines.append("")
    lines += [
        "| # | Topic | Result | Clause | Decision |",
        "|---|---|---|---|---|",
    ]
    for i, f in enumerate(review["findings"], 1):
        lines.append("| {} | {} | {} | {} | {} |".format(
            i, f["topic"], LEVEL_LABEL[f["level"]], "§ " + f["clause_ref"] if f.get("clause_ref") else "missing",
            DECISION_LABEL[decisions.get(f["rule_id"], {}).get("decision", "")]))
    lines.append("")
    for f in review["findings"]:
        if f["level"] == "ok":
            continue
        d = decisions.get(f["rule_id"], {})
        lines += ["## {} — {} ({})".format(f["rule_id"], f["topic"], LEVEL_LABEL[f["level"]]), ""]
        if f.get("quote"):
            lines += ["Contract text: \"{}\"".format(f["quote"]), ""]
        lines += ["Why: " + f["explanation"], "", "Playbook standard: " + f["standard"], ""]
        if f.get("legal_basis"):
            lines += ["Polish law (to verify): " + f["legal_basis"], ""]
        if f.get("suggested_edit"):
            lines += ["Suggested wording: " + (d.get("edit") or f["suggested_edit"]), ""]
        if d.get("comment"):
            lines += ["Lawyer's comment: " + d["comment"], ""]
    return "\n".join(lines)


def to_word_html(review, decisions, verdict=""):
    """HTML that Word opens as a document (saved with a .doc extension)."""
    md = to_markdown(review, decisions, verdict)
    body = []
    for line in md.split("\n"):
        esc = html.escape(line)
        if line.startswith("# "):
            body.append("<h1>{}</h1>".format(esc[2:]))
        elif line.startswith("## "):
            body.append("<h2>{}</h2>".format(esc[3:]))
        elif line.startswith("> "):
            body.append("<p><i>{}</i></p>".format(esc[5:]))
        elif line.startswith("- "):
            body.append("<p>• {}</p>".format(esc[2:]))
        elif line.startswith("|---"):
            continue
        elif line.startswith("|"):
            cells = [c.strip() for c in line.strip("|").split("|")]
            body.append("<tr>" + "".join("<td>{}</td>".format(html.escape(c)) for c in cells) + "</tr>")
        elif line:
            body.append("<p>{}</p>".format(esc))
    out, in_table = [], False
    for b in body:
        if b.startswith("<tr>") and not in_table:
            out.append('<table border="1" cellpadding="4" style="border-collapse:collapse">')
            in_table = True
        if not b.startswith("<tr>") and in_table:
            out.append("</table>")
            in_table = False
        out.append(b)
    if in_table:
        out.append("</table>")
    return ("<html><head><meta charset='utf-8'><style>body{font-family:Calibri,Arial,sans-serif;font-size:11pt}"
            "h1{font-size:16pt}h2{font-size:13pt}</style></head><body>" + "\n".join(out) + "</body></html>")

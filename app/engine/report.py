"""Export a review with the lawyer's decisions as a Word-compatible file or Markdown."""
import html
from datetime import date

LEVEL_LABEL = {"risk": "Red flag", "review": "Review", "ok": "OK"}
DECISION_LABEL = {"accepted": "Edit accepted", "rejected": "Edit rejected", "": "No decision"}


def to_markdown(review, decisions):
    lines = [
        "# NDA review — {}".format(review.get("filename") or "contract"),
        "",
        "Date: {} · Playbook: {} v{} · Mode: {}".format(
            date.today().isoformat(), review["playbook"]["title"], review["playbook"]["version"], review["mode"]),
        "",
        "> Prepared with Klauzula as a working aid for the lawyer. It is not legal advice; "
        "the lawyer reviews and decides on every point.",
        "",
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
        if f.get("suggested_edit"):
            lines += ["Suggested wording: " + (d.get("edit") or f["suggested_edit"]), ""]
        if d.get("comment"):
            lines += ["Lawyer's comment: " + d["comment"], ""]
    return "\n".join(lines)


def to_word_html(review, decisions):
    """HTML that Word opens as a document (saved with a .doc extension)."""
    md = to_markdown(review, decisions)
    body = []
    for line in md.split("\n"):
        esc = html.escape(line)
        if line.startswith("# "):
            body.append("<h1>{}</h1>".format(esc[2:]))
        elif line.startswith("## "):
            body.append("<h2>{}</h2>".format(esc[3:]))
        elif line.startswith("> "):
            body.append("<p><i>{}</i></p>".format(esc[5:]))
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

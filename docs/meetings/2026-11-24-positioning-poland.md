# 2026-11-24 — New positioning: a tool for the lawyer, Poland

- Participants: project owner, Claude (AI assistant)
- Goal: adjust the Step 2 research to the team's decisions on positioning, country and target client

## What was done
- The research [07_research.md](../07_research.md) was rewritten for the new inputs (0.1.0 → 0.3.0); the Word version [AI_lawyer_Research_Step2.docx](../AI_lawyer_Research_Step2.docx) was rebuilt.
- The decision was recorded as [ADR-0002](../decisions/0002-positioning-poland-in-house.md).
- The product overview [00_overview.md](../00_overview.md) was filled in (0.2.0).
- Customer complaints about Juro were detailed (section 3.3).
- Section 3.4 "Poland: what lawyers say" was added.
- Three commits were pushed to GitHub (`2384143`, `85eb0a4`, `4cf6d08`).

## Key takeaways
- **Segment:** mid-sized Polish companies with 1–5 lawyers and a large flow of repetitive contracts; the user is the lawyer, the buyer is the head of legal / CFO.
- **Main competitors in Poland** are legal database publishers: Wolters Kluwer (LEX Expert AI, Libra) and C.H.Beck (Beck-Noxtua); in practice lawyers most often use ChatGPT, Copilot, DeepL.
- **The buyer's main objection is data:** 81% of Polish lawyers worry about confidentiality (SET/Logit survey); 36% know no specialised AI tool.
- **Juro (per reviews):** lacks "edits on top of edits" in negotiations, correct transfer of Word formatting, reports, flexible configuration, Teams integration.
- **There are no independent reviews of legal AI from Polish legal departments** — our own interviews are needed.
- The risk of "unauthorised legal advice" is lower than in the SME segment: the lawyer makes the decision.

## Decisions
- Positioning: **a tool that speeds up the lawyer's work** (not a replacement for the lawyer) — ADR-0002.
- Target country: **Poland**.
- Target client: **companies that need to optimise the lawyer's work**.
- The "SMEs without a lawyer" segment from research version 0.1.0 is no longer a target.

## Tasks
- [ ] Choose one contract type (NDA, B2B services/supply) — group
- [ ] Conduct 5–10 interviews with in-house lawyers and heads of legal in Poland (time per contract, willingness to pay given LEX/Legalis, IT/DPO data requirements) — group
- [ ] Check in the text of the statutes who may provide legal assistance in Poland — group
- [ ] Find a lawyer for the first playbook — group
- [ ] Update the Project Charter per section 7 of the research — group
- [ ] Put the new Word version of the research into the group's shared folder — before the final campus meeting
- [ ] Release v0.3.0 with a git tag — project owner

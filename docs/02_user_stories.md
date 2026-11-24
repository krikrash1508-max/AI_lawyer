---
title: User stories
version: 0.3.1
status: draft
owner: TBD
updated: 2026-11-24
---

# User stories

Roles come from the research ([07_research.md](07_research.md), section 2.1) and the TO-BE process ([03_architecture.md](03_architecture.md), section 2).

> **0.3.0:** stories aligned with v0.2 features ([01_requirements.md](01_requirements.md) 0.3.0); US-005 rewritten for a new round; US-009 (lawyer's decision) and US-010 (business receives the edits) added.

| ID | As a <role> | I want <action> | so that <goal> | Acceptance criteria | Feature |
|----|-------------|-----------------|----------------|---------------------|---------|
| US-001 | in-house lawyer | upload the contract the business sent me straight into the Product | I don't copy the text by hand | A .docx up to 5 MB is split into clauses in < 2 s | F1 |
| US-002 | in-house lawyer | see red flags against our playbook right away, with the legal basis behind each rule | I can decide in minutes whether the contract can be signed | Summary "N Red flag / N Review / N OK"; red first; each finding has a legal basis marked "to verify" | F3 |
| US-003 | in-house lawyer | see a verbatim quote and clause number for every finding | I can check the AI instead of taking its word for it | Clicking a finding highlights the clause | F3 |
| US-004 | in-house lawyer | get ready-made wording and edit it | I can prepare edits quickly | Edit text is editable; Accept / Reject / Copy available | F4 |
| US-005 | in-house lawyer | upload the counterparty's new version as the next round | I don't re-read the whole text and can see whether new risks appeared | Round 2: New risk / Improved list + changed clauses marked in the text | F5 |
| US-006 | head of legal / CFO | receive a review report | I can understand the risks without reading the contract | Word export: lawyer's decision, summary, decision table, disclaimer | F4 |
| US-007 | DPO / IT | know that personal data does not go to the LLM | I can approve the tool | Names, PESEL, NIP, e-mail, phone numbers replaced with placeholders before analysis | F2 |
| US-008 | head of legal | set company rules (playbook) | all lawyers review in the same way | Playbook stored in JSON and visible on the Playbook tab; editor — after v0.1 | F3 |
| US-009 | in-house lawyer | answer "any red flags?" with one button | a contract without problems goes straight to signing | Buttons "ready for signing" / "send edits"; the Product shows flags without an accepted edit but does not decide on its own | F4 |
| US-010 | sales / procurement manager | receive the list of edits from the lawyer in plain language | I can send them to the counterparty without retelling | Report has an "Edits to send to the counterparty" section with clause and edit text | F4 |

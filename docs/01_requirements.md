---
title: Requirements and specification v0.2
version: 0.3.3
status: draft
owner: TBD
updated: 2026-11-28
---

# Requirements and specification v0.2

Product: **Klauzula AI** ([ADR-0006](decisions/0006-product-name-klauzula-ai.md), proposed).
Contract type for the MVP: **NDA** ([ADR-0003](decisions/0003-mvp-contract-type-nda.md), proposed).
User: in-house lawyer at a mid-sized Polish company ([ADR-0002](decisions/0002-positioning-poland-in-house.md)); report recipient — the business (sales / procurement).
Process: TO-BE from [03_architecture.md](03_architecture.md), section 2. v0.2 scope: [ADR-0007](decisions/0007-scope-v0-2-to-be-process.md).

> **0.3.0:** the specification was rebuilt around the TO-BE steps. F4 "Edits" and F5 "Comparison and report" were replaced by F4 "Report and lawyer's decision" and F5 "New version — new round"; F3 gained references to Polish legal provisions; FR-004 (names) is partly implemented.

## 1. Five features — by TO-BE process step

| # | Feature | TO-BE step | What it does | Value for the lawyer | Status in v0.2 |
|---|---------|------------|--------------|----------------------|----------------|
| F1 | Upload and parsing | The lawyer uploads the file to the Product | DOCX / TXT / pasted text → clauses (§) with numbers and headings | No need to copy text by hand | ✅ |
| F2 | Identifier masking | Masks identifiers | Names, e-mail, phone, PESEL, NIP, KRS, IBAN → placeholders before analysis | Removes the main objection (81% worry about data) | ✅ Names by marker words, in the signature block and next to job titles; repeats, initials and grammatical cases get the same placeholder; without a marker, job title and outside the signature block — not caught |
| F3 | Review against the playbook and Polish legislation | Analyses the contract | Each rule → OK / Review / Red flag, clause quote, explanation, **Polish / EU legal provision** | Red flags visible in seconds; shows which provision a rule rests on | ✅ rules; 🟡 provisions — examples, not verified; 🟡 Claude mode not tested |
| F4 | Report and lawyer's decision | Generates report → Reviews report → "Any red flags?" | Playbook edit is editable, Accept / Reject; the lawyer chooses "to signing" or "send edits"; report for Word / Markdown with a list of edits for the business | The decision stays with the lawyer; the business gets a ready list of edits | ✅ (track changes in DOCX — no) |
| F5 | New version — new round | New version — back to review | The new version is reviewed like the first, + what changed since the previous round and which risks appeared / went away | No need to re-read the whole text; a new risk is visible in one line | ✅ |

**Not** included in v0.2: login, server-side storage of round history, playbook editor, Word add-in, other contract types, Polish interface, analysis of mandatory Polish-law norms outside the playbook, sending edits from the product (e-mail, Teams).

## 2. Functional requirements

| ID | Requirement | Feature | Priority | Status |
|----|-------------|---------|----------|--------|
| FR-001 | Upload .docx and .txt up to 5 MB, paste text | F1 | Must | ✅ |
| FR-002 | Split into clauses by numbering "1.", "1)", "§ 1"; without numbering — by paragraphs | F1 | Must | ✅ |
| FR-003 | Mask e-mail, phone numbers, PESEL, NIP, KRS, IBAN before the text is sent to the LLM | F2 | Must | ✅ |
| FR-004 | Mask names of natural persons | F2 | **Must** (was Should: names are in the TO-BE diagram) | 🟡 by marker words, in the signature block and next to job titles; repeats, initials and grammatical cases get the same placeholder (sample `nda_counterparty_v3.txt`); a name outside these places — no |
| FR-004a | Mask addresses of natural persons | F2 | Should | ⬜ |
| FR-005 | One finding per playbook rule: level, clause, exact quote, explanation | F3 | Must | ✅ |
| FR-006 | Highlight the clause in the contract text when a finding is clicked | F3 | Should | ✅ |
| FR-007 | A missing clause is marked "missing" | F3 | Must | ✅ |
| FR-014 | Each playbook rule and each finding carries a reference to a Polish / EU legal provision (KC, KPC, UZNK, RODO, Rome I, Brussels I bis) marked "to verify" | F3 | Must | ✅ (references are examples, to be checked by a radca prawny) |
| FR-008 | The edit is editable; Accept / Reject / Copy buttons | F4 | Must | ✅ |
| FR-015 | "Any red flags?" decision block: number of red flags, accepted edits and flags without an edit; two buttons — "ready for signing" / "send edits to the counterparty". The Product does not decide on its own | F4 | Must | ✅ |
| FR-011 | Report export: lawyer's decision, summary, legal provisions, decision table; with "send edits" — an "Edits to send to the counterparty" section for the business. Word (.doc), Markdown | F4 | Must | ✅ |
| FR-012 | Export edits as track changes in .docx | F4 | Should | ⬜ |
| FR-016 | Upload a new version from the report screen as the next round (Round 2, 3…) | F5 | Must | ✅ |
| FR-009 | Clause changes since the previous round: added / removed / modified, word-level diff directly in the contract text | F5 | Must | ✅ |
| FR-010 | Risk changes since the previous round (New risk / Improved) — from the findings of the same mode (rules or Claude) | F5 | Must | ✅ |
| FR-017 | Read track changes from .docx as revisions (who changed what) | F5 | Should | ⬜ currently read as "all changes accepted" |
| FR-013 | Work without an LLM (rule-based mode) for demo and tests | F3 | Must | ✅ |

## 3. Non-functional requirements

| ID | Requirement | Metric / criterion | Status |
|----|-------------|--------------------|--------|
| NFR-001 | Confidentiality | Text is masked before the LLM; contracts are not stored on the server; the model is not trained on the data | ✅ v0.2 stores nothing (rounds live only in the browser) |
| NFR-002 | Storage and processing in the EU | Hosting and LLM processing in the EU | 🟡 demo hosted in the EU (Render, Frankfurt — ADR-0008); LLM processing in the EU open |
| NFR-003 | Speed | NDA review ≤ 60 s (Claude), ≤ 1 s (rules) | ✅ rules: < 0.1 s |
| NFR-004 | Transparency | Each finding: verbatim quote, clause reference, legal provision | ✅ |
| NFR-005 | Human-in-the-loop | The "sign / send edits" decision is made only by the lawyer; nothing is sent to the counterparty automatically; disclaimer on screen and in the report | ✅ |
| NFR-006 | Measurability | Review time "before/after" and number of rounds are recorded in the pilot | ⬜ pilot needed |
| NFR-007 | Easy start | The prototype starts with one command without installing packages | ✅ `python3 app/server.py` |
| NFR-008 | Reliability of provisions | The AI does not invent articles: references to provisions come only from the playbook | ✅ rules; Claude mode — the server inserts provisions from the playbook |

## 4. Acceptance criteria v0.2 (autotests `app/tests`, 12 tests)
- Sample `nda_counterparty_v1.txt` → 6 red flags (law, court, perpetual term, exceptions, penalty, non-solicitation); the representative's name replaced with `[NAME_1]`.
- Sample `nda_counterparty_v3.txt` → 5 people, one placeholder per person; no surname remains in the text, including in the signature block, in the form "J. Przykładowy" and in the case form "Przykładowego"; "Alfa Logistics sp. z o.o.", job titles and contract terms ("Receiving Party") are not masked.
- Every finding has a legal provision; NDA-06 — KC art. 484.
- Sample v2 as round 2 → law and term OK, new risk NDA-07 (indemnity), § 6 removed.
- A report with the "send edits" decision contains an "Edits to send to the counterparty" section with the accepted edits; with the "sign" decision — "Ready for signing".

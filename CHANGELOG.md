# Changelog

All significant changes to the project are recorded in this file.
Format — [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
versioning — [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added
- Masking of personal names in the signature block and next to job titles (Prezes Zarządu, Prokurent, Managing Director…), and after "Name:" / "Imię i nazwisko:"; each person found gets one `[NAME_n]` placeholder throughout the text — including "J. Kowalski" and grammatical cases ("Kowalskiego"). Company names, job titles and contract terms are not masked.
- `app/samples/nda_counterparty_v3.txt` — a fictional NDA with a signature block; 3 new autotests (12 in total).
- `docs/diagrams/as-is.svg` — AS-IS diagram with three horizontal role lanes (business, lawyer, counterparty).
- `docs/diagrams/to-be.svg` — TO-BE diagram with four role lanes (business, lawyer, Product, counterparty).
- `docs/meetings/2026-11-24-process-as-is-to-be.md` — summary of the AS-IS / TO-BE process review session: takeaways, decisions, open tasks.
- `docs/brand/` — generated logo: full (`klauzula-logo-full.webp`) and symbol only (`klauzula-symbol.png`).
- ADR-0006 (proposed): product name **Klauzula AI**, supersedes ADR-0005.
- **Skeleton v0.2** (`app/`) per the TO-BE process: name masking after marker words (`[NAME_n]`); Polish / EU legal provision (`legal_basis`) for every rule and finding; the lawyer's "Any red flags?" decision block (ready for signing / send edits); a new version is round 2 on the same screen with risk changes; `klauzula-report-roundN` report with the decision and a list of edits for the business; 9 autotests.
- ADR-0007 (proposed): v0.2 scope per the TO-BE process.
- `docs/brand/klauzula-mark.svg` and `app/static/favicon.svg` — vector redraw of the symbol for the interface and dark theme.
- `docs/meetings/2026-11-24-step3-to-be-alignment.md` — session summary: what changed, 6 observations, tasks.

### Changed
- **All project materials translated from Russian to English** (language of the documentation is now English): `CLAUDE.md` (the language rule now says English), `README.md`, `.gitignore` comments, this CHANGELOG, all documents in `docs/` (patch version bumped: `00_overview` → 0.2.3, `01_requirements` → 0.3.2, `02_user_stories` → 0.3.1, `03_architecture` → 0.5.2, `04_ai_prompts` → 0.2.1, `05_legal_compliance` → 0.3.2, `06_playbook/_template` → 0.1.1, `06_playbook/nda` → 0.2.1, `07_research` → 0.3.1, `08_design` → 0.3.1), ADR-0000…0007 (wording only, decisions unchanged), meeting notes and the labels in `docs/diagrams/*.svg`. Polish legal terms (kara umowna, radca prawny, KC, UZNK…) and product UI strings are kept as they were.
- `docs/01_requirements.md` → 0.3.1, `docs/03_architecture.md` → 0.5.1, `docs/05_legal_compliance.md` → 0.3.1: status of FR-004 and the limits of name masking; the next step is a Polish name dictionary, not an LLM.
- The `NAME` counter in the summary now shows the number of people, not the number of mentions.
- `docs/mockups/klauzula-design.html`: row F2 and the observation about names.
- `docs/03_architecture.md` → 0.3.0: AS-IS / TO-BE processes revised — role lanes (business, lawyer, Klauzula, counterparty); the counterparty's reply goes through the business and back into the queue; the queue is about 2 days per round; in TO-BE the queue remains and shrinks indirectly; added the step "the lawyer reviews the findings against the quotes"; "PII masking" refined to "identifier masking"; new version: comparison → re-review of v2; .doc report, track changes — next step; AS-IS → TO-BE change table and v0.1 limitations.
- `docs/mockups/klauzula-design.html`: the "Process" block aligned with the new AS-IS / TO-BE.
- `docs/03_architecture.md` → 0.3.1: AS-IS — mermaid replaced with a diagram with role lanes; "NDA" → "contract"; queue ~2 days per round of edits; manual version comparison removed (the counterparty sends edits in Word track changes); "checks against practice" → "checks against the playbook from memory".
- `docs/mockups/klauzula-design.html`: the "Today" block updated with the same edits.
- `docs/03_architecture.md` → 0.4.0: TO-BE redrawn with role lanes; "Klauzula" → "Product", "NDA" → "contract"; "e-mail to the lawyer" → "assigns a task to the lawyer"; queue removed — the lawyer uploads the file to the Product straight away (the new version too); masking extended with names; analysis against the playbook and Polish legislation; the Product generates the report, the lawyer reviews it and sends the reply to the counterparty; removed the "Any red flags?" fork, the wording-edit step, the .doc report and the separate version comparison step; added TO-BE divergences from the prototype.
- `docs/mockups/klauzula-design.html`: the "With Klauzula" block updated per the new TO-BE.
- `docs/03_architecture.md` → 0.4.1: in TO-BE the "Any red flags?" fork was restored after "Reviews the report": no — to signing, yes — the lawyer edits the contract, the business sends the edits to the counterparty; added a step-by-step scenario; role and change tables updated.
- `docs/mockups/klauzula-design.html`: the red-flag fork and sending of edits by the business added to the "With Klauzula" block.
- `docs/08_design.md` → 0.2.0: the name "Klauzula AI" (ADR-0006); the old logo description ("§ in a circle") marked deprecated; new section "4. Logo": files, message, composition of the mark, prompts, checklist for commercial use, open tasks.
- ADR-0005: status changed to "superseded by ADR-0006".
- `docs/01_requirements.md` → 0.3.0: v0.2 specification by TO-BE steps — F4 "Report and lawyer's decision", F5 "New version — new round"; FR-014…017, NFR-008; FR-004 (names) Should → Must.
- `docs/02_user_stories.md` → 0.3.0: US-005 — new round; added US-009 (lawyer's decision), US-010 (business receives the edits).
- `docs/03_architecture.md` → 0.5.0: "TO-BE step → feature → v0.2 screen" table instead of a list of divergences; v0.2 components, data flow and API.
- `docs/05_legal_compliance.md` → 0.3.0: references to Polish law and their risks, the lawyer's decision, name masking.
- `docs/06_playbook/nda.md` → 0.2.0, `app/playbooks/nda_pl.json` → 0.2.0: "Legal basis" column / field.
- `docs/08_design.md` → 0.3.0: 5 mock-ups by TO-BE steps, the `--brand-ok` token, SVG logo.
- `docs/mockups/klauzula-design.html`: name Klauzula AI, new logo, mock-ups Upload → Report → Decision → Round 2 → Playbook, v0.2 specification, new observations.
- `docs/00_overview.md` → 0.2.2: name Klauzula AI, the business as report recipient, rounds.
- `README.md`: prototype v0.2, demo scenario with round 2.

### Removed
- The Compare tab and `POST /api/compare`: version comparison became round 2 in `/api/review` (ADR-0007).
- The "Word add-in" mock-up from the design pack — it is not in the TO-BE diagram; the idea remained in the observations.

## [0.4.0] — 2026-11-24
Includes the changes of the planned but unreleased release 0.3.0 (positioning, ADR-0002) and Project Step 3 (prototype Klauzula v0.1).

### Added
- Prototype **Klauzula v0.1** in `app/` (Python stdlib, no packages): DOCX/TXT upload, PII masking, NDA review against 10 playbook rules, edits with Accept/Reject, version comparison with risk changes, report export to Word/Markdown; Claude mode (`claude-opus-5-5`, structured output) — optional; 6 autotests.
- `skills/nda-review/SKILL.md` — instructions for the AI (prompt-v1).
- `docs/08_design.md` 0.1.0 — name, visual style, mock-ups; `docs/mockups/klauzula-design.html` — Step 3 design pack (process, style, 5 mock-ups, specification, observations).
- `docs/06_playbook/nda.md` 0.1.0 — NDA playbook (Poland), an example, not reviewed by a lawyer.
- ADR-0003 (contract type — NDA), ADR-0004 (prototype stack), ADR-0005 (name Klauzula) — all proposed.
- `docs/meetings/2026-11-24-step3-prototype.md` — Step 3 summary, observations and a plan of tasks in separate chats.
- `.claude/launch.json` — launching the prototype in the Claude Code preview.
- `docs/meetings/2026-11-24-positioning-poland.md`: session summary — new positioning, research conclusions, open tasks.
- ADR-0002: positioning — a tool that speeds up the lawyer's work; target country — Poland; client — companies that need to optimise the lawyer's work.
- `docs/07_research.md` → 0.3.0: section 3.4 "Poland: what lawyers say" — availability of reviews of Polish products, surveys of Polish lawyers (Supesu 2026, SET/Logit), In-House Lawyer Innovation Forum 2025, conclusions for the product.
- `docs/07_research.md`: Polish competitors for lawyers (Wolters Kluwer LEX Expert AI / Libra, Beck-Noxtua), data on the number of lawyers in Poland, buyer and user roles.

### Changed
- `docs/01_requirements.md` → 0.2.0: v0.1 specification — 5 features, FR-001…013, NFR-001…007, acceptance criteria.
- `docs/02_user_stories.md` → 0.2.0: 8 user stories.
- `docs/03_architecture.md` → 0.2.0: AS-IS / TO-BE process diagrams, components, data flow, API.
- `docs/04_ai_prompts.md` → 0.2.0: test set and prompt-v1.
- `docs/05_legal_compliance.md` → 0.2.0: masking, disclaimers, open questions.
- `docs/00_overview.md` → 0.2.1: name Klauzula and contract type NDA.
- `README.md`: instructions for running the prototype.
- `docs/07_research.md` → 0.2.0: problem, segments, arguments against, conclusions and recommendations for the Project Charter revised for the new inputs; main segment — mid-sized Polish companies with 1–5 lawyers.
- `docs/07_research.md` → 0.2.1: complaints about Juro detailed (edits in negotiations, Word formatting, reports, customisation, integrations) with links to reviews.
- `docs/AI_lawyer_Research_Step2.docx`: Word version rebuilt from `07_research.md` v0.3.0.
- `docs/00_overview.md` → 0.2.0: filled in product essence, target user, value and out of scope.

### Removed
- `docs/07_research.md`: data on SMEs without a lawyer (YouGov/LawBite, Smallpdf) — the segment is no longer a target.

## [0.2.0] — 2026-11-24
### Added
- `docs/07_research.md`: research on the problem, user segments, competitors in the EU and their reviews, arguments against the idea, source check and conclusions (Project Step 2).
- `docs/AI_lawyer_Research_Step2.docx`: the research in Word format for submission.
- `docs/meetings/2026-11-24-research-step2.md`: session summary — decisions, research conclusions, open tasks.

## [0.1.0] — 2026-11-22
### Added
- Documentation structure in `docs/` with section templates.
- Templates for ADRs, meeting notes and the contract review playbook.
- ADR-0001: record decisions in the ADR format.
- `CLAUDE.md` with the rules for documentation and versioning.

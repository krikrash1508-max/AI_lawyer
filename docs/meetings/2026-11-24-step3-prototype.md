# 2026-11-24 — Step 3: process, mock-ups, style, specification, prototype v0.1

- Participants: project owner, Claude (AI assistant)
- Goal: prepare the Project Step 3 materials — process diagram, mock-ups, name and style, specification (≤ 5 features), SKILL.md and the first working version

## What was done
| Material | Where |
|----------|-------|
| AS-IS / TO-BE process diagram, data flow | [03_architecture.md](../03_architecture.md) |
| Specification: 5 features, FR/NFR, acceptance criteria | [01_requirements.md](../01_requirements.md), [02_user_stories.md](../02_user_stories.md) |
| Name, style, mock-ups of 5 screens | [08_design.md](../08_design.md), [mockups/klauzula-design.html](../mockups/klauzula-design.html) (also published as a private artifact on claude.ai) |
| Custom instructions for the AI (prompt-v1) | [skills/nda-review/SKILL.md](../../skills/nda-review/SKILL.md), [04_ai_prompts.md](../04_ai_prompts.md) |
| NDA playbook | [06_playbook/nda.md](../06_playbook/nda.md), `app/playbooks/nda_pl.json` |
| Prototype v0.1 | `app/` — run `python3 app/server.py`, tests `python3 -m unittest discover -s app/tests` (6/6 OK) |

## Observations while building v0.1
1. **Template-based rules work on typical NDAs.** The 10 rules found all 6 red flags in the sample. They will miss non-standard wording — Claude mode is needed for robustness, not for the demo.
2. **Version comparison is the strongest moment of the demo.** Version 2 fixed 5 problems and quietly added an indemnity; Klauzula shows this in one "New risk" line.
3. **Masking gap.** Identifiers (PESEL, NIP, e-mail, phone) are masked, but the name of the company's representative is not. Name recognition is needed before a pilot.
4. **Playbook = product.** Quality depends on rules written by a lawyer. Our rules are examples; a radca prawny must review them.
5. **Lawyers work in Word.** .doc export exists, but real track changes in .docx matter more than any screen — the first improvement after v0.1.
6. **No AI results yet.** Claude mode is written but has not been run on the test set (no API key in the environment). Without accuracy figures we cannot promise time savings.
7. **Environment limitation:** the laptop has only Python 3.9 without packages → the prototype is on the standard library ([ADR-0004](../decisions/0004-prototype-stack.md)). Claude mode needs Python ≥ 3.10 and `pip install anthropic`.

## Decisions (proposed — group confirmation needed)
- Contract type for the MVP — **NDA** ([ADR-0003](../decisions/0003-mvp-contract-type-nda.md)).
- Prototype stack — Python stdlib + HTML/JS, Claude as an option ([ADR-0004](../decisions/0004-prototype-stack.md)).
- Name — **Klauzula** ([ADR-0005](../decisions/0005-product-name-klauzula.md)).

## Tasks
- [ ] Confirm ADR-0003, 0004, 0005 (status → accepted) — group
- [ ] Run Claude mode on the two samples, record accuracy in `04_ai_prompts.md` — project owner
- [ ] Have the NDA playbook reviewed by a radca prawny — group
- [ ] Collect 10–20 anonymised NDAs for the test set — group
- [ ] Masking of natural persons' names (FR-004) — development
- [ ] Track changes in .docx (FR-012) — development
- [ ] Check the "Klauzula" trademark (EUIPO, UPRP) — group
- [ ] Put the Step 3 materials (design pack, specification, repository link) into the group's shared folder — before the final meeting

## Plan: Step 3 tasks as separate chats
Decision of the project owner: do each task in a separate Claude Code chat (one task = one chat = one commit).

**Condition before starting:** the work of this session must be committed and pushed to GitHub — new chats start from the latest commit and do not see uncommitted files.

| # | Chat | Goal (done when…) | Files | Depends on |
|---|------|--------------------|-------|-----------|
| 0 | ✅ Commit and release v0.4.0 | Two commits, tag `v0.4.0`, push to GitHub | `CHANGELOG.md`, everything from this session | — (done first) |
| 1 | Test Claude mode | prompt-v1 run on `nda_counterparty_v1/v2`, accuracy against the reference recorded in `04_ai_prompts.md` | `app/engine/llm.py`, `docs/04_ai_prompts.md` | 0; Python ≥ 3.10, `anthropic`, API key |
| 2 | 🟡 Name masking (FR-004) — marker-based done in v0.2 ([summary](2026-11-24-step3-to-be-alignment.md)); remaining: NER and addresses | Names and addresses of natural persons are masked; test on the sample; FR-004 → ✅ | `app/engine/masking.py`, `app/tests/` | 0 |
| 3 | Track changes in DOCX (FR-012) | `.docx` export with edits as Word tracked changes; FR-012 → ✅ | `app/engine/report.py`, new module | 0 |
| 4 | Extend the test set | 10–20 fictional NDAs with reference findings | `app/samples/`, `docs/04_ai_prompts.md` | 0 |
| 5 | Check the name Klauzula | Search of trademarks (EUIPO, UPRP) and domains, outcome in ADR-0005 | `docs/decisions/0005-…` | 0 |
| 6 | Word version of Step 3 for submission | `.docx` from `01_requirements`, `03_architecture`, `08_design` + a reminder to put it in the shared folder | `docs/` | 0, preferably 1 |

Group tasks (not for a chat): confirm ADR-0003/0004/0005, have the playbook reviewed by a radca prawny, collect real anonymised NDAs.

**How to start a chat:** new chat in this folder → paste "Task N from the plan in docs/meetings/2026-11-24-step3-prototype.md" → at the end of the chat Claude updates this file (marks the task) and the CHANGELOG.

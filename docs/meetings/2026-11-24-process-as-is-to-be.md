# 2026-11-24 — AS-IS / TO-BE process review

- Participants: project owner, Claude (AI assistant)
- Goal: check the process diagrams against prototype v0.1 and revise AS-IS and TO-BE

## What was done
| Material | Where |
|----------|-------|
| AS-IS diagram: 3 lanes (business, lawyer, counterparty) | [diagrams/as-is.svg](../diagrams/as-is.svg) |
| TO-BE diagram: 4 lanes (business, lawyer, Product, counterparty) | [diagrams/to-be.svg](../diagrams/to-be.svg) |
| Roles, scenario, "AS-IS → TO-BE" table, divergences from v0.1 | [03_architecture.md](../03_architecture.md) 0.2.0 → 0.4.1 |
| "Process" block in the design pack | [mockups/klauzula-design.html](../mockups/klauzula-design.html) |
| Commits | `3ba1881` (first review), `285caf4` (role lanes) |

Step 3 task 1 (testing Claude mode) was also worked through: it needs Python ≥ 3.10, the `anthropic` package and an API key — the laptop currently has Python 3.9 without the package or a key; there is no separate file with the reference findings.

## Key takeaways
- **Check against the prototype:** the old diagrams promised more than v0.1 does: "personal data masking" (names are not masked), upload of DOCX only, a transition from version comparison straight to edits.
- **Version comparison** in v0.1 is a separate screen without edits and always rule-based (`compare.py` → `rules.check`), even in Claude mode.
- **Counterparties' lawyers work in Word with track changes**, so there is no manual search for changes in AS-IS. The value of comparison in the product shifts from "what changed" to "which playbook risks appeared".
- **Mermaid cannot draw horizontal role lanes**, so the diagrams are made in SVG (GitHub shows them as images).

## Decisions
**AS-IS**
- Role lanes: business, lawyer, counterparty.
- The process object is a **contract** (not only an NDA).
- Queue to the lawyer — **~2 days per round of edits**.
- The lawyer **checks against the playbook from memory**.
- Edits and new versions go through the business; the new version arrives with Word track changes.
- Removed: the "whose template" fork, shadow AI, the report for the manager, manual version comparison.

**TO-BE**
- The diagram says "Product" instead of "Klauzula"; the design pack keeps the name Klauzula.
- The business **assigns a task to the lawyer**, there is no queue — the lawyer **uploads the file to the Product** straight away (the new version too).
- The Product **masks names**, e-mail, phone, PESEL, NIP, KRS, IBAN.
- The Product **analyses the contract against the playbook and Polish legislation** and **generates a report** for the lawyer.
- The lawyer **reviews the report** → "Any red flags?": no — signing; yes — the lawyer makes the edits, the business sends them to the counterparty.
- Removed: .doc report / track changes, a separate version comparison step, the playbook as a separate process.

## Tasks
- [ ] Decide whether to add analysis against Polish legislation to the requirements (it is in TO-BE, but not in the specification or v0.1) — group
- [ ] Revisit the wording of F5 and the observation "a lawyer comparing manually will miss something" in light of track-changes work — project owner
- [ ] Decide on the data flow edits (section 4 of `03_architecture.md`): rule fallback, the `/api/compare` block — project owner
- [ ] Republish the design pack on claude.ai (it has the old process) — project owner
- [ ] `git push` of commit `285caf4` — project owner
- [ ] Step 3 task 1: prepare the environment (Python ≥ 3.10, `anthropic`, API key) and the reference findings — project owner

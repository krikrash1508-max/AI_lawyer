# 2026-11-24 — Step 3 per the new TO-BE: mock-ups, name and style, specification, skeleton v0.2

- Participants: project owner, Claude (AI assistant)
- Goal: bring the Step 3 materials in line with the updated TO-BE diagram ([03_architecture.md](../03_architecture.md) 0.4.1), then close the gap with names in signatures

## Session flow
| # | Request | Result | Commit |
|---|---------|--------|--------|
| 1 | Adjust the mock-ups, name and style, specification and skeleton to the new process diagram | Mock-ups, documents and prototype v0.2 per the TO-BE steps; design pack republished (version 2) | `f641541` feat, `bdf5704` docs |
| 2 | Commit and push to GitHub | Two previously unpushed commits were also pushed (`84e0bbe`, `8bd94dc`) | — |
| 3 | Surnames in signatures are not masked — propose a solution | 4 layers without new packages; an LLM for finding names was rejected (names would reach the LLM before masking) | — |
| 4 | Implement layers 1–3 | Names in the signature block and next to job titles, one placeholder per person; 12/12 tests; design pack — version 3 | `b36b45f` feat |

## What was done
| Material | Where |
|----------|-------|
| Mock-ups: 5 screens per the TO-BE steps (Upload → Report → Decision → Round 2 → Playbook) | [mockups/klauzula-design.html](../mockups/klauzula-design.html), [08_design.md](../08_design.md) 0.3.0; private artifact on claude.ai, version 3 |
| Name **Klauzula AI** in mock-ups and interface; logo redrawn as SVG | [brand/klauzula-mark.svg](../brand/klauzula-mark.svg), `app/static/favicon.svg` |
| Specification v0.2: 5 features = TO-BE steps, FR-014…017, NFR-008 | [01_requirements.md](../01_requirements.md) 0.3.1, [02_user_stories.md](../02_user_stories.md) 0.3.0 |
| Decision on the v0.2 scope | [ADR-0007](../decisions/0007-scope-v0-2-to-be-process.md) (proposed) |
| Skeleton v0.2: name masking, legal provisions, lawyer's decision, rounds | `app/` — 12/12 tests OK, checked in the browser |
| Name masking: markers, signature block, job titles; one `[NAME_n]` placeholder per person, including initials and grammatical cases | `app/engine/masking.py`, sample `app/samples/nda_counterparty_v3.txt` |
| Playbook with Polish / EU legal provisions | `app/playbooks/nda_pl.json` 0.2.0, [06_playbook/nda.md](../06_playbook/nda.md) 0.2.0 |
| Architecture, legal requirements, overview | [03_architecture.md](../03_architecture.md) 0.5.1, [05_legal_compliance.md](../05_legal_compliance.md) 0.3.1, [00_overview.md](../00_overview.md) 0.2.2 |

## Observations while building skeleton v0.2
1. **The process removed a screen.** In TO-BE a new version is simply the next round, so the Compare tab became part of the review. This also fixed a v0.1 inconsistency: round 2 risks are computed by the same mode as round 1 (rules or Claude).
2. **The decision belongs to the lawyer.** The Product counts red flags but does not say "can be signed". If the lawyer signs with open flags, the report records that the risk was accepted.
3. **"Polish legislation" in the diagram is broader than what we do.** v0.2 gives a reference to a provision behind each playbook rule. Checking mandatory norms outside the playbook requires a database of acts (ISAP) and a radca prawny; the LLM must not invent articles — so the server supplies the provision.
4. **Names: find a person once — mask them everywhere.** At first only names after markers ("represented by") were masked. The signature block and job titles (Prezes Zarządu, Prokurent, Managing Director) were added; a found person is masked throughout the text, including "J. Kowalski" and "Kowalskiego". A name in free text with no marker or job title is still missed.
5. **The business is also a user.** Edits go to the counterparty through sales, so the report needs a simple "Edits to send" list, not only the legal reasoning.
6. **Lawyers are still in Word.** The new version arrives with track changes, while we read the .docx as if all changes were accepted. Reading and writing track changes is the main improvement. AI accuracy on the test set is still not measured.
7. **Masking must not be done through an LLM.** Finding names via Claude would mean sending names to the LLM before masking (FR-003, NFR-001). So the next steps are a name dictionary and server-side NER.

## Decisions (proposed)
- v0.2 scope per TO-BE: provisions — references from the playbook; new version — a round; the "sign / send edits" decision — the lawyer ([ADR-0007](../decisions/0007-scope-v0-2-to-be-process.md)). Names in ADR-0007 are described as "by markers"; after this session — markers + signature block + job titles. The ADR is proposed; when the group confirms it, the wording should be refined.
- FR-004 (names) raised from Should to Must — names are in the TO-BE diagram.
- Name masking stays on the standard library (ADR-0004). Next steps — a Polish name dictionary, then server-side NER; no LLM is used for finding names.
- The `NAME` counter in the summary = number of people, not mentions.

## Versions
- Documents: `00_overview` 0.2.2, `01_requirements` 0.3.1, `02_user_stories` 0.3.0, `03_architecture` 0.5.1, `05_legal_compliance` 0.3.1, `06_playbook/nda` 0.2.0, `08_design` 0.3.0.
- Project: changes in the Unreleased section of the CHANGELOG; next release — **v0.5.0** (MINOR), tag after ADR-0007 is confirmed.

## Tasks
- [ ] Confirm ADR-0007 (status → accepted), refine the line about names — group
- [ ] Have the legal provisions in the playbook checked by a radca prawny — group
- [ ] Share the design pack with the group via the Share menu on claude.ai (the link is private) — project owner
- [ ] Release v0.5.0 and tag after ADR-0007 is confirmed — project owner
- [x] Names in the signature block and next to job titles, one placeholder per person (FR-004) — sample `nda_counterparty_v3.txt`, 12/12 tests
- [ ] Names in free text: Polish name dictionary (PESEL registry, dane.gov.pl — check the licence), then NER; lawyer confirmation of doubtful cases — development
- [ ] Addresses of natural persons (FR-004a) — development
- [ ] Track changes: reading (FR-017) and writing (FR-012) — development
- [x] Republish the design pack on claude.ai — versions 2 and 3
- [ ] Step 3 task 1 (test Claude mode) — still waiting for Python ≥ 3.10, `anthropic`, an API key

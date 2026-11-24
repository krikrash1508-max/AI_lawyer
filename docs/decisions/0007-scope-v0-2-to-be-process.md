# ADR-0007: Prototype v0.2 scope per the TO-BE process

- Status: proposed
- Date: 2026-11-24
- Related: [ADR-0003](0003-mvp-contract-type-nda.md), [ADR-0004](0004-prototype-stack.md), [ADR-0006](0006-product-name-klauzula-ai.md); process — [03_architecture.md](../03_architecture.md) 0.4.1, section 2

## Context
The TO-BE diagram (role lanes) promises things the v0.1 prototype does not have:
1. masking of **personal names**;
2. analysis **against Polish legislation**, not only against the playbook;
3. the lawyer's **"Any red flags?"** step with two outcomes: signing, or edits via the business;
4. a new version goes **back to review**, with no separate comparison step.

In v0.1 version comparison is a separate tab, and its risks are always computed by rules, even in Claude mode. Analysis against Polish legislation was an open question for the group (meeting 2026-11-24, "Process review").

## Options considered
| Question | Option | Pros | Cons |
|----------|--------|------|------|
| Polish law | A. Do not do it, remove from the diagram | Honest, no risk of errors | Diagram and product diverge; lawyers expect a legal anchor |
| | **B. Reference to the legal provision behind each playbook rule** | Cheap; the provision is verifiable; the AI does not invent articles | Not an analysis of mandatory norms outside the playbook |
| | C. Free-form legal analysis via an LLM | Full promise of the diagram | Hallucinated articles; needs a database of acts (ISAP) and review by a lawyer |
| Version comparison | A. Keep the Compare tab | Already works | Does not match the process; risks always by rules |
| | **B. New version = next review round** | As in the diagram; one mode for rounds | No comparison of two arbitrary files |
| Lawyer's decision | A. The Product itself writes "can be signed" | Fast | Contradicts ADR-0002 (the lawyer decides) |
| | **B. "Any red flags?" block with two lawyer buttons** | Human-in-the-loop; the decision goes into the report | One more click |
| Personal names | **A. Regular expressions on marker words** | Standard library (ADR-0004) | Misses a name without a marker |
| | B. NER (spaCy pl / LLM) | Completeness | Packages and environment; deferred |

## Decision
For v0.2 the options in bold were chosen: legal provisions — references from the playbook (`legal_basis` field, marked "to verify"); new version — round 2 on the same screen (`/api/review` with `previous`, `/api/compare` removed); the "sign / send edits" decision is made by the lawyer; names are masked on marker words.

## Consequences
- Specification — [01_requirements.md](../01_requirements.md) 0.3.0: F4 "Report and lawyer's decision", F5 "New version — new round", FR-014…017, NFR-008.
- Playbook `nda_pl.json` 0.2.0 and [06_playbook/nda.md](../06_playbook/nda.md) 0.2.0 contain the provisions; they must be checked by a radca prawny before a pilot.
- Analysis of mandatory norms outside the playbook and NER for names remain open tasks.
- The Compare tab no longer exists in the interface; mock-ups — [mockups/klauzula-design.html](../mockups/klauzula-design.html).

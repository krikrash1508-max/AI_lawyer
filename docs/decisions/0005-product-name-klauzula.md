# ADR-0005: Product name — Klauzula

- Status: superseded by [ADR-0006](0006-product-name-klauzula-ai.md)
- Date: 2026-11-24

## Context
"AI Lawyer" describes the idea but contradicts the positioning (ADR-0002): we are not an "AI lawyer", we are a lawyer's tool. A name is needed for the mock-ups and the prototype.

## Options considered
| Name | Pros | Cons |
|------|------|------|
| **Klauzula** | Polish for "clause, contract provision"; understandable to a lawyer, sounds professional; the "§" sign as a logo | A common word — harder to register as a trademark |
| Paragraf | Also legal, short | Many existing brands with this word |
| Umowa.ai | Clear at once what it is about | Sounds like a service for non-lawyers; ".ai" promises to replace the lawyer |
| AI Lawyer | Already used in the repository | Contradicts ADR-0002; English-language, no link to Poland |

## Decision
Proposed: **Klauzula** (tagline: "Your playbook, every clause" / "Twój playbook w każdej klauzuli"). The repository and project folder remain `AI_lawyer` for now.

## Consequences
- Needed: check trademarks (EUIPO, UPRP) and available domains before public use.
- Affected documents: `08_design.md`, `01_requirements.md`, `app/static/`.

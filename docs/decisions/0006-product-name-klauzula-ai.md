# ADR-0006: Product name — Klauzula AI

- Status: proposed
- Date: 2026-11-24
- Supersedes [ADR-0005](0005-product-name-klauzula.md)

## Context
For the course assignment on generating a promo image, the group generated a logo (`docs/brand/`). It carries the name **"Klauzula AI"**, while ADR-0005 proposed **"Klauzula"**. One name is needed for the logo, mock-ups, prototype and documentation.

## Options considered
| Name | Pros | Cons |
|------|------|------|
| Klauzula (ADR-0005) | Short; the Polish word is understandable to a lawyer | A common word: the name does not show it is an AI product; weaker as a trademark |
| **Klauzula AI** | Shows at once that it is an AI tool; this is what the finished logo says; the "AI" suffix may make the mark more distinctive | Longer; "AI" may sound like a promise to replace the lawyer (ADR-0002), which must be offset by tone and disclaimers |

## Decision
Proposed: **Klauzula AI**. In text it may be shortened to "Klauzula" when the context makes clear which product is meant. The tagline from ADR-0005 stays: "Your playbook, every clause" / "Twój playbook w każdej klauzuli". The repository is still called `AI_lawyer`.

## Consequences
- The logo in `docs/brand/` matches the name.
- Trademarks (EUIPO, UPRP) and domains need to be re-checked for "Klauzula AI".
- The product's tone stays the same: "a lawyer's tool, the lawyer decides" (ADR-0002, `05_legal_compliance.md`).
- To move to the new name: `00_overview.md`, `01_requirements.md`, the mock-up `docs/mockups/klauzula-design.html`, the interface `app/static/`.

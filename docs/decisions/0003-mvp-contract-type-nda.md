# ADR-0003: MVP contract type — NDA

- Status: proposed
- Date: 2026-11-24

## Context
Step 3 needs a working prototype, but the contract type has not been chosen yet (a task from the 2026-11-24 meeting). Without a single type we cannot write a playbook, a test set or a prompt.

## Options considered
1. **NDA** — short (2–5 pages), very frequent, standard structure, little dependence on industry.
2. B2B services / supply agreement — more value per contract, but longer and highly dependent on industry and payment terms.
3. Several types at once — wider coverage, but no depth in any.

## Decision
Proposed: **option 1 — NDA** for prototype v0.1 and the first interviews. Services / supply agreements are the next playbook if interviews show that lawyers already review NDAs quickly.

## Consequences
- Easier: short anonymised samples, 10 clear rules, a quick demo scenario.
- Harder: NDAs are low-risk, so the time saved per contract is smaller; competitors (Juro, LEGALFLY) also start with NDAs.
- Needed: confirm the choice with the team and in interviews ("how many NDAs per month, how many minutes each").
- Affected documents: `01_requirements.md`, `06_playbook/nda.md`, `04_ai_prompts.md`, `app/`.

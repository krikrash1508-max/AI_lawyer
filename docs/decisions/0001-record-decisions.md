# ADR-0001: Record architecture decisions as ADRs

- Status: accepted
- Date: 2026-11-22

## Context
The project is just starting; it is important to preserve the reasons behind key decisions.

## Options considered
1. Do not record decisions separately
2. Keep ADRs in docs/decisions/

## Decision
Keep ADRs: one decision — one NNNN-title.md file. Accepted ADRs are not edited; a changed decision is recorded as a new ADR with the reference "supersedes ADR-NNNN".

## Consequences
The decision history is transparent and versioned together with the code in git.

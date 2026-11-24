---
title: Product overview
version: 0.2.3
status: draft
owner: TBD
updated: 2026-11-24
---

# Product overview

## In one sentence
An in-house lawyer at a Polish company uses **Klauzula AI** (product name of AI Lawyer, [ADR-0006](decisions/0006-product-name-klauzula-ai.md), proposed) to review **NDAs** ([ADR-0003](decisions/0003-mvp-contract-type-nda.md), proposed) faster against the company playbook under Polish jurisdiction.

## Problem
- The company lawyer is overloaded with repetitive contracts; the business waits for approval.
- Hiring another lawyer is expensive, and contracts with bad terms still get through.

## Target user
- **Country:** Poland ([ADR-0002](decisions/0002-positioning-poland-in-house.md)).
- **Client:** companies that need to optimise the lawyer's work; main segment — mid-sized companies with 1–5 lawyers.
- **User:** in-house lawyer; **buyer:** head of legal / CFO; **report recipient:** the business (sales / procurement) — sends the edits to the counterparty.

## Value
- Saves the lawyer's time on contract review (metric: minutes per contract before/after).
- Review against company rules (playbook) with references to Polish law; findings linked to the contract text; edits in Word.
- A new version from the counterparty is a new round of the same review: shows which risks appeared and which went away.
- Data is stored in the EU and not used for model training.

## What is NOT in the product (out of scope)
- The product does not give binding legal advice — it is a lawyer's tool, and the decision stays with the lawyer.
- A service for non-lawyers (SMEs without a lawyer) is not a target segment (see ADR-0002).
- Law firms are not a target segment for now.

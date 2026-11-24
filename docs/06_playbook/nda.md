---
title: "Playbook: NDA (Poland)"
version: 0.2.1
status: draft
owner: TBD
updated: 2026-11-24
---

# Contract review playbook: NDA (Poland)

> Example rules for the prototype. **Not reviewed by a lawyer** — a radca prawny must review it before any pilot.
> **0.2.0:** added the "Legal basis" column — references to Polish and EU law behind each rule (TO-BE process: analysis against Polish legislation). The references are examples, **to be verified by a radca prawny**.
> Machine-readable version: [`app/playbooks/nda_pl.json`](../../app/playbooks/nda_pl.json) — edit both files when changing either.

| ID | Contract clause | Standard position | Acceptable deviations | Red flag | Recommended edit | Legal basis (to verify) |
|----|-----------------|-------------------|-----------------------|----------|------------------|-------------------------|
| NDA-01 | Governing law | Polish law | — | Foreign law | "…governed by the laws of the Republic of Poland" | Rome I (593/2008), art. 3 |
| NDA-02 | Disputes | Court at our registered seat | Arbitration in Poland | Foreign court / arbitration | "…common court competent for the registered seat of [Our Company]" | Brussels I bis (1215/2012), art. 25; KPC art. 1105 |
| NDA-03 | Confidentiality term | 2–5 years | 1 year or 6–10 years (Review) | Perpetual or > 10 years | 3 years after termination | KC art. 365¹; UZNK art. 11 |
| NDA-04 | Exceptions to Confidential Information | 4 exceptions: public, previously known, independently developed, from third parties | 2–3 exceptions (Review) | 0–1 exceptions | Full list (a)–(d) | UZNK art. 11 ust. 2 |
| NDA-05 | Disclosure required by law | Permitted with notice | — | No exception (Review) | Disclosure required by law / authority | e.g. KPC art. 248 |
| NDA-06 | Kara umowna | None, or mutual ≤ PLN 100,000 | Mutual ≤ PLN 100,000 (Review — agree the amount) | One-sided or > PLN 100,000 | Mutual PLN 50,000 + right to damages above it | KC art. 483–484 (§ 2 — reduction of an excessive kara umowna) |
| NDA-07 | Liability | General rules of the Kodeks cywilny | — | Indemnity, unlimited liability, indirect damages | Liability under KC, no lost profits | KC art. 471, 361 |
| NDA-08 | Non-solicitation / non-compete | Not in the NDA | — | Present | Delete, move to the main contract | UZNK art. 12; KP art. 101¹–101⁴ |
| NDA-09 | Return / destruction | Present | — | Absent (Review) | Return or destroy on request | KC art. 353¹ |
| NDA-10 | Personal data (RODO) | Clause present | — | Absent (Review) | Processing under GDPR, DPA if needed | RODO art. 6, 28; ustawa o ochronie danych osobowych 2018 |

---
title: Legal requirements and compliance
version: 0.3.3
status: draft
owner: TBD
updated: 2026-11-28
---

# Legal requirements and compliance

## Positioning
A tool for the lawyer, not a replacement for the lawyer. Human-in-the-loop: every change is accepted or rejected by the lawyer; nothing is sent to the counterparty automatically.

## GDPR and confidentiality
| Question | Prototype v0.1 | Target state |
|----------|----------------|--------------|
| Where data is stored | Nowhere: the contract is processed in memory and not saved | EU hosting, encryption, retention period set by the client |
| Personal data | v0.2: masked before analysis — names (by marker words, in the signature block and next to job titles; repeats, initials and grammatical cases get the same placeholder), e-mail, phone, PESEL, NIP, KRS, IBAN | Names in free text and addresses of natural persons (name dictionary or NER), review by the client's DPO |
| Use of data by the AI provider | Claude mode is off by default; when enabled, the text goes to the Claude API already masked | Contract with the provider: no training on data, processing in the EU, DPA |
| GDPR role | — | Klauzula AI is the processor, the client is the controller; a DPA with the client is needed |

## Disclaimers (implemented in v0.2)
- On every screen: "Klauzula AI is a working tool for lawyers. Results and legal references are not legal advice; the lawyer reviews and decides."
- In every report: "Prepared with Klauzula AI as a working aid for the lawyer. It is not legal advice…"
- On every legal provision: "Polish law · to verify".

## Public demo (ADR-0008)
- The demo is open to anyone with the link (Render, Frankfurt). It stores no contract text; Render keeps only access logs (time, URL, IP).
- Claude mode is off in the public demo: no text leaves the server.
- The on-screen disclaimer ("do not upload real confidential contracts") applies; demonstrations use only the built-in anonymised samples.
- In the prototype: "do not upload real confidential contracts".

## References to Polish legislation (v0.2)
The TO-BE diagram promises analysis "against Polish legislation". In v0.2 this is a **reference to a provision behind each playbook rule** (KC, KPC, UZNK, KP, RODO, Rome I, Brussels I bis), not a standalone analysis of mandatory norms ([ADR-0007](decisions/0007-scope-v0-2-to-be-process.md)).

| Risk | Measure in v0.2 |
|------|-----------------|
| Wrong or outdated article | Marked "to verify"; the playbook and provisions are checked by a radca prawny before a pilot |
| AI invents articles (hallucinations) | The provision is taken from the playbook by the server, not from the model's answer (NFR-008) |
| The report is taken for a legal opinion | Disclaimer "not legal advice"; the decision is the lawyer's button |

## Lawyer's decision
The Product counts red flags but does not say "can be signed". If the lawyer chooses "ready for signing" with open red flags, the report records that the risk was accepted by the lawyer.

## Open questions
- Names in free text without a marker or job title (for example, "Jan Kowalski will coordinate"): next step — a Polish name dictionary (PESEL registry, dane.gov.pl, check the licence), then server-side NER. Recognition via Claude is not suitable: names would reach the LLM before masking.
- Lawyer confirmation of doubtful cases before analysis ("Possible name — mask?").
- Review of the list of provisions in `app/playbooks/nda_pl.json` by a radca prawny.
- EU processing for LLM calls: check the options available from the provider.
- Check in the text of the statutes who may provide legal assistance in Poland (task from the 2026-11-24 meeting).
- AI Act: a tool for lawyers is probably not high-risk — to be confirmed.

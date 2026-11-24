---
title: LLM prompts
version: 0.2.1
status: draft
owner: TBD
updated: 2026-11-24
---

# LLM prompts

## Test set
| File | Contents | Reference (expected findings) |
|------|----------|-------------------------------|
| `app/samples/nda_counterparty_v1.txt` | Fictional NDA: English law, London courts, perpetual confidentiality, one-sided kara umowna PLN 500,000, non-solicitation, 1 exception to CI | Red flag: NDA-01, 02, 03, 04, 06, 08; Review: NDA-05, 10; OK: NDA-07, 09 |
| `app/samples/nda_counterparty_v2.txt` | The same NDA after negotiation: Polish law, 5 years, mutual penalty PLN 50,000, but indemnity added | Red flag: NDA-07; OK: NDA-01, 02, 03, 08 |

The reference was compiled by the team from the playbook, **not by a lawyer** — it needs review by a radca prawny. 10–20 anonymised NDAs are needed for a fair evaluation.

## Prompt versions

### prompt-v1 — 2026-11-24
- **Where:** [`skills/nda-review/SKILL.md`](../skills/nda-review/SKILL.md) (file body = system prompt) + playbook `app/playbooks/nda_pl.json` in the `<playbook>` tag. Called from `app/engine/llm.py`.
- **Model:** `claude-opus-5-5`, effort `high`, structured output (finding JSON schema), server-side fallback if the model refuses.
- **What changed:** first version.
- **Key techniques:**
  - one finding per playbook rule — the model does not invent new topics;
  - verbatim quote + clause number → the lawyer can verify;
  - when in doubt — `review`, not a guess;
  - personal data is already masked, placeholders are preserved;
  - Polish law as the frame; foreign law is only flagged.
- **Result on the test set:** ⬜ not run (no API key in the development environment). Baseline — rule-based engine: 10/10 rules match the reference on v1 and v2 (`python3 -m unittest discover -s app/tests`).
- **Next step:** run prompt-v1 on both samples, compare with the reference, record accuracy and errors here.

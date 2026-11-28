# AI Lawyer

A web service that helps review and compare contracts between counterparties.

> Product name: **Klauzula AI** (ADR-0006, proposed) — NDA review against the company playbook and Polish law for in-house lawyers.
> Status: prototype v0.2 (Project Step 3, per the TO-BE process).

## Where things are
| Path | Contents |
|------|----------|
| `docs/00_overview.md` | Product essence and target user |
| `docs/01_requirements.md` | Requirements |
| `docs/02_user_stories.md` | User stories |
| `docs/03_architecture.md` | Architecture |
| `docs/04_ai_prompts.md` | LLM prompts and their versions |
| `docs/05_legal_compliance.md` | GDPR, confidentiality, disclaimers |
| `docs/06_playbook/` | Contract review checklists |
| `docs/07_research.md` | Research: problem, users, competitors in Poland and the EU (Project Step 2) |
| `docs/08_design.md` | Name, visual style, mock-ups (Step 3) |
| `docs/mockups/` | Design pack: process, style, screen mock-ups (HTML) |
| `docs/diagrams/` | Process diagrams (SVG) |
| `skills/nda-review/SKILL.md` | Instructions for the AI (prompt-v1) |
| `app/` | Prototype v0.2: server, review engine, interface, tests |
| `docs/decisions/` | Architecture decisions (ADR) |
| `docs/meetings/` | Meeting and interview notes |
| `CHANGELOG.md` | Change history |
| `CLAUDE.md` | Instructions for Claude on running the project |

## Running the prototype
Only Python 3.9+ is needed (already on macOS), no packages to install.

```bash
python3 app/server.py
```

Open http://localhost:8000 and click **Try the sample NDA**. Then: accept the edits → "Yes — send edits to the counterparty" → "Try sample version 2" (round 2). Stop the server: `Ctrl+C`.

### Public demo (Render)
Link: **https://klauzula-ai.onrender.com** (works on a computer and on a phone; click **Try the sample NDA**).

The demo is deployed from `render.yaml` (Render → New → Blueprint → this repository), region Frankfurt, free plan; every `git push` to `main` updates it. The free instance sleeps after ~15 minutes without visitors — open the link 2–3 minutes before a demo. Details: [ADR-0008](docs/decisions/0008-demo-hosting-render.md).

Tests:

```bash
python3 -m unittest discover -s app/tests
```

### Claude mode (optional)
By default a rule-based review runs (demo, offline). To review through Claude you need Python ≥ 3.10:

```bash
pip3 install anthropic
export ANTHROPIC_API_KEY=...   # do not commit the key
python3 app/server.py
```

"Claude mode" appears in the top right corner. The text is masked before sending (names — by marker words, in the signature block and next to job titles; e-mail, phone numbers, PESEL, NIP, KRS, IBAN).

> Do not upload real confidential contracts — only anonymised examples.

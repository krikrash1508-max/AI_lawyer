# ADR-0008: Public demo hosted on Render (Frankfurt)

- Status: proposed
- Date: 2026-11-28
- Related: [ADR-0004](0004-prototype-stack.md) (prototype stack), [01_requirements.md](../01_requirements.md) NFR-001, NFR-002

## Context
The course assignment requires the solution to be **published under a permanent link**, to work **on another computer and on a phone**, and the live demo to show the main scenario working reliably end to end ("fewer features that work are better than more that fail").

Prototype v0.2 runs only on the author's laptop (`python3 app/server.py`, `localhost:8000`). It is a Python standard-library server (ADR-0004) with no packages; the history of rounds lives in the browser and is passed in each request, so the server keeps no state.

## Options considered
| Option | Pros | Cons |
|--------|------|------|
| **A. Render — Web Service (free)** | Runs `server.py` as is; deploys from the GitHub repo on every `git push`; EU region (Frankfurt); no Dockerfile | Free instance sleeps after ~15 min without visitors, first open takes 30–60 s |
| B. Hugging Face Spaces (Docker) | Free; familiar for AI demos | Needs a `Dockerfile`, port 7860 and a separate Space repository; the Space page shows the app in a frame, awkward on a phone |
| C. Vercel (serverless) | Fast, no sleeping | `server.py` must be split into static files + serverless functions; free plan is for non-commercial use only |
| D. GitHub Pages | Permanent link, no sleeping | Static files only — the Python review engine cannot run |

## Decision
**Option A — Render**, Web Service on the free plan, region **Frankfurt**, configured in `render.yaml` (Blueprint):
- `HOST=0.0.0.0` (server accepts visitors; locally it still listens only on `127.0.0.1`), port from `PORT`;
- `PYTHON_VERSION=3.12.8` (code uses only stable standard-library modules; tested locally on 3.9);
- health check `GET /api/status`; auto-deploy from `main`.
- **Claude mode stays off** in the public demo (no `anthropic` package, no API key): the rule-based scenario works without a key and without a cost per visitor.

## Consequences
- Easier: one permanent link (`*.onrender.com`) for the assignment, phone and other computers; every `git push` to `main` updates the demo.
- NFR-002 (EU hosting) is met for the demo; LLM processing in the EU remains open for Claude mode.
- NFR-001 holds: the server still stores nothing; Render keeps only access logs (URL, time, IP), not contract text.
- The site is public: anyone with the link can upload a file. The on-screen disclaimer already says not to upload real confidential contracts; the demo uses the built-in anonymised samples.
- Risk: sleeping on the free plan — open the link 2–3 minutes before the demo (optionally an uptime ping); fallback — run locally.
- `http.server` is not a production server (ADR-0004). This is acceptable for a course demo; a pilot with real clients still needs FastAPI + EU hosting with a DPA (new ADR).

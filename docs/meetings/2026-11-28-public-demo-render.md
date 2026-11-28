# 2026-11-28 — Public demo on Render: deployment and verification

- Participants: project author, Claude (technical writer)
- Goal: meet the assignment criterion "the solution is published under a permanent link and works on another computer and on a phone; the live demo shows the main features working reliably from start to finish".

## Result
**Permanent link:** https://klauzula-ai.onrender.com — Render Web Service, free plan, region Frankfurt (EU), deployed from `render.yaml`, auto-deploy on every `git push` to `main` ([ADR-0008](../decisions/0008-demo-hosting-render.md)).

## Verification of the main scenario
Scenario: Try the sample NDA → accept edits → "Yes — send edits to the counterparty" → Try sample version 2 (round 2) → export report.

| # | Where | How | Result |
|---|-------|-----|--------|
| 1 | Laptop, local | 12 autotests (`app/tests`) | ✅ all pass |
| 2 | Laptop, local | Browser at phone screen size (375 × 812) | ✅ full scenario, layout in one column, no console errors |
| 3 | Laptop, local network | Server with `HOST=0.0.0.0`, opened via the laptop's network address | ✅ page opens |
| 4 | Render (public link) | API check: round 1 → round 2 → export | ✅ round 1: 6 red flags; round 2: 7 risk changes; Word report 200 OK |
| 5 | Phone, mobile internet | Author opened the link and went through the scenario | ✅ works |

## Key takeaways
- The prototype needed only one code change (bind address from `HOST`); the rest is configuration (`render.yaml`). Choosing a hosting option that runs the server "as is" kept the demo reliable — in line with "fewer features that work are better than more that fail".
- The server stores nothing: the history of rounds lives in the browser, so Render restarts and sleeping do not break the scenario.
- Claude mode is deliberately off in the public demo: no API key on a public server, no cost per visitor, no contract text leaves the server.
- The free instance sleeps after ~15 minutes without visitors; the first open then takes 30–60 s.

## Decisions
- Hosting — Render, Frankfurt ([ADR-0008](../decisions/0008-demo-hosting-render.md)).
- Release 0.5.0, git tag `v0.5.0`.

## Tasks
- [ ] Open the link 2–3 minutes before the live demo (wake the server) — author — before the demo
- [ ] Optional: uptime ping (e.g. UptimeRobot) so the demo does not sleep — author — before the demo
- [ ] Check on another computer (e.g. a classmate's laptop) — author — before the demo
- [ ] Fallback for the demo without internet: `python3 app/server.py` locally — author — before the demo

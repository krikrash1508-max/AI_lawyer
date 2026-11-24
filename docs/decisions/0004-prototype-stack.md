# ADR-0004: Prototype v0.1 stack — Python stdlib + HTML/JS, Claude as an option

- Status: proposed
- Date: 2026-11-24

## Context
A working skeleton (v0.1) is needed for the course. The team's laptop has only Python 3.9; there is no Node.js, Homebrew or pandoc. The team are beginner developers; the prototype must start with one command.

## Options considered
1. Python standard library (`http.server`) + static HTML/CSS/JS; LLM connected optionally.
2. Python + FastAPI/Streamlit — more convenient, but needs package installation and a virtual environment.
3. Next.js / React — modern, but needs Node.js.
4. No-code (Bubble, Softr) — fast, but we cannot show our own engine or control over data.

## Decision
Option 1. The review works in two modes:
- **Demo (default):** regular-expression rules — free, offline, deterministic, covered by tests.
- **Claude:** if the `anthropic` package and a key are available — the same playbook via the Claude API (`claude-opus-5-5`, structured output), instructions in `skills/nda-review/SKILL.md`.

## Consequences
- Easier: `python3 app/server.py` and everything works; the demo does not depend on the internet or keys.
- Harder: `http.server` is not for production; no authentication or storage. For a pilot — move to FastAPI + EU hosting (new ADR).
- Risk: the rule-based mode works well only on "typical" wording; real quality will be shown by the Claude mode on the test set.

---
title: Name, visual style and mock-ups
version: 0.3.1
status: draft
owner: TBD
updated: 2026-11-24
---

# Name, visual style and mock-ups

Interactive version (process, style, screen mock-ups, specification, observations): [`docs/mockups/klauzula-design.html`](mockups/klauzula-design.html) — open in a browser.

> **0.3.0:** the mock-ups were rebuilt around the TO-BE process ([ADR-0007](decisions/0007-scope-v0-2-to-be-process.md)): screens Upload → Report → Decision → Round 2 → Playbook; the Compare tab and the Word add-in screen were removed from the mock-ups; the logo was redrawn as SVG and is used in the prototype; the name "Klauzula AI" appears in all mock-ups and in the interface.

## 1. Name
**Klauzula AI** (Klauzula — Polish for "clause, contract provision"): [ADR-0006](decisions/0006-product-name-klauzula-ai.md), proposed. Supersedes "Klauzula" from ADR-0005.
- Tagline: *Your playbook, every clause.* / *Twój playbook w każdej klauzuli.*
- Logo: a contract sheet with a "§" sign and a line with a check mark, details in [section 4](#4-logo).
- ~~Logo: a "§" sign in a circle — like a seal stamp (pieczątka), no pictures or icons.~~ **Deprecated (0.2.0):** replaced by the generated logo (section 4). A sheet with a checked line shows directly what the product does: it checks contract clauses.
- Tone: calm, precise, no promises to "replace the lawyer". Verbs: check, flag, propose, decide.

## 2. Visual style
Idea: **the lawyer's desk** — the contract sheet on the left, comments on the right, the lawyer's "Any red flags?" decision on top. The contract is set in a serif font (like a document), the interface in sans-serif.

| Token | Colour | Role |
|-------|--------|------|
| `--ink` | `#16213A` | Text, logo |
| `--paper` | `#F2F4F8` | Page background (cool, not cream) |
| `--sheet` | `#FFFFFF` | Contract sheet, cards |
| `--stamp` | `#3A3D9E` | Accent: violet-blue stamp ink |
| `--risk` | `#B42318` | Red flag (semantics, not accent) |
| `--review` | `#A15C07` | Review |
| `--ok` | `#1E7A4F` | OK |
| `--brand-ok` | `#6FD3A0` | Check mark in the logo (brand only, not status) |

| Role | Font | Where |
|------|------|-------|
| Interface | IBM Plex Sans | Buttons, cards, headings |
| Document | IBM Plex Serif | Contract text, quotes, wording |
| Utility | IBM Plex Mono | Clause numbers "§ 4", rule IDs, placeholders `[NAME_1]`, `[EMAIL_1]` |

Rules: the risk colour only for risk (stripe on the left of a card and clause); the accent only for actions, brand and the lawyer's decision block; a legal provision reference is a chip in the `--stamp-soft` colour with the label "Polish law · to verify"; clauses changed since the previous round carry a `modified / added / removed` label and a word-level diff directly in the text; dark theme is supported.

## 3. Screen mock-ups
Screens follow the order of the TO-BE steps ([03_architecture.md](03_architecture.md), section 2). Everything is one "Review contract" screen and a "Playbook" tab.

| # | Screen | TO-BE step | What is on it | In v0.2 |
|---|--------|------------|---------------|---------|
| 1 | Upload | The lawyer uploads the file | "Task from sales / purchasing · round 1", drag-and-drop, paste text, "Try the sample NDA" | ✅ |
| 2 | Report | Masks → analyses → generates the report | Summary (N Red flag / Review / OK, what was masked, including NAME), contract sheet with highlighting, cards: quote, explanation, playbook, **legal provision**, edit with Accept / Reject | ✅ |
| 3 | Decision | Reviews the report → "Any red flags?" | "Your decision" block: number of flags and accepted edits; "No — ready for signing" / "Yes — send edits"; report export; list of edits for the business | ✅ |
| 4 | Round 2 | New version — back to review | "Upload new version" → "Since round 1" block (New risk / Improved), changed clauses in the text | ✅ (replaces the Compare tab) |
| 5 | Playbook | — | Rules table: standard, red flag, **legal provision**, fallback wording | ✅ (view only) |

~~Screen 5 "Word add-in"~~ **removed from the mock-ups (0.3.0):** it is not in the TO-BE diagram. The idea stays in the observations as a direction after the pilot (track changes in .docx).

## 4. Logo
Generated for the course assignment "promo image of the solution". The files are in [`docs/brand/`](brand/).

| File | Variant | Where to use |
|------|---------|--------------|
| [`klauzula-logo-full.webp`](brand/klauzula-logo-full.webp) | Full: symbol and the "Klauzula AI" wordmark | Site header, slides, poster |
| [`klauzula-symbol.png`](brand/klauzula-symbol.png) | Symbol only (244×292 px) | Avatar |
| [`klauzula-mark.svg`](brand/klauzula-mark.svg) | Symbol as a vector (redrawn by hand from the PNG) | Favicon and prototype header (`app/static/favicon.svg`, inline SVG), mock-ups; in dark theme colours come from the tokens |

### Message of the image
Klauzula AI helps in-house lawyers at Polish companies review NDAs faster against the company playbook. Every comment is backed by a quote from the contract, and the decision stays with the lawyer.

### Composition of the mark
| Element | Meaning |
|---------|---------|
| Sheet with a folded corner | The contract |
| "§" | A contract clause, legal context |
| Green line with a check mark | The clause is checked against the playbook |
| Colours | Indigo `#3A3D9E` (`--stamp`) and green `#6FD3A0` (`--ok` of the dark theme) on white |

### Prompt (full logo)
```text
Minimalist flat vector logo for "Klauzula", an AI tool that helps in-house lawyers review contracts (NDAs) faster against their company's rules.

Symbol: a simple geometric mark combining a document page with a folded corner and a section sign "§". One clause line on the page is highlighted with a small check mark, suggesting "clause reviewed". Clean, confident, trustworthy. No gavel, no scales of justice, no robot, no brain, no circuit lines.

Layout: symbol on the left, wordmark on the right, horizontally aligned, generous white space around. Centered on the canvas.

Text: exactly the word "Klauzula" — capital K, the rest lowercase, 8 letters: K-l-a-u-z-u-l-a. Modern geometric sans-serif, medium weight, slightly wide letter spacing. No other text, no slogan.

Colour scheme: deep indigo #3A3D9E as the main colour, a single accent of soft green #6FD3A0 for the check mark, on a plain white background. Maximum 2 colours plus white. No gradients, no shadows, no 3D, no texture.

Style: professional legal-tech / SaaS brand identity, Swiss design, flat vector, crisp edges, works in monochrome and at small sizes (favicon).

The logo must be completely original and must not resemble any existing company logo, trademark, app icon or artwork. Do not imitate any known brand or designer style. Avoid generic stock legal clichés.

Format: square 1:1, 1024x1024, high resolution.
```
Iterations in the same chat: the generator first produced the merged "KlauzulaAI", then "Klauzula AI" with a space. This spelling was adopted in ADR-0006.

### Prompt (symbol only)
```text
Now create a symbol-only version of this logo: just the document icon with "§" and the green check mark, no wordmark, no text. Centered in a square 1:1 canvas, filling about 70% of it, on white background. Keep the same colours and line style. It must stay clear and recognisable at 32x32 px.
```

### Checks before use (commercial use)
| Check | How | Status |
|-------|-----|--------|
| The service's terms allow commercial use | Current Terms of Use of the service and plan; save a screenshot and the date | ⬜ Not checked (tool: TBD) |
| No similarity to other logos | Image search: Google Lens, TinEye | ⬜ |
| No similarity to registered marks | EUIPO eSearch / TMview: by image and by the words "Klauzula AI" | ⬜ |
| Text without distortions | Letter by letter: "Klauzula AI" | ✅ |
| Rights to the image | In the EU an image created by AI alone may not receive copyright protection; for a real brand the logo is better refined with a designer | ⚠️ Noted |

Similarity risk: the combination of "§" and a document sheet is common among legal brands, so an image search is mandatory.

### Open
- A square 1024×1024 symbol for the avatar (the current file is small and not square).
- ~~Variant for the dark theme (background `#11151F`).~~ Resolved in 0.3.0: the SVG symbol takes its colours from the theme tokens.
- Compare the SVG redraw with the original PNG (proportions, line thickness) when choosing the final version.
- Choose the final version by group vote.

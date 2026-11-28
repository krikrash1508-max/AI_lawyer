# ADR-0009: Knowledge base (RAG) — NotebookLM for the lawyer, built-in BM25 search in Klauzula AI

- Status: proposed
- Date: 2026-11-28
- Related: [ADR-0004](0004-prototype-stack.md) (stack), [ADR-0007](0007-scope-v0-2-to-be-process.md) (`legal_basis` from the playbook), [ADR-0008](0008-demo-hosting-render.md) (public demo); [01_requirements.md](../01_requirements.md) NFR-001, NFR-002, NFR-008

## Context
The course assignment requires a **RAG knowledge base on NotebookLM**. NotebookLM has **no API**, so the prototype cannot query it from code. At the same time the lawyer needs, next to each finding, the sources that explain it (law, company playbook), and the public demo must stay reliable ("fewer features that work are better than more that fail").

## Options considered
| Option | Pros | Cons |
|--------|------|------|
| **A. Own keyword search (BM25) inside Klauzula AI** | Python standard library; no keys or external services; works on Render as is; deterministic and testable; no text leaves the server | Matches words, not meaning; shows quotes, does not "reason" |
| B. Gemini API (file search) | Semantic search + generated answer with citations | API key on a public server; free tier may use data for model improvement; rate limits; non-deterministic answers |
| C. Vector database (Qdrant, Pinecone) + embedding model | Industry-standard semantic RAG | Separate embedding model (paid, or too heavy for the free Render instance); 2–3 services and keys |
| D. Self-hosted NotebookLM alternatives (AnythingLLM, Open Notebook) | API and UI | Needs a strong server and its own LLM; does not fit free hosting |
| E. Supabase (Postgres full-text / pgvector), EU region | Real cloud database, useful for a pilot (users, round history); EU region | Free project pauses after ~7 days without requests; second service and keys; built-in embedding model weak for Polish |

## Decision
Two parts working on **one shared source library** `docs/rag/sources/` (law excerpts from official sources — ISAP, EUR-Lex; the NDA playbook in readable form; anonymised samples):
1. **NotebookLM** — the RAG base required by the assignment: a shared notebook where the lawyer asks follow-up questions ("why is this a risk?"). Instructions for the notebook are versioned as a prompt (`notebooklm-v1`) in [04_ai_prompts.md](../04_ai_prompts.md).
2. **Option A** — built-in BM25 search in `app/engine/` over the same library: each finding gets a "Legal sources" block with 2–3 relevant excerpts and their source. To bridge English contract text and Polish statutes, every playbook rule carries keywords in both languages, and the search uses them.

## Consequences
- Easier: the RAG part of the demo works without keys, limits or external services; tests can check which excerpts are returned.
- NFR-001 holds: contract text never leaves the server; only anonymised material is uploaded to NotebookLM (Google).
- NFR-008 holds: excerpts are shown verbatim from the library, nothing is generated.
- Harder: two places use the library — after changing `docs/rag/sources/`, re-upload the files to NotebookLM.
- Limit: no semantic search. For a pilot, revisit B or E (paid tier without training on data, EU processing) in a new ADR.
- Open: the playbook and legal references are not yet checked by a radca prawny.

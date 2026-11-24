"""Claude mode: review clauses against the playbook with an LLM.

Enabled only when the `anthropic` package is installed and credentials are available
(ANTHROPIC_API_KEY or `ant auth login`). Text is masked before it is sent.
Instructions for the model live in skills/nda-review/SKILL.md (prompt-v1 in docs/04_ai_prompts.md).
"""
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SKILL_PATH = ROOT / "skills" / "nda-review" / "SKILL.md"
MODEL = os.environ.get("AI_LAWYER_MODEL", "claude-opus-5-5")

FINDING_SCHEMA = {
    "type": "object",
    "properties": {
        "findings": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "rule_id": {"type": "string"},
                    "level": {"type": "string", "enum": ["risk", "review", "ok"]},
                    "missing": {"type": "boolean"},
                    "clause_ref": {"type": ["string", "null"]},
                    "quote": {"type": "string"},
                    "explanation": {"type": "string"},
                    "suggested_edit": {"type": "string"},
                },
                "required": ["rule_id", "level", "missing", "clause_ref", "quote", "explanation", "suggested_edit"],
                "additionalProperties": False,
            },
        }
    },
    "required": ["findings"],
    "additionalProperties": False,
}


def available():
    try:
        import anthropic  # noqa: F401
    except ImportError:
        return False
    return bool(os.environ.get("ANTHROPIC_API_KEY") or os.environ.get("AI_LAWYER_USE_CLAUDE"))


def _skill_instructions():
    text = SKILL_PATH.read_text(encoding="utf-8")
    # Drop the YAML front matter; the body is the instruction set.
    if text.startswith("---"):
        text = text.split("---", 2)[2]
    return text.strip()


def check(masked_clauses, playbook):
    import anthropic

    client = anthropic.Anthropic()
    system = _skill_instructions() + "\n\n<playbook>\n" + json.dumps(playbook, ensure_ascii=False, indent=1) + "\n</playbook>"
    contract = "\n\n".join(
        '<clause ref="{}" heading="{}">\n{}\n</clause>'.format(c["ref"], c["heading"], c["text"]) for c in masked_clauses
    )
    response = client.beta.messages.create(
        model=MODEL,
        max_tokens=16000,
        betas=["server-side-fallback-2026-07-01"],
        fallbacks="default",
        system=system,
        output_config={"effort": "high", "format": {"type": "json_schema", "schema": FINDING_SCHEMA}},
        messages=[{"role": "user", "content": "<contract>\n" + contract + "\n</contract>\n\nReview this NDA against the playbook. Return one finding per playbook rule."}],
    )
    if response.stop_reason == "refusal":
        raise RuntimeError("The model declined to review this document.")
    text = next(b.text for b in response.content if b.type == "text")
    data = json.loads(text)

    rules_by_id = {r["id"]: r for r in playbook["rules"]}
    headings = {c["ref"]: c["heading"] for c in masked_clauses}
    findings = []
    for f in data["findings"]:
        rule = rules_by_id.get(f["rule_id"])
        if not rule:
            continue  # ignore anything outside the playbook
        f["topic"] = rule["topic"]
        f["standard"] = rule["standard"]
        f["clause_heading"] = headings.get(f["clause_ref"])
        if f["level"] == "ok":
            f["suggested_edit"] = ""
        findings.append(f)
    return findings

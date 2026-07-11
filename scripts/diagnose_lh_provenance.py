#!/usr/bin/env python3
"""Replay and classify the frozen v8/v10 LH provenance failures.

This diagnostic does not alter historical artifacts or scores. Counterfactuals are
builder-authored calibration cases evaluated in temporary files only.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import tempfile
from pathlib import Path
from typing import cast

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.grade_lh_evidence import grade

PILOT = ROOT / "pilots/lh-skill-adoption"
ABLATION = PILOT / "ablation"
SOURCE = PILOT / "source-pack/decision-evidence.csv"
TASK = ABLATION / "agent-attempts-20260710/no_skill_01/task.md"
SKILL = PILOT / "public-skill.md"
GRADER = ROOT / "scripts/grade_lh_evidence.py"
ARMS = tuple((pair, arm) for pair in ("isolated-agent-pair-v8", "isolated-agent-pair-v10") for arm in ("no-skill", "public-skill"))
DIAGNOSTIC_RE = re.compile(r"^(?P<code>[^|]+) \| (?P<location>[^|]+) \| (?P<message>.*)$")
PAREN_CITATION_RE = re.compile(r"\((E\d{2}(?:\s*,\s*E\d{2})+)\)")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def classify(code: str, location: str, message: str) -> tuple[str, str]:
    if code == "UNCITED_MATERIAL_CLAIM" and "recommendation" in location:
        return "artifact_convention_mismatch", "The memo has numeric text but no grader-recognized square-bracket citation on that line."
    if code == "UNSUPPORTED_NUMERIC_VALUE" and "evidence-matrix" in location:
        return "artifact_realization", "A matrix row binds a numeric claim to one evidence row whose reported_value does not contain that token."
    if code == "UNSUPPORTED_NUMERIC_VALUE" and "recommendation" in location:
        return "grader_scope_false_rejection_candidate", "The lexical grader cannot distinguish sourced measurements from builder-proposed thresholds, counts, dates, or design parameters."
    return "unresolved", message


def diagnose() -> dict[str, object]:
    frozen = [TASK, SKILL, GRADER, SOURCE]
    cases: list[dict[str, object]] = []
    totals: dict[str, int] = {}
    for pair, arm in ARMS:
        base = ABLATION / pair / arm
        matrix = base / "trial/outputs/evidence-matrix.csv"
        memo = base / "trial/outputs/recommendation.md"
        record = base / "grader-results/evidence-link-grader.json"
        frozen.extend((matrix, memo, record))
        replay = grade(SOURCE, matrix, memo)
        original = json.loads(record.read_text(encoding="utf-8"))
        replay_evidence = cast(list[str], replay["evidence"])
        original_evidence = cast(list[str], original["evidence"])
        if replay["outcome"] != original["outcome"] or replay_evidence != original_evidence:
            raise ValueError(f"historical replay mismatch: {pair}/{arm}")
        diagnostics = []
        for rendered in replay_evidence:
            match = DIAGNOSTIC_RE.match(str(rendered))
            if not match:
                raise ValueError(f"unparseable diagnostic: {rendered}")
            category, explanation = classify(**match.groupdict())
            totals[category] = totals.get(category, 0) + 1
            diagnostics.append({**match.groupdict(), "category": category, "explanation": explanation})

        memo_text = memo.read_text(encoding="utf-8")
        bracketed = PAREN_CITATION_RE.sub(lambda m: f"[{m.group(1)}]", memo_text)
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_memo = Path(temp_dir) / "recommendation.md"
            temp_memo.write_text(bracketed, encoding="utf-8")
            counterfactual = grade(SOURCE, matrix, temp_memo)
        cases.append({
            "case_id": f"{pair}/{arm}",
            "historical_outcome": original["outcome"],
            "replay_exact": True,
            "diagnostics": diagnostics,
            "counterfactual_parentheses_to_brackets": {
                "kind": "builder_authored_calibration_only",
                "changed": bracketed != memo_text,
                "outcome": counterfactual["outcome"],
                "diagnostic_count": 0 if counterfactual["outcome"] == "passed" else len(cast(list[str], counterfactual["evidence"])),
            },
        })

    return {
        "schema_version": "0.1.0",
        "analysis_kind": "frozen_exact_version_root_cause_diagnostic",
        "claims_prohibited": ["Skill efficacy", "professional validity", "agent capability", "release readiness"],
        "predeclaration": {
            "hypotheses": [
                {"id": "H1_agent_omission", "expected": "square-bracket syntax is disclosed and examples are available, but the agent omits links"},
                {"id": "H2_instruction_insufficiency", "expected": "public task/Skill request evidence IDs but do not disclose the grader's exact square-bracket-only syntax or threshold-number policy"},
                {"id": "H3_artifact_convention_mismatch", "expected": "semantically recognizable parenthetical or ranged evidence IDs fail lexical parsing"},
                {"id": "H4_grader_false_rejection", "expected": "prospective governance numbers, dates, design counts, or legitimate alternate citation forms are rejected despite not being source-derived factual claims"},
            ],
            "instrument_change_permitted": False,
            "new_agent_calls_permitted": False,
        },
        "frozen_files": [{"path": rel(path), "bytes": path.stat().st_size, "sha256": sha256(path)} for path in sorted(set(frozen))],
        "cases": cases,
        "diagnostic_category_counts": dict(sorted(totals.items())),
        "conclusions": {
            "supported": [
                "H2: neither task nor public Skill discloses the square-bracket-only parser convention or how prospective numeric decision rules must be represented.",
                "H3: v10 no-skill uses conventional parenthetical evidence IDs that are human-recognizable but parser-invisible; bracket-only counterfactual replay separates syntax from absent provenance.",
                "H4: the grader applies source-value matching to every numeric memo line, including prospective thresholds, sample-design counts, dates, and confidence levels; these are not all source-derived claims.",
            ],
            "partially_supported": ["H1: some rows genuinely bind a numeric claim to the wrong single evidence row, but recurrent whole-memo failure cannot be assigned to omission alone."],
            "unresolved": ["Whether a revised convention improves future agent behavior; a fresh frozen validation is required.", "Semantic entailment and professional adequacy remain outside this lexical grader."],
        },
        "minimal_versioned_correction": {
            "recommendation": "Version the public artifact contract and grader together: disclose accepted [E##] syntax and add an explicit machine-readable marker for prospective program-set numbers that the provenance grader abstains on rather than treating as source measurements.",
            "fresh_validation_gate": "Before another agent trial, add positive/negative conformance cases for bracketed groups, conventional parenthetical IDs, ranges, dates, prospective thresholds, mixed sourced/prospective lines, and wrong-row numeric attribution; require independent review of abstention boundaries and preserve all v8/v10 scores unchanged.",
            "historical_rescore_permitted": False,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = diagnose()
    text = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

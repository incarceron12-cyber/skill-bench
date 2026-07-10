#!/usr/bin/env python3
"""Audit retained LH pilot agent attempts without upgrading invalid runs.

The 2026-07-10 Hermes attempts exposed a harness-root defect: although launched
from temporary workspaces, file tools resolved from /home/sam and exposed the
repository. This audit hashes the retained evidence, reruns only post-hoc
internal graders, and deterministically keeps capability_evidence false when
trace isolation or artifact location fails.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.grade_lh_claims import grade as grade_claims
from scripts.grade_lh_evidence import grade as grade_evidence

PILOT = ROOT / "pilots/lh-skill-adoption"
ATTEMPTS = PILOT / "ablation/agent-attempts-20260710"
REPORT = ATTEMPTS / "audit-report.json"
CONDITIONS = ("no_skill_01", "public_skill_01")
EXPECTED_TASK_CWD = "/tmp/lh-genuine"
PRIVATE_MARKERS = (
    "rubric-skeleton.json",
    "independent-claim-rubric.json",
    "calibration/passing",
    "calibration/agreement-overclaim",
    "calibration/tiny-ablation-overclaim",
)


def _hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _relative(path: Path) -> str:
    return path.resolve().relative_to(ROOT).as_posix()


def _ref(path: Path) -> dict[str, Any]:
    return {"path": _relative(path), "sha256": _hash(path), "bytes": path.stat().st_size}


def _write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _trace_audit(path: Path, condition: str) -> dict[str, Any]:
    records = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    observed_cwds = sorted({str(item.get("cwd")) for item in records if item.get("cwd")})
    trace_text = path.read_text(encoding="utf-8")
    markers = list(PRIVATE_MARKERS)
    if condition == "no_skill_01":
        markers.append("public-skill.md")
    exposed = sorted(marker for marker in markers if marker in trace_text)

    broad_searches: list[dict[str, str]] = []
    for item in records:
        message = item.get("message", {})
        for content in message.get("content", []) if isinstance(message, dict) else []:
            if not isinstance(content, dict) or content.get("type") != "tool_use":
                continue
            if content.get("name") != "search_files":
                continue
            tool_input = content.get("input", {})
            search_path = str(tool_input.get("path", ""))
            if search_path in {".", "skill-bench", "skill-bench/pilots/lh-skill-adoption"}:
                broad_searches.append({"path": search_path, "pattern": str(tool_input.get("pattern", ""))})

    cwd_isolated = bool(observed_cwds) and all(value.startswith(EXPECTED_TASK_CWD) for value in observed_cwds)
    return {
        "observed_cwds": observed_cwds,
        "cwd_isolated": cwd_isolated,
        "private_or_treatment_markers_exposed": exposed,
        "broad_repository_searches": broad_searches,
        "isolation_passed": cwd_isolated and not exposed and not broad_searches,
    }


def build() -> dict[str, Any]:
    source = PILOT / "source-pack/decision-evidence.csv"
    claim_config = PILOT / "graders/independent-claim-rubric.json"
    prompt_hashes: list[str] = []
    attempts: list[dict[str, Any]] = []

    for condition in CONDITIONS:
        trial = ATTEMPTS / condition
        prompt = trial / "task.md"
        matrix = trial / "outputs/evidence-matrix.csv"
        memo = trial / "outputs/recommendation.md"
        usage_path = trial / "usage.json"
        trace_path = trial / "session-trace.jsonl"
        transcript_path = trial / "transcript.log"
        prompt_hashes.append(_hash(prompt))

        evidence = grade_evidence(source, matrix, memo)
        claims = grade_claims(claim_config, matrix, memo)
        evidence_path = trial / "grader-results/evidence-link-grader.json"
        claim_path = trial / "grader-results/independent-claim-calibrator.json"
        _write_json(evidence_path, evidence)
        _write_json(claim_path, {"results": claims})

        usage = json.loads(usage_path.read_text(encoding="utf-8"))
        trace_audit = _trace_audit(trace_path, condition)
        valid_environment = trace_audit["isolation_passed"]
        attempts.append({
            "condition_id": condition,
            "skill_visible_by_design": condition.startswith("public_skill"),
            "valid_environment": valid_environment,
            "capability_evidence": False,
            "invalid_reasons": [
                "Hermes file tools resolved from /home/sam rather than the requested temporary trial workspace.",
                "Repository-wide searches exposed grader, calibration, or treatment-adjacent filenames outside the allowed source pack.",
                "Agent artifacts were written to /home/sam/outputs and had to be retained post hoc; the launch wrapper did not enforce the artifact root.",
            ] if not valid_environment else [],
            "usage": {
                key: usage[key]
                for key in ("model", "provider", "session_id", "input_tokens", "output_tokens", "reasoning_tokens", "total_tokens", "api_calls", "estimated_cost_usd", "cost_status", "completed", "failed")
            },
            "trace_audit": trace_audit,
            "artifacts": {
                "prompt": _ref(prompt),
                "matrix": _ref(matrix),
                "memo": _ref(memo),
                "usage": _ref(usage_path),
                "trace": _ref(trace_path),
                "transcript": _ref(transcript_path),
                "evidence_grader_result": _ref(evidence_path),
                "claim_grader_result": _ref(claim_path),
            },
            "grader_outcomes": {
                str(evidence["check_id"]): str(evidence["outcome"]),
                **{str(item["check_id"]): str(item["outcome"]) for item in claims},
            },
        })

    report = {
        "schema_version": "0.1.0",
        "run_kind": "invalid_agent_attempt_audit",
        "capability_evidence": False,
        "condition_effect_permitted": False,
        "task_prompt_matched": len(set(prompt_hashes)) == 1,
        "attempts": attempts,
        "invalid_concurrent_launch": {
            "path": _relative(ATTEMPTS / "invalid-concurrent-collision"),
            "reason": "Two initial sessions wrote concurrently to the same unexpected /home/sam/outputs root, so the retained output pair is unattributable and excluded from grading.",
        },
        "interpretation": [
            "These are genuine model executions but invalid benchmark trials because environment isolation failed.",
            "Both retained sequential outputs passed the internal claim-boundary calibrator and failed the deterministic evidence-link grader; this is diagnostic grader evidence only.",
            "No skill effect, rubric effect, professional-capability claim, or release-gate change is permitted.",
        ],
        "continuation_gate": "A future launcher must prove task-scoped cwd/input/output confinement with a canary smoke test before any additional model call, then run a fresh matched pair with traces and no repository visibility.",
    }
    if report["task_prompt_matched"] is not True:
        raise ValueError("condition prompts are not hash-matched")
    if any(item["capability_evidence"] for item in attempts) or report["capability_evidence"]:
        raise ValueError("invalid attempts cannot be upgraded to capability evidence")
    _write_json(REPORT, report)
    return report


def main() -> int:
    report = build()
    print(json.dumps({
        "report": _relative(REPORT),
        "capability_evidence": report["capability_evidence"],
        "task_prompt_matched": report["task_prompt_matched"],
        "attempts": {
            item["condition_id"]: {
                "valid_environment": item["valid_environment"],
                "grader_outcomes": item["grader_outcomes"],
            }
            for item in report["attempts"]
        },
    }, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Materialize and grade the LH pilot's matched 2x2 task-only preflight.

This runner deliberately replays one builder-authored cautious fixture in every
condition. It verifies component pinning, artifact materialization, and grader
selection; it does not execute an agent and cannot estimate a skill or rubric
effect. Shared-rubric human checks remain explicitly unexecuted.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.grade_lh_claims import grade as grade_claims
from scripts.grade_lh_evidence import grade as grade_evidence
PILOT = ROOT / "pilots/lh-skill-adoption"
DEFAULT_OUTPUT = PILOT / "ablation/preflight"
SCHEMA = ROOT / "schemas/ablation-preflight.schema.json"
CONDITIONS = (
    "no_skill_independent_rubric",
    "no_skill_shared_rubric",
    "public_skill_independent_rubric",
    "public_skill_shared_rubric",
)


def _hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _relative(path: Path) -> str:
    return path.resolve().relative_to(ROOT).as_posix()


def _file_ref(path: Path) -> dict[str, Any]:
    return {"path": _relative(path), "sha256": _hash(path), "bytes": path.stat().st_size}


def _component(component_id: str, version: str, path: Path) -> dict[str, str]:
    return {"component_id": component_id, "version": version, "sha256": _hash(path), "path": _relative(path)}


def _write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def build(output_root: Path = DEFAULT_OUTPUT) -> dict[str, Any]:
    if not output_root.is_absolute():
        output_root = ROOT / output_root
    try:
        output_root.resolve().relative_to(ROOT)
    except ValueError as exc:
        raise ValueError("output root must stay inside the repository") from exc

    bundle_path = PILOT / "benchmark-bundle.json"
    bundle = json.loads(bundle_path.read_text(encoding="utf-8"))
    skill_record = bundle["procedural_skills"][0]
    rubrics = {item["relationship_to_skill"]: item for item in bundle["rubrics"]}
    fixture = PILOT / "calibration/passing"
    source = PILOT / "source-pack/decision-evidence.csv"
    evidence_config = PILOT / "graders/evidence-link-grader.json"
    claim_config = PILOT / "graders/independent-claim-rubric.json"

    components = {
        "task": _component(bundle["task"]["task_id"], bundle["task"]["version"], bundle_path),
        "skill": _component(skill_record["skill_id"], skill_record["version"], ROOT / skill_record["content_path"]),
        "independent_rubric": _component(rubrics["independent"]["rubric_id"], rubrics["independent"]["version"], claim_config),
        "shared_rubric": _component(rubrics["shared_expert_model"]["rubric_id"], rubrics["shared_expert_model"]["version"], PILOT / "rubric-skeleton.json"),
        "tool_interface": _component("lh-local-filesystem-interface", "0.1.0", PILOT / "ablation/filesystem-tool-interface.json"),
        "harness": _component("lh-fixture-replay-harness", "0.1.0", PILOT / "ablation/fixture-replay-harness.json"),
        "feedback_policy": _component("lh-no-agent-feedback-policy", "0.1.0", PILOT / "ablation/no-feedback-policy.json"),
    }

    condition_records: list[dict[str, Any]] = []
    for condition_id in CONDITIONS:
        condition_dir = output_root / condition_id
        matrix = condition_dir / "outputs/evidence-matrix.csv"
        memo = condition_dir / "outputs/recommendation.md"
        matrix.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(fixture / "evidence-matrix.csv", matrix)
        shutil.copyfile(fixture / "recommendation.md", memo)

        evidence_result = grade_evidence(source, matrix, memo)
        evidence_path = condition_dir / "grader-results/evidence-link-grader.json"
        _write_json(evidence_path, evidence_result)
        grader_runs = [{
            "grader_id": "evidence-link-grader",
            "result_path": _relative(evidence_path),
            "result_sha256": _hash(evidence_path),
            "outcomes": {str(evidence_result["check_id"]): str(evidence_result["outcome"])},
        }]

        independent = condition_id.endswith("independent_rubric")
        unexecuted = ["decision-operability"]
        rubric = components["independent_rubric"] if independent else components["shared_rubric"]
        if independent:
            claim_results = grade_claims(claim_config, matrix, memo)
            claim_path = condition_dir / "grader-results/independent-claim-calibrator.json"
            _write_json(claim_path, {"results": claim_results})
            grader_runs.append({
                "grader_id": "independent-claim-calibrator",
                "result_path": _relative(claim_path),
                "result_sha256": _hash(claim_path),
                "outcomes": {str(item["check_id"]): str(item["outcome"]) for item in claim_results},
            })
        else:
            unexecuted.extend(["contradiction-reconciliation", "causal-claim-strength"])

        condition_records.append({
            "condition_id": condition_id,
            "skill": None if condition_id.startswith("no_skill_") else components["skill"],
            "rubric": rubric,
            "matrix": _file_ref(matrix),
            "memo": _file_ref(memo),
            "grader_runs": grader_runs,
            "unexecuted_checks": unexecuted,
            "interpretation": "plumbing_preflight_only_no_condition_effect",
        })

    report = {
        "schema_version": "0.1.0",
        "run_kind": "task_only_fixture_replay",
        "capability_evidence": False,
        "bundle_source": _file_ref(bundle_path),
        "fixture_source": {
            "authorship": "builder_authored_calibration_fixture_not_agent_output",
            "matrix": _file_ref(fixture / "evidence-matrix.csv"),
            "memo": _file_ref(fixture / "recommendation.md"),
        },
        "components": components,
        "conditions": condition_records,
        "matched_controls": {
            "same_task_hash": True,
            "same_fixture_hashes": True,
            "same_tool_hash": True,
            "same_harness_hash": True,
            "same_feedback_policy_hash": True,
            "only_treatments": ["procedural_skill_visibility", "rubric_relationship"],
        },
        "limitations": [
            "The replayed artifacts are builder-authored calibration fixtures, not agent outputs.",
            "Identical artifacts across conditions prove packaging parity but cannot estimate a skill or rubric effect.",
            "Shared-rubric contradiction, causal, decision, and all expert checks remain unexecuted pending qualified human review.",
            "The independent calibrator is deterministic and internally authored, not blinded independent human adjudication.",
        ],
    }
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    Draft202012Validator(schema, format_checker=FormatChecker()).validate(report)
    _write_json(output_root.parent / "preflight-report.json", report)
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-root", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    report = build(args.output_root)
    print(json.dumps({
        "report": _relative((args.output_root if args.output_root.is_absolute() else ROOT / args.output_root).parent / "preflight-report.json"),
        "conditions": len(report["conditions"]),
        "capability_evidence": report["capability_evidence"],
        "grader_outcomes": {
            item["condition_id"]: {key: value for run in item["grader_runs"] for key, value in run["outcomes"].items()}
            for item in report["conditions"]
        },
    }, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

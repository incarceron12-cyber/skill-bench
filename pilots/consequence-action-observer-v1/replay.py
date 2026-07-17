#!/usr/bin/env python3
"""Validate frozen action-observer artifacts and replay retained v2 outputs once."""
from __future__ import annotations

import hashlib
import importlib.util
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V2 = ROOT / "pilots/analytical-hypothesis-lifecycle-v2"


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dump(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def validate_snapshot(manifest: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for group in ("frozen_components", "v2_immutable_snapshot"):
        for ref in manifest[group]:
            path = ROOT / ref["path"]
            if not path.is_file() or sha(path) != ref["sha256"]:
                errors.append(f"missing or changed frozen artifact: {ref['path']}")
    if any(manifest.get("claim_ceiling", {}).values()):
        errors.append("claim ceiling upgrade")
    return errors


def validate_matrix(matrix: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    fields = set(matrix["required_semantic_fields"])
    cases = matrix.get("cases", [])
    ids = [case.get("case_id") for case in cases]
    if len(cases) != 12 or len(ids) != len(set(ids)):
        errors.append("matrix must contain twelve unique cases")
    if Counter(case.get("split") for case in cases) != {"calibration": 6, "test": 6}:
        errors.append("matrix split drift")
    texts = defaultdict(set)
    for case in cases:
        missing = fields - set(case)
        if missing:
            errors.append(f"missing semantic fields for {case.get('case_id')}: {sorted(missing)}")
        texts[case.get("split")].add(" ".join(case.get("text", "").lower().split()))
        if case.get("expected_disposition") not in {"pass", "fail", "insufficient_evidence", "invalid_evaluator"}:
            errors.append(f"invalid label: {case.get('case_id')}")
        rationale = case.get("source_rationale")
        if rationale not in matrix.get("rule_basis", {}):
            errors.append(f"missing rule basis: {case.get('case_id')}")
    if texts["calibration"] & texts["test"]:
        errors.append("calibration/test text leakage")
    if any(matrix.get("claim_ceiling", {}).values()):
        errors.append("matrix claim ceiling upgrade")
    return errors


def evaluate(expected: str, observed: str) -> tuple[bool, bool, bool]:
    false_accept = expected != "pass" and observed == "pass"
    false_reject = expected == "pass" and observed == "fail"
    abstention = observed == "insufficient_evidence"
    return false_accept, false_reject, abstention


def replay() -> dict[str, Any]:
    spec = importlib.util.spec_from_file_location("frozen_consequence_observer", HERE / "observer.py")
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load frozen observer")
    observer_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(observer_module)
    observe = observer_module.observe

    manifest = load(HERE / "manifest.json")
    matrix = load(HERE / "matrix.json")
    adjudications = load(HERE / "stress-set-adjudications.json")
    errors = validate_snapshot(manifest) + validate_matrix(matrix)

    conformance = []
    for case in matrix["cases"]:
        observation = observe(case["text"])
        fa, fr, abstain = evaluate(case["expected_disposition"], observation["disposition"])
        conformance.append({
            "case_id": case["case_id"], "split": case["split"], "family": case["family"],
            "expected": case["expected_disposition"], "observed": observation["disposition"],
            "matched": case["expected_disposition"] == observation["disposition"],
            "false_accept": fa, "false_reject": fr, "abstention": abstain,
            "criteria": observation["criteria"],
        })
    if not all(row["matched"] for row in conformance):
        errors.append("frozen conformance label mismatch")

    stress = []
    for label in adjudications["rows"]:
        attempt_id = label["attempt_id"]
        output_path = V2 / "execution" / attempt_id / "trial/outputs/analysis.json"
        old_report_path = V2 / "execution" / attempt_id / "trial-report.json"
        output = load(output_path)
        old = load(old_report_path)["stage_observers"]["authorized_consequence"]
        observation = observe(output["recommended_consequence"])
        fa, fr, abstain = evaluate(label["expected_disposition"], observation["disposition"])
        stress.append({
            "attempt_id": attempt_id, "family": label["family"],
            "input_path": output_path.relative_to(ROOT).as_posix(), "input_sha256": sha(output_path),
            "recommended_consequence": output["recommended_consequence"],
            "adjudicated_expected": label["expected_disposition"],
            "old_v2_observer": {"state": old["state"], "denominator": old["denominator"], "numerator": old["numerator"]},
            "descendant_observer": observation,
            "false_accept": fa, "false_reject": fr, "abstention": abstain,
        })

    by_family: dict[str, Any] = {}
    for family in sorted({row["family"] for row in stress}):
        rows = [row for row in stress if row["family"] == family]
        by_family[family] = {
            "rows": len(rows),
            "false_accepts": sum(row["false_accept"] for row in rows),
            "false_rejects": sum(row["false_reject"] for row in rows),
            "abstentions": sum(row["abstention"] for row in rows),
            "dispositions": dict(Counter(row["descendant_observer"]["disposition"] for row in rows)),
        }
    if len(stress) != 8:
        errors.append("stress replay denominator drift")

    return {
        "kind": "consequence_action_observer_v1_replay",
        "passed": not errors,
        "errors": errors,
        "model_calls": 0,
        "historical_v2_mutated": False,
        "historical_v2_consequence_denominator": 0,
        "conformance_summary": {
            "rows": len(conformance), "matched": sum(row["matched"] for row in conformance),
            "false_accepts": sum(row["false_accept"] for row in conformance),
            "false_rejects": sum(row["false_reject"] for row in conformance),
            "abstentions": sum(row["abstention"] for row in conformance),
        },
        "conformance_rows": conformance,
        "stress_summary_by_family": by_family,
        "stress_rows": stress,
        "claim_ceiling": manifest["claim_ceiling"],
    }


def main() -> int:
    report = replay()
    dump(HERE / "replay-report.json", report)
    print(json.dumps({
        "passed": report["passed"], "errors": report["errors"],
        "conformance_summary": report["conformance_summary"],
        "stress_summary_by_family": report["stress_summary_by_family"],
        "model_calls": 0,
    }, indent=2, sort_keys=True))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

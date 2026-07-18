#!/usr/bin/env python3
"""Audit retained v3 generation attempts without repairing candidate bytes."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scripts.validate_procedure_generation_output import validate_documents

HERE = Path(__file__).resolve().parent
CLAIMS = {
    "expert_provenance", "professional_validity", "transfer", "agent_capability",
    "utility", "production_fitness", "readiness",
}
FAMILIES = {
    "family-gamma": (
        HERE / "families/capacity-apportionment/corpus.json",
        HERE / "generation-policies/family-gamma.json",
    ),
    "family-delta": (
        HERE / "families/dependency-release/corpus.json",
        HERE / "generation-policies/family-delta.json",
    ),
}
PROHIBITED_DIRS = ("controls", "checkers", "treatments", "assignments", "executions", "trials")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def audit(base: Path = HERE) -> dict[str, Any]:
    errors: list[str] = []
    observations: dict[str, Any] = {}
    generation = base / "generation"
    actual_families = {path.name for path in generation.iterdir() if path.is_dir()} if generation.exists() else set()
    if actual_families != set(FAMILIES):
        errors.append("generation inventory must contain exactly the two predeclared families")
    for dirname in PROHIBITED_DIRS:
        if (base / dirname).exists():
            errors.append(f"downstream directory exists after failed gate: {dirname}")

    for family_id, (source_path, policy_path) in FAMILIES.items():
        attempt = generation / family_id
        try:
            report_path = attempt / "report.json"
            package_path = attempt / "outputs/package.json"
            usage_path = attempt / "outputs/usage.json"
            report = json.loads(report_path.read_text(encoding="utf-8"))
            package_bytes = package_path.read_bytes()
            package = json.loads(package_bytes)
            source_bytes = source_path.read_bytes()
            source = json.loads(source_bytes)
            policy = json.loads(policy_path.read_text(encoding="utf-8"))
            usage = json.loads(usage_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{family_id}: retained attempt unreadable: {exc}")
            continue

        validation_errors = validate_documents(package, package_bytes, source, source_bytes, policy, report)
        if report.get("package_sha256") != sha256(package_path):
            errors.append(f"{family_id}: package hash drift")
        if report.get("source_corpus_sha256") != sha256(source_path):
            errors.append(f"{family_id}: source hash drift")
        if report.get("policy_sha256") != sha256(policy_path):
            errors.append(f"{family_id}: policy hash drift")
        if report.get("generation_attempts") != 1 or report.get("model_attempts") != 1 or report.get("provider_attempts") != 1:
            errors.append(f"{family_id}: attempt count is not exactly one")
        if report.get("repair_attempts") != 0 or report.get("executor_attempts") != 0:
            errors.append(f"{family_id}: repair or executor attempt occurred")
        if set(report.get("claim_ceiling", {})) != CLAIMS or any(report.get("claim_ceiling", {}).values()):
            errors.append(f"{family_id}: claim ceiling drift")
        if report.get("launcher_valid") is not (not validation_errors and report.get("returncode") == 0):
            errors.append(f"{family_id}: launcher verdict disagrees with independent validation")
        if usage.get("completed") is not True or usage.get("failed") is not False:
            errors.append(f"{family_id}: provider usage does not record a completed call")
        if report.get("output_inventory", {}).get("package.json", {}).get("sha256") != sha256(package_path):
            errors.append(f"{family_id}: output inventory does not bind candidate bytes")
        observations[family_id] = {
            "package_sha256": sha256(package_path),
            "launcher_returncode": report.get("returncode"),
            "launcher_valid": report.get("launcher_valid"),
            "independent_validation": "valid" if not validation_errors else "invalid",
            "validation_errors": validation_errors,
            "usage": {
                "api_calls": usage.get("api_calls"),
                "input_tokens": usage.get("input_tokens"),
                "output_tokens": usage.get("output_tokens"),
                "reasoning_tokens": usage.get("reasoning_tokens"),
                "total_tokens": usage.get("total_tokens"),
                "estimated_cost_usd": usage.get("estimated_cost_usd"),
                "cost_status": usage.get("cost_status"),
            },
            "attempts": {"generation": 1, "model": 1, "provider": 1, "repair": 0, "executor": 0},
        }

    both_valid = len(observations) == 2 and all(row["independent_validation"] == "valid" for row in observations.values())
    return {
        "audit_status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "generation_gate": "pass" if both_valid else "fail",
        "study_status": "candidates_frozen" if both_valid else "blocked_invalid_generated_candidates",
        "observations": observations,
        "aggregate_attempts": {"generation": 2, "model": 2, "provider": 2, "repair": 0, "executor": 0},
        "downstream_authorized": both_valid and not errors,
        "claim_boundaries": {claim: False for claim in sorted(CLAIMS)},
        "interpretation": (
            "The audit verifies immutable retention and fail-closed adjudication only. "
            "A failed generation gate forbids controls, checkers, assignment, or execution and licenses no transfer or capability claim."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    result = audit()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.report:
        args.report.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0 if result["audit_status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())

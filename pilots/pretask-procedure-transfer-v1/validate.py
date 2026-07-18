#!/usr/bin/env python3
"""Validate the fail-closed pre-task procedure-transfer feasibility record."""
from __future__ import annotations
import argparse
import copy
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
REQUIRED_TREATMENTS = {
    "no_package_no_raw", "equal_budget_raw", "generated_package",
    "generated_plus_raw", "reference_procedure", "irrelevant_package",
    "defective_package", "task_conditioned_hindsight",
}
CLAIMS = {
    "expertise", "general_skill_efficacy", "professional_validity",
    "cross_domain_transfer", "utility", "production_fitness", "readiness",
    "agent_capability",
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate(protocol: dict[str, Any], report: dict[str, Any], *, check_paths: bool = True) -> list[str]:
    errors: list[str] = []
    if protocol.get("status") != "frozen_infeasible_before_calls":
        errors.append("protocol must remain frozen infeasible")
    treatments = {row.get("condition_id") for row in protocol.get("treatments", [])}
    if treatments != REQUIRED_TREATMENTS:
        errors.append("required eight-arm treatment set drift")
    families = protocol.get("candidate_families", [])
    if len(families) != 2 or any(len(f.get("forms", [])) != 2 for f in families):
        errors.append("candidate inventory must remain two families x two forms")
    if any(f.get("family_level_source_authority") is not None for f in families):
        errors.append("v1 must not invent a family source authority")
    if any(f.get("eligible_for_transfer") is not False for f in families):
        errors.append("ineligible candidate family upgraded")
    for family in families:
        for form in family.get("forms", []):
            if form.get("untouched_model_execution") is not True:
                errors.append(f"untouched status drift: {form.get('form_id')}")
            if form.get("public_task_discloses_complete_procedure") is not True:
                errors.append(f"public procedure-overlap finding removed: {form.get('form_id')}")
    split = protocol.get("source_and_task_split", {})
    if split.get("current_gate") != "fail":
        errors.append("source/task split must fail closed")
    claims = protocol.get("claim_boundaries", {})
    if set(claims) != CLAIMS or any(value is not False for value in claims.values()):
        errors.append("protocol claim ceiling drift")
    if set(report.get("claim_boundaries", {})) != CLAIMS or any(report.get("claim_boundaries", {}).values()):
        errors.append("report claim ceiling drift")
    if report.get("status") != "blocked_before_model_calls" or report.get("model_calls") != 0 or report.get("provider_attempts") != 0:
        errors.append("report must preserve zero-call blocker")
    inventory = report.get("candidate_inventory", {})
    if inventory.get("untouched_exact_forms") != 4 or inventory.get("eligible_transfer_forms") != 0:
        errors.append("feasibility denominator drift")
    gates = {row.get("gate"): row.get("status") for row in report.get("gate_results", [])}
    if gates.get("independent_family_source_authority_exists") != "fail" or gates.get("public_tasks_do_not_disclose_complete_source_procedure") != "fail":
        errors.append("decisive source-treatment gates must remain failed")
    scrub = protocol.get("leakage_scrubs", {})
    forbidden = set(scrub.get("forbidden_in_pretask_generation_inputs_and_package", []))
    form_ids = {form["form_id"] for family in families for form in family["forms"]}
    if not form_ids <= forbidden or "outputs/decision.json" not in forbidden:
        errors.append("task-ID/output-name scrub coverage drift")
    if check_paths:
        for component in protocol.get("frozen_candidate_components", []):
            path = ROOT / component.get("path", "")
            if not path.is_file():
                errors.append(f"missing component: {component.get('path')}")
            elif sha(path) != component.get("sha256"):
                errors.append(f"hash drift: {component.get('path')}")
        for role in ("launcher", "grader"):
            binding = protocol.get("identities", {}).get(role, {})
            path = ROOT / binding.get("path", "")
            if not path.is_file() or sha(path) != binding.get("sha256"):
                errors.append(f"{role} identity/hash drift")
    return errors


def mutation_self_test(protocol: dict[str, Any], report: dict[str, Any]) -> list[str]:
    cases = []
    p = copy.deepcopy(protocol); p["treatments"] = p["treatments"][:-1]
    cases.append(("missing treatment", p, report))
    p = copy.deepcopy(protocol); p["claim_boundaries"]["utility"] = True
    cases.append(("claim upgrade", p, report))
    p = copy.deepcopy(protocol); p["candidate_families"][0]["eligible_for_transfer"] = True
    cases.append(("eligibility laundering", p, report))
    p = copy.deepcopy(protocol); p["leakage_scrubs"]["forbidden_in_pretask_generation_inputs_and_package"].remove("er-adoption-v1")
    cases.append(("task ID scrub removal", p, report))
    failures = [name for name, p, r in cases if not validate(p, r, check_paths=False)]
    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check-paths", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    protocol = json.loads((HERE / "protocol.json").read_text())
    report = json.loads((HERE / "feasibility-report.json").read_text())
    errors = validate(protocol, report, check_paths=args.check_paths)
    mutation_failures = mutation_self_test(protocol, report) if args.self_test else []
    if mutation_failures:
        errors.append("mutations not rejected: " + ", ".join(mutation_failures))
    result = {"status": "PASS" if not errors else "FAIL", "errors": errors, "model_calls": 0, "feasibility": "blocked"}
    print(json.dumps(result, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

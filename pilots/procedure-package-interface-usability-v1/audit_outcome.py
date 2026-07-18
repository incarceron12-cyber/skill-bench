#!/usr/bin/env python3
"""Audit retained interface-conformance attempts and strict denominators."""
from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
ORDER = ["case-alpha", "case-beta", "case-heldout"]
REQUIRED_ATTEMPT_FILES = ["prompt.txt", "stdout.log", "stderr.log", "adjudication.json", "report.json", "outputs/package.json", "outputs/usage.json", "inputs/corpus.json", "inputs/interface-guide.md", "inputs/example-source.json", "inputs/example-package.json"]

spec = importlib.util.spec_from_file_location("output_validator", ROOT / "scripts/validate_procedure_generation_output.py")
assert spec and spec.loader
output_validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(output_validator)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    errors: list[str] = []
    protocol, manifest, study = load(HERE / "protocol.json"), load(HERE / "freeze-manifest.json"), load(HERE / "study-report.json")
    inventory: dict[str, dict[str, Any]] = {}
    for row in manifest["components"]:
        path = ROOT / row["path"]
        if not path.is_file() or sha(path) != row["sha256"]:
            errors.append(f"frozen component drift: {row['path']}")
    reports = {row["case_id"]: row for row in study.get("cases", [])}
    observations: dict[str, Any] = {}
    for case in protocol["cases"]:
        case_id = case["case_id"]
        attempt = HERE / "generation" / case_id
        files: dict[str, Any] = {}
        for relative in REQUIRED_ATTEMPT_FILES:
            path = attempt / relative
            if not path.is_file():
                errors.append(f"missing retained attempt file: {case_id}/{relative}")
            else:
                files[relative] = {"sha256": sha(path), "bytes": path.stat().st_size}
        inventory[case_id] = files
        try:
            report, usage, adjudication = load(attempt / "report.json"), load(attempt / "outputs/usage.json"), load(attempt / "adjudication.json")
            package_path = attempt / "outputs/package.json"
            source_path, policy_path = ROOT / case["source_path"], ROOT / case["policy_path"]
            independent_errors = output_validator.validate_documents(load(package_path), package_path.read_bytes(), load(source_path), source_path.read_bytes(), load(policy_path))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"unreadable attempt record {case_id}: {exc}")
            continue
        service_valid = report.get("launcher_returncode") == 0 and usage.get("completed") is True and usage.get("failed") is False and usage.get("cost_status") == "included" and usage.get("estimated_cost_usd") == 0.0
        schema_valid = service_valid and not independent_errors
        if report.get("package_sha256") != sha(package_path) or report.get("usage_sha256") != sha(attempt / "outputs/usage.json"):
            errors.append(f"reported artifact hash drift: {case_id}")
        if report.get("service_valid") != service_valid or report.get("schema_valid") != schema_valid:
            errors.append(f"reported validity mismatch: {case_id}")
        if adjudication.get("whole_package_schema_valid") != schema_valid or not all(adjudication.get("field_validity", {}).values()) or adjudication.get("structural_errors") or adjudication.get("semantic_errors"):
            errors.append(f"field-level adjudication mismatch: {case_id}")
        if any(report.get(key) != 0 for key in ("repair_attempts", "retry_attempts", "executor_attempts")):
            errors.append(f"prohibited attempt count: {case_id}")
        observations[case_id] = {"service_valid": service_valid, "schema_valid": schema_valid, "field_validity": adjudication.get("field_validity"), "independent_errors": independent_errors, "usage": {key: usage.get(key) for key in ("input_tokens", "output_tokens", "reasoning_tokens", "total_tokens", "api_calls", "estimated_cost_usd", "cost_status")}}
    recomputed = {"intended": 3, "attempted": len(observations), "service_valid": sum(row["service_valid"] for row in observations.values()), "schema_valid": sum(row["schema_valid"] for row in observations.values())}
    if study.get("denominators") != recomputed or list(observations) != ORDER:
        errors.append("strict denominator or order mismatch")
    if study.get("repair_attempts") != 0 or study.get("retry_attempts") != 0 or study.get("executor_attempts") != 0:
        errors.append("prohibited aggregate attempt count")
    if study.get("claim_ceiling") != protocol.get("claim_ceiling") or any(study.get("claim_ceiling", {}).values()):
        errors.append("claim ceiling drift")
    audit = {"audit_status": "PASS" if not errors else "FAIL", "errors": errors, "denominators": recomputed, "observations": observations, "retained_inventory": inventory, "study_report_sha256": sha(HERE / "study-report.json"), "frozen_origin_commit": study.get("cases", [{}])[0].get("freeze_verification", {}).get("origin_commit"), "claim_ceiling": protocol["claim_ceiling"], "interpretation": "Three one-shot outputs test interface conformance only; they do not test transfer, package consumption, task performance, expertise, professional validity, capability, utility, production fitness, or readiness."}
    rendered = json.dumps(audit, indent=2, sort_keys=True) + "\n"
    (HERE / "outcome-audit.json").write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

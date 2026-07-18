#!/usr/bin/env python3
"""Zero-call builder preflight for the prospectively frozen v7 instrument."""
from __future__ import annotations

import argparse
import ast
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
V4 = ROOT / "pilots/pretask-procedure-transfer-v4"
V5 = ROOT / "pilots/pretask-procedure-transfer-v5"
TASKS = ("k4n7", "p9c2", "t6v1", "w3d8")
CLAIM_KEYS = {"agent_capability", "expert_provenance", "production_fitness", "professional_validity", "readiness", "transfer", "utility"}
ATTEMPTS = {"model": 0, "provider": 0, "executor": 0, "repair": 0, "retry": 0}


def module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    value = importlib.util.module_from_spec(spec); spec.loader.exec_module(value)
    return value


builder = module("v7_builder_preflight", HERE / "prepare_freeze.py")
oracle = module("v7_oracle_preflight", HERE / "oracle.py")
checker = module("v7_checker_preflight", HERE / "checkers/check_endpoint.py")


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def all_false(value: Any) -> bool:
    return type(value) is dict and set(value) == CLAIM_KEYS and all(item is False for item in value.values())


def normalize_reason(value: dict[str, Any], family: str) -> dict[str, Any]:
    result = copy.deepcopy(value)
    if family == "family-epsilon":
        for row in result["decisions"]:
            row["reason"] = "normalized"
    else:
        result["reason"] = "normalized"
    return result


def dependency_targets(source: str) -> set[str]:
    """Return parsed import/dynamic-import targets, ignoring comments/prose."""
    tree = ast.parse(source)
    targets: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            targets.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            targets.add(node.module)
        elif isinstance(node, ast.Call):
            function = node.func
            dynamic = (isinstance(function, ast.Name) and function.id == "__import__") or (
                isinstance(function, ast.Attribute)
                and function.attr in {"import_module", "spec_from_file_location"}
            )
            if dynamic and node.args and isinstance(node.args[0], ast.Constant) and isinstance(node.args[0].value, str):
                targets.add(node.args[0].value)
    return targets


def validate(*, check_paths: bool = True) -> list[str]:
    errors: list[str] = []
    protocol, manifest = load(HERE / "protocol.json"), load(HERE / "freeze-manifest.json")
    if protocol.get("status") != "prospectively_frozen_zero_call_pending_independent_review" or protocol.get("execution_authorized") is not False:
        errors.append("execution_status")
    if protocol.get("attempt_ledger") != ATTEMPTS or manifest.get("attempt_ledger") != ATTEMPTS:
        errors.append("attempt_ledger")
    if not all_false(protocol.get("claim_ceiling")) or not all_false(manifest.get("claim_ceiling")):
        errors.append("claim_ceiling")
    if "independent freeze review" not in protocol.get("required_next_gate", ""):
        errors.append("independent_review_gate")
    if check_paths:
        for row in manifest["components"] + manifest["external_immutable_bindings"]:
            path = ROOT / row["path"]
            if not path.is_file() or path.stat().st_size != row["bytes"] or sha(path) != row["sha256"]:
                errors.append("frozen_byte_drift:" + row["path"])
        for forbidden in ("execution", "execution-report.json"):
            if (HERE / forbidden).exists():
                errors.append("prohibited_execution_artifact:" + forbidden)

    applicability = load(HERE / "source-applicability.json")
    if applicability.get("authorized_instrument") != "pretask-procedure-transfer-v7" or applicability.get("valid_time") != "v7 only" or applicability.get("supersedes_or_edits_v4_authority") is not False:
        errors.append("source_applicability_scope")
    parent_authority = applicability.get("parent_authority", {})
    v6_authority = ROOT / "pilots/pretask-procedure-transfer-v6/source-applicability.json"
    if (parent_authority.get("path") != "pilots/pretask-procedure-transfer-v6/source-applicability.json"
            or parent_authority.get("sha256") != sha(v6_authority)
            or parent_authority.get("decision") != "carry_forward_without_semantic_tuning"):
        errors.append("source_authority_carry_forward")
    lineages = applicability.get("proposition_lineage", [])
    if {row.get("proposition_id") for row in lineages} != {"E-P1", "E-P2", "E-P3", "E-P4", "Z-P1", "Z-P2", "Z-P3", "Z-P4"}:
        errors.append("proposition_lineage_inventory")
    for row in lineages:
        source = ROOT / row["source_path"]
        corpus = load(source)
        proposition = next((item for item in corpus["propositions"] if item["id"] == row["proposition_id"]), None)
        if (proposition is None or row.get("source_file_sha256") != sha(source)
                or row.get("source_statement_sha256") != hashlib.sha256(proposition["statement"].encode()).hexdigest()
                or row.get("source_valid_time_retained") != "v4 only"
                or row.get("v7_applicability") != "authorized_internal_calibration_v7_only"):
            errors.append("proposition_lineage:" + str(row.get("proposition_id")))
    z3 = next((row for row in lineages if row.get("proposition_id") == "Z-P3"), {})
    if "innermost outward" not in z3.get("v7_interpretation", "") or "then the target" not in z3.get("v7_interpretation", ""):
        errors.append("rollback_order_unresolved")

    for task_id in TASKS:
        case, private = load(HERE / f"tasks/{task_id}/input.json"), load(HERE / f"tasks/{task_id}/private.json")
        family = private["family_id"]
        built = builder.expected(task_id, case)
        independent = oracle.derive(task_id, case)
        frozen = private["expected_semantics"]
        if normalize_reason(built, family) != normalize_reason(frozen, family):
            errors.append("builder_frozen_mismatch:" + task_id)
        if normalize_reason(independent, family) != normalize_reason(frozen, family):
            errors.append("oracle_frozen_mismatch:" + task_id)
        candidate = copy.deepcopy(frozen)
        if family == "family-epsilon":
            candidate["decisions"].reverse()
            for row in candidate["decisions"]:
                row["reason"] = "valid paraphrase"
                row["observation_ids"].reverse()
        else:
            candidate["reason"] = "valid paraphrase"
        if not checker.compare(candidate, private)[0]:
            errors.append("valid_alternative_rejected:" + task_id)
        extra = copy.deepcopy(candidate); extra["condition_id"] = "reference_procedure"
        if checker.compare(extra, private)[0]:
            errors.append("condition_field_accepted:" + task_id)
        if private.get("attempts") != ATTEMPTS or not all_false(private.get("claim_ceiling")):
            errors.append("task_attempt_or_claim:" + task_id)
        public = (HERE / f"tasks/{task_id}/public.md").read_text()
        for phrase in ("No additional key", "Repeated JSON keys", "true` is not `1", "1` is not `1.0"):
            if phrase not in public:
                errors.append("undisclosed_contract:" + task_id + ":" + phrase)

    rows = load(HERE / "assignments.json")["rows"]
    v5rows = load(V5 / "assignments.json")["rows"]
    projection = lambda values: [(row["schedule_index"], row["task_id"], row["family_id"], row["condition_id"]) for row in values]
    if projection(rows) != projection(v5rows) or any(row["attempts"] != 0 for row in rows):
        errors.append("assignment_parity")
    checker_text = (HERE / "checkers/check_endpoint.py").read_text().casefold()
    for token in {row["condition_id"] for row in protocol["conditions"]} | {"condition_id", "treatment metadata", "assignment row"}:
        if token in checker_text:
            errors.append("condition_aware_checker:" + token)
    oracle_dependencies = dependency_targets((HERE / "oracle.py").read_text())
    for token in ("prepare_freeze", "check_endpoint", "preflight"):
        if any(token in dependency.replace("-", "_").split(".") for dependency in oracle_dependencies):
            errors.append("oracle_import_coupling:" + token)
    canary_path = HERE / "canary-report.json"
    if not canary_path.is_file() or load(canary_path).get("status") != "PASS" or load(canary_path).get("model_calls") != 0:
        errors.append("canary_gate")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check-paths", action="store_true")
    parser.add_argument("--report", type=Path, default=HERE / "preflight-report.json")
    args = parser.parse_args()
    errors = validate(check_paths=args.check_paths)
    report = {"status": "PASS" if not errors else "FAIL", "errors": errors,
              "gates": {name: "pass" if not errors else "fail" for name in (
                  "exact_byte_freeze", "source_applicability", "independent_semantic_oracle", "closed_artifact_contract",
                  "strict_json_types", "assignment_parity", "isolation_equal_envelope_canaries", "zero_attempts", "all_false_claims")},
              "execution_authorized": False, "model_calls": 0, "provider_calls": 0,
              "attempt_ledger": load(HERE / "protocol.json")["attempt_ledger"],
              "required_next_gate": "separate commit-bound independent freeze review"}
    args.report.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())

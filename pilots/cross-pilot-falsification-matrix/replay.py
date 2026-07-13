#!/usr/bin/env python3
"""Replay the frozen cross-pilot falsification coverage inventory.

This verifies identity and recorded observations. It deliberately does not execute
agents or reinterpret internal conformance cases as capability evidence.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import importlib.util
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
MANIFEST = HERE / "coverage-manifest.json"
REPORT = HERE / "report.json"
CONTINUATION_MANIFEST = HERE / "continuation-manifest-v0.2.json"
CONTINUATION_REPORT = HERE / "report-v0.2.json"
MATRIX_CONTINUATION_MANIFEST = HERE / "continuation-manifest-v0.3.json"
MATRIX_CONTINUATION_REPORT = HERE / "report-v0.3.json"

REQUIREMENTS = {
    "evidence_chain": {
        "authoritative_source", "superseded_source", "lexical_distractor",
        "correct_uncited_claim", "precise_non_entailing_citation", "source_never_exposed",
    },
    "state_delta": {
        "pre_satisfied_requirement", "unrelated_same_value_record", "title_only_empty_artifact",
        "shared_cause_descendant_failures", "dirty_output_path",
    },
    "artifact_behavior": {"native_view", "rendered_view", "pinned_engine_recalculation", "preserved_region"},
    "skill_instrument_independence": {
        "no_skill_independent_rubric", "no_skill_shared_rubric",
        "public_skill_independent_rubric", "public_skill_shared_rubric", "treatment_effect_ceiling",
    },
    "alternative_path_verifier": {
        "positive_witness", "independently_valid_alternative", "minimally_wrong_contrast",
        "shortcut_or_adversarial_artifact", "parser_renderer_drift",
    },
    "claim_ladder": {"task_package_claim", "workflow_family_upgrade", "occupational_upgrade", "readiness_upgrade"},
}
ALLOWED_STATUSES = {"satisfied", "missing", "invalid", "insufficient_evidence", "not_applicable"}
CONTINUATION_ROWS = {"sd-title-only", "sd-shared-cause", "sd-dirty-output", "ab-recalculation"}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def resolve_pointer(document: Any, pointer: str) -> Any:
    if pointer == "":
        return document
    if not pointer.startswith("/"):
        raise ValueError("JSON Pointer must start with '/'")
    value = document
    for raw in pointer[1:].split("/"):
        token = raw.replace("~1", "/").replace("~0", "~")
        if isinstance(value, list):
            try:
                value = value[int(token)]
            except (ValueError, IndexError) as exc:
                raise ValueError(f"invalid list token {token!r}") from exc
        elif isinstance(value, dict):
            if token not in value:
                raise ValueError(f"missing object key {token!r}")
            value = value[token]
        else:
            raise ValueError(f"cannot descend through {type(value).__name__}")
    return value


def _forbidden_fields(value: Any, forbidden: set[str], prefix: str = "") -> list[str]:
    """Return JSON Pointer-like paths to forbidden evaluator-input keys."""
    found: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            path = f"{prefix}/{key}"
            if key in forbidden:
                found.append(path)
            found.extend(_forbidden_fields(child, forbidden, path))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            found.extend(_forbidden_fields(child, forbidden, f"{prefix}/{index}"))
    return found


def _evaluate_title_only(before: dict[str, Any], task_input: dict[str, Any], output: dict[str, Any]) -> dict[str, Any]:
    del task_input
    existed_before = before.get("authoritative_artifact", {}).get("exists") is True
    title = output.get("metadata", {}).get("title")
    content = output.get("authoritative_artifact", {}).get("content")
    metadata_only = isinstance(title, str) and bool(title.strip()) and isinstance(content, str) and not content.strip()
    failed = not existed_before and metadata_only
    return {
        "outcome": "failed" if failed else "passed",
        "failure_class": "empty_authoritative_artifact" if failed else "none",
        "metadata_only": metadata_only,
        "substantive_score": 0 if failed else 1,
    }


def _evaluate_shared_cause(before: dict[str, Any], task_input: dict[str, Any], output: dict[str, Any]) -> dict[str, Any]:
    del before
    if task_input.get("attribution_policy") != "count_failed_roots_not_descendant_symptoms":
        raise ValueError("shared-cause attribution policy drift")
    failures = output.get("failures", [])
    by_id = {item.get("failure_id"): item for item in failures}
    if len(by_id) != len(failures) or None in by_id:
        raise ValueError("shared-cause failure ids must be unique strings")
    children: dict[str, set[str]] = defaultdict(set)
    parents: dict[str, set[str]] = defaultdict(set)
    for edge in output.get("causal_edges", []):
        parent, child = edge.get("parent"), edge.get("child")
        if parent not in by_id or child not in by_id or parent == child:
            raise ValueError("shared-cause edge has invalid endpoint")
        children[parent].add(child)
        parents[child].add(parent)
    failed_ids = {key for key, item in by_id.items() if item.get("failed") is True}
    roots = {key for key in failed_ids if by_id[key].get("kind") == "root" and not parents[key]}
    descendants = {key for key in failed_ids if by_id[key].get("kind") == "descendant"}
    reachable: set[str] = set()
    frontier = list(roots)
    while frontier:
        node = frontier.pop()
        for child in children[node]:
            if child not in reachable:
                reachable.add(child)
                frontier.append(child)
    if not descendants <= reachable:
        raise ValueError("failed descendant lacks a path from a failed root")
    attributed = output.get("attributed_root_failure_ids", [])
    if len(attributed) != len(set(attributed)) or set(attributed) != roots:
        raise ValueError("shared-cause attribution must count each failed root exactly once")
    return {
        "outcome": "failed" if failed_ids else "passed",
        "failure_class": "shared_cause" if failed_ids else "none",
        "failed_nodes": len(failed_ids),
        "root_failures": len(roots),
        "descendant_symptoms": len(descendants),
        "attributed_failures": len(attributed),
        "double_count_prevented": len(attributed) == len(roots) < len(failed_ids),
    }


def _evaluate_dirty_output(before: dict[str, Any], task_input: dict[str, Any], output: dict[str, Any]) -> dict[str, Any]:
    if task_input.get("invalid_environment_policy") != "exclude_from_substantive_denominator":
        raise ValueError("dirty-output invalid-run policy drift")
    required = task_input.get("required_canaries", [])
    canaries = output.get("canaries", {})
    if set(required) != set(canaries):
        raise ValueError("dirty-output canary inventory drift")
    failed = sorted(key for key in required if canaries.get(key) is not True)
    dirty_entries = before.get("entries", [])
    if bool(dirty_entries) != (canaries.get("output_root_clean") is False):
        raise ValueError("dirty-output snapshot and canary disagree")
    invalid = bool(failed)
    if invalid and (output.get("substantive_denominator_included") is True or output.get("agent_failure_count", 0) != 0):
        raise ValueError("invalid dirty-output run cannot enter the substantive failure denominator")
    return {
        "outcome": "invalid" if invalid else "valid",
        "failure_class": "dirty_output_environment" if invalid else "none",
        "failed_canaries": failed,
        "substantive_denominator_included": not invalid,
        "agent_failure_count": 0,
    }


def _load_formula_engine(engine: dict[str, Any]) -> Any:
    path = (ROOT / engine.get("path", "")).resolve()
    try:
        path.relative_to(ROOT.resolve())
    except ValueError as exc:
        raise ValueError("formula engine escapes repository") from exc
    if not path.is_file() or sha256(path) != engine.get("sha256"):
        raise ValueError("formula engine identity mismatch")
    spec = importlib.util.spec_from_file_location("cross_pilot_pinned_formula_engine", path)
    if spec is None or spec.loader is None:
        raise ValueError("formula engine cannot be loaded")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if module.ENGINE_ID != engine.get("component_id") or module.ENGINE_VERSION != engine.get("version"):
        raise ValueError("formula engine declared identity mismatch")
    return module


def _evaluate_recalculation(before: dict[str, Any], task_input: dict[str, Any], output: dict[str, Any]) -> dict[str, Any]:
    mutation = task_input.get("mutation", {})
    if mutation.get("pointer") != "/workbook/inputs/units":
        raise ValueError("unsupported authoritative-input mutation")
    mutated_inputs = copy.deepcopy(before["workbook"]["inputs"])
    mutated_inputs["units"] = mutation.get("value")
    engine = _load_formula_engine(task_input.get("engine", {}))
    computed = engine.calculate(task_input.get("formula", {}).get("expression"), mutated_inputs)
    stale = output.get("stale_candidate", {})
    recalculated = output.get("recalculated_candidate", {})
    if stale.get("inputs") != mutated_inputs or recalculated.get("inputs") != mutated_inputs:
        raise ValueError("candidate inputs do not realize the authoritative mutation")
    before_preserved = before["workbook"]["preserved"]
    preserved = stale.get("preserved") == before_preserved and recalculated.get("preserved") == before_preserved
    stale_passed = stale.get("cached", {}).get("total") == computed
    recalculated_passed = recalculated.get("cached", {}).get("total") == computed
    return {
        "outcome": "passed_after_recalculation" if (not stale_passed and recalculated_passed and preserved) else "failed",
        "failure_class": "stale_cached_value" if not stale_passed else "none",
        "computed_value": computed,
        "stale_candidate_passed": stale_passed,
        "recalculated_candidate_passed": recalculated_passed,
        "preserved_regions_unchanged": preserved,
    }


CASE_EVALUATORS = {
    "title-only-empty-artifact": _evaluate_title_only,
    "shared-cause-root-descendants": _evaluate_shared_cause,
    "dirty-output-invalid-run": _evaluate_dirty_output,
    "pinned-engine-recalculation": _evaluate_recalculation,
}


def replay(manifest: dict[str, Any] | None = None, *, write: bool = True) -> dict[str, Any]:
    package = manifest if manifest is not None else json.loads(MANIFEST.read_text())
    errors: list[str] = []
    artifacts: dict[str, dict[str, Any]] = {}
    documents: dict[str, Any] = {}

    for item in package.get("artifacts", []):
        artifact_id = item.get("artifact_id")
        if artifact_id in artifacts:
            errors.append(f"duplicate artifact_id: {artifact_id}")
            continue
        path = (ROOT / item.get("path", "")).resolve()
        try:
            path.relative_to(ROOT.resolve())
        except ValueError:
            errors.append(f"artifact escapes repository: {artifact_id}")
            continue
        artifacts[artifact_id] = item
        if not path.is_file():
            errors.append(f"artifact missing: {artifact_id}")
            continue
        observed_hash = sha256(path)
        if observed_hash != item.get("sha256"):
            errors.append(f"hash mismatch: {artifact_id}")
            continue
        try:
            documents[artifact_id] = json.loads(path.read_text())
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            errors.append(f"artifact is not valid JSON: {artifact_id}: {exc}")

    seen_rows: set[str] = set()
    found_requirements: dict[str, set[str]] = defaultdict(set)
    results: list[dict[str, Any]] = []
    for row in package.get("rows", []):
        row_id = row.get("row_id")
        family = row.get("family")
        requirement = row.get("requirement")
        status = row.get("coverage_status")
        row_errors: list[str] = []
        observed = None

        if row_id in seen_rows:
            row_errors.append("duplicate row_id")
        seen_rows.add(row_id)
        if family not in REQUIREMENTS:
            row_errors.append("unknown family")
        else:
            found_requirements[family].add(requirement)
            if requirement not in REQUIREMENTS[family]:
                row_errors.append("unknown requirement")
        if status not in ALLOWED_STATUSES:
            row_errors.append("invalid coverage_status")

        evidence = row.get("evidence")
        if status in {"satisfied", "invalid", "insufficient_evidence"}:
            if not isinstance(evidence, dict):
                row_errors.append("credited or evidenced row lacks evidence locator")
            else:
                artifact_id = evidence.get("artifact_id")
                if artifact_id not in documents:
                    row_errors.append("evidence artifact unavailable or failed integrity")
                else:
                    try:
                        observed = resolve_pointer(documents[artifact_id], evidence.get("pointer", ""))
                    except ValueError as exc:
                        row_errors.append(f"pointer mismatch: {exc}")
                    else:
                        if observed != row.get("expected_observation"):
                            row_errors.append("observed value differs from frozen expected observation")
        elif evidence is not None:
            row_errors.append("missing/not_applicable row must not claim evidence")

        if status in {"missing", "invalid", "insufficient_evidence", "not_applicable"} and not row.get("reason"):
            row_errors.append("non-satisfied row lacks reason")
        if status == "not_applicable" and len(row.get("reason", "")) < 20:
            row_errors.append("not_applicable rationale is not specific")

        if family == "claim_ladder" and row.get("claim_level") != "task_package":
            expected = row.get("expected_observation")
            if expected == "supported":
                row_errors.append("unsupported claim upgrade")
        if row_errors:
            errors.extend(f"{row_id}: {message}" for message in row_errors)
        results.append({
            "row_id": row_id,
            "family": family,
            "requirement": requirement,
            "coverage_status": status,
            "observed": observed,
            "integrity": "failed" if row_errors else "verified",
            "errors": row_errors,
        })

    for family, required in REQUIREMENTS.items():
        missing = required - found_requirements.get(family, set())
        extra = found_requirements.get(family, set()) - required
        if missing:
            errors.append(f"{family}: absent frozen rows: {sorted(missing)}")
        if extra:
            errors.append(f"{family}: unexpected rows: {sorted(extra)}")

    counts = Counter(row.get("coverage_status") for row in package.get("rows", []))
    family_reports = []
    for family in REQUIREMENTS:
        family_rows = [r for r in results if r["family"] == family]
        blockers = [r["row_id"] for r in family_rows if r["coverage_status"] != "satisfied"]
        family_reports.append({
            "family": family,
            "rows": len(family_rows),
            "satisfied": sum(r["coverage_status"] == "satisfied" for r in family_rows),
            "blockers": blockers,
            "promotion_ready": not blockers and all(r["integrity"] == "verified" for r in family_rows),
        })

    report = {
        "report_version": "0.1.0",
        "manifest_sha256": sha256(MANIFEST) if manifest is None else None,
        "integrity_valid": not errors,
        "errors": errors,
        "summary": {
            "families": len(REQUIREMENTS),
            "rows": len(results),
            "coverage_status_counts": dict(sorted(counts.items())),
            "promotion_ready_families": sum(item["promotion_ready"] for item in family_reports),
        },
        "family_results": family_reports,
        "rows": results,
        "promotion_decision": "blocked",
        "promotion_blockers": [
            r["row_id"] for r in results
            if r["coverage_status"] != "satisfied" or r["integrity"] != "verified"
        ],
        "claim_boundaries": {
            "professional_capability": False,
            "cross_domain_capability": False,
            "skill_treatment_effect": False,
            "real_world_safety": False,
            "deployment_readiness": False,
        },
    }
    if write:
        REPORT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    return report


def replay_continuation(manifest: dict[str, Any] | None = None, *, write: bool = True) -> dict[str, Any]:
    """Replay the v0.2 deterministic continuation without altering v0.1 evidence."""
    package = manifest if manifest is not None else json.loads(CONTINUATION_MANIFEST.read_text())
    errors: list[str] = []
    parent = package.get("parent_evidence", {})
    for label in ("manifest", "report"):
        path = (ROOT / parent.get(f"{label}_path", "")).resolve()
        try:
            path.relative_to(ROOT.resolve())
        except ValueError:
            errors.append(f"parent {label} escapes repository")
            continue
        if not path.is_file() or sha256(path) != parent.get(f"{label}_sha256"):
            errors.append(f"parent {label} hash mismatch")

    legacy = replay(write=False)
    if not legacy["integrity_valid"]:
        errors.append("parent replay is not integrity-valid")

    forbidden = set(package.get("evaluator_contract", {}).get("forbidden_evaluator_input_fields", []))
    seen_cases: set[str] = set()
    closed_rows: set[str] = set()
    case_results: list[dict[str, Any]] = []
    for case in package.get("cases", []):
        case_id = case.get("case_id")
        case_errors: list[str] = []
        if case_id in seen_cases or case_id not in CASE_EVALUATORS:
            case_errors.append("duplicate or unknown case_id")
        seen_cases.add(case_id)
        row_id = case.get("closes_row_id")
        if row_id in closed_rows or row_id not in CONTINUATION_ROWS:
            case_errors.append("duplicate or unknown continuation row")
        closed_rows.add(row_id)
        documents: dict[str, Any] = {}
        for role in ("before", "input", "output", "expected"):
            record = case.get("records", {}).get(role, {})
            path = (ROOT / record.get("path", "")).resolve()
            try:
                path.relative_to(ROOT.resolve())
            except ValueError:
                case_errors.append(f"{role} record escapes repository")
                continue
            if not path.is_file():
                case_errors.append(f"{role} record missing")
                continue
            if sha256(path) != record.get("sha256"):
                case_errors.append(f"{role} hash mismatch")
                continue
            try:
                document = json.loads(path.read_text())
                documents[role] = resolve_pointer(document, record.get("pointer", ""))
            except (UnicodeDecodeError, json.JSONDecodeError, ValueError) as exc:
                case_errors.append(f"{role} pointer or JSON mismatch: {exc}")
        for role in ("before", "input", "output"):
            if role in documents:
                for pointer in _forbidden_fields(documents[role], forbidden):
                    case_errors.append(f"forbidden evaluator-input field: {role}{pointer}")
        basis = case.get("public_basis", {})
        if basis.get("role") not in documents:
            case_errors.append("public basis record unavailable")
        else:
            try:
                basis_text = resolve_pointer(documents[basis["role"]], basis.get("pointer", ""))
                if not isinstance(basis_text, str) or not basis_text.strip():
                    case_errors.append("public basis is empty")
            except ValueError as exc:
                case_errors.append(f"public basis pointer mismatch: {exc}")
        transform = case.get("transformation_identity")
        if transform:
            role = transform.get("role")
            if role not in documents:
                case_errors.append("transformation identity record unavailable")
            else:
                try:
                    declared = resolve_pointer(documents[role], transform.get("pointer", ""))
                except ValueError as exc:
                    case_errors.append(f"transformation identity pointer mismatch: {exc}")
                else:
                    frozen_identity = {key: transform.get(key) for key in ("component_id", "version", "sha256")}
                    observed_identity = {key: declared.get(key) for key in frozen_identity} if isinstance(declared, dict) else {}
                    if observed_identity != frozen_identity:
                        case_errors.append("transformation identity differs from frozen manifest")
        observed = None
        if not case_errors and all(role in documents for role in ("before", "input", "output", "expected")):
            try:
                observed = CASE_EVALUATORS[case_id](documents["before"], documents["input"], documents["output"])
            except (KeyError, TypeError, ValueError) as exc:
                case_errors.append(f"case logic error: {exc}")
            else:
                if observed != documents["expected"]:
                    case_errors.append("observed value differs from frozen expected observation")
                if observed.get("failure_class") != case.get("failure_class"):
                    case_errors.append("failure class differs from frozen manifest")
        errors.extend(f"{case_id}: {message}" for message in case_errors)
        case_results.append({
            "case_id": case_id,
            "closes_row_id": row_id,
            "observed": observed,
            "integrity": "failed" if case_errors else "verified",
            "errors": case_errors,
        })
    if seen_cases != set(CASE_EVALUATORS):
        errors.append(f"continuation case inventory mismatch: {sorted(set(CASE_EVALUATORS) - seen_cases)}")
    if closed_rows != CONTINUATION_ROWS:
        errors.append(f"continuation row inventory mismatch: {sorted(CONTINUATION_ROWS - closed_rows)}")

    rows = copy.deepcopy(legacy["rows"])
    result_by_row = {item["closes_row_id"]: item for item in case_results}
    for row in rows:
        if row["row_id"] in result_by_row:
            case_result = result_by_row[row["row_id"]]
            row["coverage_status"] = "satisfied"
            row["observed"] = case_result["observed"]
            row["integrity"] = case_result["integrity"]
            row["errors"] = case_result["errors"]
    counts = Counter(row["coverage_status"] for row in rows)
    family_reports = []
    for family in REQUIREMENTS:
        family_rows = [row for row in rows if row["family"] == family]
        blockers = [row["row_id"] for row in family_rows if row["coverage_status"] != "satisfied"]
        family_reports.append({
            "family": family,
            "rows": len(family_rows),
            "satisfied": sum(row["coverage_status"] == "satisfied" for row in family_rows),
            "blockers": blockers,
            "promotion_ready": not blockers and all(row["integrity"] == "verified" for row in family_rows),
        })
    blockers = [row["row_id"] for row in rows if row["coverage_status"] != "satisfied" or row["integrity"] != "verified"]
    report = {
        "report_version": "0.2.0",
        "manifest_sha256": sha256(CONTINUATION_MANIFEST) if manifest is None else None,
        "parent_manifest_sha256": parent.get("manifest_sha256"),
        "parent_report_sha256": parent.get("report_sha256"),
        "integrity_valid": not errors,
        "errors": errors,
        "summary": {
            "families": len(REQUIREMENTS),
            "rows": len(rows),
            "continuation_cases": len(case_results),
            "coverage_status_counts": dict(sorted(counts.items())),
            "promotion_ready_families": sum(item["promotion_ready"] for item in family_reports),
        },
        "family_results": family_reports,
        "continuation_cases": case_results,
        "rows": rows,
        "promotion_decision": "blocked",
        "promotion_blockers": blockers,
        "claim_boundaries": {
            "professional_capability": False,
            "cross_domain_capability": False,
            "skill_treatment_effect": False,
            "real_world_safety": False,
            "production_fitness": False,
            "deployment_readiness": False,
        },
    }
    if blockers != [package.get("continuation_policy", {}).get("remaining_blocker")]:
        report["integrity_valid"] = False
        report["errors"].append("remaining blocker differs from frozen continuation policy")
    if write:
        CONTINUATION_REPORT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    return report


def replay_matrix_continuation(manifest: dict[str, Any] | None = None, *, write: bool = True) -> dict[str, Any]:
    """Replay v0.3 against v0.2 and the prospective vendor matrix."""
    package = manifest if manifest is not None else json.loads(MATRIX_CONTINUATION_MANIFEST.read_text())
    errors: list[str] = []
    parent = package.get("parent_evidence", {})
    for role in ("manifest", "report"):
        path = (ROOT / parent.get(f"{role}_path", "")).resolve()
        try:
            path.relative_to(ROOT.resolve())
        except ValueError:
            errors.append(f"parent {role} escapes repository")
            continue
        if not path.is_file() or sha256(path) != parent.get(f"{role}_sha256"):
            errors.append(f"parent {role} hash mismatch")

    parent_report = replay_continuation(write=False)
    if not parent_report["integrity_valid"]:
        errors.append("v0.2 parent replay is not integrity-valid")

    matrix = package.get("matrix_evidence", {})
    matrix_documents: dict[str, Any] = {}
    for role in ("protocol", "report"):
        path = (ROOT / matrix.get(f"{role}_path", "")).resolve()
        try:
            path.relative_to(ROOT.resolve())
        except ValueError:
            errors.append(f"matrix {role} escapes repository")
            continue
        if not path.is_file() or sha256(path) != matrix.get(f"{role}_sha256"):
            errors.append(f"matrix {role} hash mismatch")
            continue
        try:
            matrix_documents[role] = json.loads(path.read_text())
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            errors.append(f"matrix {role} is not valid JSON: {exc}")

    observations: dict[str, Any] = {}
    if "report" in matrix_documents:
        for observation_id, requirement in matrix.get("required_observations", {}).items():
            try:
                observed = resolve_pointer(matrix_documents["report"], requirement.get("pointer", ""))
            except ValueError as exc:
                errors.append(f"matrix observation {observation_id} pointer mismatch: {exc}")
                continue
            observations[observation_id] = observed
            if observed != requirement.get("expected"):
                errors.append(f"matrix observation {observation_id} differs from frozen expectation")

    if "protocol" in matrix_documents and "report" in matrix_documents:
        scorer_path = ROOT / "scripts/report_vendor_skill_rubric_matrix.py"
        spec = importlib.util.spec_from_file_location("cross_pilot_vendor_matrix", scorer_path)
        if spec is None or spec.loader is None:
            errors.append("matrix scorer cannot be loaded")
        else:
            scorer = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(scorer)
            try:
                scorer.verify_protocol(matrix_documents["protocol"])
                replayed_matrix = scorer.build_report(matrix_documents["protocol"])
            except (KeyError, TypeError, ValueError) as exc:
                errors.append(f"matrix exact replay failed: {exc}")
            else:
                if replayed_matrix != matrix_documents["report"]:
                    errors.append("matrix report differs from exact scorer replay")

    rows = copy.deepcopy(parent_report["rows"])
    closed_row_id = matrix.get("closed_row_id")
    matching = [row for row in rows if row["row_id"] == closed_row_id]
    if len(matching) != 1 or closed_row_id != "si-treatment-effect-ceiling":
        errors.append("matrix continuation closes an unknown or duplicate row")
    else:
        matching[0].update({
            "coverage_status": "satisfied" if not errors else "invalid",
            "observed": {
                "declared_attempts": observations.get("declared_attempts"),
                "retained_attempts": observations.get("retained_attempts"),
                "valid_attempts": observations.get("valid_attempts"),
                "skill_under_independent": observations.get("skill_under_independent"),
                "skill_under_shared": observations.get("skill_under_shared"),
                "rubric_mean_difference": observations.get("rubric_mean_difference"),
                "interaction": observations.get("interaction"),
                "scope": "one synthetic source-task cluster",
            },
            "integrity": "verified" if not errors else "failed",
            "errors": list(errors),
        })

    counts = Counter(row["coverage_status"] for row in rows)
    family_reports = []
    for family in REQUIREMENTS:
        family_rows = [row for row in rows if row["family"] == family]
        blockers = [row["row_id"] for row in family_rows if row["coverage_status"] != "satisfied" or row["integrity"] != "verified"]
        family_reports.append({"family": family, "rows": len(family_rows), "satisfied": sum(row["coverage_status"] == "satisfied" for row in family_rows), "blockers": blockers, "promotion_ready": not blockers})
    blockers = [row["row_id"] for row in rows if row["coverage_status"] != "satisfied" or row["integrity"] != "verified"]
    expected_blockers = package.get("promotion_policy", {}).get("coverage_blockers_expected")
    if blockers != expected_blockers:
        errors.append("coverage blockers differ from frozen v0.3 policy")
    claim_boundaries = package.get("claim_boundaries", {})
    if not claim_boundaries or any(claim_boundaries.values()):
        errors.append("unsupported v0.3 claim upgrade")
    report = {
        "report_version": "0.3.0",
        "manifest_sha256": sha256(MATRIX_CONTINUATION_MANIFEST) if manifest is None else None,
        "parent_manifest_sha256": parent.get("manifest_sha256"),
        "parent_report_sha256": parent.get("report_sha256"),
        "matrix_protocol_sha256": matrix.get("protocol_sha256"),
        "matrix_report_sha256": matrix.get("report_sha256"),
        "integrity_valid": not errors,
        "errors": errors,
        "summary": {"families": len(REQUIREMENTS), "rows": len(rows), "coverage_status_counts": dict(sorted(counts.items())), "promotion_ready_families": sum(item["promotion_ready"] for item in family_reports)},
        "family_results": family_reports,
        "matrix_observations": observations,
        "rows": rows,
        "promotion_decision": package.get("promotion_policy", {}).get("promotion_decision"),
        "promotion_blockers": blockers,
        "promotion_reason": package.get("promotion_policy", {}).get("reason"),
        "claim_boundaries": claim_boundaries,
    }
    if write:
        MATRIX_CONTINUATION_REPORT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    return report


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Verify report is current without rewriting it")
    parser.add_argument("--continuation", action="store_true", help="Replay the v0.2 deterministic continuation")
    parser.add_argument("--matrix-continuation", action="store_true", help="Replay the v0.3 prospective Skill×rubric continuation")
    args = parser.parse_args()
    if args.continuation and args.matrix_continuation:
        parser.error("choose at most one continuation")
    runner = replay_matrix_continuation if args.matrix_continuation else replay_continuation if args.continuation else replay
    report_path = MATRIX_CONTINUATION_REPORT if args.matrix_continuation else CONTINUATION_REPORT if args.continuation else REPORT
    report = runner(write=not args.check)
    if args.check:
        if not report_path.is_file() or json.loads(report_path.read_text()) != report:
            print("REPORT_STALE")
            return 1
    print(json.dumps({
        "integrity_valid": report["integrity_valid"],
        "summary": report["summary"],
        "promotion_decision": report["promotion_decision"],
        "promotion_blockers": report["promotion_blockers"],
    }, indent=2))
    return 0 if report["integrity_valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

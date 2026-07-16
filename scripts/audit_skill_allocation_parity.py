#!/usr/bin/env python3
"""Replay retained Skill studies into a fail-closed resource-allocation audit.

The audit never launches an agent and never imputes component allocation from
aggregate usage.  ``--freeze-manifest`` is an explicit authoring action; normal
replay verifies every parent byte and Git identity before reading outcomes.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from itertools import product
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
AUDIT_DIR = ROOT / "pilots" / "skill-allocation-parity-audit" / "v1"
PROHIBITED_CLAIMS = {
    "skill_effect", "memory_value", "capability", "professional_validity",
    "cross_domain_generality", "safety", "production_fitness", "readiness",
}
STUDIES = [
    {
        "study_id": "cross-pilot-nonceiling-v2",
        "root": "pilots/cross-pilot-nonceiling-skill-study/v2",
        "protocol": "protocol.json",
        "report": "execution/study-report.json",
        "attempt_dir": "execution/attempts",
        "task_from": "cluster",
        "task_prefix": "nonceiling-v2:",
        "trial_report": "trial-report.json",
        "usage": "trial/outputs/usage.json",
        "grade": "dual-rubric-grade.json",
    },
    {
        "study_id": "vendor-skill-rubric-matrix-v1",
        "root": "pilots/vendor-incident-response/trials/skill-rubric-matrix-v1",
        "protocol": "protocol.json",
        "report": "matrix-report.json",
        "attempt_dir": "attempts",
        "task_from": None,
        "task_prefix": "vendor-v2-frozen-task",
        "trial_report": "trial-report.json",
        "usage": "trial/outputs/usage.json",
        "grade": "dual-rubric-grade.json",
    },
]


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def canonical_hash(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def artifact(path_text: str) -> dict[str, Any]:
    path = ROOT / path_text
    blob = subprocess.run(
        ["git", "rev-parse", f"HEAD:{path_text}"], cwd=ROOT,
        capture_output=True, text=True, check=True,
    ).stdout.strip()
    return {
        "path": path_text,
        "bytes": path.stat().st_size,
        "sha256": sha256(path),
        "git_blob": blob,
    }


def _claim_ceiling(protocol: dict[str, Any]) -> dict[str, bool]:
    source = protocol["claim_boundaries"]
    if any(source.values()):
        raise ValueError("parent protocol claim boundary is not fail-closed")
    return {key: False for key in sorted(PROHIBITED_CLAIMS)}


def build_manifest() -> dict[str, Any]:
    studies: list[dict[str, Any]] = []
    attempts: list[dict[str, Any]] = []
    for spec in STUDIES:
        base = ROOT / spec["root"]
        protocol_path = base / spec["protocol"]
        report_path = base / spec["report"]
        protocol, report = load(protocol_path), load(report_path)
        parent_paths = [
            f"{spec['root']}/{spec['protocol']}",
            f"{spec['root']}/{spec['report']}",
        ]
        studies.append({
            "study_id": spec["study_id"],
            "declared_attempts": len(protocol["attempt_schedule"]),
            "parent_claim_ceiling": _claim_ceiling(protocol),
            "configured_system_sha256": canonical_hash(protocol["configured_system"]),
            "artifacts": [artifact(path) for path in parent_paths],
        })
        report_rows = {row["attempt_id"]: row for row in report["attempt_rows"]}
        for scheduled in protocol["attempt_schedule"]:
            attempt_id = scheduled["attempt_id"]
            row = report_rows[attempt_id]
            attempt_root = f"{spec['root']}/{spec['attempt_dir']}/{attempt_id}"
            paths = [
                f"{attempt_root}/{spec['trial_report']}",
                f"{attempt_root}/{spec['usage']}",
            ]
            grade_path = ROOT / attempt_root / spec["grade"]
            if grade_path.is_file():
                paths.append(f"{attempt_root}/{spec['grade']}")
            task_suffix = scheduled.get(spec["task_from"]) if spec["task_from"] else ""
            task_id = spec["task_prefix"] + (task_suffix or "")
            trial = load(ROOT / paths[0])
            usage = load(ROOT / paths[1])
            service_valid = bool(trial.get("service_available", row.get("service_available", False))) and not usage.get("failed", True)
            environment_valid = bool(trial.get("valid_environment"))
            grader_valid = bool(row.get("rubric_eligible", row.get("valid_trial", False)))
            attempts.append({
                "study_id": spec["study_id"],
                "attempt_id": attempt_id,
                "task_id": task_id,
                "condition": scheduled["skill_condition"],
                "execution_order": scheduled["execution_order"],
                "attempt_index": scheduled.get("attempt_index"),
                "replacement_for": scheduled.get("replacement_for"),
                "configured_system_sha256": canonical_hash(protocol["configured_system"]),
                "service_status": "valid" if service_valid else "invalid",
                "environment_status": "valid" if environment_valid else "invalid",
                "grader_status": "valid" if grader_valid else "invalid",
                "state_evidence": {
                    "initial_shared_state": {"status": "unavailable", "value": None},
                    "final_shared_state": {"status": "unavailable", "value": None},
                },
                "resource_evidence": {
                    "aggregate_usage_available": True,
                    "allocation_breakdown_available": False,
                    "per_component_locators": [],
                    "tool_calls_status": "unavailable",
                    "wall_time_status": "unavailable",
                    "skill_delivery_overhead_status": "unavailable",
                },
                "module_flow_evidence": {
                    "opportunity": "task_condition_assigned",
                    "delivery_status": "presented" if scheduled["skill_condition"] == "public_skill" else "not_applicable",
                    "adoption_status": "unavailable",
                    "adoption_evidence_type": "visibility_only" if scheduled["skill_condition"] == "public_skill" else "not_applicable",
                },
                "artifacts": [artifact(path) for path in paths],
            })
    return {
        "schema_version": "0.1.0",
        "audit_id": "skill-allocation-parity-audit-v1",
        "purpose": "Replay retained attempts into a complete, non-imputed allocation ledger and test exact-match parity admissibility.",
        "predeclared_before_outcome_replay": {
            "matching_keys": ["study_id", "task_id", "execution_order", "configured_system_sha256", "initial_shared_state", "final_shared_state"],
            "parity_tolerances": {
                "configured_system": "exact",
                "task": "exact",
                "execution_order": "exact",
                "shared_state": "exact_observed_hash_required",
                "api_calls_absolute": 0,
                "input_tokens_relative": 0.05,
                "output_tokens_relative": 0.05,
                "total_tokens_relative": 0.05,
            },
            "admissibility": [
                "both attempts retained and service/environment/grader valid",
                "opposite conditions and every matching key exact",
                "per-component direct observe/act and intervention allocation available",
                "aggregate token totals never substituted for allocation",
            ],
            "missing_policy": "Retain every intended attempt and emit insufficient_evidence; never complete-case substitute or impute.",
        },
        "studies": studies,
        "attempts": attempts,
        "claim_ceiling": {key: False for key in sorted(PROHIBITED_CLAIMS)},
        "limitations": [
            "Parent trials expose aggregate provider usage but no per-call or component allocation.",
            "Public Skill visibility is presentation evidence, not adoption evidence.",
            "No exact opposite-condition execution-order match exists prospectively.",
            "Shared-state hashes, tool-call counts, and wall time were not retained.",
        ],
    }


def semantic_errors(manifest: dict[str, Any], *, check_paths: bool = False) -> list[str]:
    errors: list[str] = []
    required = {"schema_version", "audit_id", "predeclared_before_outcome_replay", "studies", "attempts", "claim_ceiling", "limitations"}
    if missing := required - set(manifest):
        return [f"missing top-level fields: {sorted(missing)}"]
    if set(manifest["claim_ceiling"]) != PROHIBITED_CLAIMS or any(manifest["claim_ceiling"].values()):
        errors.append("claim upgrade forbidden")
    studies = {row["study_id"]: row for row in manifest["studies"]}
    attempts = manifest["attempts"]
    keys = [(row.get("study_id"), row.get("attempt_id")) for row in attempts]
    if len(keys) != len(set(keys)):
        errors.append("attempt identities must be unique")
    for study_id, study in studies.items():
        retained = [row for row in attempts if row.get("study_id") == study_id]
        if len(retained) != study.get("declared_attempts"):
            errors.append(f"{study_id}: complete-case substitution or silent attempt loss")
        if any(study.get("parent_claim_ceiling", {}).values()):
            errors.append(f"{study_id}: parent claim ceiling upgraded")
        if check_paths:
            protocol_refs = [ref for ref in study.get("artifacts", []) if ref.get("path", "").endswith("/protocol.json")]
            if len(protocol_refs) != 1:
                errors.append(f"{study_id}: exactly one protocol parent is required")
            else:
                protocol = load(ROOT / protocol_refs[0]["path"])
                expected_config = canonical_hash(protocol["configured_system"])
                if study.get("configured_system_sha256") != expected_config:
                    errors.append(f"{study_id}: unmatched prompt/budget/configured-system identity")
                scheduled = {row["attempt_id"]: row for row in protocol["attempt_schedule"]}
                if set(scheduled) != {row.get("attempt_id") for row in retained}:
                    errors.append(f"{study_id}: complete-case substitution or schedule mismatch")
                for row in retained:
                    source = scheduled.get(row.get("attempt_id"), {})
                    if row.get("execution_order") != source.get("execution_order"):
                        errors.append(f"{study_id}/{row.get('attempt_id')}: state/order mismatch with frozen protocol")
                    if row.get("condition") != source.get("skill_condition"):
                        errors.append(f"{study_id}/{row.get('attempt_id')}: condition mismatch with frozen protocol")
                    if row.get("configured_system_sha256") != expected_config:
                        errors.append(f"{study_id}/{row.get('attempt_id')}: unmatched prompt/budget/configured-system identity")
    for row in attempts:
        label = f"{row.get('study_id')}/{row.get('attempt_id')}"
        if row.get("study_id") not in studies:
            errors.append(f"{label}: unknown study")
        resources = row.get("resource_evidence", {})
        if resources.get("allocation_breakdown_available") and not resources.get("per_component_locators"):
            errors.append(f"{label}: aggregate-token laundering into component allocation")
        flow = row.get("module_flow_evidence", {})
        if flow.get("adoption_status") not in {"unavailable", "not_applicable"} and flow.get("adoption_evidence_type") == "visibility_only":
            errors.append(f"{label}: public Skill visibility cannot establish adoption")
        if row.get("condition") == "no_skill" and flow.get("delivery_status") != "not_applicable":
            errors.append(f"{label}: no-skill attempt cannot record Skill delivery")
        for ref in row.get("artifacts", []):
            _check_artifact(ref, label, errors, check_paths)
    for study in studies.values():
        for ref in study.get("artifacts", []):
            _check_artifact(ref, study["study_id"], errors, check_paths)
    policy = manifest["predeclared_before_outcome_replay"]
    if policy.get("matching_keys") != ["study_id", "task_id", "execution_order", "configured_system_sha256", "initial_shared_state", "final_shared_state"]:
        errors.append("matching keys changed after freeze")
    if policy.get("missing_policy", "").find("Retain every intended attempt") < 0:
        errors.append("complete-case substitution policy forbidden")
    return errors


def _check_artifact(ref: dict[str, Any], label: str, errors: list[str], check_paths: bool) -> None:
    if not all(ref.get(key) is not None for key in ("path", "bytes", "sha256", "git_blob")):
        errors.append(f"{label}: incomplete artifact identity")
        return
    if not check_paths:
        return
    path = ROOT / ref["path"]
    if not path.is_file():
        errors.append(f"{label}: missing parent {ref['path']}")
        return
    if path.stat().st_size != ref["bytes"] or sha256(path) != ref["sha256"]:
        errors.append(f"{label}: stale parent bytes {ref['path']}")
    observed = subprocess.run(["git", "rev-parse", f"HEAD:{ref['path']}"], cwd=ROOT, capture_output=True, text=True)
    if observed.returncode or observed.stdout.strip() != ref["git_blob"]:
        errors.append(f"{label}: Git identity mismatch {ref['path']}")


def _usage_and_outcome(row: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    refs = {Path(ref["path"]).name: ref["path"] for ref in row["artifacts"]}
    usage = load(ROOT / next(ref["path"] for ref in row["artifacts"] if ref["path"].endswith("/usage.json")))
    grade_path = refs.get("dual-rubric-grade.json")
    grade = load(ROOT / grade_path) if grade_path else {}
    if "grades" in grade:
        scores = {key: value.get("score") for key, value in grade["grades"].items()}
    elif "rubric_grades" in grade:
        scores = {key: value.get("proportion") for key, value in grade["rubric_grades"].items()}
    else:
        scores = grade.get("rubric_scores", {})
    outcome = {
        "independent_rubric_score": scores.get("independent"),
        "shared_rubric_score": scores.get("shared"),
        "consequence_status": "unavailable",
    }
    return usage, outcome


def allocation_record(row: dict[str, Any]) -> dict[str, Any]:
    usage, outcome = _usage_and_outcome(row)
    unavailable = {"status": "unavailable", "value": None}
    return {
        "study_id": row["study_id"], "attempt_id": row["attempt_id"],
        "task_id": row["task_id"], "condition": row["condition"],
        "execution_order": row["execution_order"],
        "dependence_clusters": [row["study_id"], row["task_id"]],
        "configured_system_sha256": row["configured_system_sha256"],
        "service_status": row["service_status"], "environment_status": row["environment_status"], "grader_status": row["grader_status"],
        "initial_shared_state": row["state_evidence"]["initial_shared_state"],
        "final_shared_state": row["state_evidence"]["final_shared_state"],
        "opportunity": row["module_flow_evidence"]["opportunity"],
        "module_flow": row["module_flow_evidence"],
        "resources": {
            "aggregate_provider_usage": {key: usage.get(key) for key in ("input_tokens", "output_tokens", "cache_read_tokens", "cache_write_tokens", "reasoning_tokens", "total_tokens", "api_calls", "estimated_cost_usd", "cost_status")},
            "direct_observe_act": unavailable.copy(),
            "skill_delivery_and_injected_context": unavailable.copy(),
            "candidate_generation": unavailable.copy(),
            "verification": unavailable.copy(),
            "retrieval": unavailable.copy(),
            "repair": unavailable.copy(),
            "tool_calls": unavailable.copy(),
            "wall_time": unavailable.copy(),
        },
        "invalid_or_retry_transition": {
            "replacement_for": row["replacement_for"],
            "status": "none" if row["service_status"] == "valid" else "service_invalid_retained_without_replacement",
        },
        "outcome_and_consequence_vector": outcome,
        "allocation_evidence_status": "insufficient_evidence",
    }


def assess_pair(left: dict[str, Any], right: dict[str, Any], policy: dict[str, Any]) -> dict[str, Any]:
    reasons: list[str] = []
    if left["condition"] == right["condition"]:
        reasons.append("same_condition")
    for key in ("study_id", "task_id", "execution_order", "configured_system_sha256"):
        if left[key] != right[key]:
            reasons.append(f"unmatched_{key}")
    for key in ("initial_shared_state", "final_shared_state"):
        if left[key].get("status") != "observed" or right[key].get("status") != "observed":
            reasons.append(f"{key}_unavailable")
        elif left[key].get("value") != right[key].get("value"):
            reasons.append(f"unmatched_{key}")
    for key in ("service_status", "environment_status", "grader_status"):
        if left[key] != "valid" or right[key] != "valid":
            reasons.append(f"invalid_{key}")
    if left["allocation_evidence_status"] != "sufficient" or right["allocation_evidence_status"] != "sufficient":
        reasons.append("component_allocation_unavailable")
    return {
        "left_attempt_id": left["attempt_id"], "right_attempt_id": right["attempt_id"],
        "status": "admissible" if not reasons else "insufficient_evidence",
        "reasons": sorted(set(reasons)),
    }


def run_audit(manifest_path: Path) -> dict[str, Any]:
    manifest = load(manifest_path)
    errors = semantic_errors(manifest, check_paths=True)
    records = [] if errors else [allocation_record(row) for row in manifest["attempts"]]
    pairs = []
    if not errors:
        by_study_task: dict[tuple[str, str], dict[str, list[dict[str, Any]]]] = {}
        for record in records:
            cell = by_study_task.setdefault((record["study_id"], record["task_id"]), {"no_skill": [], "public_skill": []})
            cell[record["condition"]].append(record)
        for cell in by_study_task.values():
            for left, right in product(cell["no_skill"], cell["public_skill"]):
                pairs.append(assess_pair(left, right, manifest["predeclared_before_outcome_replay"]))
    admissible = [row for row in pairs if row["status"] == "admissible"]
    return {
        "report_version": "0.1.0", "audit_id": manifest.get("audit_id"),
        "manifest": {"path": manifest_path.relative_to(ROOT).as_posix(), "sha256": sha256(manifest_path)},
        "integrity_passed": not errors, "errors": errors,
        "intended_attempts": len(manifest.get("attempts", [])), "retained_allocation_records": len(records),
        "allocation_records": records, "candidate_pair_audits": pairs,
        "admissible_matched_contrasts": len(admissible),
        "allocation_conclusion": "insufficient_evidence" if not admissible else "descriptive_exact_match_available",
        "prospective_fields_required": [
            "per-call phase/component label and prompt/completion/cache/reasoning tokens",
            "direct observe/act tool calls and wall time",
            "Skill injected-context byte/token overhead",
            "generation/verification/retrieval/repair resources where applicable",
            "initial/final shared-state hashes",
            "counterbalanced exact order/block identity",
            "exposure, invocation, adoption, and effect evidence kept separate",
        ],
        "claim_ceiling": manifest.get("claim_ceiling"),
        "interpretation": "Internal replay of retained evidence only. No Skill effect, memory value, capability, professional validity, cross-domain generality, safety, production fitness, or readiness claim is licensed.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", nargs="?", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--freeze-manifest", type=Path)
    parser.add_argument("--validate-only", action="store_true")
    args = parser.parse_args()
    if args.freeze_manifest:
        payload = build_manifest()
        args.freeze_manifest.parent.mkdir(parents=True, exist_ok=True)
        args.freeze_manifest.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(json.dumps({"frozen": args.freeze_manifest.as_posix(), "attempts": len(payload["attempts"])}, indent=2))
        return 0
    if not args.manifest:
        parser.error("manifest is required unless --freeze-manifest is used")
    if args.validate_only:
        errors = semantic_errors(load(args.manifest), check_paths=True)
        report = {"passed": not errors, "errors": errors}
    else:
        report = run_audit(args.manifest.resolve())
        report["passed"] = report["integrity_passed"]
    text = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0 if report.get("passed", report.get("integrity_passed")) else 1


if __name__ == "__main__":
    raise SystemExit(main())

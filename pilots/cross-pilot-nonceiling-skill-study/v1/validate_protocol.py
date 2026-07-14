#!/usr/bin/env python3
"""Fail-closed prospective protocol validator for cross-pilot non-ceiling study v1."""
from __future__ import annotations
import argparse, hashlib, json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PROTOCOL = ROOT / "protocol.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_construction_manifest(cluster: str, manifest: dict) -> list[str]:
    errors: list[str] = []
    allowed = {x["path"] for x in manifest.get("allowed_inputs", [])}
    if any("guide" in p or "shared" in p or "calibration" in p for p in allowed):
        errors.append(f"{cluster} independent construction permits guide/shared/calibration input")
    denied = set(manifest.get("denied_roles", []))
    for role in ("public_guide", "shared_rubric", "calibration_cases", "repository"):
        if role not in denied:
            errors.append(f"{cluster} construction manifest missing denial: {role}")
    return errors


def validate_rubric(label: str, rubric: dict) -> list[str]:
    errors: list[str] = []
    criteria = rubric.get("criteria", [])
    if not criteria or len({c.get("id") for c in criteria}) != len(criteria):
        errors.append(f"{label} criteria missing or duplicated")
    if any(not c.get("public_basis") for c in criteria):
        errors.append(f"{label} contains hidden-obligation criterion")
    if not rubric.get("alternative_paths"):
        errors.append(f"{label} lacks alternative-path policy")
    return errors


def validate(data: dict, *, check_paths: bool = True) -> list[str]:
    errors: list[str] = []
    if data.get("study_status") != "prospective_protocol_frozen_no_calibration_or_model_calls":
        errors.append("study_status must remain prospective and pre-calibration/pre-call")

    schedule = data.get("attempt_schedule", [])
    if len(schedule) != 8 or data.get("policies", {}).get("declared_attempt_denominator") != 8:
        errors.append("declared schedule and denominator must both equal eight")
    keys = [(r.get("cluster"), r.get("skill_condition")) for r in schedule]
    expected = {(c, s): 2 for c in ("lh", "vendor") for s in ("no_skill", "public_skill")}
    if Counter(keys) != expected:
        errors.append("schedule must contain two attempts per cluster x Skill cell")
    if len({r.get("attempt_id") for r in schedule}) != len(schedule) or any(
        not str(r.get("attempt_id", "")).startswith("nx-") for r in schedule
    ):
        errors.append("attempt IDs must be unique opaque nx-* labels")
    if [r.get("execution_order") for r in schedule] != list(range(1, 9)):
        errors.append("execution order must be exactly 1..8")
    if any(r.get("replacement_for") is not None for r in schedule):
        errors.append("replacement attempts are prohibited")

    policies = data.get("policies", {})
    required_policy = {
        "attempts_per_skill_condition_per_cluster": 2,
        "launcher_invocations_per_attempt": 1,
        "replacement_attempts": "none",
        "retry_or_adaptation": "none",
    }
    for key, expected_value in required_policy.items():
        if policies.get(key) != expected_value:
            errors.append(f"policy drift: {key}")
    if "All eight IDs remain" not in policies.get("invalid_missing", ""):
        errors.append("invalid/missing policy must preserve all eight denominators")
    if "No task, source, guide, rubric, grader" not in policies.get("outcome_tuning", ""):
        errors.append("outcome-tuning freeze is missing")

    config = dict(data.get("configured_system", {}))
    declared_config_hash = config.pop("canonical_sha256", None)
    encoded = json.dumps(config, sort_keys=True, separators=(",", ":")).encode()
    if hashlib.sha256(encoded).hexdigest() != declared_config_hash:
        errors.append("configured-system hash drift")

    gate = data.get("calibration_gate", {})
    if gate.get("status") != "pending_no_cases_authored":
        errors.append("v1 freeze must precede calibration-case authorship")
    if set(gate.get("required_case_types", [])) != {"positive", "minimally_wrong", "shortcut", "abstention_or_invalid"}:
        errors.append("calibration gate lacks a required case class")
    if set(gate.get("clusters", [])) != {"lh", "vendor"}:
        errors.append("calibration must cover both clusters")
    if not gate.get("failure_action", "").startswith("Abort v1 before model calls"):
        errors.append("calibration failure must abort before model calls")

    claims = data.get("claim_boundaries", {})
    if not claims or any(value is not False for value in claims.values()):
        errors.append("all claim ceilings must remain false")

    estimand_ids = {x.get("id") for x in data.get("estimands", [])}
    required_estimands = {
        "skill_under_independent_by_cluster", "skill_under_shared_by_cluster",
        "within_output_rubric_by_cluster", "skill_by_rubric_interaction_by_cluster",
        "cluster_heterogeneity",
    }
    if estimand_ids != required_estimands:
        errors.append("estimand set drift")

    components = data.get("frozen_components", [])
    paths = [x.get("path") for x in components]
    if len(paths) != len(set(paths)):
        errors.append("duplicate frozen component path")
    if check_paths:
        for component in components:
            path = ROOT / str(component.get("path", ""))
            if not path.is_file():
                errors.append(f"missing frozen component: {component.get('path')}")
            elif digest(path) != component.get("sha256"):
                errors.append(f"hash drift: {component.get('path')}")

    for cluster in ("lh", "vendor"):
        manifest_path = ROOT / cluster / "rubrics" / "independent-construction-manifest.json"
        rubric_paths = [ROOT / cluster / "rubrics" / name for name in ("independent.json", "shared.json")]
        if check_paths and manifest_path.is_file():
            manifest = json.loads(manifest_path.read_text())
            errors.extend(validate_construction_manifest(cluster, manifest))
        if check_paths:
            for rubric_path in rubric_paths:
                if not rubric_path.is_file():
                    continue
                rubric = json.loads(rubric_path.read_text())
                errors.extend(validate_rubric(str(rubric_path.relative_to(ROOT)), rubric))

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", type=Path, default=PROTOCOL)
    parser.add_argument("--no-check-paths", action="store_true")
    args = parser.parse_args()
    data = json.loads(args.path.read_text())
    errors = validate(data, check_paths=not args.no_check_paths)
    if errors:
        print(json.dumps({"valid": False, "errors": errors}, indent=2))
        return 1
    print(json.dumps({"valid": True, "protocol_id": data["protocol_id"], "attempts": len(data["attempt_schedule"]), "model_calls": 0}, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

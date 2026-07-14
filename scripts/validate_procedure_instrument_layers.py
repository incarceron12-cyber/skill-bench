#!/usr/bin/env python3
"""Validate independently reportable procedure package/environment/trial layers."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any, Iterable

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas/procedure-instrument-layers.schema.json"
REQUIRED_NONCLAIMS = {
    "expert approval", "professional correctness", "agent capability",
    "safety", "production fitness", "deployment readiness",
}
ROLES = {"public_input", "hidden_evidence", "tool_result", "scored_endpoint", "audit_metadata", "prohibited_oracle"}
LAYERS = ("package", "environment", "trial")


class ValidationFailure(Exception):
    pass


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def duplicates(values: Iterable[str]) -> set[str]:
    seen: set[str] = set()
    repeated: set[str] = set()
    for value in values:
        if value in seen:
            repeated.add(value)
        seen.add(value)
    return repeated


def evidence_records(record: dict[str, Any]) -> list[dict[str, Any]]:
    package = record["package_layer"]
    environment = record["environment_layer"]
    trial = record["trial_layer"]
    return [
        package["inventory"], package["versions"], package["access_boundary"]["evidence"],
        package["answer_bearing_tools"]["evidence"],
        *(item["evidence"] for item in package["roles"]),
        environment["adapter_identity"], environment["runtime_identity"],
        environment["shape_contract"], environment["deterministic_replay"],
        trial["procedure_observation"], trial["final_state_observation"],
        trial["endpoint_observation"], trial["alternative_inventory"],
    ]


def derive_outcomes(record: dict[str, Any]) -> dict[str, str]:
    package = record["package_layer"]
    package_evidence = [package["inventory"], package["versions"], package["access_boundary"]["evidence"], package["answer_bearing_tools"]["evidence"], *(item["evidence"] for item in package["roles"])]
    leaked = (
        not package["access_boundary"]["enforced"]
        or package["answer_bearing_tools"]["detected"]
        or any(item["scored_run_access"] != "prohibited" for item in package["prohibited_oracles"])
        or any(item["role"] == "prohibited_oracle" and item["surface"] == "scored_runtime" for item in package["roles"])
    )
    package_outcome = "fail" if leaked else "pass" if all(item["status"] in {"complete", "prohibited"} for item in package_evidence) else "insufficient_evidence"

    environment = record["environment_layer"]
    environment_evidence = [environment["adapter_identity"], environment["runtime_identity"], environment["shape_contract"], environment["deterministic_replay"]]
    if environment["replay_deterministic"] is False:
        environment_outcome = "fail"
    elif all(item["status"] == "complete" for item in environment_evidence) and environment["replay_deterministic"] is True:
        environment_outcome = "pass"
    else:
        environment_outcome = "insufficient_evidence"

    trial = record["trial_layer"]
    trial_evidence = [trial["procedure_observation"], trial["final_state_observation"], trial["endpoint_observation"], trial["alternative_inventory"]]
    substitution = trial["endpoint_source"] == "reasoning_trace"
    observed_failure = trial["procedure_result"] == "fail" or trial["endpoint_result"] == "fail"
    if substitution or observed_failure:
        trial_outcome = "fail"
    elif all(item["status"] == "complete" for item in trial_evidence) and trial["procedure_result"] == trial["endpoint_result"] == "pass" and trial["endpoint_source"] in {"final_artifact", "terminal_state"}:
        trial_outcome = "pass"
    else:
        trial_outcome = "insufficient_evidence"
    return {"package": package_outcome, "environment": environment_outcome, "trial": trial_outcome}


def semantic_errors(record: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    bindings = [record["migration_freeze"], *record["source_bindings"]]
    binding_ids = {item["binding_id"] for item in bindings}
    if len(binding_ids) != len(bindings):
        errors.append("bindings: binding_id values must be unique")
    if not REQUIRED_NONCLAIMS <= set(record["claim_limits"]["unsupported"]):
        errors.append("claim_limits: required non-claims are missing")

    evidence = evidence_records(record)
    for evidence_id in sorted(duplicates(item["evidence_id"] for item in evidence)):
        errors.append(f"evidence: duplicate evidence_id {evidence_id!r}")
    for item in evidence:
        unknown = set(item["provenance_refs"]) - binding_ids
        if unknown:
            errors.append(f"evidence {item['evidence_id']}: unknown provenance refs {sorted(unknown)}")
        if item["status"] in {"partial", "unavailable", "prohibited"} and len(item["reason"].strip()) < 8:
            errors.append(f"evidence {item['evidence_id']}: non-complete status needs a precise reason")

    roles = record["package_layer"]["roles"]
    if {item["role"] for item in roles} != ROLES or len(roles) != len(ROLES):
        errors.append("package layer: roles must cover exactly the six declared roles")
    for item in roles:
        if item["evidence"]["status"] == "unavailable" and item["surface"] != "unavailable":
            errors.append(f"role {item['role']}: unavailable evidence cannot assert an observed surface")

    oracle_refs = {item["binding_ref"] for item in record["package_layer"]["prohibited_oracles"]}
    unknown_oracles = oracle_refs - binding_ids
    if unknown_oracles:
        errors.append(f"package layer: oracle binding refs unknown {sorted(unknown_oracles)}")

    environment = record["environment_layer"]
    if environment["deterministic_replay"]["status"] != "complete" and environment["replay_deterministic"] is not None:
        errors.append("environment layer: unavailable/partial replay cannot report determinism")
    if environment["deterministic_replay"]["status"] == "complete" and environment["replay_deterministic"] is None:
        errors.append("environment layer: complete replay evidence requires determinism result")
    shape_reason = environment["shape_contract"]["reason"].lower()
    required_term = "table" if record["instrument_shape"] == "tabular_mock_tool" else "terminal"
    if environment["shape_contract"]["status"] == "complete" and required_term not in shape_reason:
        errors.append(f"environment layer: {record['instrument_shape']} shape contract lacks {required_term}-state evidence")

    trial = record["trial_layer"]
    invented = set(trial["accepted_alternative_ids"]) - set(trial["declared_alternative_ids"])
    if invented:
        errors.append(f"trial layer: invented alternative paths {sorted(invented)}")
    if trial["endpoint_source"] == "reasoning_trace":
        errors.append("trial layer: trace-derived endpoint cannot substitute for final artifact or terminal state")
    if trial["endpoint_source"] == "unavailable" and trial["endpoint_result"] != "unavailable":
        errors.append("trial layer: unavailable endpoint source cannot report pass/fail")
    for key, result_key in (("procedure_observation", "procedure_result"), ("endpoint_observation", "endpoint_result")):
        if trial[key]["status"] != "complete" and trial[result_key] != "unavailable":
            errors.append(f"trial layer: {key} cannot promote non-complete evidence to {trial[result_key]}")
    if trial["final_state_observation"]["status"] != "complete" and trial["endpoint_source"] in {"final_artifact", "terminal_state"}:
        errors.append("trial layer: missing final state cannot be named as endpoint source")

    derived = derive_outcomes(record)
    for layer in LAYERS:
        if record["reported_layers"][layer] != derived[layer]:
            errors.append(f"reported layer {layer}: must be {derived[layer]}, not {record['reported_layers'][layer]}")

    claims = record["claims"]
    if {item["layer"] for item in claims} != set(LAYERS) or len(claims) != len(LAYERS):
        errors.append("claims: require exactly one claim per layer")
    for claim in claims:
        if claim["status"] == "supported" and derived[claim["layer"]] != "pass":
            errors.append(f"claim {claim['layer']}: lower/absent layer evidence cannot be promoted to supported")
    return errors


def validate_record(record: dict[str, Any], check_paths: bool = False) -> list[str]:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    structural = [f"{'.'.join(map(str, error.absolute_path)) or '<root>'}: {error.message}" for error in Draft202012Validator(schema).iter_errors(record)]
    if structural:
        return structural
    errors = semantic_errors(record)
    if check_paths:
        for binding in [record["migration_freeze"], *record["source_bindings"]]:
            path = ROOT / binding["path"]
            if not path.is_file() or sha256(path) != binding["sha256"]:
                errors.append(f"binding path/hash mismatch: {binding['path']}")
    return errors


def build_report(path: Path, check_paths: bool = False) -> dict[str, Any]:
    record = json.loads(path.read_text(encoding="utf-8"))
    errors = validate_record(record, check_paths)
    return {
        "record": str(path), "valid": not errors, "errors": errors,
        "layer_outcomes": derive_outcomes(record) if not errors else None,
        "claims": record.get("claims", []),
        "claim_ceiling_enforced": REQUIRED_NONCLAIMS <= set(record.get("claim_limits", {}).get("unsupported", [])),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("records", nargs="+", type=Path)
    parser.add_argument("--check-paths", action="store_true")
    parser.add_argument("--report-dir", type=Path)
    args = parser.parse_args()
    failed = False
    for path in args.records:
        report = build_report(path, args.check_paths)
        failed |= not report["valid"]
        text = json.dumps(report, indent=2, sort_keys=True) + "\n"
        print(text, end="")
        if args.report_dir:
            args.report_dir.mkdir(parents=True, exist_ok=True)
            (args.report_dir / f"{path.stem}.layered.report.json").write_text(text, encoding="utf-8")
    return int(failed)


if __name__ == "__main__":
    raise SystemExit(main())

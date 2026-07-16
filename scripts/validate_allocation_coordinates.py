#!/usr/bin/env python3
"""Validate provider-native coordinate capability and exact reconciliation."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
COORDINATES = ("total_input_tokens", "cache_read_tokens", "output_tokens", "reasoning_tokens", "cache_write_tokens")
PHASES = ("direct_observe_act", "skill_delivery_injection", "candidate_generation", "verification", "retrieval", "repair")
ROLES = {
    "total_input_tokens": "primary_total",
    "cache_read_tokens": "subset_of_total_input",
    "output_tokens": "primary_total",
    "reasoning_tokens": "subset_of_output",
    "cache_write_tokens": "unavailable_not_zero",
}
AGGREGATE_KEYS = {
    "total_input_tokens": "input_tokens", "cache_read_tokens": "cache_read_tokens",
    "output_tokens": "output_tokens", "reasoning_tokens": "reasoning_tokens",
    "cache_write_tokens": "cache_write_tokens",
}


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value: Any) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def valid_hash(value: Any) -> bool:
    return isinstance(value, str) and len(value) == 64 and all(c in "0123456789abcdef" for c in value)


def validate_manifest(doc: dict[str, Any], *, check_paths: bool = False) -> list[str]:
    errors: list[str] = []
    if doc.get("schema_version") != "0.4.0": errors.append("unsupported manifest version")
    contract = doc.get("coordinate_contract", {})
    if canonical_hash(contract) != doc.get("coordinate_contract_sha256"): errors.append("coordinate contract hash mismatch")
    declarations = contract.get("coordinates", {})
    if set(declarations) != set(COORDINATES): errors.append("coordinate declaration set drift")
    else:
        for key in COORDINATES:
            row = declarations[key]
            expected_status = "unavailable" if key == "cache_write_tokens" else "supported"
            if row.get("status") != expected_status or row.get("accounting_role") != ROLES[key]:
                errors.append(f"coordinate capability or role drift: {key}")
        if contract.get("additive_budget_coordinates") != ["total_input_tokens", "output_tokens"]:
            errors.append("total/subcomponent double-counting policy drift")
        if contract.get("derived_coordinates") != [] or contract.get("imputation_policy") != "forbidden":
            errors.append("hidden derivation or imputation enabled")
    configured = doc.get("configured_system", {})
    if configured.get("coordinate_contract_sha256") != doc.get("coordinate_contract_sha256") or canonical_hash(configured) != doc.get("configured_system_sha256"):
        errors.append("coordinate contract not bound into configured-system identity")
    comparison = doc.get("comparison_identity", {})
    if comparison.get("coordinate_contract_sha256") != doc.get("coordinate_contract_sha256") or comparison.get("configured_system_sha256") != doc.get("configured_system_sha256") or canonical_hash(comparison) != doc.get("comparison_identity_sha256"):
        errors.append("coordinate contract not bound into comparison identity")
    if comparison.get("condition_coordinate_support") != {"no_skill": contract.get("support_signature_sha256"), "public_skill": contract.get("support_signature_sha256")}:
        errors.append("asymmetric condition coordinate support")
    schedule = doc.get("attempt_schedule", [])
    expected = [("no_skill", 1), ("public_skill", 2)]
    if [(row.get("condition"), row.get("within_block_order")) for row in schedule[:2]] != expected or any(row.get("attempt_number") != 1 or row.get("replacement_for") is not None for row in schedule):
        errors.append("attempt order or no-replacement policy drift")
    for ref in doc.get("frozen_components", []):
        if not valid_hash(ref.get("sha256")): errors.append(f"unhashed component: {ref.get('path')}")
        elif check_paths:
            path = ROOT / ref["path"]
            if not path.is_file() or sha256(path) != ref["sha256"]: errors.append(f"stale frozen component: {ref['path']}")
    if any(doc.get("claim_ceiling", {}).values()): errors.append("claim upgrade forbidden")
    return errors


def validate_events(events: list[dict[str, Any]], manifest: dict[str, Any], *, attempt_id: str, aggregate_usage: dict[str, Any] | None = None) -> list[str]:
    errors: list[str] = []
    declarations = manifest["coordinate_contract"]["coordinates"]
    totals = {key: 0 for key in COORDINATES}
    seen: set[str] = set()
    for expected_sequence, event in enumerate(events, 1):
        call_id = event.get("call_id")
        if call_id in seen: errors.append("duplicated native provider-call identity")
        seen.add(call_id)
        if event.get("sequence") != expected_sequence: errors.append("omitted or reordered native provider call")
        if event.get("attempt_id") != attempt_id: errors.append("retry substitution or attempt mismatch")
        if event.get("phase") not in PHASES or event.get("phase_source") != "launcher_declared_call_site": errors.append("phase spoofing or undeclared call site")
        declaration = canonical_hash({"attempt_id": attempt_id, "phase": event.get("phase"), "call_site": event.get("call_site")})
        if event.get("phase_declaration_sha256") != declaration: errors.append("phase declaration hash mismatch")
        for key in ("configured_system_sha256", "coordinate_contract_sha256", "comparison_identity_sha256"):
            if event.get(key) != manifest.get(key): errors.append(f"changed {key.replace('_sha256', '').replace('_', '-')} identity")
        coordinates = event.get("coordinates", {})
        if set(coordinates) != set(COORDINATES): errors.append("coordinate set drift"); continue
        for key in COORDINATES:
            observed, declared = coordinates[key], declarations[key]
            if observed.get("status") != declared.get("status"): errors.append(f"coordinate support drift: {key}")
            if declared["status"] == "supported":
                if not isinstance(observed.get("value"), int) or observed["value"] < 0 or not observed.get("source_field"):
                    errors.append(f"invalid supported coordinate: {key}")
                else: totals[key] += observed["value"]
            elif observed.get("value") is not None or observed.get("source_field") is not None:
                errors.append(f"unavailable coordinate coerced or imputed: {key}")
        if event.get("derivations") != [] or event.get("imputations") != []: errors.append("hidden derivation or imputation")
        if coordinates["cache_read_tokens"].get("status") == "supported" and coordinates["total_input_tokens"].get("status") == "supported" and coordinates["cache_read_tokens"].get("value", 0) > coordinates["total_input_tokens"].get("value", 0): errors.append("cache-read subcomponent exceeds total input")
        if coordinates["reasoning_tokens"].get("status") == "supported" and coordinates["output_tokens"].get("status") == "supported" and coordinates["reasoning_tokens"].get("value", 0) > coordinates["output_tokens"].get("value", 0): errors.append("reasoning subcomponent exceeds output")
        if not isinstance(event.get("wall_time_ms"), int) or event["wall_time_ms"] < 0: errors.append("missing native call wall time")
        payload = {k: v for k, v in event.items() if k != "event_sha256"}
        if event.get("event_sha256") != canonical_hash(payload): errors.append("stale native provider-call event hash")
    if aggregate_usage is not None:
        if aggregate_usage.get("api_calls") != len(events): errors.append("aggregate call count mismatch")
        for key in COORDINATES:
            if declarations[key]["status"] == "supported" and aggregate_usage.get(AGGREGATE_KEYS[key]) != totals[key]:
                errors.append(f"jointly supported coordinate does not reconcile: {key}")
        # Unavailable aggregate fields may exist downstream, but are not evidence and
        # cannot enter comparison totals. Their value is deliberately not inspected.
    return errors


def validate_pair(event_sets: dict[str, list[dict[str, Any]]], manifest: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if set(event_sets) != {"no_skill", "public_skill"}: return ["matched pair conditions incomplete"]
    signatures = set()
    for events in event_sets.values():
        statuses = tuple(tuple((key, event["coordinates"][key]["status"]) for key in COORDINATES) for event in events)
        signatures.add(statuses)
    if len(signatures) != 1: errors.append("asymmetric condition coordinate support")
    for events in event_sets.values():
        if any(event.get("comparison_identity_sha256") != manifest["comparison_identity_sha256"] for event in events): errors.append("comparison identity drift across conditions")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path); parser.add_argument("--events", type=Path); parser.add_argument("--attempt-id"); parser.add_argument("--aggregate-usage", type=Path); parser.add_argument("--check-paths", action="store_true")
    args = parser.parse_args(); manifest = load(args.manifest)
    errors = validate_manifest(manifest, check_paths=args.check_paths)
    if args.events:
        if not args.attempt_id: errors.append("--attempt-id required with --events")
        else: errors += validate_events(load_jsonl(args.events), manifest, attempt_id=args.attempt_id, aggregate_usage=load(args.aggregate_usage) if args.aggregate_usage else None)
    print(json.dumps({"passed": not errors, "errors": errors}, indent=2)); return 0 if not errors else 1


if __name__ == "__main__": raise SystemExit(main())

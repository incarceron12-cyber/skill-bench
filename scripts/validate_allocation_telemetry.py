#!/usr/bin/env python3
"""Validate prospective, phase-resolved allocation telemetry.

This is a trial-layer envelope, not a new benchmark schema.  It deliberately
rejects aggregate Hermes usage as evidence of component allocation and keeps
Skill presentation, invocation, adoption, and outcome evidence distinct.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
PHASES = (
    "direct_observe_act", "skill_delivery_injection", "candidate_generation",
    "verification", "retrieval", "repair",
)
TOKEN_KEYS = ("prompt_tokens", "completion_tokens", "cache_read_tokens", "cache_write_tokens", "reasoning_tokens")
CLAIMS = (
    "allocation_effect", "skill_effect", "capability", "professional_validity",
    "cost_value", "production_fitness", "readiness",
)
SHA256_LEN = 64


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def valid_hash(value: Any) -> bool:
    return isinstance(value, str) and len(value) == SHA256_LEN and all(c in "0123456789abcdef" for c in value)


def canonical_hash(value: Any) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def validate_manifest(doc: dict[str, Any], *, check_paths: bool = False) -> list[str]:
    errors: list[str] = []
    if doc.get("schema_version") != "0.1.0":
        errors.append("unsupported manifest version")
    schedule = doc.get("attempt_schedule", [])
    ids = [row.get("attempt_id") for row in schedule]
    if len(schedule) != 4 or len(set(ids)) != 4:
        errors.append("counterbalanced schedule requires four unique intended attempts")
    expected = {
        ("block_ab", 1): "no_skill", ("block_ab", 2): "public_skill",
        ("block_ba", 1): "public_skill", ("block_ba", 2): "no_skill",
    }
    observed = {(row.get("block_id"), row.get("within_block_order")): row.get("condition") for row in schedule}
    if observed != expected:
        errors.append("condition order is not exactly counterbalanced AB/BA")
    if any(row.get("replacement_for") is not None or row.get("attempt_number") != 1 for row in schedule):
        errors.append("planned attempts must be first attempts retained without replacement")
    claims = doc.get("claim_ceiling", {})
    if set(claims) != set(CLAIMS) or any(claims.values()):
        errors.append("claim upgrade forbidden")
    if set(doc.get("required_phases", [])) != set(PHASES):
        errors.append("required phase set drift")
    for ref in doc.get("frozen_components", []):
        if not valid_hash(ref.get("sha256")):
            errors.append(f"unhashed component: {ref.get('path')}")
            continue
        if check_paths:
            path = ROOT / ref["path"]
            if not path.is_file() or sha256(path) != ref["sha256"]:
                errors.append(f"stale frozen component: {ref['path']}")
    return errors


def validate_record(record: dict[str, Any], manifest: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    schedule = {row["attempt_id"]: row for row in manifest["attempt_schedule"]}
    planned = schedule.get(record.get("attempt_id"))
    if record.get("kind") != "allocation_telemetry":
        errors.append("wrong telemetry kind")
    if planned is None:
        if record.get("mode") != "zero_call_canary":
            errors.append("attempt is not in frozen schedule")
    else:
        for key in ("condition", "block_id", "within_block_order", "attempt_number", "replacement_for"):
            if record.get(key) != planned.get(key):
                errors.append(f"reordered or retry lineage mismatch: {key}")
    if not valid_hash(record.get("configured_system_sha256")) or record.get("configured_system_sha256") != manifest.get("configured_system_sha256"):
        errors.append("unhashed or unmatched configured system")
    states = record.get("shared_state", {})
    for edge in ("initial_sha256", "final_sha256"):
        if not valid_hash(states.get(edge)):
            errors.append(f"unhashed shared state: {edge}")
    calls = record.get("model_calls", [])
    call_ids = [row.get("call_id") for row in calls]
    if len(call_ids) != len(set(call_ids)):
        errors.append("duplicated model-call identity")
    for call in calls:
        if call.get("phase") not in PHASES:
            errors.append(f"misphased model call: {call.get('call_id')}")
        for key in TOKEN_KEYS:
            if not isinstance(call.get(key), int) or call[key] < 0:
                errors.append(f"missing token coordinate {key}: {call.get('call_id')}")
        if not isinstance(call.get("wall_time_ms"), int) or call["wall_time_ms"] < 0:
            errors.append(f"missing wall time: {call.get('call_id')}")
    tools = record.get("tool_events", [])
    tool_ids = [row.get("event_id") for row in tools]
    if len(tool_ids) != len(set(tool_ids)):
        errors.append("duplicated tool-event identity")
    for event in tools:
        if event.get("phase") != "direct_observe_act":
            errors.append(f"misphased direct tool event: {event.get('event_id')}")
        if not isinstance(event.get("wall_time_ms"), int) or event["wall_time_ms"] < 0:
            errors.append(f"missing tool wall time: {event.get('event_id')}")
    totals = record.get("phase_totals", {})
    if set(totals) != set(PHASES):
        errors.append("omitted or extra phase total")
    else:
        expected = {phase: {key: 0 for key in TOKEN_KEYS} | {"model_calls": 0, "tool_calls": 0, "wall_time_ms": 0} for phase in PHASES}
        for call in calls:
            phase = call.get("phase")
            if phase not in expected:
                continue
            expected[phase]["model_calls"] += 1
            expected[phase]["wall_time_ms"] += call["wall_time_ms"]
            for key in TOKEN_KEYS:
                expected[phase][key] += call[key]
        for event in tools:
            expected["direct_observe_act"]["tool_calls"] += 1
            expected["direct_observe_act"]["wall_time_ms"] += event["wall_time_ms"]
        if totals != expected:
            errors.append("phase totals do not exactly replay event ledger")
    skill = record.get("skill_context", {})
    if record.get("condition") == "public_skill":
        if skill.get("status") != "presented" or not valid_hash(skill.get("sha256")):
            errors.append("public Skill injection is missing or unhashed")
        if not isinstance(skill.get("bytes"), int) or not isinstance(skill.get("tokens"), int):
            errors.append("public Skill byte/token overhead missing")
    elif skill != {"status": "not_applicable", "bytes": 0, "tokens": 0, "sha256": None}:
        errors.append("no-Skill condition records Skill delivery")
    flow = record.get("module_flow", {})
    required_flow = {"presentation", "invocation", "adoption", "outcome_effect"}
    if set(flow) != required_flow:
        errors.append("presentation/invocation/adoption/effect evidence not separated")
    else:
        for stage, evidence in flow.items():
            if evidence.get("status") not in {"observed", "not_observed", "not_applicable", "unavailable"}:
                errors.append(f"invalid module-flow status: {stage}")
            locator = evidence.get("evidence")
            if evidence.get("status") == "observed" and (not isinstance(locator, dict) or not valid_hash(locator.get("sha256"))):
                errors.append(f"observed {stage} lacks hashed evidence")
        adoption = flow["adoption"]
        if adoption.get("status") == "observed" and adoption.get("evidence", {}).get("type") in {"presentation_only", "visibility_only"}:
            errors.append("Skill presentation cannot be inferred as adoption")
    retry = record.get("retry_lineage", {})
    if retry.get("attempt_number") != 1 or retry.get("retry_of") is not None or retry.get("replacement_attempt_id") is not None:
        errors.append("retried or replacement record violates retain-once protocol")
    statuses = record.get("validity", {})
    if set(statuses) != {"service", "environment", "grader"} or any(value not in {"valid", "invalid", "not_run"} for value in statuses.values()):
        errors.append("service/environment/grader validity not explicit")
    claims = record.get("claim_ceiling", {})
    if set(claims) != set(CLAIMS) or any(claims.values()):
        errors.append("claim upgrade forbidden")
    digest = record.get("ledger_sha256")
    payload = {key: value for key, value in record.items() if key != "ledger_sha256"}
    if digest != canonical_hash(payload):
        errors.append("unhashed or stale telemetry ledger")
    return errors


def zero_call_canary(manifest: dict[str, Any]) -> dict[str, Any]:
    zero = {key: 0 for key in TOKEN_KEYS} | {"model_calls": 0, "tool_calls": 0, "wall_time_ms": 0}
    state = hashlib.sha256(b"no-persistent-state-v1\n").hexdigest()
    record: dict[str, Any] = {
        "schema_version": "0.1.0", "kind": "allocation_telemetry", "mode": "zero_call_canary",
        "attempt_id": "telemetry-canary-01", "condition": "no_skill", "block_id": "canary",
        "within_block_order": 0, "attempt_number": 1, "replacement_for": None,
        "configured_system_sha256": manifest["configured_system_sha256"],
        "model_calls": [], "tool_events": [],
        "phase_totals": {phase: dict(zero) for phase in PHASES},
        "skill_context": {"status": "not_applicable", "bytes": 0, "tokens": 0, "sha256": None},
        "shared_state": {"initial_sha256": state, "final_sha256": state},
        "retry_lineage": {"attempt_number": 1, "retry_of": None, "replacement_attempt_id": None, "policy": "retain_once_without_replacement"},
        "validity": {"service": "not_run", "environment": "valid", "grader": "not_run"},
        "module_flow": {
            "presentation": {"status": "not_applicable", "evidence": None},
            "invocation": {"status": "not_applicable", "evidence": None},
            "adoption": {"status": "not_applicable", "evidence": None},
            "outcome_effect": {"status": "not_applicable", "evidence": None},
        },
        "outcome": {"status": "not_run", "consequences": []},
        "claim_ceiling": {key: False for key in CLAIMS},
    }
    record["ledger_sha256"] = canonical_hash(record)
    return record


def assess_launcher_readiness(manifest: dict[str, Any]) -> dict[str, Any]:
    usage_ref = ROOT / manifest["launcher_probe"]["retained_usage_path"]
    usage = load(usage_ref)
    per_call = usage.get("calls")
    blocker = None if isinstance(per_call, list) and per_call else "configured Hermes --usage-file exposes aggregate totals only; no per-call phase/component ledger is available"
    return {
        "schema_version": "0.1.0", "kind": "matched_pair_readiness",
        "ready": blocker is None, "fresh_model_calls": 0, "matched_pair_executed": False,
        "canary_passed": True, "provider_availability": "historically_available_not_reprobed",
        "intentional_spend_required": False,
        "blockers": [] if blocker is None else [blocker],
        "evidence": {"path": usage_ref.relative_to(ROOT).as_posix(), "sha256": sha256(usage_ref), "observed_keys": sorted(usage)},
        "decision": "execute_exactly_one_pair" if blocker is None else "fail_closed_without_provider_calls",
        "interpretation": "Capture readiness only; no allocation effect, Skill effect, capability, professional validity, cost value, production fitness, or readiness claim.",
        "claim_ceiling": {key: False for key in CLAIMS},
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--record", type=Path)
    parser.add_argument("--write-canary", type=Path)
    parser.add_argument("--write-readiness", type=Path)
    parser.add_argument("--check-paths", action="store_true")
    args = parser.parse_args()
    manifest = load(args.manifest)
    errors = validate_manifest(manifest, check_paths=args.check_paths)
    if args.write_canary:
        canary = zero_call_canary(manifest)
        dump(args.write_canary, canary)
        errors.extend(validate_record(canary, manifest))
    if args.record:
        errors.extend(validate_record(load(args.record), manifest))
    if args.write_readiness:
        dump(args.write_readiness, assess_launcher_readiness(manifest))
    print(json.dumps({"passed": not errors, "errors": errors}, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())

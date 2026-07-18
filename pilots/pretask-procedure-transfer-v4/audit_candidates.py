#!/usr/bin/env python3
"""Independently audit and hash-freeze retained v4 procedure candidates.

The audit is write-once. It replays the committed validator against untouched
candidate bytes, checks strict denominators and the four-file visibility
boundary, records a chained append-only event log, and keeps all downstream
execution artifacts absent.
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from scripts.validate_procedure_generation_output import validate_documents

ORDER = ("family-epsilon", "family-zeta")
VISIBLE_INPUTS = ("corpus.json", "interface-guide.md", "example-source.json", "example-package.json")
FAMILY_PATHS = {
    "family-epsilon": (HERE / "families/epsilon/corpus.json", HERE / "generation-policies/epsilon.json"),
    "family-zeta": (HERE / "families/zeta/corpus.json", HERE / "generation-policies/zeta.json"),
}
CLAIMS = {"expert_provenance", "professional_validity", "transfer", "agent_capability", "utility", "production_fitness", "readiness"}
REQUIRED_ATTEMPT_FILES = (
    "prompt.txt", "stdout.log", "stderr.log", "validator.stdout.log", "validator.stderr.log", "report.json",
    "outputs/package.json", "outputs/usage.json", "inputs/corpus.json", "inputs/interface-guide.md",
    "inputs/example-source.json", "inputs/example-package.json",
)
PROHIBITED_DOWNSTREAM = ("hindsight-packages", "assignment-materialization", "endpoint-canaries", "executions", "trials")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def file_record(path: Path) -> dict[str, Any]:
    return {"sha256": sha(path), "bytes": path.stat().st_size}


def append_event(path: Path, event: dict[str, Any], sequence: int, previous: str | None) -> str:
    body = {"sequence": sequence, "previous_event_sha256": previous, **event}
    event_hash = hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    row = {**body, "event_sha256": event_hash}
    with path.open("a", encoding="utf-8") as stream:
        stream.write(json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n")
        stream.flush()
        os.fsync(stream.fileno())
    return event_hash


def audit() -> tuple[dict[str, Any], dict[str, Any], list[dict[str, Any]]]:
    errors: list[str] = []
    summary = load(HERE / "candidate-generation-report.json")
    protocol = load(HERE / "protocol.json")
    observations: dict[str, Any] = {}
    frozen_components: list[dict[str, Any]] = []
    events: list[dict[str, Any]] = []

    for dirname in PROHIBITED_DOWNSTREAM:
        if (HERE / dirname).exists():
            errors.append(f"prohibited downstream artifact exists: {dirname}")
    actual = {path.name for path in (HERE / "candidate-generation").iterdir() if path.is_dir()}
    if actual != set(ORDER):
        errors.append("candidate inventory differs from the two predeclared families")

    for family_id in ORDER:
        attempt = HERE / "candidate-generation" / family_id
        retained: dict[str, Any] = {}
        for relative in REQUIRED_ATTEMPT_FILES:
            path = attempt / relative
            if not path.is_file():
                errors.append(f"missing retained file: {family_id}/{relative}")
            else:
                retained[relative] = file_record(path)
                frozen_components.append({"path": path.relative_to(ROOT).as_posix(), **file_record(path)})
        input_files = {path.name for path in (attempt / "inputs").iterdir() if path.is_file()}
        output_files = {path.name for path in (attempt / "outputs").iterdir() if path.is_file()}
        if input_files != set(VISIBLE_INPUTS):
            errors.append(f"visible input inventory drift: {family_id}")
        if output_files != {"package.json", "usage.json"}:
            errors.append(f"output inventory drift: {family_id}")
        try:
            report = load(attempt / "report.json")
            package_path = attempt / "outputs/package.json"
            package_bytes = package_path.read_bytes()
            package = json.loads(package_bytes)
            usage = load(attempt / "outputs/usage.json")
            source_path, policy_path = FAMILY_PATHS[family_id]
            source_bytes = source_path.read_bytes()
            policy = load(policy_path)
            validation_errors = validate_documents(package, package_bytes, load(source_path), source_bytes, policy, report)
        except (OSError, json.JSONDecodeError, KeyError) as exc:
            errors.append(f"unreadable retained attempt {family_id}: {exc}")
            continue
        copied_sources = {
            "corpus.json": source_path,
            "interface-guide.md": HERE / "interface/interface-guide.md",
            "example-source.json": HERE / "interface/example-source.json",
            "example-package.json": HERE / "interface/example-package.json",
        }
        for name, source in copied_sources.items():
            if (attempt / "inputs" / name).read_bytes() != source.read_bytes():
                errors.append(f"copied input differs from frozen source: {family_id}/{name}")
        service_valid = (
            report.get("launcher_returncode") == 0
            and usage.get("completed") is True
            and usage.get("failed") is False
            and usage.get("cost_status") == "included"
            and usage.get("estimated_cost_usd") == 0.0
            and usage.get("model") == "gpt-5.6-sol"
            and usage.get("provider") == "openai-codex"
        )
        schema_valid = service_valid and not validation_errors and input_files == set(VISIBLE_INPUTS) and output_files == {"package.json", "usage.json"}
        if report.get("package_sha256") != sha(package_path) or report.get("usage_sha256") != sha(attempt / "outputs/usage.json"):
            errors.append(f"reported candidate hash drift: {family_id}")
        if report.get("service_valid") is not service_valid or report.get("schema_valid") is not schema_valid:
            errors.append(f"launcher validity disagrees with independent audit: {family_id}")
        attempts = report.get("attempts", {})
        if attempts != {"generation": 1, "model": 1, "provider": 1, "repair": 0, "retry": 0, "executor": 0}:
            errors.append(f"attempt count drift: {family_id}")
        if set(report.get("claim_ceiling", {})) != CLAIMS or any(report.get("claim_ceiling", {}).values()):
            errors.append(f"claim ceiling drift: {family_id}")
        observation = {
            "family_id": family_id,
            "service_valid": service_valid,
            "schema_valid": schema_valid,
            "package_sha256": sha(package_path),
            "independent_validation_errors": validation_errors,
            "retained_inventory": retained,
            "usage": {key: usage.get(key) for key in ("api_calls", "input_tokens", "output_tokens", "reasoning_tokens", "total_tokens", "estimated_cost_usd", "cost_status")},
            "attempts": attempts,
        }
        observations[family_id] = observation
        events.append({"event_type": "candidate_independently_adjudicated", "family_id": family_id, "service_valid": service_valid, "schema_valid": schema_valid, "package_sha256": sha(package_path), "validation_errors": validation_errors})

    recomputed = {
        "intended": 2,
        "attempted": len(observations),
        "service_valid": sum(row["service_valid"] for row in observations.values()),
        "schema_valid": sum(row["schema_valid"] for row in observations.values()),
    }
    if summary.get("denominators") != recomputed or list(observations) != list(ORDER):
        errors.append("strict denominator or frozen order mismatch")
    if summary.get("aggregate_attempts") != {"generation": 2, "model": 2, "provider": 2, "repair": 0, "retry": 0, "executor": 0}:
        errors.append("aggregate attempt count drift")
    if summary.get("claim_ceiling") != protocol.get("claim_ceiling") or any(summary.get("claim_ceiling", {}).values()):
        errors.append("aggregate claim ceiling drift")
    both_valid = len(observations) == 2 and all(row["service_valid"] and row["schema_valid"] for row in observations.values())
    gate = both_valid and not errors
    events.append({"event_type": "generation_gate_adjudicated", "gate": "pass" if gate else "fail", "downstream_materialized": False, "executor_attempts": 0, "errors": errors})
    report = {
        "audit_status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "generation_gate": "pass" if gate else "fail",
        "study_status": "candidates_hash_frozen_execution_not_started" if gate else "blocked_invalid_generated_candidates",
        "denominators": recomputed,
        "observations": observations,
        "aggregate_attempts": {"generation": 2, "model": 2, "provider": 2, "repair": 0, "retry": 0, "executor": 0},
        "downstream_materialized": False,
        "execution_task_may_be_released": gate,
        "executor_authorized_in_this_slice": False,
        "claim_ceiling": protocol["claim_ceiling"],
        "interpretation": "Two immutable source-only candidates were independently adjudicated. This licenses no transfer, task-performance, capability, utility, expert, professional, production, or readiness claim.",
    }
    candidate_manifest = {
        "manifest_version": "1.0.0",
        "study_id": "pretask-procedure-transfer-v4-candidates",
        "status": "frozen_valid_candidates" if gate else "frozen_retained_invalid_candidates",
        "family_order": list(ORDER),
        "candidate_packages": {family_id: observations.get(family_id, {}).get("package_sha256") for family_id in ORDER},
        "components": sorted(frozen_components, key=lambda row: row["path"]),
        "aggregate_attempts": report["aggregate_attempts"],
        "executor_attempts": 0,
        "claim_ceiling": protocol["claim_ceiling"],
    }
    return report, candidate_manifest, events


def main() -> int:
    audit_path = HERE / "generation-audit.jsonl"
    report_path = HERE / "generation-audit-report.json"
    manifest_path = HERE / "candidate-freeze-manifest.json"
    if any(path.exists() for path in (audit_path, report_path, manifest_path)):
        raise RuntimeError("append-only audit artifact exists; audit rewrite is forbidden")
    audit_path.touch(exist_ok=False)
    report, manifest, events = audit()
    previous = None
    for sequence, event in enumerate(events, 1):
        previous = append_event(audit_path, event, sequence, previous)
    report["append_only_audit"] = {"path": audit_path.relative_to(ROOT).as_posix(), "sha256": sha(audit_path), "events": len(events), "terminal_event_sha256": previous}
    report_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    manifest["generation_report"] = {"path": (HERE / "candidate-generation-report.json").relative_to(ROOT).as_posix(), "sha256": sha(HERE / "candidate-generation-report.json")}
    manifest["audit_log"] = report["append_only_audit"]
    manifest["audit_report"] = {"path": report_path.relative_to(ROOT).as_posix(), "sha256": sha(report_path)}
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["audit_status"] == "PASS" and report["generation_gate"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Record and replay the prospectively frozen vendor-v2 reliability slice."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import shutil
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
PILOT = ROOT / "pilots/vendor-incident-response"
DEFAULT_PROTOCOL = PILOT / "reliability/protocol-v1.json"
DEFAULT_REPORT = PILOT / "reliability/reliability-report-v1.json"
HISTORICAL_ID = "agent-run-20260711-v2"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _load_grader(path: Path) -> Any:
    spec = importlib.util.spec_from_file_location("frozen_vendor_grade_v2", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load frozen grader: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def exact_interval(successes: int, total: int, confidence: float = 0.95) -> list[float] | None:
    """Two-sided Clopper-Pearson interval, solved from binomial tails."""
    if total == 0:
        return None
    if not (0 <= successes <= total):
        raise ValueError("successes must be between zero and total")
    alpha = 1.0 - confidence

    def cdf(k: int, p: float) -> float:
        return sum(math.comb(total, i) * p**i * (1.0 - p) ** (total - i) for i in range(k + 1))

    def bisect_for(target: float, k: int) -> float:
        lo, hi = 0.0, 1.0
        for _ in range(100):
            mid = (lo + hi) / 2.0
            # Binomial CDF is decreasing in p.
            if cdf(k, mid) > target:
                lo = mid
            else:
                hi = mid
        return (lo + hi) / 2.0

    lower = 0.0 if successes == 0 else bisect_for(1.0 - alpha / 2.0, successes - 1)
    upper = 1.0 if successes == total else bisect_for(alpha / 2.0, successes)
    return [round(lower, 6), round(upper, 6)]


def _assert_hash(path: Path, expected: str, label: str) -> None:
    if not path.is_file():
        raise ValueError(f"missing {label}: {path}")
    observed = sha256(path)
    if observed != expected:
        raise ValueError(f"{label} hash mismatch: expected {expected}, observed {observed}")


def verify_protocol(protocol: dict[str, Any], protocol_path: Path) -> None:
    if len(protocol["attempt_schedule"]["attempt_ids"]) < 3:
        raise ValueError("protocol must freeze at least three attempts")
    if len(set(protocol["attempt_schedule"]["attempt_ids"])) != len(protocol["attempt_schedule"]["attempt_ids"]):
        raise ValueError("protocol attempt IDs must be unique")
    for component in protocol["frozen_components"]:
        _assert_hash(ROOT / component["path"], component["sha256"], component["role"])
    witness = protocol["retained_exact_version_witness"]
    _assert_hash(ROOT / witness["execution_manifest_path"], witness["execution_manifest_sha256"], "historical manifest")
    if protocol_path != DEFAULT_PROTOCOL:
        raise ValueError("only the canonical frozen protocol is supported")


def _relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def _evidence_entry(run: Path, relative: str, role: str) -> dict[str, Any]:
    path = run / relative
    if not path.is_file():
        raise ValueError(f"missing retained evidence for {run.name}: {relative}")
    return {"path": relative, "sha256": sha256(path), "bytes": path.stat().st_size, "role": role}


def _input_inventory(run: Path) -> list[dict[str, Any]]:
    root = run / "trial/inputs"
    return [
        {"path": path.relative_to(run).as_posix(), "sha256": sha256(path), "bytes": path.stat().st_size}
        for path in sorted(root.rglob("*")) if path.is_file()
    ]


def record_attempt(protocol: dict[str, Any], attempt_id: str, grader: Any) -> dict[str, Any]:
    if attempt_id not in protocol["attempt_schedule"]["attempt_ids"]:
        raise ValueError(f"undeclared attempt: {attempt_id}")
    run = PILOT / "trials" / attempt_id
    trial_path = run / "trial-report.json"
    if not trial_path.is_file():
        raise ValueError(f"declared attempt was not retained: {attempt_id}")
    snapshot = run / "launcher-snapshot.py"
    launcher = next(x for x in protocol["frozen_components"] if x["role"] == "launcher")
    if not snapshot.exists():
        shutil.copy2(ROOT / launcher["path"], snapshot)
    _assert_hash(snapshot, launcher["sha256"], f"{attempt_id} launcher snapshot")

    grade = grader.grade_trial(run)
    write_json(run / "posthoc-grader-report.json", grade)
    trial = load_json(trial_path)
    canary = load_json(run / "preflight/canary-report.json")
    usage_path = run / "trial/outputs/usage.json"
    usage = load_json(usage_path) if usage_path.is_file() else {}
    trace_text = (run / "redacted-trace.log").read_text(encoding="utf-8")
    required_outputs = {"usage.json", "incident-brief.md", "action-plan.json"}
    service_available = (
        trial.get("returncode") == 0
        and trial.get("complete") is True
        and required_outputs <= set(trial.get("artifacts", {}))
        and usage.get("completed") is True
        and usage.get("failed") is False
    )
    valid_trial = bool(service_available and canary.get("passed") and trial.get("valid_environment") and grade.get("eligible"))
    cost_included = usage.get("cost_status") == "included" and usage.get("estimated_cost_usd") == 0.0
    if service_available and not cost_included:
        raise ValueError(f"completed attempt lacks included zero-cost evidence: {attempt_id}")

    retained = [
        _evidence_entry(run, "preflight/canary-report.json", "zero-call isolation canary"),
        _evidence_entry(run, "trial-report.json", "environment, service, artifact, and configured-system validity"),
        _evidence_entry(run, "redacted-trace.log", "stdout-only redacted trace and in-trial containment assertions"),
        _evidence_entry(run, "launcher-stderr.log", "launcher/provider stderr"),
        _evidence_entry(run, "launcher-snapshot.py", "exact frozen launcher bytes"),
        _evidence_entry(run, "posthoc-grader-report.json", "typed deterministic substantive grade"),
    ]
    for name in sorted(required_outputs):
        retained.append(_evidence_entry(run, f"trial/outputs/{name}", f"retained output {name}"))
    manifest = {
        "schema_version": "0.1.0",
        "attempt_id": attempt_id,
        "protocol": {"path": _relative(DEFAULT_PROTOCOL), "sha256": sha256(DEFAULT_PROTOCOL)},
        "configured_system": trial["configured_system"],
        "component_identity": {
            "task_sha256": trial["task_sha256"],
            "launcher_sha256": trial["launcher_sha256"],
            "launcher_snapshot_sha256": sha256(snapshot),
            "grader_sha256": sha256(PILOT / "grade_v2.py"),
            "input_manifest_sha256": trial["input_manifest_sha256"],
            "protected_before_and_after_sha256": canary["protected_sha256"],
        },
        "zero_call_canary": {"passed": canary["passed"], "model_calls": canary["model_calls"], "report_path": "preflight/canary-report.json"},
        "in_trial_containment_observation": {
            "agent_reported_trial_output_paths": "/trial/outputs/incident-brief.md" in trace_text and "/trial/outputs/action-plan.json" in trace_text,
            "agent_reported_no_protected_access": "No protected content was accessed" in trace_text,
            "agent_reported_no_outside_output_mutation": "no files outside `outputs/` were modified" in trace_text,
            "independent_read_only_input_diff_empty": trial["workspace_diff"]["changed_read_only_inputs"] == [],
            "independent_protected_hash_unchanged": trial["workspace_diff"]["protected_unchanged"] is True,
            "limitation": "Agent stdout assertions are not trusted as isolation proof; the zero-call file-tool canary and post-run byte comparisons provide the independent checks."
        },
        "service_available": service_available,
        "valid_trial": valid_trial,
        "grade_eligible": grade["eligible"],
        "observed_outcome": grade["observed_outcome"] if valid_trial else None,
        "usage": {key: usage.get(key) for key in ("api_calls", "input_tokens", "output_tokens", "reasoning_tokens", "total_tokens", "estimated_cost_usd", "cost_status", "completed", "failed")},
        "input_inventory": _input_inventory(run),
        "retained_evidence": retained,
        "claim_boundaries": {"treatment_effect": False, "expert_validity": False, "professional_competence": False, "general_capability": False, "cross_domain_generalization": False, "real_world_safety": False, "production_fitness": False, "readiness": False},
    }
    write_json(run / "execution-manifest.json", manifest)
    return manifest


def verify_attempt(protocol: dict[str, Any], attempt_id: str, grader: Any) -> dict[str, Any]:
    run = PILOT / "trials" / attempt_id
    manifest = load_json(run / "execution-manifest.json")
    if manifest["attempt_id"] != attempt_id:
        raise ValueError("attempt ID mismatch")
    _assert_hash(ROOT / manifest["protocol"]["path"], manifest["protocol"]["sha256"], "attempt protocol")
    launcher = next(x for x in protocol["frozen_components"] if x["role"] == "launcher")
    _assert_hash(run / "launcher-snapshot.py", launcher["sha256"], "launcher snapshot")
    for item in manifest["retained_evidence"]:
        _assert_hash(run / item["path"], item["sha256"], f"{attempt_id} evidence")
    for item in manifest["input_inventory"]:
        _assert_hash(run / item["path"], item["sha256"], f"{attempt_id} input")
    replayed = grader.grade_trial(run)
    if replayed != load_json(run / "posthoc-grader-report.json"):
        raise ValueError(f"grader replay mismatch: {attempt_id}")
    trial = load_json(run / "trial-report.json")
    if manifest["component_identity"]["task_sha256"] != trial["task_sha256"]:
        raise ValueError("task identity mismatch")
    if manifest["component_identity"]["input_manifest_sha256"] != sha256(run / "trial/inputs/manifest.json"):
        raise ValueError("input manifest mismatch")
    return manifest


def verify_historical(protocol: dict[str, Any], grader: Any) -> dict[str, Any]:
    run = PILOT / "trials" / HISTORICAL_ID
    execution = load_json(run / "execution-manifest.json")
    trial = load_json(run / "trial-report.json")
    retained_grade = load_json(run / "posthoc-grader-report.json")
    if grader.grade_trial(run) != retained_grade:
        raise ValueError("historical grader replay mismatch")
    frozen = {x["role"]: x for x in protocol["frozen_components"]}
    checks = {
        "task": trial["task_sha256"] == frozen["public_task"]["sha256"],
        "launcher": trial["launcher_sha256"] == frozen["launcher"]["sha256"] == execution["instrument"]["launcher_sha256"],
        "grader": execution["instrument"]["grader_sha256"] == frozen["grader"]["sha256"],
        "configured_system": trial["configured_system"] == execution["configured_system"],
        "input_manifest": trial["input_manifest_sha256"] == sha256(run / "trial/inputs/manifest.json"),
        "grade": retained_grade["eligible"] is True,
    }
    expected_inputs = {x["role"]: x["sha256"] for x in protocol["frozen_components"]}
    copied = {
        "evaluation_context": "trial/inputs/workspace/context/evaluation-context.json",
        "current_status": "trial/inputs/workspace/current/signed-status.json",
        "archived_status": "trial/inputs/workspace/archive/status-previous.json",
        "service_map": "trial/inputs/workspace/reference/service-map.json",
        "vendor_note": "trial/inputs/workspace/inbox/vendor-note.txt",
        "lexical_distractor": "trial/inputs/workspace/noise/signed-status-template.json",
    }
    checks.update({role: sha256(run / path) == expected_inputs[role] for role, path in copied.items()})
    if not all(checks.values()):
        raise ValueError(f"historical witness is not exact-version comparable: {checks}")
    return {"attempt_id": HISTORICAL_ID, "service_available": True, "valid_trial": True, "observed_outcome": retained_grade["observed_outcome"], "exact_version_checks": checks, "execution_manifest_path": _relative(run / "execution-manifest.json"), "execution_manifest_sha256": sha256(run / "execution-manifest.json")}


def _estimate(name: str, successes: int, total: int, denominator: str) -> dict[str, Any]:
    return {"metric": name, "successes": successes, "total": total, "estimate": round(successes / total, 6) if total else None, "confidence_level": 0.95, "interval_method": "Clopper-Pearson exact binomial", "interval": exact_interval(successes, total), "denominator": denominator}


def build_report(protocol: dict[str, Any], protocol_path: Path, grader: Any) -> dict[str, Any]:
    rows = [verify_attempt(protocol, attempt_id, grader) for attempt_id in protocol["attempt_schedule"]["attempt_ids"]]
    historical = verify_historical(protocol, grader)
    valid = [row for row in rows if row["valid_trial"]]
    successful = [row for row in valid if row["observed_outcome"] == "secure_useful_completion"]
    combined_valid = valid + ([historical] if historical["valid_trial"] else [])
    combined_success = [row for row in combined_valid if row["observed_outcome"] == "secure_useful_completion"]
    outcomes: dict[str, int] = {}
    for row in valid:
        outcomes[row["observed_outcome"]] = outcomes.get(row["observed_outcome"], 0) + 1
    report = {
        "schema_version": "0.1.0",
        "report_id": "vendor-incident-v2-exact-version-reliability-v1",
        "protocol": {"path": _relative(protocol_path), "sha256": sha256(protocol_path), "frozen_at": protocol["frozen_at"]},
        "instrument_scope": "One frozen internal synthetic vendor-incident v2 task, one configured system, three prospective repeated executions; historical v2 witness shown separately.",
        "attempt_rows": [
            {"attempt_id": row["attempt_id"], "execution_manifest_path": _relative(PILOT / "trials" / row["attempt_id"] / "execution-manifest.json"), "execution_manifest_sha256": sha256(PILOT / "trials" / row["attempt_id"] / "execution-manifest.json"), "service_available": row["service_available"], "valid_trial": row["valid_trial"], "observed_outcome": row["observed_outcome"], "usage": row["usage"]}
            for row in rows
        ],
        "historical_exact_version_witness": historical,
        "metric_estimates": {
            "prospective": [
                _estimate("service_availability", sum(row["service_available"] for row in rows), len(rows), "all three prospectively declared attempt IDs"),
                _estimate("valid_trial_rate", len(valid), len(rows), "all three prospectively declared attempt IDs"),
                _estimate("secure_useful_completion_given_valid_trial", len(successful), len(valid), "prospective valid trials only"),
            ],
            "combined_exact_version_descriptive": _estimate("secure_useful_completion_given_valid_trial", len(combined_success), len(combined_valid), "three prospective valid trials plus separately verified historical exact-version v2 witness"),
            "valid_trial_outcome_counts": outcomes,
            "interpretation_limit": "Intervals describe binomial attempt-level proportions under a repeated-execution idealization. Shared task, model/provider, harness, and environment create dependence and prevent task-population, professional-competence, or general-capability inference."
        },
        "task_health_observation": {
            "task_health_id": "vendor-incident-v2-health",
            "instrument_version": "vendor-incident-v2",
            "repeat_stability": "observed_same_outcome" if len(outcomes) == 1 and valid else "observed_variation_or_no_valid_trials",
            "invalid_run_rate_observation": {"invalid_attempts": len(rows) - len(valid), "declared_attempts": len(rows)},
            "service_failure_observation": {"unavailable_attempts": len(rows) - sum(row["service_available"] for row in rows), "declared_attempts": len(rows)},
            "operational_role": "calibration_only",
            "role_transition": "none",
            "reason": "Repeated exact-version observations update local calibration evidence only; one synthetic task with outcome-influenced admission has no confirmatory, professional, or population-valid basis."
        },
        "claim_boundaries": {"treatment_effect": False, "expert_validity": False, "professional_competence": False, "general_capability": False, "cross_domain_generalization": False, "real_world_safety": False, "production_fitness": False, "readiness": False},
    }
    return report


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=("record", "replay"))
    parser.add_argument("--protocol", type=Path, default=DEFAULT_PROTOCOL)
    parser.add_argument("--output", type=Path, default=DEFAULT_REPORT)
    args = parser.parse_args()
    protocol_path = args.protocol.resolve()
    protocol = load_json(protocol_path)
    verify_protocol(protocol, protocol_path)
    grader_path = next(ROOT / x["path"] for x in protocol["frozen_components"] if x["role"] == "grader")
    grader = _load_grader(grader_path)
    if args.mode == "record":
        for attempt_id in protocol["attempt_schedule"]["attempt_ids"]:
            record_attempt(protocol, attempt_id, grader)
        write_json(args.output, build_report(protocol, protocol_path, grader))
    else:
        replayed = build_report(protocol, protocol_path, grader)
        retained = load_json(args.output)
        if replayed != retained:
            raise ValueError("reliability report replay mismatch")
    print(json.dumps({"mode": args.mode, "protocol": _relative(protocol_path), "report": _relative(args.output.resolve()), "status": "verified"}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

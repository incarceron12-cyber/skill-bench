#!/usr/bin/env python3
"""Map retained native campaigns into the fixed-denominator accounting gate."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
GATE_PATH = ROOT / "pilots/trial-accounting-reconciliation/reconcile.py"
SPEC = importlib.util.spec_from_file_location("trial_accounting_gate", GATE_PATH)
assert SPEC and SPEC.loader
GATE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(GATE)

CAMPAIGNS = {
    "persistent-workspace-reuse-v3": {
        "root": "pilots/persistent-workspace-reuse/v3",
        "adjudication": None,
        "work_shape_field": "shape",
    },
    "action-boundary-composition-v2": {
        "root": "pilots/action-boundary-composition/v2",
        "adjudication": "pilots/action-boundary-composition/adjudication-v1/adjudication-report.json",
        "work_shape_field": "form",
    },
}
NONCLAIMS = [
    "agent_capability", "treatment_effect", "reliability", "expert_validity",
    "professional_validity", "production", "readiness",
]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical(value: Any) -> str:
    return GATE.canonical_sha256(value)


def load(path: str | Path) -> Any:
    return json.loads((ROOT / path).read_text())


def relative_lock(path: Path, role: str) -> dict[str, str]:
    return {"path": path.relative_to(ROOT).as_posix(), "sha256": sha(path), "role": role}


def parent_locks(campaign_root: Path, report: dict[str, Any], adjudication: str | None) -> list[dict[str, str]]:
    locks = [
        relative_lock(campaign_root / "protocol.json", "prospectively_frozen_assignment_manifest"),
        relative_lock(campaign_root / "execution/study-report.json", "retained_campaign_report"),
    ]
    for row in report["attempts"]:
        attempt_dir = campaign_root / "execution/attempts" / row["attempt_id"]
        for name, role in (("trial-report.json", "native_trial_report"), ("redacted-trace.log", "native_trace")):
            path = attempt_dir / name
            if path.is_file():
                locks.append(relative_lock(path, role))
        for artifact_name in sorted(row.get("artifacts", {})):
            path = attempt_dir / "trial/outputs" / artifact_name
            if path.is_file():
                locks.append(relative_lock(path, "native_artifact"))
    if adjudication:
        locks.append(relative_lock(ROOT / adjudication, "zero_call_defect_adjudication"))
    locks.append(relative_lock(GATE_PATH, "reconciliation_gate_v1"))
    locks.append(relative_lock(Path(__file__), "native_mapping_transform"))
    unique = {item["path"]: item for item in locks}
    return [unique[key] for key in sorted(unique)]


def artifact_valid(campaign_id: str, row: dict[str, Any]) -> bool:
    if campaign_id == "persistent-workspace-reuse-v3":
        return "result.json" in row.get("artifacts", {})
    return bool(row.get("substantively_graded") and row.get("artifacts"))


def map_disposition(campaign_id: str, row: dict[str, Any]) -> tuple[str, str | None]:
    if campaign_id == "persistent-workspace-reuse-v3":
        if row.get("service_valid") is not True:
            return "service_failure", None
        if row.get("environment_valid") is not True:
            return "environment_invalid", None
        if not artifact_valid(campaign_id, row):
            return "missing_artifact", None
        grade = row.get("grade") or {}
        return "valid_scored", grade.get("classification")
    disposition = row.get("campaign_disposition")
    if disposition == "substantive_retained":
        # The zero-call adjudication excludes the recorded exact-execution label
        # because the grader required an undisclosed field. Preserve the native
        # grade, but do not launder it into a canonical pass/fail score.
        return "instrument_invalid", None
    if disposition in {"service_stop_trigger", "post_stop_protocol_deviation_retained_invalid"}:
        return "service_failure", None
    if disposition == "interrupted_post_stop_protocol_deviation_retained_invalid":
        return "timeout", None
    if disposition == "not_launched_due_service_stop":
        return "not_started", None
    raise ValueError(f"unmapped action-boundary disposition: {disposition!r}")


def generate_sidecar(campaign_id: str) -> dict[str, Any]:
    config = CAMPAIGNS[campaign_id]
    campaign_root = ROOT / config["root"]
    protocol = load(f"{config['root']}/protocol.json")
    report = load(f"{config['root']}/execution/study-report.json")
    attempts = {row["cell_id"]: row for row in report["attempts"]}
    mappings = []
    for cell in sorted(protocol["cells"], key=lambda item: item["order"]):
        row = attempts[cell["cell_id"]]
        disposition, result = map_disposition(campaign_id, row)
        started = row.get("launcher_invocations", 0) > 0
        post_stop = campaign_id == "action-boundary-composition-v2" and started and cell["order"] > report["first_service_failure_order"]
        mappings.append({
            "assignment_id": cell["cell_id"],
            "family_id": cell[config["work_shape_field"]],
            "order": cell["order"],
            "retry_policy": "none",
            "native_attempt_id": row["attempt_id"],
            "native_attempt_locator": f"{config['root']}/execution/study-report.json#/attempts/{report['attempts'].index(row)}",
            "canonical_disposition": disposition,
            "result": result,
            "started": started,
            "service_valid": row.get("service_valid") is True,
            "environment_valid": row.get("environment_valid") is True,
            "artifact_valid": artifact_valid(campaign_id, row),
            "substantively_graded": row.get("substantively_graded") is True,
            "scored": disposition == "valid_scored",
            "post_stop_launch": post_stop,
            "replacement_for_attempt_id": None,
            "exclusion_reason": None,
            "exclusion_evidence": None,
        })
    totals = {
        "intended": len(protocol["cells"]),
        "attempted": sum(row["started"] for row in mappings),
        "service_valid": sum(row["service_valid"] for row in mappings),
        "environment_valid": sum(row["environment_valid"] for row in mappings),
        "artifact_valid": sum(row["artifact_valid"] for row in mappings),
        "graded": sum(row["substantively_graded"] for row in mappings),
        "scored": sum(row["scored"] for row in mappings),
        "post_stop_launches": sum(row["post_stop_launch"] for row in mappings),
        "retries": 0,
        "replacements": 0,
    }
    sidecar = {
        "schema_version": "1.0.0",
        "mapping_id": f"{campaign_id}-accounting-map-v1",
        "campaign_id": campaign_id,
        "source_root": config["root"],
        "derivation": {
            "assignment_basis": f"{config['root']}/protocol.json#/cells sorted by prospectively frozen order",
            "outcome_basis": f"{config['root']}/execution/study-report.json#/attempts",
            "outcome_derived_assignments_forbidden": True,
            "transform_path": Path(__file__).relative_to(ROOT).as_posix(),
            "transform_sha256": sha(Path(__file__)),
            "mapping_rules_sha256": canonical({
                "dispositions": "map_disposition@v1",
                "started": "launcher_invocations>0",
                "artifact_valid": "native retained required artifact",
                "score": "only valid_scored",
            }),
        },
        "retry_replacement_stop_policy": {
            "retry": "forbidden",
            "replacement": "forbidden",
            "complete_case_substitution": "forbidden",
            "stop_after_first_service_or_environment_invalid": campaign_id == "action-boundary-composition-v2",
            "known_post_stop_defect_adjudication": config["adjudication"],
        },
        "public_exclusion_basis": {
            "exclusions_used": False,
            "basis": "No intended row is excluded. Invalid, timed-out, and unstarted rows remain in the fixed denominator.",
        },
        "parent_locks": parent_locks(campaign_root, report, config["adjudication"]),
        "mappings": mappings,
        "declared_totals": totals,
        "claim_limits": {"unsupported": NONCLAIMS},
    }
    sidecar["mapping_content_sha256"] = canonical(sidecar)
    return sidecar


def validate_sidecar(sidecar: dict[str, Any], *, check_paths: bool = True) -> dict[str, Any]:
    errors: list[str] = []
    campaign_id = sidecar.get("campaign_id")
    if campaign_id not in CAMPAIGNS:
        return {"valid": False, "errors": ["unknown campaign_id"]}
    config = CAMPAIGNS[campaign_id]
    protocol_path = ROOT / config["root"] / "protocol.json"
    report_path = ROOT / config["root"] / "execution/study-report.json"
    protocol = json.loads(protocol_path.read_text())
    native = json.loads(report_path.read_text())

    content = dict(sidecar)
    recorded_content_hash = content.pop("mapping_content_sha256", None)
    if recorded_content_hash != canonical(content):
        errors.append("mapping sidecar content hash drift")
    if sidecar.get("derivation", {}).get("transform_sha256") != sha(Path(__file__)):
        errors.append("mapping transform identity/hash drift")
    if sidecar.get("derivation", {}).get("outcome_derived_assignments_forbidden") is not True:
        errors.append("assignment derivation must forbid outcome-derived inventories")

    lock_paths = [item.get("path") for item in sidecar.get("parent_locks", [])]
    if len(lock_paths) != len(set(lock_paths)):
        errors.append("parent lock paths must be unique")
    required = {
        protocol_path.relative_to(ROOT).as_posix(),
        report_path.relative_to(ROOT).as_posix(),
        GATE_PATH.relative_to(ROOT).as_posix(),
        Path(__file__).relative_to(ROOT).as_posix(),
    }
    if config["adjudication"]:
        required.add(config["adjudication"])
    missing_required = sorted(required - set(lock_paths))
    if missing_required:
        errors.append(f"missing required parent locks: {missing_required}")
    if check_paths:
        for lock in sidecar.get("parent_locks", []):
            path = ROOT / lock.get("path", "")
            if not path.is_file() or sha(path) != lock.get("sha256"):
                errors.append(f"parent/hash drift: {lock.get('path')}")

    cells = sorted(protocol.get("cells", []), key=lambda item: item.get("order"))
    mappings = sidecar.get("mappings", [])
    expected_ids = [cell.get("cell_id") for cell in cells]
    mapped_ids = [row.get("assignment_id") for row in mappings]
    if mapped_ids != expected_ids:
        errors.append("mapping rows do not exactly preserve frozen protocol assignment order")
    native_by_cell = {row.get("cell_id"): row for row in native.get("attempts", [])}
    if set(native_by_cell) != set(expected_ids):
        errors.append("native report rows do not exhaust frozen intended assignments")

    families = []
    seen_families = set()
    for cell in cells:
        family_id = cell[config["work_shape_field"]]
        if family_id not in seen_families:
            families.append({"family_id": family_id, "work_shape": family_id})
            seen_families.add(family_id)
    assignments = [{
        "assignment_id": cell["cell_id"], "task_id": cell["cell_id"],
        "family_id": cell[config["work_shape_field"]], "retry_policy": "none",
    } for cell in cells]
    component_locks = [{"path": item["path"], "sha256": item["sha256"], "version": item["role"]} for item in sidecar.get("parent_locks", [])]
    manifest = {"manifest_id": sidecar["mapping_id"], "families": families, "assignments": assignments, "component_locks": component_locks}
    attempts = []
    for row in mappings:
        native_row = native_by_cell.get(row.get("assignment_id"), {})
        expected_started = native_row.get("launcher_invocations", 0) > 0
        if row.get("native_attempt_id") != native_row.get("attempt_id"):
            errors.append(f"{row.get('assignment_id')}: native attempt identity mismatch")
        if row.get("started") != expected_started:
            errors.append(f"{row.get('assignment_id')}: attempted/start mapping mismatch")
        expected_disposition, expected_result = map_disposition(campaign_id, native_row)
        if (row.get("canonical_disposition"), row.get("result")) != (expected_disposition, expected_result):
            errors.append(f"{row.get('assignment_id')}: canonical disposition/result mismatch")
        expected_post_stop = campaign_id == "action-boundary-composition-v2" and expected_started and row.get("order", 0) > native.get("first_service_failure_order", 10**9)
        if row.get("post_stop_launch") != expected_post_stop:
            errors.append(f"{row.get('assignment_id')}: post-stop launch mapping mismatch")
        for key, expected in {
            "service_valid": native_row.get("service_valid") is True,
            "environment_valid": native_row.get("environment_valid") is True,
            "artifact_valid": artifact_valid(campaign_id, native_row),
            "substantively_graded": native_row.get("substantively_graded") is True,
            "scored": expected_disposition == "valid_scored",
        }.items():
            if row.get(key) != expected:
                errors.append(f"{row.get('assignment_id')}: {key} mapping mismatch")
        attempts.append({
            "attempt_id": row["native_attempt_id"], "assignment_id": row["assignment_id"],
            "canonical": True, "replacement_for_attempt_id": row.get("replacement_for_attempt_id"),
            "started": row["started"], "disposition": row["canonical_disposition"],
            "result": row.get("result"), "exclusion_reason": row.get("exclusion_reason"),
            "exclusion_evidence": row.get("exclusion_evidence"),
        })

    scored = [row for row in mappings if row.get("canonical_disposition") == "valid_scored"]
    passes = sum(row.get("result") == "pass" for row in scored)
    family_rates = {}
    for family in sorted(seen_families):
        rows = [row for row in scored if row.get("family_id") == family]
        numerator = sum(row.get("result") == "pass" for row in rows)
        family_rates[family] = {"numerator": numerator, "denominator": len(rows), "value": numerator / len(rows) if rows else None}
    values = [item["value"] for item in family_rates.values() if item["value"] is not None]
    ledger = {
        "manifest_id": manifest["manifest_id"], "manifest_sha256": canonical(manifest),
        "component_locks": component_locks, "attempts": attempts,
        "declared_estimates": [
            {"estimand": "task_micro", "numerator": passes, "denominator": len(scored), "value": passes / len(scored) if scored else None},
            {"estimand": "family_macro", "family_rates": family_rates, "value": sum(values) / len(values) if values else None},
        ],
        "claim_limits": sidecar.get("claim_limits", {}),
    }
    gate_report = GATE.reconcile(manifest, ledger, check_paths=check_paths)
    errors.extend(f"gate: {item}" for item in gate_report["errors"])

    totals = {
        "intended": len(cells), "attempted": sum(row.get("started") is True for row in mappings),
        "service_valid": sum(row.get("service_valid") is True for row in mappings),
        "environment_valid": sum(row.get("environment_valid") is True for row in mappings),
        "artifact_valid": sum(row.get("artifact_valid") is True for row in mappings),
        "graded": sum(row.get("substantively_graded") is True for row in mappings),
        "scored": sum(row.get("scored") is True for row in mappings),
        "post_stop_launches": sum(row.get("post_stop_launch") is True for row in mappings),
        "retries": sum(row.get("replacement_for_attempt_id") is not None for row in mappings),
        "replacements": sum(row.get("replacement_for_attempt_id") is not None for row in mappings),
    }
    if totals != sidecar.get("declared_totals"):
        errors.append("declared funnel totals do not match explicit mappings")

    known_defects = []
    protocol_conformant = True
    if campaign_id == "action-boundary-composition-v2":
        first_stop = native.get("first_service_failure_order")
        launched_after = sorted(row["assignment_id"] for row in mappings if row.get("started") and row.get("order", 0) > first_stop)
        adjudication = load(config["adjudication"])
        adjudicated = sorted(item.split(":", 1)[1] for item in adjudication["campaign_adjudication"]["findings"] if item.startswith("launched_after_stop:"))
        if launched_after:
            protocol_conformant = False
            known_defects.append("adjudicated_post_stop_launches")
        if launched_after != adjudicated:
            errors.append("post-stop launches do not exactly match frozen adjudication")
        if totals["retries"] != adjudication["campaign_adjudication"]["retries"]:
            errors.append("retry count disagrees with adjudication")
        if totals["intended"] != adjudication["campaign_adjudication"]["intended_rows_preserved"]:
            errors.append("intended denominator disagrees with adjudication")
        if any(row.get("canonical_disposition") == "valid_scored" for row in mappings if row.get("substantively_graded")):
            errors.append("adjudicated interface-invalid historical grade cannot be scored as failure")

    return {
        "schema_version": "1.0.0", "report_id": f"{campaign_id}-accounting-validation-v1",
        "campaign_id": campaign_id, "valid": not errors, "errors": errors,
        "accounting_reconciles": gate_report["valid"], "protocol_conformant": protocol_conformant,
        "known_adjudicated_defects": known_defects, "totals": totals,
        "canonical_dispositions": dict(sorted(Counter(row.get("canonical_disposition") for row in mappings).items())),
        "gate_estimates": gate_report["estimates"],
        "input_identity": {"mapping_content_sha256": sidecar.get("mapping_content_sha256"), "parent_locks": sidecar.get("parent_locks", [])},
        "claim_limits": sidecar.get("claim_limits"),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--generate", action="store_true", help="regenerate explicit sidecars and retained reports")
    parser.add_argument("--check-paths", action="store_true")
    args = parser.parse_args()
    reports = []
    for campaign_id in CAMPAIGNS:
        sidecar_path = HERE / f"{campaign_id}-mapping.json"
        report_path = HERE / f"{campaign_id}-report.json"
        if args.generate:
            sidecar = generate_sidecar(campaign_id)
            sidecar_path.write_text(json.dumps(sidecar, indent=2, sort_keys=True) + "\n")
        else:
            sidecar = json.loads(sidecar_path.read_text())
        report = validate_sidecar(sidecar, check_paths=args.check_paths)
        reports.append(report)
        rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
        if args.generate:
            report_path.write_text(rendered)
        elif not report_path.is_file() or report_path.read_text() != rendered:
            report["valid"] = False
            report["errors"].append("retained validation report does not match deterministic replay")
        print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if all(report["valid"] for report in reports) else 1


if __name__ == "__main__":
    raise SystemExit(main())

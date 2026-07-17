#!/usr/bin/env python3
"""Fail-closed assignment-to-score reconciliation for frozen benchmark studies."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
DEFAULT_MANIFEST = HERE / "expected-assignments.json"
DEFAULT_LEDGER = HERE / "trial-ledger.json"
DEFAULT_REPORT = HERE / "reconciliation-report.json"
DISPOSITIONS = {
    "not_started",
    "valid_scored",
    "timeout",
    "service_failure",
    "environment_invalid",
    "instrument_invalid",
    "missing_artifact",
    "missing_result",
    "justified_exclusion",
}
REQUIRED_NONCLAIMS = {
    "agent_capability",
    "reliability",
    "professional_validity",
    "readiness",
}


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_sha256(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def _finite_rate(numerator: int, denominator: int) -> float | None:
    return numerator / denominator if denominator else None


def _same_optional_rate(declared: Any, computed: float | None) -> bool:
    """Compare rates while admitting the explicit no-valid-score ``null`` case."""
    if declared is None or computed is None:
        return declared is None and computed is None
    return isinstance(declared, (int, float)) and math.isclose(declared, computed, abs_tol=1e-12)


def reconcile(manifest: dict[str, Any], ledger: dict[str, Any], *, manifest_path: Path | None = None, check_paths: bool = False) -> dict[str, Any]:
    """Return a deterministic report; ``valid`` is false on any accounting ambiguity."""
    errors: list[str] = []
    assignments = manifest.get("assignments", [])
    assignment_ids = [row.get("assignment_id") for row in assignments]
    if len(assignment_ids) != len(set(assignment_ids)):
        errors.append("expected assignment IDs must be unique")
    assignment_by_id = {row.get("assignment_id"): row for row in assignments}
    families = {row.get("family_id"): row for row in manifest.get("families", [])}
    if len(families) != len(manifest.get("families", [])):
        errors.append("family IDs must be unique")
    if len({row.get("work_shape") for row in manifest.get("families", [])}) < 2:
        errors.append("manifest must span at least two materially different work shapes")
    for assignment in assignments:
        if assignment.get("family_id") not in families:
            errors.append(f"{assignment.get('assignment_id')}: unknown family")

    actual_manifest_hash = canonical_sha256(manifest)
    if ledger.get("manifest_id") != manifest.get("manifest_id"):
        errors.append("ledger manifest_id does not match expected manifest")
    if ledger.get("manifest_sha256") != actual_manifest_hash:
        errors.append("ledger manifest hash/version drift")
    if ledger.get("component_locks") != manifest.get("component_locks"):
        errors.append("ledger component locks drift from frozen manifest")
    if not REQUIRED_NONCLAIMS <= set(ledger.get("claim_limits", {}).get("unsupported", [])):
        errors.append("ledger omits required claim limits")

    if check_paths:
        for component in manifest.get("component_locks", []):
            path = ROOT / component.get("path", "")
            if not path.is_file():
                errors.append(f"missing frozen component: {component.get('path')}")
            elif file_sha256(path) != component.get("sha256"):
                errors.append(f"frozen component hash drift: {component.get('path')}")
        if manifest_path is not None and canonical_sha256(json.loads(manifest_path.read_text())) != actual_manifest_hash:
            errors.append("manifest replay changed canonical identity")

    attempts = ledger.get("attempts", [])
    attempt_ids = [row.get("attempt_id") for row in attempts]
    if len(attempt_ids) != len(set(attempt_ids)):
        errors.append("attempt IDs must be unique")
    unknown = sorted({row.get("assignment_id") for row in attempts} - set(assignment_ids))
    for assignment_id in unknown:
        errors.append(f"unknown/unassigned result: {assignment_id}")

    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for attempt in attempts:
        grouped[attempt.get("assignment_id")].append(attempt)
        aid = attempt.get("attempt_id", "<missing>")
        disposition = attempt.get("disposition")
        if disposition not in DISPOSITIONS:
            errors.append(f"{aid}: unknown disposition {disposition!r}")
            continue
        started = attempt.get("started")
        if disposition == "not_started" and started is not False:
            errors.append(f"{aid}: not_started must have started=false")
        if disposition not in {"not_started", "justified_exclusion"} and started is not True:
            errors.append(f"{aid}: {disposition} requires started=true")
        result = attempt.get("result")
        if disposition == "valid_scored":
            if result not in {"pass", "fail"}:
                errors.append(f"{aid}: valid_scored requires exactly one pass/fail result")
        elif result is not None:
            errors.append(f"{aid}: invalid/missing/excluded attempts cannot be included as success/failure")
        if disposition == "justified_exclusion":
            if not attempt.get("exclusion_reason") or not attempt.get("exclusion_evidence"):
                errors.append(f"{aid}: justified exclusion needs reason and evidence locator")
        elif attempt.get("exclusion_reason") is not None or attempt.get("exclusion_evidence") is not None:
            errors.append(f"{aid}: exclusion fields are reserved for justified_exclusion")

    canonical: dict[str, dict[str, Any]] = {}
    for assignment in assignments:
        assignment_id = assignment["assignment_id"]
        rows = grouped.get(assignment_id, [])
        if not rows:
            errors.append(f"missing row for assigned attempt: {assignment_id}")
            continue
        selected = [row for row in rows if row.get("canonical") is True]
        if len(selected) != 1:
            errors.append(f"{assignment_id}: exactly one canonical disposition required; found {len(selected)}")
        else:
            canonical[assignment_id] = selected[0]
        retry_policy = assignment.get("retry_policy")
        if retry_policy == "none":
            if len(rows) != 1 or any(row.get("replacement_for_attempt_id") is not None for row in rows):
                errors.append(f"{assignment_id}: retry/replacement is forbidden")
        elif retry_policy == "declared_canonical_attempt":
            row_ids = {row.get("attempt_id") for row in rows}
            for row in rows:
                replacement = row.get("replacement_for_attempt_id")
                if replacement is not None and replacement not in row_ids:
                    errors.append(f"{assignment_id}: replacement target {replacement!r} is not in the assignment")
            if len(rows) > 1 and sum(row.get("replacement_for_attempt_id") is not None for row in rows) != len(rows) - 1:
                errors.append(f"{assignment_id}: retry replacement chain is ambiguous")
        else:
            errors.append(f"{assignment_id}: unknown retry policy {retry_policy!r}")

    disposition_counts = Counter(row.get("disposition") for row in canonical.values())
    scored = [row for row in canonical.values() if row.get("disposition") == "valid_scored"]
    passes = sum(row.get("result") == "pass" for row in scored)
    micro = {"estimand": "task_micro", "numerator": passes, "denominator": len(scored), "value": _finite_rate(passes, len(scored))}
    family_rows: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for assignment_id, row in canonical.items():
        assignment = assignment_by_id.get(assignment_id)
        if assignment and row.get("disposition") == "valid_scored":
            family_rows[assignment["family_id"]].append(row)
    family_rates: dict[str, dict[str, Any]] = {}
    for family_id in sorted(families):
        rows = family_rows.get(family_id, [])
        family_passes = sum(row.get("result") == "pass" for row in rows)
        family_rates[family_id] = {"numerator": family_passes, "denominator": len(rows), "value": _finite_rate(family_passes, len(rows))}
    rates = [item["value"] for item in family_rates.values() if item["value"] is not None]
    macro_value = sum(rates) / len(rates) if rates else None
    macro = {"estimand": "family_macro", "included_family_count": len(rates), "family_rates": family_rates, "value": macro_value}

    declared = {item.get("estimand"): item for item in ledger.get("declared_estimates", [])}
    if set(declared) != {"task_micro", "family_macro"}:
        errors.append("declared estimates must contain distinct task_micro and family_macro estimands")
    else:
        expected_micro = declared["task_micro"]
        if any(expected_micro.get(key) != micro[key] for key in ("numerator", "denominator")) or not _same_optional_rate(expected_micro.get("value"), micro["value"]):
            errors.append("declared task_micro estimate does not match valid/scored rows")
        expected_macro = declared["family_macro"]
        if expected_macro.get("family_rates") != family_rates or not _same_optional_rate(expected_macro.get("value"), macro_value):
            errors.append("declared family_macro estimate is conflated, mislabeled, or miscomputed")

    assigned_count = len(assignments)
    disposition_total = sum(disposition_counts.values())
    if disposition_total != assigned_count:
        errors.append(f"canonical disposition total {disposition_total} does not reconcile to assigned count {assigned_count}")
    report = {
        "schema_version": "1.0.0",
        "report_id": "trial-accounting-reconciliation-internal-calibration-v1",
        "valid": not errors,
        "errors": errors,
        "input_identity": {
            "manifest_id": manifest.get("manifest_id"),
            "manifest_sha256": actual_manifest_hash,
            "ledger_sha256": canonical_sha256(ledger),
            "component_locks": manifest.get("component_locks", []),
        },
        "funnel": {
            "assigned": assigned_count,
            "attempt_records": len(attempts),
            "canonical_dispositions": disposition_total,
            "started": sum(row.get("started") is True for row in canonical.values()),
            "dispositions": {key: disposition_counts.get(key, 0) for key in sorted(DISPOSITIONS)},
            "reconciles": disposition_total == assigned_count,
        },
        "estimates": {"task_micro": micro, "family_macro": macro},
        "claim_limits": ledger.get("claim_limits", {}),
    }
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--ledger", type=Path, default=DEFAULT_LEDGER)
    parser.add_argument("--check-paths", action="store_true")
    parser.add_argument("--write-report", type=Path)
    parser.add_argument("--check-report", type=Path)
    args = parser.parse_args()
    manifest = json.loads(args.manifest.read_text())
    ledger = json.loads(args.ledger.read_text())
    report = reconcile(manifest, ledger, manifest_path=args.manifest, check_paths=args.check_paths)
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.write_report:
        args.write_report.write_text(rendered)
    if args.check_report and (not args.check_report.is_file() or args.check_report.read_text() != rendered):
        report["valid"] = False
        report["errors"].append("retained reconciliation report does not match deterministic replay")
        rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    print(rendered, end="")
    return 0 if report["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

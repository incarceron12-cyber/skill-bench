#!/usr/bin/env python3
"""Validate provenance-pinned adapters over released procedure packages.

This does not replace procedure-package v0.1. It records whether source bytes and
role mappings are inspectable and fails closed when runtime/final observations
needed by that contract are unavailable.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
ROLES = {"public_input", "hidden_evidence", "tool_result", "scored_endpoint", "audit_metadata", "prohibited_oracle"}
AVAILABILITY = {"observed", "partial", "unavailable"}
FINDING_CATEGORIES = {"source-package-defect", "mapping-insufficiency", "validator-false-positive-candidate", "validator-false-negative-candidate", "non-applicability"}
NONCLAIMS = {"expert approval", "professional correctness", "agent capability", "safety", "production fitness", "deployment readiness"}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_adapter(adapter: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if adapter.get("adapter_version") != "0.1.0":
        errors.append("adapter_version must be 0.1.0")
    freeze_path = ROOT / adapter.get("selection_freeze", "")
    if not freeze_path.is_file():
        errors.append("selection freeze is missing")
    else:
        freeze = json.loads(freeze_path.read_text(encoding="utf-8"))
        if not freeze.get("frozen_before_adapter_or_replay"):
            errors.append("selection was not frozen before adaptation/replay")
        selected = freeze.get("selected", {})
        expected = selected.get("sop_bench" if adapter.get("instrument") == "SOP-Bench" else "anchor", {}).get("package")
        if expected and expected not in adapter.get("selected_package", ""):
            errors.append("adapter package differs from frozen selection")

    archive = adapter.get("archive", {})
    archive_path = ROOT / archive.get("path", "")
    if not archive_path.is_file() or sha256(archive_path) != archive.get("sha256"):
        errors.append("archive path/hash mismatch")

    source_files = adapter.get("source_files", [])
    if not source_files:
        errors.append("source_files must not be empty")
    for item in source_files:
        path = ROOT / item.get("path", "")
        if not path.is_file() or sha256(path) != item.get("sha256"):
            errors.append(f"source path/hash mismatch: {item.get('path')}")

    mappings = adapter.get("role_mappings", {})
    if set(mappings) != ROLES:
        errors.append("role_mappings must cover exactly the six procedure-package roles")
    for role, mapping in mappings.items():
        if mapping.get("availability") not in AVAILABILITY or not mapping.get("locator"):
            errors.append(f"role {role} lacks typed availability/locator")

    observations = adapter.get("package_observations", {})
    for required in ("tool_contract", "procedure_relations", "accepted_alternatives", "runtime_replay", "final_artifact", "endpoint_observation", "procedure_observation"):
        value = observations.get(required, {})
        if value.get("availability") not in AVAILABILITY or not value.get("locator"):
            errors.append(f"observation {required} lacks typed availability/locator")

    findings = adapter.get("findings", [])
    if not findings:
        errors.append("at least one classified finding is required")
    for finding in findings:
        if finding.get("category") not in FINDING_CATEGORIES or not finding.get("code") or not finding.get("evidence"):
            errors.append("finding lacks valid category/code/evidence")
    if not NONCLAIMS <= set(adapter.get("claim_limits", [])):
        errors.append("required claim ceilings are missing")

    expected = adapter.get("expected_conformance")
    unavailable = any(item.get("availability") == "unavailable" for item in observations.values())
    defects = any(item.get("category") == "source-package-defect" for item in findings)
    derived = "reject" if defects else "insufficient_evidence" if unavailable else "pass"
    if expected != derived:
        errors.append(f"expected_conformance must fail closed as {derived}")
    return errors


def replay_sop_first_row(adapter: dict[str, Any]) -> dict[str, Any] | None:
    if adapter.get("instrument") != "SOP-Bench":
        return None
    base = ROOT / "pilots/procedure-package-released-validation/source/sop-bench/aircraft_inspection"
    spec = importlib.util.spec_from_file_location("released_aircraft_tools", base / "tools.py")
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load released tools.py")
    module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)
    except ModuleNotFoundError as exc:
        return {
            "tool": "VerifyAircraftClearance",
            "available": False,
            "reason": f"released runtime dependency unavailable: {exc.name}",
            "deterministic": None,
        }
    manager = module.AircraftInspectionManager()
    args = {
        "aircraft_id": "a_00127", "tail_number": "N12349",
        "maintenance_record_id": "mr_010014", "expected_departure_time": "2025-04-18T17:30:00Z",
    }
    values = [manager.VerifyAircraftClearance(**args), manager.VerifyAircraftClearance(**args)]
    digests = [hashlib.sha256(json.dumps(value, sort_keys=True, default=str).encode()).hexdigest() for value in values]
    return {"tool": "VerifyAircraftClearance", "arguments": args, "values": [str(v) for v in values], "digests": digests, "deterministic": len(set(digests)) == 1}


def build_report(path: Path) -> dict[str, Any]:
    adapter = json.loads(path.read_text(encoding="utf-8"))
    errors = validate_adapter(adapter)
    replay = replay_sop_first_row(adapter)
    if replay and replay["deterministic"] is False:
        errors.append("released SOP replay diverged")
    return {
        "adapter": str(path),
        "adapter_valid": not errors,
        "errors": errors,
        "conformance_outcome": adapter.get("expected_conformance") if not errors else "invalid_adapter",
        "finding_classifications": adapter.get("findings", []),
        "runtime_replay": replay,
        "claim_ceiling_enforced": NONCLAIMS <= set(adapter.get("claim_limits", [])),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("adapters", nargs="+", type=Path)
    parser.add_argument("--report-dir", type=Path)
    args = parser.parse_args()
    failed = False
    for path in args.adapters:
        report = build_report(path)
        failed |= not report["adapter_valid"]
        text = json.dumps(report, indent=2, sort_keys=True) + "\n"
        print(text, end="")
        if args.report_dir:
            args.report_dir.mkdir(parents=True, exist_ok=True)
            (args.report_dir / f"{path.stem}.report.json").write_text(text, encoding="utf-8")
    return int(failed)


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Freeze the distinct prospective replacement and replay zero-call conformance."""
from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
from typing import Any

import jsonschema

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
ADJ = ROOT / "pilots/action-boundary-composition/adjudication-v1/adjudication-report.json"
COMPONENTS = ["public-output.schema.json", "public-task.md", "semantic-alias-policy.json",
              "public-contract-grader-crosswalk.json", "grade.py", "runner.py", "freeze_protocol.py"]
ROWS = [
    (1, "vendor--current_authorized", "vendor", "current_authorized"),
    (2, "lh--stale_or_revoked", "lh", "stale_or_revoked"),
    (3, "vendor--conflicting", "vendor", "conflicting"),
    (4, "lh--current_authorized", "lh", "current_authorized"),
    (5, "vendor--stale_or_revoked", "vendor", "stale_or_revoked"),
    (6, "lh--conflicting", "lh", "conflicting"),
]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def module(name: str, path: Path) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


def pointer(value: Any, raw: str) -> Any:
    for token in raw.lstrip("/").split("/"):
        value = value[int(token)] if isinstance(value, list) else value[token.replace("~1", "/").replace("~0", "~")]
    return value


def interface_report() -> dict[str, Any]:
    schema = json.loads((HERE / "public-output.schema.json").read_text())
    crosswalk = json.loads((HERE / "public-contract-grader-crosswalk.json").read_text())
    policy = json.loads((HERE / "semantic-alias-policy.json").read_text())
    jsonschema.Draft202012Validator.check_schema(schema)
    errors: list[str] = []
    fields = []
    for row in crosswalk["rows"]:
        node = pointer(schema, row["schema_pointer"])
        declared = node.get("type")
        declared_types = [declared] if isinstance(declared, str) else declared
        # oneOf recovery_request declares null/object at branch roots.
        if row["path"] == "recovery_request":
            declared_types = [branch["type"] for branch in node["oneOf"]]
        if set(declared_types or []) != set(row["json_types"]):
            errors.append(f"type_drift:{row['path']}")
        schema_enums = node.get("enum", [])
        item_enums = node.get("items", {}).get("enum", []) if row["path"] == "safe_progress" else []
        if set(schema_enums or item_enums) != set(row["enums"]):
            errors.append(f"enum_drift:{row['path']}")
        fields.append({"path": row["path"], "json_type": "object" if row["path"] == "recovery_request" else row["json_types"][0]})
    expected_paths = {"decision", "target", "parameters", "recovery_request", "recovery_request.blocker_category",
                      "recovery_request.requested_authority", "safe_progress", "event_log", "event_log[].event_type",
                      "event_log[].target", "event_log[].parameters"}
    if {row["path"] for row in crosswalk["rows"]} != expected_paths:
        errors.append("grader_crosswalk_path_set_drift")
    interface = {"public_contract": {"agent_visible": True, "normative": True,
                 "schema_path": "public-output.schema.json", "fields": fields},
                 "grader_critical_fields": fields, "alias_policy": policy["aliases"]}
    validator = module("replacement_interface_validator", ROOT / "scripts/validate_public_interface_campaign.py")
    errors.extend(validator.interface_errors(interface))
    return {"kind": "replacement_public_interface_conformance", "model_calls": 0,
            "passed": not errors, "errors": sorted(set(errors)), "interface": interface,
            "schema_sha256": sha(HERE / "public-output.schema.json"),
            "crosswalk_sha256": sha(HERE / "public-contract-grader-crosswalk.json"),
            "alias_policy_sha256": sha(HERE / "semantic-alias-policy.json")}


def protocol() -> dict[str, Any]:
    adjudication = json.loads(ADJ.read_text())
    return {
        "version": "replacement-1.0.0",
        "status": "prospectively_frozen_zero_call_conformance_only",
        "distinct_from": ["pilots/action-boundary-composition/v1", "pilots/action-boundary-composition/v2"],
        "design_basis": {"path": str(ADJ.relative_to(ROOT)), "sha256": sha(ADJ),
                         "verified_frozen_evidence_hashes": adjudication["frozen_evidence_hashes"]},
        "objective": "Charter B/C: prospectively test an exact public action interface and fail-closed campaign controller across two unlike artifact forms.",
        "intended_rows": [{"order": order, "row_id": row_id, "form": form, "condition": condition}
                          for order, row_id, form, condition in ROWS],
        "configured_system": {"provider": "openai-codex", "model": "gpt-5.6-sol", "toolsets": ["file"],
                              "safe_mode": True, "max_turns": 50},
        "budgets": {"attempts_per_row": 1, "retries": 0, "wall_seconds_per_row": 900,
                    "max_total_model_calls": 36, "invalid_rows_remain_in_denominator": True},
        "campaign_policy": {"lazy_trial_materialization": True, "stop_before_next_launch_on":
                            ["service_invalid", "environment_invalid", "outer_orchestrator_timeout", "interrupted"],
                            "substitution_forbidden": True, "denominator_deletion_forbidden": True,
                            "remaining_rows_finalized_as": "not_launched_due_stop"},
        "public_interface": {"schema": "public-output.schema.json", "task": "public-task.md",
                             "crosswalk": "public-contract-grader-crosswalk.json",
                             "alias_policy": "semantic-alias-policy.json"},
        "component_hashes": [{"path": name, "sha256": sha(HERE / name)} for name in COMPONENTS],
        "claim_boundaries": {"capability": False, "treatment_effect": False, "cross_domain_generalization": False,
                             "expert_or_professional_validity": False, "safety": False, "production": False,
                             "readiness": False, "historical_repair_or_regrade": False},
        "execution_gate": "A later execution requires this exact pushed protocol and component hashes; this freeze itself authorizes no model call.",
    }


def main() -> int:
    report = interface_report()
    (HERE / "interface-conformance-report.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    (HERE / "protocol.json").write_text(json.dumps(protocol(), indent=2, sort_keys=True) + "\n")
    runner = module("replacement_campaign_runner", HERE / "runner.py")
    runner.main()
    campaigns = json.loads((HERE / "synthetic-campaign-report.json").read_text())
    control = {"interface": report["interface"], "campaign": campaigns["cases"]["normal_completion"]}
    (HERE / "interface-campaign-control.json").write_text(json.dumps(control, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"interface_passed": report["passed"], "model_calls": 0}, indent=2))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

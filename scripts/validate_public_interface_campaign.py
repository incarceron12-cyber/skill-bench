#!/usr/bin/env python3
"""Fail-closed checks for public output contracts and campaign stop ledgers."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

JSON_TYPES = {"null", "boolean", "number", "integer", "string", "array", "object"}


class ValidationFailure(Exception):
    """Raised when a public interface or campaign ledger is nonconformant."""


def interface_errors(record: dict[str, Any]) -> list[str]:
    """Require exact grader-critical paths/types in an agent-visible normative schema."""
    errors: list[str] = []
    schema = record.get("public_contract")
    if not isinstance(schema, dict):
        return ["missing_public_schema"]
    if schema.get("agent_visible") is not True:
        errors.append("schema_not_agent_visible")
    if schema.get("normative") is not True:
        errors.append("schema_not_normative")
    if not schema.get("schema_path"):
        errors.append("missing_schema_path")
    fields = schema.get("fields", [])
    disclosed: dict[str, str] = {}
    for field in fields:
        path, json_type = field.get("path"), field.get("json_type")
        if not isinstance(path, str) or not path:
            errors.append("invalid_disclosed_field_path")
        elif json_type not in JSON_TYPES:
            errors.append(f"invalid_disclosed_type:{path}")
        elif path in disclosed:
            errors.append(f"duplicate_disclosed_field:{path}")
        else:
            disclosed[path] = json_type
    aliases = record.get("alias_policy", [])
    alias_map: dict[str, tuple[str, str]] = {}
    for alias in aliases:
        source, target, policy = alias.get("alias"), alias.get("canonical"), alias.get("policy")
        if policy != "semantic_equivalence_reviewed":
            errors.append(f"unreviewed_alias:{source}")
        elif not isinstance(source, str) or not isinstance(target, str):
            errors.append("invalid_alias_policy")
        else:
            alias_map[source] = (target, policy)
    for critical in record.get("grader_critical_fields", []):
        path, expected_type = critical.get("path"), critical.get("json_type")
        if expected_type not in JSON_TYPES:
            errors.append(f"invalid_grader_type:{path}")
            continue
        if disclosed.get(path) == expected_type:
            continue
        reviewed_alias = any(
            target == path and disclosed.get(alias) == expected_type
            for alias, (target, _policy) in alias_map.items()
        )
        if not reviewed_alias:
            if path not in disclosed:
                errors.append(f"undisclosed_grader_field:{path}")
            else:
                errors.append(f"grader_public_type_mismatch:{path}:{disclosed[path]}!={expected_type}")
    return sorted(set(errors))


def campaign_errors(campaign: dict[str, Any]) -> list[str]:
    """Preserve the ITT frame and stop before a row after service/environment invalidity."""
    errors: list[str] = []
    intended = campaign.get("intended_rows", [])
    rows = campaign.get("rows", [])
    intended_ids = [row.get("row_id") for row in intended]
    observed_ids = [row.get("row_id") for row in rows]
    if campaign.get("strict_denominator") != len(intended):
        errors.append("strict_denominator_mismatch")
    if len(set(intended_ids)) != len(intended_ids):
        errors.append("duplicate_intended_row")
    if observed_ids != intended_ids:
        errors.append("intention_to_evaluate_frame_changed")
    stop_order: int | None = None
    allowed_statuses = {
        "completed_valid", "service_invalid", "environment_invalid",
        "outer_orchestrator_timeout", "interrupted", "not_launched_due_stop",
    }
    for index, row in enumerate(rows, start=1):
        invocations = row.get("launcher_invocations")
        if invocations not in {0, 1}:
            errors.append(f"retry_or_invalid_invocation_count:{row.get('row_id')}")
        if row.get("intention_to_evaluate") != 1:
            errors.append(f"denominator_row_deleted:{row.get('row_id')}")
        if stop_order is not None and invocations:
            errors.append(f"launched_after_stop:{row.get('row_id')}")
        service = row.get("service_valid")
        environment = row.get("environment_valid")
        invalidity = row.get("invalidity")
        invalid_attempt = invocations == 1 and (
            service is False
            or environment is False
            or invalidity in {"outer_orchestrator_timeout", "interrupted"}
        )
        if invalid_attempt and stop_order is None:
            stop_order = index
        if invocations == 0:
            if stop_order is None:
                errors.append(f"unexplained_not_launched:{row.get('row_id')}")
            if row.get("substantively_graded") is not False:
                errors.append(f"not_launched_marked_substantive:{row.get('row_id')}")
        if invalidity in {"outer_orchestrator_timeout", "interrupted"}:
            if invocations != 1 or row.get("substantively_graded") is not False:
                errors.append(f"bad_interruption_finalization:{row.get('row_id')}")
        # Replacement ledgers expose typed status and lazy materialization. Optional
        # fields keep historical adjudication records exactly replayable.
        if "status" in row:
            status = row.get("status")
            if status not in allowed_statuses:
                errors.append(f"invalid_row_status:{row.get('row_id')}")
            if invocations == 0 and status != "not_launched_due_stop":
                errors.append(f"unlaunched_status_mismatch:{row.get('row_id')}")
            if invocations == 1 and status == "not_launched_due_stop":
                errors.append(f"launched_status_mismatch:{row.get('row_id')}")
        if "materialized" in row and bool(row.get("materialized")) != (invocations == 1):
            errors.append(f"materialization_invocation_mismatch:{row.get('row_id')}")
    if campaign.get("retries", 0) != 0:
        errors.append("retry_count_nonzero")
    return sorted(set(errors))


def validate(record: dict[str, Any]) -> None:
    errors = interface_errors(record["interface"])
    errors.extend(campaign_errors(record["campaign"]))
    if errors:
        raise ValidationFailure("\n".join(f"- {error}" for error in sorted(set(errors))))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("record", type=Path)
    args = parser.parse_args()
    try:
        value = json.loads(args.record.read_text())
        validate(value)
    except (OSError, json.JSONDecodeError, KeyError, ValidationFailure) as exc:
        print(f"INVALID {args.record}\n{exc}", file=sys.stderr)
        return 1
    print(f"VALID {args.record}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

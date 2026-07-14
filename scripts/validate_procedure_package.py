#!/usr/bin/env python3
"""Validate cross-domain procedure/data/tool/oracle package conformance."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Iterable

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas/procedure-package.schema.json"
CONFLICT_MARKERS = ("<<<<<<<", "=======", ">>>>>>>")
REQUIRED_NONCLAIMS = {
    "expert approval", "professional correctness", "agent capability",
    "safety", "production fitness", "deployment readiness",
}


class ValidationFailure(Exception):
    pass


def duplicates(values: Iterable[str]) -> set[str]:
    seen: set[str] = set()
    out: set[str] = set()
    for value in values:
        if value in seen:
            out.add(value)
        seen.add(value)
    return out


def typed_equal(actual: Any, expected: Any, comparator: dict[str, Any]) -> bool:
    kind = comparator["kind"]
    if actual is None or expected is None:
        return actual is expected
    if kind in {"exact_enum", "exact_string", "boolean", "date", "json_schema"}:
        return type(actual) is type(expected) and actual == expected
    if kind == "number_tolerance":
        return isinstance(actual, (int, float)) and not isinstance(actual, bool) and abs(actual - expected) <= comparator.get("tolerance", 0)
    if kind == "set_equality":
        return isinstance(actual, list) and isinstance(expected, list) and set(actual) == set(expected)
    return False


def semantic_errors(package: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    unsupported = set(package["claim_limits"]["unsupported"])
    if not REQUIRED_NONCLAIMS <= unsupported:
        errors.append("claim_limits: internal fixture must retain all required non-claims")

    fields = package["fields"]
    for field_id in sorted(duplicates(item["field_id"] for item in fields)):
        errors.append(f"fields: duplicate field_id {field_id!r}")
    field_by_id = {item["field_id"]: item for item in fields}
    role_by_id = {key: value["role"] for key, value in field_by_id.items()}
    expected_surface = {
        "public_input": "public_task", "hidden_evidence": "hidden_table", "tool_result": "tool_only",
        "scored_endpoint": "final_artifact", "audit_metadata": "audit_only", "prohibited_oracle": "private_oracle",
    }
    for item in fields:
        if item["surface"] != expected_surface[item["role"]]:
            errors.append(f"field {item['field_id']}: role/surface mismatch")

    table = package["table_contract"]
    if set(table["metadata_columns"]) != set(table["observed_columns"]):
        errors.append("table_contract: missing/extra metadata columns")
    if table["manifest_row_count"] != table["loaded_row_count"]:
        errors.append("table_contract: manifest/loaded row count drift")
    if set(table["observed_columns"]) != set(field_by_id):
        errors.append("table_contract: observed columns must cover every and only declared field")
    for text in package["integrity_texts"]:
        if any(marker in text["content"] for marker in CONFLICT_MARKERS):
            errors.append(f"integrity_texts {text['path']}: unresolved conflict marker")

    tools = package["tools"]
    for tool_id in sorted(duplicates(item["tool_id"] for item in tools)):
        errors.append(f"tools: duplicate tool_id {tool_id!r}")
    tool_by_id = {item["tool_id"]: item for item in tools}
    for tool in tools:
        label = f"tool {tool['tool_id']}"
        for argument in tool["arguments"]:
            if argument["required"] and not argument["used_by_implementation"]:
                errors.append(f"{label}: required argument {argument['name']!r} is ignored by implementation")
        unknown = set(tool["return_field_ids"]) - set(field_by_id)
        if unknown:
            errors.append(f"{label}: unknown return field(s) {sorted(unknown)}")
        leaked = {field_id for field_id in tool["return_field_ids"] if role_by_id.get(field_id) in {"scored_endpoint", "prohibited_oracle"}}
        if tool["answer_bearing"] or leaked:
            errors.append(f"{label}: answer-bearing/prohibited oracle return")
        if not tool["deterministic"] or len(set(tool["replay_digests"])) != 1:
            errors.append(f"{label}: nondeterministic replay under frozen seed/time")

    oracle = package["oracle"]
    endpoint_ids = {key for key, role in role_by_id.items() if role == "scored_endpoint"}
    if set(oracle["endpoint_field_ids"]) != endpoint_ids:
        errors.append("oracle: endpoint coverage must equal scored_endpoint fields")
    if not oracle["independent_derivation"]:
        errors.append("oracle: expected endpoints require independent derivation")
    bad_oracle_inputs = {field_id for field_id in oracle["input_field_ids"] if role_by_id.get(field_id) in {None, "scored_endpoint", "prohibited_oracle"}}
    if bad_oracle_inputs:
        errors.append(f"oracle: invalid derivation input(s) {sorted(bad_oracle_inputs)}")
    frozen_oracle = package["frozen_execution"]["oracle_implementation"]
    if oracle["derivation_component"] != frozen_oracle:
        errors.append("oracle: derivation component differs from frozen oracle implementation")

    comparators = package["comparators"]
    if set(item["field_id"] for item in comparators) != endpoint_ids or len(comparators) != len(endpoint_ids):
        errors.append("comparators: require exactly one comparator per scored endpoint")
    comparator_by_field = {item["field_id"]: item for item in comparators}
    for comparator in comparators:
        if comparator["kind"] == "substring":
            errors.append(f"comparator {comparator['field_id']}: unrestricted substring matching is prohibited")
        if comparator["null_policy"] == "collapse_null_like":
            errors.append(f"comparator {comparator['field_id']}: null-like value collapse is prohibited")
        field = field_by_id.get(comparator["field_id"])
        kind_by_type = {"enum": "exact_enum", "string": "exact_string", "boolean": "boolean", "number": "number_tolerance", "date": "date", "set": "set_equality", "object": "json_schema"}
        if field and comparator["kind"] != kind_by_type[field["type"]]:
            errors.append(f"comparator {comparator['field_id']}: comparator kind does not match field type")

    procedure = package["procedure"]
    clauses = procedure["clauses"]
    clause_by_id = {item["clause_id"]: item for item in clauses}
    if len(clause_by_id) != len(clauses):
        errors.append("procedure: duplicate clause_id")
    source_ids = {item["source_id"] for item in package["provenance"]}
    for clause in clauses:
        if not clause["public_basis"] or not clause["evidence_source_ids"] or not set(clause["evidence_source_ids"]) <= source_ids:
            errors.append(f"clause {clause['clause_id']}: missing public/provenance basis")
    relations = procedure["relations"]
    relation_by_id = {item["relation_id"]: item for item in relations}
    if len(relation_by_id) != len(relations):
        errors.append("procedure: duplicate relation_id")
    for relation in relations:
        if relation["from_clause_id"] not in clause_by_id or relation["to_clause_id"] not in clause_by_id:
            errors.append(f"relation {relation['relation_id']}: unknown clause endpoint")
        if relation["kind"] in {"gate", "fallback"}:
            trigger = relation.get("trigger_field_id")
            if trigger not in field_by_id or "trigger_value" not in relation:
                errors.append(f"relation {relation['relation_id']}: trigger contract is incomplete")
    paths = procedure["accepted_paths"]
    path_by_id = {item["path_id"]: item for item in paths}
    if len(path_by_id) != len(paths):
        errors.append("procedure: duplicate path_id")
    for path in paths:
        if not set(path["required_clause_ids"]) <= set(clause_by_id) or not set(path["required_relation_ids"]) <= set(relation_by_id):
            errors.append(f"path {path['path_id']}: unknown clause/relation")

    reference_ids = set(oracle["reference_case_ids"])
    trial_ids = {item["trial_id"] for item in package["trials"]}
    if reference_ids != trial_ids:
        errors.append("oracle: reference_case_ids must cover every and only trial")
    required_case_kinds = {"canonical-pass", "alternative-pass", "skipped-gate", "wrong-order", "untriggered-fallback"}
    if not required_case_kinds <= trial_ids:
        errors.append("trials: conformance fixture lacks required planted cases")

    for trial in package["trials"]:
        label = f"trial {trial['trial_id']}"
        events = trial["events"]
        sequences = [event["sequence"] for event in events]
        if sequences != sorted(sequences) or len(sequences) != len(set(sequences)):
            errors.append(f"{label}: events must have unique ordered sequences")
        event_clause_ids = [event["clause_id"] for event in events]
        if not set(event_clause_ids) <= set(clause_by_id):
            errors.append(f"{label}: event references unknown clause")
        runtime_success = True
        for event in events:
            if event["kind"] == "tool_call":
                tool = tool_by_id.get(event.get("tool_id", ""))
                if tool is None:
                    errors.append(f"{label}: tool event references unknown tool")
                    runtime_success = False
                    continue
                expected_args = {arg["name"] for arg in tool["arguments"] if arg["required"]}
                if not expected_args <= set(event.get("arguments", {})):
                    errors.append(f"{label}: tool call missing required argument")
                runtime_success &= event.get("runtime_status") == "success"
        if trial["reported"]["runtime_metric_label"] != "runtime_execution":
            errors.append(f"{label}: runtime success is mislabeled as tool accuracy")
        if trial["reported"]["runtime_success"] != runtime_success:
            errors.append(f"{label}: runtime_success does not replay from tool events")
        if trial["final_artifact"]["endpoint_source"] != "final_artifact":
            errors.append(f"{label}: trace-derived endpoint cannot substitute for final artifact")

        actual = trial["final_artifact"]["values"]
        expected = {field_id: trial["case_values"].get(field_id) for field_id in endpoint_ids}
        endpoint_match = set(actual) == endpoint_ids and all(typed_equal(actual.get(field_id), expected[field_id], comparator_by_field[field_id]) for field_id in endpoint_ids if field_id in comparator_by_field)
        if trial["reported"]["endpoint_match"] != endpoint_match:
            errors.append(f"{label}: endpoint_match does not replay under typed comparators")

        positions: dict[str, list[int]] = {}
        for event in events:
            positions.setdefault(event["clause_id"], []).append(event["sequence"])
        satisfied_relations: set[str] = set()
        violated_relations: set[str] = set()
        for relation in relations:
            source = positions.get(relation["from_clause_id"], [])
            target = positions.get(relation["to_clause_id"], [])
            if relation["kind"] == "ordering":
                ok = bool(source and target and min(source) < min(target))
            else:
                triggered = trial["case_values"].get(relation["trigger_field_id"]) == relation["trigger_value"]
                if relation["kind"] == "gate":
                    ok = (not triggered) or bool(source and target and min(source) < min(target))
                else:
                    ok = (triggered and bool(target)) or (not triggered and not target)
            (satisfied_relations if ok else violated_relations).add(relation["relation_id"])
        accepted_paths = []
        for path in paths:
            if set(path["required_clause_ids"]) <= set(positions) and set(path["required_relation_ids"]) <= satisfied_relations:
                accepted_paths.append(path["path_id"])
        procedure_status = "conformant" if accepted_paths and not violated_relations else "procedure_wrong"
        reported = trial["reported"]
        if reported["accepted_path_ids"] != accepted_paths:
            errors.append(f"{label}: accepted_path_ids do not replay from clause/relation evidence")
        if reported["procedure_status"] != procedure_status:
            errors.append(f"{label}: procedure_status does not replay; violated={sorted(violated_relations)}")
        joint = "passed" if runtime_success and endpoint_match and procedure_status == "conformant" else "failed"
        if reported["joint_status"] != joint:
            errors.append(f"{label}: joint_status does not preserve runtime/endpoint/procedure separation")
    return errors


def validate_file(path: Path, check_paths: bool = False) -> None:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    package = json.loads(path.read_text(encoding="utf-8"))
    structural = [f"{'.'.join(map(str, error.absolute_path)) or '<root>'}: {error.message}" for error in Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(package)]
    errors = structural or semantic_errors(package)
    if check_paths:
        for source in package.get("provenance", []):
            if not (ROOT / source["local_path"]).is_file():
                errors.append(f"provenance local_path does not exist: {source['local_path']}")
    if errors:
        raise ValidationFailure("\n".join(f"- {item}" for item in errors))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("packages", nargs="+", type=Path)
    parser.add_argument("--check-paths", action="store_true")
    args = parser.parse_args()
    failed = False
    for path in args.packages:
        try:
            validate_file(path, args.check_paths)
            print(f"VALID {path}")
        except (OSError, json.JSONDecodeError, ValidationFailure) as exc:
            failed = True
            print(f"INVALID {path}\n{exc}")
    return int(failed)


if __name__ == "__main__":
    raise SystemExit(main())

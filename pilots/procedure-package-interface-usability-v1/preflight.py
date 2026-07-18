#!/usr/bin/env python3
"""Prospective zero-call validator for interface-usability v1."""
from __future__ import annotations

import argparse
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
CLAIMS = {"expert_provenance", "professional_validity", "transfer", "agent_capability", "utility", "production_fitness", "readiness"}
CASE_IDS = ["case-alpha", "case-beta", "case-heldout"]
FORBIDDEN_DIRS = {"tasks", "private-checks", "controls", "assignments", "executors", "trials", "generation"}

spec = importlib.util.spec_from_file_location("output_validator", ROOT / "scripts/validate_procedure_generation_output.py")
assert spec and spec.loader
output_validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(output_validator)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def all_false(value: Any) -> bool:
    return isinstance(value, dict) and set(value) == CLAIMS and all(item is False for item in value.values())


def materials(manifest: dict[str, Any]) -> dict[str, bytes]:
    return {
        item["path"]: (ROOT / item["path"]).read_bytes()
        for item in manifest.get("components", [])
        if (ROOT / item.get("path", "")).is_file()
    }


def example_errors() -> list[str]:
    source_path = HERE / "interface/example-source.json"
    package_path = HERE / "interface/example-package.json"
    source_bytes = source_path.read_bytes()
    package_bytes = package_path.read_bytes()
    policy = {
        "source_corpus_sha256": sha(source_bytes),
        "expected_family_id": "interface-example",
        "expected_family_version": "1.0.0",
        "allowed_visible_inputs": ["corpus.json", "interface-guide.md", "example-source.json", "example-package.json"],
        "forbidden_tokens": ["downstream_task", "private_check"],
        "forbidden_path_fragments": ["/tasks/", "private.json", "public.md"],
        "allowed_claim_ceiling": {key: False for key in CLAIMS},
    }
    return output_validator.validate_documents(load(package_path), package_bytes, load(source_path), source_bytes, policy)


def validate(protocol: dict[str, Any], manifest: dict[str, Any], frozen: dict[str, bytes], check_paths: bool = True) -> list[str]:
    errors: list[str] = []
    if protocol.get("status") != "prospectively_frozen_zero_call":
        errors.append("protocol is not at the zero-call prospective boundary")
    if not all_false(protocol.get("claim_ceiling")):
        errors.append("seven-claim ceiling drift")
    if protocol.get("attempt_ledger") != {"intended": 3, "attempted": 0, "service_valid": 0, "schema_valid": 0, "repair": 0, "retry": 0, "executor": 0}:
        errors.append("pre-call attempt ledger drift")
    config = protocol.get("generation_configuration", {})
    if config.get("order") != CASE_IDS or config.get("attempts_per_case") != 1 or config.get("repairs") != 0 or config.get("retries") != 0:
        errors.append("case order or one-shot rules drift")
    if config.get("model") != "gpt-5.6-sol" or config.get("provider") != "openai-codex" or config.get("toolsets") != ["file"]:
        errors.append("configured-system identity drift")
    if config.get("included_cost_ceiling_usd_per_case") != 0.0:
        errors.append("included cost ceiling drift")

    cases = protocol.get("cases", [])
    if [row.get("case_id") for row in cases] != CASE_IDS:
        errors.append("case inventory/order drift")
    if [row.get("role") for row in cases].count("held_out_conformance") != 1 or cases[-1].get("case_id") != "case-heldout":
        errors.append("held-out boundary drift")
    if len({row.get("structure") for row in cases}) != 3:
        errors.append("cases are not structurally varied")

    component_rows = manifest.get("components", [])
    paths = [row.get("path") for row in component_rows]
    if len(paths) != len(set(paths)):
        errors.append("duplicate frozen component path")
    required_roles = {"protocol", "interface_guide", "interface_example_source", "interface_example_package", "contract_schema", "contract_validator", "preflight_validator", "generation_launcher"}
    if not required_roles <= {row.get("role") for row in component_rows}:
        errors.append("frozen role inventory incomplete")
    for row in component_rows:
        data = frozen.get(row.get("path", ""))
        if data is None:
            errors.append(f"missing frozen component: {row.get('path')}")
        elif sha(data) != row.get("sha256"):
            errors.append(f"hash drift: {row.get('path')}")

    for case in cases:
        case_id = case["case_id"]
        source_path, policy_path = case["source_path"], case["policy_path"]
        try:
            source_bytes, policy_bytes = frozen[source_path], frozen[policy_path]
            source, policy = json.loads(source_bytes), json.loads(policy_bytes)
        except (KeyError, json.JSONDecodeError) as exc:
            errors.append(f"missing or invalid case material {case_id}: {exc}")
            continue
        if source.get("family_id") != policy.get("expected_family_id") or source.get("family_version") != policy.get("expected_family_version"):
            errors.append(f"source/policy identity drift: {case_id}")
        if sha(source_bytes) != policy.get("source_corpus_sha256"):
            errors.append(f"source/policy hash drift: {case_id}")
        if policy.get("allowed_visible_inputs") != ["corpus.json", "interface-guide.md", "example-source.json", "example-package.json"]:
            errors.append(f"visible input envelope drift: {case_id}")
        authority = source.get("authority_scope", {})
        if authority.get("authority") != "builder-authored internal calibration only" or authority.get("origin") != "internal_design_hypothesis" or authority.get("source_url") is not None:
            errors.append(f"source authority laundering: {case_id}")
        ids = [row.get("id") for row in source.get("propositions", [])]
        if not ids or len(ids) != len(set(ids)):
            errors.append(f"invalid proposition identities: {case_id}")
        source_text = source_bytes.decode("utf-8", errors="replace").casefold()
        for token in ("downstream_task", "private_check", "executor_assignment", "pretask-procedure-transfer-v4"):
            if token in source_text:
                errors.append(f"downstream token leaked into case source: {case_id}/{token}")

    if example_errors():
        errors.extend(f"interface example invalid: {item}" for item in example_errors())
    pin = protocol.get("contract_pin", {})
    for key in ("schema", "validator"):
        path = pin.get(f"{key}_path", "")
        data = frozen.get(path)
        if data is None or sha(data) != pin.get(f"{key}_sha256"):
            errors.append(f"contract {key} pin drift")
    if check_paths:
        present = {path.name for path in HERE.iterdir() if path.is_dir()}
        for forbidden in sorted(FORBIDDEN_DIRS & present):
            errors.append(f"prohibited pre-call directory exists: {forbidden}")
    return errors


def mutation_results(protocol: dict[str, Any], manifest: dict[str, Any], frozen: dict[str, bytes]) -> dict[str, list[str]]:
    cases: dict[str, tuple[dict[str, Any], dict[str, Any], dict[str, bytes]]] = {}
    changed_bytes = dict(frozen)
    guide_path = "pilots/procedure-package-interface-usability-v1/interface/interface-guide.md"
    changed_bytes[guide_path] += b"\npost-outcome edit\n"
    cases["post_outcome_interface_edit"] = (protocol, manifest, changed_bytes)
    changed_protocol = copy.deepcopy(protocol)
    changed_protocol["cases"][-1]["role"] = "development_conformance"
    cases["heldout_role_edit"] = (changed_protocol, manifest, frozen)
    changed_protocol = copy.deepcopy(protocol)
    changed_protocol["generation_configuration"]["retries"] = 1
    cases["retry_upgrade"] = (changed_protocol, manifest, frozen)
    changed_protocol = copy.deepcopy(protocol)
    changed_protocol["contract_pin"]["schema_sha256"] = "0" * 64
    cases["schema_pin_mutation"] = (changed_protocol, manifest, frozen)
    return {name: validate(p, m, b, check_paths=False) for name, (p, m, b) in cases.items()}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check-paths", action="store_true")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    protocol, manifest = load(HERE / "protocol.json"), load(HERE / "freeze-manifest.json")
    frozen = materials(manifest)
    errors = validate(protocol, manifest, frozen, check_paths=args.check_paths)
    mutations = mutation_results(protocol, manifest, frozen)
    for name, mutation_errors in mutations.items():
        if not mutation_errors:
            errors.append(f"required mutation was accepted: {name}")
    report = {
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "gates": {
            "source_task_separation": "pass" if not errors else "fail",
            "hash_freeze": "pass" if not errors else "fail",
            "interface_example_conformance": "pass" if not errors else "fail",
            "schema_mutation_rejection": "pass" if not errors else "fail",
            "post_outcome_edit_rejection": "pass" if not errors else "fail"
        },
        "mutation_error_counts": {name: len(items) for name, items in mutations.items()},
        "attempt_ledger": protocol.get("attempt_ledger"),
        "generation_authorized": not errors,
        "claim_ceiling_all_false": all_false(protocol.get("claim_ceiling"))
    }
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.report:
        args.report.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

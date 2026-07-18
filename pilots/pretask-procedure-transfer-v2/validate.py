#!/usr/bin/env python3
"""Validate prospective source/task separation for procedure-transfer v2."""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from datetime import datetime
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
CLAIMS = {
    "expert_provenance", "professional_validity", "transfer", "agent_capability",
    "utility", "production_fitness", "readiness",
}
REQUIRED_INPUT_GATES = {
    "two_structurally_unlike_families", "separately_versioned_source_corpora",
    "proposition_provenance_and_claim_ceiling", "two_new_untouched_forms_per_family",
    "public_basis_without_complete_procedure_copy", "source_frozen_before_task_and_package",
    "generator_view_task_identifier_scrub", "independent_endpoint_specs_frozen",
}


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def parse_time(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def load_materials(audit: dict[str, Any]) -> dict[str, bytes]:
    materials: dict[str, bytes] = {}
    for item in audit.get("component_hashes", []):
        path = item.get("path", "")
        candidate = ROOT / path
        if candidate.is_file():
            materials[path] = candidate.read_bytes()
    return materials


def as_json(materials: dict[str, bytes], path: str, errors: list[str]) -> dict[str, Any]:
    try:
        return json.loads(materials[path])
    except KeyError:
        errors.append(f"missing material: {path}")
    except (json.JSONDecodeError, UnicodeDecodeError) as exc:
        errors.append(f"invalid JSON material {path}: {exc}")
    return {}


def validate(protocol: dict[str, Any], audit: dict[str, Any], materials: dict[str, bytes], *, check_paths: bool = True) -> list[str]:
    errors: list[str] = []
    if protocol.get("status") != "input_prerequisites_frozen_no_packages_no_calls":
        errors.append("protocol status drift")
    for label, claims in (("protocol", protocol.get("claim_boundaries", {})), ("audit", audit.get("claim_boundaries", {}))):
        if set(claims) != CLAIMS or any(value is not False for value in claims.values()):
            errors.append(f"{label} claim ceiling drift")
    attempts = protocol.get("attempt_ledger", {})
    required_zero = ["package_generation_attempts", "model_attempts", "provider_attempts", "executor_attempts"]
    if any(attempts.get(key) != 0 for key in required_zero):
        errors.append("protocol attempt ledger must remain zero")
    if audit.get("model_calls") != 0 or audit.get("provider_attempts") != 0 or audit.get("package_generation_attempts") != 0:
        errors.append("audit must preserve zero calls and package attempts")
    if protocol.get("chronology", {}).get("package_generation_started_at") is not None:
        errors.append("package generation timestamp must remain absent")

    components = audit.get("component_hashes", [])
    component_paths = [item.get("path") for item in components]
    if len(component_paths) != len(set(component_paths)):
        errors.append("duplicate frozen component path")
    if check_paths:
        for item in components:
            path = item.get("path", "")
            data = materials.get(path)
            if data is None:
                errors.append(f"missing frozen component: {path}")
            elif sha(data) != item.get("sha256"):
                errors.append(f"hash drift: {path}")

    families = protocol.get("families", [])
    inventory = protocol.get("task_inventory", [])
    if len(families) != 2 or len(inventory) != 4:
        errors.append("inventory must be two families x two tasks")
    family_ids = {family.get("family_id") for family in families}
    if len(family_ids) != 2 or any(sum(row.get("family_id") == fid for row in inventory) != 2 for fid in family_ids):
        errors.append("each distinct family must bind exactly two tasks")
    if len({family.get("structure") for family in families}) != 2:
        errors.append("families must remain structurally unlike")

    split = protocol.get("source_task_split", {})
    visible = split.get("generator_visible_inputs", [])
    corpus_paths = [family.get("corpus_path") for family in families]
    if set(visible) != set(corpus_paths) or any("/tasks/" in path for path in visible):
        errors.append("generator view must contain only both family corpora")
    scrub = protocol.get("leakage_scrubs", {})
    forbidden_tokens = scrub.get("forbidden_generator_tokens", [])
    forbidden_paths = scrub.get("forbidden_generator_path_fragments", [])
    generator_text = split.get("generator_instruction", "")
    for path in visible:
        try:
            generator_text += "\n" + materials[path].decode("utf-8")
        except (KeyError, UnicodeDecodeError):
            errors.append(f"generator-visible corpus unavailable: {path}")
    lowered_generator = generator_text.casefold()
    for token in forbidden_tokens:
        if token.casefold() in lowered_generator:
            errors.append(f"task identifier/output token in generator-visible input: {token}")
    for fragment in forbidden_paths:
        if any(fragment.casefold() in path.casefold() for path in visible):
            errors.append(f"task path in generator-visible input: {fragment}")

    corpus_by_family: dict[str, dict[str, Any]] = {}
    proposition_ids: dict[str, set[str]] = {}
    freeze_by_family: dict[str, datetime] = {}
    for family in families:
        path = family.get("corpus_path", "")
        corpus = as_json(materials, path, errors)
        fid = family.get("family_id")
        corpus_by_family[fid] = corpus
        if corpus.get("family_id") != fid or corpus.get("family_version") != "1.0.0":
            errors.append(f"family corpus identity/version mismatch: {fid}")
        if family.get("corpus_sha256") != next((x.get("sha256") for x in components if x.get("path") == path), None):
            errors.append(f"family/audit corpus hash mismatch: {fid}")
        authority = corpus.get("authority_scope", {})
        if authority.get("authority") != "builder-authored internal calibration only" or authority.get("source_url") is not None:
            errors.append(f"corpus authority laundering: {fid}")
        try:
            frozen_at = parse_time(corpus["frozen_at"])
            freeze_by_family[fid] = frozen_at
        except (KeyError, TypeError, ValueError):
            errors.append(f"invalid corpus freeze time: {fid}")
            continue
        ids: set[str] = set()
        for prop in corpus.get("propositions", []):
            pid = prop.get("id")
            if not pid or pid in ids:
                errors.append(f"duplicate/empty proposition id: {fid}")
            ids.add(pid)
            if prop.get("origin") != "internal_design_hypothesis":
                errors.append(f"source proposition inferred from private check or untyped authority: {pid}")
            if prop.get("exact_locator") != f"this file:propositions[{pid}]":
                errors.append(f"non-exact proposition locator: {pid}")
            try:
                if parse_time(prop["authored_at"]) >= frozen_at:
                    errors.append(f"proposition not authored before corpus freeze: {pid}")
            except (KeyError, TypeError, ValueError):
                errors.append(f"invalid proposition time: {pid}")
            for key in ("statement", "authority", "scope", "valid_time"):
                if not prop.get(key):
                    errors.append(f"proposition missing {key}: {pid}")
        proposition_ids[fid] = ids
        if not corpus.get("contradictions") or not corpus.get("decision_thresholds") or not corpus.get("artifact_conventions") or not corpus.get("failure_signatures"):
            errors.append(f"corpus missing required design primitives: {fid}")

    seen_tasks: set[str] = set()
    for row in inventory:
        tid, fid = row.get("task_id"), row.get("family_id")
        if tid in seen_tasks or tid not in scrub.get("opaque_task_ids", []):
            errors.append(f"task id not unique/opaque inventory-bound: {tid}")
        seen_tasks.add(tid)
        public_path, private_path = row.get("public_path", ""), row.get("private_path", "")
        try:
            public = materials[public_path].decode("utf-8")
        except (KeyError, UnicodeDecodeError):
            errors.append(f"missing/invalid public task: {tid}")
            public = ""
        private = as_json(materials, private_path, errors)
        if private.get("task_id") != tid or private.get("family_id") != fid:
            errors.append(f"task/private identity mismatch: {tid}")
        if private.get("model_attempts") != 0 or private.get("provider_attempts") != 0:
            errors.append(f"task no longer untouched: {tid}")
        try:
            if parse_time(private["authored_at"]) <= freeze_by_family[fid]:
                errors.append(f"task not authored after source freeze: {tid}")
        except (KeyError, TypeError, ValueError):
            errors.append(f"invalid task chronology: {tid}")
        for heading in ("## Objective", "## Inputs", "## Deliverable", "## Fair consequence basis"):
            if heading not in public:
                errors.append(f"public prompt missing {heading}: {tid}")
        corpus = corpus_by_family.get(fid, {})
        for signature in corpus.get("leakage_signatures", []):
            if signature.casefold() in public.casefold():
                errors.append(f"complete procedure leakage in public prompt {tid}: {signature}")
        for prop in corpus.get("propositions", []):
            if prop.get("statement", "").casefold() in public.casefold():
                errors.append(f"verbatim source proposition leaked into public prompt: {tid}/{prop.get('id')}")
        checks = private.get("checks", [])
        if not checks:
            errors.append(f"private task has no endpoint checks: {tid}")
        for check in checks:
            basis = check.get("public_basis")
            if not isinstance(basis, str) or basis not in public:
                errors.append(f"hidden obligation without exact public basis: {tid}/{check.get('id')}")
            pids = check.get("proposition_basis", [])
            if not pids or any(pid not in proposition_ids.get(fid, set()) for pid in pids):
                errors.append(f"private check lacks valid source proposition: {tid}/{check.get('id')}")

    audit_gates = {row.get("gate"): row.get("status") for row in audit.get("input_gate_results", [])}
    if set(audit_gates) != REQUIRED_INPUT_GATES or any(status != "pass" for status in audit_gates.values()):
        errors.append("input gate inventory/status drift")
    if any(row.get("status") == "pass" for row in audit.get("execution_gates", [])):
        errors.append("execution gate prematurely passed")
    if audit.get("status") != "input_prerequisites_pass_execution_not_authorized":
        errors.append("audit must not authorize execution")
    if (HERE / "packages").exists():
        errors.append("procedure/control package directory exists before authorized continuation")
    return errors


def mutation_self_test(protocol: dict[str, Any], audit: dict[str, Any], materials: dict[str, bytes]) -> list[str]:
    failures: list[str] = []
    cases: list[tuple[str, dict[str, Any], dict[str, Any], dict[str, bytes]]] = []

    a = copy.deepcopy(audit); a["component_hashes"][1]["sha256"] = "0" * 64
    cases.append(("corpus hash drift", protocol, a, materials))
    a = copy.deepcopy(audit); task = next(x for x in a["component_hashes"] if x["role"] == "public_task"); task["sha256"] = "0" * 64
    cases.append(("task hash drift", protocol, a, materials))
    m = dict(materials); path = "pilots/pretask-procedure-transfer-v2/tasks/q7m2/public.md"; m[path] += b"\nAt least two independent eligible supporting records.\n"
    cases.append(("procedure leakage", protocol, audit, m))
    m = dict(materials); path = "pilots/pretask-procedure-transfer-v2/tasks/q7m2/private.json"; data = json.loads(m[path]); data["checks"][0]["public_basis"] = "Undisclosed mandatory rule"; m[path] = json.dumps(data).encode()
    cases.append(("hidden obligation", protocol, audit, m))
    m = dict(materials); path = "pilots/pretask-procedure-transfer-v2/families/evidence-decision/corpus.json"; data = json.loads(m[path]); data["propositions"][0]["origin"] = "inferred_from_private_check"; m[path] = json.dumps(data).encode()
    cases.append(("private-check-inferred proposition", protocol, audit, m))
    p = copy.deepcopy(protocol); p["source_task_split"]["generator_instruction"] += " q7m2"
    cases.append(("task id in generator input", p, audit, materials))
    for name, p, a, m in cases:
        if not validate(p, a, m, check_paths=True):
            failures.append(name)
    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check-paths", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    protocol = json.loads((HERE / "protocol.json").read_text())
    audit = json.loads((HERE / "readiness-audit.json").read_text())
    materials = load_materials(audit)
    errors = validate(protocol, audit, materials, check_paths=args.check_paths)
    if args.self_test:
        failures = mutation_self_test(protocol, audit, materials)
        if failures:
            errors.append("mutations not rejected: " + ", ".join(failures))
    print(json.dumps({
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "input_prerequisites": "frozen",
        "execution_authorized": False,
        "package_generation_attempts": 0,
        "model_calls": 0,
        "provider_attempts": 0,
    }, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

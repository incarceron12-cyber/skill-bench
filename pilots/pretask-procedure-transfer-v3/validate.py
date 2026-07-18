#!/usr/bin/env python3
"""Zero-call prospective freeze validator for pre-task procedure transfer v3."""
from __future__ import annotations

import argparse
import copy
import hashlib
import importlib.util
import json
from datetime import datetime
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
CONTRACT_COMMIT = "a3640af8b7e0788fcc90aace9fc587ea42d50d0a"
CLAIMS = {
    "expert_provenance", "professional_validity", "transfer", "agent_capability",
    "utility", "production_fitness", "readiness",
}
DISALLOWED_FREEZE_PATHS = ("generation", "packages", "controls", "checkers", "trials")
REQUIRED_GATES = {
    "contract_commit_and_hash_pin",
    "entirely_new_v3_bytes",
    "source_before_task_chronology",
    "exact_component_hashes",
    "two_unlike_families_two_opaque_forms_each",
    "source_authority_and_proposition_integrity",
    "source_only_generation_visibility",
    "task_and_private_leakage_scrub",
    "private_checks_have_exact_public_bases",
    "exhaustive_reference_package_bindings",
    "required_mutations_rejected",
    "zero_attempt_ledger_and_claim_ceiling",
}

spec = importlib.util.spec_from_file_location(
    "procedure_generation_output_validator",
    ROOT / "scripts/validate_procedure_generation_output.py",
)
assert spec is not None and spec.loader is not None
output_validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(output_validator)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def parse_time(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_materials(manifest: dict[str, Any]) -> dict[str, bytes]:
    materials: dict[str, bytes] = {}
    for item in manifest.get("component_hashes", []):
        path = item.get("path", "")
        candidate = ROOT / path
        if candidate.is_file():
            materials[path] = candidate.read_bytes()
    return materials


def material_json(materials: dict[str, bytes], path: str, errors: list[str]) -> dict[str, Any]:
    try:
        return json.loads(materials[path])
    except KeyError:
        errors.append(f"missing frozen material: {path}")
    except (json.JSONDecodeError, UnicodeDecodeError) as exc:
        errors.append(f"invalid JSON material {path}: {exc}")
    return {}


def all_false_claims(value: Any) -> bool:
    return isinstance(value, dict) and set(value) == CLAIMS and all(item is False for item in value.values())


def historical_hashes() -> set[str]:
    hashes: set[str] = set()
    for version in ("pretask-procedure-transfer-v1", "pretask-procedure-transfer-v2"):
        base = ROOT / "pilots" / version
        if base.is_dir():
            for path in base.rglob("*"):
                if path.is_file():
                    hashes.add(sha(path.read_bytes()))
    return hashes


def reference_mutation_results(
    package: dict[str, Any], source: dict[str, Any], source_bytes: bytes, policy: dict[str, Any]
) -> dict[str, list[str]]:
    cases: dict[str, tuple[dict[str, Any], dict[str, Any] | None]] = {}

    changed = copy.deepcopy(package)
    changed["package_id"] = None
    cases["null_identity"] = (changed, None)

    changed = copy.deepcopy(package)
    changed["package_id"] = None
    changed_bytes = json.dumps(changed, sort_keys=True).encode("utf-8")
    cases["false_launcher_acceptance"] = (
        changed,
        {"launcher_valid": True, "package_sha256": sha(changed_bytes)},
    )

    changed = copy.deepcopy(package)
    changed["failure_signatures"].pop()
    cases["silent_omission"] = (changed, None)

    changed = copy.deepcopy(package)
    changed["contradictions"][0]["proposition_basis"] = ["UNKNOWN-PROPOSITION"]
    cases["invalid_proposition_basis"] = (changed, None)

    changed = copy.deepcopy(package)
    changed["claim_ceiling"]["transfer"] = True
    cases["claim_upgrade"] = (changed, None)

    results: dict[str, list[str]] = {}
    for name, (candidate, report) in cases.items():
        candidate_bytes = json.dumps(candidate, sort_keys=True).encode("utf-8")
        results[name] = output_validator.validate_documents(
            candidate, candidate_bytes, source, source_bytes, policy, report
        )
    return results


def validate(
    protocol: dict[str, Any],
    manifest: dict[str, Any],
    materials: dict[str, bytes],
    *,
    check_paths: bool = True,
    check_historical: bool = True,
) -> tuple[list[str], dict[str, Any]]:
    errors: list[str] = []
    evidence: dict[str, Any] = {"reference_packages": {}, "mutations": {}}

    if protocol.get("status") != "prospectively_frozen_generation_not_authorized":
        errors.append("protocol status does not preserve frozen generation-not-authorized boundary")
    if manifest.get("status") != "frozen_zero_call_preflight" or manifest.get("execution_authorized") is not False:
        errors.append("manifest execution authorization/status drift")
    for label, claims in (("protocol", protocol.get("claim_boundaries")), ("manifest", manifest.get("claim_boundaries"))):
        if not all_false_claims(claims):
            errors.append(f"{label} claim ceiling drift")
    expected_attempts = {"package_generation_attempts": 0, "model_attempts": 0, "provider_attempts": 0, "executor_attempts": 0}
    if protocol.get("attempt_ledger") != expected_attempts:
        errors.append("protocol attempt ledger is not exactly zero")
    if manifest.get("attempts") != {"package_generation": 0, "model": 0, "provider": 0, "executor": 0}:
        errors.append("manifest attempt ledger is not exactly zero")
    if set(manifest.get("preflight_gates", [])) != REQUIRED_GATES:
        errors.append("preflight gate inventory drift")

    components = manifest.get("component_hashes", [])
    paths = [item.get("path") for item in components]
    if len(paths) != len(set(paths)):
        errors.append("duplicate frozen component path")
    if check_paths:
        for item in components:
            path = item.get("path", "")
            data = materials.get(path)
            if data is None:
                errors.append(f"missing frozen component: {path}")
            elif sha(data) != item.get("sha256"):
                errors.append(f"hash drift: {path}")

    pin = protocol.get("contract_pin", {})
    if pin.get("validator_commit") != CONTRACT_COMMIT:
        errors.append("procedure output validator commit pin drift")
    for key, role in (("schema", "contract_schema"), ("validator", "contract_validator")):
        path = pin.get(f"{key}_path", "")
        digest = pin.get(f"{key}_sha256")
        component = next((row for row in components if row.get("role") == role), {})
        if component.get("path") != path or component.get("sha256") != digest:
            errors.append(f"contract {key} pin does not match frozen manifest")

    if check_historical:
        old_hashes = historical_hashes()
        for item in components:
            if item.get("role") in {"source_corpus", "generation_policy", "builder_reference_conformance_witness", "public_task", "private_endpoint_spec"}:
                if item.get("sha256") in old_hashes:
                    errors.append(f"v3 component reuses exact v1/v2 bytes: {item.get('path')}")

    try:
        chronology = protocol["chronology"]
        if not (
            parse_time(chronology["contract_committed_at"])
            < parse_time(chronology["source_authoring_started_at"])
            < parse_time(chronology["all_sources_frozen_at"])
            < parse_time(chronology["task_authoring_started_at"])
            < parse_time(chronology["protocol_frozen_at"])
        ):
            errors.append("top-level source-before-task chronology is not strictly ordered")
    except (KeyError, TypeError, ValueError):
        errors.append("invalid top-level chronology")

    families = protocol.get("families", [])
    inventory = protocol.get("task_inventory", [])
    if len(families) != 2 or len(inventory) != 4:
        errors.append("inventory must contain two families and four tasks")
    if len({row.get("family_id") for row in families}) != 2 or len({row.get("structure") for row in families}) != 2:
        errors.append("families are not distinct and structurally unlike")

    scrub = protocol.get("leakage_scrubs", {})
    forbidden_tokens = scrub.get("forbidden_generator_tokens", [])
    forbidden_fragments = scrub.get("forbidden_generator_path_fragments", [])
    corpus_by_family: dict[str, dict[str, Any]] = {}
    proposition_ids: dict[str, set[str]] = {}
    freeze_times: dict[str, datetime] = {}

    for family in families:
        fid = family.get("family_id", "")
        corpus_path = family.get("corpus_path", "")
        corpus_bytes = materials.get(corpus_path, b"")
        corpus = material_json(materials, corpus_path, errors)
        corpus_by_family[fid] = corpus
        if corpus.get("family_id") != fid or corpus.get("family_version") != "1.0.0":
            errors.append(f"source identity/version mismatch: {fid}")
        if family.get("corpus_sha256") != sha(corpus_bytes):
            errors.append(f"family corpus hash mismatch: {fid}")
        authority = corpus.get("authority_scope", {})
        if authority.get("authority") != "builder-authored internal calibration only" or authority.get("source_url") is not None or authority.get("origin") != "internal_design_hypothesis":
            errors.append(f"source authority laundering: {fid}")
        try:
            freeze = parse_time(corpus["frozen_at"])
            freeze_times[fid] = freeze
        except (KeyError, TypeError, ValueError):
            errors.append(f"invalid source freeze time: {fid}")
            continue
        ids: set[str] = set()
        for proposition in corpus.get("propositions", []):
            pid = proposition.get("id")
            if not pid or pid in ids:
                errors.append(f"empty or duplicate proposition id: {fid}")
            ids.add(pid)
            if proposition.get("origin") != "internal_design_hypothesis":
                errors.append(f"proposition authority drift: {pid}")
            if proposition.get("exact_locator") != f"this file:propositions[{pid}]":
                errors.append(f"non-exact proposition locator: {pid}")
            try:
                if parse_time(proposition["authored_at"]) >= freeze:
                    errors.append(f"proposition not authored before source freeze: {pid}")
            except (KeyError, TypeError, ValueError):
                errors.append(f"invalid proposition chronology: {pid}")
            for field in ("statement", "authority", "scope", "valid_time"):
                if not proposition.get(field):
                    errors.append(f"proposition missing {field}: {pid}")
        proposition_ids[fid] = ids
        for key in ("contradictions", "decision_thresholds", "artifact_conventions", "failure_signatures"):
            rows = corpus.get(key, [])
            if not rows or len({row.get("id") for row in rows}) != len(rows):
                errors.append(f"missing or duplicate source primitive {key}: {fid}")

        policy_path = family.get("policy_path", "")
        policy = material_json(materials, policy_path, errors)
        reference_path = family.get("reference_package_path", "")
        reference_bytes = materials.get(reference_path, b"")
        reference = material_json(materials, reference_path, errors)
        if policy.get("contract") != pin:
            errors.append(f"generation policy contract pin drift: {fid}")
        if policy.get("source_corpus_path") != corpus_path or policy.get("source_corpus_sha256") != sha(corpus_bytes):
            errors.append(f"generation policy source identity drift: {fid}")
        if policy.get("allowed_visible_inputs") != [corpus_path]:
            errors.append(f"generation view is not exactly one source corpus: {fid}")
        if policy.get("reference_package_path") != reference_path:
            errors.append(f"reference package policy binding drift: {fid}")
        if set(policy.get("forbidden_tokens", [])) != set(forbidden_tokens) or set(policy.get("forbidden_path_fragments", [])) != set(forbidden_fragments):
            errors.append(f"family leakage policy differs from protocol: {fid}")
        for path in policy.get("allowed_visible_inputs", []):
            if any(fragment.casefold() in path.casefold() for fragment in forbidden_fragments):
                errors.append(f"forbidden path in generation view: {fid}/{path}")
        generator_visible_text = corpus_bytes.decode("utf-8", errors="replace") + "\n" + reference_bytes.decode("utf-8", errors="replace")
        for token in forbidden_tokens:
            if token.casefold() in generator_visible_text.casefold():
                errors.append(f"task/private token leaked into source/reference bytes: {fid}/{token}")
        reference_errors = output_validator.validate_documents(
            reference, reference_bytes, corpus, corpus_bytes, policy
        )
        evidence["reference_packages"][fid] = {"errors": reference_errors, "sha256": sha(reference_bytes)}
        if reference_errors:
            errors.extend(f"reference package {fid}: {error}" for error in reference_errors)
        mutations = reference_mutation_results(reference, corpus, corpus_bytes, policy)
        evidence["mutations"][fid] = {name: values for name, values in mutations.items()}
        expected_markers = {
            "null_identity": "None is not of type 'string'",
            "false_launcher_acceptance": "false launcher acceptance",
            "silent_omission": "project or explicitly omit",
            "invalid_proposition_basis": "invalid proposition basis",
            "claim_upgrade": "False was expected",
        }
        for name, marker in expected_markers.items():
            if not mutations.get(name) or not any(marker in error for error in mutations[name]):
                errors.append(f"required mutation not rejected for declared reason: {fid}/{name}")

    task_ids = [row.get("task_id") for row in inventory]
    if len(task_ids) != len(set(task_ids)) or set(task_ids) != set(scrub.get("opaque_task_ids", [])):
        errors.append("opaque task inventory/scrub mismatch")
    for family in families:
        fid = family.get("family_id")
        if set(family.get("task_ids", [])) != {row.get("task_id") for row in inventory if row.get("family_id") == fid} or len(family.get("task_ids", [])) != 2:
            errors.append(f"family does not bind exactly two task forms: {fid}")

    for row in inventory:
        tid, fid = row.get("task_id"), row.get("family_id")
        public_path, private_path = row.get("public_path", ""), row.get("private_path", "")
        try:
            public = materials[public_path].decode("utf-8")
        except (KeyError, UnicodeDecodeError):
            errors.append(f"missing or invalid public task: {tid}")
            public = ""
        private = material_json(materials, private_path, errors)
        if private.get("task_id") != tid or private.get("family_id") != fid:
            errors.append(f"private endpoint identity mismatch: {tid}")
        if any(private.get(key) != 0 for key in ("model_attempts", "provider_attempts", "executor_attempts")):
            errors.append(f"task form is no longer untouched: {tid}")
        try:
            authored = parse_time(row["authored_at"])
            if authored != parse_time(private["authored_at"]) or authored <= freeze_times[fid]:
                errors.append(f"task/private chronology mismatch: {tid}")
        except (KeyError, TypeError, ValueError):
            errors.append(f"invalid task/private chronology: {tid}")
        for heading in ("## Objective", "## Inputs", "## Deliverable", "## Fair consequence basis"):
            if heading not in public:
                errors.append(f"public task missing heading {heading}: {tid}")
        corpus = corpus_by_family.get(fid, {})
        for signature in corpus.get("leakage_signatures", []):
            if signature.casefold() in public.casefold():
                errors.append(f"complete source procedure leaked into public task: {tid}")
        for proposition in corpus.get("propositions", []):
            if proposition.get("statement", "").casefold() in public.casefold():
                errors.append(f"verbatim source proposition leaked into public task: {tid}/{proposition.get('id')}")
        checks = private.get("checks", [])
        if not checks:
            errors.append(f"private endpoint has no checks: {tid}")
        for check in checks:
            basis = check.get("public_basis")
            if not isinstance(basis, str) or basis not in public:
                errors.append(f"private check lacks exact public basis: {tid}/{check.get('id')}")
            if not check.get("proposition_basis") or not set(check.get("proposition_basis", [])) <= proposition_ids.get(fid, set()):
                errors.append(f"private check has invalid proposition basis: {tid}/{check.get('id')}")

    instruction = protocol.get("source_only_generation", {}).get("instruction", "")
    for token in forbidden_tokens:
        if token.casefold() in instruction.casefold():
            errors.append(f"task/private token leaked into generator instruction: {token}")
    for name in DISALLOWED_FREEZE_PATHS:
        if (HERE / name).exists():
            errors.append(f"prohibited freeze artifact exists: {name}")

    return errors, evidence


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check-paths", action="store_true")
    parser.add_argument("--skip-historical-byte-check", action="store_true")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    protocol = load_json(HERE / "protocol.json")
    manifest = load_json(HERE / "freeze-manifest.json")
    materials = load_materials(manifest)
    errors, evidence = validate(
        protocol,
        manifest,
        materials,
        check_paths=args.check_paths,
        check_historical=not args.skip_historical_byte_check,
    )
    report = {
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "gates": {gate: "pass" if not errors else "fail" for gate in sorted(REQUIRED_GATES)},
        "reference_package_results": evidence["reference_packages"],
        "mutation_error_counts": {
            family: {name: len(values) for name, values in cases.items()}
            for family, cases in evidence["mutations"].items()
        },
        "package_generation_attempts": 0,
        "model_attempts": 0,
        "provider_attempts": 0,
        "executor_attempts": 0,
        "execution_authorized": False,
        "claim_ceiling_all_false": all_false_claims(protocol.get("claim_boundaries")),
    }
    rendered = json.dumps(report, indent=2) + "\n"
    if args.report:
        args.report.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

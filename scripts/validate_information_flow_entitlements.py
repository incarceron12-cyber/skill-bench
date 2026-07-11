#!/usr/bin/env python3
"""Validate information-flow entitlements across all observed surfaces."""
import argparse
import json
from datetime import datetime
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas/information-flow-entitlement.schema.json"
REQUIRED_NONCLAIMS = {"organizational norm validity", "professional capability", "deployment safety", "leak-detector accuracy", "release readiness"}


def _time(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def semantic_errors(package, check_paths=False):
    errors = []
    if package.get("status") != "internal_synthetic_contract_calibration":
        errors.append("status must preserve internal synthetic calibration scope")
    design = package.get("design", {})
    if check_paths:
        for field in ("source_review", "source_pdf"):
            if not (ROOT / design.get(field, "")).is_file():
                errors.append(f"design.{field} must resolve to a repository file")
        for path in design.get("reused_contracts", []):
            if not (ROOT / path).is_file(): errors.append(f"reused contract does not exist: {path}")

    actors = {x.get("actor_id") for x in package.get("actors", [])}
    atoms = {x.get("atom_id"): x for x in package.get("information_atoms", [])}
    transforms = {x.get("transformation_id"): x for x in package.get("transformations", [])}
    entitlements = {}
    for e in package.get("entitlements", []):
        key = (e.get("atom_id"), e.get("actor_id"), e.get("purpose"))
        if key in entitlements: errors.append(f"duplicate entitlement tuple: {key}")
        entitlements[key] = e
        if e.get("atom_id") not in atoms or e.get("actor_id") not in actors:
            errors.append(f"{e.get('entitlement_id')} references unknown atom or actor")
        if _time(e["valid_from"]) >= _time(e["valid_until"]):
            errors.append(f"{e.get('entitlement_id')} has an invalid time interval")
        if e.get("use") == "derived_only" or e.get("disclosure") == "derived_only":
            if "raw" in e.get("allowed_representations", []):
                errors.append(f"{e.get('entitlement_id')} derived-only policy cannot allow raw representation")

    seen_surfaces = set()
    for o in package.get("observations", []):
        seen_surfaces.add(o.get("surface"))
        atom = atoms.get(o.get("atom_id"))
        e = entitlements.get((o.get("atom_id"), o.get("actor_id"), o.get("purpose")))
        prefix = o.get("observation_id")
        if not atom or not e:
            errors.append(f"{prefix} has no matching atom entitlement")
            continue
        active = _time(e["valid_from"]) <= _time(o["timestamp"]) < _time(e["valid_until"])
        policy = e.get(o.get("operation"))
        representation_allowed = (o.get("operation") == "access" and e.get("access") == "permitted") or o.get("representation") in e.get("allowed_representations", [])
        allowed = active and o.get("surface") in e.get("allowed_surfaces", []) and representation_allowed
        if policy == "prohibited": allowed = False
        if policy == "derived_only" and o.get("representation") == "raw": allowed = False
        if o.get("operation") == "retention":
            required = {"private_memory": "private_store", "shared_memory": "shared_store"}.get(o.get("surface"))
            if required is None or e.get("retention") != required: allowed = False
        if atom.get("raw_fingerprint", "").lower() in o.get("content", "").lower() and o.get("representation") != "raw":
            allowed = False
            errors.append(f"{prefix} raw fingerprint propagated under a derived label")
        if o.get("representation") != "raw":
            t = transforms.get(o.get("transformation_id"))
            if not t or t.get("input_atom_id") != o.get("atom_id") or t.get("output_representation") != o.get("representation"):
                allowed = False; errors.append(f"{prefix} lacks matching transformation lineage")
            elif not t.get("preserves_operational_consequence") or not t.get("suppresses_raw_fingerprint") or o.get("actor_id") not in t.get("authorized_recipients", []):
                allowed = False; errors.append(f"{prefix} uses an unsafe or unauthorized transformation")
        expected = "transformed" if allowed and o.get("representation") != "raw" else ("permitted" if allowed else "prohibited")
        if o.get("outcome") != expected:
            errors.append(f"{prefix} outcome must be {expected}, got {o.get('outcome')}")
    if not {"agent_message", "shared_memory"} <= seen_surfaces:
        errors.append("fixture must audit both message and shared-memory surfaces")
    if not REQUIRED_NONCLAIMS <= set(package.get("claim_limits", {}).get("unsupported", [])):
        errors.append("claim limits omit required non-claims")
    return errors


def validate_file(path, check_paths=False):
    package = json.loads(Path(path).read_text())
    schema = json.loads(SCHEMA.read_text())
    schema_errors = sorted(Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(package), key=lambda e: list(e.path))
    errors = [f"schema: {'/'.join(map(str, e.path))}: {e.message}" for e in schema_errors] + semantic_errors(package, check_paths)
    if errors: raise ValueError("\n".join(errors))
    return package


def main():
    p = argparse.ArgumentParser()
    p.add_argument("path", type=Path)
    p.add_argument("--check-paths", action="store_true")
    args = p.parse_args()
    package = validate_file(args.path, args.check_paths)
    counts = {k: sum(o["outcome"] == k for o in package["observations"]) for k in ("permitted", "transformed", "prohibited")}
    print(json.dumps({"package_id": package["package_id"], "observations": counts, "claim_scope": "exact deterministic synthetic fixture only"}, indent=2))

if __name__ == "__main__": main()

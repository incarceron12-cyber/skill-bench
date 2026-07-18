#!/usr/bin/env python3
"""Validate and replay correction semantic-fidelity versus context-realization cases."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_PROBE_KINDS = {"adaptation", "untouched_equivalent_form", "unrelated_collision"}
REQUIRED_UNSUPPORTED = {
    "empirical effect",
    "expert validity",
    "agent capability",
    "professional utility",
    "safety",
    "transport",
    "deployment readiness",
}


def _by_id(items: list[dict[str, Any]], key: str) -> dict[str, dict[str, Any]]:
    indexed: dict[str, dict[str, Any]] = {}
    for item in items:
        identifier = item.get(key)
        if isinstance(identifier, str):
            indexed[identifier] = item
    return indexed


def classify_semantic_delta(family: dict[str, Any], representation: dict[str, Any]) -> str:
    """Classify the earliest planted proposition-fidelity or authority violation."""
    canonical = _by_id(family.get("canonical_propositions", []), "proposition_id")
    candidate = _by_id(representation.get("propositions", []), "proposition_id")
    extra = set(candidate) - set(canonical)
    missing = set(canonical) - set(candidate)
    if extra:
        return "unsupported_addition"
    if missing:
        return "unsupported_deletion"
    for proposition_id, expected in canonical.items():
        observed = candidate[proposition_id]
        if not observed.get("evidence_locator"):
            return "missing_evidence_locator"
        if observed.get("authority_rank", 0) < expected.get("authority_rank", 0):
            return "authority_precedence_inversion"
        if observed.get("modality") != expected.get("modality"):
            return "modality_drift"
        if observed.get("scope") != expected.get("scope"):
            return "scope_widening"
        if observed.get("valid_time") != expected.get("valid_time"):
            return "valid_time_widening"
        for field in ("subject", "predicate", "object"):
            if observed.get(field) != expected.get(field):
                return "semantic_mutation"
    return "passed"


def replay(package: dict[str, Any]) -> dict[str, Any]:
    families: dict[str, Any] = {}
    for family in package["families"]:
        probes = _by_id(family["probes"], "probe_id")
        required = {probe_id for probe_id, probe in probes.items() if probe["kind"] == "adaptation" and probe["required"]}
        untouched = {probe_id for probe_id, probe in probes.items() if probe["kind"] == "untouched_equivalent_form"}
        collisions = {probe_id for probe_id, probe in probes.items() if probe["kind"] == "unrelated_collision"}
        cells = {}
        for representation in family["representations"]:
            realization = representation["realization"]
            retrieval = realization["probe_retrieval"]
            semantic = classify_semantic_delta(family, representation)
            converged = bool(required) and all(retrieval.get(probe_id) is True for probe_id in required)
            untouched_pass = bool(untouched) and all(retrieval.get(probe_id) is True for probe_id in untouched)
            collision_clear = all(retrieval.get(probe_id) is False for probe_id in collisions)
            promotion_gates_pass = (
                family["correction"]["status"] == "admitted"
                and semantic == "passed"
                and converged
                and untouched_pass
                and realization["correctness_observer"] == "independent_fixture_oracle"
                and realization["independently_correct"] is True
                and collision_clear
                and realization["rollback"] == "armed"
            )
            cells[representation["representation_id"]] = {
                "semantic_outcome": semantic,
                "all_required_adaptation_probes": converged,
                "untouched_equivalent_form": untouched_pass,
                "collision_clear": collision_clear,
                "generator_exposed": realization["generator_exposed"],
                "semantically_adopted": realization["semantically_adopted"],
                "independently_correct": realization["independently_correct"],
                "collateral_effect": realization["collateral_effect"],
                "rollback": realization["rollback"],
                "promotion_gates_pass": promotion_gates_pass,
            }
        families[family["family_id"]] = cells
    return {"families": families}


def semantic_errors(package: dict[str, Any], check_paths: bool = False) -> list[str]:
    errors: list[str] = []
    if package.get("status") != "internal_synthetic_contract_calibration":
        errors.append("status must preserve internal synthetic calibration scope")
    design = package.get("design", {})
    for path in design.get("source_reviews", []) + design.get("reused_contracts", []):
        if not path or (check_paths and not (ROOT / path).is_file()):
            errors.append(f"design provenance path does not exist: {path!r}")

    policy = package.get("policy", {})
    if policy.get("convergence_quantifier") != "all_required_probes":
        errors.append("convergence must use explicit all-required-probe semantics, never any-probe semantics")
    if policy.get("adaptation_probe_reuse_as_confirmation") is not False:
        errors.append("adaptation probes cannot be reused as untouched confirmation")
    if policy.get("retrieval_is_readiness") is not False:
        errors.append("retrieval cannot be treated as readiness")

    families = package.get("families", [])
    if len(families) < 2 or len({family.get("domain_shape") for family in families}) < 2:
        errors.append("at least two unlike synthetic correction families are required")
    for family in families:
        family_id = family.get("family_id", "<unknown>")
        correction = family.get("correction", {})
        for field in ("actor_role", "authority_scope", "evidence_locator", "valid_time", "scope", "authority_rank", "disposition"):
            if not correction.get(field) and correction.get(field) != 0:
                errors.append(f"{family_id}: admitted correction lacks {field}")
        if correction.get("status") != "admitted":
            errors.append(f"{family_id}: correction must be explicitly admitted")

        canonical = family.get("canonical_propositions", [])
        canonical_ids = [item.get("proposition_id") for item in canonical]
        if len(canonical_ids) != len(set(canonical_ids)):
            errors.append(f"{family_id}: duplicate canonical proposition ids")
        for proposition in canonical:
            if not proposition.get("evidence_locator"):
                errors.append(f"{family_id}: canonical proposition {proposition.get('proposition_id')} lacks evidence locator")

        probes = family.get("probes", [])
        probes_by_id = _by_id(probes, "probe_id")
        kinds = {probe.get("kind") for probe in probes}
        if kinds != REQUIRED_PROBE_KINDS:
            errors.append(f"{family_id}: adaptation, untouched-equivalent, and unrelated-collision probes must remain separate")
        required = {probe["probe_id"] for probe in probes if probe.get("kind") == "adaptation" and probe.get("required")}
        if len(required) < 2:
            errors.append(f"{family_id}: at least two required adaptation probes are needed to exercise all-vs-any convergence")
        if any(probe.get("required") for probe in probes if probe.get("kind") != "adaptation"):
            errors.append(f"{family_id}: only adaptation probes may drive convergence")

        representations = family.get("representations", [])
        representation_ids = [item.get("representation_id") for item in representations]
        if len(representation_ids) != len(set(representation_ids)):
            errors.append(f"{family_id}: duplicate representation ids")
        for representation in representations:
            owner = f"{family_id}/{representation.get('representation_id')}"
            semantic = classify_semantic_delta(family, representation)
            if semantic != representation.get("expected_semantic_outcome"):
                errors.append(f"{owner}: expected semantic outcome {representation.get('expected_semantic_outcome')!r} does not replay; got {semantic!r}")
            realization = representation.get("realization", {})
            retrieval = realization.get("probe_retrieval", {})
            if set(retrieval) != set(probes_by_id):
                errors.append(f"{owner}: retrieval results must cover every declared probe exactly once")
            converged = bool(required) and all(retrieval.get(probe_id) is True for probe_id in required)
            if realization.get("reported_converged") is not converged:
                errors.append(f"{owner}: reported convergence does not equal all required adaptation probes")
            if realization.get("generator_exposed") and not any(retrieval.values()):
                errors.append(f"{owner}: generator exposure requires retrieval")
            if realization.get("semantically_adopted") and not realization.get("generator_exposed"):
                errors.append(f"{owner}: semantic adoption requires generator exposure")
            if realization.get("independently_correct") and realization.get("correctness_observer") != "independent_fixture_oracle":
                errors.append(f"{owner}: same-loop correctness cannot promote a context object")
            if realization.get("readiness_claim"):
                errors.append(f"{owner}: retrieval-only or synthetic evidence cannot support readiness claims")
            if semantic == "passed":
                untouched_ids = [p["probe_id"] for p in probes if p["kind"] == "untouched_equivalent_form"]
                collision_ids = [p["probe_id"] for p in probes if p["kind"] == "unrelated_collision"]
                if not converged or not all(retrieval[item] for item in untouched_ids):
                    errors.append(f"{owner}: faithful representation requires adaptation plus untouched confirmation")
                if any(retrieval[item] for item in collision_ids):
                    errors.append(f"{owner}: faithful representation has collateral collision retrieval")
                if not realization.get("independently_correct") or realization.get("rollback") != "armed":
                    errors.append(f"{owner}: faithful realization requires independent correctness and armed rollback")

    variants = {representation.get("variant") for family in families for representation in family.get("representations", [])}
    required_variants = {"faithful_rewrite", "unsupported_addition", "scope_widening", "valid_time_widening", "stale_conflicting_authority", "discoverable_but_wrong"}
    if not required_variants <= variants:
        errors.append(f"fixture omits required planted variants: {sorted(required_variants - variants)}")
    unsupported = set(package.get("claim_limits", {}).get("unsupported", []))
    if not REQUIRED_UNSUPPORTED <= unsupported:
        errors.append("claim limits omit required synthetic conformance non-claims")
    execution = package.get("execution", {})
    if execution.get("model_calls") != 0 or execution.get("cost_usd") != 0:
        errors.append("this deterministic slice must use zero model calls and zero cost")
    if execution.get("stochastic_components") and execution.get("repetitions_per_cell", 0) < 2:
        errors.append("stochastic components require repeated cells")
    return errors


def validate_file(path: Path, check_paths: bool = False) -> dict[str, Any]:
    package = json.loads(path.read_text(encoding="utf-8"))
    errors = semantic_errors(package, check_paths=check_paths)
    if errors:
        raise ValueError("\n".join(f"- {error}" for error in errors))
    return package


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    parser.add_argument("--check-paths", action="store_true")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    try:
        package = validate_file(args.path, check_paths=args.check_paths)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"INVALID {args.path}\n{exc}")
        return 1
    result = {
        "package_sha256": hashlib.sha256(args.path.read_bytes()).hexdigest(),
        "replay": replay(package),
        "claim_scope": "exact deterministic synthetic contract conformance only",
    }
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"VALID {args.path}")
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

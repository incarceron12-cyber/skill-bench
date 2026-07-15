#!/usr/bin/env python3
"""Deterministic intervention-to-attribution-rung conformance replay."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PROTOCOL = HERE / "protocol.json"
INPUTS = HERE / "observer-inputs.json"
ORACLE = HERE / "oracle-private.json"
REPORT = HERE / "replay-report.json"
REPORT_SHA = HERE / "replay-report.sha256"
REQUIRED_CONDITIONS = {
    "original", "single_upstream_injection", "repaired_injection", "sham_no_op",
    "downstream_surface_only_defect", "dual_fault",
}
REQUIRED_VIEWS = {"prefix_only", "full_trace_answer_withheld", "answer_bearing"}
REQUIRED_LIMITS = {
    "natural failure prevalence", "auditor generalization", "expert validity",
    "professional validity", "agent capability", "safety", "production fitness",
    "deployment readiness",
}


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text())


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def digest(label: str) -> str:
    return hashlib.sha256(label.encode()).hexdigest()


def validate_config(protocol: dict[str, Any], inputs: dict[str, Any], oracle: dict[str, Any], *, check_paths: bool = False) -> list[str]:
    errors: list[str] = []
    shapes = protocol.get("work_shapes", [])
    if len(shapes) < 2 or len({x.get("artifact_type") for x in shapes}) < 2:
        errors.append("at least two structurally unlike artifact-heavy work shapes are required")
    if set(protocol.get("conditions", [])) != REQUIRED_CONDITIONS:
        errors.append("condition cross is incomplete")
    if len(protocol.get("equivalent_forms", [])) < 2:
        errors.append("at least two deterministic equivalent forms are required")
    if {x.get("id") for x in protocol.get("observer_views", [])} != REQUIRED_VIEWS:
        errors.append("observer view cross is incomplete")
    if set(oracle.get("condition_semantics", {})) != REQUIRED_CONDITIONS:
        errors.append("oracle condition semantics are incomplete")
    if oracle.get("claim_authority", {}).get("natural_failure_root", "").split(":", 1)[0] != "prohibited":
        errors.append("natural-failure root must remain prohibited")
    if not oracle.get("claim_authority", {}).get("earliest_sufficient_cause", "").startswith("unsupported"):
        errors.append("earliest-sufficient cause must remain unsupported")
    unsupported = set(protocol.get("claim_limits", {}).get("unsupported", []))
    if not REQUIRED_LIMITS <= unsupported:
        errors.append("required claim limits are missing")
    sham = oracle.get("condition_semantics", {}).get("sham_no_op", {})
    if sham.get("first_divergence") is not None or sham.get("outcome") != "success":
        errors.append("sham control must have no divergence and must succeed")
    dual = oracle.get("condition_semantics", {}).get("dual_fault", {})
    if set(dual.get("causes", [])) != {"upstream", "surface"}:
        errors.append("dual-fault oracle must preserve both sufficient alternatives")
    if inputs.get("case_generation", {}).get("attempt_count") != len(shapes) * len(REQUIRED_CONDITIONS) * len(protocol.get("equivalent_forms", [])):
        errors.append("predeclared attempt count does not match full cross")
    if check_paths:
        for relative in protocol.get("reused_frozen_sources", []):
            if not (ROOT / relative).is_file():
                errors.append(f"missing frozen source: {relative}")
    return errors


def attempt_record(shape: dict[str, Any], condition: str, form: int, semantics: dict[str, Any], divergence: dict[str, Any]) -> dict[str, Any]:
    stem = f"{shape['id']}:{form}"
    pre_hash = digest(stem + ":pre")
    divergent = shape["id"] == divergence["work_shape"] and condition == divergence["condition"] and form == divergence["equivalent_form"]
    observed_pre = digest(stem + ":replay-drift") if divergent else pre_hash
    loci = shape["event_loci"]
    first = semantics["first_divergence"]
    first_locator = loci[first] if first else None
    causes = [loci[x] for x in semantics["causes"]]
    disposition = "invalid_replay_diverged" if divergent else semantics["disposition"]
    propagation = []
    if "upstream" in semantics["causes"]:
        propagation.append({"from": loci["upstream"], "to": loci["propagation"], "relation": "data"})
        propagation.append({"from": loci["propagation"], "to": loci["surface"], "relation": "artifact"})
    if "surface" in semantics["causes"]:
        propagation.append({"from": loci["surface"], "to": loci["surface"], "relation": "surface_mutation"})
    return {
        "attempt_id": f"{shape['id']}--{condition}--f{form}",
        "work_shape": shape["id"], "artifact_type": shape["artifact_type"], "equivalent_form": form,
        "condition": condition, "successful_witness_id": shape["successful_witness"],
        "expected_pre_state_sha256": pre_hash, "observed_pre_state_sha256": observed_pre,
        "prefix_identity": "diverged" if divergent else "exact",
        "injected_delta": semantics["delta"],
        "first_observed_divergence": first_locator,
        "propagation_edges": propagation,
        "surfaced_check": loci["surface"] if semantics["surface_failed"] else None,
        "artifact_outcome": semantics["outcome"],
        "repair_result": "recovered" if condition == "repaired_injection" and not divergent else ("invalid" if divergent else "not_applied"),
        "unaffected_control": {"locator": shape["unaffected_control"], "outcome": "passed" if not divergent else "not_scored"},
        "alternative_sufficient_causes": causes[1:] if len(causes) > 1 else [],
        "oracle_causal_slice": causes,
        "attempt_disposition": disposition,
        "valid_for_attribution": not divergent,
    }


def dimension(outcome: str, evidence: str) -> dict[str, str]:
    return {"outcome": outcome, "evidence": evidence}


def audit(attempt: dict[str, Any], view: str) -> dict[str, Any]:
    condition = attempt["condition"]
    loci = attempt["oracle_causal_slice"]
    surface = attempt["surfaced_check"]
    valid = attempt["valid_for_attribution"]
    if not valid:
        dims = {name: dimension("invalid", "prefix replay diverged") for name in (
            "injected_delta_recovery", "first_divergence_localization", "supported_causal_slice",
            "unresolved_alternatives", "but_for_repair", "collateral_regression")}
        return {"view_id": view, "predicted_root": None, "claimed_rung": "none", "dimensions": dims}

    no_fault = condition in {"original", "sham_no_op"}
    if view == "prefix_only":
        upstream_visible = condition in {"single_upstream_injection", "repaired_injection", "dual_fault"}
        delta_outcome = "correct" if upstream_visible or no_fault else "insufficient_evidence"
        first_outcome = "correct" if upstream_visible or no_fault else "insufficient_evidence"
        predicted = loci[0] if upstream_visible and loci else None
        return {
            "view_id": view, "predicted_root": predicted,
            "claimed_rung": "first_observed_divergence" if upstream_visible else "injected_delta",
            "dimensions": {
                "injected_delta_recovery": dimension(delta_outcome, "prefix comparison through propagation event"),
                "first_divergence_localization": dimension(first_outcome, "earliest visible event comparison"),
                "supported_causal_slice": dimension("insufficient_evidence", "surface and full propagation withheld"),
                "unresolved_alternatives": dimension("insufficient_evidence", "later independent causes withheld"),
                "but_for_repair": dimension("insufficient_evidence", "paired outcomes withheld"),
                "collateral_regression": dimension("insufficient_evidence", "unaffected control withheld"),
            },
        }

    if view == "answer_bearing" and surface:
        predicted = surface
        upstream_truth = bool(loci and loci[0] != surface)
        causal_correct = loci == [surface]
        return {
            "view_id": view, "predicted_root": predicted, "claimed_rung": "propagated_surface_failure",
            "dimensions": {
                "injected_delta_recovery": dimension("incorrect" if upstream_truth else "correct", "endpoint-anchored surface attribution"),
                "first_divergence_localization": dimension("incorrect" if upstream_truth else "correct", "endpoint-anchored surface attribution"),
                "supported_causal_slice": dimension("correct" if causal_correct else "incorrect", "surface-only causal slice"),
                "unresolved_alternatives": dimension("incorrect" if len(loci) > 1 else "correct", "answer-bearing observer reports no alternative"),
                "but_for_repair": dimension("insufficient_evidence", "endpoint answer is not a paired repair"),
                "collateral_regression": dimension("insufficient_evidence", "endpoint answer omits unaffected control"),
            },
        }

    predicted = loci[0] if loci else None
    repair_applicable = condition in {"single_upstream_injection", "repaired_injection", "downstream_surface_only_defect", "dual_fault"}
    return {
        "view_id": view, "predicted_root": predicted,
        "claimed_rung": "but_for_effect_under_replay" if repair_applicable else "injected_delta",
        "dimensions": {
            "injected_delta_recovery": dimension("correct", "complete witness-relative delta comparison"),
            "first_divergence_localization": dimension("correct", "complete ordered event comparison"),
            "supported_causal_slice": dimension("correct", "all observed dependency loci retained"),
            "unresolved_alternatives": dimension("correct", "dual causes preserved when present"),
            "but_for_repair": dimension("correct" if repair_applicable else "not_applicable", "matched original/injected/repaired/sham cells"),
            "collateral_regression": dimension("correct" if condition == "repaired_injection" else "not_applicable", "declared unaffected control checked"),
        },
    }


def build_report(protocol: dict[str, Any], inputs: dict[str, Any], oracle: dict[str, Any], *, check_paths: bool = False) -> dict[str, Any]:
    errors = validate_config(protocol, inputs, oracle, check_paths=check_paths)
    attempts = []
    divergence = inputs["case_generation"]["intentional_replay_divergence"]
    for shape in protocol["work_shapes"]:
        for condition in protocol["conditions"]:
            for form in protocol["equivalent_forms"]:
                row = attempt_record(shape, condition, form, oracle["condition_semantics"][condition], divergence)
                row["audits"] = [audit(row, view["id"]) for view in protocol["observer_views"]]
                attempts.append(row)

    counts: dict[str, int] = {}
    for row in attempts:
        counts[row["attempt_disposition"]] = counts.get(row["attempt_disposition"], 0) + 1
    by_view: dict[str, dict[str, int]] = {}
    for view in REQUIRED_VIEWS:
        values = [d["outcome"] for row in attempts for audit_row in row["audits"] if audit_row["view_id"] == view for d in audit_row["dimensions"].values()]
        by_view[view] = {status: values.count(status) for status in sorted(set(values))}

    answer_anchor = sum(
        1 for row in attempts if row["valid_for_attribution"] and row["condition"] in {"single_upstream_injection", "dual_fault"}
        for audit_row in row["audits"] if audit_row["view_id"] == "answer_bearing" and audit_row["predicted_root"] == row["surfaced_check"]
    )
    full_upstream_correct = sum(
        1 for row in attempts if row["valid_for_attribution"] and row["condition"] in {"single_upstream_injection", "dual_fault"}
        for audit_row in row["audits"] if audit_row["view_id"] == "full_trace_answer_withheld" and audit_row["predicted_root"] == row["first_observed_divergence"]
    )
    expected_upstream_contrasts = len(protocol["work_shapes"]) * 2 * len(protocol["equivalent_forms"])
    if answer_anchor != expected_upstream_contrasts:
        errors.append(f"answer-anchoring calibration expected {expected_upstream_contrasts} surface collapses, observed {answer_anchor}")
    if full_upstream_correct != expected_upstream_contrasts:
        errors.append(f"full-trace calibration expected {expected_upstream_contrasts} upstream localizations, observed {full_upstream_correct}")
    if counts.get("invalid_replay_diverged") != 1:
        errors.append("exactly one replay-diverged attempt must be retained")

    frozen_hashes = {
        "policy": sha(PROTOCOL), "observer_input": sha(INPUTS), "oracle": sha(ORACLE), "replay_code": sha(Path(__file__)),
        "reused_sources": {relative: sha(ROOT / relative) for relative in protocol["reused_frozen_sources"] if (ROOT / relative).is_file()},
    }
    return {
        "package_id": protocol["package_id"], "valid": not errors, "errors": errors,
        "frozen_hashes": frozen_hashes, "attempt_count": len(attempts), "disposition_counts": counts,
        "auditor_dimension_outcomes": by_view,
        "contrast_checks": {"answer_bearing_surface_collapses_on_upstream_failures": answer_anchor, "answer_withheld_full_trace_upstream_localizations": full_upstream_correct},
        "attempts": attempts,
        "licensed_claim": protocol["claim_limits"]["supported"],
        "claim_ceiling": protocol["claim_limits"]["unsupported"],
        "rung_conclusions": {
            "injected_delta": "supported locally for declared construction deltas",
            "first_observed_divergence": "supported locally only for exact-prefix valid attempts",
            "propagated_surface_failure": "supported locally from explicit dependency edges and checks",
            "but_for_effect_under_replay": "supported locally for complete valid matched cells, not the replay-diverged cell",
            "earliest_sufficient_cause": "unsupported",
            "natural_failure_root": "prohibited",
            "repair_utility": "supported only as local synthetic recovery with the declared collateral control",
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check-paths", action="store_true")
    parser.add_argument("--write-report", action="store_true")
    args = parser.parse_args()
    report = build_report(load(PROTOCOL), load(INPUTS), load(ORACLE), check_paths=args.check_paths)
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.write_report:
        REPORT.write_text(rendered)
        REPORT_SHA.write_text(f"{sha(REPORT)}  {REPORT.name}\n")
    print(json.dumps({k: report[k] for k in ("package_id", "valid", "errors", "attempt_count", "disposition_counts", "contrast_checks")}, indent=2))
    return 0 if report["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

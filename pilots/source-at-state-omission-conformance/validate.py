#!/usr/bin/env python3
"""Validate and replay source-at-state omission/substitution conformance."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
REQUIRED_ROLES = {"terminal_support", "transition_support", "substitute_support", "stale_contradictory", "distractor", "neutral_control"}
REQUIRED_KINDS = {"baseline", "unchanged_replay", "omission", "neutral_replacement", "cue_mask", "equivalent_source_substitution", "joint_omission", "stale_contradictory_substitution"}


def canonical_sha(value: Any) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def materialize_context(scenario: dict[str, Any], intervention: dict[str, Any]) -> list[dict[str, str]]:
    records = [{"source_id": s["source_id"], "content": s["content"]} for s in scenario["sources"] if s["baseline_available"]]
    by_id = {s["source_id"]: s for s in scenario["sources"]}
    targets = set(intervention["target_source_ids"])
    kind = intervention["kind"]
    if kind in {"omission", "joint_omission"}:
        records = [r for r in records if r["source_id"] not in targets]
    elif kind in {"neutral_replacement", "equivalent_source_substitution", "stale_contradictory_substitution"}:
        replacement = by_id[intervention["replacement_source_id"]]
        records = [r for r in records if r["source_id"] not in targets]
        if replacement["source_id"] not in {r["source_id"] for r in records}:
            records.append({"source_id": replacement["source_id"], "content": replacement["content"]})
    elif kind == "cue_mask":
        cue = intervention["masked_cue"]
        records = [{**r, "content": r["content"].replace(cue, "[MASK]")} if r["source_id"] in targets else r for r in records]
    return records


def effect(base: dict[str, Any], variant: dict[str, Any]) -> dict[str, Any]:
    if variant["status"] != "observed":
        return {"status": variant["status"], "eligible": False, "vector": None}
    return {
        "status": "observed",
        "eligible": True,
        "vector": {
            "final_acceptance": int(base["final_acceptance"]) - int(variant["final_acceptance"]),
            "next_operation_valid": int(base["next_operation_valid"]) - int(variant["next_operation_valid"]),
            "safety_preserved": int(base["safety_preserved"]) - int(variant["safety_preserved"]),
            "effort_units": variant["effort_units"] - base["effort_units"],
        },
    }


def semantic_errors(data: dict[str, Any], root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    if len(data.get("scenarios", [])) < 2 or len({s.get("work_shape") for s in data.get("scenarios", [])}) < 2:
        errors.append("matrix must contain at least two unlike work shapes")
    basis = data.get("design_basis", {})
    review = root / basis.get("review_path", "")
    if not review.is_file() or hashlib.sha256(review.read_bytes()).hexdigest() != basis.get("review_sha256"):
        errors.append("review provenance path/hash mismatch")
    if data.get("effect_contract", {}).get("aggregation") != "none_noncompensatory_vector":
        errors.append("effect dimensions must remain noncompensatory")
    unsupported = set(data.get("claim_boundary", {}).get("unsupported", []))
    for required in {"agent capability", "professional validity", "portable document utility", "cross-domain generalization", "deployment readiness"}:
        if required not in unsupported:
            errors.append(f"required unsupported claim missing: {required}")

    for sc in data.get("scenarios", []):
        sid = sc.get("shape_id", "missing")
        sources = sc.get("sources", [])
        source_ids = [s.get("source_id") for s in sources]
        by_id = {s.get("source_id"): s for s in sources}
        if len(source_ids) != len(set(source_ids)):
            errors.append(f"{sid}: duplicate source identity")
        roles = {s.get("role_at_state") for s in sources}
        if not REQUIRED_ROLES <= roles or sum(s.get("role_at_state") == "substitute_support" for s in sources) < 2:
            errors.append(f"{sid}: required source-at-state roles absent")
        for src in sources:
            content = src.get("content", "")
            if hashlib.sha256(content.encode()).hexdigest() != src.get("content_sha256") or len(content.encode()) != src.get("byte_length"):
                errors.append(f"{sid}: source content hash/length mismatch for {src.get('source_id')}")
        if canonical_sha(sc.get("configured_system")) != sc.get("configured_system_sha256") or canonical_sha(sc.get("frozen_prefix")) != sc.get("frozen_prefix_sha256"):
            errors.append(f"{sid}: configuration or prefix hash mismatch")
        cells = sc.get("conditions", [])
        kinds = {c.get("intervention", {}).get("kind") for c in cells}
        if not REQUIRED_KINDS <= kinds or sum(c.get("intervention", {}).get("kind") == "unchanged_replay" for c in cells) < 2:
            errors.append(f"{sid}: intervention matrix incomplete")
        baseline_cells = [c for c in cells if c.get("intervention", {}).get("kind") == "baseline"]
        if len(baseline_cells) != 1 or baseline_cells[0].get("outcome", {}).get("status") != "observed":
            errors.append(f"{sid}: exactly one observed baseline required")
            continue
        baseline = baseline_cells[0]["outcome"]
        for cell in cells:
            iv = cell.get("intervention", {})
            targets = iv.get("target_source_ids", [])
            if any(t not in by_id for t in targets):
                errors.append(f"{sid}/{cell.get('condition_id')}: unknown intervention target")
            if "replacement_source_id" in iv and iv["replacement_source_id"] not in by_id:
                errors.append(f"{sid}/{cell.get('condition_id')}: unknown replacement source")
            if iv.get("kind") == "neutral_replacement" and iv.get("replacement_source_id") in by_id and targets:
                if by_id[iv["replacement_source_id"]]["byte_length"] != by_id[targets[0]]["byte_length"]:
                    errors.append(f"{sid}/{cell.get('condition_id')}: neutral replacement is not length preserving")
            if iv.get("kind") == "equivalent_source_substitution" and by_id.get(iv.get("replacement_source_id"), {}).get("role_at_state") != "substitute_support":
                errors.append(f"{sid}/{cell.get('condition_id')}: equivalent substitution lacks typed substitute")
            if iv.get("kind") == "equivalent_source_substitution" and by_id.get(iv.get("replacement_source_id"), {}).get("baseline_available"):
                errors.append(f"{sid}/{cell.get('condition_id')}: equivalent replacement must be a newly exposed source")
            if iv.get("kind") == "stale_contradictory_substitution" and by_id.get(iv.get("replacement_source_id"), {}).get("role_at_state") != "stale_contradictory":
                errors.append(f"{sid}/{cell.get('condition_id')}: stale substitution lacks stale contradictory source")
            if iv.get("kind") == "stale_contradictory_substitution" and by_id.get(iv.get("replacement_source_id"), {}).get("baseline_available"):
                errors.append(f"{sid}/{cell.get('condition_id')}: stale replacement must be absent from baseline")
            if iv.get("kind") == "cue_mask" and (not iv.get("masked_cue") or not targets or iv["masked_cue"] not in by_id.get(targets[0], {}).get("content", "")):
                errors.append(f"{sid}/{cell.get('condition_id')}: cue mask does not bind an observed cue")
            try:
                realized = canonical_sha(materialize_context(sc, iv))
            except (KeyError, TypeError):
                realized = "invalid"
            if realized != cell.get("realized_context_sha256"):
                errors.append(f"{sid}/{cell.get('condition_id')}: realized context hash mismatch")
            out = cell.get("outcome", {})
            if out.get("status") == "observed" and any(out.get(k) is None for k in ("final_acceptance", "next_operation_valid", "safety_preserved", "effort_units")):
                errors.append(f"{sid}/{cell.get('condition_id')}: observed outcome is incomplete")
            if out.get("status", "").startswith("invalid") and any(out.get(k) is not None for k in ("final_acceptance", "next_operation_valid", "safety_preserved", "effort_units")):
                errors.append(f"{sid}/{cell.get('condition_id')}: invalid state must not carry effect values")
        unchanged = [c["outcome"] for c in cells if c["intervention"]["kind"] == "unchanged_replay"]
        if any(u != baseline for u in unchanged):
            errors.append(f"{sid}: unchanged replay noise gate failed")
        joint = [c for c in cells if c["intervention"]["kind"] == "joint_omission"]
        if not joint or effect(baseline, joint[0]["outcome"])["vector"] == {"final_acceptance": 0, "next_operation_valid": 0, "safety_preserved": 0, "effort_units": 0}:
            errors.append(f"{sid}: joint omission must expose source-set dependence")
    return errors


def replay(data: dict[str, Any], root: Path = ROOT) -> dict[str, Any]:
    errors = semantic_errors(data, root)
    if errors:
        raise ValueError("; ".join(errors))
    rows = []
    for sc in data["scenarios"]:
        base = next(c["outcome"] for c in sc["conditions"] if c["intervention"]["kind"] == "baseline")
        for cell in sc["conditions"]:
            rows.append({"shape_id": sc["shape_id"], "condition_id": cell["condition_id"], "intervention_kind": cell["intervention"]["kind"], "realized_context_sha256": cell["realized_context_sha256"], "effect": effect(base, cell["outcome"])})
    return {
        "version": data["version"],
        "status": "passed",
        "matrix_cells": len(rows),
        "work_shapes": sorted({r["shape_id"] for r in rows}),
        "effect_aggregation": "none_noncompensatory_vector",
        "invalid_cells": sum(not r["effect"]["eligible"] for r in rows),
        "bounded_claim": data["claim_boundary"],
        "results": rows,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("fixture", type=Path)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    data = json.loads(args.fixture.read_text())
    report = replay(data, args.root)
    text = json.dumps(report, indent=2) + "\n"
    if args.report:
        args.report.write_text(text)
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

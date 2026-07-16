#!/usr/bin/env python3
"""Replay the domain-neutral workspace evidence-closure conformance slice."""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
LAYERS = (
    "record_closure",
    "predicate_closure",
    "obligation_closure",
    "source_entailment",
    "byte_lineage",
    "artifact_validity",
    "report_handoff",
)


def canonical_sha256(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _index(rows: list[dict[str, Any]], key: str, label: str) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for row in rows:
        value = row.get(key)
        if not isinstance(value, str) or not value:
            raise ValueError(f"{label}: missing {key}")
        if value in result:
            raise ValueError(f"{label}: duplicate {key} {value!r}")
        result[value] = row
    return result


def _rehash_artifact(workspace: dict[str, Any], target_id: str) -> None:
    artifacts = _index(workspace["artifacts"], "target_id", "artifacts")
    executions = _index(workspace["executions"], "target_id", "executions")
    digest = canonical_sha256(artifacts[target_id]["payload"])
    artifacts[target_id]["accepted_sha256"] = digest
    artifacts[target_id]["current_sha256"] = digest
    executions[target_id]["output_sha256"] = digest


def _rehash_report(workspace: dict[str, Any]) -> None:
    source = workspace["report_source"]
    source["sha256"] = canonical_sha256({"findings": source["findings"]})
    render = workspace["render"]
    render["source_sha256"] = source["sha256"]
    render["sha256"] = canonical_sha256(
        {"source_sha256": render["source_sha256"], "rendered_text": render["rendered_text"]}
    )


def apply_mutation(base: dict[str, Any], mutation: dict[str, Any]) -> dict[str, Any]:
    workspace = copy.deepcopy(base)
    kind = mutation["kind"]
    if kind == "none":
        return workspace
    if kind == "remove_target":
        target_id = mutation["target_id"]
        workspace["target_ids"] = [item for item in workspace["target_ids"] if item != target_id]
        for field in ("executions", "artifacts", "predicates"):
            workspace[field] = [item for item in workspace[field] if item["target_id"] != target_id]
        workspace["coverage"] = [item for item in workspace["coverage"] if item["target_id"] != target_id]
        return workspace
    if kind == "replace_payload_field":
        artifact = _index(workspace["artifacts"], "target_id", "artifacts")[mutation["target_id"]]
        artifact["payload"][mutation["field"]] = mutation["value"]
        _rehash_artifact(workspace, mutation["target_id"])
        return workspace
    if kind == "replace_execution_hash":
        execution = _index(workspace["executions"], "target_id", "executions")[mutation["target_id"]]
        execution["output_sha256"] = mutation["sha256"]
        return workspace
    if kind == "replace_source_review":
        review = _index(workspace["source_reviews"], "obligation_id", "source_reviews")[mutation["obligation_id"]]
        review["quoted_proposition"] = mutation["quoted_proposition"]
        review["review_status"] = mutation["review_status"]
        return workspace
    if kind == "clear_report_findings":
        workspace["report_source"]["findings"] = []
        workspace["render"]["rendered_text"] = "requirements.numeric_total requirements.decision_label"
        _rehash_report(workspace)
        return workspace
    if kind == "replace_render_source_hash":
        workspace["render"]["source_sha256"] = mutation["sha256"]
        workspace["render"]["sha256"] = canonical_sha256(
            {
                "source_sha256": workspace["render"]["source_sha256"],
                "rendered_text": workspace["render"]["rendered_text"],
            }
        )
        return workspace
    if kind == "replace_artifact":
        artifact = _index(workspace["artifacts"], "target_id", "artifacts")[mutation["target_id"]]
        artifact["payload"] = mutation["payload"]
        _rehash_artifact(workspace, mutation["target_id"])
        if canonical_sha256(mutation["payload"]) != mutation["sha256"]:
            raise ValueError("alternative artifact mutation carries a stale declared hash")
        return workspace
    raise ValueError(f"unknown mutation kind {kind!r}")


def _status(reasons: list[str]) -> dict[str, Any]:
    return {"outcome": "failed" if reasons else "passed", "reasons": reasons}


def evaluate(workspace: dict[str, Any], inventory_record: dict[str, Any]) -> dict[str, Any]:
    obligations = _index(inventory_record["obligations"], "obligation_id", "obligations")
    target_ids = workspace["target_ids"]
    record_reasons: list[str] = []
    if len(target_ids) != len(set(target_ids)):
        record_reasons.append("duplicate target identity")
    indexes: dict[str, dict[str, dict[str, Any]]] = {}
    for field in ("executions", "artifacts", "predicates"):
        try:
            indexes[field] = _index(workspace[field], "target_id", field)
        except (KeyError, ValueError) as exc:
            record_reasons.append(str(exc))
            indexes[field] = {}
    for target_id in target_ids:
        for field in ("executions", "artifacts", "predicates"):
            if target_id not in indexes[field]:
                record_reasons.append(f"target {target_id}: missing {field[:-1]} record")
    dangling = {
        target_id
        for field in indexes.values()
        for target_id in field
        if target_id not in set(target_ids)
    }
    if dangling:
        record_reasons.append(f"records reference undeclared targets {sorted(dangling)}")

    predicate_reasons: list[str] = []
    for predicate in workspace["predicates"]:
        artifact = indexes["artifacts"].get(predicate["target_id"])
        if artifact is None:
            predicate_reasons.append(f"{predicate['predicate_id']}: missing artifact")
            continue
        actual = artifact["payload"].get(predicate["field"])
        if predicate["operator"] != "eq":
            predicate_reasons.append(f"{predicate['predicate_id']}: unsupported operator")
        elif actual != predicate["expected"]:
            predicate_reasons.append(
                f"{predicate['predicate_id']}: executable predicate failed; actual={actual!r}, expected={predicate['expected']!r}"
            )

    obligation_reasons: list[str] = []
    if inventory_record.get("author_role") != "independent_reviewer" or not inventory_record.get("frozen_before_case_execution"):
        obligation_reasons.append("obligation denominator is not independently frozen before execution")
    if canonical_sha256(inventory_record["obligations"]) != inventory_record["sha256"]:
        obligation_reasons.append("frozen obligation inventory hash mismatch")
    coverage: dict[str, list[dict[str, Any]]] = {key: [] for key in obligations}
    for row in workspace["coverage"]:
        coverage.setdefault(row["obligation_id"], []).append(row)
    for obligation_id in obligations:
        rows = coverage.get(obligation_id, [])
        if len(rows) != 1:
            obligation_reasons.append(f"{obligation_id}: requires exactly one coverage disposition")
        elif rows[0]["status"] == "covered" and rows[0]["target_id"] not in target_ids:
            obligation_reasons.append(f"{obligation_id}: covered by absent target")
        elif rows[0]["status"] not in {"covered", "reviewed_exclusion"}:
            obligation_reasons.append(f"{obligation_id}: invalid coverage disposition")

    source_reasons: list[str] = []
    try:
        source_reviews = _index(workspace["source_reviews"], "obligation_id", "source_reviews")
    except ValueError as exc:
        source_reasons.append(str(exc))
        source_reviews = {}
    for obligation_id, obligation in obligations.items():
        review = source_reviews.get(obligation_id)
        if review is None:
            source_reasons.append(f"{obligation_id}: missing source review")
            continue
        expected = (
            obligation["source_id"],
            obligation["locator"],
            obligation["source_proposition"],
            "entailed",
        )
        actual = (
            review.get("source_id"),
            review.get("locator"),
            review.get("quoted_proposition"),
            review.get("review_status"),
        )
        if actual != expected:
            source_reasons.append(f"{obligation_id}: locator/proposition entailment review mismatch")

    lineage_reasons: list[str] = []
    artifact_reasons: list[str] = []
    for target_id in target_ids:
        artifact = indexes["artifacts"].get(target_id)
        execution = indexes["executions"].get(target_id)
        if not artifact or not execution:
            continue
        current = canonical_sha256(artifact["payload"])
        bindings = {
            "execution": execution["output_sha256"],
            "accepted": artifact["accepted_sha256"],
            "current": artifact["current_sha256"],
            "computed": current,
        }
        if len(set(bindings.values())) != 1:
            lineage_reasons.append(f"{target_id}: execution→accepted→current byte binding mismatch")
        if execution["status"] != "succeeded":
            lineage_reasons.append(f"{target_id}: accepted artifact lacks a successful execution")
        missing_keys = set(artifact["required_keys"]) - set(artifact["payload"])
        if missing_keys:
            artifact_reasons.append(f"{target_id}: native artifact missing keys {sorted(missing_keys)}")

    report_reasons: list[str] = []
    source = workspace["report_source"]
    if canonical_sha256({"findings": source["findings"]}) != source["sha256"]:
        report_reasons.append("report source hash mismatch")
    try:
        findings = _index(source["findings"], "obligation_id", "report findings")
    except ValueError as exc:
        report_reasons.append(str(exc))
        findings = {}
    for obligation_id in obligations:
        finding = findings.get(obligation_id)
        if not finding or not finding.get("finding", "").strip() or not finding.get("caveat", "").strip():
            report_reasons.append(f"{obligation_id}: report lacks a substantive finding and caveat")
    render = workspace["render"]
    if render["source_sha256"] != source["sha256"]:
        report_reasons.append("render is stale relative to current report source")
    render_payload = {"source_sha256": render["source_sha256"], "rendered_text": render["rendered_text"]}
    if canonical_sha256(render_payload) != render["sha256"]:
        report_reasons.append("rendered artifact hash mismatch")

    layers = {
        "record_closure": _status(record_reasons),
        "predicate_closure": _status(predicate_reasons),
        "obligation_closure": _status(obligation_reasons),
        "source_entailment": _status(source_reasons),
        "byte_lineage": _status(lineage_reasons),
        "artifact_validity": _status(artifact_reasons),
        "report_handoff": _status(report_reasons),
    }
    overall = "passed" if all(item["outcome"] == "passed" for item in layers.values()) else "failed"
    return {"overall": overall, "layers": layers}


def validate_fixture(fixture: dict[str, Any]) -> None:
    required = {
        "fixture_id", "version", "scope", "provenance", "frozen_obligation_inventory",
        "base_workspace", "cases", "claim_boundary",
    }
    if set(fixture) != required:
        raise ValueError("fixture top-level field mismatch")
    if not fixture["cases"]:
        raise ValueError("fixture requires cases")
    if any(value is not False for value in fixture["claim_boundary"].values()):
        raise ValueError("internal conformance fixture cannot license scientific/professional/effect/readiness claims")
    for source in fixture["provenance"]:
        path = ROOT / source["path"]
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != source["sha256"]:
            raise ValueError(f"provenance path/hash mismatch: {source['path']}")
        if not source["locators"]:
            raise ValueError(f"provenance lacks locators: {source['path']}")


def build_report(fixture: dict[str, Any]) -> dict[str, Any]:
    validate_fixture(fixture)
    results = []
    exact_matches = 0
    detected_failures = 0
    for case in fixture["cases"]:
        workspace = apply_mutation(fixture["base_workspace"], case["mutation"])
        observed = evaluate(workspace, fixture["frozen_obligation_inventory"])
        observed_failing = [layer for layer in LAYERS if observed["layers"][layer]["outcome"] == "failed"]
        exact = observed["overall"] == case["expected_overall"] and observed_failing == case["expected_failing_layers"]
        exact_matches += int(exact)
        detected_failures += int(case["expected_overall"] == "failed" and exact)
        results.append(
            {
                "case_id": case["case_id"],
                "expected_overall": case["expected_overall"],
                "observed_overall": observed["overall"],
                "expected_failing_layers": case["expected_failing_layers"],
                "observed_failing_layers": observed_failing,
                "exact_match": exact,
                "layers": observed["layers"],
            }
        )
    report = {
        "fixture_id": fixture["fixture_id"],
        "fixture_version": fixture["version"],
        "inventory_id": fixture["frozen_obligation_inventory"]["inventory_id"],
        "inventory_sha256": fixture["frozen_obligation_inventory"]["sha256"],
        "summary": {
            "total_cases": len(results),
            "exact_matches": exact_matches,
            "planted_failures_detected_at_expected_layers": detected_failures,
            "all_exact": exact_matches == len(results),
        },
        "results": results,
        "claim_boundary": fixture["claim_boundary"],
    }
    if not report["summary"]["all_exact"]:
        mismatches = [row["case_id"] for row in results if not row["exact_match"]]
        raise ValueError(f"conformance mismatch: {mismatches}")
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fixture", nargs="?", type=Path, default=HERE / "fixture.json")
    parser.add_argument("--write-report", type=Path)
    args = parser.parse_args()
    fixture = json.loads(args.fixture.read_text(encoding="utf-8"))
    report = build_report(fixture)
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.write_report:
        args.write_report.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Replay the internal multilingual workflow-edge conformance matrix."""
from __future__ import annotations
import argparse, json, re
from pathlib import Path

REQUIRED_FORMS = {"native-monolingual", "instruction-swapped", "source-swapped", "output-swapped", "full-multilingual"}
SEMANTIC_ORDER = ("entity", "number", "date", "unit", "negation", "modality", "scope")
HASH = re.compile(r"^[0-9a-f]{64}$")


def _classify(case, facts, forms):
    form = forms[case["form_id"]]
    supported = set(case.get("observer_supported_languages", [case["observer_language"]]))
    if form["output_language"] not in supported:
        return "insufficient_evidence", "grader_language_bias"
    observed = case["observed"]
    for key in SEMANTIC_ORDER:
        if observed.get(key) != facts["invariants"][key]:
            return "failed", "semantic_transfer"
    if not observed.get("provenance") or observed["provenance"] != facts["invariants"]["provenance"]:
        return "failed", "provenance_loss"
    if observed.get("authority") != facts["invariants"]["authority"]:
        return "failed", "unsupported_authority"
    allowed = facts["allowed_localization_transforms"][form["output_locale"]]
    if any(observed.get(key) != value for key, value in allowed.items()):
        return "failed", "locale_format"
    return "passed", "none"


def replay(data):
    errors = []
    forms_list = data["matched_forms"]
    forms = {row["id"]: row for row in forms_list}
    if len(forms) != len(forms_list) or set(forms) != REQUIRED_FORMS:
        errors.append("matched forms must contain each required condition exactly once")
    for component in ("font", "renderer", "locale_tool"):
        if not HASH.fullmatch(data["environment"][component]["sha256"]):
            errors.append(f"environment {component} is not hash-pinned")
    if data["environment"].get("unicode_normalization") not in {"NFC", "NFKC"}:
        errors.append("Unicode normalization is not pinned")
    for locale in {row["output_locale"] for row in forms_list}:
        if locale not in data["fact_pack"]["allowed_localization_transforms"]:
            errors.append(f"missing allowed localization transform for {locale}")
    for gate in ("bilingual_equivalence_review", "domain_authority_review"):
        value = data["review_gates"][gate]
        if not value["required"] or value["status"] not in {"unmet", "passed", "failed"}:
            errors.append(f"invalid review gate {gate}")
        if value["status"] == "passed" and not value.get("reviewer"):
            errors.append(f"passed review gate {gate} lacks a real reviewer record")
    required_limits = {"multilingual capability", "cross-language equivalence", "professional validity", "grader fairness", "deployment readiness"}
    if not required_limits <= set(data["claim_limits"]["unsupported"]):
        errors.append("unsupported claim boundary was weakened")

    results = []
    seen = set()
    for case in data["cases"]:
        if case["id"] in seen:
            errors.append(f"duplicate case {case['id']}")
        seen.add(case["id"])
        if case["form_id"] not in forms:
            errors.append(f"case {case['id']}: unknown form")
            continue
        outcome, failure = _classify(case, data["fact_pack"], forms)
        observed = {"outcome": outcome, "failure": failure}
        if observed != case["expected"]:
            errors.append(f"case {case['id']}: expected {case['expected']} but replayed {observed}")
        results.append({"case_id": case["id"], "form_id": case["form_id"], **observed})
    expected_failures = {"none", "semantic_transfer", "locale_format", "provenance_loss", "unsupported_authority", "grader_language_bias"}
    if {row["failure"] for row in results} != expected_failures:
        errors.append("planted case coverage is incomplete")
    return {
        "valid": not errors,
        "instrument_id": data["instrument"]["id"],
        "cases_replayed": len(results),
        "matched_forms": sorted(forms),
        "review_gates": data["review_gates"],
        "claim_status": "internal_calibration_only",
        "results": results,
        "errors": errors,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("fixture", type=Path)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    report = replay(json.loads(args.fixture.read_text(encoding="utf-8")))
    text = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    if args.report:
        args.report.write_text(text, encoding="utf-8")
    print(text, end="")
    raise SystemExit(0 if report["valid"] else 1)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Post-hoc audit of frozen v4 endpoint admissibility; never rescoring evidence."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
CLAIMS = {"agent_capability": False, "expert_provenance": False, "production_fitness": False,
          "professional_validity": False, "readiness": False, "transfer": False, "utility": False}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    execution = load(HERE / "execution-report.json")
    rows = []
    for report_path in sorted((HERE / "execution").glob("*/trial-report.json")):
        report = load(report_path)
        result_path = report_path.parent / "outputs/result.json"
        result = load(result_path) if result_path.is_file() else {}
        expected = load(HERE / "tasks" / report["task_id"] / "private.json")["expected_endpoint"]
        if report["family_id"] == "family-zeta":
            core_fields = ("valid", "final_state", "committed_transactions", "rolled_back_transactions")
            core_match = all(result.get(field) == expected.get(field) for field in core_fields)
        else:
            actual_decisions = result.get("decisions", [{}])
            expected_decisions = expected.get("decisions", [{}])
            core_fields = ("disposition",)
            core_match = bool(actual_decisions and expected_decisions and
                              actual_decisions[0].get("disposition") == expected_decisions[0].get("disposition"))
        rows.append({"schedule_index": report["schedule_index"], "family_id": report["family_id"],
                     "task_id": report["task_id"], "condition_id": report["condition_id"],
                     "frozen_endpoint_pass": report["endpoint_pass"],
                     "diagnostic_core_fields": list(core_fields), "diagnostic_core_match": core_match})

    families = ("family-epsilon", "family-zeta")
    conditions = sorted({row["condition_id"] for row in rows})
    diagnostic_rates = {family: {condition: sum(row["diagnostic_core_match"] for row in rows
                                                    if row["family_id"] == family and row["condition_id"] == condition) / 2
                                 for condition in conditions} for family in families}
    findings = [
        {"finding_id": "k4n7-private-endpoint-contradiction", "severity": "fatal_for_k4n7_scoring",
         "evidence": {"public_review_hour": 100, "blue_controlling_hour": 80, "computed_age_hours": 20,
                      "frozen_rule_max_age_hours": 24, "private_expected_disposition": "quarantine",
                      "private_reason": "blue controlling observation is older than 24 hours"},
         "conclusion": "The private endpoint contradicts the frozen source rule: 100 - 80 = 20, which is not older than 24 hours."},
        {"finding_id": "journal-id-hidden-literal", "severity": "fatal_for_exact_json_scoring",
         "evidence": {"public_tasks": ["t6v1", "w3d8"], "public_task_supplies_journal_id_value": False,
                      "private_literals": {"t6v1": "J6", "w3d8": "J9"}},
         "conclusion": "The public tasks require a journal_id field but supply no value; exact private literals are hidden obligations."},
        {"finding_id": "reason-wording-exactness", "severity": "fatal_for_exact_json_scoring",
         "evidence": {"checker_kind": "whole-object exact equality", "endpoint_mismatch_rows": 32,
                      "semantically_free_reason_field": True},
         "conclusion": "Exact equality requires one undisclosed reason string and rejects substantively equivalent explanations."},
        {"finding_id": "controlling-seals-type-undisclosed", "severity": "fair_basis_threat",
         "evidence": {"public_declares_field": True, "public_declares_type": False,
                      "private_requires": "object mapping seal to observation", "observed_alternative": "array of seal names"},
         "conclusion": "The private object representation is not disclosed by the public artifact convention."},
    ]
    report = {
        "schema_version": "0.1.0", "study_id": "pretask-procedure-transfer-v4-posthoc-endpoint-audit",
        "audit_kind": "posthoc_instrument_defect_diagnosis_not_rescoring",
        "frozen_execution_report": {"path": "pilots/pretask-procedure-transfer-v4/execution-report.json",
                                    "sha256": sha(HERE / "execution-report.json")},
        "frozen_checker_result": {"endpoint_pass": execution["denominators"]["endpoint_pass"],
                                  "checker_scored": execution["denominators"]["checker_scored"],
                                  "unchanged": True},
        "findings": findings, "diagnostic_rows": rows, "diagnostic_core_match_rates": diagnostic_rates,
        "diagnostic_core_matches": sum(row["diagnostic_core_match"] for row in rows),
        "diagnostic_core_denominator": len(rows),
        "admissibility_conclusion": "The all-zero frozen exact-endpoint score is not an interpretable procedure-transfer outcome because the endpoint instrument contains a factual contradiction and undisclosed exact-value, type, and wording obligations.",
        "use_limit": "Core-field matches are an explicitly post-hoc failure-localization diagnostic. They were not prospectively frozen, are not replacement scores, and must not be used for treatment estimates.",
        "required_next_instrument": "Create a new version; do not edit or rescore v4. Prospectively freeze typed structural checks, reason invariances, disclosed identifiers, recomputed endpoints, and checker mutation tests before any new calls.",
        "claim_ceiling": CLAIMS,
    }
    output = HERE / "posthoc-endpoint-audit.json"
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"output": output.relative_to(ROOT).as_posix(), "findings": len(findings),
                      "diagnostic_core_matches": report["diagnostic_core_matches"],
                      "diagnostic_core_denominator": report["diagnostic_core_denominator"]}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

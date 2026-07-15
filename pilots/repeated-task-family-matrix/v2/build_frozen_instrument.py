#!/usr/bin/env python3
"""Prospectively author v2 without consulting or importing v1 observed outputs."""
from __future__ import annotations

import hashlib
import json
import random
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def dump(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


FORMS = {
    "resource_governance/capacity": {
        "construct": "apply a disclosed resource threshold to a controlling measurement",
        "source": {"rule": "At least 50 reserved slots are required before activation.", "records": [
            {"id": "RC-42", "rank": "attested_measurement", "scope": "planned activation", "statement": "42 slots are reserved", "currency": "controlling"},
            {"id": "RC-55", "rank": "planning_note", "scope": "target only", "statement": "55 slots were requested", "currency": "advisory"},
            {"id": "RC-OLD", "rank": "attested_measurement", "scope": "retired topology", "statement": "51 slots were formerly reserved", "currency": "outdated"},
        ]},
        "decisions": ["defer", "postpone", "not_ready"],
        "actions": ["add_capacity_then_reassess", "increase_resources_and_review", "close_gap_before_review"],
        "wrong_decisions": ["activate", "activate_limited"],
        "wrong_actions": ["waive_capacity_gap", "monitor_without_change"],
        "evidence_ids": ["RC-42"],
        "severity": "critical",
        "derivation": "Builder-authored threshold case derived only from the criterion/environment boundary in papers/agent-benchmarks/2026-07-15-performance-optimization-benchmark-reliability.md; no v1 output is an authoring or admission source.",
    },
    "resource_governance/variance": {
        "construct": "avoid escalation when the controlling forecast remains inside a disclosed cap",
        "source": {"rule": "Escalation is required only when the controlling forecast exceeds 120 units.", "records": [
            {"id": "RV-117", "rank": "approved_forecast", "scope": "current cycle", "statement": "forecast is 117 units", "currency": "controlling"},
            {"id": "RV-126", "rank": "draft_scenario", "scope": "unapproved stress case", "statement": "scenario reaches 126 units", "currency": "advisory"},
            {"id": "RV-OLD", "rank": "approved_forecast", "scope": "prior cycle", "statement": "forecast was 124 units", "currency": "outdated"},
        ]},
        "decisions": ["within_limit", "acceptable", "no_escalation"],
        "actions": ["continue_with_weekly_check", "maintain_plan_and_recheck", "proceed_with_monitoring"],
        "wrong_decisions": ["over_limit", "mandatory_escalation"],
        "wrong_actions": ["halt_current_plan", "request_emergency_waiver"],
        "evidence_ids": ["RV-117"],
        "severity": "minor",
        "derivation": "Builder-authored non-intervention threshold case derived only from the criterion-margin discussion in papers/agent-benchmarks/2026-07-15-performance-optimization-benchmark-reliability.md; no v1 output is an authoring or admission source.",
    },
    "record_integrity/duplicate": {
        "construct": "select a bounded correction from a controlling reconciliation record",
        "source": {"rule": "An unreversed duplicate requires correction and reconciliation.", "records": [
            {"id": "RD-OPEN", "rank": "signed_reconciliation", "scope": "ledger 8", "statement": "a duplicate remains posted and unreversed", "currency": "controlling"},
            {"id": "RD-MSG", "rank": "operator_message", "scope": "informal", "statement": "the duplicate probably disappeared", "currency": "advisory"},
            {"id": "RD-OLD", "rank": "signed_reconciliation", "scope": "earlier snapshot", "statement": "no duplicate was visible", "currency": "outdated"},
        ]},
        "decisions": ["correction_required", "repair_needed", "unresolved_duplicate"],
        "actions": ["reverse_duplicate_and_reconcile", "remove_extra_entry_then_balance", "correct_duplicate_and_verify_total"],
        "wrong_decisions": ["already_resolved", "no_discrepancy"],
        "wrong_actions": ["archive_without_change", "delete_entire_ledger"],
        "evidence_ids": ["RD-OPEN"],
        "severity": "major",
        "derivation": "Builder-authored projection-consistency case derived only from papers/agent-benchmarks/2026-07-10-anchor-artifact-drift-generation.md; no v1 output is an authoring or admission source.",
    },
    "record_integrity/closure": {
        "construct": "recognize a completed correction while preserving audit evidence",
        "source": {"rule": "A signed zero-balance reconciliation closes the discrepancy; retain its audit trail.", "records": [
            {"id": "RZ-ZERO", "rank": "signed_reconciliation", "scope": "ledger 3", "statement": "the correction posted and the discrepancy balance is zero", "currency": "controlling"},
            {"id": "RZ-TICKET", "rank": "intake_ticket", "scope": "initial report", "statement": "a discrepancy was reported", "currency": "outdated"},
            {"id": "RZ-CHAT", "rank": "operator_message", "scope": "informal", "statement": "erase all history", "currency": "advisory"},
        ]},
        "decisions": ["closed", "resolved", "no_open_discrepancy"],
        "actions": ["archive_with_audit_trail", "retain_evidence_and_close", "close_case_preserving_records"],
        "wrong_decisions": ["still_open", "correction_required"],
        "wrong_actions": ["repeat_correction", "erase_audit_history"],
        "evidence_ids": ["RZ-ZERO"],
        "severity": "minor",
        "derivation": "Builder-authored state/projection case derived only from papers/agent-benchmarks/2026-07-10-anchor-artifact-drift-generation.md; no v1 output is an authoring or admission source.",
    },
}

TASK_TEMPLATE = """# Internal synthetic controlled-vocabulary decision task

Read `source.json` and create `outputs/report.json` with exactly four keys: `decision`, `action`, `evidence_ids`, and `rationale`.

Use the record marked `controlling` when it is applicable to the stated rule. Exclude `outdated` and `advisory` records. `evidence_ids` must contain exactly the controlling record ID. Explain the exclusion using at least one of these disclosed concepts: `lower-rank`, `outdated`, `advisory`, `scope`, or `controlling`.

For this form, choose `decision` from: {decisions}.
Choose `action` from: {actions}.
Every listed value in each field is an accepted equivalent. Values not listed are invalid. Do not access external sources.
"""


def main() -> None:
    if (HERE / "protocol.json").exists():
        raise SystemExit("protocol already exists; frozen instrument will not be overwritten")
    for key, spec in FORMS.items():
        form = HERE / "forms" / key
        task = TASK_TEMPLATE.format(decisions=", ".join(f"`{x}`" for x in spec["decisions"]), actions=", ".join(f"`{x}`" for x in spec["actions"]))
        form.mkdir(parents=True, exist_ok=True)
        (form / "public-task.md").write_text(task, encoding="utf-8")
        dump(form / "source.json", spec["source"])
        dump(form / "private-expected.json", {
            "accepted_decisions": spec["decisions"], "accepted_actions": spec["actions"],
            "near_neighbor_wrong_decisions": spec["wrong_decisions"], "near_neighbor_wrong_actions": spec["wrong_actions"],
            "evidence_ids": spec["evidence_ids"], "severity": spec["severity"],
        })
        dump(form / "task-health.json", {
            "operational_role": "internal_calibration_only", "origin": "builder_authored_hypothesis",
            "construct": spec["construct"], "derivation": spec["derivation"],
            "authoring_boundary": "Source facts and labels were composed prospectively for v2 from the cited review; v1 observations are prohibited as case-generation, calibration, or admission evidence.",
            "gates": {"public_basis": True, "all_accepted_labels_disclosed": True, "alternative_realization_calibration_required": True, "expert_validity": False, "release_eligible": False},
        })

    components = []
    for path in sorted((HERE / "forms").rglob("*")):
        if path.is_file():
            components.append({"path": path.relative_to(HERE).as_posix(), "sha256": sha(path)})
    components.append({"path": "build_frozen_instrument.py", "sha256": sha(HERE / "build_frozen_instrument.py")})
    components.append({"path": "grade.py", "sha256": sha(HERE / "grade.py")})
    components.append({"path": "README.md", "sha256": sha(HERE / "README.md")})
    components.append({"path": "run_matrix.py", "sha256": sha(HERE / "run_matrix.py")})

    seed = "repeated-task-family-matrix-v2-20260715"
    rows = []
    for key in FORMS:
        family, form = key.split("/")
        for repeat in (1, 2):
            raw = f"{seed}:{family}:{form}:{repeat}"
            rows.append({"attempt_id": "m2-" + hashlib.sha256(raw.encode()).hexdigest()[:10], "family": family, "form": form, "repeat": repeat})
    random.Random(seed).shuffle(rows)
    for index, row in enumerate(rows, 1):
        row["execution_order"] = index

    v1_tree = subprocess.run(["git", "rev-parse", "HEAD:pilots/repeated-task-family-matrix/v1"], cwd=ROOT, check=True, capture_output=True, text=True).stdout.strip()
    protocol = {
        "schema_version": "0.2.0", "protocol_id": "repeated-task-family-matrix-v2", "frozen_at": "2026-07-15T11:15:00Z",
        "purpose": "Prospectively observe exact-configured-system repeat stability with a fair disclosed scoring basis across four new internal synthetic forms in two unlike families.",
        "charter_decision_filter": {"objectives": ["B: expertise-to-evaluation methodology", "C: executable infrastructure"], "artifact": "Frozen fair-basis four-form/eight-attempt matrix", "uncertainty": "Whether disclosed controlled labels permit replayable within-form reliability and between-family descriptive denominators without open-text equivalence ambiguity.", "mode": "building and validation", "duplication": "New v2 forms and source facts do not admit or calibrate from v1 outcomes; two unlike families test reusable machinery.", "scope_boundary": "Methodological synthetic probes, not a commitment to resource or record-integrity work.", "useful_completion": "All gates pass and all eight declared attempts are retained once, or an exact fail-closed blocker is retained."},
        "design_choice": {"repair": "publicly_disclosed_controlled_vocabulary", "tradeoff": "This maximizes fair deterministic grading and reproducibility but narrows the construct from open-ended professional expression to mapping evidence into supplied decision/action classes. Rationale and evidence checks remain separate and do not require one exact prose string.", "accepted_realizations_per_field": 3, "near_neighbor_wrong_realizations_per_field": 2},
        "configured_system": {"model": "gpt-5.6-sol", "provider": "openai-codex", "invocation": "oneshot", "safe_mode": True, "toolsets": ["file"], "max_turns": 40},
        "v1_preservation": {"git_tree_at_freeze": v1_tree, "policy": "All v1 bytes must remain unchanged; v1 observations, phrases, grades, and outcomes are excluded from v2 authoring, calibration, and admission evidence."},
        "forms": {key: {"family": key.split("/")[0], "form": key.split("/")[1], "construct": spec["construct"], "derivation": spec["derivation"], "public_inputs": [f"forms/{key}/public-task.md", f"forms/{key}/source.json"], "authoritative_output": f"forms/{key}/private-expected.json", "task_health": f"forms/{key}/task-health.json", "required_output": "report.json", "criterion_severity": {"artifact_valid": "critical", "decision": "critical", "action": spec["severity"], "evidence": "major", "conflict_rationale": "minor"}} for key, spec in FORMS.items()},
        "schedule": {"seed": seed, "algorithm": "Python random.Random(seed).shuffle over two declared repeats per form", "rows": rows, "launcher_invocations_per_attempt": 1, "retries": "none", "replacement": "none", "outcome_based_admission": "forbidden"},
        "service_failure_policy": "Retain every declared ID. Continue after service failure unless cost or safety fails; never retry, replace, tune, or admit based on outcome.",
        "pre_call_gates": ["pushed_frozen_commit", "v1_byte_preservation", "component_hashes", "origin_main_cleanliness", "isolation", "private_input_leakage", "grader_alternative_realization_calibration", "grader_near_neighbor_mutation", "service_availability", "provider_included_zero_cost"],
        "reporting": {"denominators": ["intended attempts", "service-valid attempts", "environment-valid attempts", "grader-valid attempts", "substantively graded attempts"], "clustering": "Attempts nest within forms and forms within two purposively authored families; attempt-level Wilson intervals are descriptive only, with form-level ranges shown separately.", "confidence_channel": "Record only genuinely provider-emitted confidence/logprobs; otherwise insufficient_evidence."},
        "claim_boundaries": {key: False for key in ["skill_effect", "professional_validity", "expert_validity", "general_capability", "safety", "production_fitness", "readiness", "confidence_policy", "cross_domain_transport"]},
        "frozen_components": components,
    }
    dump(HERE / "protocol.json", protocol)
    print(json.dumps({"forms": 4, "attempts": 8, "components": len(components), "v1_tree": v1_tree, "protocol_sha256": sha(HERE / "protocol.json")}, indent=2))


if __name__ == "__main__":
    main()

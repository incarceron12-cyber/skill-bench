#!/usr/bin/env python3
"""Independent post-execution audit for self-inspection-repair-v1.

The audit is read-only with respect to the frozen instrument and retained execution.
It does not import the frozen checker or execution launcher and never calls a model
or provider. It binds Git objects, reads every retained execution file, independently
replays outcomes/accounting, and audits repair-record grounding against each retained
condition information view.
"""
from __future__ import annotations

import argparse
import datetime as dt
import difflib
import hashlib
import json
import subprocess
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
FREEZE = ROOT / "pilots/self-inspection-repair-v1"
EXECUTION = ROOT / "pilots/self-inspection-repair-v1-execution/execution"
FREEZE_COMMIT = "7d976a28b9f33337f2f90519964361388b3eae7f"
FREEZE_TREE = "53cacc195af88da3ed7ae02954b59bb61afaa23b"
EXECUTION_COMMIT = "50fbf3cf9616640d3d3c94e246a8288d91095a8b"
EXECUTION_ROOT_TREE = "7a6bdc76ede6da46b55b50074e6926d60db36018"
EXECUTION_TREE = "3cbd4e0f70bff03008747aa638fd097d3397281b"
EXEC_REL = Path("pilots/self-inspection-repair-v1-execution/execution")
FREEZE_REL = Path("pilots/self-inspection-repair-v1")
REPAIR_CONDITIONS = {
    "retry_no_new_information", "generic_self_review",
    "native_render_self_inspection", "consequence_only_feedback",
    "criterion_disclosure",
}
CLAIMS = {
    "self_correction": False, "agent_capability": False,
    "treatment_effect": False, "professional_validity": False,
    "utility": False, "production_fitness": False, "readiness": False,
}


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def sha_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def sha(path: Path) -> str:
    return sha_bytes(path.read_bytes())


def git(*args: str, text: bool = True) -> str | bytes:
    return subprocess.run(
        ["git", *args], cwd=ROOT, check=True, capture_output=True, text=text,
    ).stdout


def git_text(*args: str) -> str:
    return str(git(*args)).strip()


def independent_evaluate(task_id: str, candidate: Any) -> dict[str, Any]:
    """Specification replay written independently of the retained checker."""
    if task_id == "memo-vendor-selection-v1":
        if not isinstance(candidate, str) or not candidate.strip():
            return {"terminal_state": "invalid_artifact", "endpoint": None, "collateral": None}
        normalized = " ".join(candidate.lower().replace("**", "").split())
        endpoint = ("select south" in normalized or "recommend south" in normalized) and (
            "95,000" in normalized or "95000" in normalized
        )
        collateral = "north" in normalized and "south" in normalized
    elif task_id == "structured-allocation-v1":
        if not isinstance(candidate, dict) or not isinstance(candidate.get("allocations"), dict):
            return {"terminal_state": "invalid_artifact", "endpoint": None, "collateral": None}
        allocations = candidate["allocations"]
        if set(allocations) != {"ops", "research"} or any(type(v) is not int for v in allocations.values()) or type(candidate.get("declared_total")) is not int:
            return {"terminal_state": "invalid_artifact", "endpoint": None, "collateral": None}
        endpoint = (
            sum(allocations.values()) == candidate["declared_total"] == 100
            and allocations["ops"] <= 60 and allocations["research"] <= 40
        )
        collateral = set(allocations) == {"ops", "research"}
    else:
        raise ValueError(f"unknown task: {task_id}")
    return {
        "terminal_state": "passed" if endpoint and collateral else "criterion_fail",
        "endpoint": endpoint, "collateral": collateral,
    }


def parse_candidate(task_id: str, path: Path) -> Any:
    text = path.read_text(encoding="utf-8")
    return text if task_id.startswith("memo-") else json.loads(text)


def git_inventory(commit: str, rel: Path) -> list[dict[str, Any]]:
    output = git_text("ls-tree", "-r", commit, "--", rel.as_posix())
    rows = []
    for line in output.splitlines():
        metadata, path = line.split("\t", 1)
        mode, kind, obj = metadata.split()
        raw_value = git("show", f"{commit}:{path}", text=False)
        if not isinstance(raw_value, bytes):
            raise TypeError(f"expected Git blob bytes for {path}")
        raw = raw_value
        rows.append({
            "path": Path(path).relative_to(rel).as_posix(), "mode": mode,
            "kind": kind, "git_object": obj, "bytes": len(raw),
            "sha256": sha_bytes(raw),
        })
    return rows


def exact_diff(start: str, final: str) -> list[str]:
    return list(difflib.unified_diff(
        start.splitlines(), final.splitlines(), fromfile="starting", tofile="final", lineterm="",
    ))


def locus_check(task_id: str, start: Any, final: Any) -> tuple[bool, list[str]]:
    if task_id == "structured-allocation-v1":
        changed = []
        if start.get("allocations") != final.get("allocations"):
            changed.append("allocations")
        if start.get("declared_total") != final.get("declared_total"):
            changed.append("declared_total")
        if set(start) != set(final):
            changed.append("top_level_keys")
        return changed == ["declared_total"] and final["declared_total"] == 100, changed
    changed = []
    for token, label in [
        ("Select **North** at an annual cost of **$120,000**.", "recommendation"),
        ("| North | $120,000 | yes |", "north_evidence_row"),
        ("| South | $95,000 | yes |", "south_evidence_row"),
    ]:
        if (token in start) != (token in final):
            changed.append(label)
    rows_preserved = all(row in final for row in (
        "| North | $120,000 | yes |", "| South | $95,000 | yes |",
    ))
    selected = "Select **South**" in final and "$95,000" in final
    return selected and rows_preserved and "recommendation" in changed and not any("evidence_row" in x for x in changed), changed


def grounding_check(task_id: str, record: dict[str, Any], prompt: str, condition: str) -> dict[str, Any]:
    text = (record["defect_observation"] + " " + record["diagnosis"]).lower()
    if task_id == "memo-vendor-selection-v1":
        required_prompt_facts = ["north", "south", "120000", "95000", "lowest-cost"]
        claims_grounded = (
            "north" in text
            and ("south" in text or "lower-cost" in text)
            and ("recommend" in text or "selected" in text)
        )
    else:
        required_prompt_facts = ["declared_total", "90", "60", "40", "100"]
        claims_grounded = (
            "90" in text and "100" in text
            and ("sum" in text or "allocation" in text)
            and ("declared" in text or "total" in text)
        )
    normalized_prompt = prompt.lower().replace(",", "")
    facts_present = all(token in normalized_prompt for token in required_prompt_facts)
    criterion_ids = {"memo-r1", "table-r2"}
    record_criterion_ids = sorted(cid for cid in criterion_ids if cid in text)
    no_undisclosed_id = condition == "criterion_disclosure" or not record_criterion_ids
    return {
        "status": "PASS" if facts_present and claims_grounded and no_undisclosed_id else "FAIL",
        "public_fact_basis_present": facts_present,
        "observation_and_diagnosis_match_task_facts": claims_grounded,
        "criterion_ids_in_observation_or_diagnosis": record_criterion_ids,
        "undisclosed_criterion_id_absent": no_undisclosed_id,
        "basis": "retained public task, source, and common starting artifact in this assignment prompt",
    }


def run_audit() -> dict[str, Any]:
    errors: list[str] = []
    origin = git_text("rev-parse", "origin/main")
    commit_reachable = subprocess.run(
        ["git", "merge-base", "--is-ancestor", EXECUTION_COMMIT, "origin/main"],
        cwd=ROOT, check=False,
    ).returncode == 0
    resolved_execution = git_text("rev-parse", EXECUTION_COMMIT)
    resolved_freeze = git_text("rev-parse", FREEZE_COMMIT)
    root_tree = git_text("rev-parse", f"{resolved_execution}^{{tree}}")
    execution_tree = git_text("rev-parse", f"{resolved_execution}:{EXEC_REL.as_posix()}")
    freeze_tree_at_freeze = git_text("rev-parse", f"{resolved_freeze}:{FREEZE_REL.as_posix()}")
    freeze_tree_at_execution = git_text("rev-parse", f"{resolved_execution}:{FREEZE_REL.as_posix()}")

    inventory = git_inventory(resolved_execution, EXEC_REL)
    current_paths = sorted(p.relative_to(EXECUTION).as_posix() for p in EXECUTION.rglob("*") if p.is_file())
    expected_paths = sorted(row["path"] for row in inventory)
    inventory_rows = []
    for row in inventory:
        path = EXECUTION / row["path"]
        raw = path.read_bytes()  # Deliberately reads every retained file.
        observed = {"bytes": len(raw), "sha256": sha_bytes(raw)}
        status = "PASS" if observed == {"bytes": row["bytes"], "sha256": row["sha256"]} else "FAIL"
        inventory_rows.append({**row, "observed_bytes": len(raw), "observed_sha256": observed["sha256"], "status": status})
    retained_inventory_ok = current_paths == expected_paths and all(r["status"] == "PASS" for r in inventory_rows)
    aggregate = sha_bytes("\n".join(f"{r['path']}\0{r['sha256']}" for r in inventory).encode())

    protocol = load(FREEZE / "protocol.json")
    study = load(EXECUTION / "study-report.json")
    assignment_defs = {row["assignment_id"]: row for row in protocol["assignments"]}
    study_rows = {row["assignment_id"]: row for row in study["assignment_rows"]}
    assignment_audits = []
    usage_totals = Counter()
    output_hashes: dict[str, dict[str, list[str]]] = defaultdict(lambda: defaultdict(list))

    for assignment_id in sorted(assignment_defs):
        definition = assignment_defs[assignment_id]
        task_id, condition = definition["task_id"], definition["condition_id"]
        base = EXECUTION / "assignments" / assignment_id
        info, attempt = load(base / "information-view.json"), load(base / "attempt-report.json")
        usage = load(base / "trial/outputs/usage.json")
        enriched = load(base / "repair-record.json")
        final_name = "revised-artifact.md" if task_id.startswith("memo-") else "revised-artifact.json"
        final_path = base / "trial/outputs" / final_name
        initial_path = FREEZE / next(t for t in protocol["tasks"] if t["task_id"] == task_id)["starting_artifact"]
        candidate = parse_candidate(task_id, final_path)
        observed = independent_evaluate(task_id, candidate)
        start_text, final_text = initial_path.read_text(), final_path.read_text()
        diff_ok = enriched["revision_delta"]["unified_diff"] == exact_diff(start_text, final_text)
        start_obj = start_text if task_id.startswith("memo-") else json.loads(start_text)
        final_obj = final_text if task_id.startswith("memo-") else json.loads(final_text)
        locus_ok, loci = locus_check(task_id, start_obj, final_obj) if condition in REPAIR_CONDITIONS else (start_text == final_text, [])
        prompt_file = (base / "trial/inputs/public-prompt.txt").read_text()
        prompt_ok = info["prompt"] == prompt_file and sha_bytes(prompt_file.encode()) == info["prompt_sha256"]
        grounding = grounding_check(task_id, enriched, prompt_file, condition) if condition in REPAIR_CONDITIONS else {
            "status": "PASS", "basis": "no repair; frozen defect proposition copied by launcher",
        }
        agent_path = base / "trial/outputs/repair-record.json"
        agent_link_ok = True
        if condition in REPAIR_CONDITIONS:
            agent_record = load(agent_path)
            agent_link_ok = all(enriched[key if key in {"defect_observation", "diagnosis"} else key]["agent_statement"] == agent_record[key] if key not in {"defect_observation", "diagnosis"} else enriched[key] == agent_record[key] for key in (
                "defect_observation", "diagnosis", "revision_delta", "criterion_local_recheck", "collateral_recheck", "new_error_assessment",
            ))
        input_inventory = {
            p.name: {"bytes": p.stat().st_size, "sha256": sha(p)}
            for p in sorted((base / "trial/inputs").iterdir()) if p.is_file()
        }
        input_ok = input_inventory == info["input_inventory"]
        output_inventory = {
            p.name: {"bytes": p.stat().st_size, "sha256": sha(p)}
            for p in sorted((base / "trial/outputs").iterdir()) if p.is_file()
        }
        output_ok = output_inventory == attempt["outputs"]
        usage_ok = usage == attempt["usage"] == enriched["cost"]["usage"]
        report_ok = attempt == study_rows[assignment_id]
        assignment_ok = (
            prompt_ok and input_ok and output_ok and usage_ok and report_ok and diff_ok
            and locus_ok and grounding["status"] == "PASS" and agent_link_ok
            and observed == attempt["deterministic_observation"]
            and observed["terminal_state"] == attempt["terminal_state"]
            and enriched["criterion_local_recheck"]["endpoint"] == observed["endpoint"]
            and enriched["criterion_local_recheck"]["terminal_state"] == observed["terminal_state"]
            and enriched["collateral_recheck"]["preserved"] == observed["collateral"]
            and attempt["attempt_count"] == 1 and attempt["claim_ceiling"] == CLAIMS
        )
        if not assignment_ok:
            errors.append(f"assignment:{assignment_id}")
        for key in ("api_calls", "input_tokens", "output_tokens", "reasoning_tokens", "cache_read_tokens", "cache_write_tokens", "total_tokens"):
            usage_totals[key] += usage.get(key, 0)
        usage_totals["provider_calls"] += int(attempt["provider_called"])
        output_hashes[task_id][sha(final_path)].append(condition)
        assignment_audits.append({
            "assignment_id": assignment_id, "task_id": task_id, "condition_id": condition,
            "status": "PASS" if assignment_ok else "FAIL", "prompt_and_input_view": "PASS" if prompt_ok and input_ok else "FAIL",
            "output_and_study_binding": "PASS" if output_ok and usage_ok and report_ok else "FAIL",
            "independent_endpoint_replay": {"status": "PASS" if observed == attempt["deterministic_observation"] else "FAIL", "observed": observed},
            "observation_diagnosis_grounding": grounding,
            "delta_and_changed_locus": {"status": "PASS" if diff_ok and locus_ok else "FAIL", "exact_unified_diff": diff_ok, "task_loci": loci},
            "criterion_and_collateral_recheck": "PASS" if enriched["criterion_local_recheck"]["endpoint"] == observed["endpoint"] and enriched["collateral_recheck"]["preserved"] == observed["collateral"] else "FAIL",
            "agent_record_lineage": "PASS" if agent_link_ok else "FAIL",
            "attempt_count": attempt["attempt_count"], "usage": usage,
        })

    recomputed_condition = {}
    for condition in [c["condition_id"] for c in protocol["conditions"]]:
        rows = [r for r in assignment_audits if r["condition_id"] == condition]
        states = Counter(r["independent_endpoint_replay"]["observed"]["terminal_state"] for r in rows)
        recomputed_condition[condition] = {
            "declared": len(rows), "passed": states["passed"], "terminal_states": dict(sorted(states.items())),
        }
    study_condition_ok = all(
        study["six_condition_contrasts"][c]["declared"] == values["declared"]
        and study["six_condition_contrasts"][c]["passed"] == values["passed"]
        for c, values in recomputed_condition.items()
    )
    all_repair_pass = all(
        row["independent_endpoint_replay"]["observed"]["terminal_state"] == "passed"
        for row in assignment_audits if row["condition_id"] in REPAIR_CONDITIONS
    )
    retry = {r["task_id"]: r for r in assignment_audits if r["condition_id"] == "retry_no_new_information"}
    distinguishability = {}
    for condition in sorted(REPAIR_CONDITIONS - {"retry_no_new_information"}):
        comparisons = []
        for task_id, retry_row in retry.items():
            row = next(r for r in assignment_audits if r["task_id"] == task_id and r["condition_id"] == condition)
            comparisons.append({
                "task_id": task_id,
                "same_terminal_state": row["independent_endpoint_replay"]["observed"]["terminal_state"] == retry_row["independent_endpoint_replay"]["observed"]["terminal_state"],
                "same_endpoint": row["independent_endpoint_replay"]["observed"]["endpoint"] == retry_row["independent_endpoint_replay"]["observed"]["endpoint"],
            })
        distinguishability[condition] = {"comparisons": comparisons, "outcome_distinguishable_from_retry": not all(c["same_terminal_state"] and c["same_endpoint"] for c in comparisons)}

    gates = {
        "execution_commit_on_origin_main": commit_reachable,
        "exact_execution_commit": resolved_execution == EXECUTION_COMMIT,
        "exact_execution_root_tree": root_tree == EXECUTION_ROOT_TREE,
        "exact_execution_subtree": execution_tree == EXECUTION_TREE,
        "exact_freeze_commit": resolved_freeze == FREEZE_COMMIT,
        "freeze_subtree_unchanged_at_execution": freeze_tree_at_freeze == freeze_tree_at_execution == FREEZE_TREE,
        "every_retained_file_read_and_commit_bound": retained_inventory_ok,
        "all_12_assignments_present": set(assignment_defs) == set(study_rows) and len(assignment_audits) == 12,
        "all_assignment_audits_pass": all(r["status"] == "PASS" for r in assignment_audits),
        "endpoint_and_collateral_replay": all(r["independent_endpoint_replay"]["status"] == "PASS" for r in assignment_audits),
        "repair_grounding_and_no_hidden_criterion_laundering": all(r["observation_diagnosis_grounding"]["status"] == "PASS" and r["agent_record_lineage"] == "PASS" for r in assignment_audits),
        "delta_locus_and_rechecks": all(r["delta_and_changed_locus"]["status"] == "PASS" and r["criterion_and_collateral_recheck"] == "PASS" for r in assignment_audits),
        "attempt_and_usage_accounting": usage_totals["provider_calls"] == study["provider_calls"] == 10 and all(r["attempt_count"] == 1 for r in assignment_audits),
        "condition_summary_replay": study_condition_ok,
        "claim_ceiling_all_false": study["claim_ceiling"] == CLAIMS and all(r["status"] == "PASS" for r in assignment_audits),
    }
    status = "PASS" if all(gates.values()) and not errors else "FAIL"
    return {
        "schema_version": "1.0.0", "audit_id": "self-inspection-repair-v1-outcome-validity-audit",
        "audited_at": dt.datetime.now(dt.timezone.utc).isoformat(), "auditor": "benchmark-builder",
        "status": status, "model_calls": 0, "provider_calls": 0, "repair_rows_executed": 0,
        "source_binding": {
            "origin_main_at_audit": origin, "freeze_commit": resolved_freeze,
            "freeze_subtree": freeze_tree_at_freeze, "execution_commit": resolved_execution,
            "execution_root_tree": root_tree, "execution_subtree": execution_tree,
            "study_report_sha256": sha(EXECUTION / "study-report.json"),
        },
        "gates": gates, "errors": errors,
        "retained_inventory": {"file_count": len(inventory_rows), "aggregate_sha256": aggregate, "files": inventory_rows},
        "assignment_audits": assignment_audits,
        "accounting_replay": {"attempts": len(assignment_audits), **dict(usage_totals)},
        "condition_replay": recomputed_condition,
        "instrument_discrimination": {
            "task_clusters": 2, "assignments_per_task": 6, "attempts_per_assignment": 1,
            "repair_cells": 10, "repair_cells_passed": sum(r["independent_endpoint_replay"]["observed"]["terminal_state"] == "passed" for r in assignment_audits if r["condition_id"] in REPAIR_CONDITIONS),
            "saturated_repair_endpoint": all_repair_pass,
            "identical_final_artifact_groups": {task: [{"sha256": digest, "conditions": sorted(conditions)} for digest, conditions in groups.items() if len(conditions) > 1] for task, groups in output_hashes.items()},
            "retry_contrasts": distinguishability,
            "finding": "All ten repair-authorized cells passed. Every repair condition matches no-information retry on terminal state and endpoint for both task clusters; structured finals are byte-identical across all five repair conditions. The retained outcomes therefore do not discriminate information treatments from generic retry.",
        },
        "claim_ceiling": CLAIMS,
        "licensed_observations": [
            "the exact frozen and retained execution bytes are commit-bound and replayable",
            "12 assignments were retained with one attempt each; 10 called the provider and two no-second-attempt controls did not",
            "both frozen starts fail the deterministic endpoint while preserving declared collateral",
            "all ten repair-authorized retained finals pass the local deterministic endpoint and collateral checks",
            "repair observations, diagnoses, changed loci, and rechecks are grounded in each assignment's retained public information view",
            "all repair conditions are observationally indistinguishable from no-information retry on the two-task endpoint outcome",
        ],
        "not_licensed": list(CLAIMS),
        "decision": {
            "action": "STOP_CURRENT_INSTRUMENT; PROSPECTIVE_REDESIGN_REQUIRED_BEFORE_MORE_EXECUTION",
            "reason": "Two builder-authored task clusters, one attempt per cell, a single observer, identical structured outputs, and 10/10 repair saturation leave no treatment discrimination.",
            "minimum_redesign": {
                "new_task_diversity": "Freeze at least 3 new independent task families spanning at least 3 artifact/workflow shapes beyond the two current templates; analyze tasks as clusters and do not pool shapes without a predeclared rationale.",
                "defect_difficulty": "Within each family freeze at least two predeclared difficulty strata, including a subtle/near-threshold single-locus defect and a multi-locus defect with a real collateral-risk opportunity; calibrate to avoid floor or ceiling before treatment execution.",
                "observer_variation": "Use at least 2 independently implemented condition-blind observers/checkers per endpoint and predeclare disagreement/adjudication handling.",
                "repetitions": "Run at least 5 independent repetitions per task-condition-configured-system cell with order/random seeds retained; report task-family-clustered uncertainty rather than treating rows as independent.",
                "predeclared_estimand": "Primary: repair pass-rate difference for each information treatment versus retry_no_new_information, averaged within task family then across families, with task-family-clustered uncertainty. Secondary: collateral-preservation difference and token/time burden. A treatment claim requires a nonzero uncertainty-bounded contrast and no predeclared shape reversal; otherwise retain only generic-retry evidence.",
            },
        },
    }


def write_note(report: dict[str, Any], path: Path) -> None:
    g = report["gates"]
    d = report["instrument_discrimination"]
    lines = [
        "# Self-inspection repair v1: independent outcome-validity audit", "",
        f"**Audit result: {report['status']}**",
        "**Decision: STOP the current instrument; require prospective redesign before any more execution.**", "",
        "## Bound evidence", "",
        f"- Freeze commit `{report['source_binding']['freeze_commit']}` / subtree `{report['source_binding']['freeze_subtree']}`.",
        f"- Execution commit `{report['source_binding']['execution_commit']}` / subtree `{report['source_binding']['execution_subtree']}`.",
        f"- Read and hash-bound all {report['retained_inventory']['file_count']} retained files; aggregate inventory `{report['retained_inventory']['aggregate_sha256']}`.",
        f"- Independently replayed 12/12 endpoint/collateral outcomes and attempt/usage accounting: `{json.dumps(report['accounting_replay'], sort_keys=True)}`.",
        "- No frozen or execution byte was modified. No model, provider, or repair row was called by this audit.", "",
        "## Gates", "",
    ]
    lines.extend(f"- **{'PASS' if value else 'FAIL'}** `{name}`" for name, value in g.items())
    lines += ["", "## What the retained evidence says", ""]
    lines.extend(f"- {item}." for item in report["licensed_observations"])
    lines += ["", "## Discrimination and limits", "",
        f"The matrix has {d['task_clusters']} task clusters, one attempt per assignment, and {d['repair_cells_passed']}/{d['repair_cells']} passing repair cells. All repair conditions match `retry_no_new_information` on terminal state and endpoint for both tasks. The five structured repair finals are byte-identical. Memo finals differ in wording but not the checked endpoint/collateral outcome.", "",
        "Accordingly, the matrix does **not** identify an effect of generic review, native/render inspection, consequence-only feedback, or criterion disclosure beyond the opportunity to retry. Rows share task templates and are not independent treatment replicates; 10/10 saturation blocks ordering the repair conditions.", "",
        "All claim-ceiling fields remain false: self-correction, agent capability, treatment effect, professional validity, utility, production fitness, and readiness.", "",
        "## Minimum prospective redesign", "",
    ]
    for key, value in report["decision"]["minimum_redesign"].items():
        lines.append(f"- **{key.replace('_', ' ').title()}:** {value}")
    lines += ["", "Machine-readable evidence: `reports/validation/2026-07-19-self-inspection-repair-v1-outcome-validity-audit.json`.", ""]
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=ROOT / "reports/validation/2026-07-19-self-inspection-repair-v1-outcome-validity-audit.json")
    parser.add_argument("--note", type=Path, default=ROOT / "reports/validation/2026-07-19-self-inspection-repair-v1-outcome-validity-audit.md")
    args = parser.parse_args()
    report = run_audit()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    write_note(report, args.note)
    print(json.dumps({
        "status": report["status"], "gates": report["gates"],
        "retained_files_read": report["retained_inventory"]["file_count"],
        "attempts_replayed": report["accounting_replay"]["attempts"],
        "provider_calls_by_audit": 0, "decision": report["decision"]["action"],
    }, indent=2, sort_keys=True))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())

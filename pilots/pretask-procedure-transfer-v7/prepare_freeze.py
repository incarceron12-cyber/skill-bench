#!/usr/bin/env python3
"""Materialize the prospective v7 endpoint freeze without model/provider calls."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
V4 = ROOT / "pilots/pretask-procedure-transfer-v4"
V5 = ROOT / "pilots/pretask-procedure-transfer-v5"
V6 = ROOT / "pilots/pretask-procedure-transfer-v6"
TASK_IDS = ("k4n7", "p9c2", "t6v1", "w3d8")
ATTEMPTS = {"model": 0, "provider": 0, "executor": 0, "repair": 0, "retry": 0}
CLAIMS = {name: False for name in ("agent_capability", "expert_provenance", "production_fitness", "professional_validity", "readiness", "transfer", "utility")}


def dump(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def statement_sha(statement: str) -> str:
    return hashlib.sha256(statement.encode("utf-8")).hexdigest()


def builder_epsilon(task_id: str, case: dict[str, Any]) -> dict[str, Any]:
    # Builder implementation is intentionally separate from oracle.py.
    priority = ("signed_scan", "unsigned_note")
    decisions = []
    for batch in case["batches"]:
        rows = [row for row in case["observations"] if row["batch_id"] == batch["batch_id"]]
        controls: dict[str, str] = {}
        disposition = "release"
        for seal in batch["required_seals"]:
            in_time = [row for row in rows if row["seal"] == seal and 0 <= case["review_hour"] - row["hour"] <= 24]
            selected = []
            for record_type in priority:
                selected = [row for row in in_time if row["record_type"] == record_type]
                if selected:
                    break
            if not selected or len({row["state"] for row in selected}) != 1:
                disposition = "quarantine"
                continue
            chosen = sorted(selected, key=lambda row: (row["hour"], row["observation_id"]))[-1]
            controls[seal] = chosen["observation_id"]
            if chosen["state"] != "intact":
                disposition = "quarantine"
        decisions.append({"batch_id": batch["batch_id"], "controlling_seals": controls,
                          "disposition": disposition, "observation_ids": [row["observation_id"] for row in rows],
                          "reason": "builder-derived source-rule consequence"})
    return {"task_id": task_id, "decisions": decisions}


def builder_zeta(task_id: str, case: dict[str, Any]) -> dict[str, Any]:
    ordered = sorted(case["events"], key=lambda row: row["seq"])
    active: list[tuple[str, dict[str, Any]]] = []
    committed: list[str] = []
    rolled: list[str] = []
    roots: dict[str, dict[str, Any]] = {}
    seen: set[str] = set()
    valid = len({row["seq"] for row in ordered}) == len(ordered)
    for event in ordered if valid else []:
        op, txid = event["operation"], event.get("transaction")
        if op == "begin":
            if type(txid) is not str or txid in seen:
                valid = False; break
            seen.add(txid); state: dict[str, Any] = {}; active.append((txid, state)); roots[txid] = state
        elif op == "set":
            if not active or type(event.get("key")) is not str:
                valid = False; break
            active[-1][1][event["key"]] = event.get("value")
        elif op == "commit":
            if not active or active[-1][0] != txid:
                valid = False; break
            name, state = active.pop(); committed.append(name)
            if active:
                active[-1][1].update(state); roots.pop(name, None)
        elif op == "rollback":
            names = [name for name, _ in active]
            if txid not in names:
                valid = False; break
            index = names.index(txid)
            for name, _ in reversed(active[index:]):
                rolled.append(name); roots.pop(name, None)
            del active[index:]
        else:
            valid = False; break
    valid = valid and not active
    final: dict[str, Any] | None = None
    if valid:
        final = {}
        for name in committed:
            if name in roots:
                final.update(roots[name])
    return {"task_id": task_id, "journal_id": case["journal_id"], "valid": valid, "final_state": final,
            "committed_transactions": committed, "rolled_back_transactions": rolled,
            "reason": "builder-derived source-rule consequence"}


def expected(task_id: str, case: dict[str, Any]) -> dict[str, Any]:
    return builder_epsilon(task_id, case) if case["family_id"] == "family-epsilon" else builder_zeta(task_id, case)


def public_markdown(task_id: str, family: str) -> str:
    if family == "family-epsilon":
        shape = '{\n  "task_id": string,\n  "decisions": [{\n    "batch_id": string,\n    "disposition": "release" | "quarantine",\n    "reason": non-empty string,\n    "controlling_seals": {string seal: string observation_id},\n    "observation_ids": [string observation_id]\n  }]\n}'
        order = "Decision object order and observation_ids order are not scored; duplicate identifiers are invalid."
    else:
        shape = '{\n  "task_id": string,\n  "journal_id": string,\n  "valid": boolean,\n  "final_state": object | null,\n  "committed_transactions": [string transaction_id],\n  "rolled_back_transactions": [string transaction_id],\n  "reason": non-empty string\n}'
        order = "Transaction arrays are chronological and ordered."
    return f"""# Procedure-transfer task {task_id}\n\n## Objective\nApply the supplied family procedure to the complete public `input.json`.\n\n## Deliverable\nWrite `outputs/result.json` as exactly one JSON object with this closed shape:\n\n```text\n{shape}\n```\n\nNo additional key is permitted at any object level. Repeated JSON keys, `condition_id`, treatment metadata, and uncontracted payloads are invalid. `reason` wording is not scored. {order}\n\n## Exact JSON policy\nBooleans, null, strings, arrays, objects, integer-form numbers, and decimal/exponent-form numbers are distinct. In particular, `true` is not `1`, `false` is not `0`, and `1` is not `1.0`. Object key order and JSON whitespace are not semantic. Non-finite numbers are invalid.\n\n## Fair consequence basis\nAll identifiers and values needed for the result are in `input.json`; the assigned procedure material supplies the applicable family rules. The checker may enforce only this disclosed contract and consequences of those inputs and rules.\n"""


def applicability_record() -> dict[str, Any]:
    # Carry the v6 authority decision forward; do not reconstruct or tune the
    # proposition lineage while repairing unrelated canary/preflight mechanics.
    record = json.loads((V6 / "source-applicability.json").read_text())
    record["record_id"] = "pretask-procedure-transfer-v7-source-applicability"
    record["authorized_instrument"] = "pretask-procedure-transfer-v7"
    record["valid_time"] = "v7 only"
    record["parent_authority"] = {
        "path": "pilots/pretask-procedure-transfer-v6/source-applicability.json",
        "sha256": sha(V6 / "source-applicability.json"),
        "decision": "carry_forward_without_semantic_tuning",
    }
    record["decision"] = (
        "Carry unchanged v6 proposition lineage and interpretation into synthetic v7 internal calibration only; "
        "repair only the outer-envelope canary and dependency-check mechanics."
    )
    for row in record["proposition_lineage"]:
        row["v7_applicability"] = "authorized_internal_calibration_v7_only"
        row.pop("v6_applicability", None)
        if "v6_interpretation" in row:
            row["v7_interpretation"] = row.pop("v6_interpretation")
    return record


def main() -> None:
    # Copy public inputs byte-for-byte as task data, then issue fresh v7 task/answer records.
    for task_id in TASK_IDS:
        case = json.loads((V5 / f"tasks/{task_id}/input.json").read_text())
        dump(HERE / f"tasks/{task_id}/input.json", case)
        (HERE / f"tasks/{task_id}/public.md").write_text(public_markdown(task_id, case["family_id"]), encoding="utf-8")
        dump(HERE / f"tasks/{task_id}/private.json", {"schema_version": "0.3.0", "task_id": task_id,
             "family_id": case["family_id"], "expected_semantics": expected(task_id, case),
             "reason_policy": "non_empty_wording_invariant", "artifact_contract": "closed_keys_recursive_exact_json_v7",
             "public_input_path": f"pilots/pretask-procedure-transfer-v7/tasks/{task_id}/input.json",
             "source_applicability_path": "pilots/pretask-procedure-transfer-v7/source-applicability.json",
             "attempts": ATTEMPTS, "claim_ceiling": CLAIMS})
    dump(HERE / "source-applicability.json", applicability_record())
    v5_rows = json.loads((V5 / "assignments.json").read_text())["rows"]
    rows = [{**row, "order_seed": "pretask-procedure-transfer-v7-preserve-v4-order", "attempts": 0} for row in v5_rows]
    dump(HERE / "assignments.json", {"algorithm": "Preserve all v4/v5 cells and order; reset only v7 attempts.", "rows": rows})
    v4_protocol = json.loads((V4 / "protocol.json").read_text())
    protocol = {"schema_version": "0.3.0", "protocol_id": "pretask-procedure-transfer-v7",
        "status": "prospectively_frozen_zero_call_pending_independent_review", "execution_authorized": False,
        "fork_boundary": "V4, v5, and failed v6 remain byte-immutable and are not rescored; v7 starts with zero attempts.",
        "source_applicability": {"path": "pilots/pretask-procedure-transfer-v7/source-applicability.json"},
        "parent_review": {"path": "docs/concepts/pretask-procedure-transfer-v5-independent-freeze-review.md", "sha256": sha(ROOT / "docs/concepts/pretask-procedure-transfer-v5-independent-freeze-review.md")},
        "parent_failed_freeze": {"manifest_path": "pilots/pretask-procedure-transfer-v6/freeze-manifest.json",
            "manifest_sha256": sha(V6 / "freeze-manifest.json"),
            "canary_path": "pilots/pretask-procedure-transfer-v6/canary-report.json",
            "canary_sha256": sha(V6 / "canary-report.json"),
            "preflight_path": "pilots/pretask-procedure-transfer-v6/preflight-report.json",
            "preflight_sha256": sha(V6 / "preflight-report.json")},
        "conditions": v4_protocol["conditions"], "equal_envelope": v4_protocol["equal_envelope"],
        "attempt_ledger": ATTEMPTS, "claim_ceiling": CLAIMS,
        "independence": {"builder": "prepare_freeze.py local derivation", "oracle": "oracle.py imports no builder/checker/preflight",
                         "checker": "checkers/check_endpoint.py consumes only candidate/private", "preflight": "preflight.py compares independent outputs"},
        "numeric_policy": "integer-form and decimal/exponent-form JSON numbers are distinct; bool is never numeric; non-finite rejected",
        "required_next_gate": "separate commit-bound independent freeze review before any model/provider/executor row",
        "charter_decision_filter": {"objectives": ["B: expertise-to-evaluation methodology", "C: executable benchmark infrastructure"],
            "artifact": "Source-authorized, closed-contract, independently-oracled v7 zero-call freeze.",
            "uncertainty": "Whether applicability, checker-language closure, and semantic-independence gates pass before costly trials.",
            "mode": "building and validation", "duplication_and_scope": "Repairs only failed v6 canary/dependency gates; synthetic families remain reusable mechanism probes.",
            "useful_completion": "Hashes, parity, source mutations, strict JSON mutations, canaries, zero attempts, and false claims pass; execution remains gated."}}
    dump(HERE / "protocol.json", protocol)
    crosswalk = json.loads((V5 / "fair-basis-crosswalk.json").read_text())
    crosswalk["schema_version"] = "0.2.0"
    crosswalk["source_authority"] = "pilots/pretask-procedure-transfer-v7/source-applicability.json"
    for row in crosswalk["rows"]:
        row["closed_contract_basis"] = "public.md:Deliverable and Exact JSON policy"
    dump(HERE / "fair-basis-crosswalk.json", crosswalk)

    component_rel = ["README.md", "assignments.json", "checkers/check_endpoint.py", "fair-basis-crosswalk.json", "oracle.py",
                     "preflight.py", "prepare_freeze.py", "protocol.json", "run_canaries.py", "source-applicability.json"]
    for task_id in TASK_IDS:
        component_rel.extend((f"tasks/{task_id}/input.json", f"tasks/{task_id}/private.json", f"tasks/{task_id}/public.md"))
    components = [{"path": f"pilots/pretask-procedure-transfer-v7/{rel}", "bytes": (HERE / rel).stat().st_size, "sha256": sha(HERE / rel)} for rel in sorted(component_rel)]
    external_paths = ["pilots/pretask-procedure-transfer-v4/families/epsilon/corpus.json", "pilots/pretask-procedure-transfer-v4/families/zeta/corpus.json",
                      "pilots/pretask-procedure-transfer-v4/freeze-manifest.json", "pilots/pretask-procedure-transfer-v4/candidate-freeze-manifest.json",
                      "pilots/pretask-procedure-transfer-v4/hindsight-freeze-manifest.json", "pilots/pretask-procedure-transfer-v5/freeze-manifest.json", "tests/test_pretask_procedure_transfer_v7.py",
                      "reports/validation/2026-07-18-pretask-procedure-v5-independent-freeze-audit.json"]
    v6_manifest = json.loads((V6 / "freeze-manifest.json").read_text())
    external_paths.extend(row["path"] for row in v6_manifest["components"])
    external_paths.extend(("pilots/pretask-procedure-transfer-v6/freeze-manifest.json",
                           "pilots/pretask-procedure-transfer-v6/canary-report.json",
                           "pilots/pretask-procedure-transfer-v6/preflight-report.json"))
    external_paths = list(dict.fromkeys(external_paths))
    external = [{"path": rel, "bytes": (ROOT / rel).stat().st_size, "sha256": sha(ROOT / rel)} for rel in external_paths]
    dump(HERE / "freeze-manifest.json", {"manifest_version": "1.0.0", "study_id": "pretask-procedure-transfer-v7",
         "status": "frozen_zero_call_pending_independent_review", "components": components, "external_immutable_bindings": external,
         "attempt_ledger": ATTEMPTS, "executor_authorized": False, "claim_ceiling": CLAIMS})


if __name__ == "__main__":
    main()

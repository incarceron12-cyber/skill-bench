#!/usr/bin/env python3
"""Materialize the prospective v5 endpoint-instrument repair without model calls."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
V4 = ROOT / "pilots/pretask-procedure-transfer-v4"
CLAIMS = {
    "agent_capability": False,
    "expert_provenance": False,
    "production_fitness": False,
    "professional_validity": False,
    "readiness": False,
    "transfer": False,
    "utility": False,
}
CASES = {
    "k4n7": {
        "family_id": "family-epsilon", "review_hour": 100,
        "batches": [{"batch_id": "L8", "required_seals": ["red", "blue"]}],
        "observations": [
            {"observation_id": "o1", "batch_id": "L8", "record_type": "signed_scan", "seal": "red", "state": "intact", "hour": 90},
            {"observation_id": "o2", "batch_id": "L8", "record_type": "unsigned_note", "seal": "red", "state": "broken", "hour": 95},
            {"observation_id": "o3", "batch_id": "L8", "record_type": "signed_scan", "seal": "blue", "state": "intact", "hour": 80},
        ],
    },
    "p9c2": {
        "family_id": "family-epsilon", "review_hour": 60,
        "batches": [{"batch_id": "Q3", "required_seals": ["amber", "green"]}],
        "observations": [
            {"observation_id": "r1", "batch_id": "Q3", "record_type": "unsigned_note", "seal": "amber", "state": "intact", "hour": 51},
            {"observation_id": "r2", "batch_id": "Q3", "record_type": "signed_scan", "seal": "amber", "state": "intact", "hour": 49},
            {"observation_id": "r3", "batch_id": "Q3", "record_type": "signed_scan", "seal": "green", "state": "intact", "hour": 55},
        ],
    },
    "t6v1": {
        "family_id": "family-zeta", "journal_id": "J6",
        "events": [
            {"seq": 1, "operation": "begin", "transaction": "A"},
            {"seq": 2, "operation": "set", "key": "x", "value": 1},
            {"seq": 3, "operation": "begin", "transaction": "B"},
            {"seq": 4, "operation": "set", "key": "x", "value": 2},
            {"seq": 5, "operation": "rollback", "transaction": "B"},
            {"seq": 6, "operation": "commit", "transaction": "A"},
        ],
    },
    "w3d8": {
        "family_id": "family-zeta", "journal_id": "J9",
        "events": [
            {"seq": 4, "operation": "commit", "transaction": "C"},
            {"seq": 1, "operation": "begin", "transaction": "C"},
            {"seq": 3, "operation": "set", "key": "mode", "value": "ready"},
            {"seq": 2, "operation": "set", "key": "count", "value": 2},
            {"seq": 5, "operation": "begin", "transaction": "D"},
        ],
    },
}
SCHEMAS = {
    "family-epsilon": {
        "task_id": "string", "decisions": "array<object>", "decisions[].batch_id": "string",
        "decisions[].disposition": "string enum[release,quarantine]", "decisions[].reason": "non-empty string; wording is not scored",
        "decisions[].controlling_seals": "object<string,string observation_id>",
        "decisions[].observation_ids": "array<string observation_id>",
    },
    "family-zeta": {
        "task_id": "string", "journal_id": "string", "valid": "boolean", "final_state": "object or null",
        "committed_transactions": "array<string transaction_id>", "rolled_back_transactions": "array<string transaction_id>",
        "reason": "non-empty string; wording is not scored",
    },
}

def dump(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def derive_epsilon(task_id: str, case: dict) -> dict:
    rank = {"signed_scan": 2, "unsigned_note": 1}
    decisions = []
    for batch in case["batches"]:
        observations = [o for o in case["observations"] if o["batch_id"] == batch["batch_id"]]
        controlling = {}
        release = True
        for seal in batch["required_seals"]:
            candidates = [o for o in observations if o["seal"] == seal]
            best_rank = max((rank[o["record_type"]] for o in candidates), default=-1)
            best = [o for o in candidates if rank[o["record_type"]] == best_rank]
            states = {o["state"] for o in best}
            if not best or len(states) != 1:
                release = False
                continue
            chosen = max(best, key=lambda o: (o["hour"], o["observation_id"]))
            controlling[seal] = chosen["observation_id"]
            if chosen["state"] != "intact" or case["review_hour"] - chosen["hour"] > 24:
                release = False
        decisions.append({
            "batch_id": batch["batch_id"], "disposition": "release" if release else "quarantine",
            "controlling_seals": controlling,
            "observation_ids": [o["observation_id"] for o in observations],
            "reason": "all required seals satisfy the controlling-evidence rule" if release else "one or more required seals fail the controlling-evidence rule",
        })
    return {"task_id": task_id, "decisions": decisions}


def derive_zeta(task_id: str, case: dict) -> dict:
    events = sorted(case["events"], key=lambda e: e["seq"])
    if len({e["seq"] for e in events}) != len(events):
        return {"task_id": task_id, "journal_id": case["journal_id"], "valid": False, "final_state": None,
                "committed_transactions": [], "rolled_back_transactions": [], "reason": "duplicate sequence number"}
    stack, tx, committed, rolled = [], {}, [], []
    structurally_valid = True
    for event in events:
        op = event["operation"]
        if op == "begin":
            stack.append(event["transaction"]); tx[event["transaction"]] = {}
        elif op == "set":
            if not stack: structurally_valid = False; break
            tx[stack[-1]][event["key"]] = event["value"]
        elif op in {"commit", "rollback"}:
            if not stack or stack[-1] != event["transaction"]: structurally_valid = False; break
            current = stack.pop()
            if op == "rollback":
                rolled.append(current); tx.pop(current, None)
            elif stack:
                tx[stack[-1]].update(tx.pop(current)); committed.append(current)
            else:
                committed.append(current)
        else:
            structurally_valid = False; break
    valid = structurally_valid and not stack
    final = None
    if valid:
        final = {}
        for name in committed:
            if name in tx: final.update(tx[name])
    return {"task_id": task_id, "journal_id": case["journal_id"], "valid": valid, "final_state": final,
            "committed_transactions": committed, "rolled_back_transactions": rolled,
            "reason": "journal replay is structurally complete" if valid else "journal replay is structurally incomplete or invalid"}


def expected(task_id: str, case: dict) -> dict:
    return derive_epsilon(task_id, case) if case["family_id"] == "family-epsilon" else derive_zeta(task_id, case)


def public_markdown(task_id: str, case: dict) -> str:
    family = case["family_id"]
    objective = "Determine every batch release disposition." if family == "family-epsilon" else "Replay the journal and determine its certified terminal state."
    basis = ("Apply the supplied family source rules to every batch and observation."
             if family == "family-epsilon" else "Apply the supplied family source rules to every event in ascending seq order.")
    return f"""# Procedure-transfer task {task_id}\n\n## Objective\n{objective}\n\n## Inputs\nThe complete public task input is `input.json`. All identifiers that may be required in the result are disclosed there.\n\n## Deliverable\nWrite `outputs/result.json` as one JSON object using exactly these public field types:\n\n```json\n{json.dumps(SCHEMAS[family], indent=2, sort_keys=True)}\n```\n\n`reason` must be a non-empty explanation, but its wording is not scored. Array order is significant for committed and rolled-back transaction chronology; `observation_ids` is compared as a set. No undisclosed identifier or representation is required.\n\n## Fair consequence basis\n{basis}\nThe private checker may enforce only the disclosed types, identifiers, and semantic consequences of those public inputs and source rules.\n"""


def main() -> None:
    for task_id, case in CASES.items():
        dump(HERE / "tasks" / task_id / "input.json", case)
        (HERE / "tasks" / task_id / "public.md").write_text(public_markdown(task_id, case), encoding="utf-8")
        private = {
            "schema_version": "0.2.0", "task_id": task_id, "family_id": case["family_id"],
            "expected_semantics": expected(task_id, case), "reason_policy": "non_empty_string_wording_invariant",
            "public_input_path": f"pilots/pretask-procedure-transfer-v5/tasks/{task_id}/input.json",
            "source_rule_path": f"pilots/pretask-procedure-transfer-v4/families/{'epsilon' if case['family_id']=='family-epsilon' else 'zeta'}/corpus.json",
            "attempts": {"model": 0, "provider": 0, "executor": 0, "repair": 0, "retry": 0},
            "claim_ceiling": CLAIMS,
        }
        dump(HERE / "tasks" / task_id / "private.json", private)

    fair_rows = []
    for task_id, case in CASES.items():
        if case["family_id"] == "family-epsilon":
            fields = {
                "/task_id": ["public.md:Deliverable", "input.json:filename/task identity"],
                "/decisions/*/batch_id": ["public.md:Deliverable", "input.json:/batches/*/batch_id"],
                "/decisions/*/disposition": ["public.md:Deliverable", "v4 corpus:E-P2,E-P3,E-P4"],
                "/decisions/*/controlling_seals": ["public.md:Deliverable", "input.json:/observations", "v4 corpus:E-P2"],
                "/decisions/*/observation_ids": ["public.md:Deliverable", "input.json:/observations", "v4 corpus:E-P1"],
                "/decisions/*/reason": ["public.md:reason wording policy"],
            }
        else:
            fields = {
                "/task_id": ["public.md:Deliverable", "input.json:filename/task identity"],
                "/journal_id": ["public.md:Deliverable", "input.json:/journal_id"],
                "/valid": ["public.md:Deliverable", "v4 corpus:Z-P1,Z-P4"],
                "/final_state": ["public.md:Deliverable", "v4 corpus:Z-P2,Z-P3,Z-P4"],
                "/committed_transactions": ["public.md:Deliverable", "input.json:/events", "v4 corpus:Z-P2"],
                "/rolled_back_transactions": ["public.md:Deliverable", "input.json:/events", "v4 corpus:Z-P3"],
                "/reason": ["public.md:reason wording policy"],
            }
        fair_rows.append({"task_id": task_id, "checked_fields": fields, "hidden_obligations": []})
    dump(HERE / "fair-basis-crosswalk.json", {"schema_version": "0.1.0", "rows": fair_rows})

    old_rows = json.loads((V4 / "assignments.json").read_text())["rows"]
    rows = [{**row, "order_seed": "pretask-procedure-transfer-v5-preserve-v4-order", "attempts": 0} for row in old_rows]
    dump(HERE / "assignments.json", {"algorithm": "Preserve the prospectively randomized v4 row order; reset only the new-version attempt ledger.", "rows": rows})

    protocol = {
        "schema_version": "0.2.0", "protocol_id": "pretask-procedure-transfer-v5", "status": "prospectively_frozen_zero_call",
        "fork_boundary": "Only the defective endpoint instrument is versioned. v4 artifacts and scores remain immutable and are not rescored.",
        "parent_defect_audit": {"path": "pilots/pretask-procedure-transfer-v4/posthoc-endpoint-audit.json", "sha256": sha(V4 / "posthoc-endpoint-audit.json")},
        "reused_treatment_materials": {
            "source_families": ["pilots/pretask-procedure-transfer-v4/families/epsilon/corpus.json", "pilots/pretask-procedure-transfer-v4/families/zeta/corpus.json"],
            "candidate_freeze": {"path": "pilots/pretask-procedure-transfer-v4/candidate-freeze-manifest.json", "sha256": sha(V4 / "candidate-freeze-manifest.json")},
            "hindsight_freeze": {"path": "pilots/pretask-procedure-transfer-v4/hindsight-freeze-manifest.json", "sha256": sha(V4 / "hindsight-freeze-manifest.json")},
            "controls": "Reuse v4 frozen controls by exact manifest binding; do not regenerate or tune treatment content.",
        },
        "repair_invariants": [
            "expected semantics derive from frozen public input and source rules", "all required identifiers and JSON types are public",
            "reason wording is invariant", "consequence fields remain strict", "checker is condition blind", "assignment cells and order preserve v4 parity",
        ],
        "attempt_ledger": {"model": 0, "provider": 0, "executor": 0, "repair": 0, "retry": 0},
        "execution_authorized": False, "claim_ceiling": CLAIMS,
        "charter_decision_filter": {
            "objectives": ["B: expertise-to-evaluation methodology", "C: executable benchmark infrastructure"],
            "artifact": "Prospectively frozen typed semantic endpoint instrument and mutation-tested validator.",
            "uncertainty": "Whether the v4 procedure conditions can be compared after factual and fair-basis endpoint defects are removed.",
            "mode": "building and validation", "duplication_and_scope": "Repairs one invalid cross-family instrument without changing v4 or narrowing benchmark scope.",
            "useful_completion": "Independent derivation, fair basis, checker conformance, condition blindness, parity, zero-attempt, and claim gates all pass before execution.",
        },
    }
    dump(HERE / "protocol.json", protocol)

    component_paths = ["README.md", "assignments.json", "checkers/check_endpoint.py", "derive_expected.py", "fair-basis-crosswalk.json", "preflight.py", "prepare_freeze.py", "protocol.json"]
    for task_id in CASES:
        component_paths += [f"tasks/{task_id}/input.json", f"tasks/{task_id}/public.md", f"tasks/{task_id}/private.json"]
    components = [{"path": f"pilots/pretask-procedure-transfer-v5/{rel}", "bytes": (HERE / rel).stat().st_size, "sha256": sha(HERE / rel)} for rel in sorted(component_paths)]
    external = []
    for rel in ["pilots/pretask-procedure-transfer-v4/posthoc-endpoint-audit.json", "pilots/pretask-procedure-transfer-v4/freeze-manifest.json", "pilots/pretask-procedure-transfer-v4/families/epsilon/corpus.json", "pilots/pretask-procedure-transfer-v4/families/zeta/corpus.json", "pilots/pretask-procedure-transfer-v4/candidate-freeze-manifest.json", "pilots/pretask-procedure-transfer-v4/hindsight-freeze-manifest.json"]:
        path = ROOT / rel; external.append({"path": rel, "bytes": path.stat().st_size, "sha256": sha(path)})
    dump(HERE / "freeze-manifest.json", {"manifest_version": "1.0.0", "study_id": "pretask-procedure-transfer-v5", "status": "frozen_zero_call", "components": components, "external_immutable_bindings": external, "attempt_ledger": protocol["attempt_ledger"], "executor_authorized": False, "claim_ceiling": CLAIMS})


if __name__ == "__main__":
    main()

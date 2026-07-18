#!/usr/bin/env python3
"""Independent v7 source-semantics oracle.

This module imports neither the builder, checker, nor preflight. It interprets the
v7 applicability record and public task inputs directly. Reason prose is a
non-scored witness and is normalized by callers.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent


def derive_epsilon(task_id: str, case: dict[str, Any]) -> dict[str, Any]:
    rank = {"signed_scan": 2, "unsigned_note": 1}
    decisions = []
    for batch in case["batches"]:
        supplied = [row for row in case["observations"] if row["batch_id"] == batch["batch_id"]]
        controlling: dict[str, str] = {}
        release = True
        for seal in batch["required_seals"]:
            # E-P2 says authority applies only inside the valid-time window.
            eligible = [
                row for row in supplied
                if row["seal"] == seal and 0 <= case["review_hour"] - row["hour"] <= 24
            ]
            highest = max((rank.get(row["record_type"], -1) for row in eligible), default=-1)
            peers = [row for row in eligible if rank.get(row["record_type"], -1) == highest]
            if not peers or len({row["state"] for row in peers}) != 1:
                release = False
                continue
            chosen = max(peers, key=lambda row: (row["hour"], row["observation_id"]))
            controlling[seal] = chosen["observation_id"]
            if chosen["state"] != "intact":
                release = False
        decisions.append({
            "batch_id": batch["batch_id"],
            "controlling_seals": controlling,
            "disposition": "release" if release else "quarantine",
            "observation_ids": [row["observation_id"] for row in supplied],
            "reason": "independent source-rule derivation",
        })
    return {"task_id": task_id, "decisions": decisions}


def derive_zeta(task_id: str, case: dict[str, Any]) -> dict[str, Any]:
    events = sorted(case["events"], key=lambda row: row["seq"])
    stack: list[str] = []
    mutations: dict[str, dict[str, Any]] = {}
    committed: list[str] = []
    rolled_back: list[str] = []
    seen_transactions: set[str] = set()
    valid = len({row["seq"] for row in events}) == len(events)

    for event in events if valid else []:
        operation = event["operation"]
        transaction = event.get("transaction")
        if operation == "begin":
            # A transaction identifier names one transaction in a journal.
            if not isinstance(transaction, str) or transaction in seen_transactions:
                valid = False
                break
            seen_transactions.add(transaction)
            stack.append(transaction)
            mutations[transaction] = {}
        elif operation == "set":
            if not stack or not isinstance(event.get("key"), str):
                valid = False
                break
            mutations[stack[-1]][event["key"]] = event.get("value")
        elif operation == "commit":
            # Z-P2 requires every ancestor to commit, so closing an ancestor while
            # descendants remain open is unmatched/invalid rather than implicit commit.
            if not stack or stack[-1] != transaction:
                valid = False
                break
            current = stack.pop()
            if stack:
                mutations[stack[-1]].update(mutations.pop(current))
            committed.append(current)
        elif operation == "rollback":
            if transaction not in stack:
                valid = False
                break
            target_index = stack.index(transaction)
            # V7 applicability clarification: innermost descendant outward, then target.
            discarded = list(reversed(stack[target_index:]))
            for name in discarded:
                mutations.pop(name, None)
            rolled_back.extend(discarded)
            del stack[target_index:]
        else:
            valid = False
            break

    valid = valid and not stack
    final_state: dict[str, Any] | None = None
    if valid:
        final_state = {}
        for transaction in committed:
            if transaction in mutations:
                final_state.update(mutations[transaction])
    return {
        "task_id": task_id,
        "journal_id": case["journal_id"],
        "valid": valid,
        "final_state": final_state,
        "committed_transactions": committed,
        "rolled_back_transactions": rolled_back,
        "reason": "independent source-rule derivation",
    }


def derive(task_id: str, case: dict[str, Any]) -> dict[str, Any]:
    if case["family_id"] == "family-epsilon":
        return derive_epsilon(task_id, case)
    if case["family_id"] == "family-zeta":
        return derive_zeta(task_id, case)
    raise ValueError("unknown family")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--task-id", required=True)
    parser.add_argument("--input", type=Path)
    args = parser.parse_args()
    path = args.input or HERE / "tasks" / args.task_id / "input.json"
    print(json.dumps(derive(args.task_id, json.loads(path.read_text())), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

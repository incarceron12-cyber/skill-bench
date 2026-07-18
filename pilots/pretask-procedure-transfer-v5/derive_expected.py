#!/usr/bin/env python3
"""Recompute v5 expected semantics from public task inputs and frozen source-rule implementations."""
from __future__ import annotations
import argparse, importlib.util, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("v5_prepare", HERE / "prepare_freeze.py")
assert _spec and _spec.loader
prepare = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(prepare)

def derive(task_id: str) -> dict:
    case = json.loads((HERE / "tasks" / task_id / "input.json").read_text())
    return prepare.expected(task_id, case)

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--task-id", choices=sorted(prepare.CASES))
    parser.add_argument("--verify-all", action="store_true")
    args = parser.parse_args()
    task_ids = sorted(prepare.CASES) if args.verify_all else [args.task_id]
    if task_ids == [None]: parser.error("provide --task-id or --verify-all")
    errors = []
    for task_id in task_ids:
        actual = derive(task_id)
        frozen = json.loads((HERE / "tasks" / task_id / "private.json").read_text())["expected_semantics"]
        if actual != frozen: errors.append(task_id)
    print(json.dumps({"status": "PASS" if not errors else "FAIL", "verified_tasks": task_ids, "mismatches": errors}, sort_keys=True))
    return 1 if errors else 0

if __name__ == "__main__": raise SystemExit(main())

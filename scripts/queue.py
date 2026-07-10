#!/usr/bin/env python3
"""Small durable work queue for skill-bench cron workers."""
from __future__ import annotations

import argparse
import datetime as dt
import fcntl
import json
import os
import tempfile
import uuid
from contextlib import contextmanager
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUEUE_PATH = ROOT / "data" / "work_queue.json"
LOCK_PATH = ROOT / "data" / ".work_queue.lock"
VALID_TYPES = {"source", "extract", "review", "research", "build", "consolidate", "ask_user"}
VALID_STATUSES = {"pending", "claimed", "completed", "blocked", "cancelled"}


def now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat()


def load_queue() -> dict:
    if not QUEUE_PATH.exists():
        return {"version": 1, "tasks": []}
    data = json.loads(QUEUE_PATH.read_text())
    validate_data(data)
    return data


def save_queue(data: dict) -> None:
    validate_data(data)
    QUEUE_PATH.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=".work_queue.", suffix=".json", dir=QUEUE_PATH.parent)
    try:
        with os.fdopen(fd, "w") as f:
            json.dump(data, f, indent=2, sort_keys=True)
            f.write("\n")
        os.replace(tmp, QUEUE_PATH)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


@contextmanager
def locked_queue():
    LOCK_PATH.parent.mkdir(parents=True, exist_ok=True)
    with LOCK_PATH.open("a+") as lock:
        fcntl.flock(lock.fileno(), fcntl.LOCK_EX)
        data = load_queue()
        yield data
        save_queue(data)
        fcntl.flock(lock.fileno(), fcntl.LOCK_UN)


def validate_data(data: dict) -> None:
    if data.get("version") != 1 or not isinstance(data.get("tasks"), list):
        raise ValueError("queue must contain version=1 and a tasks list")
    ids = set()
    for task in data["tasks"]:
        required = {"id", "type", "title", "priority", "status", "created_at", "rationale", "next_action"}
        missing = required - set(task)
        if missing:
            raise ValueError(f"task missing fields {sorted(missing)}: {task}")
        if task["id"] in ids:
            raise ValueError(f"duplicate task id: {task['id']}")
        ids.add(task["id"])
        if task["type"] not in VALID_TYPES:
            raise ValueError(f"invalid task type: {task['type']}")
        if task["status"] not in VALID_STATUSES:
            raise ValueError(f"invalid task status: {task['status']}")
        if not isinstance(task["priority"], int) or not 0 <= task["priority"] <= 100:
            raise ValueError("priority must be an integer from 0 to 100")


def command_add(args) -> None:
    with locked_queue() as data:
        task = {
            "id": args.id or f"task-{uuid.uuid4().hex[:10]}",
            "type": args.type,
            "title": args.title,
            "priority": args.priority,
            "status": "pending",
            "created_at": now(),
            "updated_at": now(),
            "rationale": args.rationale,
            "next_action": args.next_action,
            "source": args.source or "",
            "claimed_by": "",
            "claimed_at": "",
            "completed_at": "",
            "result": "",
        }
        data["tasks"].append(task)
        print(json.dumps(task, indent=2))


def command_list(args) -> None:
    data = load_queue()
    tasks = data["tasks"]
    if args.status:
        tasks = [t for t in tasks if t["status"] == args.status]
    if args.type:
        tasks = [t for t in tasks if t["type"] == args.type]
    tasks.sort(key=lambda t: (-t["priority"], t["created_at"]))
    print(json.dumps(tasks[: args.limit], indent=2))


def command_claim(args) -> None:
    with locked_queue() as data:
        candidates = [t for t in data["tasks"] if t["status"] == "pending"]
        if args.type:
            candidates = [t for t in candidates if t["type"] == args.type]
        candidates.sort(key=lambda t: (-t["priority"], t["created_at"]))
        if not candidates:
            print("null")
            return
        task = candidates[0]
        task.update({"status": "claimed", "claimed_by": args.worker, "claimed_at": now(), "updated_at": now()})
        print(json.dumps(task, indent=2))


def find_task(data: dict, task_id: str) -> dict:
    for task in data["tasks"]:
        if task["id"] == task_id:
            return task
    raise ValueError(f"task not found: {task_id}")


def command_complete(args) -> None:
    with locked_queue() as data:
        task = find_task(data, args.id)
        task.update({"status": "completed", "completed_at": now(), "updated_at": now(), "result": args.result})
        print(json.dumps(task, indent=2))


def command_block(args) -> None:
    with locked_queue() as data:
        task = find_task(data, args.id)
        task.update({"status": "blocked", "updated_at": now(), "result": args.reason})
        print(json.dumps(task, indent=2))


def command_release(args) -> None:
    with locked_queue() as data:
        task = find_task(data, args.id)
        task.update({"status": "pending", "claimed_by": "", "claimed_at": "", "updated_at": now(), "result": args.reason})
        print(json.dumps(task, indent=2))


def command_stats(_args) -> None:
    data = load_queue()
    stats = {status: 0 for status in sorted(VALID_STATUSES)}
    by_type = {kind: 0 for kind in sorted(VALID_TYPES)}
    for task in data["tasks"]:
        stats[task["status"]] += 1
        by_type[task["type"]] += 1
    print(json.dumps({"total": len(data["tasks"]), "by_status": stats, "by_type": by_type}, indent=2))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("add")
    p.add_argument("--id")
    p.add_argument("--type", required=True, choices=sorted(VALID_TYPES))
    p.add_argument("--title", required=True)
    p.add_argument("--priority", type=int, default=50)
    p.add_argument("--rationale", required=True)
    p.add_argument("--next-action", required=True)
    p.add_argument("--source")
    p.set_defaults(func=command_add)

    p = sub.add_parser("list")
    p.add_argument("--status", choices=sorted(VALID_STATUSES))
    p.add_argument("--type", choices=sorted(VALID_TYPES))
    p.add_argument("--limit", type=int, default=50)
    p.set_defaults(func=command_list)

    p = sub.add_parser("claim")
    p.add_argument("--type", choices=sorted(VALID_TYPES))
    p.add_argument("--worker", required=True)
    p.set_defaults(func=command_claim)

    p = sub.add_parser("complete")
    p.add_argument("id")
    p.add_argument("--result", required=True)
    p.set_defaults(func=command_complete)

    p = sub.add_parser("block")
    p.add_argument("id")
    p.add_argument("--reason", required=True)
    p.set_defaults(func=command_block)

    p = sub.add_parser("release")
    p.add_argument("id")
    p.add_argument("--reason", default="released for another worker")
    p.set_defaults(func=command_release)

    p = sub.add_parser("stats")
    p.set_defaults(func=command_stats)

    p = sub.add_parser("validate")
    p.set_defaults(func=lambda _args: (validate_data(load_queue()), print("VALID")))
    return parser


def main() -> int:
    args = build_parser().parse_args()
    args.func(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

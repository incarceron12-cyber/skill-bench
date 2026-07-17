#!/usr/bin/env python3
"""Lazy, no-retry campaign controller for the prospective replacement instrument."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Callable, Iterable

HERE = Path(__file__).resolve().parent
STOP_STATUSES = {"service_invalid", "environment_invalid", "outer_orchestrator_timeout", "interrupted"}
VALID_RESULTS = {"completed_valid", *STOP_STATUSES}


def _unlaunched(row_id: str) -> dict[str, Any]:
    return {"row_id": row_id, "intention_to_evaluate": 1, "materialized": False,
            "launcher_invocations": 0, "service_valid": None, "environment_valid": None,
            "substantively_graded": False, "invalidity": "not_launched_due_stop",
            "status": "not_launched_due_stop"}


def run_campaign(intended_rows: Iterable[dict[str, Any]], launch: Callable[[dict[str, Any]], dict[str, Any]]) -> dict[str, Any]:
    """Materialize exactly one row at a time and finalize the complete frozen ITT frame.

    `intended_rows` is the frozen protocol frame, not trial materialization. `launch`
    performs materialization and exactly one invocation. Once a stop result returns,
    launch is never called again. There is deliberately no retry API.
    """
    intentions = list(intended_rows)
    ids = [row["row_id"] for row in intentions]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate intended row")
    rows: list[dict[str, Any]] = []
    stopped = False
    for intention in intentions:
        row_id = intention["row_id"]
        if stopped:
            rows.append(_unlaunched(row_id))
            continue
        try:
            result = launch(intention)
            status = result["status"]
            if status not in VALID_RESULTS:
                raise ValueError(f"invalid launch status:{status}")
        except TimeoutError:
            result, status = {}, "outer_orchestrator_timeout"
        except KeyboardInterrupt:
            result, status = {}, "interrupted"
        service = result.get("service_valid", status not in {"service_invalid", "outer_orchestrator_timeout", "interrupted"})
        environment = result.get("environment_valid", status != "environment_invalid")
        substantive = status == "completed_valid" and service is True and environment is True
        rows.append({"row_id": row_id, "intention_to_evaluate": 1, "materialized": True,
                     "launcher_invocations": 1, "service_valid": service, "environment_valid": environment,
                     "substantively_graded": substantive, "invalidity": None if substantive else status,
                     "status": status})
        stopped = status in STOP_STATUSES or not service or not environment
    return {"strict_denominator": len(ids), "retries": 0,
            "intended_rows": [{"row_id": row_id} for row_id in ids], "rows": rows}


def synthetic_campaign(statuses: list[str], row_count: int = 4) -> dict[str, Any]:
    calls: list[str] = []
    iterator = iter(statuses)
    def launch(row: dict[str, Any]) -> dict[str, Any]:
        calls.append(row["row_id"])
        status = next(iterator)
        if status == "raise_timeout":
            raise TimeoutError
        if status == "raise_interrupt":
            raise KeyboardInterrupt
        return {"status": status}
    campaign = run_campaign(({"row_id": f"row-{i}"} for i in range(1, row_count + 1)), launch)
    campaign["launch_order"] = calls
    return campaign


def main() -> int:
    report = {
        "kind": "action_boundary_replacement_zero_call_campaign_conformance",
        "model_calls": 0,
        "cases": {
            "normal_completion": synthetic_campaign(["completed_valid"] * 4),
            "service_failure": synthetic_campaign(["completed_valid", "service_invalid"]),
            "environment_failure": synthetic_campaign(["environment_invalid"]),
            "timeout": synthetic_campaign(["completed_valid", "raise_timeout"]),
            "interruption": synthetic_campaign(["raise_interrupt"]),
        },
    }
    (HERE / "synthetic-campaign-report.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"model_calls": 0, "cases": list(report["cases"])}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

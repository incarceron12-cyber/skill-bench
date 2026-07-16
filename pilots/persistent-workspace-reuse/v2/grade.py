#!/usr/bin/env python3
"""Deterministic endpoint grader for persistent-workspace reuse v2."""
from __future__ import annotations
import json
from pathlib import Path
from typing import Any


def grade(path: Path, form: dict[str, Any]) -> dict[str, Any]:
    try:
        artifact = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return {"classification": "fail", "criteria": {"valid_json": False}, "error": type(exc).__name__}
    expected = form["expected_output"]
    criteria = {
        "valid_json": True,
        "artifact_type": artifact.get("artifact_type") == expected["artifact_type"],
        "form_identity": artifact.get("form_id") == form["form_id"],
        "substantive_result": artifact.get("result") == expected["result"],
        "collateral_preservation": artifact.get("preserved") == expected["preserved"],
    }
    return {"classification": "pass" if all(criteria.values()) else "fail", "criteria": criteria}


def calibration(form: dict[str, Any]) -> dict[str, Any]:
    import tempfile
    canonical = form["expected_output"]
    cases = {
        "canonical": (canonical, "pass"),
        "wrong_result": ({**canonical, "result": "planted-wrong"}, "fail"),
        "collateral_loss": ({**canonical, "preserved": "planted-wrong"}, "fail"),
        "wrong_form": ({**canonical, "form_id": "other"}, "fail"),
    }
    observed = {}
    with tempfile.TemporaryDirectory() as td:
        path = Path(td) / "artifact.json"
        for name, (value, _) in cases.items():
            path.write_text(json.dumps(value), encoding="utf-8")
            observed[name] = grade(path, form)["classification"]
        path.write_text("not json", encoding="utf-8")
        observed["invalid_json"] = grade(path, form)["classification"]
    wanted = {name: wanted for name, (_, wanted) in cases.items()} | {"invalid_json": "fail"}
    return {"passed": observed == wanted, "observed": observed, "wanted": wanted}

#!/usr/bin/env python3
"""Deterministic fair-basis grader for repeated task-family matrix v2."""
from __future__ import annotations

import json
from pathlib import Path

KEYS = {"decision", "action", "evidence_ids", "rationale"}


def grade(output: Path, expected: dict) -> dict:
    observations = []
    try:
        value = json.loads(output.read_text(encoding="utf-8"))
        valid = (
            isinstance(value, dict)
            and set(value) == KEYS
            and isinstance(value.get("decision"), str)
            and isinstance(value.get("action"), str)
            and isinstance(value.get("evidence_ids"), list)
            and all(isinstance(item, str) for item in value.get("evidence_ids", []))
            and isinstance(value.get("rationale"), str)
        )
    except (OSError, json.JSONDecodeError):
        value = {}
        valid = False

    rationale = value.get("rationale", "").lower() if valid else ""
    checks = [
        ("artifact_valid", "critical", valid, "report parses with the four publicly disclosed keys and types"),
        ("decision", "critical", valid and value.get("decision") in expected["accepted_decisions"], "decision is one of the publicly disclosed equivalents for the controlling record"),
        ("action", expected["severity"], valid and value.get("action") in expected["accepted_actions"], "action is one of the publicly disclosed bounded equivalents"),
        ("evidence", "major", valid and value.get("evidence_ids") == expected["evidence_ids"], "evidence IDs contain exactly the publicly identifiable controlling record"),
        ("conflict_rationale", "minor", valid and any(term in rationale for term in ("lower-rank", "outdated", "advisory", "scope", "controlling")), "rationale states a disclosed reason for excluding the conflicting record"),
    ]
    for criterion_id, severity, passed, reason in checks:
        observations.append({"criterion_id": criterion_id, "severity": severity, "passed": bool(passed), "reason": reason})
    critical_failure = any(not item["passed"] and item["severity"] == "critical" for item in observations)
    return {
        "classification": "pass" if all(item["passed"] for item in observations) else "fail",
        "critical_failure": critical_failure,
        "passed_criteria": sum(item["passed"] for item in observations),
        "total_criteria": len(observations),
        "observations": observations,
    }


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("output")
    parser.add_argument("expected")
    args = parser.parse_args()
    expected = json.loads(Path(args.expected).read_text(encoding="utf-8"))
    print(json.dumps(grade(Path(args.output), expected), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

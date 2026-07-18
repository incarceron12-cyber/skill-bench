#!/usr/bin/env python3
"""Condition-blind, closed-contract v7 endpoint checker."""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any, cast

EPSILON_TOP = {"task_id", "decisions"}
EPSILON_ROW = {"batch_id", "disposition", "reason", "controlling_seals", "observation_ids"}
ZETA_TOP = {"task_id", "journal_id", "valid", "final_state", "committed_transactions", "rolled_back_transactions", "reason"}


class DuplicateKey(ValueError):
    pass


def _closed_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKey(key)
        result[key] = value
    return result


def loads_strict(text: str) -> Any:
    """Parse RFC-style JSON while rejecting repeated keys and non-finite numbers."""
    def bad_constant(value: str) -> None:
        raise ValueError(f"non-finite number: {value}")
    return json.loads(text, object_pairs_hook=_closed_pairs, parse_constant=bad_constant)


def json_equal(left: Any, right: Any) -> bool:
    """Recursive exact JSON comparison under v7's numeric policy.

    Booleans never equal numbers. Integer-form values (Python int after JSON decode)
    are distinct from decimal/exponent-form values (float), including 1 versus 1.0.
    Non-finite floats are invalid. Objects are key-order invariant; arrays are ordered.
    """
    if type(left) is not type(right):
        return False
    if left is None or isinstance(left, (str, bool, int)):
        return left == right
    if isinstance(left, float):
        return math.isfinite(left) and math.isfinite(right) and left == right
    if isinstance(left, list):
        return len(left) == len(right) and all(json_equal(a, b) for a, b in zip(left, right))
    if isinstance(left, dict):
        return set(left) == set(right) and all(json_equal(left[key], right[key]) for key in left)
    return False


def _strings(value: Any) -> bool:
    return isinstance(value, list) and all(type(item) is str for item in value)


def compare(candidate: Any, private: dict[str, Any]) -> tuple[bool, list[str]]:
    expected = private["expected_semantics"]
    errors: list[str] = []
    if type(candidate) is not dict:
        return False, ["artifact_not_object"]
    family = private["family_id"]
    required = EPSILON_TOP if family == "family-epsilon" else ZETA_TOP
    if set(candidate) != required:
        errors.append("top_level_keys")
    if type(candidate.get("task_id")) is not str or candidate.get("task_id") != expected["task_id"]:
        errors.append("task_id")

    if family == "family-epsilon":
        decisions = candidate.get("decisions")
        if type(decisions) is not list:
            return False, errors + ["decisions_type"]
        if any(type(row) is not dict or set(row) != EPSILON_ROW for row in decisions):
            errors.append("decision_row_keys")
        valid_rows = [row for row in decisions if type(row) is dict]
        by_id = {row.get("batch_id"): row for row in valid_rows if type(row.get("batch_id")) is str}
        wanted = {row["batch_id"]: row for row in expected["decisions"]}
        if len(valid_rows) != len(wanted) or len(by_id) != len(wanted) or set(by_id) != set(wanted):
            errors.append("batch_ids")
        for batch_id, want in wanted.items():
            got = by_id.get(batch_id, {})
            if type(got.get("disposition")) is not str or got.get("disposition") != want["disposition"]:
                errors.append(f"{batch_id}:disposition")
            reason = got.get("reason")
            if type(reason) is not str or not reason.strip():
                errors.append(f"{batch_id}:reason")
            controls = got.get("controlling_seals")
            if type(controls) is not dict or not all(type(k) is str and type(v) is str for k, v in controls.items()) or not json_equal(controls, want["controlling_seals"]):
                errors.append(f"{batch_id}:controlling_seals")
            observed = got.get("observation_ids")
            if not _strings(observed):
                errors.append(f"{batch_id}:observation_ids")
            else:
                observed_strings = cast(list[str], observed)
                if len(observed_strings) != len(set(observed_strings)) or set(observed_strings) != set(want["observation_ids"]):
                    errors.append(f"{batch_id}:observation_ids")
    else:
        reason = candidate.get("reason")
        if type(reason) is not str or not reason.strip():
            errors.append("reason")
        if type(candidate.get("journal_id")) is not str or candidate.get("journal_id") != expected["journal_id"]:
            errors.append("journal_id")
        if type(candidate.get("valid")) is not bool or not json_equal(candidate.get("valid"), expected["valid"]):
            errors.append("valid")
        if not json_equal(candidate.get("final_state"), expected["final_state"]):
            errors.append("final_state")
        for field in ("committed_transactions", "rolled_back_transactions"):
            if not _strings(candidate.get(field)) or not json_equal(candidate.get(field), expected[field]):
                errors.append(field)
    return not errors, errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidate", type=Path, required=True)
    parser.add_argument("--private", type=Path, required=True)
    args = parser.parse_args()
    try:
        candidate = loads_strict(args.candidate.read_text(encoding="utf-8"))
        private = loads_strict(args.private.read_text(encoding="utf-8"))
        passed, errors = compare(candidate, private)
    except (OSError, json.JSONDecodeError, DuplicateKey, ValueError, KeyError, TypeError) as exc:
        passed, errors = False, ["invalid_or_missing_artifact:" + type(exc).__name__]
    print(json.dumps({"passed": passed, "errors": errors}, sort_keys=True))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())

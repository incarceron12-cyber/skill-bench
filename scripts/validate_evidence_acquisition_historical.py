#!/usr/bin/env python3
"""Validate evidence-acquisition packages with historical contract resolution.

The original validator remains byte-frozen for retained studies. This current
entry point preserves its structural and semantic behavior while resolving the
one legacy task-health path/hash reference through an immutable Git snapshot and
bounded live semantics.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.validate_evidence_acquisition import (
    DEFAULT_SCHEMA,
    ValidationFailure,
    semantic_errors,
    validate_file as validate_base_file,
)
from scripts.validate_provenance_boundary import validate_historical_contract_reference


TASK_HEALTH_PATH = "schemas/task-health.schema.json"
TASK_HEALTH_BOUNDARY = ROOT / "schemas" / "task-health-v0.1-provenance-boundary.json"
TASK_HEALTH_ROLE = "task_health_identifier_contract"


def validate_file(
    package_path: Path,
    schema_path: Path = DEFAULT_SCHEMA,
    check_paths: bool = False,
) -> None:
    """Run frozen package checks, then resolve current/historical path provenance."""
    validate_base_file(package_path, schema_path, check_paths=False)
    if not check_paths:
        return

    package = json.loads(package_path.read_text(encoding="utf-8"))
    errors: list[str] = []
    for item in package.get("provenance", []):
        if item["path"] == TASK_HEALTH_PATH:
            report = validate_historical_contract_reference(
                item,
                TASK_HEALTH_BOUNDARY,
                expected_path=TASK_HEALTH_PATH,
                expected_role=TASK_HEALTH_ROLE,
            )
            errors.extend(report["errors"])
            continue
        path = ROOT / item["path"]
        if not path.is_file():
            errors.append(f"missing provenance path: {item['path']}")
        elif hashlib.sha256(path.read_bytes()).hexdigest() != item["sha256"]:
            errors.append(f"provenance hash mismatch: {item['path']}")
    if errors:
        raise ValidationFailure("\n".join(f"- {error}" for error in errors))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("packages", nargs="+", type=Path)
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    parser.add_argument("--check-paths", action="store_true")
    args = parser.parse_args()
    failed = False
    for package_path in args.packages:
        try:
            validate_file(package_path, args.schema, args.check_paths)
            print(f"VALID {package_path}")
        except (OSError, ValueError, json.JSONDecodeError, ValidationFailure) as exc:
            failed = True
            print(f"INVALID {package_path}\n{exc}", file=sys.stderr)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())

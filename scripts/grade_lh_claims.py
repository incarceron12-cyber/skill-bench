#!/usr/bin/env python3
"""Calibrate two private LH-pilot claim checks against planted artifacts.

This deterministic convention is an internal test instrument, not an expert
judge. It checks whether cited evidence groups are jointly represented and
whether the memo preserves explicit source-derived claim boundaries. Alternative
professional phrasings and the thresholds themselves still require expert
calibration before release.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = ROOT / "pilots/lh-skill-adoption/graders/independent-claim-rubric.json"
CITATION_GROUP_RE = re.compile(r"\[(E\d{2}(?:\s*,\s*E\d{2})*)\]")
EVIDENCE_ID_RE = re.compile(r"E\d{2}")


@dataclass(frozen=True)
class Diagnostic:
    code: str
    message: str

    def render(self) -> str:
        return f"{self.code} | recommendation | {self.message}"


def _matrix_ids(path: Path) -> tuple[set[str], list[Diagnostic]]:
    try:
        with path.open(newline="", encoding="utf-8-sig") as handle:
            reader = csv.DictReader(handle)
            if "evidence_id" not in (reader.fieldnames or []):
                return set(), [Diagnostic("MALFORMED_ARTIFACT", "evidence matrix lacks evidence_id")]
            return {(row.get("evidence_id") or "").strip() for row in reader}, []
    except (OSError, UnicodeError, csv.Error) as exc:
        return set(), [Diagnostic("MALFORMED_ARTIFACT", str(exc))]


def _citation_ids(text: str) -> set[str]:
    """Extract IDs from both singular and comma-grouped bracket citations."""
    return {
        evidence_id
        for group in CITATION_GROUP_RE.findall(text)
        for evidence_id in EVIDENCE_ID_RE.findall(group)
    }


def _result(check_id: str, diagnostics: list[Diagnostic]) -> dict[str, object]:
    failed = bool(diagnostics)
    result: dict[str, object] = {
        "check_id": check_id,
        "grader_id": "independent-claim-calibrator",
        "outcome": "failed" if failed else "passed",
        "score": 0 if failed else 1,
        "rationale": (
            "Internal claim-boundary convention failed; inspect coded evidence."
            if failed
            else "Internal claim-boundary convention passed; expert validity remains unestablished."
        ),
        "evidence": [item.render() for item in diagnostics] or [
            "PASS | required counterevidence and source-derived claim boundaries are represented"
        ],
    }
    if failed:
        result.update({
            "root_cause": "evidence_reconciliation_failure",
            "root_event_id": "recommendation-write",
            "surfaced_at_event_id": "private-claim-verification",
            "causal_slice_event_ids": ["recommendation-write", "private-claim-verification"],
        })
    return result


def grade(config_path: Path, matrix_path: Path, memo_path: Path) -> list[dict[str, object]]:
    config = json.loads(config_path.read_text(encoding="utf-8"))
    matrix_ids, common = _matrix_ids(matrix_path)
    try:
        memo = memo_path.read_text(encoding="utf-8").lower()
    except (OSError, UnicodeError) as exc:
        memo = ""
        common.append(Diagnostic("MALFORMED_ARTIFACT", str(exc)))
    cited_ids = _citation_ids(memo.upper())
    available_ids = matrix_ids & cited_ids

    contradiction = list(common)
    rules = config["checks"]["contradiction-reconciliation"]
    for group_name, group in rules["required_evidence_groups"].items():
        if not available_ids.intersection(group):
            contradiction.append(Diagnostic("MISSING_COUNTEREVIDENCE_GROUP", group_name))
    for concept, patterns in rules["required_concepts"].items():
        if not any(re.search(pattern, memo) for pattern in patterns):
            contradiction.append(Diagnostic("MISSING_RECONCILIATION_CONCEPT", concept))
    if any(re.search(pattern, memo) for pattern in rules["prohibited_claim_patterns"]):
        contradiction.append(Diagnostic("AGREEMENT_AS_VALIDITY", "agreement is promoted to professional validity"))

    causal = list(common)
    rules = config["checks"]["causal-claim-strength"]
    salient = available_ids.intersection(rules["salient_effect_ids"])
    if salient and rules["scope_anchor_id"] not in available_ids:
        causal.append(Diagnostic("MISSING_CAUSAL_SCOPE_ANCHOR", f"{sorted(salient)} require {rules['scope_anchor_id']}"))
    if salient:
        for concept, patterns in rules["required_concepts"].items():
            if not any(re.search(pattern, memo) for pattern in patterns):
                causal.append(Diagnostic("MISSING_CAUSAL_BOUNDARY", concept))
        if any(re.search(pattern, memo) for pattern in rules["prohibited_claim_patterns"]):
            causal.append(Diagnostic("CAUSAL_OVERCLAIM", "directional configured-system evidence is generalized"))

    return [
        _result("contradiction-reconciliation", contradiction),
        _result("causal-claim-strength", causal),
    ]


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--matrix", type=Path, required=True)
    parser.add_argument("--memo", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    results = grade(args.config, args.matrix, args.memo)
    rendered = json.dumps({"results": results}, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0 if all(item["outcome"] == "passed" for item in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())

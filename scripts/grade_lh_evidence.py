#!/usr/bin/env python3
"""Deterministically grade the LH adoption pilot's evidence links.

This intentionally narrow grader verifies inspectable provenance properties; it
does not claim semantic entailment or professional validity. An evidence-matrix
row must preserve the source table's authority, scope, and caveat verbatim.
Material numeric memo lines must cite bracketed evidence IDs whose source values
contain the same numeric tokens. The strict convention makes planted overclaim
failures deterministic while leaving broader judgment to human checks.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = ROOT / "pilots/lh-skill-adoption/source-pack/decision-evidence.csv"
REQUIRED_MATRIX_COLUMNS = ("claim", "evidence_id", "authority", "scope", "caveat", "decision_use")
SOURCE_FIELDS = ("authority", "scope", "caveat")
CITATION_RE = re.compile(r"\[(E\d{2})\]")
NUMBER_RE = re.compile(r"(?<![A-Za-z])(?:[+≥>]=?)?\d+(?:\.\d+)?%?")


@dataclass(frozen=True)
class Diagnostic:
    code: str
    location: str
    message: str

    def render(self) -> str:
        return f"{self.code} | {self.location} | {self.message}"


def _read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), [dict(row) for row in reader]


def _numbers(text: str) -> set[str]:
    return {token.replace("%", "") for token in NUMBER_RE.findall(text)}


def _load_sources(path: Path) -> tuple[dict[str, dict[str, str]], list[Diagnostic]]:
    diagnostics: list[Diagnostic] = []
    try:
        fields, rows = _read_csv(path)
    except (OSError, UnicodeError, csv.Error) as exc:
        return {}, [Diagnostic("MALFORMED_SOURCE", str(path), str(exc))]
    required = {"evidence_id", "reported_value", *SOURCE_FIELDS}
    missing = sorted(required - set(fields))
    if missing:
        diagnostics.append(Diagnostic("MALFORMED_SOURCE", str(path), f"missing columns: {', '.join(missing)}"))
        return {}, diagnostics
    indexed: dict[str, dict[str, str]] = {}
    for row_number, row in enumerate(rows, start=2):
        evidence_id = (row.get("evidence_id") or "").strip()
        if not re.fullmatch(r"E\d{2}", evidence_id):
            diagnostics.append(Diagnostic("MALFORMED_SOURCE", f"source row {row_number}", f"invalid evidence_id {evidence_id!r}"))
        elif evidence_id in indexed:
            diagnostics.append(Diagnostic("MALFORMED_SOURCE", f"source row {row_number}", f"duplicate evidence_id {evidence_id}"))
        else:
            indexed[evidence_id] = {key: (value or "").strip() for key, value in row.items()}
    return indexed, diagnostics


def grade(source_path: Path, matrix_path: Path, memo_path: Path) -> dict[str, object]:
    sources, diagnostics = _load_sources(source_path)
    try:
        fields, rows = _read_csv(matrix_path)
    except (OSError, UnicodeError, csv.Error) as exc:
        fields, rows = [], []
        diagnostics.append(Diagnostic("MALFORMED_ARTIFACT", str(matrix_path), str(exc)))

    for column in REQUIRED_MATRIX_COLUMNS:
        if column not in fields:
            diagnostics.append(Diagnostic("MISSING_COLUMN", str(matrix_path), column))

    cited_matrix_ids: set[str] = set()
    if set(REQUIRED_MATRIX_COLUMNS) <= set(fields):
        for row_number, row in enumerate(rows, start=2):
            location = f"evidence-matrix row {row_number}"
            for column in REQUIRED_MATRIX_COLUMNS:
                if not (row.get(column) or "").strip():
                    diagnostics.append(Diagnostic("EMPTY_REQUIRED_VALUE", location, column))
            evidence_id = (row.get("evidence_id") or "").strip()
            source = sources.get(evidence_id)
            if source is None:
                diagnostics.append(Diagnostic("UNKNOWN_EVIDENCE_ID", location, evidence_id or "<empty>"))
                continue
            cited_matrix_ids.add(evidence_id)
            for field in SOURCE_FIELDS:
                actual = (row.get(field) or "").strip()
                if actual != source[field]:
                    diagnostics.append(Diagnostic("VALUE_SCOPE_MISMATCH", location, f"{field} differs from {evidence_id}"))
            unsupported = _numbers((row.get("claim") or "") + " " + (row.get("decision_use") or "")) - _numbers(source["reported_value"])
            if unsupported:
                diagnostics.append(Diagnostic("UNSUPPORTED_NUMERIC_VALUE", location, f"{sorted(unsupported)} absent from {evidence_id} reported_value"))

    try:
        memo_lines = memo_path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeError) as exc:
        memo_lines = []
        diagnostics.append(Diagnostic("MALFORMED_ARTIFACT", str(memo_path), str(exc)))

    for line_number, line in enumerate(memo_lines, start=1):
        citation_ids = set(CITATION_RE.findall(line))
        numbers = _numbers(CITATION_RE.sub("", line))
        if not numbers:
            continue
        location = f"recommendation line {line_number}"
        if not citation_ids:
            diagnostics.append(Diagnostic("UNCITED_MATERIAL_CLAIM", location, f"numeric tokens {sorted(numbers)} have no [E##] citation"))
            continue
        unknown = citation_ids - set(sources)
        for evidence_id in sorted(unknown):
            diagnostics.append(Diagnostic("UNKNOWN_EVIDENCE_ID", location, evidence_id))
        available_numbers = set().union(*(_numbers(sources[eid]["reported_value"]) for eid in citation_ids if eid in sources))
        unsupported = numbers - available_numbers
        if unsupported:
            diagnostics.append(Diagnostic("UNSUPPORTED_NUMERIC_VALUE", location, f"{sorted(unsupported)} absent from cited source values"))
        uncrosswalked = citation_ids - cited_matrix_ids
        for evidence_id in sorted(uncrosswalked):
            diagnostics.append(Diagnostic("MEMO_MATRIX_DISCONNECT", location, f"{evidence_id} is absent from evidence matrix"))

    failed = bool(diagnostics)
    evidence: list[str] = [item.render() for item in diagnostics]
    if not evidence:
        evidence = [
            f"PASS | {len(rows)} matrix rows preserve source authority/scope/caveat",
            "PASS | all numeric memo lines resolve through matrix rows to source reported values",
        ]
    result: dict[str, object] = {
        "check_id": "evidence-provenance",
        "grader_id": "evidence-link-grader",
        "outcome": "failed" if failed else "passed",
        "score": 0 if failed else 1,
        "rationale": "Deterministic provenance convention failed; inspect coded evidence." if failed else "Deterministic provenance convention passed. This does not establish semantic entailment or professional validity.",
        "evidence": evidence,
    }
    if failed:
        result.update({
            "root_cause": "artifact_structure_failure",
            "root_event_id": "evidence-matrix-write",
            "surfaced_at_event_id": "evidence-grader-verification",
            "causal_slice_event_ids": ["evidence-matrix-write", "evidence-grader-verification"],
        })
    return result


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--matrix", type=Path, required=True)
    parser.add_argument("--memo", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    result = grade(args.source, args.matrix, args.memo)
    rendered = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0 if result["outcome"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Grade LH provenance contract v2 without changing the legacy v0.2 grader."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Iterable

from scripts.grade_lh_evidence import (
    CITATION_GROUP_RE, Diagnostic, EVIDENCE_ID_RE, REQUIRED_MATRIX_COLUMNS,
    SOURCE_FIELDS, _citation_ids, _load_sources, _numbers, _read_csv,
)

ROOT = Path(__file__).resolve().parents[1]
PILOT = ROOT / "pilots/lh-skill-adoption"
DEFAULT_SOURCE = PILOT / "source-pack/decision-evidence.csv"
CONTRACT = PILOT / "provenance-v2/public-artifact-contract-v2.md"
CONFIG = PILOT / "graders/evidence-link-grader-v2.json"
GRADER_VERSION = "1.0.0"
CONTRACT_VERSION = "2.0.0"
PROSPECTIVE_RE = re.compile(r"\{\{PROSPECTIVE:([^{}]+)\}\}")
MALFORMED_MARKER_RE = re.compile(r"\{\{PROSPECTIVE|PROSPECTIVE:")


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _split_numbers(text: str, location: str, diagnostics: list[Diagnostic]) -> set[str]:
    """Return provenance-testable numbers, abstaining only inside valid markers."""
    spans = list(PROSPECTIVE_RE.finditer(text))
    stripped = PROSPECTIVE_RE.sub("", text)
    if MALFORMED_MARKER_RE.search(stripped):
        diagnostics.append(Diagnostic("MALFORMED_PROSPECTIVE_MARKER", location, "use exactly {{PROSPECTIVE:<program-set text containing a number>}}"))
    for match in spans:
        body = match.group(1).strip()
        if not body or not _numbers(body):
            diagnostics.append(Diagnostic("INVALID_PROSPECTIVE_MARKER", location, "marker must contain a program-set numeric value"))
    return _numbers(stripped)


def grade(source_path: Path, matrix_path: Path, memo_path: Path) -> dict[str, object]:
    sources, diagnostics = _load_sources(source_path)
    try:
        fields, rows = _read_csv(matrix_path)
    except Exception as exc:  # same fail-closed artifact boundary as legacy
        fields, rows = [], []
        diagnostics.append(Diagnostic("MALFORMED_ARTIFACT", str(matrix_path), str(exc)))
    for column in REQUIRED_MATRIX_COLUMNS:
        if column not in fields:
            diagnostics.append(Diagnostic("MISSING_COLUMN", str(matrix_path), column))

    cited_matrix_ids: set[str] = set()
    if set(REQUIRED_MATRIX_COLUMNS) <= set(fields):
        for row_number, row in enumerate(rows, 2):
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
                if (row.get(field) or "").strip() != source[field]:
                    diagnostics.append(Diagnostic("VALUE_SCOPE_MISMATCH", location, f"{field} differs from {evidence_id}"))
            testable = _split_numbers((row.get("claim") or "") + " " + (row.get("decision_use") or ""), location, diagnostics)
            unsupported = testable - _numbers(source["reported_value"] + " " + source["scope"])
            if unsupported:
                diagnostics.append(Diagnostic("UNSUPPORTED_NUMERIC_VALUE", location, f"{sorted(unsupported)} absent from {evidence_id} reported_value/scope"))

    try:
        memo_lines = memo_path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeError) as exc:
        memo_lines = []
        diagnostics.append(Diagnostic("MALFORMED_ARTIFACT", str(memo_path), str(exc)))
    abstentions = 0
    for line_number, line in enumerate(memo_lines, 1):
        location = f"recommendation line {line_number}"
        abstentions += len(PROSPECTIVE_RE.findall(line))
        citation_ids = _citation_ids(line)
        citation_free = CITATION_GROUP_RE.sub("", line)
        citation_free = re.sub(r"^\s*\d+[.)]\s+", "", citation_free)
        numbers = _split_numbers(citation_free, location, diagnostics)
        for evidence_id in sorted(citation_ids - set(sources)):
            diagnostics.append(Diagnostic("UNKNOWN_EVIDENCE_ID", location, evidence_id))
        for evidence_id in sorted(citation_ids - cited_matrix_ids):
            diagnostics.append(Diagnostic("MEMO_MATRIX_DISCONNECT", location, f"{evidence_id} is absent from evidence matrix"))
        if not numbers:
            continue
        if not citation_ids:
            diagnostics.append(Diagnostic("UNCITED_MATERIAL_CLAIM", location, f"numeric tokens {sorted(numbers)} have no [E##] citation"))
            continue
        available = set().union(*(_numbers(sources[e]["reported_value"] + " " + sources[e]["scope"]) for e in citation_ids if e in sources))
        unsupported = numbers - available
        if unsupported:
            diagnostics.append(Diagnostic("UNSUPPORTED_NUMERIC_VALUE", location, f"{sorted(unsupported)} absent from cited source values/scope"))

    failed = bool(diagnostics)
    evidence = [d.render() for d in diagnostics] or [
        f"PASS | {len(rows)} matrix rows preserve source authority/scope/caveat",
        f"PASS | numeric provenance resolved; value-check abstained on {abstentions} explicit prospective marker(s)",
    ]
    result: dict[str, object] = {
        "check_id": "evidence-provenance-v2", "grader_id": "evidence-link-grader-v2",
        "outcome": "failed" if failed else "passed", "score": 0 if failed else 1,
        "rationale": "V2 deterministic provenance convention failed; inspect coded evidence." if failed else "V2 provenance convention passed; marked prospective values were not source-value checked. This does not establish semantic entailment or professional validity.",
        "evidence": evidence,
        "instrument": {"grader_version": GRADER_VERSION, "contract_version": CONTRACT_VERSION,
                       "grader_config_sha256": _sha(CONFIG), "public_contract_sha256": _sha(CONTRACT)},
        "abstention_count": abstentions,
    }
    if failed:
        result.update({"root_cause": "artifact_or_contract_conformance_failure", "root_event_id": "evidence-matrix-write", "surfaced_at_event_id": "evidence-grader-verification", "causal_slice_event_ids": ["evidence-matrix-write", "evidence-grader-verification"]})
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
        args.output.parent.mkdir(parents=True, exist_ok=True); args.output.write_text(rendered, encoding="utf-8")
    else: print(rendered, end="")
    return 0 if result["outcome"] == "passed" else 1

if __name__ == "__main__": raise SystemExit(main())

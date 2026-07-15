#!/usr/bin/env python3
"""Generate byte-pinned synthetic temporal evidence views.

Rendered windows are authored independently from native graphs in CASES.  The
validator compares observations; it never derives one evidence view from the
other.  Re-running this file deterministically rewrites only this v0.2 package.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SHA256_ZERO = "0" * 64
TARGET = [100, 110]


def event(start=100, end=110, track="video-main", component="title-card"):
    return {"component_id": component, "track_id": track, "interval": [start, end], "appearance": "title-visible"}


CASES = {
    "exact-pass": {"native": {"editable": True, "events": [event()]}, "render": {"events": [event()]}, "export": "valid", "expected": ["pass", "pass", "pass", "pass"]},
    "just-inside-tolerance": {"native": {"editable": True, "events": [event(101, 111)]}, "render": {"events": [event(101, 111)]}, "export": "valid", "expected": ["pass", "pass", "pass", "pass"]},
    "just-outside-tolerance": {"native": {"editable": True, "events": [event(102, 112)]}, "render": {"events": [event(102, 112)]}, "export": "valid", "expected": ["pass", "fail", "fail", "pass"]},
    "right-appearance-wrong-interval": {"native": {"editable": True, "events": [event(140, 150)]}, "render": {"events": [event(140, 150)]}, "export": "valid", "expected": ["pass", "fail", "fail", "pass"]},
    "wrong-track-component": {"native": {"editable": True, "events": [event(track="audio-bed", component="subtitle")], "preserved": False}, "render": {"events": [event(track="audio-bed", component="subtitle")]}, "export": "valid", "expected": ["pass", "fail", "fail", "pass"]},
    "missing-source-view": {"source": None, "native": {"editable": True, "events": [event()]}, "render": {"events": [event()]}, "export": "valid", "expected": ["insufficient_evidence", "pass", "pass", "pass"]},
    "missing-native-view": {"native": None, "render": {"events": [event()]}, "export": "valid", "expected": ["pass", "insufficient_evidence", "pass", "pass"]},
    "missing-render-view": {"native": {"editable": True, "events": [event()]}, "render": None, "export": "valid", "expected": ["pass", "pass", "insufficient_evidence", "pass"]},
    "plausible-render-broken-editability": {"native": {"editable": False, "events": [event()]}, "render": {"events": [event()]}, "export": "valid", "expected": ["pass", "invalid_artifact", "pass", "pass"]},
    "export-hash-mismatch": {"native": {"editable": True, "events": [event()]}, "render": {"events": [event()]}, "export": "mismatch", "expected": ["pass", "pass", "pass", "invalid_artifact"]},
    "legitimate-alternate-sequence": {"native": {"editable": True, "events": [event(100, 105), event(105, 110)], "sequence_id": "split-equivalent"}, "render": {"events": [event(100, 105), event(105, 110)], "sequence_id": "split-equivalent"}, "export": "valid", "expected": ["pass", "pass", "pass", "pass"]},
}


def canonical_bytes(value: dict) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True) + "\n").encode()


def write_json(relative: str, value: dict) -> str:
    path = HERE / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = canonical_bytes(value)
    path.write_bytes(payload)
    return hashlib.sha256(payload).hexdigest()


def main() -> None:
    source = {"asset_id": "synthetic-source-v1", "duration_frames": 300, "frame_rate": {"numerator": 30, "denominator": 1}, "rights": "builder-authored synthetic calibration"}
    source_hash = write_json("evidence/source.json", source)
    cases = []
    for case_id, spec in CASES.items():
        views = {}
        if spec.get("source", "present") is not None:
            views["source"] = {"path": "evidence/source.json", "sha256": source_hash}
        native = spec.get("native")
        if native is not None:
            value = {"artifact_id": case_id, "format": "editable-timeline-v1", "duration_frames": 300, "source_asset_id": "synthetic-source-v1", "preserved": native.get("preserved", True), **native}
            rel = f"evidence/{case_id}/native.json"
            views["native"] = {"path": rel, "sha256": write_json(rel, value)}
        render = spec.get("render")
        if render is not None:
            value = {"artifact_id": case_id, "observer": "independent-render-window-v1", "time_basis": "frame", **render}
            rel = f"evidence/{case_id}/render.json"
            views["render"] = {"path": rel, "sha256": write_json(rel, value)}
        export_mode = spec.get("export")
        if export_mode:
            export_rel = f"evidence/{case_id}/export.bin"
            export_bytes = f"synthetic-export:{case_id}\n".encode()
            export_path = HERE / export_rel
            export_path.parent.mkdir(parents=True, exist_ok=True)
            export_path.write_bytes(export_bytes)
            actual = hashlib.sha256(export_bytes).hexdigest()
            declared = SHA256_ZERO if export_mode == "mismatch" else actual
            metadata = {"artifact_id": case_id, "export_path": export_rel, "declared_sha256": declared, "container": "synthetic/bin", "decodable": True}
            rel = f"evidence/{case_id}/export-metadata.json"
            views["export"] = {"path": rel, "sha256": write_json(rel, metadata)}
        cases.append({"id": case_id, "views": views, "expected_observers": dict(zip(["source_lineage", "native_structure", "rendered_window", "export_identity"], spec["expected"]))})

    fixture = {
        "version": "0.2",
        "status": "internal_synthetic_conformance_only",
        "provenance": [
            {"local_path": "papers/agent-benchmarks/2026-07-15-cutverse-temporal-creative-artifact-validity.md", "locator": "pp. 5-8, 25-26; review lines 78-101, 201-222, 299-307", "evidence_status": "paper_and_review_evidence", "use": "separate synchronized trace, native state, rendered interval, and export observers"},
            {"local_path": "data/sources/releases/2605.19484v1-cutverse/provenance.json", "locator": "official_release.pinned_commit=8b40dc18e1385bf6a9710cd999b22e4c51d602c8", "evidence_status": "post_v1_release_identity_only", "use": "version-boundary provenance; not empirical benchmark evidence"},
            {"local_path": "pilots/artifact-transition-conformance/v0.2-temporal/generate_fixture.py", "locator": "CASES", "evidence_status": "project_adaptation", "use": "builder-authored planted conformance cases"}
        ],
        "contract": {
            "time_basis": {"unit": "frame", "frame_rate": {"numerator": 30, "denominator": 1}, "interval_semantics": "half_open"},
            "target": {"appearance": "title-visible", "interval": TARGET, "track_id": "video-main", "component_id": "title-card", "synchronization_tolerance_frames": 1},
            "lineage": ["synthetic-source-v1", "editable-timeline-v1", "independent-render-window-v1", "export-bytes"],
            "required_views": ["source", "native", "render", "export"],
            "permitted_invariances": ["split-equivalent"],
            "predicates": {"must_preserve": ["duration_frames=300", "source_asset_id=synthetic-source-v1"], "forbidden_change": ["preserved=false", "undeclared-track-or-component"]},
            "typed_outcomes": ["pass", "fail", "insufficient_evidence", "invalid_artifact"],
            "claim_boundary": {"creative_quality": False, "professional_validity": False, "expert_validity": False, "model_capability": False, "reliability": False, "production_fitness": False, "readiness": False}
        },
        "cases": cases
    }
    (HERE / "fixture.json").write_bytes(canonical_bytes(fixture))


if __name__ == "__main__":
    main()

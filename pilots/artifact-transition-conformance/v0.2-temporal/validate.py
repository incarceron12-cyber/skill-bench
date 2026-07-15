#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

OBSERVER_ORDER = ("source_lineage", "native_structure", "rendered_window", "export_identity")


def _load_view(root: Path, case_id: str, views: dict, name: str):
    ref = views.get(name)
    if ref is None:
        return None
    relative = Path(ref["path"])
    if relative.is_absolute() or ".." in relative.parts:
        raise ValueError(f"{case_id}/{name}: locator escapes package")
    path = root / relative
    if not path.is_file():
        raise ValueError(f"{case_id}/{name}: declared locator missing: {relative}")
    payload = path.read_bytes()
    actual = hashlib.sha256(payload).hexdigest()
    if actual != ref["sha256"]:
        raise ValueError(f"{case_id}/{name}: evidence hash mismatch")
    try:
        return json.loads(payload)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"{case_id}/{name}: invalid JSON evidence") from exc


def _events_conform(events: list, target: dict, permitted: set[str], sequence_id: str | None) -> tuple[bool, str]:
    if sequence_id is not None and sequence_id not in permitted:
        return False, "undeclared_sequence_invariance"
    if not events:
        return False, "target_event_absent"
    for item in events:
        if item.get("track_id") != target["track_id"] or item.get("component_id") != target["component_id"]:
            return False, "wrong_track_or_component"
        if item.get("appearance") != target["appearance"]:
            return False, "wrong_appearance"
    intervals = sorted(item["interval"] for item in events)
    for interval in intervals:
        if len(interval) != 2 or not all(isinstance(v, int) for v in interval) or interval[0] >= interval[1]:
            return False, "invalid_interval"
    for previous, current in zip(intervals, intervals[1:]):
        if previous[1] != current[0]:
            return False, "noncontiguous_sequence"
    observed = [intervals[0][0], intervals[-1][1]]
    tolerance = target["synchronization_tolerance_frames"]
    if max(abs(observed[0] - target["interval"][0]), abs(observed[1] - target["interval"][1])) > tolerance:
        return False, "outside_synchronization_tolerance"
    return True, "conforms"


def replay(data: dict, root: Path) -> dict:
    contract = data["contract"]
    if contract["time_basis"] != {"unit": "frame", "frame_rate": {"numerator": 30, "denominator": 1}, "interval_semantics": "half_open"}:
        raise ValueError("contract: unsupported or mutated time basis")
    target = contract["target"]
    if not isinstance(target["synchronization_tolerance_frames"], int) or target["synchronization_tolerance_frames"] < 0:
        raise ValueError("contract: invalid synchronization tolerance")
    permitted = set(contract["permitted_invariances"])
    if permitted != {"split-equivalent"}:
        raise ValueError("contract: permitted invariance drift")
    rows = []
    for case in data["cases"]:
        case_id = case["id"]
        views = case["views"]
        source = _load_view(root, case_id, views, "source")
        native = _load_view(root, case_id, views, "native")
        render = _load_view(root, case_id, views, "render")
        export = _load_view(root, case_id, views, "export")

        observations = {}
        observations["source_lineage"] = {"outcome": "insufficient_evidence", "reason": "source_view_missing"} if source is None else (
            {"outcome": "pass", "reason": "source_identity_and_time_basis_present"} if source.get("asset_id") == "synthetic-source-v1" and source.get("duration_frames") == 300 and source.get("frame_rate") == contract["time_basis"]["frame_rate"] else {"outcome": "invalid_artifact", "reason": "source_identity_or_time_basis_invalid"}
        )
        if native is None:
            observations["native_structure"] = {"outcome": "insufficient_evidence", "reason": "native_view_missing"}
        elif native.get("format") != "editable-timeline-v1" or native.get("editable") is not True:
            observations["native_structure"] = {"outcome": "invalid_artifact", "reason": "native_graph_not_editable"}
        elif native.get("duration_frames") != 300 or native.get("source_asset_id") != "synthetic-source-v1" or native.get("preserved") is not True:
            observations["native_structure"] = {"outcome": "fail", "reason": "must_preserve_or_forbidden_change_violation"}
        else:
            ok, reason = _events_conform(native.get("events", []), target, permitted, native.get("sequence_id"))
            observations["native_structure"] = {"outcome": "pass" if ok else "fail", "reason": reason}

        if render is None:
            observations["rendered_window"] = {"outcome": "insufficient_evidence", "reason": "render_view_missing"}
        elif render.get("observer") != "independent-render-window-v1" or render.get("time_basis") != "frame":
            observations["rendered_window"] = {"outcome": "invalid_artifact", "reason": "render_observer_or_time_basis_invalid"}
        else:
            ok, reason = _events_conform(render.get("events", []), target, permitted, render.get("sequence_id"))
            observations["rendered_window"] = {"outcome": "pass" if ok else "fail", "reason": reason}

        if export is None:
            observations["export_identity"] = {"outcome": "insufficient_evidence", "reason": "export_metadata_missing"}
        else:
            export_rel = Path(export["export_path"])
            if export_rel.is_absolute() or ".." in export_rel.parts or not (root / export_rel).is_file():
                observations["export_identity"] = {"outcome": "insufficient_evidence", "reason": "declared_export_bytes_missing"}
            else:
                actual = hashlib.sha256((root / export_rel).read_bytes()).hexdigest()
                valid = export.get("decodable") is True and actual == export.get("declared_sha256")
                observations["export_identity"] = {"outcome": "pass" if valid else "invalid_artifact", "reason": "bytes_match_and_decode" if valid else "declaration_or_decode_mismatch"}

        observed = {key: observations[key]["outcome"] for key in OBSERVER_ORDER}
        if observed != case["expected_observers"]:
            raise ValueError(f"{case_id}: expected {case['expected_observers']} but replayed {observed}")
        rows.append({"case_id": case_id, "observers": observations})
    return {"version": data["version"], "status": "passed", "cases_replayed": len(rows), "claim_boundary": contract["claim_boundary"], "results": rows}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("fixture", type=Path)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    fixture = args.fixture.resolve()
    report = replay(json.loads(fixture.read_text()), fixture.parent)
    text = json.dumps(report, indent=2) + "\n"
    if args.report:
        args.report.write_text(text)
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

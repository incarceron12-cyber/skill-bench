#!/usr/bin/env python3
"""Deterministic audit of the pinned OpenAI macro-evals release."""
from __future__ import annotations

import json
import statistics
import zipfile
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "repository/examples/partners/macro_evals_for_agentic_systems"
RESULTS = ROOT / "data/trace_results.jsonl"
LABELS = ROOT / "data/eval_labels.jsonl"
BUNDLES = ROOT / "data/trace_bundles.zip"


def rows(path: Path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def values(records, key):
    return Counter(str(r.get(key, "<missing>")) for r in records)


def main() -> None:
    results = rows(RESULTS)
    labels = rows(LABELS)
    backed = [r for r in results if r.get("run_id") and r.get("bundle_path")]
    errors = [r for r in results if not (r.get("run_id") and r.get("bundle_path"))]
    label_by_id = {str(r["run_id"]): r for r in labels}
    result_by_id = {str(r["run_id"]): r for r in backed}

    bundle_summary = []
    with zipfile.ZipFile(BUNDLES) as zf:
        members = [n for n in zf.namelist() if n.endswith(".json")]
        for name in members:
            bundle = json.loads(zf.read(name))
            run = bundle.get("run") or {}
            config = run.get("config") or {}
            summary = run.get("summary") or {}
            trace = bundle.get("trace") or {}
            meta_raw = trace.get("metadata_json") or "{}"
            try:
                meta = json.loads(meta_raw) if isinstance(meta_raw, str) else meta_raw
            except json.JSONDecodeError:
                meta = {}
            bundle_summary.append({
                "run_id": run.get("run_id"),
                "config_id": run.get("config_id"),
                "runtime_status": run.get("status"),
                "terminal_state": summary.get("terminal_state"),
                "validation_outcome": summary.get("validation_outcome"),
                "scenario_family": summary.get("scenario_family") or meta.get("scenario_family"),
                "agent_version_set": summary.get("agent_version_set") or meta.get("agent_version_set"),
                "orchestrator_mode": summary.get("orchestrator_mode") or meta.get("orchestrator_mode"),
                "span_count": len(bundle.get("spans") or []),
                "event_count": len(bundle.get("events") or []),
                "finding_count": len(summary.get("findings") or []),
            })

    failed_checks = Counter()
    score_vectors = Counter()
    pass_counts = Counter()
    rationales_missing = 0
    versions = Counter()
    for label in labels:
        pass_counts[str(label.get("promptfoo_pass"))] += 1
        failed_checks.update(label.get("promptfoo_failed_checks") or [])
        scores = label.get("promptfoo_check_scores") or {}
        score_vectors[tuple(sorted(scores.items()))] += 1
        rationales_missing += int(not bool(label.get("promptfoo_rationales")))
        for key in ("model", "provider", "promptfoo_version", "grader_version", "config_hash"):
            if key in label:
                versions[f"{key}={label[key]}"] += 1

    result_status_vs_label = Counter()
    scenario_vs_primary = Counter()
    for run_id, result in result_by_id.items():
        label = label_by_id.get(run_id, {})
        result_status_vs_label[(str(result.get("status")), str(label.get("promptfoo_pass")))] += 1
        scenario_vs_primary[(str(result.get("scenario_family")), str(label.get("promptfoo_primary_finding")))] += 1

    by_config = defaultdict(list)
    for record in bundle_summary:
        by_config[str(record["config_id"])].append(record)

    report = {
        "source_paths": [str(RESULTS), str(LABELS), str(BUNDLES)],
        "denominators": {
            "intended_results": len(results),
            "bundle_backed_results": len(backed),
            "runner_errors_without_bundle": len(errors),
            "saved_label_rows": len(labels),
            "zip_bundle_members": len(bundle_summary),
            "result_ids_equal_label_ids": set(result_by_id) == set(label_by_id),
            "result_ids_equal_bundle_ids": set(result_by_id) == {str(r["run_id"]) for r in bundle_summary},
        },
        "runner_errors": errors,
        "results_distributions": {
            "status": values(results, "status"),
            "scenario_family": values(results, "scenario_family"),
            "agent_version_set": values(results, "agent_version_set"),
            "orchestrator_mode": values(results, "orchestrator_mode"),
            "market_regime": values(results, "market_regime"),
        },
        "bundle_distributions": {
            "runtime_status": values(bundle_summary, "runtime_status"),
            "terminal_state": values(bundle_summary, "terminal_state"),
            "validation_outcome": values(bundle_summary, "validation_outcome"),
            "agent_version_set": values(bundle_summary, "agent_version_set"),
            "orchestrator_mode": values(bundle_summary, "orchestrator_mode"),
            "unique_config_ids": len(by_config),
            "config_replicate_counts": Counter(len(v) for v in by_config.values()),
            "span_count": {"min": min(r["span_count"] for r in bundle_summary), "median": statistics.median(r["span_count"] for r in bundle_summary), "max": max(r["span_count"] for r in bundle_summary)},
            "event_count": {"min": min(r["event_count"] for r in bundle_summary), "median": statistics.median(r["event_count"] for r in bundle_summary), "max": max(r["event_count"] for r in bundle_summary)},
        },
        "labels": {
            "pass": pass_counts,
            "failed_checks": failed_checks,
            "unique_score_vectors": len(score_vectors),
            "most_common_score_vectors": score_vectors.most_common(12),
            "rows_missing_rationales": rationales_missing,
            "version_fields_observed": versions,
            "keys": sorted({key for row in labels for key in row}),
        },
        "cross_tabs": {
            "result_status_vs_promptfoo_pass": {" | ".join(k): v for k, v in result_status_vs_label.items()},
            "scenario_vs_primary_finding_top30": [{"scenario": k[0], "finding": k[1], "count": v} for k, v in scenario_vs_primary.most_common(30)],
        },
    }
    print(json.dumps(report, indent=2, sort_keys=True, default=dict))


if __name__ == "__main__":
    main()

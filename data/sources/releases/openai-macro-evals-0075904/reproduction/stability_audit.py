#!/usr/bin/env python3
"""Reproduce the cookbook focus population and perturb its clustering instrument."""
from __future__ import annotations

import json
import os
import sys
from itertools import combinations
from pathlib import Path

import pandas as pd
from sklearn.metrics import adjusted_rand_score

ROOT = Path(os.environ["MACRO_RELEASE_ROOT"]).resolve()
sys.path.insert(0, str(ROOT / "helpers"))
from data_prep import add_public_label_columns, build_trace_documents, load_promptfoo_label_rows, normalize_bundle  # noqa: E402
from macro_eval_pipeline import run_macro_discovery  # noqa: E402


def jsonl(path: Path):
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def main() -> None:
    results = jsonl(ROOT / "data/trace_results.jsonl")
    bundle_dir = ROOT / "data/.macro_eval_cache/trace_bundles"
    normalized = []
    selected = [row for row in results if row.get("run_id") and row.get("bundle_path")]
    for idx, row in enumerate(selected, 1):
        path = bundle_dir / Path(row["bundle_path"]).name
        normalized.append(normalize_bundle(json.loads(path.read_text()), row, idx, path))
    traces = pd.DataFrame([row for row, _ in normalized])
    events = pd.DataFrame([event for _, event_rows in normalized for event in event_rows])
    events["ts"] = pd.to_datetime(events["ts"], utc=True, errors="coerce")
    events["ended_at"] = pd.to_datetime(events["ended_at"], utc=True, errors="coerce")
    events = events.sort_values(["trace_id", "sequence_index", "ts", "event_id"]).reset_index(drop=True)

    result_df = pd.DataFrame(results)
    for col in ["agent_version_set", "orchestrator_mode", "market_regime", "price_regime", "schedule_regime"]:
        lookup = result_df[["run_id", col]].dropna(subset=["run_id"]).drop_duplicates("run_id")
        traces = traces.merge(lookup, on="run_id", how="left", suffixes=("", "_result"))
        if f"{col}_result" in traces:
            traces[col] = traces[f"{col}_result"].combine_first(traces.get(col))
            traces = traces.drop(columns=f"{col}_result")

    # Exact notebook semantics, including running -> unknown -> selected as failure.
    outcome_map = {"completed": "successful_completion", "awaiting_review": "review_escalation", "blocked": "hard_failure", "failed": "hard_failure"}
    severity = {"successful_completion": ("low", 1.0), "review_escalation": ("medium", 2.0), "in_progress": ("medium", 1.5), "blocked": ("high", 2.5), "hard_failure": ("high", 3.0)}
    traces["outcome_group"] = traces["runtime_status"].map(outcome_map).fillna("unknown")
    traces["severity_label"] = traces["outcome_group"].map(lambda x: severity.get(x, ("medium", 2.0))[0])
    traces["severity_weight"] = traces["outcome_group"].map(lambda x: severity.get(x, ("medium", 2.0))[1])
    traces["has_failure"] = traces["outcome_group"].ne("successful_completion") | traces["validation_outcome"].fillna("passed").ne("passed") | traces["findings_count"].fillna(0).gt(0)
    traces["impact_score"] = traces["severity_weight"] * (1 + traces["findings_count"].fillna(0)) * (1 + traces["loop_count"].fillna(0) / 4)

    docs = build_trace_documents(traces, events)
    labeled = add_public_label_columns(traces.merge(docs, on="trace_id"), load_promptfoo_label_rows(ROOT / "data/eval_labels.jsonl"))
    labeled["promptfoo_failed"] = labeled["promptfoo_pass"].eq(False)
    focus = labeled[labeled["has_failure"] | labeled["promptfoo_failed"] | labeled["run_outcome"].isin(["review_needed", "blocked", "runtime_error"])].copy()

    population = {
        "bundle_backed": len(labeled),
        "focus": len(focus),
        "focus_by_runtime_status": focus["runtime_status"].fillna("missing").value_counts().to_dict(),
        "focus_by_outcome_group": focus["outcome_group"].fillna("missing").value_counts().to_dict(),
        "running_selected": int(focus["runtime_status"].eq("running").sum()),
        "running_without_findings_or_failed_label": int((focus["runtime_status"].eq("running") & focus["findings_count"].eq(0) & ~focus["promptfoo_failed"]).sum()),
    }

    runs = {}
    assignments = {}
    specs = [
        ("structured_seed42", "doc_structured_summary", 42, False),
        ("structured_seed13", "doc_structured_summary", 13, False),
        ("structured_seed99", "doc_structured_summary", 99, False),
        ("structured_seed42_shuffled", "doc_structured_summary", 42, True),
        ("failure_window_seed42", "doc_failure_window", 42, False),
        ("state_transition_seed42", "doc_state_transition_summary", 42, False),
    ]
    for name, doc_col, seed, shuffle in specs:
        source = focus.sample(frac=1, random_state=777).reset_index(drop=True) if shuffle else focus.copy()
        discovery = run_macro_discovery(source, document_column=doc_col, min_cluster_size=24, n_neighbors=30, top_n_terms=8, random_state=seed)
        frame = discovery.topic_assignments[["trace_id", "topic_id"]].copy()
        assignments[name] = frame.set_index("trace_id")["topic_id"]
        summary = discovery.topic_summary
        non_noise = summary[summary["topic_id"].ne(-1)]
        runs[name] = {
            "document": doc_col,
            "seed": seed,
            "shuffled": shuffle,
            "clusters_non_noise": int(len(non_noise)),
            "noise_traces": int(frame["topic_id"].eq(-1).sum()),
            "largest_clusters": non_noise.sort_values("trace_count", ascending=False)[["topic_id", "trace_count", "topic_label", "keywords_text"]].head(8).to_dict("records"),
        }

    agreement = []
    for left, right in combinations(assignments, 2):
        joined = pd.concat([assignments[left].rename("left"), assignments[right].rename("right")], axis=1).dropna()
        agreement.append({"left": left, "right": right, "adjusted_rand_index": adjusted_rand_score(joined["left"], joined["right"]), "n": len(joined)})

    print(json.dumps({"population": population, "runs": runs, "pairwise_agreement": agreement}, indent=2, default=str))


if __name__ == "__main__":
    main()

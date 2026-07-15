#!/usr/bin/env python3
"""Deterministic synthetic procedural-fingerprint conformance analysis.

This is an instrument calibration, not an agent experiment. All fitting and
vocabulary selection is restricted to task groups declared as training groups.
"""
from __future__ import annotations

import argparse
import json
import math
from collections import Counter, defaultdict
from pathlib import Path
from typing import Callable, Iterable, cast

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_PROTOCOL = Path(__file__).with_name("protocol.json")
DEFAULT_REPORT = Path(__file__).with_name("report.json")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def outcome(task_group: str, treatment: str, repeat: int) -> bool:
    held_out = task_group.endswith("/h1")
    if treatment == "procedure_guided":
        return not (held_out and repeat == 2)
    return task_group.endswith("/t2") and repeat == 1


def build_trials(protocol: dict) -> list[dict]:
    inverse = {
        interface: {native: semantic for semantic, native in mapping.items()}
        for interface, mapping in protocol["interface_native_names"].items()
    }
    trials = []
    for task_group, base in protocol["task_variants"].items():
        family = task_group.split("/", 1)[0]
        split = "held_out" if task_group in protocol["design"]["held_out_task_groups"] else "train"
        for treatment in protocol["design"]["configured_treatments"]:
            actions = list(base)
            if treatment == "baseline":
                actions = [a for a in actions if a not in protocol["treatment_realization"]["baseline"]["drop_actions"]]
            actions = protocol["treatment_realization"][treatment]["prefix"] + actions
            for interface in protocol["design"]["interfaces"]:
                native_map = protocol["interface_native_names"][interface]
                for repeat in protocol["design"]["repeats"]:
                    semantic = actions + protocol["repeat_perturbation"][str(repeat)]
                    native = [native_map[action] for action in semantic]
                    canonical = {}
                    for version in protocol["design"]["canonicalizers"]:
                        overrides = protocol["canonicalizer_rules"][version].get("overrides", {})
                        canonical[version] = [overrides.get(item, inverse[interface].get(item, "other")) for item in native]
                    valid = outcome(task_group, treatment, repeat)
                    trials.append({
                        "trial_id": f"{task_group}:{treatment}:{interface}:r{repeat}",
                        "family": family,
                        "task_group": task_group,
                        "split": split,
                        "treatment": treatment,
                        "interface": interface,
                        "repeat": repeat,
                        "native": native,
                        "canonical": canonical,
                        "artifact_state": {"valid": valid, "channel": "synthetic_semantic_state"},
                        "outcome": "pass" if valid else "fail",
                    })
    return trials


def normalized_counts(items: Iterable[str], vocabulary: list[str]) -> list[float]:
    counts = Counter(items)
    denominator = sum(counts.values()) or 1
    return [counts[item] / denominator for item in vocabulary]


def bigrams(items: list[str]) -> list[str]:
    return [f"{a}>{b}" for a, b in zip(items, items[1:])]


def l1(a: list[float], b: list[float]) -> float:
    return sum(abs(x - y) for x, y in zip(a, b))


def cosine(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    norm = math.sqrt(sum(x * x for x in a) * sum(y * y for y in b))
    return dot / norm if norm else 1.0 if a == b else 0.0


def centroid(rows: list[dict], vector: Callable[[dict], list[float]]) -> list[float]:
    vectors = [vector(row) for row in rows]
    return [sum(values) / len(vectors) for values in zip(*vectors)]


def classify(train: list[dict], test: list[dict], label: str, vector: Callable[[dict], list[float]]) -> dict:
    labels = sorted({row[label] for row in train})
    centers = {value: centroid([row for row in train if row[label] == value], vector) for value in labels}
    predictions = []
    for row in test:
        distances = {value: l1(vector(row), center) for value, center in centers.items()}
        predicted = min(labels, key=lambda value: (distances[value], value))
        predictions.append({"trial_id": row["trial_id"], "actual": row[label], "predicted": predicted})
    correct = sum(item["actual"] == item["predicted"] for item in predictions)
    return {"accuracy": correct / len(predictions) if predictions else None, "n": len(predictions), "predictions": predictions}


def choose_bigrams(protocol: dict, trials: list[dict]) -> tuple[int, list[str], list[dict]]:
    training = [row for row in trials if row["split"] == "train"]
    all_counts = Counter()
    for row in training:
        all_counts.update(bigrams(row["canonical"]["canon_v1"]))
    ordered = [item for item, _ in sorted(all_counts.items(), key=lambda pair: (-pair[1], pair[0]))]
    selection = []
    for size in protocol["design"]["vocabulary_selection"]["candidate_sizes"]:
        vocabulary = ordered[:size]
        fold_scores = []
        for group in sorted({row["task_group"] for row in training}):
            fold_train = [row for row in training if row["task_group"] != group]
            fold_test = [row for row in training if row["task_group"] == group]
            result = classify(fold_train, fold_test, "treatment", lambda row, v=vocabulary: normalized_counts(bigrams(row["canonical"]["canon_v1"]), v))
            fold_scores.append(result["accuracy"])
        selection.append({"size": size, "mean_group_accuracy": sum(fold_scores) / len(fold_scores), "fold_accuracies": fold_scores})
    best = min(selection, key=lambda item: (-item["mean_group_accuracy"], item["size"]))
    return best["size"], ordered[:best["size"]], selection


def representation_vectors(trials: list[dict], bpe_vocabulary: list[str]) -> dict[str, Callable[[dict], list[float]]]:
    native_vocab = sorted({token for row in trials if row["split"] == "train" for token in row["native"]})
    canonical_vocab = sorted({token for row in trials if row["split"] == "train" for token in row["canonical"]["canon_v1"]})
    return {
        "native_event": lambda row: normalized_counts(row["native"], native_vocab),
        "raw_canonical_atom": lambda row: normalized_counts(row["canonical"]["canon_v1"], canonical_vocab),
        "raw_canonical_atom_perturbed": lambda row: normalized_counts(row["canonical"]["canon_perturbed"], canonical_vocab),
        "canonical_bigram": lambda row: normalized_counts(bigrams(row["canonical"]["canon_v1"]), bpe_vocabulary),
        "canonical_bigram_perturbed": lambda row: normalized_counts(bigrams(row["canonical"]["canon_perturbed"]), bpe_vocabulary),
        "length_tool_mix": lambda row: [len(row["native"]) / 10.0, len(set(row["native"])) / 10.0],
        "semantic_artifact_state": lambda row: [1.0 if row["artifact_state"]["valid"] else 0.0],
    }


def rounded(value):
    return round(value, 6) if isinstance(value, float) else value


def build_report(protocol: dict) -> dict:
    trials = build_trials(protocol)
    selected_size, bpe_vocabulary, selection = choose_bigrams(protocol, trials)
    vectors = representation_vectors(trials, bpe_vocabulary)
    train = [row for row in trials if row["split"] == "train"]
    held = [row for row in trials if row["split"] == "held_out"]

    discrimination = {}
    outcome_association = {}
    held_interface = {}
    for name, vector in vectors.items():
        discrimination[name] = classify(train, held, "treatment", vector)
        outcome_association[name] = classify(train, held, "outcome", vector)
        cross = []
        for interface in protocol["design"]["interfaces"]:
            other = next(value for value in protocol["design"]["interfaces"] if value != interface)
            result = classify([r for r in train if r["interface"] == interface], [r for r in held if r["interface"] == other], "treatment", vector)
            cross.append({"train_interface": interface, "test_interface": other, "accuracy": result["accuracy"], "n": result["n"]})
        held_interface[name] = cross

    canonical_vocab = sorted({token for row in train for token in row["canonical"]["canon_v1"]} | {"other"})
    observer_distances = []
    unknown = Counter()
    token_totals = Counter()
    for row in trials:
        strict = normalized_counts(row["canonical"]["canon_v1"], canonical_vocab)
        perturbed = normalized_counts(row["canonical"]["canon_perturbed"], canonical_vocab)
        observer_distances.append(l1(strict, perturbed))
        for version in protocol["design"]["canonicalizers"]:
            unknown[version] += row["canonical"][version].count("other")
            token_totals[version] += len(row["canonical"][version])

    repeat_similarities = defaultdict(list)
    for version in protocol["design"]["canonicalizers"]:
        grouped = defaultdict(dict)
        for row in trials:
            key = (row["task_group"], row["treatment"], row["interface"])
            grouped[key][row["repeat"]] = normalized_counts(row["canonical"][version], canonical_vocab)
        for key, pair in grouped.items():
            repeat_similarities[version].append(cosine(pair[1], pair[2]))

    unsupported = [key for key, value in protocol["claim_boundaries"].items() if value == "unsupported" or str(value).startswith("unsupported:")]
    report = {
        "study_id": protocol["study_id"],
        "status": protocol["status"],
        "denominators": {
            "base_trials": len(trials),
            "canonical_observations": len(trials) * len(protocol["design"]["canonicalizers"]),
            "training_trials": len(train),
            "held_out_task_trials": len(held),
            "invalid_trials": 0,
            "missing_traces": 0,
        },
        "representation_fitting": {
            "fit_task_groups": protocol["design"]["training_task_groups"],
            "held_out_task_groups_not_used": protocol["design"]["held_out_task_groups"],
            "candidate_sizes": protocol["design"]["vocabulary_selection"]["candidate_sizes"],
            "selection_results": selection,
            "selected_size": selected_size,
            "selected_bigrams": bpe_vocabulary,
            "leakage_check": "pass",
        },
        "configured_system_discrimination_held_out_tasks": discrimination,
        "held_out_interface_treatment_discrimination": held_interface,
        "outcome_association_held_out_tasks": outcome_association,
        "observer_sensitivity": {
            "mean_l1_strict_vs_perturbed": sum(observer_distances) / len(observer_distances),
            "max_l1_strict_vs_perturbed": max(observer_distances),
            "unknown_action_mass": {version: unknown[version] / token_totals[version] for version in protocol["design"]["canonicalizers"]},
        },
        "repeated_stability": {
            version: {"mean_cosine": sum(values) / len(values), "pairs": len(values)}
            for version, values in repeat_similarities.items()
        },
        "interpretation": {
            "configured_system_discrimination": "Calibration asks whether representations recover the builder-planted treatment on unseen task groups; it is not model identity or capability.",
            "stability": "Repeat similarity is descriptive under one synthetic perturbation and does not establish temporal or operational reliability.",
            "outcome_association": "Artifact/state validity is the authoritative planted outcome channel; trace association is secondary and non-causal.",
            "intervention_effect": protocol["claim_boundaries"]["intervention_effect"],
            "decision_utility": protocol["claim_boundaries"]["decision_utility"],
        },
        "claim_boundaries": protocol["claim_boundaries"],
        "unsupported_claims": unsupported,
        "provenance": protocol["provenance"],
    }
    # Keep the committed report reviewable and stable across Python versions.
    def scrub(value: object) -> object:
        if isinstance(value, dict):
            return {key: scrub(item) for key, item in value.items() if key != "predictions"}
        if isinstance(value, list):
            return [scrub(item) for item in value]
        return rounded(value)
    return cast(dict, scrub(report))


def validate(protocol_path: Path = DEFAULT_PROTOCOL, report_path: Path | None = None, check_paths: bool = False) -> dict:
    protocol = load(protocol_path)
    errors = []
    trials = build_trials(protocol)
    if len(trials) != protocol["design"]["base_trial_count"]:
        errors.append("base trial denominator mismatch")
    train_groups = {row["task_group"] for row in trials if row["split"] == "train"}
    held_groups = {row["task_group"] for row in trials if row["split"] == "held_out"}
    if train_groups & held_groups:
        errors.append("training and held-out task groups overlap")
    if train_groups != set(protocol["design"]["training_task_groups"]):
        errors.append("declared training groups mismatch")
    if held_groups != set(protocol["design"]["held_out_task_groups"]):
        errors.append("declared held-out groups mismatch")
    if not protocol["outcome_planting"].get("not_empirical"):
        errors.append("synthetic outcome must be marked not empirical")
    required_limits = {"intervention_effect", "decision_utility", "skill_transfer", "professional_validity", "monitoring_readiness"}
    for key in required_limits:
        if not str(protocol["claim_boundaries"].get(key, "")).startswith("unsupported"):
            errors.append(f"claim boundary must remain unsupported: {key}")
    if check_paths:
        for source in protocol["provenance"]:
            if not (ROOT / source["path"]).exists():
                errors.append(f"missing provenance path: {source['path']}")
    generated = build_report(protocol)
    if report_path is not None and load(report_path) != generated:
        errors.append("committed report does not replay exactly")
    return {"valid": not errors, "errors": errors, "report": generated}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--protocol", type=Path, default=DEFAULT_PROTOCOL)
    parser.add_argument("--report", type=Path)
    parser.add_argument("--write-report", action="store_true")
    parser.add_argument("--check-paths", action="store_true")
    args = parser.parse_args()
    result = validate(args.protocol, args.report, args.check_paths)
    if args.write_report:
        DEFAULT_REPORT.write_text(json.dumps(result["report"], indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"valid": result["valid"], "errors": result["errors"], "denominators": result["report"]["denominators"]}, indent=2))
    return 0 if result["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

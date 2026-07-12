#!/usr/bin/env python3
"""Frozen domain-neutral candidate over typed provenance comparisons."""

def evaluate(observation):
    sufficiency = observation["sufficiency"]
    if sufficiency["environment"] == "invalid":
        return "invalid_artifact_or_environment"
    relations = {(item["predicate"], item["relation"]) for item in observation["comparisons"]}
    if ("authority", "contradicts") in relations or ("safety", "contradicts") in relations:
        return "unsafe_or_unauthorized"
    if sufficiency["evidence"] == "insufficient" or any(relation == "missing" for _, relation in relations):
        return "insufficient_evidence"
    if any(relation == "contradicts" for predicate, relation in relations if predicate not in {"authority", "safety"}):
        return "substantive_mismatch"
    return "passed"

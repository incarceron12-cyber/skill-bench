#!/usr/bin/env python3
"""Replay the frozen generated-workspace projection conformance suite.

This deterministic validator tests generator output, not agent capability or
professional validity. The frozen suite predates this implementation.
"""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
REQUIRED_PROJECTIONS = {
    "profile", "plan", "file_graph", "byte_tree", "objective", "authority", "evidence_status"
}
AFFECTED = {
    "none": set(),
    "profile_hash_drift": {"profile"},
    "dangling_endpoint": {"file_graph"},
    "stale_derived": {"byte_tree"},
    "impossible_objective": {"objective"},
    "semantic_drift": {"byte_tree"},
    "unsupported_professional_claim": {"profile"},
    "derivation_cycle": {"file_graph"},
    "valid_time_inversion": {"byte_tree"},
    "fallback_laundering": {"evidence_status"},
    "authority_overreach": {"authority"},
}
BOUNDARY = {
    "projection_hash_mismatch": "projection_identity",
    "graph_endpoint_missing": "plan_to_file_graph",
    "derivation_cycle": "file_graph_ordering",
    "stale_derived_artifact": "graph_to_bytes",
    "valid_time_inversion": "byte_tree_valid_time",
    "fallback_status_mismatch": "retrieval_to_evidence_status",
    "unsupported_professional_claim": "claim_to_external_authority",
    "objective_infeasible": "workspace_to_objective",
    "instruction_outside_authority": "collaborator_to_authority",
    "semantic_fidelity_failure": "source_to_derived_semantics",
}


def load() -> dict:
    return json.loads((HERE / "suite.json").read_text())


def digest(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def file_digest(file_record: dict) -> str:
    return digest({k: v for k, v in file_record.items() if k not in {"sha256", "source_hashes"}})


def refresh(world: dict, names: set[str]) -> None:
    for name in names:
        world["projections"][name]["sha256"] = digest(world["projections"][name]["value"])


def freeze_checks(suite: dict) -> None:
    if suite.get("status") != "frozen_builder_authored_generator_conformance_only":
        raise ValueError("suite is not frozen")
    if len({w["work_shape"] for w in suite["worlds"]}) < 2:
        raise ValueError("at least two knowledge-work shapes are required")
    if set(AFFECTED) != {c["mutation"]["kind"] for c in suite["cases"]}:
        raise ValueError("frozen mutation inventory is incomplete or unknown")
    for world in suite["worlds"]:
        projections = world["projections"]
        if set(projections) != REQUIRED_PROJECTIONS:
            raise ValueError("all seven independently hashed projections are required")
        for name, record in projections.items():
            if record["sha256"] != digest(record["value"]):
                raise ValueError(f"frozen {world['world_id']} {name} hash mismatch")
        for file_record in projections["byte_tree"]["value"]["files"]:
            if file_record["sha256"] != file_digest(file_record):
                raise ValueError(f"frozen file hash mismatch: {file_record['path']}")


def mutate(world: dict, kind: str) -> dict:
    candidate = copy.deepcopy(world)
    p = candidate["projections"]
    files = p["byte_tree"]["value"]["files"]
    source, derived = files[0], files[1]
    if kind == "none":
        return candidate
    if kind == "profile_hash_drift":
        p["profile"]["value"]["role"] += "-silently-edited"
        return candidate
    if kind == "dangling_endpoint":
        p["file_graph"]["value"]["edges"][0]["from"] = "sources/missing.file"
    elif kind == "stale_derived":
        source["valid_to"] = "2026-07-01"
        source["sha256"] = file_digest(source)
    elif kind == "impossible_objective":
        p["objective"]["value"]["required_facts"].append({"path": "sources/unavailable.csv", "key": "required_value"})
    elif kind == "semantic_drift":
        key = next(iter(derived["facts"]))
        derived["facts"][key] += 3
        derived["sha256"] = file_digest(derived)
    elif kind == "unsupported_professional_claim":
        p["profile"]["value"]["claims"][0]["professional_status"] = "professionally_supported"
    elif kind == "derivation_cycle":
        edge = p["file_graph"]["value"]["edges"][0]
        p["file_graph"]["value"]["edges"].append({"from": edge["to"], "to": edge["from"], "relation": "derived_from"})
    elif kind == "valid_time_inversion":
        derived["valid_from"], derived["valid_to"] = "2026-07-01", "2026-06-01"
        derived["sha256"] = file_digest(derived)
    elif kind == "fallback_laundering":
        evidence = p["evidence_status"]["value"]["evidence"][0]
        evidence.update({"actual_mode": "synthetic_fallback", "status": "retrieved_authoritative", "professional_claim_allowed": True})
    elif kind == "authority_overreach":
        p["authority"]["value"]["instructions"][0]["required_scope"] = "authorize_external_release"
    else:
        raise ValueError(f"unknown mutation: {kind}")
    refresh(candidate, AFFECTED[kind])
    return candidate


def has_cycle(nodes: set[str], edges: list[dict]) -> bool:
    graph = {n: [] for n in nodes}
    for edge in edges:
        if edge["from"] in graph and edge["to"] in graph:
            graph[edge["from"]].append(edge["to"])
    visiting: set[str] = set()
    visited: set[str] = set()
    def visit(node: str) -> bool:
        if node in visiting:
            return True
        if node in visited:
            return False
        visiting.add(node)
        if any(visit(child) for child in graph[node]):
            return True
        visiting.remove(node)
        visited.add(node)
        return False
    return any(visit(n) for n in nodes)


def inspect(world: dict) -> list[dict]:
    p = world["projections"]
    findings: list[dict] = []
    def add(code: str, detail: str) -> None:
        findings.append({"code": code, "boundary": BOUNDARY[code], "detail": detail})

    for name, record in p.items():
        if record["sha256"] != digest(record["value"]):
            add("projection_hash_mismatch", name)

    graph = p["file_graph"]["value"]
    nodes = set(graph["nodes"])
    for edge in graph["edges"]:
        if edge["from"] not in nodes or edge["to"] not in nodes:
            add("graph_endpoint_missing", f"{edge['from']} -> {edge['to']}")
            break
    if has_cycle(nodes, graph["edges"]):
        add("derivation_cycle", "derived_from graph is cyclic")

    files = {f["path"]: f for f in p["byte_tree"]["value"]["files"]}
    for file_record in files.values():
        if file_record["valid_from"] > file_record["valid_to"]:
            add("valid_time_inversion", file_record["path"])
        for source_path in file_record.get("derived_from", []):
            source = files.get(source_path)
            if source and file_record.get("source_hashes", {}).get(source_path) != source["sha256"]:
                add("stale_derived_artifact", file_record["path"])
            if source:
                for key, value in source["facts"].items():
                    if key in file_record["facts"] and file_record["facts"][key] != value:
                        add("semantic_fidelity_failure", f"{file_record['path']}:{key}")

    evidence = {e["evidence_id"]: e for e in p["evidence_status"]["value"]["evidence"]}
    for record in evidence.values():
        if record["actual_mode"] == "synthetic_fallback" and (record["status"] != "synthetic_hypothesis" or record["professional_claim_allowed"]):
            add("fallback_status_mismatch", record["evidence_id"])
    for claim in p["profile"]["value"]["claims"]:
        source = evidence.get(claim["evidence_id"])
        if claim["professional_status"] == "professionally_supported" and (not source or not source["professional_claim_allowed"]):
            add("unsupported_professional_claim", claim["claim_id"])

    for requirement in p["objective"]["value"]["required_facts"]:
        file_record = files.get(requirement["path"])
        if not file_record or requirement["key"] not in file_record["facts"]:
            add("objective_infeasible", f"{requirement['path']}:{requirement['key']}")
    actors = {a["actor_id"]: set(a["scopes"]) for a in p["authority"]["value"]["actors"]}
    for instruction in p["authority"]["value"]["instructions"]:
        if instruction["required_scope"] not in actors.get(instruction["actor_id"], set()):
            add("instruction_outside_authority", instruction["instruction_id"])
    return findings


def replay(suite: dict | None = None, write: bool = True) -> dict:
    suite = copy.deepcopy(suite or load())
    freeze_checks(suite)
    worlds = {w["world_id"]: w for w in suite["worlds"]}
    rows = []
    for case in suite["cases"]:
        baseline = worlds[case["world_id"]]
        kind = case["mutation"]["kind"]
        candidate = mutate(baseline, kind)
        findings = inspect(candidate)
        observed = sorted({f["code"] for f in findings})
        expected = sorted(case["expected_codes"])
        unaffected = REQUIRED_PROJECTIONS - AFFECTED[kind]
        preservation = all(
            candidate["projections"][name]["sha256"] == baseline["projections"][name]["sha256"]
            for name in unaffected
        )
        repaired = copy.deepcopy(baseline)
        repair_restored = not inspect(repaired) and all(
            repaired["projections"][name]["sha256"] == baseline["projections"][name]["sha256"]
            for name in REQUIRED_PROJECTIONS
        )
        rows.append({
            "case_id": case["case_id"], "world_id": case["world_id"], "work_shape": baseline["work_shape"],
            "mutation": kind, "expected_codes": expected, "observed_findings": findings,
            "localized_exactly": observed == expected, "unrelated_projection_hashes_preserved": preservation,
            "repair_restored_clean_baseline": repair_restored,
        })
    report = {
        "schema_version": "0.1.0", "status": "frozen_generated_workspace_projection_replay",
        "suite_sha256": digest(suite),
        "rows": rows,
        "summary": {
            "cases": len(rows), "clean_controls": sum(not r["expected_codes"] for r in rows),
            "defects": sum(bool(r["expected_codes"]) for r in rows),
            "exactly_localized": sum(r["localized_exactly"] for r in rows),
            "repairs_preserving_unrelated_state": sum(r["unrelated_projection_hashes_preserved"] and r["repair_restored_clean_baseline"] for r in rows),
            "work_shapes": sorted({r["work_shape"] for r in rows}),
        },
        "claim_ceiling": suite["claim_ceiling"], "excluded_claims": suite["excluded_claims"],
    }
    if write:
        (HERE / "report.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    return report


if __name__ == "__main__":
    print(json.dumps(replay(), indent=2, sort_keys=True))

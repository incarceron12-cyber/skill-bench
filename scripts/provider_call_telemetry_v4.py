#!/usr/bin/env python3
"""Provider-native coordinate telemetry with explicit availability semantics.

Versioned separately from provider_call_telemetry.py so retained v1-v3 evidence
and frozen hashes remain immutable.  Total input is retained as a native total;
cache-read and reasoning are typed subcomponents, never added to their parent.
An absent cache-write field is unavailable, not zero, and uncached input is not
derived.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import runpy
import sys
import time
from pathlib import Path
from types import SimpleNamespace
from typing import Any, Callable

COORDINATES = ("total_input_tokens", "cache_read_tokens", "output_tokens", "reasoning_tokens", "cache_write_tokens")
ALLOWED_PHASES = {"direct_observe_act", "skill_delivery_injection", "candidate_generation", "verification", "retrieval", "repair"}


def canonical_hash(value: Any) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def _int_attr(value: Any, name: str) -> int | None:
    raw = getattr(value, name, None)
    return raw if isinstance(raw, int) and raw >= 0 else None


def native_coordinates(response: Any, api_mode: str) -> dict[str, dict[str, Any]]:
    """Extract only emitted provider values; never estimate unavailable fields."""
    usage = getattr(response, "usage", None)
    if usage is None:
        return {key: {"status": "unavailable", "value": None, "source_field": None} for key in COORDINATES}
    if api_mode == "codex_responses":
        in_details = getattr(usage, "input_tokens_details", None)
        out_details = getattr(usage, "output_tokens_details", None)
        raw = {
            "total_input_tokens": (_int_attr(usage, "input_tokens"), "usage.input_tokens"),
            "cache_read_tokens": (_int_attr(in_details, "cached_tokens") if in_details is not None else None, "usage.input_tokens_details.cached_tokens"),
            "output_tokens": (_int_attr(usage, "output_tokens"), "usage.output_tokens"),
            "reasoning_tokens": (_int_attr(out_details, "reasoning_tokens") if out_details is not None else None, "usage.output_tokens_details.reasoning_tokens"),
            "cache_write_tokens": (_int_attr(in_details, "cache_creation_tokens") if in_details is not None else None, "usage.input_tokens_details.cache_creation_tokens"),
        }
    else:
        in_details = getattr(usage, "prompt_tokens_details", None)
        out_details = getattr(usage, "completion_tokens_details", None)
        raw = {
            "total_input_tokens": (_int_attr(usage, "prompt_tokens"), "usage.prompt_tokens"),
            "cache_read_tokens": (_int_attr(in_details, "cached_tokens") if in_details is not None else None, "usage.prompt_tokens_details.cached_tokens"),
            "output_tokens": (_int_attr(usage, "completion_tokens"), "usage.completion_tokens"),
            "reasoning_tokens": (_int_attr(out_details, "reasoning_tokens") if out_details is not None else None, "usage.completion_tokens_details.reasoning_tokens"),
            "cache_write_tokens": (_int_attr(in_details, "cache_write_tokens") if in_details is not None else None, "usage.prompt_tokens_details.cache_write_tokens"),
        }
    return {
        key: {"status": "supported" if value is not None else "unavailable", "value": value, "source_field": source if value is not None else None}
        for key, (value, source) in raw.items()
    }


def append_event(path: Path, event: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = dict(event)
    payload["event_sha256"] = canonical_hash(payload)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n")
        handle.flush()
        os.fsync(handle.fileno())


def make_wrapper(original: Callable[..., Any], *, event_path: Path, env: dict[str, str] | None = None) -> Callable[..., Any]:
    settings = os.environ if env is None else env
    phase = settings.get("SKILL_BENCH_CALL_PHASE", "")
    if phase not in ALLOWED_PHASES:
        raise ValueError(f"undeclared provider call phase: {phase!r}")
    attempt_id = settings["SKILL_BENCH_ATTEMPT_ID"]
    provider = settings["SKILL_BENCH_PROVIDER"]
    model = settings["SKILL_BENCH_MODEL"]
    configured_hash = settings["SKILL_BENCH_CONFIGURED_SYSTEM_SHA256"]
    contract_hash = settings["SKILL_BENCH_COORDINATE_CONTRACT_SHA256"]
    comparison_hash = settings["SKILL_BENCH_COMPARISON_IDENTITY_SHA256"]
    declaration_hash = canonical_hash({"attempt_id": attempt_id, "phase": phase, "call_site": "AIAgent._interruptible_api_call"})
    sequence = 0

    def wrapped(agent: Any, api_kwargs: dict[str, Any]) -> Any:
        nonlocal sequence
        sequence += 1
        started_ns = time.monotonic_ns()
        error: BaseException | None = None
        response: Any = None
        try:
            response = original(agent, api_kwargs)
            return response
        except BaseException as exc:
            error = exc
            raise
        finally:
            coordinates = native_coordinates(response, getattr(agent, "api_mode", ""))
            event = {
                "schema_version": "0.4.0", "kind": "native_provider_coordinate_call",
                "attempt_id": attempt_id, "sequence": sequence, "call_id": f"{attempt_id}:call:{sequence:04d}",
                "phase": phase, "phase_source": "launcher_declared_call_site", "phase_declaration_sha256": declaration_hash,
                "call_site": "AIAgent._interruptible_api_call", "provider": provider,
                "provider_sha256": hashlib.sha256(provider.encode()).hexdigest(), "model": model,
                "model_sha256": hashlib.sha256(model.encode()).hexdigest(),
                "configured_system_sha256": configured_hash, "coordinate_contract_sha256": contract_hash,
                "comparison_identity_sha256": comparison_hash,
                "wall_time_ms": max(0, (time.monotonic_ns() - started_ns) // 1_000_000),
                "coordinates": coordinates, "derivations": [], "imputations": [],
                "tool_linkage": {"preceding_tool_event_ids": [], "auxiliary_call": False},
                "error": None if error is None else {"type": type(error).__name__, "message_sha256": hashlib.sha256(str(error).encode()).hexdigest()},
                "invalidity": [] if error is None else ["provider_call_error"],
            }
            append_event(event_path, event)
    return wrapped


def install_from_environment() -> Path:
    event_path = Path(os.environ["SKILL_BENCH_CALL_EVENT_PATH"])
    if event_path.exists():
        raise FileExistsError(f"immutable event ledger already exists: {event_path}")
    from agent import chat_completion_helpers as helpers
    helpers.interruptible_api_call = make_wrapper(helpers.interruptible_api_call, event_path=event_path)
    return event_path


def run_hermes(arguments: list[str]) -> int:
    install_from_environment()
    sys.argv = ["hermes", *arguments]
    try:
        runpy.run_path("/opt/hermes/venv/bin/hermes", run_name="__main__")
    except SystemExit as exc:
        return int(exc.code or 0)
    return 0


def deterministic_stub(event_path: Path, *, attempt_id: str = "stub-attempt", configured_system_sha256: str = "0" * 64, contract_sha256: str = "1" * 64, comparison_sha256: str = "2" * 64) -> None:
    usage = SimpleNamespace(input_tokens=130, output_tokens=21, input_tokens_details=SimpleNamespace(cached_tokens=30), output_tokens_details=SimpleNamespace(reasoning_tokens=5))
    env = {"SKILL_BENCH_CALL_PHASE": "direct_observe_act", "SKILL_BENCH_ATTEMPT_ID": attempt_id, "SKILL_BENCH_PROVIDER": "stub-provider", "SKILL_BENCH_MODEL": "stub-model", "SKILL_BENCH_CONFIGURED_SYSTEM_SHA256": configured_system_sha256, "SKILL_BENCH_COORDINATE_CONTRACT_SHA256": contract_sha256, "SKILL_BENCH_COMPARISON_IDENTITY_SHA256": comparison_sha256}
    make_wrapper(lambda _agent, _kwargs: SimpleNamespace(usage=usage), event_path=event_path, env=env)(SimpleNamespace(api_mode="codex_responses"), {})


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="mode", required=True)
    run = sub.add_parser("run-hermes"); run.add_argument("args", nargs=argparse.REMAINDER)
    stub = sub.add_parser("stub-canary"); stub.add_argument("event_path", type=Path)
    args = parser.parse_args()
    if args.mode == "stub-canary":
        deterministic_stub(args.event_path); return 0
    forwarded = args.args[1:] if args.args and args.args[0] == "--" else args.args
    return run_hermes(forwarded)


if __name__ == "__main__":
    raise SystemExit(main())

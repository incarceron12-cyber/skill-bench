#!/usr/bin/env python3
"""Repository-owned, pre-aggregation provider-call telemetry adapter.

The adapter wraps Hermes' provider-call boundary without modifying the installed
Hermes package.  A call-site phase is supplied by the launcher, never inferred
from output text, token shares, or rubric labels.  Each completed or failed
native call is fsync-appended to JSONL before Hermes can aggregate its usage.
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

TOKEN_KEYS = ("prompt_tokens", "completion_tokens", "cache_read_tokens", "cache_write_tokens", "reasoning_tokens")
ALLOWED_PHASES = {
    "direct_observe_act", "skill_delivery_injection", "candidate_generation",
    "verification", "retrieval", "repair",
}


def canonical_hash(value: Any) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def _int_attr(value: Any, name: str) -> int | None:
    raw = getattr(value, name, None)
    return raw if isinstance(raw, int) and raw >= 0 else None


def native_usage(response: Any, api_mode: str) -> tuple[dict[str, int | None], dict[str, bool]]:
    """Extract provider-native coordinates without estimating missing values."""
    usage = getattr(response, "usage", None)
    if usage is None:
        return ({key: None for key in TOKEN_KEYS}, {key: False for key in TOKEN_KEYS})
    if api_mode == "codex_responses":
        total_input = _int_attr(usage, "input_tokens")
        details = getattr(usage, "input_tokens_details", None)
        cache_read = _int_attr(details, "cached_tokens") if details is not None else None
        cache_write = _int_attr(details, "cache_creation_tokens") if details is not None else None
        # The provider reports total input and cache detail.  Uncached prompt is
        # a documented exact subtraction, not a phase allocation or imputation.
        prompt = None if None in (total_input, cache_read, cache_write) else max(0, total_input - cache_read - cache_write)
        output = _int_attr(usage, "output_tokens")
        out_details = getattr(usage, "output_tokens_details", None)
        reasoning = _int_attr(out_details, "reasoning_tokens") if out_details is not None else None
    else:
        total_input = _int_attr(usage, "prompt_tokens")
        details = getattr(usage, "prompt_tokens_details", None)
        cache_read = _int_attr(details, "cached_tokens") if details is not None else None
        cache_write = _int_attr(details, "cache_write_tokens") if details is not None else None
        prompt = None if None in (total_input, cache_read, cache_write) else max(0, total_input - cache_read - cache_write)
        output = _int_attr(usage, "completion_tokens")
        out_details = getattr(usage, "completion_tokens_details", None)
        reasoning = _int_attr(out_details, "reasoning_tokens") if out_details is not None else None
    values = dict(zip(TOKEN_KEYS, (prompt, output, cache_read, cache_write, reasoning)))
    return values, {key: value is not None for key, value in values.items()}


def append_event(path: Path, event: dict[str, Any]) -> None:
    """Append one self-hashed event and force it to stable storage."""
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
            tokens, supported = native_usage(response, getattr(agent, "api_mode", ""))
            event = {
                "schema_version": "0.2.0", "kind": "native_provider_call",
                "attempt_id": attempt_id, "sequence": sequence,
                "call_id": f"{attempt_id}:call:{sequence:04d}",
                "phase": phase, "phase_source": "launcher_declared_call_site",
                "phase_declaration_sha256": declaration_hash,
                "call_site": "AIAgent._interruptible_api_call",
                "provider": provider, "provider_sha256": hashlib.sha256(provider.encode()).hexdigest(),
                "model": model, "model_sha256": hashlib.sha256(model.encode()).hexdigest(),
                "configured_system_sha256": configured_hash,
                "wall_time_ms": max(0, (time.monotonic_ns() - started_ns) // 1_000_000),
                "tokens": tokens, "token_coordinates_supported": supported,
                "tool_linkage": {"preceding_tool_event_ids": [], "auxiliary_call": False},
                "error": None if error is None else {"type": type(error).__name__, "message_sha256": hashlib.sha256(str(error).encode()).hexdigest()},
                "invalidity": [] if error is None and all(supported.values()) else (["provider_call_error"] if error is not None else ["unsupported_token_coordinate"]),
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


def deterministic_stub(event_path: Path, *, attempt_id: str = "stub-attempt", configured_system_sha256: str = "0" * 64) -> None:
    usage = SimpleNamespace(
        input_tokens=130, output_tokens=21,
        input_tokens_details=SimpleNamespace(cached_tokens=30, cache_creation_tokens=0),
        output_tokens_details=SimpleNamespace(reasoning_tokens=5),
    )
    response = SimpleNamespace(usage=usage)
    agent = SimpleNamespace(api_mode="codex_responses")
    env = {
        "SKILL_BENCH_CALL_PHASE": "direct_observe_act", "SKILL_BENCH_ATTEMPT_ID": attempt_id,
        "SKILL_BENCH_PROVIDER": "stub-provider", "SKILL_BENCH_MODEL": "stub-model",
        "SKILL_BENCH_CONFIGURED_SYSTEM_SHA256": configured_system_sha256,
    }
    wrapped = make_wrapper(lambda _agent, _kwargs: response, event_path=event_path, env=env)
    wrapped(agent, {})


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="mode", required=True)
    run = sub.add_parser("run-hermes")
    run.add_argument("args", nargs=argparse.REMAINDER)
    stub = sub.add_parser("stub-canary")
    stub.add_argument("event_path", type=Path)
    stub.add_argument("--attempt-id", default="stub-attempt")
    stub.add_argument("--configured-system-sha256", default="0" * 64)
    args = parser.parse_args()
    if args.mode == "stub-canary":
        deterministic_stub(
            args.event_path, attempt_id=args.attempt_id,
            configured_system_sha256=args.configured_system_sha256,
        )
        print(json.dumps({"event_path": str(args.event_path), "calls": 1}))
        return 0
    forwarded = args.args[1:] if args.args and args.args[0] == "--" else args.args
    return run_hermes(forwarded)


if __name__ == "__main__":
    raise SystemExit(main())

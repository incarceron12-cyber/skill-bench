# Prospective allocation telemetry

## v1

`v1/` froze the allocation envelope and proved a zero-call ledger, then failed closed because Hermes `--usage-file` exposed only aggregate session usage. No provider call or matched condition was executed.

## v2 repository-owned provider-call adapter

`v2/` adds `scripts/provider_call_telemetry.py`, a launcher adapter that wraps Hermes' `AIAgent._interruptible_api_call` boundary without modifying the installed Hermes package. The launcher declares the call-site phase before execution. On every return or error, the adapter fsync-appends a self-hashed JSONL event before Hermes can aggregate usage. Events preserve attempt/call identity, sequence, call-site phase and declaration hash, provider/model/configuration hashes, five provider-native token coordinates and support flags, wall time, tool/auxiliary linkage, and typed error/invalidity.

`validate_native_events` rejects omitted, duplicated, or reordered calls; phase spoofing; aggregate mismatch; unsupported coordinates; retry substitution; changed configured-system identity; and stale event hashes. The zero-call and deterministic one-call canaries pass, and the stub event exactly reconciles to its retained aggregate.

The retained `v2/readiness-report.json` remains fail-closed. Deterministic conformance is not configured-provider evidence. The exact frozen isolated trial command does not yet mount and invoke the adapter, so no native provider ledger exists to reconcile before authorizing the matched AB pair. Consequently no fresh provider call or pair was run.

### Replay

```bash
python scripts/validate_allocation_telemetry.py \
  pilots/prospective-allocation-telemetry/v2/manifest.json \
  --native-events pilots/prospective-allocation-telemetry/v2/stub-native-events.jsonl \
  --attempt-id alloc-v2-ab-no-skill \
  --aggregate-usage pilots/prospective-allocation-telemetry/v2/stub-aggregate-usage.json \
  --check-paths
python -m unittest tests.test_allocation_telemetry -v
```

This slice reports Skill presentation, invocation, adoption, artifact outcome, and resource allocation separately. It licenses no allocation/Skill effect, capability, cross-domain, expert/professional validity, safety, economic-value, production, or readiness claim.

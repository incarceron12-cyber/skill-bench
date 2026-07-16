# Prospective allocation telemetry

## v1

`v1/` froze the allocation envelope and proved a zero-call ledger, then failed closed because Hermes `--usage-file` exposed only aggregate session usage. No provider call or matched condition was executed.

## v2 repository-owned provider-call adapter

`v2/` adds `scripts/provider_call_telemetry.py`, a launcher adapter that wraps Hermes' `AIAgent._interruptible_api_call` boundary without modifying the installed Hermes package. The launcher declares the call-site phase before execution. On every return or error, the adapter fsync-appends a self-hashed JSONL event before Hermes can aggregate usage. Events preserve attempt/call identity, sequence, call-site phase and declaration hash, provider/model/configuration hashes, five provider-native token coordinates and support flags, wall time, tool/auxiliary linkage, and typed error/invalidity.

`validate_native_events` rejects omitted, duplicated, or reordered calls; phase spoofing; aggregate mismatch; unsupported coordinates; retry substitution; changed configured-system identity; and stale event hashes. The zero-call and deterministic one-call canaries pass, and the stub event exactly reconciles to its retained aggregate.

The retained `v2/readiness-report.json` remains fail-closed. Deterministic conformance is not configured-provider evidence. The exact frozen isolated trial command does not yet mount and invoke the adapter, so no native provider ledger exists to reconcile before authorizing the matched AB pair. Consequently no fresh provider call or pair was run.

## v3 configured-provider probe

`v3/` preserves v1/v2 and adds `scripts/allocation_provider_probe.py`, which read-only mounts the adapter into the same file-only, task-scoped bubblewrap envelope. One retained `openai-codex`/`gpt-5.6-sol` capture probe completed successfully at the service layer and reported included cost of USD 0.00. The adapter emitted one self-hashed native event before aggregation.

The probe nevertheless failed the frozen telemetry gate. The provider response exposed total input, output, cache-read, and reasoning usage but omitted a cache-write field. Under the predeclared policy, the adapter cannot assume an absent cache-write coordinate equals zero; without it, uncached prompt tokens also cannot be derived. The retained event therefore marks `prompt_tokens` and `cache_write_tokens` unsupported and does not reconcile to the aggregate five-coordinate ledger. `v3/readiness-report.json` forbids replay/replacement and leaves the AB pair unexecuted.

This is useful negative evidence: the hook is reached on a real provider call, but this provider response shape cannot support the requested complete allocation coordinate system without changing the estimand or imputing missing evidence.

## v4 provider-native coordinate capability

`v4/` preserves every v1-v3 byte and freezes a provider-native coordinate contract. Total input and output are additive budget coordinates; cache-read and reasoning are typed subcomponents and are never added again; cache-write is explicitly unavailable rather than zero. The contract and identical condition support signature are bound into configured-system and comparison identity. The validator rejects support drift, asymmetric conditions, hidden imputation/derivation, parent/subcomponent double counting, omitted/duplicate/reordered calls, retry substitution, phase spoofing, identity drift, and mismatch on any jointly supported aggregate coordinate.

Exactly one fresh no-replacement `openai-codex`/`gpt-5.6-sol` probe passed. Its native total-input, cache-read, output, and reasoning coordinates exactly reconcile; cache-write remains unavailable despite the downstream aggregate reporting zero, and no uncached prompt value is derived. Included cost remains USD 0.00.

The matched pair was not run. `v4/readiness-report.json` fails closed because no frozen launcher yet binds v4 telemetry/state identities to the parent isolation and dual-rubric path, and no v4 adoption-observation rule was frozen before treatment output. Historical parent trials cannot be repurposed or replaced.

## v5 bound pair launcher and retained invalid pair

`v5/` preserves v1-v4 and freezes `scripts/allocation_pair_launcher_v5.py`, both parent rubrics, the v4 identities/adapter, exact AB order and attempt IDs, stateless initial/final hashes, bubblewrap input/output boundaries, artifact/trace/usage inventories, and `v5/adoption-observation-rule.json`. The rule permits presentation evidence from the mounted guide but refuses to infer invocation from incomplete stdout or adoption from presentation, guide terms, shared-rubric alignment, or artifact similarity.

The zero-call preflight passed coordinate-contract, isolation, retained-service, environment, grader, order, state, adoption-observability, and included-cost gates. The launcher therefore executed each already ordered attempt exactly once and did not replay `alloc-v4-configured-provider-probe-01`.

The retained pair is **not a substantive comparison**. The no-skill arm completed its artifacts and reported included USD 0.00, but its nine native transport events include three timeout/error events with unavailable coordinates while aggregate usage counts six successful API calls. The public-skill arm retained two successful and three timeout/error events, failed service completion, produced no required work artifacts, and has no cost receipt. This creates asymmetric coordinate support and invalidates the pair. No attempt may be retried or replaced. `v5/execution/posthoc-artifact-observation.json` describes the no-skill artifact under both frozen rubrics (independent `5/12`; shared `5/13`) without restoring pair validity. Public-skill presentation is observed, invocation unavailable, and adoption not observed.

### Replay

```bash
python scripts/validate_allocation_telemetry.py \
  pilots/prospective-allocation-telemetry/v2/manifest.json \
  --native-events pilots/prospective-allocation-telemetry/v2/stub-native-events.jsonl \
  --attempt-id alloc-v2-ab-no-skill \
  --aggregate-usage pilots/prospective-allocation-telemetry/v2/stub-aggregate-usage.json \
  --check-paths
python scripts/validate_allocation_coordinates.py \
  pilots/prospective-allocation-telemetry/v4/manifest.json \
  --events pilots/prospective-allocation-telemetry/v4/configured-provider-probe/outputs/call-events.jsonl \
  --attempt-id alloc-v4-configured-provider-probe-01 \
  --aggregate-usage pilots/prospective-allocation-telemetry/v4/configured-provider-probe/outputs/usage.json \
  --check-paths
python scripts/allocation_pair_launcher_v5.py validate
python scripts/allocation_pair_launcher_v5.py replay
python -m unittest tests.test_allocation_telemetry tests.test_allocation_coordinates tests.test_allocation_pair_launcher_v5 -v
```

This slice reports Skill presentation, invocation, adoption, artifact outcome, and resource allocation separately. It licenses no allocation/Skill effect, capability, cross-domain, expert/professional validity, safety, economic-value, production, or readiness claim.

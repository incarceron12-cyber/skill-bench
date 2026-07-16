# Prospective allocation telemetry v1

This bounded slice advances charter objectives B and C by turning the allocation audit's seven missing field families into a fail-closed executable trial envelope. It reuses the non-ceiling LH evidence-reconciliation task as an experimental substrate; it does not narrow `skill-bench` to this domain.

`manifest.json` freezes the task, configured system, sources, public Skill, exact AB/BA block identities, no-replacement policy, and claim ceiling. `scripts/validate_allocation_telemetry.py` validates per-call phase labels and five token coordinates; direct tool calls and wall time; all six phase totals; Skill bytes/tokens/hash; initial/final state hashes; retry and validity states; and separate presentation, invocation, adoption, and outcome-effect evidence.

The deterministic canary makes zero model calls and proves that a complete zero-resource ledger replays. Mutation tests reject omitted phases, duplicate events, misphasing, stale hashes, reordered attempts, retries/replacements, and presentation-as-adoption.

The retained readiness report is intentionally fail-closed. The configured Hermes one-shot `--usage-file` currently records aggregate session totals only. It does not expose native per-call records or reliable call-to-phase attribution, so wrapping the subprocess timer or dividing aggregate tokens would fabricate the required evidence. No fresh provider call or matched pair was executed. The exact blocker is a launcher/runtime telemetry hook that emits one record per provider call before aggregation.

## Replay

```bash
python scripts/validate_allocation_telemetry.py \
  pilots/prospective-allocation-telemetry/v1/manifest.json \
  --record pilots/prospective-allocation-telemetry/v1/canary-telemetry.json \
  --check-paths
python -m unittest tests.test_allocation_telemetry -v
```

This slice establishes capture-envelope conformance only. It makes no allocation-effect, Skill-effect, capability, professional-validity, cost-value, production-fitness, or readiness claim.

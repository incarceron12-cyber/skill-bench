# v6 logical-call / transport-attempt conformance

This zero-call slice projects the immutable v5 native event ledgers into two distinct levels:

1. a **logical agent call**, counted by retained aggregate `api_calls`; and
2. one or more ordered **transport attempts**, retained by the pre-aggregation adapter.

The projection is backward-compatible: no v1-v5 byte is changed and no provider call is replayed. Stable transport IDs are the original self-hashed `call_id` values. Logical IDs are versioned post-hoc IDs. Consecutive error events are grouped with the next successful event, or with the terminal end of the ledger. That grouping is an auditable reconstruction needed to reconcile the aggregate call count, **not** provider-native retry identity.

Resource evidence is typed per coordinate. `complete` means every retained transport attempt emitted the coordinate, `lower_bound` means emitted values are summed while one or more attempts remain unknown, and `unavailable` means no attempt emitted a value. Unknown is never replaced by zero. Successful-call aggregate linkage is separate from all-attempt resource evidence.

The retained audit explains:

- no-skill: 9 transport events → 6 logical calls, including two recovered retry runs; 6 successful aggregate calls; token coordinates are lower bounds across all attempts because three timeout attempts expose no usage;
- public-skill: 5 transport events → 3 logical calls; 2 successful calls plus one terminal failed logical call; token coordinates are lower bounds across attempts and the failed session aggregate is unavailable.

This does not restore v5 pair validity. It licenses no allocation or Skill effect, capability, economic value, expert/professional validity, production fitness, or readiness claim.

## Replay

```bash
python scripts/validate_transport_topology.py pilots/prospective-allocation-telemetry/v6/topology.json --check-paths
python scripts/validate_transport_topology.py pilots/prospective-allocation-telemetry/v6/topology.json --mutation-report --report-output pilots/prospective-allocation-telemetry/v6/conformance-report.json
python -m unittest tests.test_transport_topology -v
```

Design evidence: `pilots/prospective-allocation-telemetry/v5/execution/pair-summary.json`, both retained v5 trial reports, native ledgers, and aggregate usage files. General hypothesis: separating logical work calls from transport attempts preserves partial service/resource evidence across domains without treating retry failures as zero-cost or as independent agent actions.

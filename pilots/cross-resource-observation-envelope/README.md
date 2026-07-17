# Cross-resource observation and commit-envelope conformance

This is an **inert, builder-authored contract calibration package**. It extends the existing optional persistent-workspace instrument rather than introducing a PostgreSQL- or copy-on-write-specific subsystem. It executes no agent, database, network operation, or commit.

## General hypothesis

A stateful knowledge-work trial is not valid environment evidence merely because one selected state substrate was forked. A reusable envelope must freeze four independently inspectable identities:

1. **parent** — state root, schema/application version, start boundary, and concurrent-writer policy;
2. **overlay** — session, ordered operations/dependencies, heterogeneous mutable-resource inventory, and foreground/background propagation canaries;
3. **observer** — immutable comparator/read-set identity, exclusions, accepted alternatives, and ambiguity policy;
4. **commit** — selected operations, authorization, dependency closure, stale-base handling, discard default, and rollback policy.

The package tests that the benchmark validator fails closed when any identity is incomplete or contradicted. The reusable machinery applies to files, tables/spreadsheets, object stores, tickets, notebooks, queues/caches, and mixed workspaces. It does not make databases or Plane the project scope.

## Artifacts

- `package.json`: task/trial fragments with immutable observer hash and one synthetic attempt.
- `replay.py`: runs the package through the shared benchmark semantic-validator machinery and reproduces the retained defect report.
- `replay-report.json`: retained, hash-bound replay result.
- `tests/test_cross_resource_observation_envelope.py`: schema, backward-compatibility, replay, and mutation tests.
- `schemas/resource-observation-envelope.schema.json`: generic task/observation contract linked by the existing workspace instrument identity without changing historical benchmark-bundle bytes.
- `scripts/validate_benchmark.py`: fail-closed semantic checks.

Run:

```bash
python pilots/cross-resource-observation-envelope/replay.py
python -m unittest tests.test_cross_resource_observation_envelope -v
```

## Evidence and design-rationale map

All source-grounded fields cite the deep immutable-paper/release audit at `papers/agent-benchmarks/2026-07-17-copy-on-write-application-evaluation-validity.md`.

| Contract element or planted case | Evidence locator | Adaptation status |
|---|---|---|
| parent root, schema/app version, start boundary, concurrent-writer policy | “Parent and overlay state identity,” lines 61–78; “Repair” item 1 | Cross-domain project adaptation of the observed live-parent weakness |
| session and operation IDs; ordered dependency ledger | lines 63–78, 115–129; “Repair” items 1 and 6 | Source-grounded requirement; exact JSON representation is project-authored |
| structured table plus sequence and cache/queue inventory | “Isolation envelope,” lines 79–94; “Repair” item 3 | Source-grounded resource classes; synthetic locators are hypotheses only |
| foreground/background fail-closed canaries | lines 81–93; “Repair” item 2 | Source-grounded propagation gap; exact canary protocol is project-authored |
| required, forbidden, preserved, and unobserved regions | “Unique insight,” lines 212–224; “Repair” items 3 and 7 | Cross-domain project adaptation |
| immutable scorer read set, exclusions, comparator, alternatives, ambiguity | “Session-level scoring,” lines 95–113; “Repair” items 4 and 7 | Source-grounded observer weaknesses; canonical observer hash is project machinery |
| intentional null update | lines 73–78; limitation 10; “Repair” item 6 | Directly planted from audited semantic risk |
| untagged background write | lines 81–93; limitations 5–6 | Directly planted from fail-open/context-propagation risk |
| sequence increment | lines 81–89; limitation 7 | Directly planted unobserved global effect |
| cache/queue effect | lines 81–93; limitation 7 | Directly planted non-table observer gap |
| same-resource wrong-item ambiguity | lines 95–113; limitations 13–15 | Directly planted greedy-matching ambiguity |
| accepted alternative | lines 103–113; “Repair” item 7 | Source-grounded need; the synthetic item is not expert-approved domain evidence |
| concurrent parent change | lines 61–75; limitation 4 | Directly planted live-base conflict |
| failed attempt retained in denominator | lines 147–157; limitation 23; “Repair” item 10 | Directly planted missingness/disposition requirement |
| selected operations, stale/dependency-incomplete commit, discard, rollback | lines 187–224; limitations 19–20; “Repair” item 11 | Source-grounded policy; no real commit or rollback was executed |
| exact claim ceilings | source “Claim ceiling,” lines 316–318 | Conservatively expanded to keep every prohibited project claim false |

The synthetic expected values, item keys, state hashes, operation graph, and one accepted-equivalence record are **internal project hypotheses for validator calibration**, not expert testimony or professional ground truth.

## Planted result and claim ceiling

The replay records all eight required contrasts: preserved null, escaped untagged background write, sequence increment, excluded cache effect, same-resource ambiguity, parent change, rejected stale/dependency-incomplete commit, and failed evaluation retained in the denominator. The package disposition is `invalid_environment`; this is the expected detection result, not an agent failure.

The package licenses only this claim: **the current validator detects these exact builder-authored cross-resource envelope defects and admits the declared unambiguous alternative in the retained synthetic fixture**. It does not establish complete isolation, workflow correctness, causal repair, capability, professional validity, safety, reliability, production fitness, or readiness.

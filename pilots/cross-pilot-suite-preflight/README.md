# Cross-pilot suite assembly preflight

This internal package implements the frame/content/assembly/inference boundary in
`docs/benchmark-design-taxonomy.md` §2.6 as a bounded conformance check. It does
not introduce a new suite schema and does not alter any parent pilot.

## Design rationale

The frozen manifest inventories three unlike work shapes: spreadsheet/memo,
incident memo/action plan, and persistent workspace/action-state. Every parent
has repository path, SHA-256, and Git blob identity; public/private boundaries;
lineage; configured-system eligibility; task/grader health; replay commands; and
an explicit false claim ceiling. Admission means only that the package can
participate in this internal interface preflight. `substantive_evidence_eligible`
is false for every component, so package admission cannot become a pooled
capability denominator.

The runner is fail-closed: stale or missing parents, command failure, service-
invalid evidence presented as substantive, unexplained disposition, lineage
laundering, mixture drift, or claim upgrades fail the whole frozen assembly.
Commands are restricted to existing local validators, deterministic graders,
and exact replay; no agent command is allowed. Leave-one-component-out output
shows which work shape disappears, but cannot make unsupported claims robust.

## Run

```bash
python scripts/preflight_cross_pilot_suite.py \
  pilots/cross-pilot-suite-preflight/v1/manifest.json \
  --output pilots/cross-pilot-suite-preflight/v1/preflight-report.json
python -m unittest tests.test_cross_pilot_suite_preflight -v
```

The retained report is internal conformance evidence only. It makes no cross-
domain coverage, capability, expert/professional validity, safety, privacy,
production, public-release, or readiness claim.

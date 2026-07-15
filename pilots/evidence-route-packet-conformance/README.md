# Evidence-route packet conformance

This bounded internal pilot tests a general benchmark-design hypothesis: a structurally complete evidence packet is not decision-eligible unless its route is admissible and sufficiently covered, its raw and transformed evidence is identity-bound and true for the criterion, and environment or intervention invalidity remains separate from substantive failure.

## Charter decision filter

- **Objective:** advances charter objectives B and C by converting evidence-path and artifact-review research into executable cross-domain validation machinery.
- **Artifact/evidence:** `cases.json`, independently stored `labels.json`, hash-pinned raw evidence, `validate.py`, mutation/leakage tests, and `replay-report.json`.
- **Uncertainty clarified:** whether existing artifact-admissibility, trace, task-health, and validity concepts can represent route and packet defects without another schema. This slice found no missing schema invariant; a pilot-level checker is sufficient.
- **Mode:** building plus validation.
- **Duplication/scope:** reuses existing contracts and spans software-replication review and procurement-memo review. The software shape is a methodological case, not a scope commitment.
- **Useful completion:** all 12 frozen planted cases replay exactly, checker inputs exclude oracle/rationale fields, identity and locator mutations fail closed, and outputs separate structure, route coverage, evidence truth/sufficiency, invalidity, criterion conclusion, and decision eligibility.

## Contents and design

`cases.json` defines two route contracts and 12 packets. Routes carry required/optional phases, prerequisites, bounded substitutes, backtracking, intervention boundaries, environment/service state, actual phase/action paths, and stop reasons. Packets bind raw locators and SHA-256 digests to a minimal transformed observation and digest, while preserving declared contradictions, insufficiency, and packet-check records.

`labels.json` contains planted-defect names, rationales, and expected outcomes. `validate.py` never accepts labels in `check_case()` or `check_cases()`; it rejects `expected`, `oracle`, `rationale`, and `planted_defect` anywhere in checker input. `replay()` invokes the checker first and only then compares outputs with independently loaded labels. `freeze-manifest.json` pins the pre-checker case, label, and evidence corpus. Hashes establish identity, not truth.

The planted set includes:

1. supported packet;
2. contradicted packet;
3. insufficient packet;
4. failed documented route followed by a legitimate alternative;
5. prohibited semantic repair;
6. bounded valid substitute;
7. true environment invalidity;
8. irrelevant log;
9. fabricated log;
10. wrong-artifact evidence;
11. stale-service evidence; and
12. structurally complete but false packet.

The deterministic report deliberately keeps six outputs separate. `structural_completeness` does not imply `route_coverage`; either can coexist with invalid or contradicted evidence. `environment_invalid` is not a failed professional criterion, and a real but irrelevant or identity-mismatched log produces `evidence_invalid`, not zero credit.

## Provenance and rationale

- `papers/agent-benchmarks/2026-07-15-artifactcopilot-evaluation-workflow-validity.md`, especially lines 111–119, 185–205, and 301–322: phase packets, alternative routes, intervention boundaries, environment invalidity, and adversarial packet cases.
- `papers/agent-benchmarks/2026-07-14-groundeval-evidence-path-validity.md`, especially lines 137–167 and 210–238: proof-carrying evidence paths, alternative-complete contracts, source/service identity, valid-time, insufficiency, and strict claim ceilings.
- `schemas/README.md`, artifact-view admissibility section: raw/derived representation identity and fail-closed evidence outcomes.
- `schemas/TASK_HEALTH.md`: exact-version witnesses and instrument/environment invalidity.
- `schemas/VALIDITY_ARGUMENTS.md`: passing conformance licenses only narrow fixture behavior.

The cases and labels are builder-authored synthetic calibration, not expert testimony. They make no claim of expert or professional validity, general evaluator reliability, model capability, causal diagnosis, production fitness, or readiness.

## Run

```bash
python pilots/evidence-route-packet-conformance/validate.py \
  pilots/evidence-route-packet-conformance/cases.json \
  pilots/evidence-route-packet-conformance/labels.json \
  --report pilots/evidence-route-packet-conformance/replay-report.json
python -m unittest tests.test_evidence_route_packet_conformance -v
```

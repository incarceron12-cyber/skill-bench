# Cross-pilot non-ceiling Skill study v2

This additive directory is the prospective v2 continuation after v1 failed closed. Every v1 byte remains preserved. V2 changes one instrument defect before any model call: the guide-shared LH rubric now independently scores the already-public prospective-number marker requirement. The planted cases, grader mapping, rubric, manifest, schedule, and hashes are newly frozen for v2.

## What is frozen

- two structurally distinct synthetic clusters: LH evidence synthesis and vendor persistent-workspace state reconciliation;
- task-specific no-Skill/public-Skill inputs;
- guide-independent and explicitly guide-shared rubric definitions;
- auditable independent-construction manifests (file-access independence, not blinded human independence);
- eight opaque scheduled attempts: two per Skill condition per cluster, one invocation each, no retry, replacement, or adaptation;
- configured-system identity/hash, cost and service gates, missingness/denominator/stopping rules, cluster-aware estimands, and strict false claim ceilings;
- a mandatory four-class calibration gate and alternative-valid-path requirement that must pass before any model call.

The source split, distractor, sequence supersession, and state-transition requirements are public. `design-rationale.json` records their reviewed local basis or labels them as builder-authored unvalidated hypotheses. No task, guide, rubric, or threshold is expert-approved.

## Verify the freeze

```bash
python pilots/cross-pilot-nonceiling-skill-study/v2/validate_protocol.py
python pilots/cross-pilot-nonceiling-skill-study/v2/calibration/grade_calibration.py
python pilots/cross-pilot-nonceiling-skill-study/v2/preflight/run_canaries.py
python -m unittest tests.test_cross_pilot_nonceiling_v2 -v
```

## Continuation gate

Do not execute agents until the v2 calibration and all six zero-call canaries pass and that evidence is committed and pushed separately. If any frozen discrimination, public-basis, alternative-path, hash, or isolation requirement fails, abort v2 before calls and retain the failure. Calls are allowed only after that separate commit and provider-reported included USD 0.00.

This instrument can eventually describe exact retained contrasts within two synthetic clusters. It cannot establish a general Skill effect, task-cluster capability, expert/professional validity, safety, production fitness, cross-domain generality, or readiness.

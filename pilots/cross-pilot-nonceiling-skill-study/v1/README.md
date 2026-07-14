# Cross-pilot non-ceiling Skill study v1

This directory freezes the **prospective, pre-calibration, pre-model-call** vertical slice for the queued cross-pilot study. It preserves every byte of the completed vendor matrix, LH trials, and cross-pilot v0.1–v0.3 audit.

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
python pilots/cross-pilot-nonceiling-skill-study/v1/validate_protocol.py
python -m unittest tests.test_cross_pilot_nonceiling_protocol -v
```

## Continuation gate

Do not execute agents from this commit. The next bounded slice must preserve these bytes, create hash-bound planted positive, minimally wrong, shortcut, abstention/invalid, and alternative-valid cases for **both** rubrics in **both** clusters, implement/replay the graders, and run independent-construction plus agent/private-input zero-call canaries. If any frozen discrimination/public-basis/alternative-path requirement fails, abort v1 before calls and retain the failure. Calls are allowed only after a separate committed passing calibration/canary record and provider-reported included USD 0.00.

This instrument can eventually describe exact retained contrasts within two synthetic clusters. It cannot establish a general Skill effect, task-cluster capability, expert/professional validity, safety, production fitness, cross-domain generality, or readiness.

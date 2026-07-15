# Procedural fingerprint component-invariance calibration

This bounded vertical slice tests whether a trajectory-sequence diagnostic can be exercised without laundering configured-system discrimination into a skill, capability, or monitoring claim. It advances charter objectives **B** (expertise-to-evaluation methodology) and **C** (executable diagnostic infrastructure). It is validation/building, not a new benchmark domain.

## General hypothesis

A procedural representation can retain treatment-associated sequence structure across held-out task groups while remaining sensitive to native interface and canonicalizer choices. Even when it discriminates a configured treatment, semantic artifact/state evidence can be more outcome-relevant. Therefore a fingerprint belongs to a configured system plus observer policy and should remain a secondary diagnostic.

## Artifact and uncertainty

`protocol.json` deterministically expands to 48 builder-authored synthetic trials crossing:

- two unlike work shapes: evidence memo and incident triage;
- three task groups per shape (two fit/tuning groups and one held out);
- baseline versus procedure-guided configured treatments;
- shell-like versus workspace-API native interfaces;
- strict versus deliberately perturbed canonicalizers;
- two repeated attempts and planted pass/fail artifact states.

`analyze.py` fits bigram vocabulary and selects its size using leave-one-training-task-group-out treatment discrimination. Held-out groups never enter fitting or selection. It compares native events, strict and perturbed canonical atoms, strict and perturbed learned bigrams, length/tool-mix, and authoritative semantic artifact/state baselines. It reports held-out-task discrimination, held-out-interface transport, outcome association, unknown-action mass, observer sensitivity, repeated stability, and missing/invalid denominators. `report.json` is an exact deterministic replay.

The fixture is intentionally synthetic. It clarifies whether the machinery catches observer and interface nuisance, not whether any real agent has a stable procedure or useful skill. There are no model calls, expert judgments, randomized interventions, or prospective decisions.

## Main calibration result

On the planted matrix, strict canonical atoms and selected bigrams recover treatment labels on all 16 held-out-task trials, while the native-event representation degrades when transported across interfaces. The perturbed canonicalizer creates nonzero unknown-action mass and measurable strict-versus-perturbed distance. Trace representations associate with, but do not perfectly recover, planted held-out outcomes; semantic artifact/state evidence does. These are fixture conformance facts only.

The report separately keeps these claims unsupported:

- causal intervention effect;
- transferable skill or professional capability;
- temporal/operational reliability;
- calibrated routing or monitoring decision utility;
- production or release readiness.

## Provenance and rationale

Every design family in `protocol.json` points to a local full review or existing executable conformance artifact. The primary rationale is the ProcGrep review and bounded release audit. Harness-Bench motivates interface identity; Claw-Eval and the trajectory-observer fixture motivate action/state channel separation; Agent Reliability Profile motivates repeats; Agentic Confidence Calibration motivates the prediction/decision boundary.

## Replay

```bash
python pilots/procedural-fingerprint-invariance/analyze.py \
  --report pilots/procedural-fingerprint-invariance/report.json \
  --check-paths
python -m unittest tests.test_procedural_fingerprint_invariance
```

Useful completion is a deterministic, fail-closed calibration slice with explicit claim ceilings. A real follow-on would require valid repeated traces crossed over task, interface/harness, and treatment; it must not reuse this fixture as empirical evidence.

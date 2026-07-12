# Generated evaluator validity slice

This retained internal experiment tests the general hypothesis that evaluator-engineering guidance can improve more than syntax while still not licensing evaluator-validity claims. It uses two structurally different work shapes: stateful workflow trajectories and authoritative structured state plus rendered artifact views.

## Design and provenance

The design follows `papers/agent-benchmarks/2026-07-12-evalagent-domain-evaluation-skill-validity.md`, especially its independent-oracle, planted-defect, invariance, abstention, and held-out-reuse recommendations. Frozen criteria were adapted before generation from `pilots/trajectory-observer-conformance/conformance.json` and `tests/fixtures/valid-artifact-admissibility-bundle.json`. The twelve oracle labels in `frozen-cases.json` were never included in either generation prompt.

One model/provider/harness generated both evaluators: `gpt-5.6-sol` / `openai-codex` / Hermes one-shot, one API call per arm. The treatment adds only `evaluation-procedure.md`; prompts, raw final responses, generated code, stderr, usage, hashes, and replay outcomes are retained under `trials/`. The standard library is the complete dependency set; replay uses Python isolated mode. No dynamic documentation was queried, so there is no documentation response to preserve.

Run:

```bash
# Regenerates both arms (uses configured provider access)
python pilots/generated-evaluator-validity/run_experiment.py --generate

# Replays retained code without model calls
python pilots/generated-evaluator-validity/run_experiment.py
python -m unittest tests.test_generated_evaluator_validity -v
```

## Observed result

Both generated programs compiled and executed. No-guidance passed 7/12 oracle cases: 2/4 intended discrimination, 0/2 superficial-cue adversaries, 2/2 abstention, 2/2 invariance, and 1/2 held-out reuse. Procedure guidance passed 12/12. Inspection shows the no-guidance evaluator used the undeclared label `rejected` where the frozen outcome vocabulary required `failed`; this is a genuine interface/criterion-conformance failure, not evidence that its substantive logic was wholly wrong. The procedure arm preserved the required vocabulary and all planted distinctions.

Generation used 20,881 versus 21,400 total tokens, one call each; the provider usage reports included cost as `$0.00`. Generation wall time was 25.31 versus 28.45 seconds. These are single generated evaluators over twelve builder-authored cases, so no uncertainty or general treatment-effect estimate is available.

## Claim ledger

Supported, narrowly:

- both retained artifacts have syntax/import and pinned-execution conformance;
- on this frozen internal matrix, procedure guidance had higher exact oracle-outcome agreement (12/12 vs 7/12);
- the matrix separately exposes discrimination, superficial-cue, abstention, invariance, and held-out-reuse behavior rather than collapsing them into execution success.

Not supported:

- criterion equivalence to an expert evaluator;
- evaluator-expertise transfer as a general causal effect;
- professional or user validity;
- reliability/calibration, production use, or deployment readiness.

The 12/12 result must not promote these claims: criteria and cases are builder-authored, each condition has one generation, development examples overlap both work shapes, and held-out reuse is only one case per shape. A future continuation should add repeated generation seeds and a genuinely different held-out pilot whose criteria were not present in the prompt; it should not add another schema.

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

The 12/12 result must not promote these claims: criteria and cases are builder-authored, each condition has one generation, development examples overlap both work shapes, and held-out reuse is only one case per shape.

## Cross-pilot transfer continuation (three matched pairs)

`transfer-cases.json` freezes eight vendor-incident-response cases adapted from `pilots/vendor-incident-response/calibration-cases.json`, `grade_v2.py`, and the public v2 task. This pilot is meaningfully different from both original prompt shapes: it combines evidence freshness, bounded action, protected-state integrity, utility, and environment eligibility. Every case records a source locator or a builder-authored calibration label. The original prompts contain none of these criterion semantics; the transfer prompts disclose the criterion contract and two unlabeled examples, but omit all frozen case IDs, complete payloads, and oracle labels.

`run_transfer_experiment.py --generate` retained three independently generated matched pairs under the same `gpt-5.6-sol` / `openai-codex` / Hermes one-shot harness. All six artifacts compiled and scored **7/8**. Per-pair procedure-minus-no-guidance differences were therefore **0, 0, 0**. Every arm passed valid, substantive-failure, superficial-cue, insufficient-evidence, invalid-environment, invariance, and one held-out-reuse case. Every arm mapped the held-out over-refusal case to `insufficient_evidence` rather than `over_refusal` because its incident object is null.

That shared miss is a **substantive criterion-priority conflict, not a vocabulary/interface error**: the source calibration labels an artifact-free refusal `over_refusal`, while the disclosed fail-closed rule can also make its missing incident observation insufficient evidence. The repeated convergence falsifies a simple claim that the procedure treatment improves this transfer matrix, and it exposes an authoring defect that exact outcome agreement alone would otherwise misattribute to generated evaluators. No post-generation oracle was changed. A future instrument revision should separate “observed refusal with sufficient refusal evidence” from “missing task evidence,” version the matrix, and retain these scores as historical evidence rather than rewrite them.

Generation used one call per arm (six total), 20,891–22,051 total tokens per call, 21.03–39.10 seconds, and provider-reported included cost of `$0.00`. These are three generation attempts from one configured model/provider/harness, not randomized seeds or independent professional judgments; descriptive repetition does not license a general treatment effect.

Additional narrow support:

- all six retained evaluators have syntax/import and pinned replay conformance;
- the procedure advantage observed on the original prompt-overlapping matrix did not recur on this held-out pilot;
- the frozen matrix detected a shared criterion-priority ambiguity and preserved it rather than silently relabeling the oracle.

Still unsupported: criterion equivalence, expert validity, professional capability, a general treatment effect, production use, and deployment readiness.

## Criterion adjudication continuation

`criterion-adjudication.md` freezes the public-basis, evidence-view, accepted-alternative, and precedence decision. It finds the old null-incident oracle defective because the case contains neither observed refusal nor authoritative incident evidence; the conclusion-like `utility: "over_refusal"` cannot establish refusal. The immutable v1 matrix and scores remain untouched. `adjudication-cases-v2.json` relabels that copied case as `insufficient_evidence` and adds nine boundary cases. `adjudicate_criterion.py` independently implements the protocol and replays all six retained evaluators.

The reference passed 10/10. Retained evaluator scores were 7/10, 7/10, 7/10, 6/10, 7/10, and 7/10, demonstrating that agreement on the original conflict did not establish broader criterion validity. Exact diagnostics and hashes are in `criterion-adjudication-report.json`. No expert, professional, capability, treatment-effect, production, or readiness claim is licensed.

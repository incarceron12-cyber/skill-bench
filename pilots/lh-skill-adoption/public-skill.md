# Skill-grounded scoring adoption analysis

This is public procedural guidance, not an exact rubric.

## Inspect

1. Read every row in `source-pack/decision-evidence.csv` and follow its locator to the reviewed source when wording or scope is uncertain.
2. Distinguish the configured system (model, harness, skill integration, tools) from a base-model claim.
3. Keep measurement consistency, artifact quality, professional preference/readiness, cost, and diagnosis as separate claim families.

## Reconcile

Choose either procedure below, or another procedure that reaches the same observable boundaries:

- **Evidence-first:** build a row-level evidence matrix, compare apparently conflicting results, then formulate the decision.
- **Risk-first:** state the decision threshold and principal validity risks, seek disconfirming evidence, then complete the evidence matrix.

For either route:

1. Pair each material claim with an evidence ID, reported scope, and caveat.
2. Explicitly reconcile stronger aggregate inter-judge agreement with weak individual human/automated concordance.
3. Treat the seven-run execution ablation as directional, not a stable causal estimate.
4. Separate what the evidence supports now from what requires a controlled pilot.

## Decide and verify

1. Recommend `adopt`, `pilot with controls`, or `do not adopt` for skill-grounded scoring.
2. State the decision threshold, the minimum controlled experiment, and at least one stop/reconsider condition.
3. Deliver `outputs/evidence-matrix.csv` and `outputs/recommendation.md`.
4. Before delivery, verify that every material number and causal statement has an evidence ID and that no aggregate agreement result is presented as proof of professional validity.

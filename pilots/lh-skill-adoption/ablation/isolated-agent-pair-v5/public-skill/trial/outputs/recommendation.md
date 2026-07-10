# Recommendation: pilot with controls

## Decision

Run a controlled pilot; do not make skill-grounded scoring the production benchmark score yet.

The evidence supports promise on reliability but not current validity or causal readiness. In the reported Figma comparison, mean pairwise quadratic-weighted kappa was 0.60 for expert rubrics and 0.46 for generic rubrics [E01, E02]. Reported judge variance was 0.10 versus 0.25 [E03, E04]. Those comparisons are encouraging, but the intervention changed author source, rubric count, grouping, weights, anchor language, and observability together, so they do not identify which change caused the agreement difference [E01]. Agreement also is not professional validity [E03, E04].

The direct validity evidence is weak: human/LLM kappa was 0.08 for individual outputs and 0.06 for individual skills [E05, E06]. The human baseline came from one Figma domain expert, and no independent human process annotation validated the skill judges [E05, E06]. Readiness is similarly unresolved: only 60 percent of pairwise-winning Figma outputs met the expert score threshold of at least 4, based on 31 rated tasks and one expert [E10]. Thus, relative ranking cannot currently substitute for an absolute professional-readiness gate [E10].

The execution evidence must not be used as a causal justification for scoring adoption. The ablation had 7 paired runs over 3 tasks and bundled model, harness, and integration factors [E07]. The reported aggregate Codex gain of +0.87 is a directional signal from a subset of those 7 pairs, not a stable causal estimate [E08]. Likewise, 2 of 7 no-skill runs deployed, but deployment cannot be attributed to procedure content rather than integration or stochasticity [E09].

## Explicit decision threshold

Advance from pilot to adoption only if **all** of the following pre-registered gates pass on a held-out test set:

1. **Scoring validity:** for both output-level and skill-level judgments, human/automated kappa is at least 0.40 and its 95% confidence-interval lower bound is at least 0.20. These are prospective program gates, deliberately above the observed 0.08 and 0.06 baselines [E05, E06].
2. **Reliability advantage:** skill-grounded scoring has mean pairwise quadratic-weighted kappa of at least 0.60, exceeds the generic rubric by at least 0.10, and the 95% confidence interval for that paired difference excludes zero. The absolute gate matches the reported 0.60 signal, while the controlled difference is needed because the reported 0.60-versus-0.46 comparison bundled multiple rubric changes [E01, E02].
3. **Readiness calibration:** at least 80% of outputs that skill-grounded scoring labels “ready” also meet the independently defined expert readiness threshold, with a 95% confidence-interval lower bound of at least 70%. This is a prospective program gate responding to the reported 60% expert-threshold rate among pairwise winners; it is not claimed as a threshold established by the paper [E10].
4. **Robustness:** every tested domain and model/harness stratum meets the validity lower-bound gate, and no stratum shows a statistically supported decrease in expert-rated outcome quality under any execution intervention. This prevents a pooled result from hiding the heterogeneity observed in the small skill ablation [E07].

The numerical cutoffs in this section are proposed governance criteria, not empirical facts from the source pack. Failure of any gate means no production adoption from this pilot.

## Minimum controlled experiment

Use a preregistered, blinded, crossed design with two separately analyzed components:

All experiment sizes and confidence levels below are prospective design requirements, not reported source-pack results; their purpose is to address the documented single-domain, single-expert, and underpowered evidence [E05, E07, E10].

### A. Scoring experiment (required for the adoption decision)

- Sample at least 3 task domains, including Figma, with at least 30 held-out tasks per domain. This is a proposed minimum to move beyond the single-domain evidence and the 31-task, one-expert readiness assessment [E05, E10].
- Include at least 3 materially different model/harness systems. The source ablation covered Claude, Codex, and Gemini systems but bundled system and integration effects; stratification is therefore required [E07].
- Generate outputs before scoring and score each identical output under both generic and skill-grounded rubrics. Randomize rubric order and conceal system identity from judges. Holding outputs fixed isolates the scoring/rubric comparison from execution quality.
- Use at least 2 independent domain experts per item, with adjudication of disagreements and a written readiness standard fixed before automated judging. This proposed minimum addresses the one-expert baseline and missing independent process annotation [E05, E06, E10].
- Keep rubric content, criterion count, grouping, weights, anchor language, and observable evidence constant except for the single preregistered skill-grounding contrast. This is necessary because those factors were bundled in the reported comparison [E01].
- Report paired estimates and 95% confidence intervals for inter-judge agreement, human/automated concordance, readiness precision, and domain/system strata. Determine the final sample size prospectively from the number required to test the gates above; the stated task count is a floor, not a substitute for power analysis.

### B. Execution experiment (required only for claims that supplying skills improves agent outcomes)

- Within every task and system stratum, randomize skill versus no-skill execution; use at least 3 independent repeated runs per cell and identical budgets, tools, harness settings, and integration paths. These are prospective controls designed to address the 7-pair underpowered result and its bundled factors [E07, E08, E09].
- Evaluate all outputs with blinded experts and both scoring methods. Estimate skill effects separately by system and domain before reporting any pooled effect.
- Do not treat a positive execution effect as evidence that the scoring method is valid, or stronger scoring agreement as evidence that supplying skills improves execution. They are different hypotheses.

## Stop and reconsider conditions

Stop the pilot and recommend **against production adoption** if either human/automated validity gate fails, if readiness precision falls below its gate, or if any domain shows a statistically supported harmful execution effect. Also stop if experts cannot reach a stable readiness definition or if blinding/audit reveals rubric leakage of model, condition, or expected answer.

Reconsider the rubric design rather than expanding deployment if reliability passes but validity does not: the existing evidence already shows that judges can agree more while matching human judgments poorly [E01, E03, E05, E06]. A later adoption decision requires a new held-out evaluation after revisions; the present evidence alone is insufficient.

## Bottom line

The appropriate action now is **pilot with controls**. The agreement and variance results justify testing [E01, E02, E03, E04], while weak human concordance, uncertain readiness, and underpowered bundled ablations rule out an adoption claim today [E05, E06, E07, E08, E09, E10].

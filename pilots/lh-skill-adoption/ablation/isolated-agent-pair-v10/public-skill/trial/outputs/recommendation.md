# Recommendation: pilot with controls

## Decision

Run a controlled pilot; do not adopt skill-grounded scoring as the production or sole benchmark score yet.

The evidence shows a useful reliability signal, but not sufficient professional validity or causal identification. In the same 92 Figma runs, mean pairwise quadratic-weighted kappa was 0.60 with the expert rubric and 0.46 with the generic rubric [E01, E02]. Reported judge variance likewise favored the expert rubric, 0.10 versus 0.25 [E03, E04]. Those comparisons bundled author source, rubric count, grouping, weights, anchor language, and observability, so they cannot establish that skill grounding caused the difference [E01]. Agreement also is not professional validity [E03, E04].

The validity evidence is presently adverse: individual-output human/LLM concordance was kappa 0.08 [E05], and individual-skill concordance was kappa 0.06 without independent human process annotation [E06]. The human baseline itself is narrow because the Figma assessment used one domain expert [E05]. Readiness is also unresolved: only 60 percent of pairwise-winning outputs met the expert threshold in 31 rated Figma tasks, and that single-expert threshold is not a universal professional standard [E10].

The causal evidence is too small to justify adoption. The execution ablation had 7 paired runs across 3 tasks and bundled harness, model, and integration factors [E07]. A +0.87 aggregate improvement in one configured Codex subset is promising but too sparse for a stable causal claim [E08]. Likewise, 2 of 7 no-skill runs deployed, but that difference cannot separate procedure content from integration and stochasticity [E09]. These findings justify testing, not production adoption or rejection of the approach.

## Explicit decision threshold

Adopt after the pilot only if all preregistered gates pass on a held-out evaluation set:

1. **Validity gate:** the lower bound of a 95% confidence interval for agreement between automated scores and the consensus of independent domain experts is at least quadratic-weighted kappa 0.60 at both output and skill levels. This is a program-set adoption threshold, deliberately far above the currently observed kappas of 0.08 and 0.06 [E05, E06].
2. **Reliability gate:** skill-grounded scoring improves mean pairwise inter-judge kappa by at least 0.10 over the generic-rubric control, with a 95% confidence interval excluding zero, while not increasing judge variance. The margin is a preregistered program threshold informed by the reported 0.60-versus-0.46 agreement and 0.10-versus-0.25 variance signals [E01, E02, E03, E04].
3. **Readiness gate:** at least 80% of outputs declared passing by the automated method must also meet a preregistered absolute readiness standard by expert consensus, with a 95% confidence-interval lower bound of at least 70%. These are program-set risk tolerances; the need for an absolute gate follows from the observed 60% readiness among pairwise winners and the single-expert limitation [E10].
4. **Operational gate:** scoring cost, latency, missing-score rate, and adjudication burden must stay within limits fixed before unblinding. No favorable validity or reliability result may be traded against an unregistered operational exception.

Failure of any gate means no adoption. The thresholds must not be revised after results are inspected.

## Minimum controlled experiment

Use a preregistered, randomized, blinded, blocked comparison:

- Sample at least 30 tasks from each of at least 3 materially different benchmark domains, with at least 3 independent runs per task-condition. These are minimum design requirements, not claims that this sample guarantees power; final sample size must be increased if an a priori power analysis for the reliability margin requires it. Multiple domains and repeated runs are required because the existing causal evidence covers only 3 tasks and 7 pairs and reports heterogeneous effects [E07].
- For each frozen output, randomly assign scoring order and evaluate it with both a skill-grounded rubric and a matched generic rubric. Hold model output, judge models, prompts outside the rubric treatment, decoding, rubric length/count, weights, grouping, and execution environment constant. This isolates rubric content/grounding from the bundled changes in the existing comparison [E01, E02].
- Separately randomize skill availability during generation within blocks defined by task, model, harness, and seed. Compare paired outcomes without changing integration or other instructions. This is needed because the current ablation bundles harness/model/integration factors and cannot identify the cause of the directional effects [E07, E09].
- Obtain blinded ratings from at least 3 independent domain experts per output. Experts must score both absolute output readiness and independently annotated process/skill adherence before seeing automated scores. This directly addresses the one-expert output baseline and absent independent process annotation [E05, E06].
- Keep a held-out confirmatory set, lock analysis code and exclusions before unblinding, report confidence intervals and domain-level effects, and treat task, model, harness, and seed as blocking or modeled factors. Do not pool away heterogeneous or negative effects, which were already observed directionally [E07].

## Stop and reconsider conditions

Stop the pilot or reconsider the method if any of the following occurs:

- interim blinded quality checks show systematic rubric leakage, treatment contamination, or inability to keep rubric length/count, weights, grouping, and observability matched—the same bundled dimensions that prevent causal attribution in the current evidence [E01];
- expert disagreement makes a stable consensus standard unattainable, or automated output-level or skill-level agreement remains near the currently reported kappas of 0.08 or 0.06 [E05, E06];
- any domain shows a materially harmful readiness or completion effect that is hidden by the aggregate, given the existing heterogeneous directional effects [E07]; or
- the confirmatory results fail any adoption gate. In that case retain human-led scoring, diagnose failure by domain and component, and require a new preregistered experiment before reconsidering adoption.

## Scope of conclusion

This recommendation is limited to the supplied source pack, which is pinned to the reviewed v2 evidence and marked internal-pilot-only. It does not claim transfer from Figma to other professional domains. The source pack also states that no domain expert has validated its row selection, scenario framing, procedures, or decision thresholds; therefore the pilot protocol and thresholds require independent domain review before execution.

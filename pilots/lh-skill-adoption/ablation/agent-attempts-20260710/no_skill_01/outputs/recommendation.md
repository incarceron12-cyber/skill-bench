# Recommendation: pilot with controls

## Decision

Run a bounded, non-production pilot with controls. Do not adopt skill-grounded scoring as the benchmark's official score yet, and do not reject it outright.

The positive evidence is about reliability and is worth testing: expert-rubric mean pairwise quadratic-weighted kappa was 0.60, versus 0.46 for the generic rubric, across the reported 92-run comparison [E01, E02]. Reported judge variance was 0.10 with the expert rubric and 0.25 with the generic rubric [E03, E04]. Those findings show a consistency signal, but they do not establish professional validity [E03, E04], and the rubric comparison bundled source, rubric count, grouping, weights, anchor language, and observability rather than isolating skill grounding [E01].

The validity evidence blocks immediate adoption. Individual automated output grades had human/LLM kappa 0.08 [E05], and individual automated skill grades had human/LLM kappa 0.06 [E06]. The human baseline itself came from one Figma domain expert for output concordance, while no independent human process annotation validated the skill judges [E05, E06]. In addition, only 60 percent of pairwise-winning outputs met the expert >=4 readiness threshold among 31 rated Figma tasks, so relative ranking cannot be treated as absolute readiness; that threshold also came from one expert and is not a universal professional standard [E10].

The execution evidence is hypothesis-generating, not causal support for adopting the scoring method. The ablation contained 7 paired runs over 3 tasks, with directional and heterogeneous effects and model, harness, and integration factors still bundled [E07]. The reported +0.87 Codex aggregate delta came from a subset of those 7 paired runs and is too small a base for a stable causal adoption claim [E08]. Likewise, 2 of 7 no-skill runs deployed, but that contrast cannot separate procedure content from integration or stochasticity [E09]. These execution outcomes also do not directly validate the scoring construct.

## Explicit decision threshold

Adopt after the pilot only if all of the following preregistered conditions hold on a held-out evaluation set:

- the skill-grounded scorer's automated scores achieve a positive, uncertainty-bounded improvement over the generic control in concordance with the consensus of independent domain experts;
- absolute expert-readiness classification is non-inferior to the generic control under a margin set before any outcomes are observed;
- the reliability advantage is reproduced across judges and task strata, rather than being driven by one judge, task, model, or harness;
- material disagreements pass blinded adjudication without revealing a construct failure, leakage, or rubric-induced gaming; and
- operational burden and failure rates stay within limits set before the pilot.

A higher inter-judge agreement result alone cannot satisfy this threshold because agreement is not professional validity [E03, E04]. The adoption decision must use held-out validity, reliability, safety, and operational results jointly. If the study is inconclusive, retain the current scoring system and classify the outcome as “no adoption,” not as evidence of equivalence.

## Minimum controlled experiment

Use a preregistered, randomized, blinded, matched-output scoring study:

- Freeze a stratified set of outputs spanning tasks, quality levels, models, and harnesses. Score the identical outputs with both the skill-grounded and generic rubrics so output quality cannot confound scorer comparisons.
- Recruit multiple independent domain experts. Have them rate absolute readiness and annotate process/skill evidence without seeing automated scores, condition labels, or each other's ratings. Resolve expert disagreement by a prespecified consensus or adjudication rule.
- Randomize rubric order and judge assignment; mask conditions in analysis where feasible. Keep task set, outputs, judge models, prompts, tools, sampling settings, and scoring aggregation fixed between conditions. The source comparison bundled several of these factors, so this isolation is necessary before making a causal attribution [E01].
- Prospectively power the sample using a smallest effect of practical interest and expected clustering by task and output. Do not use the underpowered 7-paired-run, 3-task execution ablation as the power basis for a definitive causal claim [E07].
- Make expert-consensus concordance and absolute-readiness error the primary outcomes. Treat cross-LLM agreement and judge variance as secondary reliability outcomes. Report uncertainty, missing ratings, subgroup/task heterogeneity, and all exclusions.
- Keep pilot scores shadow-only: they must not affect public rankings, release gates, or procurement decisions until the threshold above is met.

If the program also wants to test whether providing a skill changes agent execution, run that as a separate randomized matched-condition experiment with skill availability as the only manipulated factor. Do not infer that execution effect from the scoring study or infer scoring validity from execution results; the existing ablation bundles model, harness, and integration effects [E07].

## Stop and reconsider conditions

Stop the pilot or reconsider the approach if any of these occur:

- skill-grounded scoring worsens held-out concordance with independent expert consensus or absolute-readiness classification relative to the generic control;
- apparent gains disappear under task-, model-, judge-, or harness-stratified analysis;
- blinded adjudication finds systematic reward for superficial rubric-language matching, unverifiable process claims, or professionally unacceptable outputs;
- expert disagreement prevents a stable reference standard, in which case the validity question remains unresolved rather than favoring adoption; or
- the preregistered sample or masking is materially compromised.

Immediate rejection would be premature because the reported agreement and variance differences are promising [E01–E04]. Immediate adoption would overclaim because individual human/automated concordance is weak [E05, E06], readiness remains uncertain [E10], and the causal execution evidence is underpowered and confounded [E07–E09]. A controlled pilot is therefore the proportionate decision.

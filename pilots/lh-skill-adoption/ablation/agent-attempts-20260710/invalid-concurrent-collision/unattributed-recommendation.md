# Recommendation: pilot with controls

Do not adopt skill-grounded scoring program-wide yet, and do not reject it outright. Run a controlled pilot. The method has a promising consistency signal: mean pairwise quadratic-weighted kappa was 0.60 with expert rubrics versus 0.46 with generic rubrics (E01, E02), and reported judge variance was 0.10 versus 0.25 (E03, E04). Those are agreement findings, not proof of professional validity (E03, E04). Fine-grained human/LLM concordance was only kappa 0.08 for outputs and 0.06 for skills (E05, E06). In addition, only 60 percent of pairwise-winning outputs met the study expert's readiness threshold (E10). Immediate adoption would therefore convert a consistency result into a validity claim the evidence does not support.

The causal evidence also remains insufficient. The execution ablation comprised 7 paired runs over 3 tasks and reported directional, heterogeneous effects while bundling harness, model, and integration factors (E07). The reported +0.87 aggregate Codex improvement came from only a subset of those 7 paired runs, too few for a stable causal adoption claim (E08). Deployment in 2 of 7 no-skill runs is compatible with a procedure benefit, but it cannot separate procedure content from integration or stochasticity (E09). These findings justify reducing uncertainty through controlled replication, not claiming that skill grounding caused better performance.

## Decision threshold

Adopt after the pilot only if all of these preregistered gates pass:

1. The primary paired skill-grounded-versus-generic treatment effect has a two-sided 95 percent confidence interval whose lower bound is above zero on the prespecified task-level utility score. This is a conservative program decision rule prompted by the underpowered and bundled causal evidence, not an effect size inferred from it (E07-E09).
2. On independently annotated items, overall human/automated concordance is at least kappa 0.40, no tested domain is below 0.30, and the lower bound of the paired improvement over generic scoring is above zero. These are prospective program floors, selected to demand a material improvement over the reported kappas of 0.08 for outputs and 0.06 for skills rather than inferred from those results (E05, E06).
3. Skill-grounded scoring is non-inferior to generic scoring on absolute expert readiness: sensitivity and specificity must each be at least 0.80 and no more than 0.05 below the generic arm. These are prospective program gates; pairwise preference alone is insufficient because the current 60 percent readiness result came from one expert and is not an adoption bar (E10).
4. The benefit is not confined to one model/harness or one task type, because the existing effects are heterogeneous and system factors are bundled (E07, E08).

Failure to clear every gate means no broad adoption. The 95 percent confidence rule is a chosen control against false-positive rollout, not a claim that the source established that threshold (E07).

## Minimum controlled experiment

Use a preregistered, blinded, paired, randomized crossover comparing the same outputs under skill-grounded and generic scoring. At minimum, sample 3 materially different knowledge-work domains, 100 held-out outputs per domain, and 2 independent domain experts per domain; these are prospective program controls chosen to broaden the current one-domain, one-expert evidence, not source-derived sufficiency claims (E05, E10). Hold the output set, judge models and versions, prompts, criterion count, weights, score scale, and aggregation fixed; randomize scoring-condition order. Increase the sample if an ex ante power analysis for the decision threshold requires it. Analyze at the task and domain levels, report configuration-specific effects as well as the pooled effect, and preserve failures as outcomes rather than exclusions.

Run any separate procedure-execution test as a distinct randomized paired experiment with balanced condition order, fixed prompts, tools, budgets, and integration, plus independent stochastic replicates. Do not use it to identify scoring validity. The existing 7 paired runs over 3 tasks are explicitly inadequate for a stable causal claim, and their configured-system and deployment results retain integration and stochasticity confounds (E07-E09).

At least two blinded domain experts should independently annotate both final-output quality and process/skill execution, adjudicating disagreements without seeing treatment or automated scores. This minimum is a program control chosen to remedy the current reliance on one Figma expert and the absence of independent human process annotation; it is not a source-derived claim that two experts are sufficient for universal validity (E05, E06, E10). Evaluate both inter-judge reliability and human concordance, because improved agreement alone does not establish professional validity (E03-E06).

## Stop and reconsider conditions

Stop expansion and reconsider the method if the skill-grounded condition worsens absolute expert readiness, if its primary effect confidence interval includes zero, or if independent human concordance does not clear the preregistered floor (E05-E07, E10). Also stop or redesign if effects reverse across model/harness configurations, deployment differences disappear after integration and order are controlled, or scorer agreement improves without corresponding expert validity (E03, E04, E07-E09). A severe or systematic false-positive readiness pattern is an immediate stop condition even if average agreement improves (E03-E06, E10).

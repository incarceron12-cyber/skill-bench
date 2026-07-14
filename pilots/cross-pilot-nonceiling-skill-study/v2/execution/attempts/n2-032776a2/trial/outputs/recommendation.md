# Recommendation: pilot with controls

## Decision

**Pilot with controls.** The evidence supports a bounded evaluation of skill-grounded scoring, but not unsupervised or organization-wide use.

## Evidence synthesis

Aggregate judge consistency improved under the expert-rubric bundle: mean pairwise quadratic-weighted kappa was 0.60 versus 0.46 for generic rubrics across the same 92 Figma runs. The comparison bundled author source, rubric count, grouping, weights, anchor language, and observability, so it does not establish expert authorship—or any single component—as the cause. [E01, E02]

Reported judge variance was 0.10 under expert rubrics and 0.25 under generic rubrics on those runs, but agreement and low variance are not evidence of professional validity. [E03, E04]

At the individual-run level, human/LLM concordance was weak: kappa was 0.08 for output grades and 0.06 for skill grades. The human output baseline came from one Figma domain expert, and no independent human process annotation validated the skill judges. [E05, E06]

Absolute readiness also remains unresolved: only 60 percent of pairwise-winning outputs met the expert score threshold of at least 4 among 31 rated Figma tasks, and the supplied evidence says that this single-expert threshold is not a universal professional standard. [E10]

The configured-system ablation covered 7 paired runs over 3 tasks and reported directional, heterogeneous effects across Claude, Codex, and Gemini harness/model systems; harness, model, and integration factors remained bundled. [E07] One Codex subset showed an aggregate improvement of +0.87, but it was too small for a stable causal adoption claim. [E08] Also, 2 of 7 no-skill runs deployed, so deployment alone cannot separate procedure content from integration or stochasticity. [E09]

Taken together, aggregate consistency is promising, while individual human concordance, absolute readiness, and causal attribution are insufficient. These are conflicting measurement signals rather than proof that skill-grounded scoring is valid or deployment-ready.

## Controlled pilot and prospective gate

Use skill-grounded scores only as decision support; retain human approval for every consequential score or deployment decision. Pre-register tasks, rubric wording, scoring rules, exclusions, and analysis before examining outcomes. Randomize and blind paired skill/no-skill conditions, hold the harness, model, integration, prompts, and task inputs fixed, and repeat seeds so that skill content is the intended contrast. Include generic-rubric scoring as a measurement comparator.

The minimum experiment is {{PROSPECTIVE:at least 120 paired runs}}, spanning {{PROSPECTIVE:at least 30 tasks}}, {{PROSPECTIVE:at least 2 materially different configured systems}}, and independent ratings from {{PROSPECTIVE:at least 3 qualified domain experts per output}}. Collect both outcome/readiness ratings and independent process annotations. Report uncertainty intervals, missingness, disagreements, task-level results, system-level results, and all failures; do not rely on aggregate preference alone.

Proceed beyond the pilot only if all pre-registered gates are met: human/automated concordance has a lower confidence bound of {{PROSPECTIVE:kappa 0.60}} for both output and process grades; absolute expert readiness is at least {{PROSPECTIVE:80%}} with a lower confidence bound of {{PROSPECTIVE:70%}}; and the paired skill effect is positive with a lower confidence bound above {{PROSPECTIVE:0.00}} in every configured system tested. These are analyst-selected prospective thresholds, not findings from the supplied evidence.

## Stop or reconsider conditions

Stop consequential use and reconsider the scoring design if either output-grade or process-grade concordance falls below {{PROSPECTIVE:kappa 0.40}}, if expert readiness falls below {{PROSPECTIVE:70%}}, if any tested configured system has a negative paired effect, or if serious failures are hidden by the aggregate score. Also stop causal interpretation if blinding or randomization fails, the skill/no-skill contrast changes the harness or integration, or independent process annotation cannot be obtained.

## Evidence needed to change the decision

Evidence sufficient to support broader adoption would be a pre-registered, adequately powered, multi-task and multi-system replication that passes every prospective gate; uses multiple independent domain experts; validates both outcomes and process; isolates skill content from rubric, harness, model, integration, and stochastic effects; and demonstrates absolute readiness without material safety or quality regressions.

Evidence sufficient to move away from the pilot would be a controlled replication showing persistently poor human concordance, failure of the absolute-readiness gate, null or harmful effects across configured systems, or inability to isolate the skill intervention. Until such evidence exists, missing cross-domain generalization and independent human process validation must be reported rather than inferred.

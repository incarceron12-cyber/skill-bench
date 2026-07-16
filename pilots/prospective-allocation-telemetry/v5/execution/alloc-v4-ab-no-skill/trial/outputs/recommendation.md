# Recommendation: pilot with controls

## Decision

Use skill-grounded scoring only in a bounded, human-supervised evaluation pilot. Do not use its scores as an autonomous release, ranking, compensation, or procurement gate during the pilot.

The evidence supports testing because expert-rubric inter-judge agreement was 0.60 versus 0.46 for the generic rubric across the reported 92 Figma runs [E01, E02]. Reported judge variance was likewise 0.10 versus 0.25 [E03, E04]. These are consistency signals, not proof of professional validity: the comparison jointly changed author source, rubric count, grouping, weights, anchor language, and observability, and agreement itself is not professional validity [E01, E03].

The strongest counterweight is individual-level validity. Human/LLM concordance was kappa 0.08 for output grades and 0.06 for skill grades [E05, E06]. The output baseline came from one Figma domain expert, while the skill judges lacked independent human process annotation, so neither general validity nor invalidity beyond that setting should be guessed [E05, E06]. Absolute readiness is also unresolved: only 60 percent of pairwise-winning outputs met the expert >=4 threshold among 31 rated Figma tasks, and that threshold came from one expert rather than a universal professional standard [E10].

The configured-system ablation is promising but not decision-grade. It comprised 7 paired runs over 3 tasks, produced directional and heterogeneous effects, and bundled harness, model, and integration factors [E07]. One configured-system subset reported a +0.87 aggregate improvement, but had too few runs for a stable causal claim [E08]. Also, 2 of 7 no-skill runs deployed; deployment alone cannot separate procedure content from integration and stochasticity [E09]. Thus the evidence does not establish that skill grounding caused a general performance gain [E07, E09].

## Prospective success threshold

Advance beyond the pilot only if all of these analyst-defined gates are met on a preregistered holdout:

- Human/automated concordance for both output and skill scores is kappa >= {{PROSPECTIVE:0.50}}.
- At least {{PROSPECTIVE:80%}} of outputs selected as winners meet a task-specific absolute-readiness standard established before scoring by independent professionals.
- The skill condition's primary performance effect has a {{PROSPECTIVE:95%}} confidence interval whose lower bound is greater than {{PROSPECTIVE:0.00}}.
- No prespecified configured-system or task subgroup declines by more than {{PROSPECTIVE:5 percentage points}} on absolute readiness.

These are prospective governance thresholds, not values reported by the supplied study.

## Minimum controlled experiment

1. Preregister tasks, scoring rules, primary outcome, exclusions, subgroup analysis, and the thresholds above.
2. Use at least {{PROSPECTIVE:30}} representative tasks per configured system, with paired skill/no-skill conditions, randomized condition order, identical prompts and resources apart from the skill intervention, and at least {{PROSPECTIVE:3}} independent run seeds per task-condition.
3. Mask evaluators to condition. Use at least {{PROSPECTIVE:2}} independent domain professionals per output to score absolute readiness and output quality; separately annotate whether the claimed skill steps were actually performed.
4. Keep harness, model, integration, runtime budget, and deployment checks fixed within each pair. Log failures and score all randomized runs under an intention-to-treat rule so completion and integration failures are not silently excluded.
5. Compare skill-grounded automated scores with the independent human output and process annotations, report uncertainty and subgroup results, and retain human review for every operational decision.

This design directly addresses the bundled rubric changes [E01, E02], the absence of independent process annotation [E06], the single-expert readiness boundary [E10], and the underpowered, bundled ablation [E07, E09].

## Stop or reconsider conditions

Stop operational use and reconsider the method if any preregistered gate fails, if evaluator masking or condition isolation is broken, or if the automated score can be improved without a corresponding improvement in independently judged readiness. In particular, stop if either concordance estimate is below {{PROSPECTIVE:0.50}}, readiness is below {{PROSPECTIVE:80%}}, the effect interval includes {{PROSPECTIVE:0.00}}, or any subgroup decline exceeds {{PROSPECTIVE:5 percentage points}}. The low reported individual concordance makes disagreement a central safety condition rather than a secondary diagnostic [E05, E06].

## Evidence needed to change the decision

Evidence supporting broader operational use would require a preregistered controlled study meeting every prospective gate, stable benefits across configured systems and representative tasks, independent multi-professional output and process validation, and a design that isolates skill content from rubric construction, harness, model, integration, and stochasticity. Those isolation needs follow from the current comparison and ablation caveats [E01, E07, E09]. Replication outside Figma would also be needed because all reported measurement and readiness evidence here is scoped to Figma runs or tasks [E01, E05, E10].

Evidence supporting discontinuation would be a sufficiently powered controlled estimate showing no benefit or material harm, persistent failure of the concordance or readiness gates, or evidence that score gains arise from judge-facing rubric artifacts rather than improved professional outcomes. The present rows conflict—aggregate judge consistency improves while individual human concordance remains weak—and do not resolve that question [E01, E02, E05, E06].

# Recommendation: pilot with controls

## Decision

Run a controlled pilot; do not make skill-grounded scoring the production decision rule yet.

The case is promising on consistency but unresolved on validity, operational readiness, and causality. In the rubric comparison, expert-rubric inter-judge agreement was 0.60 versus 0.46 for the generic rubric [E01][E02], while reported judge variance was 0.10 versus 0.25 [E03][E04]. Those results support further testing, not causal attribution: the comparison bundled authorship, source material, rubric structure, weights, anchor language, and observability [E01], and agreement is not professional validity [E03][E04].

The strongest disconfirming evidence is criterion validity. Human/LLM concordance was 0.08 for individual outputs [E05] and 0.06 for individual skills [E06]. These estimates come from Figma runs, with a single domain expert for the output baseline and no independent human process annotation for the skill judges [E05][E06]. The evidence is therefore too narrow to prove broad invalidity, but it is also too weak to justify production use of fine-grained automated skill scores.

Readiness is similarly mixed: 60 percent of pairwise-winning outputs met the expert >=4 threshold among 31 rated Figma tasks [E10]. Relative preference therefore did not reliably imply absolute readiness, and the single-expert threshold is not a universal professional standard [E10].

The causal evidence on whether providing a skill improves agent performance is underpowered. The ablation contained 7 paired runs over 3 tasks across bundled harness/model systems and found heterogeneous directional effects [E07]. A +0.87 aggregate gain appeared for one configured Codex subset, but there were too few runs for a stable causal adoption claim [E08]. Deployment in 2 of 7 no-skill runs is an operational signal, not proof that procedure content caused completion, because integration and stochasticity were not separated [E09].

## Explicit decision threshold

Move from pilot to production adoption if and only if all of the following preregistered conditions are met:

- The controlled estimate on the primary task-quality endpoint exceeds a program-defined smallest worthwhile improvement, and its uncertainty interval excludes both no improvement and the program-defined harmful boundary.
- Agreement gains survive on held-out tasks and configurations while the independent-human validity endpoint meets its preregistered acceptance criterion; improved judge-to-judge consistency alone does not pass.
- Absolute readiness meets a threshold set by independent domain experts before results are unblinded, rather than relying on pairwise preference.
- The effect remains after procedure content is isolated from rubric visibility, harness integration, and evaluator access.

This is an explicit conjunctive threshold: failure of any condition means no production adoption, regardless of a favorable aggregate score.

## Minimum controlled experiment

Use a preregistered, randomized, paired evaluation with skill and no-skill conditions applied to the same held-out task set. Keep model, harness, tool access, integration, budget, prompts other than the skill treatment, and retry policy fixed within each pair. Counterbalance run order and repeat runs under independently assigned random seeds.

Cross the execution treatment with evaluator access: score outputs using blinded independent-human outcome ratings and automated rubrics that either can or cannot inspect skill/process traces. This design is intended to distinguish an execution benefit from evaluator leakage or rubric alignment, addressing the bundled rubric comparison and unresolved integration confounding [E01][E09]. Include multiple task families, model/harness configurations, and independent domain experts. Collect both outcome quality and human process annotations, because current fine-grained output and skill concordance is weak [E05][E06]. Prospectively power the study for the smallest worthwhile effect rather than extrapolating from the 7 paired runs over 3 tasks [E07].

Predefine the primary outcome, smallest worthwhile effect, validity and readiness acceptance criteria, exclusion rules, missing/deployment handling, multiplicity policy, and subgroup analyses. Report paired effect estimates with uncertainty by task family and configuration; do not let the +0.87 subset result define the confirmatory endpoint after the fact [E08]. Track deployment explicitly while preventing the 2-of-7 no-skill observation from being interpreted causally without fixed integration [E09].

## Stop and reconsider conditions

Stop the pilot or retain the current scoring system if the controlled uncertainty interval crosses the preregistered harmful boundary, if independent-human validity fails its acceptance criterion despite higher inter-judge agreement, or if absolute readiness fails its expert-set threshold. Reconsider the scoring construct—not merely the sample size—if automated skill scores remain weakly aligned with independent human process annotations, if gains disappear when evaluator access to skill traces is removed, or if effects reverse materially across task families or harness/model configurations.

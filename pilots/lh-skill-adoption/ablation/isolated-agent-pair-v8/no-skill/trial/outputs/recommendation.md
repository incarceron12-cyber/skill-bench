# Recommendation: pilot with controls

## Decision

Run a controlled, non-production pilot. The evidence supports further evaluation, but not operational adoption: expert-rubric judges had mean pairwise quadratic-weighted kappa 0.60, versus 0.46 for generic-rubric judges, on the same 92 Figma runs [E01, E02], and reported judge variance was 0.10 versus 0.25 [E03, E04]. Those are useful agreement signals, not proof of professional validity [E03, E04]. At the individual-run level, human/LLM concordance was only kappa 0.08 for outputs and 0.06 for skills [E05, E06].

Readiness is also unresolved. Only 60% of pairwise-winning outputs met the single expert's score-at-least-4 threshold among 31 rated Figma tasks [E10]. That result cannot establish a universal professional standard because it uses one domain expert [E10]. The causal evidence is too weak for rollout: the ablation comprised 7 paired runs over 3 tasks, with directional and heterogeneous effects and bundled harness, model, and integration factors [E07]. The reported aggregate gain of +0.87 for Codex came from only a subset of those 7 pairs and is explicitly too small for a stable causal adoption claim [E08]. Likewise, deployment in 2 of 7 no-skill runs does not isolate procedure content from integration or stochasticity [E09].

## Explicit decision threshold

Advance from pilot to adoption only if a preregistered held-out analysis meets **all** of these gates:

1. The lower bound of a 95% confidence interval for the skill-grounded-versus-generic difference in human/LLM agreement is above 0 for both output scores and skill/process scores.
2. Inter-judge agreement is non-inferior to the generic rubric under a preregistered margin and improves without materially increasing judge variance. This treats the reported 0.60-versus-0.46 agreement and 0.10-versus-0.25 variance as motivating baselines, not guaranteed effects [E01-E04].
3. At least 80% of pilot outputs that win pairwise also pass an absolute readiness rubric independently scored by at least two domain experts. The 80% gate is a program governance choice, deliberately stricter than the observed 60% under one expert [E10].
4. The intervention improves the preregistered primary task outcome with a multiplicity-adjusted 95% confidence interval excluding zero, while deployment success and severe-failure rates are not worse than control.

Failure of any gate means no adoption on this evidence package.

## Minimum controlled experiment

Run a randomized, blinded, paired experiment on held-out Figma tasks, with the unit of randomization being an independent task instance. Compare otherwise identical runs with skill-grounded scoring/procedure enabled versus a generic-rubric control. Use no fewer than 30 independent task instances per arm, and increase that number if a prospective power analysis requires it. The minimum of 30 per arm is a conservative program-design floor, not an effect-size claim from the source pack.

The experiment must:

- cover each of the three harness/model systems represented in the existing ablation and use at least three task types, while stratifying randomization by system and task type; the prior 7-pair, 3-task ablation was underpowered and bundled system factors [E07];
- hold model version, harness, prompts, integration path, tool access, budget, and retry policy fixed within each pair, because existing deployment differences cannot separate procedure content, integration, and stochasticity [E09];
- use repeated seeds and report system-by-treatment heterogeneity rather than treating the +0.87 Codex direction as a general causal effect [E08];
- obtain independent, blinded ratings from at least two domain experts, adjudicating disagreements, because the existing human baseline used one Figma expert [E05, E10];
- collect independent human process annotations before comparing them with automated skill grades, since none currently validates the skill judges [E06]; and
- preregister primary outcomes, exclusions, non-inferiority margins, multiplicity handling, and the adoption gates above before examining treatment results.

## Stop and reconsider conditions

Stop the pilot early for safety or validity review if severe-failure or deployment-failure rates are materially worse in the skill-grounded arm, if blinding or treatment isolation is broken, or if independent experts cannot reach the preregistered minimum agreement. Reconsider the entire approach—not merely tune the rubric—if held-out human/LLM concordance remains near the reported individual-run kappas of 0.08 for outputs or 0.06 for skills [E05, E06], or if gains appear only in one configured system, as the small directional Codex result currently allows [E08].

## Evidence boundary

This recommendation is limited to the supplied source pack, which is pinned to arXiv v2 dated 2026-05-29 and marked internal-pilot-only. The manifest also states that no domain expert has validated the row selection, scenario framing, procedures, or decision thresholds. Therefore, the proposed thresholds are governance criteria for a controlled decision, not findings established by the reviewed study.

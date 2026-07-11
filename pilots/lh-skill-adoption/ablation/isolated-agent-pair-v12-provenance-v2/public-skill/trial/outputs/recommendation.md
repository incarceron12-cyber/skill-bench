# Recommendation: pilot with controls

## Decision

Run a controlled pilot; do not adopt skill-grounded scoring program-wide yet. The evidence is promising on inter-judge consistency but weak on professional validity, absolute readiness, and causal attribution.

The reliability signal is real enough to test: across 92 reported Figma runs, mean pairwise quadratic-weighted kappa was 0.60 with the expert rubric and 0.46 with the generic rubric [E01, E02], while reported judge variance was 0.10 versus 0.25 [E03, E04]. However, the comparison simultaneously changed rubric authorship/source, rubric count, grouping, weights, anchor language, and observability, so it does not identify skill grounding—or expert authorship—as the cause [E01, E02]. Agreement also is not professional validity [E03, E04].

Validity is the principal blocker. Human/LLM concordance was only kappa 0.08 for individual output grades and 0.06 for individual skill grades [E05, E06]. Those estimates are themselves limited by one Figma domain expert and the absence of independent human process annotation [E05, E06], so they neither validate the scorer nor prove that it cannot work elsewhere. They do rule out treating agreement among automated judges as sufficient evidence of validity.

Readiness is also unresolved. Only 60 percent of pairwise-winning outputs met the expert score threshold of at least 4 among 31 rated Figma tasks [E10]. That threshold came from one domain expert and is not a universal professional standard [E10]. Relative ranking gains therefore cannot be equated with acceptable absolute output quality.

Finally, causal evidence is underpowered. The skill-execution ablation comprised 7 paired runs over 3 tasks and bundled model, harness, and integration effects [E07]. The reported aggregate Codex gain of +0.87 is directional evidence from a subset, not a stable causal estimate [E08]. Likewise, 2 of 7 no-skill runs deployed, but deployment cannot separate procedure content from integration or stochasticity [E09]. These signals justify experimentation, not adoption.

## Explicit decision threshold

Advance from pilot to adoption only if a preregistered analysis simultaneously shows:

1. **Professional validity:** the lower bound of a two-sided 95% confidence interval for the skill-grounded scorer's association with blinded, independently adjudicated expert output ratings is greater than zero, and the association is materially stronger than the observed human/LLM kappas of 0.08 for output and 0.06 for skills [E05, E06]. The 95% rule is a prospective governance threshold, not a result reported by the source pack; it is chosen because the existing 7-pair ablation is explicitly underpowered [E07].
2. **Incremental reliability:** skill-grounded scoring improves inter-judge agreement over the same generic-rubric comparator while holding judge models, rubric count, grouping, weights, and observability fixed. The pilot should test whether the reported 0.60-versus-0.46 difference survives removal of the bundled design changes [E01, E02].
3. **Absolute readiness:** skill-grounded scoring does not increase acceptance of outputs that fail a domain-expert readiness standard defined before scoring. The existing result—60 percent of pairwise winners reaching at least 4 on a single-expert scale—is not an adoption threshold [E10].
4. **Operational benefit:** the confidence interval for the randomized skill-versus-control effect on the primary completion/deployment outcome excludes no improvement, with model, harness, integration, task, and run budget held constant. This is required because the current 7 paired runs bundle those factors [E07] and the 2-of-7 no-skill deployment observation is not causally diagnostic [E09].

Failure on any one criterion means no adoption from this pilot.

## Minimum controlled experiment

Use a preregistered, randomized, paired, blinded experiment with these minimum elements:

- Evaluate the same task instances both with and without the skill/procedure, using matched run budgets and blocked randomization by task, model, and harness. Repeat seeds within each block. This directly addresses the heterogeneity and bundled system effects in the 7 paired runs over 3 tasks [E07].
- Cross the scoring treatment separately: apply a skill-grounded rubric and a generic rubric to every anonymized output while holding judge models, rubric count, grouping, weights, anchor observability, and presentation order constant. This isolates rubric grounding from the co-changes in the reported 92-run comparison [E01, E02].
- Use at least two independent domain experts, plus blinded adjudication of disagreements, to rate output quality and annotate whether claimed skills/process steps are actually evidenced. “At least two” is a prospective minimum control, motivated by the single-expert limitation and missing independent process annotation [E05, E06, E10], not a claim that two experts guarantee validity.
- Select the number of tasks, systems, and repeated seeds through an a priori power analysis for the preregistered primary effect; it must exceed the existing 7 paired runs over 3 tasks. This is a minimum evidentiary requirement rather than a claim that any particular larger count is sufficient [E07].
- Report agreement, expert concordance, absolute readiness, completion/deployment, effect estimates, confidence intervals, missing runs, and integration failures. Keep relative preference separate from absolute readiness [E10].

## Stop and reconsider conditions

Stop the pilot and reject adoption if any of the following occurs:

- blinded expert concordance is no better than the reported kappa 0.08 for outputs or 0.06 for skills after the preregistered sample is complete [E05, E06];
- apparent agreement gains disappear when bundled rubric changes are controlled [E01, E02];
- the scorer systematically approves outputs below the preregistered professional-readiness standard, reflecting the documented gap between pairwise wins and the at-least-4 threshold [E10]; or
- benefit reverses materially across model/harness blocks, cannot be separated from integration failures, or remains too imprecise to exclude no improvement [E07, E09].

Also reconsider the program design before expansion if independent experts cannot agree on the process annotations: automated judge agreement would then lack a defensible human criterion [E03, E04, E06].

## Evidence boundary

This recommendation is limited to the supplied source pack, pinned to the reviewed v2 evidence. The pack identifies itself as internal-pilot-only and notes that no domain expert has validated its row selection, scenario framing, procedures, or decision thresholds. Accordingly, the proposed thresholds are governance choices for a controlled test, not claims established by the paper.

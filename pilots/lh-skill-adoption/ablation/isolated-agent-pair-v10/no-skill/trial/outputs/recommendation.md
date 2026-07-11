# Recommendation: pilot with controls

## Decision

Run a controlled pilot; do not adopt skill-grounded scoring program-wide now.

The case for a pilot is improved reported reliability: mean pairwise quadratic-weighted kappa was 0.60 with expert-workflow rubrics versus 0.46 with generic rubrics on the same Figma runs (E01, E02), while reported judge variance was 0.10 versus 0.25 (E03, E04). These comparisons justify further testing, but they do not establish professional validity. The rubric conditions changed several features together, so the agreement difference cannot be causally assigned to expert authorship, skill grounding, anchors, weighting, or observability (E01, E02).

The immediate-adoption case fails on validity and readiness. Individual-run human/LLM concordance was only kappa 0.08 for output grades and 0.06 for skill grades (E05, E06). The human baseline came from one Figma expert, and skill judgments lacked independent human process annotation, so these results are neither a universal validity estimate nor evidence that automated skill scores match professional judgment (E05, E06). In addition, only 60 percent of pairwise-winning outputs met the expert score threshold of at least 4 among 31 rated Figma tasks; relative preference therefore did not establish absolute readiness, and the threshold itself came from one expert (E10).

The execution ablation should not be treated as validation of the scoring method. It comprised 7 paired runs over 3 tasks across bundled harness/model systems and produced heterogeneous directional effects (E07). The reported aggregate Codex gain of +0.87 came from only a subset of those 7 pairs (E08). Likewise, 2 of 7 no-skill runs deployed, but deployment cannot be causally assigned to procedure content rather than integration or stochasticity (E09). This evidence can motivate an execution hypothesis, not an adoption claim (E07–E09).

## Explicit decision threshold

Advance from pilot to adoption only if all prespecified gates are met on a held-out evaluation set:

1. **Reliability:** the skill-grounded condition exceeds the generic-rubric condition by at least 0.10 in mean pairwise quadratic-weighted kappa, with the lower bound of a 95% paired confidence interval above zero. This is a prospective governance threshold, informed by but deliberately more conservative than merely reproducing the observed 0.14 gap (E01, E02).
2. **Criterion validity:** both output-level and skill-level automated scores achieve human-consensus quadratic-weighted kappa of at least 0.40, with each 95% lower confidence bound at least 0.30. These are prospective minimums chosen because the observed kappas of 0.08 and 0.06 are inadequate for consequential use (E05, E06).
3. **Readiness:** at least 80% of outputs selected as winners by the automated method also clear a prespecified absolute professional-readiness threshold under expert consensus, with a 95% lower confidence bound of at least 70%. This prospective gate directly addresses the reported 60% single-expert result rather than treating pairwise wins as readiness (E10).
4. **Robustness:** every included domain must meet the validity gate; an aggregate result may not mask a failing domain. No adoption decision may rely on the small skill-execution ablation as causal evidence (E07–E09).

Failure of any gate means no broad adoption. Passing permits adoption only for the tested domains, task families, rubric version, judge configuration, and operating conditions—not automatic generalization beyond them.

## Minimum controlled experiment

Conduct a preregistered, blinded, paired comparison on at least 300 previously unseen outputs spanning at least 3 materially different domains, with at least 100 outputs per domain. Obtain independent ratings from at least 3 qualified experts per domain and resolve the human reference by a prespecified consensus rule. The larger, multi-domain and multi-expert design is required because the present agreement result is confined to 92 Figma runs (E01, E02), human concordance relies on one Figma expert (E05), and readiness relies on 31 rated Figma tasks with that expert (E10).

Hold the outputs, judge models, prompts outside the rubric text, sampling settings, and scoring scale constant. Randomly assign and counterbalance generic versus skill-grounded rubrics; blind experts and automated judges to condition and study hypothesis; prevent the same judge context from seeing both rubric versions for an output. Freeze both rubrics before evaluation. Report paired confidence intervals, domain-stratified results, missingness, judge failures, and all exclusions.

To identify what produces any reliability change, include a factorial or staged ablation that changes one rubric component at a time—such as anchors, observability, grouping, and weights—because the original comparison bundled those changes (E01). Independently annotate whether required skills/process steps occurred; automated skill grades currently lack that independent process reference (E06).

If the program also wants to test whether supplying skills improves agent execution, run that as a separate randomized experiment with identical model, harness, integration, task distribution, and deployment rules across skill/no-skill arms, repeated sufficiently to power a prespecified effect. Do not infer that effect from the existing 7 paired runs, the +0.87 subset result, or the 2-of-7 no-skill deployments (E07–E09).

## Stop and reconsider conditions

Stop the pilot or prohibit consequential use if any of the following occurs:

- either automated-to-human validity estimate remains below the 0.40 gate, or its 95% lower confidence bound remains below 0.30;
- any domain fails the validity gate or shows systematic rank reversals despite acceptable aggregate agreement;
- the skill-grounded reliability advantage is below 0.10 or its paired 95% confidence interval includes zero;
- winner readiness is below 80% or its 95% lower confidence bound is below 70%;
- results depend materially on one judge model, one expert, one task family, or post hoc rubric changes; or
- component ablation shows that the apparent gain comes from a generic feature such as clearer anchors rather than skill grounding, in which case adopt the simpler validated feature—not the broader skill-grounded claim (E01, E02).

These conditions separate agreement from validity, relative preference from readiness, and exploratory execution effects from causal evidence. On the supplied evidence, a controlled pilot is the only proportionate decision.

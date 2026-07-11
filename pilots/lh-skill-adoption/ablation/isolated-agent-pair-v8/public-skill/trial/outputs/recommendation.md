# Recommendation: pilot with controls

## Decision

Run a controlled pilot; do not adopt skill-grounded scoring for production decisions yet.

The case for a pilot is meaningful but incomplete. In the reported 92-run Figma rubric comparison, mean pairwise quadratic-weighted kappa was 0.60 for expert rubrics and 0.46 for generic rubrics (E01, E02), while mean judge variance was 0.10 versus 0.25 (E03, E04). These results support a reliability hypothesis. They do not establish professional validity: individual-output human/LLM concordance was kappa 0.08 (E05), and individual-skill concordance was kappa 0.06 without independent human process annotation (E06).

Readiness evidence also argues against immediate adoption. Only 60 percent of pairwise-winning outputs met the single expert's score-at-least-4 threshold across 31 rated Figma tasks (E10). Thus relative wins cannot be treated as deployment readiness. Generalization is limited because this boundary came from one expert in one domain (E10).

The skill-execution evidence is hypothesis-generating, not causal evidence for adoption. The ablation comprised 7 paired runs over 3 tasks and bundled model, harness, and integration factors (E07). A reported aggregate gain of +0.87 for Codex came from only a subset of those 7 paired runs (E08). Likewise, 2 of 7 no-skill runs deployed, but that observation cannot separate procedure content from integration and stochasticity (E09). No claim that skill grounding caused better execution or scoring should be made from these results.

## Explicit decision threshold

Advance from pilot to adoption only if a preregistered held-out evaluation meets all of these gates:

1. **Reliability:** the lower bound of a 95% confidence interval for inter-judge quadratic-weighted kappa is at least 0.60, and skill-grounded scoring's kappa is non-inferior to the generic control by a margin of 0.05.
2. **Criterion validity:** against a blinded consensus label from at least two independent domain experts, the lower bound of the 95% confidence interval for human/LLM quadratic-weighted kappa is at least 0.40 at both output and skill levels.
3. **Absolute readiness:** at least 80% of outputs classified as passing by skill-grounded scoring also meet a preregistered expert readiness threshold, with the lower 95% confidence bound at least 70%.
4. **Robustness:** gates 1–3 hold separately in every included domain and for every evaluated model/harness configuration; no result may depend only on pooled averages.

These are prospective program decision rules, not estimates from the source pack. The validity gate is deliberately above the weak reported concordances of 0.08 and 0.06 (E05, E06), and the readiness gate is deliberately above the reported 60% boundary (E10).

## Minimum controlled experiment

Conduct a preregistered, blinded, randomized evaluation with the following minimum design:

- **Coverage:** at least 3 materially different domains, 2 model/harness configurations, and 100 independently sampled tasks per domain (300 tasks total). Use a held-out task set not used to author skills, rubrics, or prompts.
- **Factorial scoring arms:** score every output with (a) a generic rubric, (b) an expert-authored rubric with skill anchors removed, and (c) a skill-grounded rubric. Keep rubric count, grouping, weights, wording length, and observable evidence requirements matched where possible. This isolates skill anchors from the bundled rubric changes that limit the existing comparison (E01) and from expert authorship (E02).
- **Execution control:** separately randomize skill access on/off within each model/harness configuration, using repeated seeds and identical task inputs. Do not infer scoring validity from execution gains. This addresses the bundled and underpowered 7-run ablation (E07) and the integration/stochasticity ambiguity (E09).
- **Human reference:** obtain independent, blinded ratings from at least 2 qualified experts per domain; adjudicate disagreements by a prespecified rule. Experts rate both final-output readiness and process/skill execution without seeing automated scores. This directly addresses the single-expert limitation (E05, E10) and missing independent process annotation (E06).
- **Analysis:** preregister primary endpoints, confidence intervals, non-inferiority margins, multiplicity handling, exclusions, missing/deployment-failure treatment, and subgroup reporting. Report agreement, criterion validity, absolute readiness, and execution effects separately.

The task count is a minimum design requirement, not a claim of statistical sufficiency. Before launch, determine the final sample size by simulation or power analysis using the preregistered estimand, clustering, expected missingness, and the thresholds above; increase it if 300 tasks cannot provide the required precision.

## Stop and reconsider conditions

Stop the pilot or reject adoption if any of the following occurs:

- the criterion-validity or absolute-readiness gate fails in any domain or model/harness configuration;
- skill-grounded scoring increases agreement but does not improve validity against blinded expert consensus, because agreement alone is not professional validity (E03, E04);
- results reverse materially across domains, configurations, seeds, or rubric authors, consistent with the reported heterogeneous and bundled effects (E07);
- experts cannot reach a stable consensus reference or independent process labels cannot be obtained, leaving the core validity gap unresolved (E06);
- matching rubric construction removes the apparent advantage, indicating that authoring, wording, weighting, grouping, or observability—not skill grounding—explained the original contrast (E01, E02); or
- deployment failures or missing outcomes differ by arm enough to compromise the preregistered analysis, particularly because the existing 2-of-7 no-skill deployment observation is causally ambiguous (E09).

Until all adoption gates pass, pilot scores should be advisory only and must not determine benchmark rankings, public claims, or production-readiness decisions.

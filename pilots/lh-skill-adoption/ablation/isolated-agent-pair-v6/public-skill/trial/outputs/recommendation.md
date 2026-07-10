# Recommendation memo

## Decision

**Recommendation: pilot with controls.**

The evidence is promising on judge consistency but not yet adequate on professional validity, operational readiness, or causal impact. Expert-rubric agreement was reported at mean pairwise quadratic-weighted kappa 0.60 versus 0.46 for generic rubrics [E01, E02], and reported judge variance was 0.10 versus 0.25 [E03, E04]. Those are useful reliability signals, but they do not show that the grades are professionally correct [E03, E04]. The strongest validity checks point the other way: human/LLM concordance was kappa 0.08 for individual outputs [E05] and 0.06 for individual skills [E06].

The causal evidence is also too weak for a program-wide decision. The ablation comprised 7 paired runs over 3 tasks, with heterogeneous directional effects and model, harness, and integration factors still bundled [E07]. The reported Codex aggregate gain of +0.87 is therefore a hypothesis-generating result for one configured subset, not a stable general effect [E08]. Likewise, 2 of 7 no-skill runs deployed, but that difference cannot separate procedure content from integration or stochasticity [E09]. Finally, only 60 percent of pairwise-winning outputs cleared the single expert's >=4 readiness threshold, so relative wins cannot serve as an absolute readiness gate [E10].

## Explicit decision threshold

Advance from pilot to operational use only if one preregistered controlled experiment meets **all** of these gates:

1. **Reliability:** skill-grounded scoring achieves pairwise quadratic-weighted kappa **at least 0.60** and mean judge variance **no greater than 0.10** on held-out tasks. These are conservative replication gates based on the reported expert-rubric results, not universal standards [E01, E03].
2. **Professional validity:** independently aggregated expert judgments achieve kappa **at least 0.60** with automated grades for both output scores and skill/process scores. This is a proposed program threshold, deliberately much stronger than the observed output kappa 0.08 and skill kappa 0.06; it is not claimed as a threshold validated by the source study [E05, E06].
3. **Causal utility of the skill package:** the preregistered effect estimate for exposing agents to the skill procedure has a confidence interval whose lower bound is above zero on the primary quality endpoint, while deployment and completion are not worse than control. This gate is separate from scoring validity and is necessary because the existing 7-run ablation is underpowered and bundled [E07], the +0.87 result is subset-specific [E08], and deployment alone is causally ambiguous [E09].
4. **Absolute readiness:** more than the reported **60 percent** of outputs must clear a threshold fixed in advance by independent domain experts, with no material regression in any preregistered safety or quality stratum. The source result supplies the baseline warning, not a universal professional standard [E10].

Failure of any gate means the pilot does not justify operational use. Passing all gates supports a bounded rollout only in the tested domains and system configurations; transfer must be tested rather than presumed because the current evidence is scoped to Figma runs and specific harness/model systems [E01, E05, E07, E10].

## Minimum controlled experiment

Run one preregistered pilot with two linked but separately analyzed arms: an evaluator arm testing the scoring method and an agent arm testing the skill package. Use the following minimum design:

- **Evaluator arm:** score the same held-out outputs with skill-grounded and generic rubrics under blinded assignment. Hold authorship, item count, grouping, weights, anchor language, and observability constant except for the single rubric factor assigned in a comparison. The reported agreement contrast changed these together and cannot isolate expert authorship or skill grounding [E01, E02].
- **Agent arm:** use the same task, model, harness, integration path, budget, and run conditions within each pair; randomize only whether the agent receives the skill procedure. Replicate stochastic runs. This targets the bundled factors in the existing ablation and prevents deployment differences from being attributed to procedure content without control [E07, E09].
- Include **more than 7 paired runs over more than 3 tasks**, and require a prospective power analysis against a predeclared minimum meaningful effect to determine the final sample. Merely repeating the existing 7-run, 3-task scale is not acceptable because it is explicitly underpowered [E07].
- Include multiple model/harness configurations and report each stratum separately rather than relying only on an aggregate. The observed effects were heterogeneous, and the +0.87 result applies only to a configured Codex subset [E07, E08].
- Use at least **2 independent domain experts** per evaluated item, adjudicate disagreements under a protocol fixed before unblinding, and keep automated judges blind to treatment. The current human baseline relies on one Figma expert [E05, E10].
- Obtain independent human annotations for both final-output quality and process/skill execution. Do not treat judge agreement as validity, and do not use automated skill scores without independent process annotation [E03, E04, E06].
- Predeclare primary quality, deployment/completion, reliability, professional-validity, and absolute-readiness endpoints; publish paired and per-configuration results, uncertainty intervals, exclusions, and failures. Deployment is secondary evidence unless integration and stochasticity are controlled [E09].

## Stop or reconsider conditions

Stop the pilot or redesign it before further expansion if any of the following occurs:

- output or skill/process validity misses the proposed kappa 0.60 gate, especially if results remain near the observed 0.08 or 0.06 [E05, E06];
- the primary causal-effect interval includes zero, or apparent gains disappear when harness and integration are held constant [E07, E09];
- gains are confined to one configuration or reverse in a preregistered model/domain stratum, consistent with the existing heterogeneous evidence [E07, E08];
- absolute readiness does not improve beyond the reported 60 percent baseline, or relative winners continue to fail the fixed expert threshold [E10]; or
- agreement improves while independent expert validity does not, because lower variance and higher inter-judge agreement are not proof of professional correctness [E01, E03, E04].

This controlled pilot reconciles the positive agreement signal with the weak human concordance, limited readiness, and underpowered causal evidence without treating any one metric as dispositive.

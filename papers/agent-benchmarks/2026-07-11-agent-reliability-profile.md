# Paper Review: Towards a Science of AI Agent Reliability

- **Paper:** https://arxiv.org/abs/2602.16666v3
- **Authors:** Stephan Rabanser, Sayash Kapoor, Peter Kirgis, Kangheng Liu, Saiteja Utpala, and Arvind Narayanan
- **Date read:** 2026-07-11
- **Venue / source:** ICML 2026, PMLR 306; immutable arXiv v3 dated 2 June 2026
- **Local PDF:** `data/papers/pdfs/2602.16666v3-agent-reliability-profile.pdf` (52 pages; SHA-256 `f6347ad130f009ea385cfa341a32fd1c7d757d65458b4d1d73dae5c3a28a2ccf`)
- **Local text:** `data/papers/text/2602.16666v3-agent-reliability-profile.txt` (SHA-256 `56832d91ef486f2e6a18554f8a9c77b82cbf4b2545c1d67395daa97b3d326ce8`)
- **Linked implementation:** https://github.com/princeton-pli/hal-harness; source acquisition inspected commit `16bb03ebc11577fb5ea6dc8bb6c968387085e6aa`, but the paper does not identify its experiment commit, so this is not treated as exact paper-time code.
- **Tags:** reliability, repeated-trials, perturbations, calibration, safety, operational-profiles

## One-sentence contribution

The paper usefully separates mean success from repeatability, perturbation sensitivity, confidence quality, and violation severity through twelve metrics applied to 15 configured systems on GAIA and a cleaned τ-bench subset, but its five repeats are not demonstrably independent, several “semantic-preserving” and fault interventions are unvalidated or partly simulator-controlled, post-hoc confidence is not prospective prediction, and generic LLM severity weights do not license deployment-readiness claims.

## Why this matters for skill-bench

This work advances charter objectives A and C by showing that a benchmark response matrix should not collapse to mean artifact correctness. Two systems with equal task accuracy can differ in whether failure is task-specific or run-random, whether equivalent instructions change results, whether costs have heavy variance, whether the system can triage likely failures, and whether errors violate professional constraints. Those are distinct operational questions and should remain separate estimands.

Its deepest contribution is also its sharpest limit: reliability is conditional on an **operational profile**—task population, configured system, environment, intervention distribution, time window, and consequence model. The paper explicitly acknowledges that classical reliability requires a failure definition, exposure model, and bounded operating conditions (Appendix D.3, pp. 22–23), but its headline profile lacks a deployment exposure model. `skill-bench` should adopt the profile as a diagnostic response-matrix design, not as a universal scalar or certification proxy.

The two evaluated families are methodological cases, not a scope boundary. The reusable hypothesis is cross-domain: realistic knowledge-work evaluation needs repeated forms and controlled interventions whose meaning, equivalence, exposure frequency, and consequences are independently validated.

## Research question and claim boundary

The paper asks how agent reliability should be operationalized beyond average task success, whether reliability has improved alongside capability, and which dimensions remain weak. It synthesizes four dimensions from safety-critical engineering and reports twelve measures:

- **Consistency:** outcome, action-distribution, action-sequence, and resource consistency.
- **Robustness:** injected-fault, environment-format, and prompt-paraphrase robustness.
- **Predictability:** expected calibration error, AUROC discrimination, and Brier quality from post-hoc self-confidence.
- **Safety:** constraint-compliance frequency and conditional violation severity.

The experiment supports the bounded conclusion that these exact configured systems, on these two benchmark treatments and intervention implementations, exhibit materially different profiles that mean accuracy does not expose. It also supports the diagnostic observation that prompt robustness varies more than the tested fault/environment measures and that confidence discrimination is especially weak on τ-bench (Sections 4.2 and G.4–G.5, pp. 6–8, 37–49).

It does **not** establish a stable cross-domain reliability ordering, causal model-generation trends, prospective failure prediction, calibrated deployment risk, human-validated safety severity, or minimum deployment thresholds. The release-date regressions compare a small, provider-confounded convenience sample of models rather than controlled longitudinal versions.

## Methodology and system

### Benchmarks and configured systems

The study evaluates 15 models from OpenAI, Google, and Anthropic, dated March 2024 through May 2026 (Table 3, p. 29). GAIA uses all 165 validation tasks with a HAL ReAct-style generalist agent, web browsing, code, and files. τ-bench uses a benchmark-specific tool-calling scaffold and primarily the 26 airline tasks left after an external audit called 24 of 50 original tasks erroneous; Figure 6 contrasts the clean and original subsets (Sections 4.1 and F.1–F.2, pp. 5, 27–30).

Thus “model” comparisons are configured-system comparisons. Benchmark, scaffold, tools, timeouts, network state, and success oracle differ across GAIA and τ-bench. Each benchmark has one chosen scaffold, which the authors correctly list as a limitation (Appendix B, p. 17).

### Repeats and consistency

Each task is run five times. Non-reasoning endpoints use temperature zero; reasoning endpoints retain provider defaults because no temperature control is exposed. Error bars are ±1 standard error, clipped to [0,1] (Section 4.1, p. 5). The paper says different seeds are used, while temperature-zero variation is attributed to provider-side floating-point, batching, and kernel nondeterminism.

Outcome consistency averages `(2 p_t - 1)^2` per task. This is high both for repeated success and repeated failure, intentionally separating repeatability from capability. Action distributions use pairwise Jensen–Shannon divergence; action sequences use normalized Levenshtein distance. Resource consistency exponentiates the negative average coefficient of variation across resource types (Table 2, pp. 3–4).

This design is useful but the replicate unit is incompletely controlled. Live GAIA web state, concurrent provider load, endpoint routing, caches, retries, and task execution time can vary jointly. Seeds do not make proprietary calls independent, and five runs provide weak tail or per-task variance estimates. Pairwise trajectory comparisons also reuse each trajectory in four pairs, so treating pairwise values as independent would understate uncertainty; the manuscript does not describe cluster-aware inference.

### Robustness interventions

For each task, GPT-4o generates five cached paraphrases. Four strength prompts range from mild to “naturalistic,” but primary results use naturalistic variants. Outputs shorter than ten characters are filtered; no independent semantic-equivalence annotation, contradiction audit, or difficulty-equivalence study is reported (Section F.3.1, pp. 30–31).

Fault injection applies independently to wrapped calls with probability 0.2. Seven fault labels are sampled; an internal recovery draw rises from 0.3 to 0.7 over three attempts before returning the synthetic fault (Table 5 and pseudocode, pp. 31–32). This means measured `R_fault` is not solely the agent’s response to faults: the wrapper probabilistically resolves faults on the agent’s behalf. The fault distribution and recovery curve are asserted rather than estimated from a production exposure profile.

Environment perturbations alter formatting, key names, nesting, parameter names, and tool responses; τ-bench mappings are reversed before execution so underlying semantics should remain fixed. GAIA’s environment treatment also modifies question text and injects irrelevant context, overlapping prompt robustness and potentially changing search behavior (Table 6 and examples, pp. 32–33). The ratio `Acc_perturbed / Acc_baseline`, clamped at one, hides improvements and is unstable when baseline accuracy is low.

### Predictability

After task completion, the same agent receives its full trajectory and reports a confidence number from 0–100. Parse failures trigger a heuristic based on execution error count (Section F.3.4, pp. 33–34). ECE, AUROC, and one-minus-Brier are then computed.

This is retrospective self-assessment, not prospective prediction. The agent already knows its observed tool errors and trajectory, and the fallback leaks an evaluator-authored error heuristic into the metric. It can test whether a completed run emits a useful acceptance signal, but cannot establish whether pre-run task routing, early escalation, or a frozen external monitor predicts failure. ECE bin count and small-bin handling are not stated in the metric table, while figures visibly include sparse bins.

### Safety and aggregation

GPT-4o judges full traces against benchmark-specific constraints, citing evidence and assigning severity. A second prompt identifies errors on a 0–10 scale. Scores are remapped to low/medium/high weights 0.25/0.5/1.0; per task, the maximum violation severity is retained. Compliance measures violation-free frequency, while harm is one minus mean severity conditional on a violation (Section F.3.5, pp. 34–36).

No human validation, inter-rater reliability, judge-repeat analysis, blind adjudication, or domain loss calibration is reported. The prompt calls wrong output “low,” PII/security/data-integrity errors “high,” and destructive operations “critical,” but the final remapping collapses informational/critical boundaries and uses generic weights. These are rubric choices, not measured financial, legal, safety, or remediation consequences.

Within dimensions, equal-weight aggregates are used. Overall `R` equally averages consistency, predictability (Brier only), and robustness, while safety is excluded as a hard constraint (Section 3.5, pp. 4–5). This is a defensible dashboard convention, not a validated latent scale. Notably, the prose says twelve metrics, while Table 2 presents four consistency + three robustness + three predictability + two safety measures; the displayed consistency dimension includes outcome, two trajectory views, and resource consistency.

## Evidence and results interpretation

The empirical results are strongest as profile demonstrations. Outcome consistency remains moderate even for frontier systems; distributional action consistency is usually higher than sequence consistency, the paper’s “what but not when” pattern (Figures 2 and 11, pp. 6, 43). GAIA resource consistency is lower than τ-bench, consistent with an open web/tool environment, but this bundles model behavior with mutable external latency/content.

Fault and environment robustness mostly cluster near one, while prompt robustness varies substantially (Figure 17, p. 49). The authors appropriately interpret the former as ceiling effects under a limited perturbation suite, not proof of broad robustness (Section G.5, p. 38). A further threat is mechanical: clamping ratios at one discards beneficial intervention effects, and wrapper-side fault recovery weakens treatment intensity.

Predictability separates calibration from discrimination. Newer systems can match aggregate success frequency while failing to rank which individual runs will succeed. On τ-bench most AUROCs are near random; the manuscript highlights only modest selective ability for two Claude systems (Figures 14 and 16, pp. 46, 48). This is valuable evidence against equating calibration with actionable deferral, though all signals are elicited after execution.

The safety results identify financial-accuracy violations as common on τ-bench and fewer violations in recent frontier systems (Figure 5, p. 8). Because one unvalidated LLM judge supplies both compliance and severity, rare high-severity claims lack trustworthy uncertainty. Conditioning severity on observed violations also makes comparisons unstable when a system has very few violations.

The headline that reliability gains lag accuracy is descriptive, not causal. Release-date slopes use 15 nonrandom models with provider, size, reasoning mode, endpoint policy, and chronology confounded. GAIA reliability’s date trend is weak (`r=0.46`, slope 0.03/year, reported `p=0.08`), while τ-bench is stronger (Figure 8, p. 40). The paper does not report clustered confidence intervals over tasks/runs, correction for many metric/model comparisons, or sensitivity to weights.

## Unique insight

The strongest transferable insight is that **reliability is a conditional response surface, not a trait score**.

A useful profile indexes behavior by:

`configured system × task/form family × environment version × intervention type/intensity × exposure distribution × time × consequence model`.

The paper supplies several slices of this surface but then compresses them. For `skill-bench`, compression should occur only after the intended use defines which variation is nuisance and which is construct-relevant. Diverse solution paths may be desirable in ideation but unacceptable for a regulated state transition. A paraphrase may be equivalent linguistically but remove a professional cue experts legitimately use. A schema rename may preserve database semantics while changing a real integration contract. A retry may represent robust recovery or consume an unacceptable latency budget.

This reframes “robustness”: every perturbation must carry a **preservation claim** and evidence that it leaves the intended requirement and difficulty invariant, plus an **exposure claim** about how often and where it occurs operationally. Without those, a ratio measures sensitivity to an authored treatment, not reliability under deployment conditions.

A second insight is that predictability requires a decision point. Post-hoc confidence can support acceptance/review of a completed artifact; it cannot automatically support pre-task routing or early intervention. The metric record must bind signal time, evidence available then, action policy, threshold, loss, and outcome horizon.

## Limitations and validity threats

1. Two benchmark families and one scaffold per family cannot establish cross-domain reliability.
2. The 26-task clean τ-bench subset is small; subset selection changes the target population.
3. Five repeats are insufficient for tail behavior and unstable per-task consistency.
4. Proprietary endpoint runs are not demonstrably independent; seeds do not control serving nondeterminism, caching, or correlated outages.
5. Temperature differs structurally between reasoning and non-reasoning endpoints.
6. Live GAIA web state makes nominal repeats environmentally non-identical.
7. Standard errors do not visibly account for task, repeated-run, and pairwise-comparison dependence.
8. Outcome consistency rewards deterministic failure; it must never be read without accuracy.
9. Action-sequence similarity can punish valid procedural diversity and ignores action semantics/arguments.
10. Resource coefficients of variation are unstable near zero means and the included resource set/conditioning is not fully specified in the main metric table.
11. GPT-4o paraphrases lack independent semantic and difficulty validation.
12. Naturalistic typos or implicit wording may remove cues rather than preserve exact meaning.
13. GAIA “environment” changes overlap prompt intervention and search-strategy changes.
14. Fault frequency/type weights are not production-estimated.
15. Wrapper-side probabilistic recovery partly measures the injector, not agent recovery.
16. Robustness ratios are unstable at low baseline accuracy and clamping suppresses improvements.
17. Post-hoc confidence is not prospective predictability.
18. Confidence parse fallback uses evaluator-authored error counts and changes the signal definition for invalid outputs.
19. ECE binning and sparse-bin uncertainty are under-specified.
20. Safety labels and severities rely on one unvalidated LLM judge.
21. Generic severity weights are not domain consequence or expected-loss estimates.
22. Maximum-per-task severity discards multiplicity and accumulated harm.
23. Conditional harm is unstable and undefined in the no-violation edge case unless explicitly handled.
24. Equal-weight aggregates lack psychometric or decision-theoretic validation.
25. Safety is excluded from `R`, so the headline reliability scalar is explicitly incomplete.
26. Release-date trends are observational and heavily confounded.
27. Multiple metric/model/trend comparisons lack multiplicity treatment.
28. Costs are logged, but total experimental cost and missing/invalid run counts are not reported.
29. Retry and timeout policies can censor hard runs and alter both resource and success estimands.
30. Paper-time code is not pinned; the inspected July commit postdates v3 and cannot prove exact implementation.
31. The analogy to aviation/nuclear practice supplies design motivation, not transferable certification thresholds.
32. No operational exposure distribution, deployment loss model, incident base rate, or external validation supports readiness claims.

## Reproducibility and operational realism

Reproducibility is moderate at the protocol level and weak for exact regeneration. The immutable paper gives formulas, prompts, model list, benchmark subsets, hyperparameters, perturbation categories, fault pseudocode, judge constraints, and many per-model figures. The linked HAL repository contains relevant reliability machinery at the inspected commit. However, the manuscript does not pin an experiment revision or preserve a complete immutable run manifest; proprietary model aliases, web results, provider serving behavior, and future model dates make exact replay impossible. Missing/invalid-run handling, task order/concurrency, ECE bins, complete resource definitions, total cost, judge versions, and all seeds are not reported.

Operational realism is mixed. Repeated agent runs, live web variability, tool faults, API-format changes, costs, full traces, and policy violations are genuine deployment concerns. Yet the perturbation distributions are authored rather than empirically sampled, the injector sometimes recovers faults itself, confidence arrives only after completion, and severity has no human/domain calibration. The protocol is best viewed as a broad conformance battery that discovers failure signatures, not an estimated reliability guarantee over a real operating envelope.

## Transferable changes for skill-bench

1. **Preserve a reliability profile, not one score.** Use existing metric-monitoring records for separate accuracy, repeatability, resource variance, intervention effects, confidence quality, violation frequency, and consequence severity. Any aggregate must reference an intended use and validated weighting/loss basis.
2. **Bind every estimate to an operational-profile record.** Record task/form population, configured-system hashes, environment, time window, retries/timeouts, network state, unit, clustering, missingness, and exposure distribution. Existing metric, task-health, execution, and validity contracts are the right homes.
3. **Add perturbation preservation evidence.** Each prompt/environment/fault variant should identify the transformed loci, preservation claim, independent review or metamorphic invariant, applicability boundary, intensity, and source/exposure rationale. Invalid variants are instrument defects, not agent failures.
4. **Use matched hierarchical uncertainty.** Predeclare paired baseline/intervention runs; cluster by task and form family; preserve every invalid/provider-failed run; report task-level heterogeneity rather than only ratios of pooled accuracy. More repetitions are needed for tail or per-task claims.
5. **Separate recovery loci.** Trace injected fault, delivery to agent, wrapper retry, agent retry/fallback, recovery, cost/latency, and final consequence. A harness-resolved fault cannot count as agent robustness.
6. **Bind predictability to decision time.** Distinguish pre-task routing, in-run escalation, and post-artifact acceptance signals. Store the evidence view, confidence method/fallback, threshold, coverage, false-intervention/missed-failure loss, and frozen calibration population.
7. **Calibrate consequence models by domain.** Keep constraint occurrence, grader evidence, severity, reversibility, remediation effort, stakeholder harm, and decision loss separate. Require expert/human validation and judge reliability before readiness use.
8. **Treat consistent failure as diagnostic only.** Cross-tab outcome consistency with capability, failure root, and task family. A stable zero is useful for debugging but never a positive readiness signal.
9. **Reuse existing contracts; add no queue task.** The benchmark bundle, artifact-view admissibility, metric-monitoring, task-health, validity-argument, execution-isolation, and longitudinal records can absorb these requirements. The evidence does not justify another schema.

## Action items for repository

- [x] Read and preserve the full immutable v3 PDF and extraction.
- [x] Reconstruct all twelve metrics, configured systems, repeated-run design, perturbations, confidence protocol, safety judging, aggregation, and evidence with page/section anchors.
- [x] Distinguish diagnostic response profiles from operational reliability and deployment certification.
- [x] Identify independence, preservation, prospective-signal, severity-calibration, uncertainty, missingness, and revision-provenance limits.
- [x] Map nonduplicate requirements into existing contracts; add no build task.

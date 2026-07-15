# Paper Review: Who&When Pro — Failure-Attribution Validity

- **Paper:** https://arxiv.org/abs/2607.09996v1
- **Authors:** Jiale Liu, Huajun Xi, Shaokun Zhang, Yifan Zeng, Tianwei Yue, Chi Wang, Jian Kang, Qingyun Wu, and Huazheng Wang
- **Date read:** 2026-07-15
- **Version read:** immutable arXiv v1, submitted 10 July 2026
- **Local PDF:** `data/papers/pdfs/2607.09996v1-whowhen-pro.pdf` (36 pages; SHA-256 `50ee0997c80913b7cd9d7946da9e0d583e0177f3791bfa236aec72673054417a`)
- **Local text:** `data/papers/text/2607.09996v1-whowhen-pro.txt` (SHA-256 `e32743534e8273230502ea47f06002caaa88f0b7c15652bcf037f6cf50a4178f`)
- **Official code repository inspected:** https://github.com/whowhenpro/whowhen_pro/tree/db3946cae6895c8056b9b482c283fc3949a6654f
- **Official project repository inspected:** https://github.com/whowhenpro/whowhenpro.github.io/tree/9c3046586bcfee8fbf103db4f3c06ecfcafc156d
- **Release provenance:** `data/sources/releases/2607.09996v1-whowhen-pro/provenance.json`
- **Important version/release boundary:** both official commits are dated 12 July, two days after v1. The code archive contains only a README and illustration; its README says code and data are coming soon. The website archive contains six illustrative traces. Neither is the paper-time implementation or the claimed 12,326-row corpus.
- **Tags:** failure-attribution, controlled-injection, causal-identification, trajectory-observers, root-surface, synthetic-faults, release-validity

## One-sentence contribution

Who&When Pro turns successful agent trajectories into 12,326 reported failures by replaying a prefix, injecting one taxonomy-conditioned action, retaining continuations that fail, and asking LLM auditors to identify the responsible agent, step, and error mode; this gives strong labels for **which intervention the generator inserted**, but not automatically for the earliest sufficient cause of a natural failure, and the absent benchmark/code release prevents auditing the claimed construction correspondence.

## Why this matters for skill-bench

The benchmark addresses a central `skill-bench` objective: a useful knowledge-work evaluation should explain why an artifact or workflow failed rather than stop at a red check. Its controlled contrast is substantially better than post-hoc storytelling over an arbitrary failed trace. A successful seed proves one path worked; exact prefix replay limits pre-intervention drift; the injected action gives a known locator and actor; and downstream execution exposes propagation into a failed outcome.

The paper also reveals the validity ceiling of synthetic root-cause labels. The intervention is known because the generator chose it. That does not prove that the injected action is the unique or earliest sufficient cause under the paper's own counterfactual definition, that the assigned taxonomy mode is uniquely correct, or that auditor performance transfers to naturally occurring, interacting, recoverable, or environment-induced failures. For `skill-bench`, the reusable object is therefore an **intervention-to-consequence evidence chain**, not a generic `root_cause = injected_step` rule:

`valid successful seed → replay-equivalent prefix → declared injected delta → realized agent exposure → first observed divergence → downstream propagation → surfaced artifact/check failure → recovery/counterfactual evidence → alternative sufficient causes → observer view → attribution judgment → licensed claim`

This advances charter objectives A, B, and C through diagnostic-validity evidence. It does not narrow the project to multi-agent systems, QA, or synthetic fault injection.

## Research question and claim boundary

The paper asks whether LLMs can attribute failures across text, image, and video agent traces at much larger scale than prior benchmarks, and how attribution varies by modality, protocol, model family, trace length, ground-truth-answer access, and cost.

The evidence supports these bounded claims:

- the authors specify a pipeline that starts from successful trajectories, replays a prefix, injects one generated action, and retains failed continuations (pp. 3–5);
- the reported corpus has 12,326 retained traces from 26 benchmarks, 15 frameworks, nine task categories, three modalities, and 18 authored failure modes (pp. 2, 5, 17–28);
- under the reported all-at-once prompts and corpus labels, ten configured judge models have markedly different agent, exact-step, mode-macro-F1, and joint scores (p. 6);
- on a reported 1,444-trace stratified subset, full-trajectory prompting usually outperforms sequential and binary localization, while ground-truth answers can help perception labels and hurt reasoning labels (pp. 7–8, 18);
- three annotators reviewing 100 selected traces usually accepted generated step, agent, and family labels, with reported family-level Fleiss κ of 0.73 (p. 5).

It does **not** establish exact causal-root truth, unique necessity or sufficiency of the injected action, realism or prevalence of the 18 modes in natural failures, full prefix-state equivalence, general auditor accuracy, transfer to multi-cause failures, professional diagnostic validity, correction utility, improved agent behavior, production readiness, or reproducibility of the paper tables.

## Methodology and system

### Source trajectories and outcome conditioning

The authors run 15 frameworks over 26 source benchmarks, log task inputs, messages, observations, and intermediate artifacts, and grade final answers with official evaluators where available. Successful runs become injection seeds. Naturally failed runs are used only to develop the taxonomy and per-(agent, benchmark) applicability profiles (pp. 3–4).

This creates two selection gates before any auditor is evaluated:

1. the base configured agent must first succeed, so source tasks and trajectory styles are conditioned on seed success;
2. after injection, only continuations that end in task failure survive, so the benchmark is conditioned on successful fault induction.

The 12,326 rows are therefore not a sample of natural agent failures or even all attempted injections. They represent `successful seed × eligible generated intervention × failed continuation × passed filters`. The paper does not report seed attempts, base successes, candidate injection attempts, replay aborts, generated-action rejects, non-failing injected continuations, filter losses, or retained rates by benchmark/mode. Framework, modality, mode, and position frequencies cannot be read as failure prevalence.

### Taxonomy and label authority

Ph.D.-level reviewers inspect sampled natural failures for each (agent, benchmark) pair, identify what they regard as the earliest decisive error, consolidate recurring patterns into six families and 18 modes, and define where each mode plausibly applies. The families are perception, reasoning, planning, action, verification, and coordination; each generated trace receives exactly one mode (pp. 4, 16–18).

The expert contribution is important but under-specified. The paper gives no reviewer count for taxonomy development, disciplines, training, assignment, number of natural traces sampled, coding protocol, independent labels, disagreement ledger, saturation criterion, mode revision history, or coverage by framework. Several categories overlap at causal boundaries: task misunderstanding versus ineffective planning, reasoning versus inadequate verification, hallucination versus context loss, and orchestration versus communication. Forcing one label erases co-causes and nested descriptions.

The taxonomy is a useful authored vocabulary, not an empirically exhaustive ontology. The authors acknowledge non-exhaustiveness (p. 15), but their broader language of externally verified step-level labels and shared failure vocabulary exceeds the reported authority.

### Injection construction

For a successful seed `τ`, the pipeline selects a mode-compatible step `t`. A frontier model generates an adaptive injection prompt using the task, answer, observations, and target mode; that prompt is appended to the original base agent call so the base model produces an on-style erroneous action. The original framework then continues from `t+1` (p. 4; Appendix K).

The released appendix provides complete templates only for hallucination and reasoning error, not all 18 modes (pp. 32–36). Those templates actively constrain the action: the hallucination prompt instructs the agent to ignore contradictory observations, search in support of a fabricated claim, and not answer yet; the reasoning prompt specifies the confusion and requires another search. These are controlled red-team treatments, but their explicitness can create construction signatures unlike spontaneous mistakes. A judge may detect prompt-engineered discourse shape rather than natural causal diagnosis.

The frontier generator sees the reference answer. Generation, eligibility, and post-hoc failure selection jointly optimize for a wrong endpoint. This is useful for producing diagnostic contrasts, but it further separates the retained distribution from ordinary errors.

### Replay fidelity

For static web/search tools, raw outputs are cached by canonicalized parameters and replayed. For `web_visit_and_summarize`, only raw page content is cached; the secondary LLM summary is regenerated. For live browser/filesystem systems, recorded actions are executed on fresh instances and attempts are aborted on exceptions; the appendix reports Bing DOM rotation as a common replay failure and a URL fallback for search input (pp. 5, 23–24).

This repairs obvious pre-injection action drift but does not prove full state equivalence:

- regenerated summaries can change the pre-injection observation context even when raw bytes are fixed;
- exact recorded actions do not imply identical hidden browser, filesystem, service, clock, or credential state;
- the described browser check emphasizes action exceptions, not a complete pre-state hash or semantic state comparison;
- retrying another slot after a replay abort changes the retained injection population;
- model/provider versions, sampling settings, seeds, cache manifests, environment images, and replay timestamps are not reported in an inspectable run ledger.

The project page says every pre-injection step matches the seed and calls the injected step “provably” decisive. The methods support a narrower statement: the pipeline attempts recorded-prefix action replay and filters some visible divergence.

### Why the injected step is not automatically the causal root

The paper defines the decisive step as the earliest action whose correction would turn a failed trajectory into success (p. 3). It then argues that because reverting the injected action recovers the successful seed, `t` is decisive by definition (p. 4).

That inference conflates two counterfactuals:

- **observed seed:** original `a_t` followed by the original successful suffix;
- **injected run:** altered `ã_t` followed by a newly sampled suffix.

The study does not report replaying `a_t` under the same reconstructed state and fresh continuation, repeated paired suffixes, repairing only `ã_t` inside the failed branch, or testing alternative corrections. With stochastic agents and environments, the original seed demonstrates one sufficient successful path, not that correction of `ã_t` would make the observed failed branch succeed. The injected action is certainly the controlled treatment. It may be a but-for cause for one paired construction under stronger replay assumptions. Unique necessity, earliest sufficiency, and natural root cause require additional interventions.

Recoverability matters too. An injected error can be detected and repaired before the endpoint; such runs are dropped because they do not fail. Conversely, a later independent mistake may be necessary for the retained final failure. Conditioning on endpoint failure enriches unrecovered propagation, not root-cause uniqueness.

### Human review

Three independent annotators review 100 traces stratified across modality and error family. They see the task, reference answer, full trajectory, and generated label, then accept, correct, or mark no clear decisive error. Majority acceptance is 94% for step, 90% for mode, and 90% for responsible agent on multi-agent traces; 2% receive majority “no clear” and family-level Fleiss κ is 0.73 (p. 5).

This is useful face-validity evidence, but limited:

- 100 rows are about 0.8% of the claimed corpus;
- the sampling allocation, random seed, inclusion probabilities, and mode/framework coverage are absent;
- generated labels are visible, so acceptance is not a blind independent annotation task;
- only family agreement receives κ; exact-step and agent agreement are not reported;
- majority acceptance does not establish each label's precision, taxonomy completeness, or counterfactual causality;
- no correction/adjudication lineage is released or shown to update the other 12,226 rows;
- annotators see the answer and full outcome, while the primary judge condition withholds the answer.

The 90–94% figures validate recognizability of selected injected cases better than causal-root truth.

### Auditor protocols, information views, and metrics

All-at-once shows the complete transcript and asks for agent, exact step, mode, and rationale. Step-by-step reveals prefixes and stops at the first flagged step. Binary search shows contiguous slices and asks which half contains the error. Each can optionally receive the reference answer (pp. 5, 29–32).

These are not just search algorithms; they are different observer-information and decision policies. Step-by-step cannot revise after later evidence. Binary slices can omit dependencies. All-at-once sees post-error consequences that may expose the treatment. Their score differences therefore estimate configured protocol effects, not one underlying auditor ability.

The four metrics are responsible-agent accuracy on multi-agent traces, exact-step accuracy, mode macro-F1, and all-correct joint accuracy. They are properly kept separate in the main table. Yet:

- no confidence intervals, task/benchmark-clustered bootstrap, hypothesis tests, or repeated judge calls accompany model comparisons;
- macro-F1 over authored modes does not resolve mode ambiguity or class-dependent label quality;
- agent accuracy uses a topology-conditioned denominator while joint mixes requirements across single- and multi-agent traces;
- exact-step scoring treats adjacent and semantically bundled steps as wrong, even though Step@1 gains are especially large for video (pp. 19–22);
- model endpoint dates, temperatures, seeds, parsing failures, invalid outputs, retries, and missing-row policies are not specified in the paper or released code.

The reported table is descriptive configured-judge performance against generated labels, not a stable model trait ranking.

## Evidence and result interpretation

### Main results

Across ten reported models, best exact-step accuracy is 73.9% on text, while best error-mode F1 is 22.2% on text, 29.5% on image, and 40.0% on video. Joint scores are much lower. Step localization decreases with longer traces; mode confusion often maps planning, verification, and coordination to reasoning (pp. 6–7).

Those patterns are plausible and diagnostically relevant, but they combine source benchmark, framework, mode, injection position, trace length, model backbone, and modality. Text, image, and video are not matched renderings of the same tasks or faults. For example, video is overwhelmingly contributed by EVA, while text and image have different framework mixtures (p. 23). A modality difference is therefore a suite interaction, not a causal modality effect.

The paper interprets planning/verification/coordination-to-reasoning confusion as surface-symptom classification rather than causal tracing. The generated label can support that interpretation in illustrative cases, but no released dependency graph, alternate-cause annotation, or repair intervention verifies it corpus-wide.

### Protocol and answer-access ablations

On the 1,444-row subset, all-at-once has the highest joint score for eight of ten models and exceeds step-by-step exact-step accuracy by a reported 7.6 points (pp. 7, 18). The subset is called representative because it preserves modality and error-category distributions, but no selection seed, task/framework balance, or uncertainty is supplied.

Providing the reference answer improves some perception classifications and degrades or barely changes some reasoning classifications. The paired case studies convincingly illustrate answer anchoring: judges focus on endpoint mismatch and skip an earlier generated fault (pp. 8, 15–17). This is a valuable warning for `skill-bench`: answer-bearing grader context is an intervention, not harmless extra evidence. However, the plotted domain/framework cells are descriptive; the paper does not report repeated calls, paired uncertainty, or a factorial model separating framework, domain, mode, and trace.

### Cost

The paper prices hosted models by provider token rates and open-weight models by OpenRouter rates, then plots cost per 1,000 traces against joint accuracy on the subset (pp. 7–8). This supports an approximate inference-cost comparison for those calls. It excludes data construction, failed injection attempts, replay/environment execution, cache/storage, human taxonomy/review labor, engineering, and correction utility. It is not total diagnostic cost or cost per valid root cause.

## Release audit and reproducibility

The paper states, “We release all traces, labels, and evaluation code” (p. 15). The inspected official code commit says the opposite operationally: evaluation code, benchmark data, dependencies, reproduction scripts, model configurations, prediction format, paper, and citation are all “coming soon.” Its archive has one 2,959-byte README and one figure.

The separately pinned project-site archive contains six illustrative JSON traces and display code. The six files cover one LVBench/EVA trace, one HumanEval/MacNet trace, three MMSearch/smolagents traces, and one SimpleQA-Verified/Magentic-One trace. They are not a representative row sample and do not include the generation/evaluation pipeline or paper result tables. Their schemas vary by framework. Injection markers are explicit in some examples but absent or encoded differently in others, reinforcing the need for a normalized released contract before paper–data counts and labels can be audited.

Consequently, this review could not verify:

- 12,326 row count or benchmark/framework/mode distributions;
- seed-to-injected row correspondence;
- prefix byte/state equality;
- injection eligibility and attempt denominators;
- all 18 generation templates;
- post-hoc filters and leakage detection;
- evaluator prompts as executed, model configurations, parsed predictions, or invalid rows;
- the 100-row human sample and labels;
- the 1,444-row ablation subset;
- any reported score, uncertainty, cost, or confusion matrix.

The paper is methodologically detailed in prose, but the benchmark is not operationally inspectable at the audited commits.

## Unique insight

The strongest insight is a distinction the paper approaches but does not fully enforce:

> **Intervention identity is not causal-root identity.**

A controlled injection gives unusually strong evidence about what changed and where. That is one rung above post-hoc diagnosis. But a useful benchmark must type the claim:

1. `injected_delta`: the generator altered action `t`;
2. `first_observed_divergence`: the earliest measured state/trace difference;
3. `propagated_surface_failure`: the later artifact/check symptom;
4. `but_for_effect_under_replay`: replacing the delta changes outcome under a declared paired policy;
5. `earliest_sufficient_cause`: no earlier supported cause and correction at this locus suffices;
6. `natural_failure_root`: attribution for an unmanipulated failure with possibly interacting causes;
7. `repair_utility`: acting on the diagnosis improves held-out outcomes without new harms.

Who&When Pro directly labels rung 1, attempts to stabilize the prefix needed for rung 4, and observes a failed endpoint. It does not generally establish rungs 4–7. This typed ladder prevents synthetic “golden root cause” from being laundered into production debugging truth.

## Limitations and validity threats

1. Base trajectories are conditioned on configured-agent success.
2. Retained traces are conditioned on generated interventions producing endpoint failure.
3. Injection attempts, replay aborts, non-failing continuations, and filter losses are unreported.
4. The retained distribution cannot estimate natural failure prevalence.
5. Taxonomy development sample size, reviewer protocol, authority, agreement, and saturation are absent.
6. Eighteen mutually exclusive modes overlap causally and descriptively.
7. Only two complete injection templates are shown.
8. Frontier-model prompts can create detectable construction style.
9. The reference answer influences generation and selection.
10. Raw-page caching does not freeze regenerated LLM summaries.
11. Recorded action replay does not prove complete hidden-state equivalence.
12. Browser fidelity checks are not a complete semantic state attestation.
13. The original successful suffix is not a paired repair of the injected failed branch.
14. Stochastic continuation prevents “correction would succeed” from following from one successful seed alone.
15. No alternative correction, necessity, sufficiency, recovery, or multi-cause intervention study is reported.
16. Endpoint-failure filtering drops recovered injections and enriches unrecovered propagation.
17. The 100-row human sample is small, label-visible, and under-specified.
18. No exact-step or agent inter-rater agreement is reported.
19. Human corrections are not shown to propagate into the full corpus.
20. Observer protocols alter available information and revision rights.
21. Modality is confounded with benchmark, framework, mode, length, and backbone.
22. No repeated judge calls or clustered uncertainty support rank differences.
23. Invalid outputs, retries, missingness, parsing, seeds, and endpoint versions are under-specified.
24. Cost omits benchmark construction, environment execution, human labor, and repair value.
25. The paper's release claim conflicts with the official code README at the audited commit.
26. No full corpus, generation code, evaluation code, predictions, or result bundle was released for audit.
27. Six website examples cannot establish paper–release correspondence.
28. No professional, operational, or downstream repair study validates diagnostic utility.

## Transferable design patterns for skill-bench

### Retain

1. **Start from a verified successful witness.** A valid seed is stronger than inventing a failure without a known workable path.
2. **Record intervention locus and actor explicitly.** Preserve exact before/after payloads rather than an analyst summary.
3. **Attempt prefix replay and fail closed on divergence.** Cache mutable observations and attest state before scoring attribution.
4. **Keep who, when, what, and joint scores separate.** Do not hide distinct diagnostic failures in one scalar.
5. **Compare observer information policies.** Full trace, prefix-only, answer-bearing, and answer-withheld are different instruments.
6. **Inspect surface/root confusion.** Planning or verification failures surfacing as reasoning mistakes is a useful diagnostic hypothesis to test with interventions.

### Repair

1. Rename injected labels as `construction_intervention` unless paired repair establishes a stronger causal claim.
2. Preserve seed, replay, injection, continuation, evaluator, and environment identities/hashes in one lineage record.
3. Record all attempted injections and dispositions: ineligible, replay-diverged, generation-invalid, recovered, failed, filtered, and retained.
4. Verify full pre-state equivalence, including regenerated summaries and hidden environment state, or mark the trial invalid/partially observed.
5. Run matched repair and sham controls with repeated suffixes: original action, injected action, corrected alternative, no-op perturbation, and unrelated perturbation.
6. Allow multiple candidate causes, dependency edges, confidence, unresolved alternatives, and root-versus-surface labels.
7. Calibrate auditors on both injected and independently annotated natural failures, with blinded labels and clustered uncertainty.
8. Measure whether diagnosis-guided repair improves held-out outcomes, cost, safety, and artifact quality—not only label recovery.

## Concrete repository actions

No new schema or build task is warranted. Existing benchmark-bundle trace events, root/surface labels, intervention records, recovery edges, invalid-trial handling, task-health lifecycle, evidence-view admissibility, metric specifications, and validity arguments can represent the required chain.

The next empirical diagnostic slice should use those existing objects on one current artifact-heavy pilot:

- freeze one successful task state and complete evidence views;
- plant one upstream evidence-selection error and one later surface artifact defect;
- cross original, injected, repaired, sham, and dual-fault continuations with repeated seeds;
- ask auditors under prefix-only, full-trace, and answer-bearing views;
- score injected-delta recovery, first-divergence localization, supported causal slice, unresolved alternative causes, and repair success separately;
- retain every invalid, recovered, and failed attempt rather than selecting only endpoint failures.

Useful completion is not high auditor accuracy. It is evidence about which attribution rung each observer can support and whether acting on that diagnosis repairs a consequential artifact without collateral regressions.

## Bottom line

Who&When Pro contributes a valuable controlled-construction idea and a broad reported stress test for automated failure auditors. Exact prefix replay plus one known action delta is materially better evidence than unconstrained post-hoc explanation, and the answer-access examples sharply demonstrate evaluator anchoring.

Its central causal wording is too strong. The pipeline knows the inserted treatment, not necessarily the unique earliest sufficient cause of the newly sampled failed continuation. Success-conditioned seeds, endpoint-failure selection, incomplete state equivalence, single-mode labels, a small label-visible human check, modality/framework confounding, absent uncertainty, and an unreleased corpus/codebase keep the evidence at synthetic intervention-recognition validity. `skill-bench` should retain controlled deltas and typed observer views while requiring paired repair, alternative-cause tests, full attempt denominators, and strict claim ladders before calling any label a causal root or using it to drive benchmark learning.

## Source and release links

- Immutable abstract: https://arxiv.org/abs/2607.09996v1
- Immutable PDF: https://arxiv.org/pdf/2607.09996v1
- Project page: https://whowhenpro.github.io/
- Official code repository: https://github.com/whowhenpro/whowhen_pro
- Inspected code commit: https://github.com/whowhenpro/whowhen_pro/tree/db3946cae6895c8056b9b482c283fc3949a6654f
- Official project repository: https://github.com/whowhenpro/whowhenpro.github.io
- Inspected project commit: https://github.com/whowhenpro/whowhenpro.github.io/tree/9c3046586bcfee8fbf103db4f3c06ecfcafc156d
- Local provenance: `data/sources/releases/2607.09996v1-whowhen-pro/provenance.json`

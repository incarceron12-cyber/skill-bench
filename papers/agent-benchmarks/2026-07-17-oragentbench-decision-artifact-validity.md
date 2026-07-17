# ORAgentBench: executable decisions are the right endpoint, but one calibrated oracle gap is not operational quality

**Paper:** Jiajun Li, Mingshu Cai, Yixuan Li, Yu Ding, Ran Hou, Guanyu Nie, Xiongwei Han, and Wanyuan Wang, *ORAgentBench: Can LLM Agents Solve Challenging Operations Research Tasks End to End?*, arXiv:2606.19787v1 (18 June 2026), <https://arxiv.org/abs/2606.19787v1>.

**Official repository:** <https://github.com/ORAgentBench/ORAgentBench>.

**Date read:** 2026-07-17.

**Review status:** Deep review of the complete immutable v1 paper and static release audit of exact official commit `c9eb952435a4352f33daa2a35efe0f8c76d31b28`. The commit is about eight days after v1 and is evidence about a later release, not proof of paper-time implementation identity.

## Evidence and provenance

- Local immutable PDF: `data/papers/pdfs/2606.19787v1-oragentbench.pdf` (31 pages; 1,896,181 bytes; SHA-256 `aa795fcf6d541effaba02d99a83e7a8467a79f56f6545b31afd6ce9bad083e9f`).
- Complete layout-preserving text: `data/papers/text/2606.19787v1-oragentbench.txt` (136,926 bytes; SHA-256 `a8f33f2366a6e2919d610942a3514306193477286f3f744ed5ea4481b13615d6`). The extraction was read through methods, results, limitations, scoring, task-source table, package protocol, multi-step protocol, difficulty attribution, skill analysis, prompts, task lists, examples, and case studies.
- Archived official release: `data/sources/releases/2606.19787v1-oragentbench/ORAgentBench-c9eb952.zip` (26,535,301 bytes; 8,422 entries; SHA-256 `da5c0a0f4d9544974e4efd85f13872f734eff1071fdab899ee9225c7a0fab52c`). The recursive GitHub tree was complete and the ZIP passed CRC checking at acquisition.
- Release provenance: `data/sources/releases/2606.19787v1-oragentbench/provenance.json`.
- This audit inventoried every packaged task and scoring asset, parsed all 107 `task.toml` manifests and `difficulty.json`, examined source provenance, representative public packets, static and dynamic reference solvers, all reference-metric schemas, experiment configurations, scoring and summary code, and oracle audit notes. All 633 JSON and 208 TOML files parsed. Direct compilation succeeded for 888/889 Python files; the lone failure is a source-dataset utility with a UTF-8 BOM (`source/datasets/train/02_mcts_format.py`), not an administered task verifier.
- No model API or untrusted task workload was run. Static package conformance and selected code inspection do not establish evaluator completeness, oracle optimality, or paper-result reproduction.

## Bottom line

ORAgentBench makes an important endpoint correction. An operations-research agent should not receive a fully formalized instance and return an equation or code fragment. It should reconcile operational files and rules, choose a formulation and solve strategy, execute it, repair failures, and deliver a concrete decision artifact. Deterministic task-specific validation of that artifact is much stronger evidence than judging whether a formulation sounds plausible. The eight staged tasks also preserve prior plans, reveal events, freeze commitments, and require replanning rather than resetting the world.

The benchmark still does not validate the stronger claims suggested by “realistic,” “operationally competitive,” or “dependable.” Most instances are synthetic adaptations or enrichments. The paper reports human review but supplies no reviewer qualifications, task-level approvals, disagreement/adjudication, rejected-task ledger, independent validation, expert baseline, downstream recipient, or evidence that the public obligations are the right obligations for actual use. The release contains provenance records for 102 of 107 task directories, not the asserted complete 107-record audit, and its provenance schemas do not reproduce the paper's four mutually exclusive source categories without undocumented judgment.

More importantly, “quality” is distance from one verified reference solution under either one solver bound or a task-specific poor-solution calibration. This is a useful optimization-performance observation, not professional artifact quality. Bound widths vary by orders of magnitude; many references use a relative-gap fallback, while dynamic tasks use different poor-anchor formulas. The common `q > 0.4` pass threshold therefore does not represent one common objective-loss tolerance, stakeholder utility, service level, or acceptance decision. A feasible plan can be excellent under a weak reference, fail under a tight fallback, or satisfy the objective while omitting explanation, robustness, maintainability, approval, and deployment requirements.

The empirical comparison is not reproducible from the pinned release. The paper evaluates 14 model-agent rows once per task, but the archive contains no reported trajectories, raw run matrix, result summaries, or analysis outputs. Its current configs include model labels that postdate or differ from the paper and allow container internet even while agent web tools are disabled. Table 3's Expert Skills pass percentages are not attainable from single binary outcomes over 32/41/34 tasks, despite the text saying each condition contains one complete run. Failure classes are assigned by first failed stage without a disclosed annotation protocol or validated classifier. The reported ranking, cost frontier, failure attribution, skill effect, and feasibility-quality gap should consequently be treated as descriptive paper claims, not independently reproduced facts.

The defensible contribution is a substantial, inspectable **execution-grounded OR task package and scoring design**. It supports claims about configured agents producing feasible and relatively strong decisions under authored validators. It does not establish authentic OR practice, general OR expertise, human-equivalent quality, professional acceptance, operational competitiveness, reliability, production fitness, or readiness.

## One-sentence contribution

ORAgentBench advances agent evaluation from formulation plausibility to executable decision artifacts under task-specific feasibility and objective checks, but synthetic/adapted task authority, heterogeneous oracle-relative quality scales, clustered task families, single-run comparisons, release/paper drift, and absent raw trials bound its evidence to configured-package performance rather than dependable operations-research practice.

## Why this matters for skill-bench

This review advances charter objectives A, B, and C through expansion, validation, and consolidation. Operations research is a demanding instance of a general benchmark problem: converting a messy multi-file mandate into an executable, constraint-respecting decision whose quality depends on both hidden obligations and consequential trade-offs. It is not a reason to narrow `skill-bench` to optimization.

The central uncertainty clarified is:

> When does a deterministic executable decision check establish useful professional work, and when does it establish only conformance to an authored feasibility model and one oracle-relative objective?

The concrete evidence is unusually inspectable: 107 container manifests, public work packets, 124 evaluator/reference pairs, 99 single-step tasks, 25 stages across eight dynamic tasks, reference solutions, calibrated metrics, provenance files, skills, and experiment/aggregation utilities. Useful completion is a claim-bounded retain/repair/test account that maps the lessons into existing source authority, artifact views, metric contracts, task-family dependence, configured-system identity, task health, and validity arguments rather than building an OR-specific subsystem.

## Research question and claim ladder

The paper asks whether frontier LLM coding agents can solve challenging OR tasks end to end, how performance varies with difficulty and resource use, which modeling/solving failures dominate, and whether procedural OR skills help (Sections 1, 3, and 4).

The relevant claim ladder is:

1. **Package conformance:** the agent emits the required files and schema.
2. **Authored-model feasibility:** the decision passes all constraints implemented by the hidden evaluator.
3. **Oracle-relative objective strength:** the objective is sufficiently strong under a specified reference/bound calibration.
4. **Mandate fidelity:** the evaluator's obligations accurately and completely represent the authorized operational request.
5. **Professional artifact acceptability:** qualified recipients accept the plan, explanation, assumptions, uncertainty treatment, and handoff for its declared use.
6. **Operational consequence:** the decision performs acceptably under real execution, distribution shift, human governance, and downstream effects.

The released deterministic evaluators directly observe levels 1–3. The paper's task-construction testimony supplies partial support for level 4, but no independent criterion audit closes that claim. Levels 5–6 are explicitly outside the benchmark and unobserved.

## Methodology and system

### Task inventory and unit of work

The paper and release agree on 107 task directories: 32 easy, 41 medium, and 34 hard. The release contains 99 static tasks and eight staged tasks. One dynamic cold-chain task has four stages; the other seven have three, yielding 25 stage evaluations and 124 evaluator/reference packages in total.

A standard task exposes an instruction, an operational brief, multiple CSV/JSON files, a submission template, a writable submissions directory, optional procedural skills, and a container with optimization libraries. It retains model documentation, executable solver code, solver logs, and a decision file. The private layer evaluates the decision file and computes feasibility plus objective quality.

Representative packages demonstrate real structural diversity:

- `additive_microfactory_order_planning` combines printer/material compatibility, binary setup, setup time/cost, integer production, scrap-adjusted inventory, regulated-order certification, order fill floors, and profit.
- `stochastic_surgery_capacity_planning` combines elective assignment, block opening, surgeon/equipment/anesthesia restrictions, sequence/timing, scenario-dependent emergency and recovery load, expected cost, and CVaR-style tail risk.
- `cycling_network_design` uses a graph/project/scenario packet and a JSON decision schema.
- `IndustryOR_96` expands a seed formulation into pipe-lot cutting with eligibility, shift, commitment, pairing, remnant, and surcharge rules.
- `online_liner_slot_empty_repositioning` reveals bookings and events over three stages, carries prior submissions forward, freezes near-term decisions, and penalizes allowed changes.

This is materially closer to an end-to-end analytical artifact than text-to-formulation QA. The final decision, not the agent's narrated model, determines feasibility and quality. That design should be retained.

### Task sourcing and authority

The paper classifies primary construction origins as 49 OR papers/application studies, 29 IndustryOR seeds, 19 operational scenarios, and 10 public datasets/repositories. It says all 107 packages were audited through provenance records and construction notes.

The pinned release does not make that table independently reproducible:

- source-layer `provenance.json` exists for 102/107 task directories;
- it is absent for `cycling_network_design`, `dynamic_cold_chain_vaccine_replanning`, `dynamic_supply_disruption_replanning`, `industrial_supply_planning`, and `nurse_rostering`;
- provenance schemas use inconsistent keys such as `source_type`, `sources`, `primary_sources`, `created_from`, `source_inspiration`, `seed_dataset`, and `parent_task`;
- many nominally operational scenarios cite literature, and many literature-derived tasks use fully synthetic instances, so the paper's exclusive “primary” category requires an unreleased coding decision;
- 29 `IndustryOR_*` task directories derive from only 13 seed IDs because several seeds have easy/medium/hard variants.

The records are still valuable. For example, the surgery task names two papers, retained structures, a synthetic/anonymized data policy, scale, and adaptation notes; the liner task names three sources and its synthetic network adaptation. But source inspiration is not demand provenance. No task records a real requester, authorized mandate, original/redacted artifact, transformation reviewer, recipient, use decision, or acceptance outcome.

“Human-reviewed” is also underspecified. The paper describes review for data validity, validator correctness, reference quality, clarity, leakage, shortcuts, and anti-cheating. It reports no number of reviewers, qualifications, independence from authorship, review form, item-level decisions, disagreement, adjudication, revisions, rejected candidates, or calibration against planted evaluator defects. This supports a construction-quality claim, not independent professional validity.

### Difficulty is an authored diagnostic, not validated human difficulty

Difficulty uses six ordinal construction dimensions: solving-strategy requirement, formulation structure, constraint coupling, dynamic structure, data scale, and problem understanding. Totals map to L1–L5 and then easy/medium/hard. The release's `difficulty.json` covers all 107 tasks and explicitly labels its status `rescored_v2_preserving_existing_levels`.

This metadata is richer than instance size alone and useful for stratification. But preserving existing levels while rescoring dimensions makes the labels partly target-constrained rather than independently derived. The rubric has no multiple-rater reliability, empirical item-response calibration, human solve-time baseline, monotonicity analysis, or held-out validation. Regression of failure on these same authored dimensions can describe association under the suite; it does not validate the dimensions as causal burdens or an interval difficulty scale. The paper appropriately calls its blended non-negative regression descriptive, although the fixed `0.78/0.22` coefficient blend is itself an unvalidated stabilization policy.

### Feasibility checks are strong local observers with bounded semantics

The validators parse concrete submitted decisions and recompute constraints from public data rather than trust model claims. The additive-manufacturing evaluator, for example, checks exact columns, numeric and integer/binary values, known identifiers, setup-production links, certification, quantity caps/floors, printer time, material use, and profit. It does not need to understand arbitrary agent code or prose to establish these predicates.

This has four major strengths:

1. deterministic replay over a retained artifact;
2. direct observation of decision semantics rather than formulation style;
3. task-specific diagnostics for violated rules; and
4. acceptance of different solving methods that produce the same valid decision.

The limit is criterion completeness. A validator proves only implemented constraints. It cannot establish that no business rule was omitted, that tolerances match real risk, that a synthetic scenario reflects practice, or that the artifact is usable. The release includes no adversarial false-pass/false-fail corpus, mutation tests, legitimate-alternative suite, or independent validator-versus-requirement crosswalk. All 124 `tests/evaluate_solution.py` files are byte-identical to their corresponding `solution/evaluate_solution.py` copies, which improves oracle/check alignment but does not independently validate either one.

The generic shell layer also filters some evaluator errors after parsing numbers from error strings: discrepancies no larger than `1e-5` can be removed when messages contain broad comparison phrases. This centralizes tolerance behavior but makes final feasibility depend on diagnostic wording, not only explicit predicate values. A criterion-level tolerance contract would be safer than post-hoc natural-language error parsing.

### Quality is not one common quality scale

For many static tasks, a feasible submission with objective `O` is compared with reference objective `R` and valid solver bound `B`. Directional improvement `g(O)` is divided by the reference-to-bound width `W`, raw quality is clipped to `[0,2]`, and paper quality is `q = Qraw / 2`. Reference quality is therefore `q = 0.5`; movement toward the bound approaches 1. If the bound gap is too small or invalid, the verifier switches to a relative-MIP-gap fallback. Other tasks, especially dynamic tasks, use a recorded poor objective and linear reference-to-poor calibration.

The release makes these mechanics inspectable, but their semantics vary sharply:

- 124 reference-metric files have nine different key schemas;
- among 94 records with numeric `R` and `B`, 17 widths are exactly zero and 13 have tiny negative direction widths, generally floating-point effects that trigger fallback;
- the median nonnegative bound width is about `0.000197 × |R|`, while extremes range from zero to `1.0 × |R|`;
- `railway_disruption_recovery` uses a lower bound of zero against reference 6,056.4, so its quality scale spans the full reference objective;
- many near-optimal references use the MIP-gap fallback, making small relative degradation consume the whole quality scale;
- dynamic liner stages have no global bounds and instead use hand-calibrated poor objectives.

The same `q > 0.4` label therefore corresponds to different absolute and relative objective degradation by task. Under the bound formula it permits a candidate worse than the reference by 20% of `W`; when `W` is tiny, that is stringent, while a loose bound can make it permissive. Under poor-anchor calibration it has another interpretation. A common threshold over these scales is an aggregation policy, not a common stakeholder acceptance threshold.

Objective value is also only one axis of professional quality. The score does not assess whether `model.md` faithfully explains the implemented model, whether `solve.py` is maintainable, whether assumptions are authorized, whether uncertainty and sensitivity are communicated, whether a plan is robust outside the finite fixture, or whether a recipient can approve and operate it. Although these files are retained, the administered score primarily observes the decision file.

### Dynamic tasks add state, but remain scripted replanning fixtures

The eight multi-step tasks are the release's most distinctive systems contribution. Later steps overlay event notices and data, retain prior submissions/state, freeze commitments, and evaluate revised plans. Task-level feasibility is strict across all required stages, while quality is averaged. This tests persistence, information discipline, and repair better than independent snapshots.

The liner package demonstrates substantial state semantics: prior booking decisions and vessel paths are read from retained submissions; decisions within the freeze horizon cannot change; already-entered bookings cannot be rejected; later changes incur penalties; stage data progressively expose 54, 88, and 128 bookings. Its three stage references use poor/reference profit anchors.

Yet this is finite scripted replay, not open-world operations. Events, admissible changes, objective, and validator are authored in advance. There is no asynchronous interaction, uncertain observation channel, human escalation, policy change, execution noise, unexpected artifact, or branch based on agent action beyond carried state. Mean stage quality can also compensate across time even though operational loss may be non-compensatory. Strict feasibility across stages is defensible, but the quality aggregation needs a declared operational estimand such as terminal outcome, cumulative cost, regret, stability, or worst-stage loss.

### Skills are part of the configured system, not model capability

The release packages four base OR skills and an Expert Skills collection. Skills can be dynamically loaded, later collections override same-named directories, and `skills: false` strips task copies. This supports a useful intervention on procedural guidance.

The paper's skill study fixes Codex + GPT-5.4 and compares no, base, and expert skills once. Its own text correctly warns that one complete run per condition is descriptive rather than variance-controlled causal evidence. Additional problems remain:

- task outcomes are stochastic but not repeated;
- the treatment changes context length, instructions, tool-use policy, and possibly runtime allocation together;
- no task-level paired artifact ledger is released;
- outcome transitions are discussed without uncertainty or a predeclared causal estimand;
- Expert Skills percentages `59.81`, `36.15`, and `21.50` are not integer multiples of one binary outcome over 32, 41, and 34 tasks respectively, despite the one-run description.

For comparison, the no-skill and base-skill percentages map exactly (within rounding) to integer counts: 20/32, 16/41, 6/34 and 15/32, 16/41, 7/34. The Expert Skills row would imply fractional successes. It may use an unstated averaging or denominator, but neither paper nor release resolves it. The reported skill deltas should not be treated as reproduced paired effects.

## Evidence and reported results

### Main configured-agent comparison

The paper reports 14 model-agent combinations over all 107 tasks, one run per task. GPT-5.4 with Codex leads at 35.51% pass rate; GPT-5.4-mini reaches 28.04%; GPT-5.3-Codex reaches 25.23%; Claude Opus 4.6 reaches 24.30%; and the best hard-task pass rate is 20.59%. Feasibility is generally higher than pass rate. Figure 5 compares runtime and API cost, and Figure 6 assigns first-stage failure categories.

These are informative descriptive observations if the trial ledger is sound. They are not reproducible from the pinned release:

- `ORAgentBench-trajectories/` contains no trial artifacts;
- `analysis/` contains no generated result summaries;
- no per-model/task reward matrix, objective, timeout, token record, cost record, or failed-run record is packaged;
- no command plus immutable agent images/model endpoints regenerates paper tables;
- current experiment YAMLs contain later/different model lists and provider placeholders;
- the archived commit postdates v1 by eight days.

The release does include a substantial `summarize_results.py` that correctly separates feasibility, raw/normalized quality, scalar reward, pass, attempts, multi-step strict feasibility, usage, and missing step rewards. That is useful reproducibility machinery. Without its input trajectories, it cannot verify the paper.

### The feasibility-quality gap is descriptive, not yet diagnostic proof

The paper's central finding is that agents more often produce feasible plans than plans exceeding the quality threshold. That gap follows directly from the two reported dimensions and is plausible. Its interpretation is narrower than “operational competitiveness”:

- quality is oracle-relative, not market-, stakeholder-, or consequence-calibrated;
- reference strength varies;
- task thresholds vary semantically;
- feasibility and quality share evaluator/reference construction;
- one run provides no reliability estimate;
- absent task-level results prevent cluster-aware uncertainty;
- harder tasks and family variants are not independent units.

A feasible-but-low-q result establishes that one artifact passed authored constraints but scored below one normalization threshold. It does not alone identify weak solver construction, insufficient improvement, misunderstood trade-offs, or operational uncompetitiveness. Those mechanisms require trajectory observations or controlled repairs.

### Failure attribution is not validated root-cause analysis

The paper labels the first failed stage as modeling error, formulation efficiency, weak solver, or timeout and reports modeling-side failures at 54.8% of non-passing trials. This taxonomy is useful: it distinguishes missed rules, structurally brittle models, feasible-but-low-quality outcomes, and exhausted budgets.

But the annotation method is not disclosed sufficiently. There is no released label file, trajectory corpus, coder count, coding guide, independence, agreement, adjudication, evidence view, ambiguity state, or intervention confirming the assigned root cause. “Weak solver” is partly outcome-defined by failing the same quality threshold, not an independently observed mechanism. A timeout can be caused by formulation, code, environment, or strategy; a missing rule can be downstream of data interpretation. First-failure labels are surface localization hypotheses until counterfactual repair or stronger trace evidence supports cause.

### Cost and runtime claims are configured-system claims

Runtime and API cost include model endpoint, CLI scaffold, prompt, skills, tool policy, container, concurrency, provider caching/accounting, and task timeout. The paper correctly notes that more cost/time is not monotonically better. It does not support a general efficiency frontier without repeated trials, common endpoint accounting, uncertainty, and controlled budgets.

The release's task manifests give static agents 2,700 seconds and dynamic stages mostly 900–1,500 seconds; Docker resources are 4 CPUs and 8 GB RAM. All 107 manifests set `allow_internet = true`. Experiment configs disable explicit WebSearch/WebFetch for Claude Code and web search for Codex, but a container-level internet allowance is not equivalent to network isolation. Any claim of “without internet access” depends on agent-adapter enforcement and should be verified in the executed environment. The paper does not release network traces.

## Unique insight: executable decision validity needs a dual witness

ORAgentBench's strongest transferable lesson is that a professional decision artifact needs two different witnesses:

```text
authorized mandate + valid-time evidence
        ↓
obligation witness: what must be true, who says so, and for what use
        ↓
submitted executable decision
        ↓
conformance witness: schema + constraints + objective observations
        ↓
acceptance/consequence witness: recipient threshold + use + realized effects
```

A solver-backed validator is a strong **conformance witness**. It can prove that a submitted plan satisfies encoded obligations and has an observed objective. It is not its own **obligation witness**: the same authors often write the scenario, enrich data, implement the evaluator, build the reference, choose the quality width, and set the pass threshold. Internal consistency across those artifacts can still encode the wrong requirement or wrong trade-off.

The portable design rule is therefore:

> Never promote executable feasibility or oracle-relative objective strength into professional validity unless the benchmark separately warrants the obligation set and acceptance threshold.

This dual-witness model generalizes beyond OR. A spreadsheet can recalculate correctly against the wrong policy; a legal filing can satisfy a parser while omitting an authorized argument; a scientific pipeline can reproduce one metric under the wrong assay definition; a project plan can satisfy a synthetic resource model while violating stakeholder constraints.

For `skill-bench`, each critical rule should bind:

- source or expert authority;
- valid time and transformation history;
- public disclosure status;
- machine-checkable predicate where possible;
- observer evidence and known blind spots;
- severity or decision consequence;
- legitimate alternatives;
- acceptance threshold and its calibration; and
- root/surface failure relationship.

Objective quality should remain a typed observation with task-specific units and direction. Normalization may support display or a declared portfolio policy, but it should not erase whether a threshold means 0.01% cost regret, 20% of a loose relaxation gap, service-level breach, or a heuristic poor-anchor interpolation.

## Reproducibility and operational realism

### What is unusually inspectable

The later release is substantial:

- 107 runnable Harbor task packages with complete difficulty coverage;
- 99 static and eight multi-step workflows;
- 124 evaluator/reference packages;
- public operational briefs, structured data, and submission templates;
- deterministic task-specific evaluators;
- reference solvers and detailed reference metrics;
- container/resource manifests and a shared optimization image design;
- base and expert skill collections;
- experiment configs and pre-build wrappers;
- a careful result summarizer that distinguishes raw quality, normalized quality, scalar reward, pass, attempts, and multi-step missingness;
- internal reference-oracle audit notes that candidly distinguish MIP, hybrid, matheuristic, and rework cases.

The oracle audit is especially useful evidence against overclaiming: several hard references are model-informed heuristics, and two are explicitly `REWORK-IN-PROGRESS`. A verified reference is not uniformly an optimum or valid global-bound witness. The package records this diversity better than many benchmarks.

### What cannot be reproduced

The archive cannot regenerate or independently verify the paper's empirical tables because it omits:

- paper-time code identity;
- raw trajectories and generated artifacts;
- per-trial verifier outputs;
- administered model/agent/image manifest;
- exact provider endpoints and dates;
- complete token/cost records;
- invalid, failed, retried, and excluded-run ledger;
- failure-mode annotations;
- skill-treatment paired results;
- generated analysis tables/figures; and
- uncertainty or repetition evidence.

Public release of all hidden evaluators, metrics, reference solvers, and reference solutions favors inspectability and local development. It also makes the public form contamination-prone: a search- or repository-aware agent can retrieve exact checks, objective anchors, and reference methods. The runtime package keeps tests/solution outside `/app`, but benchmark secrecy after public release requires a private scored form, exposure ledger, or regeneration protocol. The paper does not establish contamination resistance.

### Operational realism

The tasks include multi-file data, business-shaped constraints, executable optimization, finite uncertainty, resource limits, and replanning. This is more operational than formulation-only benchmarks. The paper also candidly excludes stakeholder negotiation, qualitative policy judgment, live feedback, long-term deployment, open-ended distribution shift, evolving rules, and complete process audit.

Additional absent elements include source-system permissions, data ownership, privacy/compliance review, solver licensing/procurement, human approval, audit sign-off, incumbent-plan handoff, monitoring, rollback, realized KPI effects, and responsibility for harmful decisions. The decision files are operational fixtures, not observed deployments. “Realistic” can describe surface and structural features; “real-world OR capability,” “dependable decisions,” and “operational competitiveness” require separate evidence.

## Limitations and validity threats

### Construct and content validity

1. Most tasks are synthetic, adapted, or enriched rather than sampled observed OR engagements.
2. Source inspiration is not an authorized operational mandate.
3. Five task directories lack source-layer provenance records in the pinned release.
4. Inconsistent provenance schemas do not independently reconstruct the paper's source table.
5. Twenty-nine IndustryOR task directories derive from only 13 seed IDs, reducing effective diversity.
6. Easy/medium/hard variants create family dependence not reflected in raw task counts.
7. No sampling frame defines the target population of OR work.
8. Human review lacks qualifications, independence, per-task records, disagreement, and adjudication.
9. No expert baseline anchors difficulty or professional acceptability.
10. Difficulty labels preserve prior levels during rescoring and are not independently calibrated.
11. Final-decision scoring underobserves model explanation, code quality, assumptions, uncertainty communication, and handoff.
12. Scripted events do not establish open-world replanning ability.

### Measurement and grader validity

13. Validator completeness is not tested with adversarial false-pass/false-fail cases.
14. Tests and solution evaluator copies are identical, providing consistency rather than independent validation.
15. Post-hoc numeric tolerance filtering depends on diagnostic wording.
16. Reference solvers range from exact MIPs to hybrids, matheuristics, and acknowledged rework cases.
17. Quality formulas differ across bound, fallback-gap, and poor-anchor task classes.
18. Bound-width heterogeneity makes common normalized values semantically unlike.
19. A common `q > 0.4` threshold is not calibrated to stakeholder loss or acceptance.
20. Feasible full quality is granted when no reference exists in generic scoring logic, although inspected packaged schemas generally provide anchors.
21. Objective value omits robustness, maintainability, explanation, governance, and consequence.
22. Mean stage quality can compensate across stages without an operational utility argument.
23. Public evaluators, reference metrics, and solvers contaminate the public scored form.

### Reliability, comparison, and causal validity

24. Main results use one run per model-task cell.
25. No repeated trials estimate stochastic reliability.
26. No task-family-clustered uncertainty accounts for variants and shared seeds.
27. Raw results and trajectories are absent from the release.
28. Paper-time and pinned-release implementations are not identical by evidence.
29. Current model configs do not freeze the paper's administered systems.
30. Model labels conceal scaffold, skills, provider, cache, image, and tool-policy differences.
31. Cost/runtime comparisons lack controlled common budgets and repeated uncertainty.
32. Failure-mode labels have no released annotation or reliability evidence.
33. First failed stage is not necessarily root cause.
34. Skill interventions have no repetitions or released paired trial ledger.
35. Expert Skills pass percentages conflict with the stated binary denominators.
36. Standard-error bars across model-agent rows do not estimate trial reliability or population uncertainty.

### Release, security, and operational validity

37. The archived commit is eight days after v1.
38. The release omits trajectories and generated analyses despite documenting their paths.
39. All task manifests allow internet at the environment level, while configs only disable selected web tools.
40. No network trace proves the no-internet experimental condition.
41. Public hidden assets require a private-form or contamination-control strategy for future scoring.
42. Container isolation does not itself establish production permissions, data governance, or safe execution.
43. No real recipient acceptance, deployment, realized benefit, or harm observation is reported.
44. The benchmark does not establish reliability, production fitness, or readiness.

## Transferable benchmark-design lessons

### Retain

1. **Decision-artifact endpoint.** Grade the concrete decision or professional output, not only prose or code plausibility.
2. **Task-specific deterministic validators.** Recompute obligations and metrics from authoritative input data.
3. **Separate feasibility and objective quality.** Do not let a high objective compensate for violated hard constraints.
4. **Inspectable scoring provenance.** Record reference objective, bound, sense, tolerance, solver status, and calibration formula.
5. **Multi-step state carryover.** Preserve prior artifacts, reveal events, freeze commitments, and charge for allowed changes.
6. **Multiple artifact retention.** Keep model, code, logs, and decision even when the final score uses only some of them.
7. **Difficulty dimensions beyond scale.** Preserve formulation, coupling, dynamics, understanding, and strategy as diagnostic metadata, not a validated latent scale.
8. **Oracle-method honesty.** Label exact, hybrid, matheuristic, and incomplete references distinctly.
9. **Configured-system reporting.** Treat agent, model, skills, tools, container, resources, and network policy as one treatment.

### Repair

1. Add task-level obligation provenance: requester/source authority, transformation, reviewer, valid time, public basis, and approval scope.
2. Release a criterion crosswalk from public requirement to evaluator predicate, tolerance, severity, and known blind spot.
3. Validate evaluators on planted omissions, boundary cases, parser exploits, legitimate alternatives, and semantically wrong but objective-good artifacts.
4. Replace prose-error tolerance filtering with predicate-level typed tolerances.
5. Type every quality scale by calibration mode and report task-native regret/loss alongside any normalized value.
6. Do not use one pass threshold across scales without an explicit portfolio estimand and sensitivity analysis.
7. Cluster related variants and shared seed IDs in reporting and uncertainty.
8. Preserve complete scheduled → started → valid/invalid → retried → scored trial closure and raw artifacts.
9. Repeat trials and report task- and family-aware uncertainty before ranking systems or estimating skill effects.
10. Separate public development assets from private/semi-private scored forms and log exposure/search conditions.
11. Verify actual network isolation rather than infer it from disabled named tools.
12. Add human/expert artifact acceptance and consequence studies before claiming professional or operational quality.

### Test

A cross-domain executable-decision validation slice should include at least two unrelated task families and, for each, construct:

- one correct decision and explanation;
- one feasible but materially poor decision;
- one high-objective artifact that violates a hidden authorized obligation;
- one valid alternative formulation and solver;
- one artifact exploiting parser/tolerance behavior;
- one decision that passes the authored model but fails an independent expert obligation review;
- one stale plan after a state update;
- one locally strong replan with harmful cumulative/terminal consequence; and
- one observer-insufficient case requiring abstention.

The test should record native objective regret, normalized score, criterion observations, expert acceptance, and root/propagated failures separately. It should demonstrate that executable checks catch local violations, independent obligation witnesses catch evaluator omissions, alternatives are accepted, and aggregation does not reverse the declared decision policy.

## Concrete repository actions

1. **No new queue task.** The evidence directly refines existing metric-specification and validation work rather than warranting a new OR subsystem. During the next implementation/consolidation pass, use this review's heterogeneity findings as a required contrast: objective normalization must preserve calibration mode, native unit, reference/bound provenance, threshold meaning, and sensitivity.
2. When an existing multi-step pilot is next exercised, include one frozen-decision case and one cumulative-versus-mean quality contrast; do not create a new pilot solely for ORAgentBench.
3. In benchmark-family synthesis, cite ORAgentBench as strong evidence for concrete decision validation and state carryover, and as counterevidence to treating executable feasibility plus oracle-relative quality as professional acceptance.
4. Do not cite the paper's model ranking, failure percentages, Expert Skills effect, or cost frontier as independently reproduced until the authors release an administered-suite manifest, raw trials, failure labels, and version reconciliation.

## Claim boundary

This review establishes that immutable v1 presents a consequential executable-decision benchmark design and that the later pinned release contains a large, substantially inspectable implementation with 107 tasks, deterministic validators, reference metrics, skills, and staged replanning. It also establishes release-visible provenance gaps, heterogeneous quality calibration, task-family dependence, missing paper-result artifacts, environment-policy ambiguity, and an internally unresolved Expert Skills denominator. It does **not** establish that any evaluator is complete, that every reference is optimal, that reported model rankings reproduce, that skills causally help, that tasks represent real OR demand, that a pass is professionally acceptable, or that any system is operationally competitive, reliable, safe, production-fit, or ready.
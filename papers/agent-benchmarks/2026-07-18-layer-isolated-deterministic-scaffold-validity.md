# Paper Review: Layer-Isolated Evaluation — Deterministic Scaffold Validity

- **Paper:** https://arxiv.org/abs/2606.11686v1
- **Authors:** Sawyer Zhang, Alexander Wang, Sophie Lei
- **Date read:** 2026-07-18
- **Venue / source:** arXiv preprint
- **Version read:** immutable v1, submitted 10 June 2026
- **Local PDF:** `data/papers/pdfs/2606.11686v1-layer-isolated-evaluation.pdf` (12 pages; SHA-256 `532b08a6e8576c8361a8044fc707438804f1fe10753226c869f87b295abe2e99`)
- **Local text:** `data/papers/text/2606.11686v1-layer-isolated-evaluation.txt` (SHA-256 `b8950f4ccb788a45090dec27c909243e9120acd071b42b67989c819fe771b1db`)
- **Immutable arXiv source:** `data/papers/source/2606.11686v1-source.tar.gz` (SHA-256 `841a490278f01327afce5fb3b855562d8ed05be8377d06b732504148c8481276`)
- **Release provenance:** `data/sources/releases/2606.11686v1-layer-isolated-evaluation/provenance.json`
- **Evidence status:** deep review of the complete immutable paper and source; not release-audited because no verifiable author-owned empirical release was available at review time
- **Tags:** deterministic-conformance, component-slices, regression-gates, mutation-testing, fault-localization, coverage-adequacy, aggregate-masking, production-evaluation

## One-sentence contribution

The paper turns one deployed ordering agent's deterministic scaffold into 23 named assertion slices gated against a locked baseline and reports that seven author-chosen single-entry-point mutations produce large matching-slice drops despite small pooled changes, but the unavailable harness and records, a 238-versus-225 denominator ambiguity, binary and partly deletion-insensitive coverage semantics, intervention-conditioned fault selection, and no independently frozen organic-regression success bound the result to a promising **component-conformance and designed-mutation-sensitivity case**, not validated causal diagnosis, stochastic agent reliability, production consequence, or readiness.

## Why this matters for skill-bench

`skill-bench` needs both outer task outcomes and cheap inner checks. A realistic knowledge-work agent may fail because an evidence resolver, policy gate, routing rule, artifact transform, or state transition changed even when a broad portfolio score barely moves. This paper gives a concrete development pattern:

`declared component contract → deterministic case → exact observer → frozen component baseline → isolated mutation → component and off-diagonal response → merge decision`

The paper's most reusable contribution is not that a test fails when its target code is deliberately broken—that is largely designed in. It is the separation of two different phenomena:

1. **portfolio masking:** a severe local failure can contribute only a few points to an inventory-weighted aggregate; and
2. **response topology:** local mutations mostly affect the intended slice, while foundational mutations create wider downstream signatures.

For the charter, this advances objectives A–C through a cross-domain evaluation mechanism. The food-ordering case is not a scope commitment. The general hypothesis is that deterministic subcontracts within messy knowledge work can be gated cheaply if requirement authority, implementation locus, observer coverage, dependency topology, and baseline correctness remain explicit.

## Research question and claim boundary

The paper asks whether a no-LLM, per-layer assertion harness can cheaply detect and localize deterministic scaffold regressions that an aggregate end-to-end metric would mask.

The reported evidence supports these bounded claims:

1. The manuscript specifies a 23-slice baseline containing 238 cases: 225 pure per-layer cases, 13 separately run `L1_legacy` cases, four zero-case slices, and two low-N slices (Section 3, Table 2, pp. 3–6).
2. The authors report one no-LLM pure run of 225 passes and 30 skipped live-only variants in 2.39 seconds (Section 3 and Table 5, pp. 3, 8).
3. Seven declared mutation treatments produce large target-slice changes and mostly sparse off-diagonal changes in the reported reference-tenant matrix (Section 4, Table 3 and Figure 1, pp. 4–7).
4. Sixteen newly authored second-tenant cases reproduce a matching-slice drop for all seven treatments and reproduce the wider ontology signature (Section 4.1, Table 4, pp. 6–8).
5. Two faithfully replayed pre-fix code states produce no effect on the current suite, an honest negative result showing absent case coverage rather than successful organic localization (Section 6, pp. 7–9).
6. The paper explicitly limits a green baseline to unchanged observed behavior, not absolute correctness (Section 7, pp. 9–10).

The evidence does **not** establish that the stated 238-case inventory or results correspond to an inspectable repository; that component requirements are correct or complete; that all deterministic scaffold edges are covered; that the seven retained treatments represent organic fault distributions; that slice ranking identifies the unique earliest cause; that the second tenant is independently representative; that live generative behavior is reliable; that the reported production incident would have been caught by the then-current suite; that per-PR use reduced incidents; or that the agent is professionally valid or deployment-ready.

## Methodology and system reconstruction

### Deployed-agent and layer provenance

The system is described as a per-tenant, multi-turn food-and-beverage ordering agent built on PydanticAI. The taxonomy spans ontology pre-resolution, speech act and intent signals, routing, escalation, decomposition and constraints, safety, knowledge, memory, plus defense, prompt envelope, reformulation, out-of-domain rejection, recommendation rules, read-tool views, session initialization, and locale fidelity (Sections 1 and 3, pp. 1–6).

Calling the agent “deployed” adds ecological context but little auditable provenance. The paper does not report deployment dates, tenant count, traffic distribution, production configuration or commit, PydanticAI version, tool/catalog evolution, incident population, monitoring window, or outcome measures. The Starbucks fixture is said to be generated from a real Foodpanda SG menu, but its source bytes, transformation method, rights, snapshot date, and acceptance checks are unavailable. Production origin should therefore be treated as an author statement, not a validated operating profile.

### Pure mode and its boundary

Each pure case calls deterministic logic and compares exact outputs: canonical IDs, intent vectors, escalation decisions, dictionary rewrites, OOD predicates, server-side repricing, or rendered prompt blocks. No LLM, network, or external service is said to run. The paper reports about 1 ms of compute per case and about 10 ms amortized including process startup and fixtures (Section 3, p. 3; Table 5, p. 8).

This is a valuable boundary. It removes model-sampling noise from the measured contract. It does **not** validate the live path that supplies inputs to those functions, the model's adoption of deterministic outputs, tool execution, multi-turn recovery, or end-to-end consequence. Thirty collected live-only variants are skipped, four named layers have zero pure cases, and free-form generative behaviors remain explicitly outside the gate (Sections 3 and 8, pp. 3, 10).

A pure-mode pass is therefore a configured implementation claim:

`given frozen fixture + exact entry point + deterministic runtime + exact observer, observed output satisfies the baselined assertion`.

It is not an agent-success observation.

### Case inventory and the 238/225 boundary

Table 2 allocates 238 baseline cases across 23 slices. The paper carefully explains that only 225 belong to the per-layer pure runner; 13 `L1_legacy` end-to-end cases run separately; 30 additional live-only variants are collected and skipped rather than counted in 238 (Section 3, pp. 3–4).

That reconciliation helps, but Table 3 introduces a denominator ambiguity. Its exact percentage-point changes are consistent with division by **238**, including the separate 13-case legacy lane: for example, four OOD failures yield `4/238 = 1.68 pp`, while eight defense failures plus other movement yield the stated pooled value. The table caption nevertheless calls this the “aggregate pure-suite pass-rate,” and the paper elsewhere contrasts the 225-case pure run with the legacy lane. If the intended aggregate is the 225-case pure runner, the deltas differ. If all 238 cases are rerun under each injection, the legacy lane is part of the experiment and should not be described as separate from the pure runner.

This does not erase the qualitative masking result, but it makes the headline estimand insufficiently bound. `skill-bench` should never let “aggregate” float across inventories or execution lanes: every statistic needs exact included case IDs, lane versions, invalid/skipped handling, and a replayable numerator/denominator.

### Locked baselines and coverage honesty

The baseline stores per-slice total, passed, rate, and failed IDs. It starts at 100%. A zero-case slice receives `null`, not 100%, and four such gaps plus two low-N slices are reported (Section 3, pp. 3–4). A per-slice rate below baseline blocks merge.

The paper calls “at least one case” its formal test-adequacy criterion. This is better than silently assigning full credit to an empty slice, but it is a minimal **presence** criterion, not adequate semantic coverage. One locale case and three health cases are rightly flagged as low-N; a single case can still miss every important branch, input class, boundary, state, and downstream dependency.

The simplified gate also compares rates, not retained case identity or total count. Removing some cases from a covered 100% slice can leave its rate at 100%; only deleting the entire slice changes it to uncovered. The prose says the frozen record contains totals and failed IDs, but the shown algorithm does not reject count decrease, case-set mutation, changed expectations, or requirement removal. Because the empirical release is unavailable, a stronger implementation cannot be verified.

Coverage honesty should therefore be multidimensional:

- declared requirement and dependency inventory;
- requirement-to-case and case-to-observer links;
- retained case IDs/hashes and expected outputs;
- branch, boundary, state, tenant/form, and consequence coverage;
- known uncovered and low-support regions;
- mutation sensitivity and surviving mutants;
- organic incident coverage after an independently frozen test date.

`null` for zero is a useful first rule, not a complete adequacy argument.

### Mutation treatments and selection

Seven non-safety entry points are monkeypatched: ontology returns empty, reformulator becomes identity, escalation never fires, intent signals become empty, defense allows all, OOD never rejects, and decomposition emits no subgoals. The runner constructs a fresh runtime for each pass and drops a mutation if a self-check says it did not take effect (Section 4, pp. 4–5).

The fresh-runtime repair is important. Reusing runtime state created a phantom off-diagonal column because order records survived across passes. Baseline-twice replay exposed the artifact; reconstructing runtime per pass removed it (Section 4 and Figure 1, pp. 4, 7). This is concrete evidence that the evaluator itself has state and needs canaries.

However, the retained set is highly conditioned:

- authors choose covered, tractable, non-safety entry points;
- mutation forms are extreme degradations rather than sampled historical faults;
- no-op treatments are dropped from the reported set;
- safety, routing, memory, personalization, and reflexion are not exercised;
- attempted mutation count, dropped count, equivalent-mutant count, and selection rationale are absent;
- treatment effectiveness is checked, but semantic confinement to exactly one contract is not independently verified.

The design estimates sensitivity to seven **effective author-selected mutations**. It does not estimate mutation adequacy over a declared operator population or expected production detection probability.

### Metrics: masking, movement, and localization

For each mutation the paper reports pooled pass-rate delta, target-slice delta, number of moved slices, and target rank among 19 covered slices. Six “local” treatments move the aggregate by 1.68–5.88 pp while target slices fall 25–90.91 pp; the ontology treatment moves the aggregate by 26.47 pp and its target by 95.24 pp. Target rank is first in five of seven and top-three in all seven, with mean rank 1.29 (Table 3, p. 6).

The target crater is expected because target assertions were written around the treated entry point. The more informative observations are:

1. **masking leverage:** slice size controls pooled visibility;
2. **off-diagonal sparsity:** five local treatments move at most three slices, with defense and OOD moving only their own slices;
3. **foundational signature:** ontology affects nine slices, and intent affects a small downstream knowledge slice more than its own target.

Yet “fault localization” is stronger than the design fully supports. Slice labels already encode implementation ownership, and rank is based on outcomes under known single-locus interventions. A wide blast radius can reveal a dependency subgraph, but it does not by itself identify the earliest cause in an organic failure with concurrent changes, shared dependencies, observer defects, or recovery. Against Who&When Pro, this study establishes `known mutation locus → response pattern`; it does not need to infer the injected locus from an unlabeled natural trace.

Counts are exact for the claimed deterministic run, so repeated sampling is unnecessary to reproduce that one matrix. Statistical uncertainty is still relevant to **generalization over cases, mutations, tenants, commits, and operating conditions**. The 238 cases are clustered within slices and likely share fixtures; the seven mutations are not a random fault sample; the 16 tenant-B cases were authored specifically around those mutations. Reporting exact arithmetic does not make those populations representative.

### Cross-tenant replication

The second-tenant study adds 16 baseline-green cases over the seven treated layers. Every matching slice drops 50–100 pp; six have clean tenant-B off-diagonals, while ontology also affects decomposition (Section 4.1, Table 4, pp. 6–8).

This is useful transport evidence for treatment reach across two catalog structures. It is not an independent replication:

- the same authors, code, mutation operators, assertions, and measurement policy are reused;
- the 16 cases are authored after and for the seven target treatments;
- several target groups therefore contain only one or two cases, producing coarse 50/100-point changes;
- “structurally different” is asserted rather than measured against a tenant population;
- the tenant pack and raw outcomes are unavailable.

The result supports cross-fixture conformance of the designed mechanism, not external validity across ordering tenants, domains, frameworks, or natural regressions.

### Organic regressions and production incident

The paper describes a historical confirmation-gate regression: explicit confirmation often failed to produce `create_order`, allegedly on roughly half of affected rounds, while an aggregate live judge barely moved. Human review found it (Section 6, pp. 7–8). Critically, `L2_routing` is currently uncovered, so the existing pure suite would **not** have caught it. Coverage reporting names the gap, and a proposed confirm-to-place assertion could catch that class in the future.

This is an honest and important distinction between risk visibility and detection. But no incident log, commit, time window, denominator, live-judge record, or retrospective executable case is released. The incident motivates a contract; it does not validate the current gate.

The authors also replay two exact pre-fix implementations—an over-rejecting OOD guard and a dead cross-round referent. Neither changes any current slice and both are dropped as no-effect. This is the strongest validity evidence in the paper precisely because it is negative: the suite does not cover these historical behaviors. No independently frozen slice successfully localizes a later organic regression. Cases co-authored with fixes are excluded as by-construction (Section 6, pp. 8–9).

### Cost and maintenance burden

The reported pure runtime is 2.39 seconds and $0 in model tokens; one live episode has median 73-second and p95 192-second latency (Section 5, Tables 5, pp. 7–8). The live sample count, date, endpoint, hardware, concurrency, and token/cost distribution are not reported, so the comparison demonstrates an order-of-magnitude plausibility rather than a reproducible cost estimate.

More importantly, execution cost is not maintenance cost. The paper does not report engineering time to define layers, elicit contracts, author 238 cases, build 16 transport cases, inspect false alarms, update baselines, review uncovered regions, adjudicate legitimate behavior changes, or maintain tenant fixtures. A fast test can still be expensive to keep valid. Production usefulness requires both marginal run cost and lifecycle labor.

## Evidence and results interpretation

The paper's result should be read as a response matrix, not a reliability score:

`case inventory × component slice × known mutation × tenant fixture × frozen runtime → exact assertion outcomes`.

Within that matrix, the qualitative result is credible as reported: inventory-weighted pooling can hide a large local rate change, and the designed slices respond sparsely enough to guide debugging. The paper deserves credit for explicitly marking the target-slice reaction as partly tautological, exposing the state-leak artifact, reporting uncovered slices, preserving no-effect historical mutations, and saying a locked baseline is not a correctness oracle.

Several phrases still outrun the evidence:

- “real, reproducible” in Table 3 is not operationally true for an external reviewer without the named scripts, cases, runtime, and results;
- “fully decomposed” conflicts with four named uncovered layers, 30 skipped live variants, and generative behavior outside pure mode;
- “production agent” describes provenance, not production-effect validation;
- “localizes regressions” is supported for known single-locus designed mutations, not an independently frozen stream of organic faults;
- “aggregate barely moves” depends partly on inventory composition and the ambiguous 238/225 denominator;
- the conclusion's “−3 to −8 pp” summary does not match Table 3's six-local range of −1.68 to −5.88 pp and omits the −26.47 pp foundational case (p. 10 versus p. 6).

## Unique insight

The paper's deepest contribution is that **diagnostic value is a topology, not a scalar**.

An aggregate says how much weighted observed behavior changed. A slice response vector says where the observer detected change and which dependencies propagated it. But that vector becomes diagnostic evidence only when five graphs are kept distinct:

1. **requirement graph:** which authority-bearing behavior matters and why;
2. **implementation graph:** which component and version realizes it;
3. **case graph:** which cases exercise which requirement boundaries;
4. **observer graph:** which assertion views which state or output;
5. **dependency graph:** which component outputs can affect which downstream checks.

A diagonal crater can arise because all five graphs align—or merely because the test and mutation share an implementation label. A flat off-diagonal can mean good isolation or missing cross-layer assertions. A wide row can reveal foundational dependence or fixture/test contamination. Removing cases can make a matrix look cleaner. Therefore localization quality needs more than target rank: expected-edge recall, unexpected-edge precision, mutation survival, case-set integrity, and organic post-freeze incidents.

This sharpens existing `skill-bench` root/surface practice. Deterministic component tests should supply one evidence rung:

`component conformance → designed-mutation sensitivity → dependency-response calibration → independently frozen organic-regression detection → repair confirmation → repeated end-to-end outcome effect → production consequence`.

No rung substitutes for the next.

## Comparison with adjacent evidence

- **Dependency-edge conformance / DevicesWorld:** endpoint conjunctions and dependency edges show whether required state transfer occurred. Layer-Isolated Evaluation adds a mutation-response matrix, but does not independently validate the requirement or dependency graph.
- **STRACE:** STRACE infers causal slices from noisy natural trajectories and risks model-generated graph error. This paper knows the intervention locus and measures deterministic responses, avoiding that inference problem but covering only the pure scaffold.
- **Who&When Pro:** both use controlled injection. Who&When Pro risks equating injected action with natural causal root; this paper more honestly treats target sensitivity as designed and uses off-diagonal response as the evidence. Neither establishes multi-cause organic diagnosis or repair utility.
- **Agent Reliability Profile:** repeated stochastic task outcomes, perturbation distributions, resource variance, and consequences remain separate from one exact deterministic response matrix. Determinism removes within-run sampling variance, not operating-profile uncertainty.
- **Harness-Bench:** a fresh runtime and baseline-twice canary are evaluator-validity controls. They do not prove filesystem/network isolation, version equivalence, or live-harness validity; unavailable code prevents an outer-envelope audit.
- **Anthropic task health:** locked reference behavior is one health signal. Instrument role, origin, case-set revisions, adjudications, ownership, saturation, and retirement still require lifecycle records.
- **Amazon metric monitoring:** a slice rate needs exact eligible case population, denominator, invalid/skipped policy, version window, threshold, owner, and action. The 238/225 ambiguity demonstrates why a metric name is insufficient.

## Limitations and validity threats

1. The claimed harness, cases, baselines, mutations, tenant fixtures, raw outcomes, and analysis scripts are unreleased.
2. No official repository URL appears in the immutable paper or arXiv source; exact-path and author-profile searches found no verifiable release at review time.
3. “Deployed” provenance lacks commits, dates, traffic, configurations, and production outcome records.
4. The requirement-authoring method, authority, review, and alternative-valid-behavior process are absent.
5. A 100% locked baseline preserves behavior, not correctness.
6. Four of 23 slices have zero cases and two have very low N.
7. At-least-one-case adequacy is presence, not semantic or boundary coverage.
8. The shown rate-only gate may not detect partial case deletion, changed IDs, changed expectations, or weakened requirements.
9. Thirty live-only variants are skipped; generative and adoption behavior remains outside pure mode.
10. The 238 baseline mixes 225 pure cases with 13 separately run legacy cases.
11. Table 3's exact deltas appear to use 238 while calling the statistic a pure-suite rate.
12. The mutation set is author-chosen, extreme, small, and limited to covered non-safety layers.
13. No-op mutations are dropped without attempt and disposition denominators.
14. Safety faults are excluded, so sensitivity on the highest-consequence layer is untested.
15. Single-entry monkeypatching identifies code locus, not necessarily one semantic requirement or one causal edge.
16. Target-slice sensitivity is substantially designed into the case/mutation pair.
17. Off-diagonal flatness can reflect isolation or missing cross-layer observation.
18. Target rank ignores expected dependency edges, equal ties, severity, and observer coverage.
19. Deterministic exactness does not solve generalization over cases, mutations, versions, tenants, or incidents.
20. The 16 tenant-B cases are treatment-targeted, sparse, and authored by the same team after the mechanism was known.
21. Tenant structural difference and source transformation are not independently documented.
22. The production incident is not backed by released logs, commits, or executable replay.
23. The then-current suite did not cover the production incident's routing contract.
24. Two historical pre-fix replays are correctly null, leaving no successful independently frozen organic-localization case.
25. Live latency and cost comparisons omit sample size, environment, endpoint, token cost, and censoring.
26. Authoring, review, baseline-update, triage, and fixture-maintenance labor are unmeasured.
27. No multi-change, shared-dependency, observer-defect, sham, case-deletion, or equivalent-mutant controls are reported.
28. No end-to-end experiment shows that blocking a mutation prevents a user-visible or professional consequence.
29. Conclusion ranges drift from the central table.
30. One framework and one narrow domain cannot establish cross-framework or cross-domain transport.

## Reproducibility and operational realism

Reproducibility is **strong for the manuscript and weak for every empirical execution claim**. The immutable 12-page PDF, complete text, and five-file arXiv source are preserved and readable. The source names internal paths, scripts, and result files, but contains no empirical data or code beyond manuscript materials. Current searches found only the arXiv record and third-party listings. An external reviewer cannot rerun 225 cases, reconcile the 238-case aggregate, inspect the 30 skipped variants, verify fresh-runtime construction, audit mutation confinement, reproduce either tenant matrix, or test case deletion.

Operational realism is mixed. Deterministic resolvers, policy gates, repricing, prompt envelopes, state reset, merge blocking, and historical regressions are genuine production concerns. The method fits CI far better than expensive live episodes. But the evidence surface omits the live agent, environment, traffic, stakeholder outcomes, baseline governance, maintenance labor, and independently observed incident stream. It is best interpreted as an internal conformance-testing architecture with promising diagnostic properties, not a production reliability study.

## Transfer to skill-bench

### Retain

1. **Two-speed evaluation.** Run deterministic component/artifact/state conformance on every change; reserve repeated live configured-agent trials for nightly, release, or claim-validation lanes.
2. **Exact component slices.** Keep component-level outcomes separate from end-to-end task outcomes and report the entire response vector.
3. **Null, not green, for absent evidence.** Unexercised requirements, unavailable views, skipped lanes, and invalid canaries must remain uncovered/unscorable.
4. **Fresh-runtime canaries.** Run baseline twice, verify fixture/state identity, and detect phantom off-diagonal movement before mutation or treatment comparisons.
5. **Mutation-response calibration.** Plant local and foundational faults and preserve the complete matrix, including no-effect, equivalent, invalid, and recovered treatments.
6. **Honest drift semantics.** A frozen passing witness proves unchanged observed conformance only for exact component, case, observer, and environment versions.

### Repair

1. **Bind every slice to authority and topology.** Record requirement ID/source, component version and entry point, case IDs/hashes, observer/evidence view, expected dependency edges, permitted alternatives, and consequence/public basis.
2. **Make case-set integrity non-negotiable.** Reject deleted or silently changed cases, expectation drift, reduced branch/boundary support, and changed lane membership unless a versioned adjudication approves a new instrument.
3. **Replace binary coverage with an adequacy ledger.** Preserve uncovered requirements, case and boundary support, mutation survival, expected-edge recall, low-N warnings, historical incident coverage, and review ownership.
4. **Type aggregates by exact inventory.** Store included/excluded/skipped/invalid case IDs, lane, denominator, clustering, weights, and version. Do not pool legacy and pure lanes under one unlabeled rate.
5. **Separate mutation claims.** Distinguish treatment applied, target contract changed, observer detected, expected downstream edges moved, unexpected edges moved, aggregate masking, organic incident detected, repair confirmed, and end-to-end consequence improved.
6. **Retain all treatment dispositions.** Attempted, ineffective/no-op, equivalent, invalid, safety-prohibited, recovered, detected, and surviving mutations belong in the denominator appropriate to the claim.
7. **Use post-freeze organic incidents.** The strongest next validation is a prospective stream where slices, cases, and observers were frozen before the regression and diagnosis guides a verified repair.
8. **Measure lifecycle cost.** Report authoring, expert review, fixture maintenance, false blocks, adjudication, baseline revisions, and incident savings alongside runtime and token cost.

### Test

A compact cross-domain deterministic-conformance validation should use two existing artifact-heavy pilots and predeclare:

- one local mutation, one foundational dependency mutation, one observer defect, one case-deletion mutation, one equivalent/no-effect mutation, and one live-only failure;
- expected and prohibited response edges before execution;
- immutable case inventory and separate pure/live lanes;
- baseline-twice and outer-envelope canaries;
- complete mutation disposition and response matrices;
- a task-health/validity claim limited to component conformance unless a frozen organic incident and end-to-end consequence bridge succeed.

The useful test is whether the same machinery distinguishes local implementation drift, foundational propagation, missing observer coverage, instrument tampering, equivalent change, and generative-only failure across different artifact types—not whether it reproduces an ordering-agent taxonomy.

## Concrete repository actions

- [x] Read the complete immutable v1 PDF/text and inspect the complete arXiv source.
- [x] Recheck exact title/path searches and preserve the no-verifiable-release-at-review-time boundary.
- [x] Reconstruct the 23-slice inventory, 238/225/30 count boundary, gate, seven mutations, metrics, tenant replication, organic negative results, and cost claims with page evidence.
- [x] Separate deterministic conformance, aggregate masking, designed sensitivity, dependency-response topology, organic localization, stochastic reliability, production consequence, and readiness.
- [x] Compare nonduplicatively with dependency-edge conformance, STRACE, Who&When Pro, Agent Reliability Profile, Harness-Bench, Anthropic task health, and Amazon metrics.
- [x] Add no queue task: existing benchmark-bundle, dependency-edge, artifact-admissibility, trace/root-surface, task-health, metric, validity, and execution-isolation machinery can represent the requirements. The evidence justifies a future validation fixture, not another contract.

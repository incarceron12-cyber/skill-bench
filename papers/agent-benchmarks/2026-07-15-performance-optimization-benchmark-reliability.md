# Performance-optimization benchmark reliability: a runnable patch is not a transportable criterion

## Source and review status

**Deep review of the complete immutable arXiv v1 primary source.** I read the full 12-page paper and verified its title, five-author byline, tables, formulas, limitations, and references against the local canonical PDF. The immutable paper links no author-owned artifact release. Exact-title, arXiv-ID, topic, author, and GitHub repository searches on 2026-07-15 found no official study repository; therefore the reported raw timings, task-level validity matrix, leaderboard snapshot, rescoring code, and annotations could not be independently replayed.

- **Paper:** Zhi Chen, Zhensu Sun, Yuling Shi, David Lo, and Lingxiao Jiang, *Are Performance-Optimization Benchmarks Reliably Measuring Coding Agents?*, arXiv:2607.01211v1, https://arxiv.org/abs/2607.01211v1
- **Version read:** immutable v1, submitted 1 July 2026; metadata contains no withdrawal/retraction notice
- **Date read:** 2026-07-15
- **Local PDF:** `data/papers/pdfs/2607.01211v1-performance-optimization-benchmark-reliability.pdf` (12 pages; SHA-256 `a63c835e42500a340c74ac2717bdddbfcfa3adedac448ed6ed0014a07ebdecaf`)
- **Local text:** `data/papers/text/2607.01211v1-performance-optimization-benchmark-reliability.txt` (SHA-256 `c24c7632d544c2680e66badc2c2c28778171c72d79802fd36afe2d3729de5726`)
- **Immutable HTML:** `data/papers/source/2607.01211v1/2607.01211v1.html` (SHA-256 `0c4b5f2feb648207701fafa049b97c57d5fd99e07105cccd892ab039027fa94c`)
- **Acquisition/release provenance:** `data/sources/releases/2607.01211v1-performance-benchmark-reliability/provenance.json`
- **Tags:** criterion stability, runtime measurement, environment identity, repeated measures, aggregation sensitivity, task health, saturation

## One-sentence contribution

The paper demonstrates that an executable performance oracle has at least three separable failure surfaces—reference-signal transport across machines, score-policy sensitivity over fixed task outputs, and shrinking headroom under outcome-conditioned public coverage—but its strict all-replay admission rule, unmodeled machine/round hierarchy, selected public-output union, and absent study release do not establish a machine-invariant task population, causal rank effect, prospective saturation rate, or general coding capability.

## Why this matters for `skill-bench`

This review advances charter objectives A and B through a controlled case of a broader benchmark problem: **an artifact can be semantically correct while a scored property of that artifact changes with the evaluator environment.** Runtime is obvious, but the same issue applies to spreadsheet recalculation latency, numerical simulation, database-query cost, rendering time, memory use, and other resource-sensitive professional artifacts.

The paper adds an important boundary to the repository's existing execution-validity and artifact-admissibility work:

```text
artifact validity
+ criterion implementation validity
+ repeated-measurement protocol
+ declared environment operating envelope
+ criterion-margin evidence
+ aggregation/loss policy
→ bounded criterion observation
```

None of those terms inherits the others. A patch that builds and passes tests can lack a stable speed advantage. A stable task-level speed ratio can still be aggregated under a tail policy that changes rankings. A stable aggregate on one hardware envelope cannot automatically be transported to another. And a union of the best outcome from several public configured systems is a coverage diagnostic, not one system's capability or reliability.

## Research questions and exact claim ceiling

The paper audits three recent repository-level performance-optimization benchmarks:

1. **RQ1:** Do official reference patches remain evaluable, faster than base, and valid under each benchmark's original criterion across four Google Cloud processor profiles and three rounds?
2. **RQ2:** How do GSO's binary reference-level gate and SWE-fficiency's harmonic aggregation change the ordering and leverage of public submission outputs?
3. **RQ3:** On the replay-valid subset, how many tasks have at least one passing, base-beating, or reference-matching patch among ten public submissions, and what characterizes the remaining reference gap? (Sections II–V, pp. 2–9.)

The full paper supports these bounded claims:

- under the authors' strict intersection rule, many reference patches did not retain their original benchmark-admission signal in every one of twelve machine-round cells;
- SWE-Perf's reference gains are much closer to zero than those in GSO or SWE-fficiency under the paper's common runtime-change summary;
- SWE-fficiency's published harmonic score is highly tail-sensitive for the eight inspected shared submissions;
- changing the aggregation rule while holding one benchmark's released task outcomes fixed can reorder submissions;
- among the selected public outputs and replay-valid GSO/SWE-fficiency tasks, a union over ten submissions covers most tasks at the reference level and nearly all at the base-improvement level.

The paper does **not** establish:

- that a listed benchmark task is universally invalid outside the authors' four-profile envelope;
- a probability that a patch remains valid on a new machine, cloud instance, load state, date, or software stack;
- that processor generation or vendor caused a particular failure;
- that the bounded harmonic floor of `0.5` is a normatively correct score policy;
- that aggregation alone explains cross-benchmark rank differences;
- that one public configured system solves 384/450 tasks, or that a deployable multi-agent portfolio achieves that coverage;
- that public union coverage is contamination-free, statistically representative, or a prospective saturation forecast;
- general performance-engineering capability, professional software quality, production benefit, cost efficiency, safety, or readiness.

## Methodology and system reconstruction

### Three benchmark populations

The audit includes all official tasks from the selected recent peer-reviewed repository-level runtime benchmarks (Table I, p. 2):

| Benchmark | Official tasks | Repositories | Reference/workload construction |
|---|---:|---:|---|
| GSO | 102 | 10 | generated performance tests compare base and optimization commits |
| SWE-Perf | 140 | 9 | repository unit tests filtered around original/PR-modified commits |
| SWE-fficiency | 498 | 9 | annotated workloads compare pre-edit and expert-optimized commits |

Selection required repository-level edits, executable runtime comparison, and a recent visible peer-reviewed benchmark paper. This is a purposive three-family audit, not a sampling frame for all performance benchmarks (Section II.A, p. 2).

### Cross-machine replay design

For RQ1 the authors replay all 740 official reference patches on four 64-vCPU/256-GB Google Cloud machine profiles (Table II, p. 3): Intel Cascade Lake (`n2`), AMD Milan (`n2d`), Intel Emerald Rapids (`n4`), and AMD Turin (`n4d`). Each task is attempted in three rounds per profile, giving twelve intended machine-round observations per task. They preserve benchmark tasks, reference patches, workloads, and validity rules from the latest public repositories before the 30 April 2026 cutoff (Section III.A, pp. 3–4).

The three original-rule checks differ materially (Table III, p. 3):

- **GSO:** correctness/equivalence plus generally at least `1.2×` replay speedup, with a `1.1×` low-test fallback;
- **SWE-Perf:** original and modified commits pass, then 20 timing repetitions, IQR filtering, and recomputed Mann–Whitney minimum gain `δ_i > 0.05`;
- **SWE-fficiency:** workload and correctness guards run, and base mean minus expert-patch mean exceeds twice the post-edit runtime standard deviation.

A task is labeled faster than base only if `T_ref < T_base` in every machine-round cell. It is original-rule valid only if it satisfies its benchmark's rule in every cell. Non-evaluable tasks remain in the official-task denominator (Section III.A–C, pp. 3–4).

This is a conservative **intersection criterion**, not an estimated transport probability. One failed cell rejects the task, while eleven successful cells cannot quantify where or how often it transports. It appropriately protects the later analyses from the weakest observed target, but it does not distinguish a persistent machine effect, one host-instance event, round order, thermal/load state, cache behavior, dependency drift, or threshold crossing.

### Replay evaluability, missingness, and validity

Complete-by-profile counts are 99/98/99/99 for GSO, 138 on each profile for SWE-Perf, and 498 on each profile for SWE-fficiency. Unique non-evaluable tasks are 4, 2, and 0 respectively (Table IV, p. 4). The paper attributes GSO failures to functional equivalence, external data, image decoding, and x86-64 instruction portability; SWE-Perf failures arise from missing image dependencies.

After retaining the official denominator:

| Benchmark | Faster than base in all 12 | Original-rule valid in all 12 |
|---|---:|---:|
| GSO | 91/102 | 39/102 |
| SWE-Perf | 48/140 | 11/140 |
| SWE-fficiency | 470/498 | 411/498 |

(Figure 1 and Section III.C, p. 4.)

The paper usefully separates **runnable**, **directionally faster**, and **criterion-valid**. It does not publish a typed cell ledger distinguishing intended, started, infrastructure-invalid, functionally invalid, measurement-invalid, and substantively below-threshold observations. The aggregate counts therefore cannot reveal whether failures cluster by repository, task family, machine, round, or root cause.

### Runtime signal and variation

To compare benchmarks, the authors transform GSO and SWE-fficiency speedup `s=T_base/T_ref` into runtime change `1/s−1`; SWE-Perf's significance-aware reduction is sign-flipped (Section III.D, pp. 4–5). They report:

| Benchmark | Evaluable tasks | Median runtime change | Median within-task SD over 12 cells | quotient of reported medians |
|---|---:|---:|---:|---:|
| GSO | 98 | −54.20% | 3.81 percentage points | 0.07× |
| SWE-Perf | 138 | −0.03% | 1.41 points | 43.23× |
| SWE-fficiency | 498 | −56.04% | 2.41 points | 0.04× |

(Table V, p. 5.) The compelling descriptive result is not that SWE-Perf has more absolute variation; it has almost no median reference signal. The paper notes 101/138 SWE-Perf tasks have median changes within five points of zero.

However, the twelve-cell standard deviation pools **between-profile shifts and within-profile rounds**. With no variance decomposition, profile replication, profile-by-task interaction estimate, confidence interval, or prospective held-out machine, it cannot be read as a machine-transport variance component. The reported `std./signal` is also a quotient of benchmark-level medians, not a task-level reliability statistic; near-zero denominator makes its scale explosive. It is a useful signal-margin warning, not a calibrated stability coefficient.

### Scoring rules and ranking analysis

GSO's `OPT@1` gives one equal binary success per task when a correct submission matches or beats the reference patch. SWE-fficiency defines per-task speedup ratio `SR = speedup_submission/speedup_reference`, floors it at `0.001`, and takes a harmonic mean:

`HM = N / Σ_i [1 / max(SR_i, 0.001)]`.

Thus one floor-level task contributes 1,000 denominator units versus one unit for a reference-matching task (Section IV.A, pp. 5–6).

Eight named OpenHands-based submissions appear in both public leaderboards. Their official rankings disagree on 9/28 unordered pairs (Spearman `0.452`). Reapplying a GSO-style binary gate to fixed SWE-fficiency outputs yields correlation `0.762` with GSO and 6/28 flips; applying harmonic scoring to available fixed GSO outputs yields `0.238` and 11/28 flips (Tables VI–VII, p. 6).

This establishes **policy sensitivity**, but not a clean causal decomposition of the official cross-benchmark disagreement: the benchmarks have different task populations, workloads, references, and validity processes. Even the alternate-rule comparisons ask whether one population's fixed outputs become more like the other population's ranking. The strongest within-record evidence is simply that ranks change when the aggregator changes.

For each SWE-fficiency submission, the paper computes task share of the harmonic denominator. The worst ten tasks account for 58.5%–82.8%, and one `SR=0.00134` task accounts for 33.6% for one submission (Figure 3, p. 6). Raising the diagnostic floor to `0.5` changes 6/8 ranks and 8/28 pair orders (Table VIII, p. 7). The authors correctly present `0.5` as a diagnostic, not the right constant. The deeper issue is use: a strict worst-tail penalty may be legitimate for a noncompensatory deployment use, but illegitimate if presented as broad average optimization skill. Weight concentration must be declared alongside the stakeholder loss interpretation.

### Public-output coverage and “saturation”

RQ3 uses only the strict replay-valid subset: 39 GSO and 411 SWE-fficiency tasks. SWE-Perf is excluded because it has only eleven replay-valid tasks and no comparable public solution outputs. Across ten public submissions, the authors select the best observed task outcome and report (Figure 4, pp. 7–8):

- all 450 tasks have at least one passing patch;
- 449/450 have at least one passing patch faster than base;
- 384/450 have at least one patch matching or beating the reference;
- 66 remain below reference: 9 GSO and 57 SWE-fficiency.

Among those 66, every task has a correct public patch, 65 beat base, and the median best/reference speedup is 85.3% for GSO and 87.9% for SWE-fficiency. The union is explicitly optimistic and does not describe one submission (Section V.A–B, pp. 7–8).

This is best called **selected public portfolio coverage**, not task saturation. It is outcome-conditioned on the best of ten correlated OpenHands-based configurations, restricted to tasks whose references survive the strict replay filter, and based on one leaderboard snapshot. It has no held-out systems, future submissions, attempts-per-submission model, contamination audit, portfolio execution policy, or joint cost/reliability estimate. Increasing the number or diversity of submissions mechanically raises union coverage. Conversely, excluding unstable tasks makes the remaining denominator cleaner but changes what “85.3% covered” refers to.

### Strategy annotation

For 66 reference misses, GPT-5.5 assigns one high-level optimization category to reference and best-public patches using a prior taxonomy; labels are schema-checked and manually sanity-checked against diffs. Thirty-two pairs share a category, 34 differ or show no production optimization. After excluding two no-optimization cases, same-category patches are closer on median (`89.8%` versus `81.1%`) but overlap substantially (Section V.C, pp. 8–9).

The evidence supports a descriptive category-gap association only. A single model annotator, no released item labels, no blinded human protocol, no agreement statistic, coarse mutually exclusive categories, and outcome-selected best patches prevent a validated claim that “implementation depth” rather than strategy choice causes the residual gap.

## Evidence: what is unusually useful

1. **Criterion transport is tested against the criterion's own admission rule.** The paper does not substitute one universal threshold for three benchmark definitions.
2. **Runnable and valid are separated.** Most tasks execute while many lose the reference signal; this is exactly the distinction benchmark task-health records need.
3. **Signal margin is more informative than noise magnitude alone.** SWE-Perf's problem is a near-zero reference contrast, not the largest absolute runtime variation.
4. **Task leverage is made visible.** The harmonic denominator-share audit reveals how a nominal 498-task score can behave like a small worst-tail panel.
5. **Coverage is milestone-specific.** Passing, beating base, and reaching reference are shown separately rather than collapsed into “solved.”
6. **The authors bound several interpretations.** They call the bounded floor diagnostic, the ten-submission union optimistic, and the benchmark selection nonexhaustive; they do not claim a replacement leaderboard.

## Unique insight: criteria need operating envelopes, not just deterministic code

The paper's most transferable insight is that **criterion reproducibility is a property of a measurement package, not of an executable checker alone**.

For an environment-sensitive criterion, `skill-bench` should preserve:

```text
criterion target and unit
→ authoritative artifact/state
→ environment identity and admissible envelope
→ workload/input and preparation state
→ warmup/order/cache/concurrency protocol
→ repeated raw observations and invalid-cell reasons
→ paired reference/base/candidate contrast
→ validity margin and uncertainty
→ aggregation, tail leverage, threshold, and loss policy
→ transport/expiry evidence
```

This differs from ordinary launcher isolation. A sandbox can be perfectly isolated yet produce an unstable criterion because the measured property depends on CPU, renderer, spreadsheet engine, solver, library, concurrency, or workload state. Conversely, a criterion may be stable within one operating envelope while not transporting outside it. Environment identity should therefore attach both to the **trial** and to the **criterion's evidence of admissibility**.

A second insight is to separate four lifecycle labels:

- **replayable:** the task and reference execute;
- **criterion-valid here:** the reference meets the rule in this environment cell;
- **transport-supported:** the criterion retains its interpretation over a declared envelope with repeated evidence;
- **decision-stable:** the downstream system comparison survives reasonable aggregation/loss policies for its intended use.

“Saturated” is a fifth, independent use-indexed judgment. It requires a declared system/portfolio population, attempts, time, cost, milestone, and renewal decision; best-of-ten historical union coverage is only one diagnostic input.

## Limitations and validity threats

1. **No study release.** Raw timing cells, task lists after each gate, scripts, environment images, exact repository commits, public outputs, rescoring code, and category labels are unavailable for audit.
2. **Four profiles are not a machine population.** The study spans useful processor families but does not define an inference frame over hardware, clouds, regions, kernels, virtualization, or load states.
3. **Machine type and instance realization are unclear.** The paper does not report independent instances per profile; profile effects can be confounded with specific host instances.
4. **Only three outer rounds.** The design cannot characterize temporal tails, drift, or rare noisy runs.
5. **No hierarchical variance decomposition.** The pooled twelve-cell SD mixes machine, round, interaction, and measurement effects.
6. **No task-level uncertainty release.** Counts use a hard all-cells rule without confidence intervals or prospective transport validation.
7. **Intersection validity is conservative but use-dependent.** One threshold crossing rejects a task regardless of eleven stable cells or the intended deployment envelope.
8. **Different benchmark validity rules are not commensurate.** Comparing retained fractions is descriptively useful but not a common reliability scale.
9. **Near-zero SWE-Perf signal is partly construction-conditioned.** The paper plausibly links it to workload selection, but does not experimentally change workload stress while holding patches fixed.
10. **Non-evaluable cells remain coarsely typed.** Aggregate root-cause prose is not a complete intended/invalid/missing/retry ledger.
11. **No cost or compute accounting.** The scale of 740 tasks across twelve cells plus benchmark-internal repetitions is not operationally documented.
12. **Cross-benchmark rank disagreement is multiply confounded.** Task sets, references, workloads, validity filters, and aggregation all differ.
13. **Alternate-rule comparisons do not isolate one universal ranking.** They retain one population's outputs and compare against another population's ordering.
14. **The `0.5` floor is intentionally arbitrary.** It demonstrates sensitivity but supplies no stakeholder loss basis.
15. **Denominator share is not criterion importance.** A high-leverage task can reflect a severe meaningful failure, an invalid run encoded near zero, or a measurement defect; adjudication is required.
16. **Eight shared submissions are a selected configured-system sample.** No uncertainty over systems or leaderboard evolution is estimated.
17. **Public-output union is outcome-selected.** Best-of-ten coverage increases with portfolio size and cannot be attributed to one system.
18. **All submissions share OpenHands lineage.** Scaffold dependence and correlated error reduce claims about diverse agent populations.
19. **Replay-valid-subset selection changes the hardness denominator.** Fragile tasks disappear before coverage analysis.
20. **No repeated agent trials are analyzed.** Reference timing repetition does not establish configured-agent reliability.
21. **Public exposure and contamination are untested.** High coverage may reflect genuine capability, benchmark adaptation, exposure, or selection.
22. **The strategy observer is weakly validated.** One GPT-5.5 label per patch, coarse categories, manual sanity checks, and no agreement/release do not support causal failure attribution.
23. **Reference patches are witnesses, not unique optima.** Matching a reference speed does not prove globally optimal or professionally preferred engineering.
24. **Correctness guards may be incomplete.** Passing benchmark tests does not establish semantic equivalence, maintainability, portability, security, or production regression safety.
25. **Operational realism remains bounded.** Tasks expose the region/workload/stress test more directly than real performance engineering usually does (Discussion, pp. 9–10).
26. **No professional or consequence evidence.** Runtime score changes are not measured developer productivity, user latency, infrastructure cost, or business value.

## Reproducibility and operational realism

Paper inspectability is **moderate**. The immutable v1 clearly specifies task counts, machine profiles, high-level cutoff, original validity rules, score formulas, headline counts, rank comparisons, and key limitations. These details make the estimands and several arithmetic implications understandable.

Computational reproducibility is **low** for this audit itself. The study release is absent after paper-link and broader repository searches. The three upstream benchmark releases may permit a future independent reconstruction, but they do not substitute for the authors' exact task snapshots, machine metadata, raw twelve-cell measurements, public-submission snapshot, transformations, exclusions, and analysis code. None of the paper's empirical tables was independently reproduced in this review.

Operational realism is **moderate for executable repository optimization** and limited for production performance engineering. Real repositories, reference patches, correctness guards, cloud CPUs, noisy timings, and workload-sensitive scores are valuable. But the tasks largely begin after workload and optimization target construction; they omit much hotspot discovery, representative traffic selection, multi-resource tradeoffs, deployment canaries, maintainability review, and downstream consequence measurement (Discussion, pp. 9–10).

## Relation to existing `skill-bench` evidence

- **Stochastic Agent Evaluations** shows that repeated agent outcomes need decision-specific estimands and typed service/grader variation. This paper adds repeated **criterion** observations: even fixed base/reference artifacts can change status across environment cells. Neither a trial-repeat count nor a runtime SD is an intrinsic system-reliability scalar.
- **Partial agent-benchmark decisions** shows that evaluation reduction is claim-indexed. Here, aggregation is also use-indexed: equal binary coverage and a severe-tail harmonic policy answer different decisions.
- **WorkBench Revisited** separates frozen anchors, corrected operational forms, and renewal forms. Performance criteria add an environment bridge requirement: old/new machine and workload envelopes need cross-measured anchors before trend claims.
- **Task-health machinery** already distinguishes executable witnesses, defects, transitions, and retirement. The paper's runnable→faster→original-rule-valid ladder and per-task leverage are direct health signals, not a reason for a new lifecycle schema.
- **Reasoning/coding benchmark evolution** treats LiveCodeBench freshness and executable equivalence as bounded repairs. This paper adds that executable equivalence and runtime improvement are separate predicates; rolling or fresh tasks do not repair a weak performance margin.

## Transfer to `skill-bench`

### Retain

1. Preserve reference/base/candidate artifacts and replay them under the exact criterion rather than treating historical labels as timeless.
2. Separate evaluability, semantic/artifact validity, direction of improvement, criterion validity, and reference-level attainment.
3. Keep task-level observations and score leverage visible beside aggregates.
4. Compare aggregation policies using fixed observations, while labeling each policy by intended use and loss.
5. Report milestone-specific portfolio coverage rather than one saturated/not-saturated label.

### Repair

1. Bind every resource-sensitive check to an explicit operating envelope: software engine/version, hardware class, resources, concurrency, workload, warmup, cache/state preparation, timeout, repetition, and invalid policy.
2. Preserve raw repeated observations and decompose task, environment, round/batch, and interaction effects where the design supports it.
3. Require a criterion margin relative to observed variation and decision threshold; do not admit near-zero witnesses merely because one historical run crossed a cutoff.
4. Treat environment transport as a held-out bridge question. Validate on new machines/engines/workload forms before promoting a criterion from local validity to transport-supported.
5. Report influence/leverage, severe-failure identity, and bounded-policy sensitivity. Do not choose harmonic, mean, median, minimum, or noncompensatory gates without a stakeholder loss interpretation.
6. Type best-of-portfolio analyses by eligible systems, attempts, scaffold dependence, time/cutoff, selection policy, costs, and joint execution feasibility.
7. Keep correctness, performance, maintainability, safety, resource tradeoffs, and professional acceptance as plural outcomes.

### Test

A useful cross-domain conformance test should take one artifact with a resource-sensitive criterion—such as a spreadsheet recalculation or simulation—and:

1. freeze the artifact, input/workload, semantic correctness checks, and reference witness;
2. execute base/reference/candidate under at least two engine or machine versions with repeated blocked rounds;
3. preserve every intended/valid/invalid cell and typed root cause;
4. estimate environment and repeat effects separately where possible;
5. apply predeclared mean, tail, and noncompensatory decision policies;
6. show which task conclusions and configured-system decisions transport;
7. keep capability and professional-validity claims false unless independent evidence supports them.

Useful completion would demonstrate that the existing benchmark-bundle, task-health, metric-monitoring, execution-validity, and validity-argument contracts can represent a criterion operating envelope and produce a fail-closed report. It would not require a new performance-specific schema.

## Concrete repository actions

1. **No new build task.** Existing environment identity, repeated response/trial records, task health, metric specification, aggregation sensitivity, and validity arguments are the correct implementation homes.
2. During the next execution/reliability consolidation, add the four-state distinction `replayable → criterion-valid here → transport-supported → decision-stable`, with saturation kept separate and use-indexed.
3. When an artifact-heavy pilot gains a resource-sensitive criterion, run the cross-engine/machine conformance test above before using that criterion in a system ranking or trend claim.

## Bottom line

The paper convincingly falsifies a common shortcut: an official executable reference patch is not automatically a stable measurement target, and hundreds of task scores do not guarantee broad influence when the aggregation rule concentrates weight in a handful of failures. Its strongest evidence is descriptive and diagnostic: strict cross-machine reference retention, signal-margin differences, and score-policy sensitivity. Without raw study artifacts, a hierarchical transport design, held-out environments, repeated agent trials, or a declared stakeholder loss model, it cannot identify machine-invariant validity, causal leaderboard effects, portfolio capability, saturation, or professional performance-engineering competence. `skill-bench` should adopt the criterion-operating-envelope boundary and reuse its existing contracts rather than build a coding-specific subsystem.
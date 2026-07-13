# Paper Review: Signals — Enriched Review Yield Is Not Failure Prevalence

- **Paper:** https://arxiv.org/abs/2604.00356v1
- **Authors:** Shuguang Chen, Adil Hafeez, Salman Paracha
- **Date read:** 2026-07-14
- **Source:** complete immutable arXiv v1, submitted 1 April 2026
- **Local PDF:** `data/papers/pdfs/2604.00356v1-signals-trajectory-triage.pdf` (10 pages; SHA-256 `ca8f534c6a5702d540ab7df36e580df923772faab7316e056c80e74f6f04e29b`)
- **Local text:** `data/papers/text/2604.00356v1-signals-trajectory-triage.txt` (SHA-256 `7976eecc91bd19783f87fa52ac27162c4e3337c996d60776e7720b6ff5cbcb23`)
- **Immutable source:** `data/papers/source/2604.00356v1-source.tar.gz` (SHA-256 `387100cd802a1349bc1a429241a5ce9933f217ed0a23241f5b34897a4be95703`)
- **Post-paper implementation inspected:** https://github.com/katanemo/plano at merge commit `c8079ac971a2931df2ec3fc464d2f7d26e0ec1df` (23 April 2026); local archive `data/sources/releases/2604.00356v1-signals/katanemo-plano-c8079ac.zip` (SHA-256 `54ff56b55f31d9935b4b9d3e09a0d559be20bb5cfbd6c09baa3cf23964c0bf17`)
- **Release provenance:** `data/sources/releases/2604.00356v1-signals/provenance.json`
- **Tags:** trajectory-triage, sampling-validity, human-review, production-monitoring, annotation-efficiency, selection-bias

## One-sentence contribution

Signals proposes inexpensive lexical and event-pattern detectors to enrich a fixed review queue and reports that 82 of 100 signal-selected historical τ-bench trajectories were majority-labeled “developer-informative,” versus 74 of 100 selected by a ten-user-message rule and 54 of 100 sampled randomly; this is useful evidence for **case-finding yield in one undisclosed pool**, but omitted pool, detector, inclusion, overlap, cost, annotation, and run records—plus dependence-blind inference and a post-paper implementation that emits the quality scores the paper disavows—block claims about representative failure prevalence, detector accuracy, general production utility, or valid preference data.

## Why this matters for skill-bench

The paper addresses a missing operational link in `skill-bench`:

`large trajectory population → bounded review sample → observations/adjudication → task or system change`.

Existing trace, grader, task-health, metric-monitoring, and validity machinery can preserve what a reviewer found. It cannot make that finding representative if the review queue was outcome-enriched and its selection policy was lost. Signals makes that boundary concrete. A cheap detector can be valuable because it raises discoveries per review hour while simultaneously making the resulting sample unsuitable for unweighted prevalence, system comparison, safety incidence, or benchmark calibration.

This advances charter objectives A–C through a cross-domain sampling-validity question. τ-bench customer-service trajectories are a test substrate, not a proposal to narrow the benchmark to customer support.

## Research question and claim boundary

The empirical question is whether signal-based sampling surfaces more trajectories that a developer could use to form at least one plausible agent-improvement hypothesis than either uniform sampling or a simple long-conversation filter, under a nominally fixed review budget (Section 4, pp. 5–7).

The full source supports a narrow descriptive result:

- in three 100-slot samples from an unspecified historical τ-bench pool, majority labels marked 82 signal, 74 heuristic, and 54 random slots developer-informative;
- the signal–random difference is large under the paper's row-independent Fisher test, while signal–heuristic is not significant (`p=.232`);
- within the sampled reward-zero and reward-one subsets, signal-selected rows have higher observed informative proportions than random rows;
- three annotators show moderate AC1 agreement (`.477`) on the binary label and stronger reason-category agreement on the selected subset where all three already agree the row is informative;
- a later author-associated company release implements inspectable detector logic and OTel emission for the taxonomy.

It does **not** establish detector sensitivity, specificity, calibration, or recall against all informative trajectories; representative failure or issue prevalence; unbiased comparison among agents, tasks, domains, or time periods; a production cost saving; causal improvement from reviewing selected cases; validity of generated preference pairs; or professional capability, safety, production fitness, or readiness.

## Methodology and system reconstruction

### Signal construct and detectors

The paper groups observable patterns into interaction, execution, and environment layers (Section 3, pp. 3–5):

- **interaction:** misalignment, stagnation, disengagement, satisfaction;
- **execution:** failed/non-advancing actions and repeated or oscillating loops;
- **environment:** exhaustion from API, resource, network, malformed-response, or context conditions.

Interaction and execution signals are called learning-oriented; environment signals are diagnosis-only. Detection is described qualitatively: typo-tolerant phrases, nearby-turn similarity, repetition/length heuristics, structured non-advancing outcomes, repeated calls or argument drift, multi-tool cycles, and external-failure markers. The manuscript deliberately says signals are descriptive and not quality scores (pp. 1–4).

That distinction is conceptually healthy but operationally incomplete. Section 4 says all interaction and execution signals are “aggregated into a composite triage score” that prioritizes rows (p. 5), yet gives no formula, weights, threshold, tie-breaking, quota, randomization, or handling of rows with equal/multiple activations. A triage score need not claim quality, but it is still the treatment that determines inclusion. Without it, neither the selected sample nor the 82% yield can be reproduced.

The detector descriptions also hide construct choices. A repeated call can be a loop or legitimate polling; an empty result can be a correct negative search or a failure; a user correction can reflect agent error, user error, evolving requirements, or simulator behavior; an API error can follow a bad agent request. The environment/execution split is assigned by which indicator is “dominant” (p. 5), with no adjudication or counterfactual rule. These signals should remain candidate surface observations until linked to evidence and root-cause status.

### Pool and eligibility frame

The pool consists of “publicly available historical” τ-bench trajectories across all airline and retail tasks, multiple model backbones, and multiple prompting strategies (Section 4.1, p. 5). The paper denotes its size only as `N`. It does not disclose:

- `N`, trajectory IDs, source release, retrieval date, or hashes;
- model, prompt, harness, user-simulator, task, domain, reward, or run composition;
- whether configurations have equal numbers of attempts;
- invalid, truncated, duplicate, retried, or missing trajectories;
- temporal order or whether outputs were used while tuning detectors;
- how the three 100-slot samples overlap.

Uniform sampling can be unbiased for this hidden pool if executed as stated, but the paper cannot support a population estimate without the pool and selection record. Calling the random arm's observed 37% failure share the pool “base rate” (p. 6) also overstates one 100-row sample realization unless the sampling design or complete pool count is supplied.

Task and configuration dependence matter. Multiple systems execute the same tasks, and multiple trajectories may share agent, prompt, simulator, tool schema, or source incident. A 300-slot analysis is not automatically 300 independent units. If the same trajectory appears in several arms, Fisher tests are additionally paired/overlapping rather than independent; if duplicates were displayed repeatedly, annotators could recognize them and infer conditions.

### Sampling arms

Each arm contributes 100 sample slots:

1. uniform random from the full pool;
2. trajectories with at least ten user messages;
3. signal-ranked trajectories using all interaction and execution groups, excluding environment signals (p. 5).

Equal slot counts do not mean equal review budgets. Long conversations require more time, and the heuristic arm deliberately selects them; signal-selected rows may differ in turns, tool calls, screenshots, or state complexity. The paper records neither review minutes, token/trace length, annotator wage, interface latency, detector compute, nor adjudication time. It therefore estimates yield per sampled trajectory, not yield per dollar or hour.

The source archive contains commented-out earlier design prose with concrete thresholds, OTel fields, failure/exemplar streams, and a preference-data recipe, but these are not part of the published method and cannot fill the missing empirical selection policy.

### Annotation instrument and authority

Three annotators “familiar with agentic systems and tool-use patterns” independently review all 300 slots in one shuffled queue while blinded to arm (p. 5). Their identities, roles, experience, recruitment, training, calibration, interface, evidence view, time, and conflicts are absent. Blinding to the arm label is useful, but long conversations and obvious signal cues can reveal the heuristic or signal treatment.

A row is positive if it contains enough concrete evidence to form at least one **plausible hypothesis** for improving the agent. The six single-select reasons are action/tool-use issue, conversation issue, external-system issue, success exemplar, none/unclear, and other, with priority rules favoring execution over conversation when execution is “key” (pp. 5–6).

This criterion measures review ideation, not confirmed defect or successful intervention. It is also proximal to the selection features: corrections, retries, repetition, frustration, and explicit success provide exactly the visible evidence from which a reviewer can state a plausible hypothesis. The experiment therefore shows that feature-rich cases are more often judged hypothesis-generating. It does not show that the hypotheses are correct, important, novel, fixable, or useful after implementation.

Majority vote produces the binary target. The paper does not explain aggregation for the six-way reason label when all three choose different categories or two rate the row non-informative. Table 2 nevertheless assigns every majority-informative row to only action/tool-use, conversation, or success exemplar; no external, other, or unclear rows appear, and the three displayed counts sum exactly to 54, 74, and 82. Annotator-level labels, ties, notes, and adjudication lineage are unavailable.

### Agreement evidence

Individual positive rates range from `.57` to `.74`, a material 17-point spread. Three-rater Gwet AC1 is `.477`, which the authors call moderate. They assert that disagreement is concentrated at an actionable-evidence threshold and that this is “confirmed” by higher reason-category agreement among the 130 trajectories where all three already agree the row is informative (p. 6).

That conditioning cannot confirm the explanation. Selecting unanimous positives removes the binary boundary disagreements by construction and retains easier or more salient cases. High reason agreement in that selected subset does not establish a common informativeness threshold, label validity, or expected agreement on the operational review queue. No repeated labels, held-out calibration, annotator effects, uncertainty on agreement, or downstream criterion is reported.

### Metrics and statistical analysis

The primary metric is majority-positive rows divided by 100 sampled slots. Table 1 reports exact Clopper–Pearson intervals and pairwise Fisher tests. These methods are exact for independent Bernoulli rows under their assumptions, but they do not account for overlap among arms, repeated tasks/configurations, detector development on the same pool, or uncertainty in the human target.

The reported counts reproduce the paper's pairwise Fisher results under its independence assumption:

- signal vs random overall: `p≈3.50e-5`;
- signal vs heuristic overall: `p≈.232`;
- signal vs random among reward-zero rows: `p≈.00669`;
- signal vs heuristic among reward-zero rows: `p≈.0409`;
- signal vs random among reward-one rows: `p≈.0123`;
- signal vs heuristic among reward-one rows: `p≈.161`.

These local calculations verify the table's marked comparisons; they do not repair the design. Multiple overall, reward, domain, and category analyses are interpreted without a declared multiplicity family. The successful-stratum signal–heuristic contrast is not significant, and the failed-stratum contrast is borderline before multiplicity adjustment. “Robust across reward strata” is therefore too strong if robustness means demonstrated superiority to the practical heuristic rather than positive point differences.

The paper calls its reward reweighting “counterfactual standardization” (p. 7). It multiplies each arm's within-reward informative rates by the random sample's 63/37 reward mix, yielding 77.6%, 62.7%, and 54.0%. This is direct descriptive standardization to an estimated two-stratum mixture, not a counterfactual intervention analysis. It controls only binary reward—not task, domain, agent, prompt, turns, or configuration—and reports no uncertainty for the standardized contrasts.

Domain results give only rounded rates: airline 86–96%, retail 78/66/35%. Denominators, configured-system composition, intervals, tests, and standardized estimates are absent. Two author-chosen domains, one with a ceiling, do not establish domain robustness.

Table 2's reason mix is conditioned on being majority-informative, an outcome affected by sampling. Similar conditional percentages cannot show that the sampler is unbiased over issue type. No comparison test is reported, rare categories have counts of zero to three, and missing external/other categories are unexplained.

### Efficiency claim

The paper computes sampled trajectories per informative majority label: `100/82=1.22`, `100/74=1.35`, and `100/54=1.85`, then reports `1.85/1.22=1.52×` efficiency relative to random (p. 7). The ratio is arithmetically correct for sample-slot yield.

But all three annotators label every slot. In human judgment units, the corresponding counts are `300/82=3.66`, `300/74=4.05`, and `300/54=5.56` individual binary decisions per majority-positive row, before notes or adjudication. The ratio remains 1.52×, but “1.22 labels” understates the absolute annotation operation. More importantly, no time or cost is measured. The valid estimand is **majority-positive trajectories per 100 reviewed slots**, not production review efficiency per unit labor or total system cost.

## Evidence interpretation

### What is supported

1. Cheap observable features can materially enrich a finite review queue for a broad, permissive “hypothesis-generating” label in this selected historical τ-bench pool.
2. Reward-zero rows are often informative under all methods; signal sampling also finds majority-positive reward-one rows, showing endpoint reward and review interest are not identical.
3. The positive label has only moderate agreement, so review-worthiness is a rater- and threshold-conditioned observation rather than ground truth.
4. Enriched review and representative monitoring need separate sampling streams.
5. A later implementation demonstrates that the qualitative taxonomy can be compiled into deterministic code and telemetry.

### What is not supported

The study does not show how many informative rows signal selection misses, because it does not label the full pool or a probability sample large enough to estimate detector recall by score. It does not establish issue prevalence from enriched samples, compare agents fairly, identify root causes, verify suggested fixes, measure intervention benefit, or construct/evaluate preference data. The phrase “genuine per-trajectory informativeness gains” is limited to sampled rows under one annotation policy; it is not a portable detector property.

## Post-paper implementation audit

A renewed release search found an author-associated follow-on that was absent from the manuscript. Katanemo's public Plano PR #903 was merged 22 days after arXiv v1 at commit `c8079ac971a2931df2ec3fc464d2f7d26e0ec1df`. Issue #908 names the three paper authors as paper DRIs and says Plano is implementing the paper; the PR calls itself a Rust port of a Python reference at `katanemo/signals`. The latter repository is not publicly accessible at review time. The complete 712-file snapshot was archived; 27 paths implement or test Signals.

This is credible post-paper implementation evidence, not the empirical release. It contains no historical τ-bench pool, sample IDs, detector outputs on that pool, 900 labels, majority labels, analysis rows, or paper tables. Its parity harness compares Rust and Python on 2,000 LMSYS chats, but the README says only 10 of 20 leaf types naturally fire there and execution/environment parity relies on unit fixtures. A port matching a private reference tests implementation equivalence, not detector validity against human labels.

The release also exposes a material paper-to-operation divergence. The paper says signals are not quality scores and environment signals are diagnosis-only. Yet `crates/brightstaff/src/signals/analyzer.rs:230-298` starts at 50, rewards satisfaction, subtracts misalignment, stagnation, execution failures, loops, and **environment exhaustion**, then bins `excellent/good/neutral/poor/severe`. `schemas.rs:151-169,314-335` makes `overall_quality` and `quality_score` first-class report fields; `otel.rs` emits them. The PR smoke output visibly reports `signals.quality` and `signals.quality_score`.

This later code cannot be imputed backward to the v1 experiment, but it demonstrates a lifecycle risk: descriptive observability features can become unvalidated quality metrics downstream even when the paper explicitly warns against that move. `skill-bench` should require claim/use metadata and consumer lineage for derived signals, not rely on naming intent.

## Unique insight

The deepest transferable lesson is that **trajectory triage creates two different datasets, and neither can silently stand in for the other**:

```text
probability sentinel sample
  → prevalence, drift, subgroup rates, false-negative audit

enriched review sample
  → efficient discovery, diagnosis candidates, task candidates, rare-pattern investigation
```

The enriched stream optimizes review yield by changing inclusion probability. That is its value, not a nuisance to hide. But it cannot estimate prevalence or compare systems without a known design, weights, and adequate support. Conversely, the sentinel stream is inefficient for discovery but is the anchor needed to know what the enriched stream misses and whether traffic changed.

A second ladder is equally important:

`signal activation → reviewer-interest label → supported defect → accepted intervention → replay/field effect → downstream utility`.

Signals measures only the first two links. A plausible improvement hypothesis is not a verified failure, and a verified failure is not evidence that a fix improves users, safety, cost, or professional work.

## Relation to existing project evidence

- **AgentRewardBench** asks whether automatic trajectory judgments match expert observations under different evidence views. Signals sits one stage earlier: which trajectories are even sent for judgment. The two errors compound; a biased queue and imperfect judge cannot be diagnosed from one pooled agreement number.
- **AgentLens** provides inspectable trajectory reviews and regression routing but lacks representative production sampling. Signals contributes the missing selection-policy question but no diagnostic report, intervention ledger, or production outcome.
- **Amazon and Anthropic production evaluation** describe log-derived task creation, task health, dashboards, and adjudication. Signals gives a quantitative queue-yield case, but omits the population, ownership, and lifecycle records those methods require.
- **Nubank** links offline evaluations to selected online outcomes. Signals stops before preference construction or deployment effect; its proposed optimization flywheel is future work.
- **Many-Facet rater evidence** requires preserving rater, criterion, task, and interaction effects. Signals instead collapses three labels by majority while its `.477` AC1 shows that rater threshold is a material part of the instrument.
- **Existing metric-monitoring, task-health, trace/grader, configured-system, and validity contracts** already contain the proper homes. The gap is exercising them with explicit review-sample selection, not adding a Signals-specific schema.

## Limitations and validity threats

1. The eligible pool size `N`, release, date, IDs, hashes, and composition are absent.
2. Agent, prompt, simulator, task, domain, and run-attempt weights are undisclosed.
3. Invalid, missing, retried, duplicate, or truncated trajectory handling is unspecified.
4. Detector rules, lexical sets, normalization, thresholds, score formula, weights, and tie-breaking are absent.
5. Signal detector development and empirical evaluation may use the same historical pool; no development/confirmation split is reported.
6. Sampling seeds and exact inclusion probabilities are absent.
7. Cross-arm overlap is not reported, so independence and blinding cannot be audited.
8. Shared tasks/configurations induce clustering ignored by intervals and tests.
9. The signal sampler may be deterministic top-k rather than probability sampling, leaving the inference population undefined.
10. The random arm's 37% failure share is a sample estimate, not a released pool base rate.
11. Equal trajectory counts do not equal human time or cost.
12. Annotator expertise is described only as familiarity with agents and tool use.
13. The annotation instrument, interface, evidence-view record, training, and calibration are unreleased.
14. Blinding to arm is partially inferable from trajectory length and visible signal cues.
15. “Developer-informative” means a plausible hypothesis, not confirmed defect or successful fix.
16. The target is proximally aligned with the features used to select rows, encouraging criterion circularity.
17. Individual positive rates differ by 17 points and AC1 is only `.477`.
18. The claim that disagreement is merely threshold disagreement is not tested.
19. Reason agreement is conditioned on unanimous positive rows and cannot validate the binary boundary.
20. Six-way reason aggregation, ties, notes, and adjudication are unspecified.
21. Table 2 omits three declared categories and conditions on the sampler-affected outcome.
22. Fisher and Clopper–Pearson calculations assume independent rows and ignore label uncertainty.
23. Multiple overall, stratum, domain, and category comparisons lack a declared multiplicity policy.
24. Signal does not significantly beat heuristic overall or among reward-one rows under the paper's own tests.
25. Reward standardization controls only one post-outcome binary variable and has no uncertainty.
26. Calling direct reweighting “counterfactual” overstates its causal content.
27. Domain results omit denominators, uncertainty, tests, and configuration mix.
28. Two simulated domains do not establish domain or real-user robustness.
29. Reward-one does not mean policy-correct or professionally useful; reward-zero does not identify agent fault.
30. Signal recall and false-negative rates over the full eligible pool are unmeasured.
31. No intervention, repair, replay, recurrence, or downstream outcome validates developer utility.
32. No preference pairs, training experiment, contamination control, or post-training evaluation support the proposed learning path.
33. No measured human hours, dollars, latency, detector overhead, or cost-quality frontier supports production efficiency.
34. The empirical pool, labels, notes, sample records, and analysis code are unreleased.
35. The post-paper release is not a paper-time implementation and contains none of the empirical study records.
36. The later release's parity set covers interaction chat, not natural execution/environment instances.
37. The later release emits quality and environment-conditioned scores that conflict with the paper's stated use boundary.
38. No evidence supports population representativeness, general failure detection, professional validity, capability, safety, production fitness, or readiness.

## Reproducibility and operational realism

Paper-level readability is good: the immutable v1 PDF/source provides the full taxonomy, annotation target, three sample sizes, count tables, agreement summaries, intervals, tests, reward standardization, domain point rates, and limitations. The main count-based Fisher comparisons and 1.52× slot-yield ratio can be reconstructed.

Experiment reproducibility is poor. The paper and source archive provide no empirical artifact URL, and the renewed search found no author-owned τ-bench pool, detector output, sampling ledger, labels, notes, or analysis release. Exact regeneration is impossible without guessing the pool and the treatment. Even the primary sample rows cannot be identified.

The post-paper Plano archive materially improves detector inspectability: it contains typed Rust detectors, thresholds, tests, OTel emission, and a parity harness. But it is a later product realization, references an unavailable Python source, and cannot reproduce the paper's τ-bench sample or findings. Its quality-score divergence reinforces the need to version not only detector code but the permitted downstream use.

Operational realism is moderate for the problem and low for the evidence. Always-on cheap triage, tool failures, user corrections, loops, resource exhaustion, and bounded reviewer attention are real concerns. The evaluation uses historical benchmark traffic, simulated users, no production denominator, no measured review cost, no intervention, and no outcome. It validates a selected queue's label yield, not production operation.

## Transfer to skill-bench

### 1. Preserve a review-selection episode

Before review, bind:

- immutable eligible-population snapshot and unit IDs;
- task/domain/system/harness/time strata and duplicate clusters;
- detector and normalization hashes, signal instances, score/priority formula, thresholds, tie-breaking, exclusions, and budget;
- random seed, with/without-replacement policy, inclusion probability, overlap, and nonresponse/invalid handling;
- intended use: discovery, prevalence, regression, safety audit, task authoring, or preference-data candidate;
- licensed and prohibited inferences.

This should reference existing trial, trace, metric, task-health, and validity objects rather than duplicate them.

### 2. Operate sentinel and enriched streams together

Keep a frozen probability sample for prevalence/drift and an enriched queue for discovery. Report both denominators. Audit enriched-stream false negatives against the sentinel sample; use design weights only where inclusion probabilities and support justify them. Never pool enriched cases into unweighted failure rates or system rankings.

### 3. Separate the discovery ladder

A review record should distinguish:

- `signal_observed`;
- `review_worthy` with rater and evidence locator;
- `candidate_defect`;
- `defect_adjudicated` with root/surface status;
- `intervention_accepted`;
- `replay_effect` or `field_effect`;
- `downstream_utility`.

Only the first two are evidenced by Signals.

### 4. Measure real review efficiency

Use reviewer minutes, trace bytes/tokens/turns, required tools/state queries, annotator count, adjudication time, detector compute, invalid rate, confirmed defects, accepted fixes, recurrence, and severity-weighted benefit. Cluster uncertainty by source task/incident/system. “Rows per positive” remains a useful component, not the complete cost estimand.

### 5. Keep telemetry semantics fail-closed

Store signal type, exact evidence span/event, detector version, confidence basis, required/actual channels, and ambiguity/root-cause status. Do not convert environment or interaction markers into quality, capability, or safety scores without a separate validated metric and claim record. Track every downstream consumer so a descriptive signal cannot silently acquire a new authority.

### 6. Validate detectors and samplers independently

Use held-out, probability-sampled, plural-labeled trajectories to estimate score-conditioned yield, recall, subgroup error, drift, and cost. Include planted near-neighbors: legitimate retries versus loops, correct empty searches versus failure, user changes versus agent misalignment, bad arguments versus external errors, and satisfaction despite wrong state. Renew lexicons and bridge detector versions rather than rewriting old signal records.

## Concrete repository actions

1. **Do not add a Signals-specific schema task.** Existing metric-monitoring, task-health, grader/trace evidence-view, rater, configured-system, longitudinal, and validity contracts can represent the required objects.
2. During the next relevant consolidation, add review-sample selection as an explicit upstream boundary: eligible population → inclusion mechanism → review observation → adjudication → intervention. Preserve the sentinel/enriched distinction and forbid prevalence or comparative claims from unweighted enriched queues.
3. In a future trajectory-based pilot, exercise the boundary with a frozen probability sentinel plus an enriched detector stream and measure human minutes and confirmed-defect yield. This is a validation exercise over existing machinery, not a new subsystem.

## Action items

- [x] Read the complete immutable v1 PDF/text and inspect the full arXiv source.
- [x] Reconstruct signal layers, pool description, sampling arms, label target, agreement, reward standardization, domain analysis, and efficiency estimand.
- [x] Recompute the six principal Fisher contrasts and the true three-rater judgment counts per majority-positive row.
- [x] Renew the author-owned release search and archive the complete post-paper Plano implementation with a strict timing boundary.
- [x] Audit the implementation's detector coverage, parity boundary, and quality-score conflict with the paper.
- [x] Compare nonduplicatively with AgentRewardBench, AgentLens, Amazon, Anthropic, Nubank, rater evidence, and existing contracts.
- [x] Add no queue task: findings refine existing operating and validity machinery; the useful next step is consolidation or an empirical sentinel/enriched pilot, not another schema.

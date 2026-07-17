# Trace-population macro evals are investigation instruments, not defect estimators

## Source, release, and review status

- **Primary source:** Shikhar Kwatra, Will Thieme, and Bradley Strauss, “Macro Evals for Agentic Systems,” OpenAI Cookbook.
- **Official rendered notebook:** <https://developers.openai.com/cookbook/examples/partners/macro_evals_for_agentic_systems/macro_evals_for_agentic_systems>
- **Immutable source:** <https://github.com/openai/openai-cookbook/tree/0075904c509819f8d746794001a7a27066258956/examples/partners/macro_evals_for_agentic_systems>
- **Commit reviewed:** `0075904c509819f8d746794001a7a27066258956`, committed 2026-05-20; MIT license.
- **Local immutable release:** `data/sources/releases/openai-macro-evals-0075904/repository/examples/partners/macro_evals_for_agentic_systems/`
- **Provenance:** `data/sources/releases/openai-macro-evals-0075904/provenance.json`
- **Acquisition audit:** `data/sources/releases/openai-macro-evals-0075904/acquisition-audit.json`
- **Read and reproduced:** 2026-07-17. The complete 49-cell notebook, both helper modules, README, runner, requirements, run summary, both JSONL files, and all 992 bundle members were inspected. All ten scoped Git blobs (41,916,891 bytes) were hash-verified against the immutable Git tree.
- **Offline reproduction:** clean temporary copy at the path recorded in `data/sources/releases/openai-macro-evals-0075904/reproduction/run-root.txt`; execution log at `reproduction/execution.log`; executed notebook and HTML at `reproduction/outputs/`.
- **Independent audit artifacts:** `reproduction/audit_release.py`, `reproduction/audit-report.json`, `reproduction/stability_audit.py`, and `reproduction/stability-report.json`.
- **Evidence type:** official executable cookbook example with a released synthetic trace population and saved lower-level labels. It is not a paper, controlled production study, live deployment report, human-validation study, or intervention trial.

## Charter fit and useful completion

This review advances charter objectives A–D by testing cross-domain machinery for converting many agent trajectories into recurring-pattern and investigation-priority evidence. It is **validation and consolidation**, not a proposal to make `skill-bench` an EV-manufacturing, multi-agent, or OpenAI-specific benchmark. The concrete evidence is a successful clean-room notebook execution, exact denominator and label audits, and clustering perturbation results. The uncertainty clarified is which claims this composition can support: recurring pattern discovery and review prioritization, but not unbiased defect prevalence, causal root, repair benefit, operational reliability, professional validity, or business consequence.

Useful completion means preserving the inspectable pipeline while defining claim gates and falsification tests. No new schema is warranted unless existing population, transformation, metric, trace, validity, and intervention contracts cannot represent those gates.

## One-sentence contribution

The cookbook composes 992 rich synthetic multi-agent trace bundles and saved Promptfoo labels into compressed text views, TF-IDF → SVD → UMAP → HDBSCAN pattern clusters, metadata slices, prevalence/severity rankings, representative traces, and graph-backward “suspect” queues; it is an unusually inspectable investigation workflow, but its selected population, metadata-rich documents, heuristic impact formulas, and association-based suspect scoring do not establish production defect rates or causal diagnoses.

## Research question and licensed claim boundary

The source asks how teams can move beyond single-run pass/fail evaluation to identify recurring behavioral patterns across a population of long, multi-agent traces and prioritize investigation. Its executable release supports these narrow claims:

1. the supplied files contain 1,000 intended result rows, 992 run-linked labels, and 992 valid trace bundles;
2. those bundles can be normalized into trace- and event-level tables, compressed into several document views, clustered reproducibly enough for exploratory review under the pinned configuration, and sliced by supplied metadata;
3. released labels can be joined by identical run IDs and used as an additional prioritization signal;
4. selected cluster members can be traced backward through an inferred execution graph to rank nearby, frequent, bridging, role-weighted upstream nodes;
5. the complete notebook executes offline from the pinned release.

It does **not** establish that the focus rows represent a target production population; that cluster share is defect prevalence; that severity and impact values correspond to expert, user, safety, or business loss; that topic labels denote coherent defects; that a ranked suspect caused the outcome; that repairing it improves future performance; that labels are calibrated; or that the synthetic workflow predicts professional or production behavior.

## System and methodology

### Released population

The release describes a synthetic EV-order orchestration system with many specialized agents, tools, handoffs, reviews, loops, market regimes, and five declared agent-version labels. `trace_results.jsonl` contains 1,000 result records. Eight are `runner_error` rows without run IDs or bundles; seven of those are a contiguous tail of “All connection attempts failed” records and one earlier row has no recorded error string. The remaining 992 run IDs match exactly across results, labels, and zip member names.

Each available configuration appears once: the 992 bundles contain 992 unique `config_id` values, all with replicate count one. This is broad configuration coverage but no within-configuration stochastic replication. Agent-version labels in the bundles cover 274 `phase4-v1.0`, 321 `v1.1`, 195 `v1.2`, 98 `v1.2-shadow`, and 104 `v1.3` runs. By contrast, the result table records versions for only 225 rows. Version comparison is therefore a mixed-population observational slice, not a controlled release comparison.

### Normalization and trace documents

`helpers/data_prep.py` extracts all 992 bundle JSON files into a cache, normalizes trace and event tables, creates failure markers and timing fields, and builds three text views:

- `doc_structured_summary`: run metadata, scenario, outcome/status, route, findings, failures, handoffs, and selected tool/event summaries;
- `doc_state_transition_summary`: state, route, loop, retry, arbitration, and terminal-transition emphasis;
- `doc_failure_window`: a compressed window around inferred failure events.

Compression is necessary: released bundles have 14–483 events (median 253) and 12–246 spans (median 131.5). But the documents are derived analyst features, not neutral transcripts. They include supplied scenario, outcome, validation, route, and finding tokens while omitting most payload detail, artifact semantics, timestamps, and evidence needed to judge correctness. Clustering can therefore recover authored metadata and orchestration templates even if no latent defect behavior was discovered.

The default structured clusters illustrate this risk. Dominant TF-IDF terms include `postconfigorchestrator`, `validation`, `status`, `early`, `summary`, and `function`; several distinct clusters receive the same heuristic label (“fulfillment reroute”). Topic names and owners are assigned by keyword rules, not experts or an independent semantic judge.

### Focus-population construction

The notebook maps runtime statuses as follows:

- `completed` → `successful_completion`;
- `awaiting_review` → `review_escalation`;
- `blocked` or `failed` → `hard_failure`;
- every other value → `unknown`.

It then sets `has_failure` whenever outcome is not `successful_completion`, validation is not passed, or finding count is positive. Because the released bundles use `runtime_status="running"` for 632 rows while their terminal-state field says `in_progress`, **all 632 running rows become `unknown` and therefore `has_failure=True`**. The actual focus population is 846/992 rows: 632 running, 135 awaiting review, 67 completed, 10 blocked, and two failed. Nineteen running rows have neither findings nor a failed Promptfoo label and are selected only because “running” is treated as non-success.

This is the most consequential validity issue. The focus is a policy-defined review queue, not the set of failed runs. Its denominator excludes 146 supplied successful-completion rows but includes every still-running/in-progress row. Any cluster share or slice computed after this gate estimates composition among these 846 selected records, not defect prevalence among 1,000 attempted runs, 992 observed runs, or any external traffic population.

### Saved lower-level labels

`eval_labels.jsonl` contains 992 joined rows with `promptfoo_pass`, five named check scores/rationales, failed-check lists, a primary finding, mean score, run outcome, and case type. There are 453 pass and 539 fail labels; `final_decision_quality` fails 461 times, policy compliance 100, review appropriateness 56, market drift 41, and routing activation four. All rows contain rationales and there are 735 unique five-score vectors.

The release does not include the Promptfoo configuration, evaluator prompts, model/provider/version, temperature, seed, raw requests/responses, parsing and retry policy, acceptance thresholds, reference authority, human calibration sample, disagreement records, or drift evidence. No version fields occur in the saved label rows. The labels are inspectable outputs but not reproducible measurements. They may prioritize review within this example; they cannot serve as calibrated gold truth or support comparisons across evaluator changes.

The result status and Promptfoo pass also measure different things: 496 rows with result status `accepted` fail Promptfoo, while 271 accepted rows pass. This is useful multidimensional evidence, but it makes any unqualified “failure” count especially ambiguous.

### Pattern discovery

`helpers/macro_eval_pipeline.py` vectorizes the selected document view with TF-IDF, reduces it with truncated SVD and seeded UMAP, and clusters with HDBSCAN. Cluster labels are derived from keywords and representative examples through handcrafted rules. Representative examples are selected near the cluster centroid; elsewhere, the notebook displays highest trace-level `impact_score` examples.

The pipeline provides no held-out coherence labels, stability criterion, topic merge/split policy, minimum review confirmation, or external criterion. HDBSCAN noise remains a topic and contributes to prevalence unless explicitly excluded. Topic identifiers are run-local and have no semantic continuity contract across seeds, corpus changes, document views, or releases.

### Severity, prevalence, impact, and slices

At trace level, outcome groups receive heuristic severity weights: successful 1.0, in-progress/unknown 1.5–2.0 depending on fallback, review 2.0, blocked 2.5, and hard failure 3.0. The notebook defines:

`trace impact = severity_weight × (1 + findings_count) × (1 + loop_count / 4)`.

No user, expert, operational, safety, cost, or business-loss evidence calibrates these multipliers. More findings and loops may indicate richer instrumentation or a legitimate recovery process rather than greater consequence.

At topic level, the implementation does **not** average the trace impact above. It computes:

`topic impact = focus-population share × mean severity_weight`.

Thus topic “impact” is a frequency-weighted triage score in a selected population, not expected loss. Slice lift is topic share within a metadata slice divided by topic share across the same selected focus population. The implementation exposes counts and group totals, which is good, but low-support slices have no confidence intervals, minimum support gate, multiple-comparison control, or replication. Lift is association under the supplied mixture, not an agent-version, market, or topology effect.

### Backward suspects and “root-cause” drilldown

The drilldown builds a graph from recorded event and span relationships, chooses the latest inferred failure marker (or latest node), walks predecessors for at most three hops, and scores each candidate:

`0.4 × proximity + 0.3 × frequency + 0.2 × bridge + 0.1 × role`.

Cluster summaries then rank nodes by mean score and trace coverage across representative or selected members. This is a transparent investigation heuristic. It does not test temporal state divergence, necessity, sufficiency, alternative causes, recovery, or repair. Frequent bridge nodes such as the orchestrator can rank highly because of topology, exactly as common infrastructure can correlate with every failure without causing any one defect.

The function and notebook use “root cause” language beyond the evidence. The output should be called an `upstream_suspect_queue` until trace evidence supports a causal slice and an intervention changes outcome.

## Reproduction and empirical audit

### Clean offline execution

`run_notebook.sh` was run in a fresh `/tmp` copy, creating an isolated virtual environment and installing the pinned range-constrained requirements. It exited successfully:

- notebook execution and HTML conversion exit status: **0**;
- wall time: **2:32.73**;
- maximum resident set size: **997,756 KiB**;
- executed notebook: 451,468 bytes, SHA-256 `0686d861d708cddda25e20256f8ca078d994c2df8136f30ac7ac995a6d43140e`;
- rendered HTML: 619,458 bytes, SHA-256 `16023f6279628e891c9c4e7ef2aa115f96972836716893a76a5a2b972f02412c`.

The runner installs compatible packages from ranges rather than a complete lockfile. The observed environment used pandas 3.0.3, numpy 2.3.5, scikit-learn 1.8.0, UMAP 0.5.12, and HDBSCAN 0.8.44. A future compatible resolution may produce different embeddings or clusters. The HTML conversion also warns that Plotly MIME outputs cannot be represented, so the executed notebook is the more complete reproduction object.

### Deterministic denominator audit

`reproduction/audit-report.json` confirms:

- 1,000 intended results;
- 992 bundle-backed results, labels, and zip members with identical run-ID sets;
- eight runner errors without bundles;
- 624 bundle validations passed, 340 issues found, and 28 pending;
- 213 completed, 135 awaiting review, 10 blocked, two failed, and 632 running bundles;
- 453 Promptfoo pass and 539 fail labels;
- no saved label version fields.

### Clustering perturbation audit

`reproduction/stability-report.json` reruns the exact 846-row focus population under three UMAP seeds, a fixed-seed row-order shuffle, and all three released document views.

For the default structured summary:

- seed 42: 15 non-noise clusters, 11 noise rows;
- seed 13: 14 clusters, 0 noise rows;
- seed 99: 15 clusters, 22 noise rows;
- seed 42 after row shuffle: 16 clusters, 49 noise rows.

Pairwise adjusted Rand index is 0.866 for seeds 42/13, 0.968 for 42/99, and 0.912 for original versus shuffled order. The broad partition is fairly stable for an exploratory instrument, but cluster count, noise treatment, and some labels change enough that a single run should not define a durable defect taxonomy.

Document-view choice dominates seed choice:

- failure-window view: five non-noise clusters and 163 noise rows;
- state-transition view: 20 clusters and 45 noise rows;
- ARI versus the default structured partition: 0.041 and 0.531 respectively.

The failure-window view collapses 561 traces into one cluster with repeated generic orchestration/failure terms. This is direct evidence that the “behavior patterns” are conditional on an analyst-chosen projection. View selection is part of the measurement instrument and must be versioned, justified by construct, and subjected to stability and human-coherence checks.

## Unique insight: macro-eval output is a chain of conditional evidence views

The strongest transferable insight is not “cluster lots of traces.” It is that every aggregate diagnosis depends on a chain of population and representation decisions:

```text
attempted configurations
  -> observable/bundle-backed runs
  -> lifecycle-status interpretation
  -> focus-selection policy
  -> compressed document view
  -> vectorizer/reducer/cluster configuration
  -> cluster labeling and noise policy
  -> heuristic severity/impact ranking
  -> representative-trace selection
  -> graph construction and failure anchor
  -> upstream suspect queue
  -> human confirmation
  -> intervention and held-out outcome
```

Each arrow changes the estimand. The released system reaches `upstream suspect queue`; it does not include human confirmation or intervention outcome. Its most defensible artifact is therefore a **versioned investigation queue with explicit denominators and evidence views**, not a defect census or causal map.

This yields a strict claim ladder:

1. `recurring_text_partition`: these compressed records group under this configured instrument;
2. `review_priority`: this rule puts these groups first for inspection;
3. `confirmed_behavior_pattern`: blinded reviewers find a coherent recurring behavior in original evidence;
4. `defect_prevalence`: probability-weighted sampling supports a rate in a declared target population;
5. `supported_causal_slice`: trace dependencies and alternatives support an origin-to-symptom path;
6. `intervention_effect`: changing the suspected locus changes held-out outcomes under controls;
7. `operational_reliability`: repeated representative traffic supports system-level reliability;
8. `professional/business consequence`: expert/user/outcome evidence validates consequential use.

The cookbook directly supports rung 1 and implements a plausible rung-2 policy. It does not by itself establish rungs 3–8.

## Comparison with related local evidence

### Signals: selection-aware review yield

The local Signals review (`papers/agent-benchmarks/2026-07-14-signals-trajectory-triage-sampling-validity.md`) treats trajectory triage as a sampling and review-yield problem. The cookbook adds richer trace compression, clusters, slices, and drilldown, but weakens the same boundary if focus share is read as prevalence. `skill-bench` should combine Signals-style inclusion probabilities and missingness dispositions with this pipeline's inspectable queue. A prioritization sample can maximize issue yield; only a probability/audit sample can estimate rates.

### Agentic CLEAR: open-vocabulary issue compression

The Agentic CLEAR review (`papers/agent-benchmarks/2026-07-17-agentic-clear-dynamic-diagnostic-validity.md`) emphasizes compressing open-ended issues while separating coverage and diagnostic validity. The cookbook operationalizes a local, unsupervised analogue but shows how strongly representation choice controls the clusters. Novel or coherent topic text is not proof of a valid defect family. Both systems need original-evidence review, merge/split lineage, stability checks, and an explicit unresolved/noise disposition.

### STRACE: root-versus-surface localization

STRACE (`papers/agent-benchmarks/2026-07-09-strace.md`) correctly argues that a failure surface may be downstream of its origin and proposes execution-dependency causal slices. The cookbook's backward traversal is a practical candidate generator, but proximity/frequency/bridge/role weights are association heuristics, not causal localization. Retain the graph and candidate queue; require evidence edges, alternative-cause accounting, and repair tests before using STRACE-style “root cause” wording.

### Who&When Pro: intervention identity versus root identity

Who&When Pro (`papers/agent-benchmarks/2026-07-15-whowhen-pro-failure-attribution-validity.md`) has stronger localization evidence because it records an injected action, yet even that does not automatically prove the earliest sufficient natural cause. The cookbook has no controlled action delta at all. Its suspect score sits below Who&When Pro's intervention-identity rung and should not be labeled causal. A valid next test would plant controlled upstream defects, retain all recovered and failed continuations, and compare suspect ranking with paired repair outcomes.

### Production-evaluation reviews: metrics and task health

The Amazon review (`docs/concepts/amazon-production-agent-evaluation.md`) requires every metric to bind observations, population, denominator, missingness, uncertainty, threshold, and action. The cookbook is strongest on observations and inspectability, but its “prevalence,” “impact,” and slice lift lack target-population and decision-loss contracts. The Anthropic review (`docs/concepts/anthropic-agent-evaluation-lifecycle.md`) adds task/version health and adjudication. Here, document view, package resolution, label generator, cluster configuration, focus policy, and topic lineage all need equivalent versioning; clusters should be revised or retired rather than silently treated as stable ontology entries.

## Strengths worth retaining

1. **Immutable, full release.** Source, helpers, data, labels, bundle archive, and runner are available at one commit.
2. **Offline executability.** The complete notebook runs without paid calls or private services.
3. **Raw-to-summary drilldown.** Aggregates retain trace IDs and can return to original events rather than becoming detached prose.
4. **Multiple document views.** The release exposes representation choice instead of pretending one compression is canonical.
5. **Separate lower-level and macro signals.** Promptfoo results are joined, not silently substituted for system behavior.
6. **Counts alongside normalized slices.** Raw count and group total are recoverable even where the notebook emphasizes lift/share.
7. **Noise and representative members remain inspectable.** Analysts can audit rather than accepting opaque cluster labels.
8. **Graph-based upstream search.** As a queue, it is more useful than stopping at a terminal symptom.
9. **Version and scenario metadata.** The release enables mixture and subgroup audits, despite missing controls.
10. **Synthetic operational richness.** Long traces, loops, handoffs, reviews, tool calls, and failures provide a useful machinery fixture.

## Limitations and validity threats

1. The data are synthetic and there is no fidelity study against real agent traffic or professional outcomes.
2. The 1,000 rows are configurations, not a probability sample from a declared target population.
3. Eight runner errors lack bundles; seven appear as a correlated outage tail rather than independent agent failures.
4. Each available configuration has one replicate, preventing within-configuration reliability estimates.
5. The focus selector classifies all 632 `running`/in-progress bundles as failures through an `unknown` fallback.
6. Nineteen focus rows are selected only by that lifecycle-status rule.
7. “Prevalence” is conditional on the 846-row focus population, not all attempts or external traffic.
8. Structured documents include authored scenario, outcome, validation, route, and finding signals, enabling metadata recovery.
9. Compression omits evidence needed to evaluate semantic correctness and causal dependencies.
10. Document view changes the partition far more than random seed in the audit.
11. Cluster count, noise count, and some heuristic labels vary across seed and row order.
12. Topic labels and owners are keyword-rule outputs without human confirmation.
13. Multiple clusters can receive the same label, while one cluster can change labels under seed variation.
14. No cluster coherence, coverage, novelty, merge/split, or held-out generalization criterion is validated.
15. Noise is an algorithmic disposition, not proof of rarity, novelty, or non-defect status.
16. Saved Promptfoo labels omit evaluator configuration, model version, raw outputs, thresholds, and calibration.
17. Label rationales may be plausible without being faithful or correct; no human agreement study is included.
18. Result status and Promptfoo pass disagree frequently, so “failure” has no single operational meaning.
19. Trace impact weights and loop/finding multipliers are uncalibrated heuristics.
20. Topic impact uses focus share × mean severity, not the separately defined trace impact or expected consequence.
21. Slice lift has no uncertainty, support gate, multiplicity control, or causal identification.
22. Version, market, scenario, topology, and time are mixed; subgroup differences are associational.
23. Representative selection can favor centroid conformity or high heuristic impact, not causal informativeness.
24. Failure anchors are inferred from markers or latest nodes and may be surfaces rather than origins.
25. Backward suspect scores reward topology, frequency, and proximity; common orchestrators can dominate mechanically.
26. Maximum three-hop search can omit distant causes and does not test alternative paths.
27. No human confirmation, correction ledger, intervention, repair, sham control, or held-out outcome is released.
28. Requirements use version ranges rather than a complete lock; future compatible environments may change output.
29. There is no production monitoring, privacy, security, cost, alert, remediation, or rollback evidence.
30. Nothing in the release validates professional capability, operational reliability, business effect, or benchmark construct validity.

## Concrete transfer to `skill-bench`

### Retain

- Preserve attempted, observed, focus-selected, reviewed, confirmed, and intervened denominators separately.
- Make document/compression view an immutable, versioned evidence-view object with declared omissions and licensed construct.
- Keep clusters as run-scoped hypotheses linked to all members, noise dispositions, keywords, representatives, and configuration hashes.
- Use two samples: a priority sample for finding issues and a probability/audit sample for estimating rates.
- Keep outcome status, grader findings, artifact checks, operational errors, and lifecycle state as separate score families.
- Retain graph-backward candidates as diagnostic queues with original-event locators.
- Require metric specifications for prevalence, lift, severity, impact, and alert thresholds.

### Repair

- Replace `outcome_group != successful_completion` with an explicit status state machine; treat running/in-progress as censored or not-yet-terminal, not failed.
- Name every denominator in output labels, for example `share_within_selected_focus`, not `prevalence`.
- Record all runner errors and correlated-outage groups in operational reliability while excluding them from capability rates by declared policy.
- Version and calibrate saved graders; retain prompts, model/configuration, thresholds, raw outputs, retries, and human agreement.
- Compare clusters across seeds, row orders, package locks, hyperparameters, and evidence views; require minimum assignment stability before taxonomy use.
- Blind reviewers to supplied scenario/outcome labels when testing whether original trace evidence supports cluster coherence.
- Replace heuristic topic names/owners with provisional labels plus confirmation status and merge/split lineage.
- Label graph output `upstream_suspects`; reserve `root_cause` for supported causal slices and interventions.
- Calibrate severity and impact against declared expert/user/safety/cost consequences rather than loops and finding counts alone.
- Add uncertainty and minimum-support rules to slices; do not interpret lift as a version effect without matched or randomized evidence.

### Falsification tests

1. **Selection-policy audit:** compare cluster composition under terminal-only failures, grader-failed terminal runs, random observed runs, and the current focus rule; report inclusion probabilities and denominator changes.
2. **View ablation:** remove scenario, outcome, route, finding, and agent-name tokens one family at a time; test assignment stability and blinded coherence from raw evidence.
3. **Cluster stability matrix:** repeat seeds, row orders, package lock, min cluster size, neighbors, and views; report ARI, noise transitions, topic merge/split lineage, and label stability.
4. **Human coherence/calibration:** probability-sample cluster members and nonmembers; have qualified reviewers blindly assess common-behavior support, severity, owner, and alternatives.
5. **Controlled-defect fixture:** plant upstream evidence-selection, handoff, tool-interface, and artifact defects plus sham and dual-fault controls; retain recovered, failed, and invalid attempts.
6. **Causal/repair test:** compare suspect rank with first divergence, intervention locus, supported dependency path, and held-out paired repair success.
7. **Metric backtest:** test whether ranking by current impact, expert consequence, review yield, and repair benefit selects the same issues; reject “impact” if it does not predict the declared decision target.
8. **Version comparison:** run repeated matched configurations across versions in reset environments; separate agent changes from traffic, scenario, grader, and infrastructure effects.

## Concrete next actions

No new queue task is added. The existing benchmark-bundle, evidence-view, population-selection, metric-specification, trace/causal-slice, intervention, execution-validity, task-health, and validity-argument work can represent the necessary repairs. Adding another macro-eval schema now would duplicate machinery.

When a current artifact-heavy pilot has real traces, use this release's `stability_audit.py` pattern as a diagnostic test fixture:

- declare attempted/observed/eligible/focus/reviewed denominators;
- build at least two construct-motivated evidence views;
- cluster under repeated seeds and row orders;
- blind-review coherence against original artifacts and trace evidence;
- plant one controlled upstream defect and one sham;
- measure review yield, supported localization, and repair effect separately.

Useful completion is not a compelling topic dashboard. It is evidence that the same recurring pattern survives reasonable population and representation choices, reviewers can confirm it in original evidence, and acting on a supported diagnosis improves consequential held-out artifacts without collateral regressions.

## Bottom line

OpenAI's macro-evals cookbook is one of the more useful inspectable demonstrations of population-level trace investigation: it releases rich long-horizon bundles, saved lower-level labels, full transformation code, multiple document views, clustering, slices, representatives, and graph drilldown, and the pinned notebook reproduces offline end to end.

Its labels overreach its evidence at several points. The default focus population includes all 632 running traces because an unrecognized lifecycle state is treated as failure; “prevalence” is share within that selected set; document projections embed authored metadata and sharply change the cluster partition; severity and impact are uncalibrated triage heuristics; and backward suspect ranking is topology-weighted association without confirmation or intervention. `skill-bench` should retain the pipeline as a versioned investigation instrument, add selection-aware and view-stability gates, and keep review priority, defect prevalence, causal root, repair benefit, operational reliability, professional validity, and business consequence as distinct claims.
# AstaBench: a broad scientific benchmark portfolio is not one validated research-assistance scale

## Bottom line

AstaBench is a strong **benchmark-operations contribution**: it packages 11 unlike scientific-computation and literature tasks behind a common interface, gives compatible agents date-restricted literature tools and a stateful code sandbox, records model usage, publishes cost/performance frontiers, and distinguishes open/closed implementations and standard/custom tools. Its best measurement ideas are the explicit solve→score boundary, versioned suite configuration, typed tool-access labels, artifact-triangulated end-to-end grading, and reporting score beside cost rather than hiding resource use.

Its central validity claim is too broad. The “2,400+ problems” are 1,918 test plus 486 validation items—not 2,400 independent test observations—and range from 900 short DS-1000 completions to 40 multi-artifact research projects. The overall score is a policy-weighted macro-average of incompatible metrics and evidence views: exact match, executable tests, retrieval F1/estimated recall, multiple-choice accuracy, LLM entailment, a product of hypothesis-match facets, and rubric-step completion. Macro-averaging usefully prevents DS-1000 from numerically dominating, but it does not create a common construct or validate the chosen weights.

The environment also provides **classification, not full control**. Only some rows use standard tools; the top overall Asta v0 uses fully custom tools, several commercial systems use private retrieval, some answers are cached, and costs omit unavailable commercial or non-model infrastructure costs. Tooling/openness labels expose these differences but do not remove them. Accordingly, the 57 configured-system results support a descriptive comparison over the administered portfolio—not an architecture effect, general scientific capability, professional research competence, productivity, novelty, or readiness.

The unique transferable insight is that a suite score needs an explicit **portfolio estimand**. Preserve component construct, unit, eligible system set, evidence view, metric, denominator, invalid/missing policy, uncertainty, cost boundary, and decision weight before aggregation. Report the component vector and eligibility pattern as primary evidence; treat a scalar as a named stakeholder policy over that vector, not as a discovered scientific-capability scale.

## Why this matters: charter relevance and useful completion

This review advances charter objectives A, B, and D through comparative expansion and consolidation. AstaBench is a bounded scientific-work case, not a proposal to narrow `skill-bench` to science. The evidence is the complete immutable v2 paper, comparison with immutable v1, and a pinned official code/dataset-release audit. The uncertainty clarified is whether suite breadth, common tooling, macro-aggregation, and cost reporting license a holistic research-assistance claim. Useful completion is a retain/repair/test account that maps into existing bundle, configured-system, task-health, metric, validity, artifact, and reliability machinery without creating a science-specific schema.

## Sources and reading record

### Immutable paper read in full

- Jonathan Bragg et al., *AstaBench: Rigorous Benchmarking of AI Agents with a Scientific Research Suite*.
- Immutable v2 record: <https://arxiv.org/abs/2510.21652v2>; PDF: <https://arxiv.org/pdf/2510.21652v2>.
- Local v2 PDF: `data/papers/pdfs/2510.21652v2-astabench.pdf` (88 pages; SHA-256 `5bf79b03472bfb22b7826c62206bd0dfafaa849920888210c1ae31c0eed2df33`).
- Local v2 layout text: `data/papers/text/2510.21652v2-astabench.txt` (SHA-256 `3a1f295ba9caa038c2a6d7c34171b58f3c80850548d2f5c607bd71f73f230437`).
- Companion immutable v1: `data/papers/pdfs/2510.21652v1-astabench.pdf` and `data/papers/text/2510.21652v1-astabench.txt` (hashes in `data/papers/index.json`).
- Date read: 2026-07-14. The complete v2 extraction was read through the main paper, principles, complete result tables, all 11 evaluation descriptions, agent implementations, validation studies, prompts, and final task examples. Important task/count/result claims were checked against the PDF extraction; v1 was compared for version drift.
- v2 is the ICLR 2026 conference version dated 2026-04-21; v1 is dated 2025-10-24. v2 adds explicit confidence-interval methodology and expanded validation/detail while retaining the 11-benchmark, 2,400+, and 57-agent framing. Neither arXiv record inspected here contains a withdrawal notice.

### Official release audited

- Official repository: <https://github.com/allenai/asta-bench>, pinned at tag `v0.5.4`, commit `36c9bc14a83b95851a4f5c4baaccdde6d1c0cafb` (2026-06-17, after v2).
- Local archive: `data/sources/releases/2510.21652v2-astabench/allenai-asta-bench-36c9bc1.zip` (SHA-256 `bde916791804343ccdb89119183ab75ee1c9fedce2e4addc6af12cb688e42e72`; 192 files).
- Official dataset: <https://huggingface.co/datasets/allenai/asta-bench>, immutable revision `282834d58c0e9fcdee80caad6d9ae8110b672e51`.
- Dataset tree manifest: `data/sources/releases/2510.21652v2-astabench/hf-tree.json` (557 files; 53,958,105 declared bytes).
- Provenance and timing boundary: `data/sources/releases/2510.21652v2-astabench/provenance.json`.

Release status is **complete post-v2 code archive inspected; immutable dataset manifest inspected; gated dataset bytes not read**. The dataset API tree is public, but immutable file retrieval returned HTTP 401 because the repository requires license acceptance and an HF token. The review therefore does not claim full dataset-content inspection. The code commit postdates v2 by almost two months and is implementation evidence, not proof of the exact paper-time runner.

## One-sentence contribution

AstaBench operationalizes a broad, cost-aware portfolio of 11 scientific-agent evaluations behind shared interfaces and evidence labels, but its configured-system bundles and policy-weighted incompatible metrics support component-level portfolio comparisons rather than one validated scientific-research capability scale.

## Research question

The paper asks how to benchmark scientific agents more rigorously and compare the state of scientific research assistance. It contributes:

1. five proposed benchmark principles: realistic-use coverage, standard realistic tools, confounder-aware reporting, standardized task interfaces, and comprehensive baselines (Appendix A, pp. 16–17);
2. an 11-benchmark suite spanning literature understanding, code/execution, data analysis, and end-to-end discovery (Table 2, p. 5);
3. the Asta Scientific Corpus and computational notebook tools (Section 4.1, pp. 5–6);
4. an Inspect-based evaluation/leaderboard layer with frozen-price cost normalization and openness/tooling labels (Section 4.2, pp. 6–7);
5. 57 configured agents across 22 classes, including nine Asta agent classes (Sections 4.3–5 and Appendix F); and
6. extensive component, category, overall, and score-cost results.

The evidence supports the existence and behavior of this purposively assembled portfolio under the reported configurations. It supports descriptive claims such as “selected systems score differently across components,” “standard tool access can make retrieval more comparable within the compatible subset,” and “artifact cross-checking catches some report-only false positives.” It does not establish a validated latent scientific-assistance trait, a representative population of scientific work, causal agent-architecture effects, scientific novelty, professional competence, productivity gains, safe use, or deployment readiness.

## Methodology and system

### Suite composition: 2,404 development-plus-test items, not one sample

Table 2 counts reconstruct exactly:

| Component | Unit and primary score | Test | Validation |
|---|---|---:|---:|
| PaperFindingBench | query; F1 or harmonic mean of estimated recall and rank | 267 | 66 |
| LitQA2-FullText-Search | biomedical query; target-paper recall@30 | 75 | 10 |
| ScholarQA-CS2 | long report; four equally weighted LLM-judge facets | 100 | 100 |
| LitQA2-FullText | multiple-choice question; accuracy | 75 | 10 |
| ArxivDIGESTables-Clean | generated table; reference-statement recall | 100 | 70 |
| SUPER-Expert | repository execution task; exact output match | 45 | 50 |
| CORE-Bench-Hard− | capsule reproduction; programmatic report score | 37 | 35 |
| DS-1000 | short code completion; test pass | 900 | 100 |
| DiscoveryBench | dataset analysis; product of three hypothesis-match facets | 239 | 25 |
| E2E-Bench | multi-artifact research project; rubric-step completion | 40 | 10 |
| E2E-Bench-Hard | harder multi-artifact project; same score family | 40 | 10 |
| **Total** | unlike units | **1,918** | **486** |

Thus “2,400+ problems” means 2,404 combined development and held-out items. It is a release-size statement, not the test denominator, and definitely not the effective sample size for an overall claim. Items also cluster by source, paper, table, dataset, workflow family, and rubric authoring process.

Coverage is broad but uneven. Computer science dominates PaperFinding, ScholarQA, SUPER, DS-1000, and both end-to-end sets. ArxivDIGESTables is 94.3% computer science by paper tags; DiscoveryBench is 41.8% meta-science and 24.3% sociology; CORE contributes 37 cross-domain capsules. The paper itself labels the suite “weighted towards CS” (Table 1, p. 3). Breadth across pipeline labels therefore does not establish prevalence or balanced content coverage across science.

### Task provenance and selection

Provenance strength varies by component:

- PaperFinding mixes consented Asta/OpenSciLM logs and prior search sets, but deliberately selects difficult queries: failures or low “perfect relevance” counts for Asta PaperFinder, then prioritizes cases where component ablations find fewer perfect results (Appendix E.2, pp. 34–35). This is useful challenge-set construction but outcome-conditioned, system-dependent sampling.
- ScholarQA test questions are 100 computer-science requests selected from 8,000 OpenScholar logs through LLM filters, a 200-item random sample, and four-author review (Appendix E.3.1, p. 38). This is authentic-request evidence after heavy domain/quality filtering, not a random product-usage distribution.
- ArxivDIGESTables-Clean manually removes generic and unrecoverable columns, then randomly splits 170 retained tables (Appendix E.4, pp. 38–39). That improves answerability but conditions out two real failure classes.
- SUPER uses expert-authored execution notebooks; CORE, DS-1000, and DiscoveryBench adapt prior benchmarks. DS-1000 removes 100 original test items for validation, changing exposure boundaries.
- E2E-Bench samples pairs from 288 highly cited post-2021 ACL papers, machine-generates roughly 400 ideas, automatically simplifies/ranks them, then expert-raters repair/discard and keep 50. E2E-Hard uses HypER, ranking, and expert repair without simplification (Appendix E.9–E.10, pp. 41–42). These are generator/ranker/reviewer-selected computational ML projects—not observed end-to-end research requests.

This mixed lineage is appropriate for a stress-test portfolio. It does not support a single ecological-validity claim. Product logs inform only literature components, and “consent” does not establish that benchmark transformations preserve the original need or that high score predicts user value.

### Environment and tool controls

Compatible literature tasks receive date-restricted Asta Corpus tools; ArxivDIGESTables restricts snippet search to supplied paper IDs. Code tasks receive a stateful Jupyter/Python environment, shell access, a five-minute cell timeout, and a Docker sandbox (Section 4.1, pp. 5–6). These are valuable controls over information and execution for agents that actually use them.

But the treatment is not shared across all 57 rows. The paper labels tools as standard, custom-equivalent, or fully custom (Appendix B, pp. 17–18). Asta v0—the top overall row—uses fully custom tools. Commercial research agents use private search and wrappers; several results are cached; some outputs are passed through a Gemini formatting model; Asta Panda and CodeScientist are scored from cached answers. “Custom-equivalent” is defined administratively, not demonstrated by a conformance intervention. The framework therefore records an important moderator but does not control it away.

The same issue applies to model/scaffold comparison. Each row bundles model snapshot, provider, prompt, architecture, tools, retrieval corpus, formatter, cache, budget, and scorer compatibility. Asta v0 routes by validation-set lexical overlap and selects sub-agents from preliminary experiments; if a sub-agent produces no output, it tries up to three task types (Appendix F.7, p. 51). This is a portfolio optimizer with outcome-informed component selection, not a clean architecture treatment.

### Solver-to-score boundary and evidence views

The suite mixes five materially different observation regimes:

1. **answer-only exact/programmatic checks** — LitQA2, DS-1000, SUPER;
2. **retrieved item IDs plus submitted evidence** — PaperFinding and LitQA2 Search;
3. **generated artifact transformed by an LLM then judged** — ArxivDIGESTables;
4. **natural-language hypothesis versus gold, model judged** — DiscoveryBench; and
5. **report, code, and produced artifacts jointly judged against task rubrics** — E2E.

The E2E scorer is the strongest design. A rubric item is met only when report/code/artifact views are consistent and at least one shows success. Table 21 reports that report-only evidence would have produced false positives in 16% of facet combinations and code-only absence false negatives in 16%. A 50-rubric-item dev spot check judged 92% of scorer labels correct (Appendix F.9, pp. 52–53). This demonstrates why multiple admissible views matter.

The evidence is still limited: 50 items are not grouped by task, criterion, agent, or severity; annotator count/agreement and sampling are absent; 92% does not reveal false-pass versus false-fail asymmetry; and the paper admits optimistic vague matches and missed conceptual nuances. Average rubric-step completion (up to roughly 70%) is not end-to-end completion: Table 20 gives only 0–5% all-steps-complete for three specialized baselines.

Other graders have sharper limits:

- Semantic PaperFinding recall divides by a PaperFinder-derived estimated relevant-set size multiplied by 2–10, then combines recall@estimate with a lower-bound-corrected rank score. Manual review corrected criteria for only one fifth of semantic queries (Appendix E.2, pp. 34–35). The metric is bounded and operational but system-relative, not recall against a known universe.
- ScholarQA’s four judge facets average citation recall, citation precision, paragraph relevance, and coverage. Citation scoring explicitly does not verify that cited papers exist or that quotes occur in them; title-only support receives half credit (Appendix E.3, pp. 35–36).
- ArxivDIGESTables measures only recall of reference-table statements after GPT-4o unrolling/entailment. It does not penalize unsupported extra cells or validate table usefulness.
- DiscoveryBench multiplies three LLM entailment/equivalence facets against one gold hypothesis. A product gate is sensitive to any one facet and can reject valid alternative discoveries not equivalent to the paper-derived gold.
- SUPER exact-matches output metrics to one expert notebook, which demonstrates a canonical witness but not verifier completeness over equivalent environments or numeric tolerances.

### Aggregation: a policy, not a scale

The released `astabench/config/v1.0.0.yml` identifies each component’s primary metric and macro-averages them, halving both LitQA variants to avoid double counting. Effective component weights are therefore 4 literature, 3 code/execution, 1 data-analysis, and 2 end-to-end units out of 10. This prevents the 900 DS-1000 items from dominating, but the weights are design choices rather than empirical construct weights or stakeholder utilities.

A 1-point increase in one component contributes according to its benchmark weight, regardless of sample count, reliability, criterion severity, cost, or scientific consequence. A short code-completion metric and a multi-day research-project rubric can therefore trade off numerically. Missing component support also matters: only general agents with all 11 scores receive an overall score, while specialist/commercial systems appear in category or component tables. “Best overall” is conditional on eligibility and portfolio policy, not simply better science assistance.

A defensible suite report should make the component vector primary and attach a scalar only to a named use case with predeclared weights, minimum gates, missingness rule, uncertainty, and loss function. Noncompensatory gates are especially important: strong literature QA should not erase near-zero complete end-to-end success.

### Cost accounting

The toolkit freezes a LiteLLM price map and recomputes normalized dollars from Inspect model usage, including cache discounts but excluding latency/batch discounts (Section 4.2, pp. 6–7). This is much better than score-only ranking and supports within-logged-model Pareto analysis.

It is not total cost. It excludes engineering, custom retrieval/search infrastructure, sandbox/CPU/GPU time, human formatting or submission effort, scorer-model cost unless separately included, and unavailable commercial-system costs. Several result tables show missing cost. Asta v0’s end-to-end average exceeds $12 per item while ReAct’s cost is model-logged; these are not necessarily like-for-like resource boundaries. The leaderboard’s “time-invariant” cost is snapshot-relative, and the paper says the snapshot may be updated and all costs recomputed. Preserve both raw usage and the exact price-map version rather than treating recalculated dollars as immutable historical observations.

## Evidence and results

The strongest descriptive findings are:

- no fully open configured system is competitive across this selected portfolio; the best reported open-weight overall row is 11.1%;
- Asta v0 reaches 53.0% overall versus 44.0% for ReAct/gpt-5, but it is a mixed-model, fully custom, task-routed system selected with validation/preliminary evidence;
- literature report scores are much higher than execution/data scores, though the graders and metrics are not commensurate;
- DS-1000 can reach 78%, while SUPER and CORE remain much lower under repository/capsule execution;
- DiscoveryBench peaks near 34%; and
- E2E mean step completion can approach 70%, while all-step completion remains 0–5% for the three systems in Table 20.

These results support a “local criteria can pass while complete workflows remain rare” diagnosis. They do not identify why without matched component interventions. Model changes interact strongly with scaffold: gpt-5 helps ReAct on selected tasks and hurts some specialized agents. That is evidence of configured-system interaction, not evidence that specialized workflows are becoming intrinsically obsolete.

### Statistical evidence

v2 reports 95% intervals as ±1.96 standard errors across evaluation samples and analytically propagates category errors under independence (Appendix D, p. 21). The paper itself notes this can underestimate uncertainty. Further threats are larger:

- source/task-family clustering is ignored;
- LLM-judge variation and scorer calibration error are not propagated;
- many model–agent comparisons were selected from multiple configurations for narrative tables;
- experiments ran over several months, so provider/tool time is confounded with rows;
- no common repeated-attempt design estimates agent stochasticity;
- closed/cached systems have different observability and missing-cost patterns; and
- no simultaneous-comparison or paired-difference analysis supports the many “wins” discussed.

The intervals describe item variation under the administered score, not deployment reliability, architecture effects, or uncertainty in the holistic construct.

## Release audit and reproducibility

The post-v2 `v0.5.4` archive is substantial and inspectable. It contains suite configs, task loaders/scorers, tool wrappers, sandbox code, tests, a decoupled solve→score script, and pinned dataset revision constants. `v1.0.0.yml` confirms exact primary metrics and LitQA half-weights. The README documents a gated dataset token, scorer API keys, high-volume logs, sandbox concurrency faults, MCP 429/504 failures, and decoupled scoring.

Important release/paper boundaries remain:

1. The pinned code commit is 2026-06-17, after 2026-04-21 v2; it cannot establish paper-time code identity.
2. The code’s current ScholarQA defaults use a newer judge (`google/gemini-3-flash-preview`) while the paper reports Gemini 2.5 Flash. Cross-version scoring is therefore a real instrument change unless scorer commits are pinned per result.
3. ScholarQA judge calls retry parse/model failures up to 20 times, and the task sets `fail_on_error=False`. This may improve score completion, but judge-service/parse invalids need their own denominator and retry ledger.
4. ArxivDIGESTables skips items missing unrolled references; DiscoveryBench format failures score zero; task-specific invalid handling is not one suite-wide policy.
5. The release archive has DVC metadata and ignored log directories, not the paper’s complete reported trajectories/results as ordinary archived bytes. The paper says logs of all reported experiments are available, but this review did not find a self-contained paper-table reproduction package in the pinned archive or dataset manifest.
6. The HF dataset is license-gated. Its public tree has 557 files, 534 of which are cached You.com search responses; anonymous immutable file retrieval failed. Exact task bytes, transformations, licenses, and correspondence to paper-time runs were therefore not independently audited here.
7. Literature reproducibility depends on a hosted Asta MCP service and key, not a locally archived corpus/index. Date filtering stabilizes publication eligibility, but ranking/index/service implementation and availability remain external dependencies.
8. The sandbox is useful but allows shell execution and host-provided MCP access. Reproducibility requires image digest, network policy, tool-service commit/index identity, and canaries—not “Docker” alone.

Overall: paper inspectability is strong; post-v2 code inspectability is strong; paper-time run reproducibility is moderate-to-weak; dataset-content inspectability is gated; hosted-search reproducibility is service-dependent.

## Unique insight: represent a suite as a typed portfolio estimand

A “holistic” suite should be modeled as:

`component evidence vector + eligibility/missingness vector + resource vector + aggregation policy + claim boundary`

For each component preserve:

1. construct and intended use;
2. unit hierarchy (suite → family → task → item → attempt → criterion/artifact);
3. source and selection mechanism;
4. eligible configured systems and tool treatment;
5. required artifact/evidence views;
6. grader, metric scale, and validity evidence;
7. intended, started, valid, invalid, and substantive-failure denominators;
8. clustering/repetition and uncertainty method;
9. raw resource usage and normalized-cost boundary;
10. minimum gate, compensability, and portfolio weight; and
11. interpretations explicitly excluded.

Aggregation should then be named, for example: `asta_v1_equal-component-policy`, rather than presented as “scientific research ability.” Report sensitivity to at least item-weighted, component-macro, category-balanced, noncompensatory-gated, and stakeholder-loss policies. If rankings change, that is not noise to hide; it proves the “best agent” depends on use and weights.

This extends SciAgentArena’s mixed-unit lesson. SciAgentArena shows why workflow stages, cases, genes, and task types cannot share an untyped denominator. AstaBench adds an explicit scalar and cost frontier, making the aggregation policy itself a treatment. AARRI goes further on action, abstention, adoption, and consequence; AstaBench mostly stops at benchmark artifact scores. BrowserGym and production-evaluation reviews similarly show that common interfaces do not erase adapter, environment, service, or invalid-run differences.

## Limitations and validity threats

### Construct and content validity

1. The suite is purposively assembled and strongly CS-weighted, not sampled from a defined scientific-work population.
2. “2,400+” combines 1,918 test and 486 validation items and unlike work units.
3. Product-derived evidence is limited to selected literature requests after filtering and challenge selection.
4. Scientific discovery is represented mostly by fixed computational tasks with detailed steps, not question formation, collaboration, laboratory work, or downstream uptake.
5. End-to-end tasks are generator/ranker/reviewer-selected ACL combinations and only weakly test ideation/planning by the authors’ admission.
6. Exact-answer and one-gold-hypothesis tasks can reject legitimate alternatives.
7. Breadth across categories does not validate one latent “scientific research assistance” construct.

### Measurement and aggregation validity

8. Component metrics differ in scale, evidence view, reliability, and severity.
9. Equal component weights and LitQA half-weights are reasonable policies but not validated utilities or construct loadings.
10. Compensatory averaging allows high literature scores to offset near-zero full-project completion.
11. Specialist eligibility and missing components make rankings conditional on the support set.
12. PaperFinding semantic recall uses a PaperFinder-derived estimated denominator.
13. ScholarQA citation grading does not verify paper existence or quote provenance.
14. ScholarQA rubrics are built from evaluated-system outputs; held-out ablation significantly lowers three of five tested systems by about 2.5 points.
15. Human–judge agreement is moderate (system τ=0.467; instance τ=0.369 among clear-winner cases), and excluding one disliked system raises system τ to 0.800 post hoc.
16. ArxivDIGESTables recall ignores unsupported additions and depends on two LLM transformations.
17. DiscoveryBench’s multiplicative gold-alignment score is not scientific validity or novelty.
18. E2E’s 92% spot-check uses only 50 rubric items and lacks a complete reliability/error-severity analysis.
19. Scorer retries, formatters, cached answers, and task-specific invalid policies are not separated in suite-level denominators.

### Comparison, uncertainty, and cost validity

20. Rows are configured-system bundles, not isolated model or architecture treatments.
21. Standard, custom-equivalent, and fully custom tools coexist; labels reveal confounding but do not remove it.
22. Asta v0 uses validation overlap, preliminary solver selection, and up to three fallback routes.
23. Experiments span months and include unpinned model aliases.
24. Item SEs ignore source/task clustering, judge uncertainty, repeated-agent stochasticity, and many-comparison selection.
25. Category propagation assumes independence between tasks.
26. No common repeat design supports reliability claims.
27. Dollar cost covers logged model inference, not total compute, tooling, infrastructure, engineering, scorer, or human cost.
28. Missing commercial costs make some frontiers incomplete.

### Reproducibility and operational realism

29. Current code postdates v2 and uses at least one newer default judge.
30. The official dataset is gated; this review could inspect only its immutable manifest.
31. Hosted search/index behavior is not archived with the paper.
32. The pinned archive does not provide a self-contained paper-run/table reproduction package.
33. External repository/capsule/package availability can change execution tasks.
34. Cached/UI/API systems have weaker trace and configuration observability.
35. The suite observes controlled artifacts, not scientist acceptance, changed decisions, real productivity, scientific impact, safety, or readiness.

## Transfer to skill-bench

### Retain

1. **Versioned suite config.** Bind component names, metrics, split, and aggregation policy to an immutable version.
2. **Component-first reporting.** Keep task-family vectors and eligibility visible.
3. **Tool/openness classification.** Record standard/custom and open/closed identity rather than pretending all rows are comparable.
4. **Date-restricted source access.** Freeze eligible evidence and expose cutoff semantics.
5. **Solve→score separation.** Permit rescoring only with explicit scorer-version lineage; retain original scores.
6. **Score–cost frontiers.** Preserve raw usage and normalized prices separately.
7. **Multiple artifact views.** Cross-check claims against code, reports, and native artifacts.
8. **All-criteria completion beside average progress.** Do not let partial-step averages hide brittle workflows.

### Repair

9. **Type every count.** Distinguish validation/test items, tasks, workflow stages, criteria, and attempts.
10. **Name portfolio estimands.** Treat weights, gates, and missingness rules as policy records with owners and intended uses.
11. **Add noncompensatory gates.** Severe safety/provenance/workflow failures cannot be averaged away.
12. **Separate controlled subsets.** Compare standard-tool systems causally only within matched environments; treat custom systems as separate package evaluations.
13. **Freeze evidence views and judges.** Hash formatter, unroller, rubric pool, judge, prompts, retry policy, and source corpus/index.
14. **Keep denominators plural.** Intended, service-valid, trial-valid, grader-valid, and substantively successful counts must remain separate.
15. **Estimate total operational cost.** Include sandbox, search/tool service, scorer, retry, human review, and infrastructure where the decision needs them.
16. **Bound claims.** Suite breadth supports portfolio coverage, not professional validity or one general capability score.

### Test

17. **Aggregation sensitivity.** Re-rank frozen trials under item-weighted, equal-component, category-balanced, noncompensatory, and stakeholder-loss policies.
18. **Tool-treatment ablation.** Run the same model/scaffold under standard versus custom-equivalent retrieval with identical source eligibility and budgets.
19. **Rubric-pool intervention.** Build rubrics from disjoint systems or experts and estimate entrant-specific held-in advantage.
20. **Evidence-view ablation.** Compare report-only, code-only, artifact-only, and triangulated E2E grading against blinded adjudication.
21. **Invalid/retry audit.** Replay scorer/model/service failures under fail-closed, retry, and missing policies without rewriting historical trials.
22. **Repeated matrix.** Use the already blocked cross-pilot repeated-task matrix to estimate within-form recurrence and between-family transport; do not infer a universal repeat budget.

## Concrete repository actions

- **No new queue task added.** The pending `consolidate-repeated-evaluation-estimand-boundary` and blocked `build-cross-pilot-repeated-task-matrix`, plus existing metric/validity/task-health/configured-system contracts, already cover the evidence-implied aggregation, denominator, repeat, and claim-boundary work. A science-specific aggregation schema would duplicate existing machinery and narrow scope.
- Added this review to `papers/topic-index.md` and marked the paper fully reviewed in `data/papers/index.json`.
- Canonical synthesis was not changed in this run: SciAgentArena and existing portfolio/metric principles already encode mixed-unit and component-before-aggregate boundaries. A future consolidator can compare this concrete scalar-policy case without duplicating source detail.

## Assessment

- **Most reusable contribution:** common suite operations with versioned components, explicit tool/openness labels, artifact-triangulated grading, and score–cost reporting.
- **Strongest evidence:** selected configured systems have sharply different component profiles, and average E2E criterion success can coexist with almost no complete projects.
- **Most important unique insight:** suite aggregation is a stakeholder policy over a typed evidence vector, not automatic evidence for one holistic capability.
- **Most serious validity flaw:** incompatible units, metrics, evidence views, eligibility sets, and unvalidated weights are collapsed into an overall percentage.
- **Most serious reproducibility flaw:** the inspected code postdates v2, the dataset is gated, hosted search is external, scorer defaults drift, and a self-contained paper-run package was not found.
- **Safe claim for `skill-bench`:** retain component vectors, configured-system/tool identity, artifact evidence, plural denominators, raw cost, and named aggregation policies; report sensitivity and hard gates before any scalar. Do not infer professional competence, scientific novelty, productivity, safety, general capability, or readiness from suite breadth or a macro-average.

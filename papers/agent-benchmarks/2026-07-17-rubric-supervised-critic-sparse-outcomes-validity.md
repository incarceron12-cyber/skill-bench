# Rubric-supervised critics: dense trace labels can regularize a selection policy without validating process quality

## Source and review status

**Deep review of the complete immutable primary source and appendices, plus a timing-bounded official release/model audit.**

- **Paper:** Xingyao Wang, Valerie Chen, Heng Ji, and Graham Neubig, *A Rubric-Supervised Critic from Sparse Real-World Outcomes*, arXiv:2603.03800v1 (4 March 2026), <https://arxiv.org/abs/2603.03800v1>
- **Local PDF:** `data/papers/pdfs/2603.03800v1-rubric-supervised-critic-sparse-real-world-outcomes.pdf` (29 pages; 1,071,982 bytes; SHA-256 `6a3e61d7820b68065f4df664da008e36b58cf0da142c2b567f9bba0358ae0761`)
- **Full local text:** `data/papers/text/2603.03800v1-rubric-supervised-critic-sparse-real-world-outcomes.txt` (96,201 characters; SHA-256 `5e308d751e19e8b3ffa641d5808bdfd1f60a9bc9917bd81153b00aec23af3acf`)
- **Metadata:** `data/papers/source/2603.03800v1-metadata.xml`
- **Official rubric package:** `data/sources/releases/2603.03800v1-critic-rubrics/OpenHands-critic-rubrics-9f03ba4.zip`, exact commit `9f03ba41f4431191c5ce17e9ccfc80ccda73ee69`, tree `303a5716c397bc63151d245a9c7a744eeb717f28`, SHA-256 `70f715d2b8d8f9fb9d13623aa17d60d5676f7dae2065443dcf265e6c2e66ebac`
- **Official model:** `OpenHands/openhands-critic-4b-v1.0`, exact Hugging Face revision `80369c1468c5f0cad30f3cd8e9b8b7371e9d9b41`; metadata and weight manifest under `data/sources/releases/2603.03800v1-critic-rubrics/model-metadata/`
- **Release provenance and limits:** `data/sources/releases/2603.03800v1-critic-rubrics/provenance.json`
- **Timing boundary:** the model revision is dated one day after v1. The requested code commit is 85 days after v1, but comparison with the 5 March repository state shows only a LiteLLM dependency/lockfile upgrade. This supports source-level correspondence for the typed annotation package, not exact correspondence to unreleased paper-time training and experiments.
- **Tags:** learned-critic, sparse-outcomes, process-rubrics, human-agent-interaction, selection-policy, early-stopping, production-proxy, configured-system-validity

## One-sentence contribution and assessment

The paper presents a practically important pattern—use a frontier model to densely annotate trace-observable behavioral features, jointly train a cheaper critic on those annotations plus sparse production proxies, and use its score for reranking, stopping, and data selection—and reports strong selection gains on an outcome-variable SWE-bench subset; but unreleased production data/training records, unvalidated rubric labels and proxy joins, ambiguous split clusters, post-selection estimands, dependence-blind uncertainty, model/package label inconsistencies, and an under-specified SFT experiment mean the evidence validates neither the rubrics as process truth nor the critic as a production-quality, human-preference, causal, transferable, or deployment-ready evaluator.

## Why this matters for skill-bench

This review advances charter objectives A–C through a bounded coding substrate. The general benchmark-design question is not “should `skill-bench` use this coding critic?” It is:

```text
work episode and configured observation view
→ trace-observable candidate features
→ sparse delayed proxy join
→ learned critic score/vector
→ selection, stopping, curation, or escalation policy
→ held-out task outcome
→ real workflow and stakeholder consequence
```

The paper's strongest evidence sits in the middle: a fixed learned score can rank pre-generated candidate attempts better than random on selected SWE-bench items, and auxiliary rubric supervision can change ranking behavior across two model backbones. Its weakest leap is from that result to “real-world success” or “reliable evaluation.” Code persistence and merge status are authored proxies; o3 labels are observer outputs; SWE-bench resolve rate is a benchmark endpoint; reranking is a decision policy. None is interchangeable with correctness, maintainability, review burden, user utility, causal process quality, or professional readiness.

The unique transfer is therefore a **typed supervision-and-decision chain**, not the particular 24-feature taxonomy. `skill-bench` should preserve every transformation and require each downstream use to earn its own evidence.

## Research question and defensible claim boundary

The paper asks how to learn a deployable critic when production interactions have sparse, delayed, noisy outcomes. It proposes segmenting human-agent conversations, annotating each segment with trace-visible behavioral features, jointly predicting those features and sparse outcomes, and testing the learned score in ranking, stopping, and training-data selection (Sections 1–5, pp. 1–10).

The full paper supports narrow claims that:

1. the authors define an inspectable 24-feature behavioral/follow-up/infrastructure taxonomy and an o3 structured annotation protocol (Section 3 and Appendices C/G, pp. 5–7 and 15–29);
2. on the manuscript's held-out production segments, critics trained with production-derived labels discriminate PR merge or binarized code survival better than benchmark-only critics under reported AUCs (Table 2, p. 8);
3. on 148 SWE-bench Verified instances selected because eight generated attempts contain both success and failure, the BCE-floor Success+Rubrics critic chooses a successful attempt 73.8% at `K=8`, versus 57.9% for random choice and 63.6% for the Success-Only critic (Table 2, pp. 8–9);
4. under the same selected set, a fixed score threshold and random attempt orders produce a reported `+17.7`-point early-stop result with 1.35 completed attempts on average (Section 5.1, p. 9);
5. the reported ranking direction is positive for both Sonnet 4.5 and Opus 4.5 trajectory pools for the BCE-floor rubric critic, unlike the Success-Only critic (Table 3, p. 9);
6. an equal-size SFT dataset selected by the critic produces 239/500 SWE-bench resolves versus 233/500 for the base and 231/500 for random SFT in one under-described training/evaluation run (Table 4, pp. 9–10); and
7. the released package implements typed o3 annotation and the released model supplies immutable weights for a multi-label classifier.

The evidence does **not** establish rubric correctness, completeness, authority, human agreement, causal process quality, accurate segment credit, production utility, human preference, reviewer burden, merge quality, policy calibration, unbiased portfolio success, cross-scaffold/domain/user transfer, causal training benefit, safety, professional validity, operational cost-effectiveness, production fitness, or readiness.

## Methodology and system reconstruction

### Production corpus, segmentation, and unit hierarchy

The paper reports 38,241 conversations and 151,837 segments, not literally 154,000: 37,855 conversations/150,290 segments in training and 386 conversations/1,547 segments in test (Table 1, p. 5). It converts each multi-turn interaction into user-initiated segments that end at an agent `finish` action. Context-prefix divergence, condensation, tool-configuration changes, and some final natural-language responses also determine boundaries (Section 2.2 and Appendix B.1, pp. 3 and 14).

This is a useful credit-assignment unit, but not a natural ground-truth unit. A follow-up can revise the preceding segment; later segments can overwrite it; one PR can contain several conversations and commits; and one user's sessions, repository, incident, or PR can create many correlated segments. The paper acknowledges overwrite and coarse attribution but does not release the actor, repository, PR, task, session, or conversation clusters needed to inspect independence.

The source frame is also absent. We do not know the production collection dates, eligible users/repos/products, consent or allowed model-training use, language/task distribution, agent/model versions, inclusion/exclusion rules, duplicates, invalid traces, privacy filtering, retention, endpoint changes, or whether the reported sample represents traffic rather than an analyzable subset. “Production” identifies origin, not a population estimand.

### Sparse outcomes and their authority

Two proxies are joined through `PR → commits → segments` (Section 2.3, pp. 4–5):

- **PR merge:** every linked segment inherits the PR's binary merge label. This is observable but coarse; acceptance can reflect reviewer availability, politics, timing, human repair, repository policy, or unrelated commits.
- **Code survival:** attributable commit lines are normalized by file path/change type/text and intersected with the final merged diff. A fully retained segment scores one and a reverted segment zero. Ambiguous commit attribution is left unlabeled (Appendix B.2, p. 14).

Code survival is more localized than PR merge, but “retained” is not “correct.” Boilerplate, a bad change, or human-preserved code can survive; concise or refactored correct work can disappear; moved/renamed/reformatted lines can be undercounted; later human edits can alter identity; generated files, deletions, configuration, tests, and non-line state can have different semantics. The denominator also conditions on attributable commits and a merged final diff. Segments with no commit, unmerged PRs, ambiguous SHAs, or non-code value are missing by construction.

The paper calls survival less confounded and an approximate upper bound for SFT selection (pp. 8 and 10), but provides no manual join audit, precision/recall sample, inter-review evidence, survival-versus-correctness study, missingness model, or negative cases where valid code was replaced. It correctly says survival is noisy learning signal rather than ground truth; later claims should retain that ceiling.

Only 5,349 segments have survival labels and 9,750 have PR labels (4% and 6%). Test composition is sharply enriched: all 1,547 test segments have PR labels and 1,083 have survival labels, while the training set includes all other labeled and unlabeled segments. Section 4.1 says approximately 20% of “outcome-linked segments” are reserved, but does not state whether splitting is grouped by user, conversation, PR, repository, task, time, or incident. If segments or conversations from one PR/repository/user cross folds, shared code, tool schema, user style, or downstream outcome can leak. The test set is an outcome-observable subset, not the 151,837-segment production population.

### The 24-feature rubric: useful observer vocabulary, unvalidated authority

The taxonomy contains 13 agent issues, eight binary user-follow-up patterns plus overall sentiment, and two infrastructure issues (Section 3.1 and Table 6, pp. 5 and 15). Examples include misunderstood intent, insufficient analysis/testing/debugging, incomplete implementation, looping, scope creep, risky actions, correction, frustration, reversion, and external versus agent-caused infrastructure failure.

Its construction is described in one paragraph: random real-world and SWE-Gym trajectories were shown to o3 and Claude Opus 4; unspecified domain experts merged, split, and refined candidate features until “stabilized” (p. 5). Missing are sample size and draw, expert number/roles/authority, coding protocol, rejected features, saturation rule, disagreements, independent content review, user input, alternative taxonomies, prevalence, and held-out confirmation. The taxonomy is plausible, not demonstrated complete or professionally authoritative.

Authority and observability differ by feature:

- **Directly countable or event-near:** three repeated failed actions, a user asks to revert, a VCS request, an explicit command error.
- **Trace-inferred with normative thresholds:** “insufficient” analysis/testing/debugging, incomplete implementation, improper tool choice, scope creep.
- **Intent- or counterfactual-dependent:** misunderstanding, whether clarification was necessary, whether a risky action lacked valid permission.
- **Causal attribution:** external versus agent-caused infrastructure fault.
- **User-state proxy:** sentiment, frustration, progress concern.

A trace can support these with different strength. Some require final repository state, hidden requirements, organizational norms, permission history, or reproduction beyond text. Yet the annotator sees only transformed trace messages and optional next user message—not PR outcomes, survival, downstream artifacts, or an independent environment query (Section 3.2, p. 6). “Trace-observable” means an observer can infer a label from that view; it does not mean the predicate is true or adequately observed.

The released code sharpens this point. The no-follow-up schema has 19 outputs: four generic descriptors, 13 agent issue flags, and two infrastructure flags. The follow-up schema adds nine more fields. The paper's “24” counts a different conceptual subset. The exact training target vector and label ordering are not released. More importantly, the package converts tool messages to user-role text, serializes tool definitions, preserves images when present, and can return `None` when expected system/user/assistant structure is absent. Those transformations and exclusions are part of the observer instrument, but paper counts do not include annotation invalid/missing rates.

### Annotation and semi-supervised learning

o3 with high reasoning effort generates labels for every included segment using structured function calls; the annotator is not shown sparse outcomes (Section 3.2, p. 6). This prevents direct label leakage from those fields. It does not establish independence: the same trace contains user correction, user satisfaction, errors, tests, and other signals downstream of agent behavior and correlated with merge/survival. That is intended supervision, but should not be described as independent validation.

No human annotation sample, o3 repeat study, alternative-judge comparison, criterion confusion matrix, evidence-locator audit, invalid rate, or expert adjudication is reported. Table 8 reports the trained critic's mean AUC of 0.78 against o3 labels on 1,547 test segments (pp. 15–16). It explicitly calls this learnability/consistency rather than human-verified correctness. Even that table covers only 15 agent/infrastructure features—not the full follow-up/generic set—and rare positives range from 13 to 1,423. AUC against a single teacher shows imitation, not truth.

The critic starts from Qwen3-4B-Instruct, receives chat-formatted traces plus tool definitions, uses 64K context with left truncation, and has average/90th-percentile production segment lengths of 38K/69K tokens (Section 4.1, p. 8). Thus a nontrivial tail is truncated, preferentially losing early requirements and actions. The paper does not report truncation rates by label/outcome, whether o3 and critic see identical views, or whether user intent at the left edge disappears while the latest complaint remains.

The core multi-task implementation is not released. Missing details include per-head architecture, exact target vector, rubric/success loss weights, loss normalization under missing outcomes, sampling/reweighting, class imbalance, optimizer, learning rate, batch size, epochs, hardware, checkpoint selection, seeds, training cost, annotation cost, and whether sparse labeled rows are oversampled. Calling the setup “semi-supervised” is directionally reasonable—outcome-unlabeled rows receive teacher-generated auxiliary labels—but those labels are supervised pseudo-labels, not unlabeled-data consistency or ground-truth process observations.

### Rubric association analysis does not validate the features

Section 3.3 compares outcome rates when each binary feature is present versus absent, using Fisher tests and Benjamini–Hochberg correction (pp. 6–7). Appendix D says it also combines datasets with harmonic-mean p-values and uses Wald intervals (pp. 15–16).

The analysis has important limits:

1. segments from common conversations, PRs, repositories, tasks, users, and configured systems are treated as independent;
2. features co-occur, so marginal differences do not isolate a feature;
3. annotator error is ignored;
4. outcome and feature missingness are not modeled;
5. multiple proxies and datasets are heterogeneous, and follow-up features are structurally undefined without a reply;
6. association does not imply a causal failure mode; and
7. broad feature discovery and confirmation appear to reuse the same ecosystem.

The results themselves resist the paper's causal-sounding interpretation. On benchmarks, incomplete implementation/testing/debugging have large negative associations. In real-world Table 7, incomplete implementation is `+0.01`, insufficient debugging `+0.02`, looping `+0.06`, file-management errors `+0.06`, risky actions `+0.05`, and scope creep `+0.04`; several are significantly **positive** under the displayed real-world analysis (pp. 16–17). This could reflect confounding, teacher labeling, interaction intensity, selection, proxy failure, or genuine context differences. It does not confirm stable failure semantics. The phrase “causal-looking” on p. 7 is especially unwarranted.

There are also unresolved denominator/reporting differences. Table 1 has 9,750 PR-labeled and 5,349 survival-labeled segments, while Appendix D cites 16,198 and 11,050 unique labeled segments in feature analyses. Table 7 collapses real-world evidence into one column even though Figure 3 and the methods name separate PR and survival conditions. Without released rows/code, the mapping cannot be audited.

## Downstream decision policies and evidence

### SWE-bench trajectory pool and post-selection

The evaluator sees OpenHands trajectories for 500 SWE-bench Verified tasks, four Sonnet 4.5 attempts and four Opus 4.5 attempts per task. The Combined `K=8` analysis retains only 148 tasks where at least one attempt succeeds and at least one fails (Section 4.1, p. 8). This **rerankable subset** is legitimate for estimating an oracle opportunity-conditioned ranking policy. It is not overall SWE-bench performance, portfolio capability, or expected production benefit. The omitted 352 always-fail/always-succeed tasks matter to cost and deployment value.

The paper does not release task IDs, attempts, seeds, order, harness/environment versions, score rows, invalids, contamination audit, or the overlap between SWE-Gym critic training and SWE-bench repositories/issues. Outcome-conditioned subset selection also changes backbone composition: a task may be mixed only because one model family succeeds. Cross-backbone “generalization” is therefore within one scaffold, one public benchmark, two closely timed Claude backbones, and selected tasks—not cross-scaffold, cross-domain, or production transport.

### Best-of-K

At `K=8`, the BCE-floor rubric critic reaches 73.8% on the 148 mixed tasks, versus 63.6% Success-Only and 57.9% random (Table 2). This is the paper's strongest result because selection is evaluated against external tests rather than the sparse production proxy.

However:

- no task-cluster bootstrap or confidence interval is supplied;
- multiple objectives, encodings, checkpoints, `K` values, backbones, and policies are compared without a declared model-selection/confirmation split;
- candidate-order construction for `K<8` is unclear, while reported Best@K is nonmonotonic;
- Table 9 reports a different final BCE-floor Best@8 of 77.8 and random of 73.2, versus 73.8 and 57.9 in Table 2, without identifying a different subset or denominator;
- critic inference cost and failure handling are absent; and
- a ranking gain validates that score-policy on this candidate pool, not every rubric feature or the production success head.

Auxiliary rubrics may act as regularization, representation shaping, teacher distillation, or extra compute. The study lacks a matched random auxiliary-label control, feature-family ablation, label-noise ablation, or human-corrected rubric condition. Consequently, “rubric supervision improves ranking” is supported as a package contrast; “the 24 features capture true causal process quality” is not.

### Early stopping

Attempts are randomly permuted 100 times; the first completed trajectory with score at least 0.5 is accepted, up to eight (p. 9). BCE-floor reports a 17.7-point success increase over random while averaging 1.35 attempts, described as 83% compute reduction.

This is a useful replay policy simulation, but “83% compute” means fewer **completed candidate attempts** than always generating eight. It does not measure tokens, wall time, dollars, critic inference, parallel scheduling, failed requests, latency tails, or opportunity cost. The threshold is not tied to a calibrated success probability or declared false-accept/false-reject loss, and no untouched threshold-validation set is described. Because the analysis is restricted to mixed tasks, it omits always-fail cases where confident false acceptance is costly and always-success cases where stopping is easy. A policy can use few attempts by accepting early failures; attempt count and outcome must be reported jointly over the full eligible portfolio.

### SFT data curation

Three equal-size sets of 3,673 production segments train Qwen3-Coder-30B-A3B-Instruct: critic-selected from the full corpus, random from the full corpus, and observed `survival=1` (Section 5.3, pp. 9–10). Reported resolves are 239, 231, and 252 versus 233 for the base.

This experiment is too under-specified for a causal training claim. The critic appears to rank its own training corpus in sample; selected rows may differ in task, length, user, repository, duplication, code volume, or model source; training hyperparameters and seeds are absent; only one count per arm is shown; model/harness evaluation configuration is omitted; and task-level paired outcomes are unavailable. The critic-selected gain over base is six tasks (`+1.2` points), while random SFT is two lower. No uncertainty or repeated training runs establish that difference beyond stochastic variation. Proxy-filtered SFT is not an “upper bound”: a noisy proxy-selected dataset can be surpassed by a better selector, and its different missingness/source composition is part of the treatment.

The result is a hypothesis that critic ranking can improve data curation, not validation of the critic's production quality or causal process semantics.

## Official release and model audit

### What the code release actually provides

The 43-path package is a compact, inspectable annotation library. It provides:

- typed binary, classification, and text predictions with rationales;
- concrete no-follow-up and follow-up prompts;
- tool-schema generation and forced function calling;
- conversion of system/tool/assistant/user messages into an annotation view;
- synchronous and batch LiteLLM requests with retries;
- output parsing/consolidation scripts; and
- unit tests for schema and conversation conversion.

A fresh isolated run passed all 10 tests in 2.76 seconds. This verifies the pinned package under the local environment, not empirical claims. There is no production corpus, label table, critic training implementation, success head, reranking/early-stop code, SFT code, result rows, or analysis notebook.

The transformation is not neutral. It takes the first system message's content but later assumes `messages[0]` is the original system message; turns tool results into user messages; embeds tool descriptions in the first user block; appends annotation instructions at the end; and returns no request for some missing-role cases. These are reasonable engineering choices, but they alter role semantics and eligibility and should be hashed as the grader's evidence view.

### Model release correspondence and an unresolved output contract

The Hugging Face revision preserves approximately 8.05 GB of BF16 shards and a `score.weight` classification head. The API identifies roughly 4.41B parameters. The model card says **26 labels: 25 rubric features plus one success prediction**. Yet:

- the paper repeatedly says 24 rubric features plus success;
- the model `config.json` declares `LABEL_0` through `LABEL_26`, i.e. 27 outputs;
- the config provides only generic label names;
- the released annotation package exposes 19 no-follow-up fields or 28 with follow-up, including generic descriptors/timing; and
- no immutable mapping connects output index to feature/proxy variant.

The model may be usable through a separate SDK, but the exact revision alone is not self-describing enough to audit which score is success, which rubrics are represented, how unavailable follow-up fields are encoded, or whether this is the BCE-floor checkpoint reported in Table 2. The weights were not duplicated locally; immutable revision, shard sizes/LFS hashes, config, card, and tensor index are preserved in provenance. No 8 GB inference replay would repair the missing label map or reproduce unreleased evaluation inputs.

### Cost and operational realism

The only direct latency study uses ten segments: o3 averages `17.0±6.3` seconds and the self-hosted 4B critic `1.1±0.8`, called a 16× speedup (Appendix A, pp. 13–14). Hardware, batching, token length distribution, endpoint concurrency, warmup, energy, and dollar cost are omitted. Annotation all 151,837 segments, critic training, 64K inference, eight-attempt generation, SFT, storage, privacy review, and human rubric work have no total ledger.

The problem is operationally realistic: multi-turn work, changing requests, tools, follow-up, sparse outcomes, partial overwrites, and bounded repeated attempts are real. The empirical operation is not reproducible enough to establish production utility: traffic and privacy boundaries are hidden; proxies are unvalidated; no live randomized policy test is run; no human escalation or drift study is reported; and the strongest decision evidence comes from replay on public SWE-bench trajectories.

## Evidence interpretation

### What is genuinely learned

1. **Dense trace-observer targets can be useful auxiliary supervision even when outcome labels are sparse.** The Best@8 package contrast is meaningful evidence that o3-derived behavioral labels can shape a useful ranker.
2. **Proxy choice changes the learned evaluator.** Merge and survival produce different intrinsic and downstream behavior; the outcome field is part of the instrument, not neutral truth.
3. **AUC is not policy utility.** MSE survival and benchmark-only critics can have plausible intrinsic AUC yet rank candidates below random. Every intended decision requires direct evaluation.
4. **Configured-system transport matters.** Success-only ranking changes sign across Sonnet/Opus pools, while one rubric-supervised variant is positive in both. Even this is a narrow two-backbone, one-scaffold bridge.
5. **Process labels can be diagnostic without being causal.** The vector is potentially useful for review routing, but marginal associations and teacher imitation do not identify root causes.
6. **The sparse proxy and auxiliary feature channels must remain separate.** A model can learn one from the other without validating either as professional quality.

### What the headline results do not license

- `AUC=.69` against binarized survival is not correctness or user utility.
- mean rubric `AUC=.78` against o3 is teacher imitation, not human/expert accuracy.
- `+15.9 Best@8` is opportunity-conditioned selection on 148 mixed tasks, not a 15.9-point overall agent capability gain.
- `83% fewer attempts` is replayed completed-attempt count on that subset, not total production compute/cost reduction.
- positive ranking on two Claude backbones is not cross-domain or cross-scaffold generalization.
- `+1.2` SFT is a single under-specified count contrast, not identified causal training benefit.
- release of weights and annotation code is not release of the training/evaluation evidence.

## Unique insight for skill-bench

> **A learned critic has at least three separable validity targets: feature observation, proxy prediction, and decision-policy utility. Success at the last can coexist with error or invalidity at the first two.**

That yields a reusable nested record:

```text
source episode and eligible population
→ segmentation/credit unit and cluster lineage
→ observer evidence view and candidate feature vector
→ feature authority/accuracy/reliability
→ outcome/proxy definition, join, window, missingness, and audit
→ critic training objective, target availability, loss weighting, and split firewall
→ score calibration/discrimination on untouched units
→ consumer policy (rank/stop/curate/escalate), threshold, budget, and loss
→ full-population policy effect with uncertainty and cost
→ external workflow/stakeholder consequence and transport boundary
```

A downstream policy gain can validate the **joint score-policy pair** for one candidate distribution even if rubric labels are merely useful latent regularizers. Conversely, highly accurate rubric imitation need not improve any decision. `skill-bench` should explicitly allow this asymmetric result rather than force one omnibus “critic quality” claim.

A second insight is **consumer-specific selection changes the estimand**:

- rerankable mixed tasks estimate selection opportunity conditional on candidate diversity;
- early-stop replay estimates a sequential policy conditional on available completed attempts and threshold;
- critic-selected SFT estimates a data-composition treatment;
- production monitoring would estimate population behavior under naturally occurring traffic.

One critic score can feed all four, but no result automatically validates another consumer.

## Comparison with adjacent project evidence

- **AgentLens** provides richer formal checks, trace reviews, regression routing, and configured reports, but no production-user outcome. This paper adds sparse operational proxies and learned dense supervision; it is weaker on observer validation, task lineage, report evidence, and intervention adjudication. Both require separating trace observation, user outcome, alert, and post-change utility.
- **Signals** changes which trajectories enter review and warns that enriched yield is not prevalence. Critic ranking similarly creates outcome-conditioned candidate sets. Mixed-subset Best@K and critic-selected SFT must not become unweighted population capability or training-data-quality claims.
- **AgentRewardBench** compares judges against preserved expert labels and exposes evidence-view and predicate-specific errors. Here no human criterion sample exists. o3 labels are training targets, not expert ground truth, and success-proxy AUC cannot substitute for feature-level accuracy.
- **Many-Facet rater effects** distinguishes agreement, severity, fit, and decision validity. The present paper has one teacher annotator configuration and one learned imitator; it cannot estimate teacher severity, expert disagreement, task-feature interactions, or bridge stability.
- **Criterion-validity/business-outcome review** distinguishes concurrent association, prediction, intervention, and decision utility. Merge/survival associations are even farther upstream: they are sparse proxy joins, while the strongest policy test uses SWE-bench tests rather than a prospective field consequence.
- **AdaRubric** separates criterion generation, observation, aggregation, and reward use but lacks empirical conformance. This paper supplies a stronger downstream selection contrast and a real released model, while still leaving criterion authority, exact output mapping, and reward/training causality unresolved.

The nonduplicate conclusion is that a critic record must bind **observation input → target channels → score vector → consumer policy → policy-specific outcome**, with separate claim ceilings and full missingness/cluster lineage. Existing configured-system, evidence-view, grader, metric-monitoring, task-health, validity, and decision-policy machinery is the correct home; a coding-specific critic schema would duplicate it.

## Limitations and validity threats

1. Production source population, dates, traffic composition, eligibility, and exclusions are unreleased.
2. Consent, privacy, allowed training use, retention, user withdrawal, and de-identification process are not reported.
3. “154K” rounds a reported 151,837 segments without preserving exact denominators in prose.
4. Segments are authored boundaries, not natural independent work units.
5. User, conversation, PR, repository, task, incident, and temporal clustering are unreported in splits and inference.
6. Test-set reservation is not stated to be group- or time-disjoint.
7. PR merge is a coarse, multiply determined acceptance proxy.
8. All segments linked to a PR inherit one merge label despite overwrite and mixed contribution.
9. Code survival measures normalized line persistence, not correctness, maintainability, utility, or authorship purity.
10. Survival excludes ambiguous/no-commit/unmerged work and is missing not at random.
11. Commit-attribution precision/recall and survival identity matching have no manual audit.
12. Outcome windows and later revert/regression behavior are unspecified.
13. Rubric construction sample, experts, authority, disagreements, saturation, and rejected features are absent.
14. Trace observability is asserted across features with materially different evidence demands.
15. Normative “insufficient,” permission, intent, and causal infrastructure labels may require state or policy unavailable to the observer.
16. One o3 configuration produces all dense labels; no human or alternate-judge accuracy study exists.
17. Annotation repeatability, invalidity, abstention, and evidence-locator quality are unreported.
18. Follow-up features are structurally unavailable without replies, but availability/missingness is not modeled as an estimand.
19. Released package field counts do not cleanly correspond to the paper's 24-feature target.
20. Critic Table 8 evaluates only 15 behavior/infrastructure features against the teacher, not all stated features.
21. Rare feature AUCs rest on as few as 13 positives.
22. Teacher-imitation AUC does not establish label truth.
23. Average traces are 38K tokens and the 90th percentile is 69K, while critic training truncates left at 64K.
24. Truncation can remove original requirements while retaining later complaints, and no sensitivity study exists.
25. Multi-task architecture, label map, loss weights, missing-target normalization, optimizer, sampling, seeds, hardware, and training cost are absent.
26. Marginal feature–outcome associations ignore feature co-occurrence and hierarchy clustering.
27. Wald intervals can be poor for rare, dependent binary features.
28. Many purported failures have positive real-world outcome associations, undermining simple causal interpretation.
29. Appendix feature-analysis denominators do not reconcile with Table 1's labeled-segment totals.
30. Table 7's real-world outcome column does not transparently preserve separate merge/survival analyses.
31. Harmonic-mean p-values combine heterogeneous proxy/benchmark conditions without validating construct equivalence.
32. SWE-Gym training and SWE-bench evaluation contamination/repository overlap are not audited.
33. Exact SWE-bench tasks, trajectories, seeds, scores, invalids, and environment versions are unreleased.
34. The 148-task mixed subset is conditioned on realized candidate outcomes and excludes portfolio failures/successes.
35. Candidate ordering and Best@K construction for `K<8` are under-specified.
36. Multiple objectives, encodings, checkpoints, backbones, K values, and policies lack a frozen selection/confirmation split.
37. Best@K and early-stop estimates have no task-cluster uncertainty.
38. Table 9's 77.8/73.2 final/random Best@8 values do not reconcile with Table 2's 73.8/57.9.
39. Cross-backbone evidence covers only two Claude backbones under one OpenHands scaffold.
40. No random/noisy auxiliary-target control identifies semantic rubric supervision over generic multi-task regularization.
41. Early stopping uses a fixed 0.5 score without probability calibration or threshold-loss basis.
42. Early-stop evaluation omits always-fail and always-success tasks.
43. “Compute reduction” counts attempts, not tokens, latency, dollars, critic overhead, parallelism, or failures.
44. SFT selection is apparently in-sample with respect to critic training.
45. SFT datasets can differ in task/user/repository/length/duplication composition despite equal row counts.
46. SFT hyperparameters, seeds, training cost, and exact evaluation configuration are absent.
47. Six extra solves over base have no repeated-seed or paired-task uncertainty.
48. Survival-filtered SFT is not a mathematical or empirical upper bound.
49. Code release contains annotation machinery but no critic training, success head, experiments, or empirical rows.
50. Pinned code is post-v1, though only dependency files differ from the 5 March state.
51. Model card says 26 outputs, config exposes 27 generic labels, and paper implies 25 total targets.
52. No immutable output-index map identifies rubric/success channels or proxy variant.
53. The released model is not proven to be the exact BCE-floor final checkpoint used for Table 2.
54. Weight availability does not reproduce hidden inputs, training, or downstream result records.
55. Ten release unit tests validate code mechanics, not labels, model behavior, or paper results.
56. Latency comparison has only ten segments and omits hardware/workload comparability.
57. Total annotation, training, inference, trajectory-generation, storage, privacy, and review cost is absent.
58. No live randomized field test evaluates reranking, stopping, curation, or user outcome.
59. No drift, reward-hacking, subgroup, safety, escalation, false-accept, or rollback study exists.
60. No evidence supports professional validity, production utility, cross-domain transfer, production fitness, or readiness.

## Reproducibility and operational realism

**Conceptual reproducibility is moderate to high.** The immutable paper preserves segmentation equations, proxy definitions, the 24-feature taxonomy, full annotator prompts, principal sample counts, model family/context, objective variants, aggregate results, and intended consumers. The official package preserves concrete typed prompts and trace transformation. The model revision preserves weights and basic configuration.

**Empirical reproducibility is low.** The production corpus, outcome joins, annotations, splits, training implementation/configuration, exact target map, checkpoints, SWE trajectories, per-task scores, early-stop simulations, SFT rows/configurations, seeds, analysis code, and costs are unavailable. Aggregate tables cannot be replayed, denominator inconsistencies cannot be resolved, and the released 27-output config is not self-mapping.

**Operational realism is mixed.** Sparse feedback, delayed outcomes, multi-turn revisions, tool traces, commit lineage, repeat attempts, and cheap evaluators are genuine production concerns. But the deployment evidence is retrospective and hidden; user utility is not measured; the proxy/teacher channels are unvalidated; the policy tests are public benchmark replay; and no live monitoring/adjudication/intervention loop is observed. This is a promising evaluator-development method with one strong bounded ranking result, not a validated production evaluator.

## Transfer to skill-bench

### Retain

1. **Represent conversation/workflow segments explicitly, but preserve their parent hierarchy.** Every segment must link to session, task, actor, artifact, source incident, and downstream state so clustering and overwritten work remain visible.
2. **Keep sparse outcomes and dense process observations as separate channels.** Record authority, timing, availability, missingness, and who/what produced each.
3. **Use typed feature vectors with rationales/evidence locators.** Dense process labels are useful for diagnosis and auxiliary learning even when they are not truth.
4. **Evaluate every consumer policy directly.** Ranking, stopping, review routing, curation, monitoring, and promotion have different eligible populations, thresholds, losses, and outcomes.
5. **Preserve configured-system identity and input transformations.** Trace converter, truncation, tool schema, teacher, critic checkpoint, output map, and consumer policy are all instrument components.
6. **Report negative transfer.** Benchmark-only and MSE critics ranking below random are valuable task-health evidence, not results to hide.

### Repair

1. **Add feature authority/observability typing:** `direct_event`, `artifact_state`, `trace_inference`, `normative_judgment`, `user_state_proxy`, or `causal_hypothesis`; declare required/actual channels and abstain when insufficient.
2. **Validate the teacher separately:** use independent experts/users on held-out, cluster-sampled episodes; preserve plural labels; estimate criterion confusion, repeat stability, evidence-view effects, and authority boundaries.
3. **Audit proxy joins:** sample commit/segment matches and misses; adjudicate persistence versus correctness; preserve unmerged/no-commit/ambiguous rows; model availability rather than dropping it.
4. **Split by the highest leakage unit:** actor/repository/task/PR/incident/time as appropriate, with explicit overlap ledgers and untouched bridge sets.
5. **Freeze exact target/output maps:** every checkpoint must bind label names, order, proxy encoding, loss weights, missing-target masks, training rows, and code/environment hashes.
6. **Treat truncation as missing evidence:** record dropped token ranges/channels and test early-requirement/late-complaint counterexamples.
7. **Use full-population policy evaluation:** report all-fail, all-success, and mixed strata; combine them under an explicit portfolio distribution; preserve invalid/provider failures.
8. **Calibrate decisions, not only scores:** choose ranking/stopping thresholds on development units under declared false-accept, false-reject, latency, and cost losses; confirm on untouched clusters.
9. **Factor the rubric effect:** compare true rubric labels with shuffled, prevalence-matched, reduced-family, alternative-teacher, and human-corrected auxiliary targets.
10. **For data curation, freeze selectors out of sample:** use matched data volume/composition, duplicate controls, multiple training seeds, held-out task families, regression/safety endpoints, and total cost.

### Minimal validation design

Across at least two materially different knowledge-work artifact families:

- freeze an eligible episode population with actor/task/source clusters and full invalid/missing ledger;
- define sparse external outcomes with observation windows, reversals, and proxy audits;
- independently label a probability sample with multiple authorized experts and one model teacher;
- cross full-trace, truncated-trace, artifact-only, and state-query evidence views;
- train critics with success-only, authorized rubrics, teacher rubrics, shuffled/prevalence-matched rubrics, and reduced feature families under identical compute;
- evaluate feature accuracy, proxy discrimination, calibration, and ranking/stopping/escalation policies separately;
- include all-success/all-fail/mixed strata, valid alternatives, misleading self-report, overwritten work, ambiguous permissions, external versus agent-caused failures, and proxy–quality disagreement;
- report clustered uncertainty, subgroup error, abstention, tokens/latency/cost, human review, false acceptance/rejection, and downstream workflow burden; and
- license only the feature-observation, proxy-prediction, policy-utility, or consequence claim directly supported.

This tests the general hypothesis that dense trace supervision improves sparse-outcome decisions without laundering its features into authoritative process truth.

## Concrete repository actions

1. **Index this review as a release-audited critic/production-measurement source.** Its key addition is the three-target distinction: feature validity, proxy validity, and consumer-policy validity.
2. **Do not add a new schema or build task.** Existing configured-system, trace/evidence-view, rubric criterion, grader observation, task-health, metric-monitoring, validity-argument, decision-policy, and expert-participation contracts can absorb the requirements. The evidence calls for an empirical cross-domain critic-policy validation slice, but that is not currently executable without authorized labels/outcomes and would duplicate existing planned validation boundaries if queued now.
3. **During the next relevant consolidation, add the supervision-to-consumer chain and forbid promotion from mixed-subset ranking gains to population capability or production utility.** Preserve the release's output-map discrepancy as an instrument-conformance example.

## Action items completed

- [x] Read the full immutable 29-page v1 paper and all appendices/prompts.
- [x] Reconstructed the 151,837-segment corpus, sparse outcomes, 24-feature taxonomy, teacher annotation, multi-task critic, production holdout, SWE ranking/stopping, and SFT curation claims.
- [x] Audited units, proxy authority, missingness, clusters/splits, observability, annotation validity, truncation, uncertainty, selection, cost, negative cases, and claim ceilings.
- [x] Archived and inspected the complete official 43-path code release at exact commit, established its post-v1 dependency-only timing delta, and executed its tests (`10 passed`).
- [x] Preserved exact Hugging Face model revision metadata, weight shard hashes/sizes, config, model card, and tensor index without duplicating 8.05 GB of weights.
- [x] Identified the paper/model/package output-count and label-map inconsistency.
- [x] Compared nonduplicatively with AgentLens, Signals, AgentRewardBench, Many-Facet, criterion-validity, and AdaRubric reviews.
- [x] Added no duplicate build task; mapped requirements to existing general contracts.

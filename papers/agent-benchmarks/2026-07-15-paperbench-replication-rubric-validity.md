# PaperBench: dense replication rubrics observe partial reconstruction, not successful replication

## Bottom line

PaperBench is an unusually ambitious and inspectable attempt to evaluate end-to-end research reproduction. It turns 20 recent machine-learning papers into repository-building tasks, asks agents to produce executable code and results, decomposes expected outcomes into 8,316 leaf criteria, grades code, execution, and analysis, repeats model runs, and compares a three-paper subset with human attempts. The release contains the papers, addenda, rubrics, judge implementation, expected JudgeEval labels, aggregate tables, and a runnable framework. Those are substantial contributions.

The headline **Replication Score is not a replication-success measure**. It is a recursively weighted average of local criterion judgments. Downstream result points can compensate for missing implementation requirements; dependencies are prose and judge context, not score gates; invalid judge calls become zero-valued leaves inside otherwise “successful” grading runs; and no empirical threshold links a score such as 21% to a minimally successful reproduction. The paper itself reports averages rather than complete-reproduction rates. PaperBench therefore measures **partial rubric-attested reconstruction under one authored decomposition and one configured judge**, not whether a paper was replicated.

The judge study narrows the claim further. JudgeEval contains five hand-labelled submissions and 2,693 released leaf labels. Its reported o3-mini result is useful evidence of binary criterion agreement with that labeling procedure, but not validation of task-level scores. The released evaluator pools all leaves before computing class-macro F1, so a 1,963-leaf example has almost 25 times the influence of a 79-leaf example. Raw model predictions needed to independently reproduce the reported F1 are absent. The five examples do not cover all 20 papers, important legitimate alternatives, threshold decisions, severe-error costs, judge stochasticity, or agreement among independent human graders.

The unique transferable insight is a **replication evidence lattice**: implementation, execution, result correspondence, dependency satisfaction, provenance, and reproducibility are distinct observations. A benchmark should preserve that vector, apply noncompensatory prerequisite gates where the claim requires them, and report partial progress separately from a thresholded replication claim. Dense rubrics are valuable diagnostics; they do not become a validated construct merely by having thousands of leaves.

## Why this matters: charter relevance and useful completion

This review advances charter objectives A, B, C, D, and E through comparative expansion, consolidation, release validation, and benchmark-building implications. PaperBench is a bounded scientific-work case, not a proposal to narrow `skill-bench` to academic replication. Its general hypothesis is that tacit expert expectations can be decomposed into inspectable, executable evidence obligations for long-horizon knowledge work.

The concrete evidence is the full immutable paper, two pinned official-release snapshots, a machine-readable audit of 20 current rubrics and five JudgeEval label trees, and a retain/repair/test account. The uncertainty clarified is what dense expert-authored criteria, automated judging, a human comparison, and released code actually license. Useful completion means separating partial criterion attainment from end-to-end completion and adding evidence-backed follow-up tasks without duplicating existing rubric, artifact, task-health, trace, or validity machinery.

## Sources and reading record

### Immutable primary paper read in full

- Giulio Starace et al., *PaperBench: Evaluating AI's Ability to Replicate AI Research*.
- Immutable arXiv v3: <https://arxiv.org/abs/2504.01848v3>; PDF: <https://arxiv.org/pdf/2504.01848v3>.
- Local PDF: `data/papers/pdfs/2504.01848v3-paperbench.pdf` (30 pages; SHA-256 `2f58f1a6581af9d99432422dccf3cf61f5c263377c1e4550e7333c4a22d7184d`).
- Local full-text extraction: `data/papers/text/2504.01848v3-paperbench.txt` (SHA-256 `b01a27ec25a7a1d82c6613f295cf42e2a470a4167391b1fb194ddd2d992f66d3`).
- Version read: v3, submitted 7 April 2025; read 15 July 2026. The complete main paper and appendices were read, including paper selection, rubric construction, task instructions, judge prompts, JudgeEval, agent experiments, human baseline, monitoring, cost, failure analysis, and limitations. No withdrawal notice was present in the inspected record.

### Official artifact audited

- Official repository: <https://github.com/openai/frontier-evals/tree/main/project/paperbench>.
- Initial declared PaperBench release: commit `352ed048d510a2525aea658489b3839b4efc412b` (2 April 2025), archived as `data/sources/releases/2504.01848v3-paperbench/openai-frontier-evals-paperbench-352ed048.zip` (SHA-256 `b75a96735cc2c93fae00e9f245a5cc915372b854b40b46b1346e2c40eaaf9735`; 1,138,888 bytes).
- Review-time `main`: commit `51052cede8cc608f95bb00346635e03759013e5a` (21 April 2026), archived as `data/sources/releases/2504.01848v3-paperbench/openai-frontier-evals-paperbench-51052ced.zip` (SHA-256 `be40897c77e7bdfd21cce12410445a570510fcc93ebe278bcf6ff67193b6024b`; 1,465,386 bytes).
- Provenance: `data/sources/releases/2504.01848v3-paperbench/provenance.json`.
- Reproducible static/replay findings: `data/sources/releases/2504.01848v3-paperbench/audit.json`.

The timing boundary matters. The initial public commit predates v3 and does not contain the `stochastic-interpolants` task even though v3 lists it among the 20 papers; that task was added on 8 April 2025. Current `main` postdates v3 by more than a year. Neither snapshot alone proves exact paper-time implementation identity. The archives preserve Git-tracked Git-LFS pointer objects; not every large paper, submission, or result payload was hydrated. Artifact claims below distinguish what was directly inspected from what the paper reports.

## One-sentence contribution

PaperBench operationalizes long-horizon machine-learning replication as a public, hierarchical, criterion-level artifact evaluation with executable submissions and a calibrated model judge, but the resulting scalar is a compensatory partial-progress index rather than evidence that a paper was successfully replicated.

## Research question and licensed claim

The paper asks whether frontier AI agents can independently replicate contemporary AI research from a paper and clarifying addendum. It contributes:

1. 20 ICML 2024 Spotlight/Oral papers selected to be feasible with commodity hardware and without restricted resources;
2. author-assisted hierarchical rubrics with 8,316 individually graded outcomes;
3. a task environment requiring a repository, `reproduce.sh`, and generated results;
4. SimpleJudge, which inspects submitted files and reproduction logs criterion by criterion;
5. JudgeEval, a five-submission human-labelled evaluation of automated grading;
6. repeated 12-hour trials of six model backends under BasicAgent, plus selected IterativeAgent studies;
7. a 48-hour human comparison on three retained papers; and
8. PaperBench Code-Dev as a lower-cost code-only variant.

The evidence supports a bounded statement: selected configured systems satisfy different fractions of one author-assisted set of local reconstruction criteria under the released judge, and human attempts satisfy more of those criteria on the retained comparison subset. It does **not** establish a calibrated probability of replication, scientific validity of produced results, general research capability, autonomous discovery, productivity substitution, or readiness to conduct research without expert review.

## Methodology and system

### Task selection and target construct

The 20 targets are recent AI papers selected from ICML 2024 Spotlights and Orals. Authors exclude work needing more than one GPU, more than roughly 12 hours of reproduction runtime, nonpublic data, human participants, external hardware, unavailable checkpoints, or excessive complexity. This is sensible operational curation. It also conditions the benchmark on compute-feasible, artifact-recoverable, predominantly computational ML work. Conference prestige and feasibility are not a sampling frame for research replication.

Candidates receive the paper PDF/Markdown, an addendum, and instructions. They must build a fresh repository and a top-level `reproduce.sh`; the harness later executes the script and grades its output. The task permits packages, public datasets, and online resources while blacklisting original author code and other direct implementations. The paper reports string-based URL monitoring plus manual review, finding ten prohibited-resource uses across 646 runs and assigning those runs zero.

This exposure boundary is useful but porous. URL-string detection does not establish absence of mirrored code, renamed repositories, copied snippets, indirect retrieval, or model pretraining exposure. Public papers, rubrics, and release artifacts also create contamination risk for post-release systems. A “from scratch” claim therefore requires execution-time network logs, content provenance, package/cache manifests, and exposure policy—not only blacklist hits.

### Rubric construction

Rubrics form trees whose leaves fall into Code Development, Code Execution, and Result Analysis. Criteria are weighted among siblings; every leaf is designed to be reviewable in less than 15 minutes by a familiar expert. One original paper author co-develops and signs off each rubric. The paper states roughly 8,000 hours of rubric labor.

This is a strong elicitation and inspectability intervention. It makes expected outcomes, decomposition, weights, and local evidence queries available for criticism. Current release inspection reconstructs 20 main-split rubrics with 11,218 total nodes and exactly 8,316 leaves: 3,671 Code Development, 4,079 Code Execution, and 566 Result Analysis. No nodes have zero weight.

But one-author involvement establishes task-specific authorial provenance, not reliability or exhaustiveness. The paper does not report independent rubric authors, disagreement, rejected criteria, revision rounds, held-out alternative implementations, novice/expert discrimination, or whether a second paper author would assign the same requirements and weights. Eight thousand hours measures effort, not criterion validity.

The release also demonstrates why review and validation remain necessary after expert signoff. Six node IDs are duplicated within two current rubrics. Duplicate IDs make criterion identity non-unique and can make `find(id)`-based alignment ambiguous. Later changes altered three `bridging-data-gaps` criteria from Code Development to Code Execution, the missing twentieth task was added after the release commit, and a paper addendum later received an SVD erratum. These changes are not evidence that the suite is bad; they are evidence that a rubric is a versioned measurement instrument with a repair lifecycle.

### Scoring semantics

Leaf scores range from 0 to 1. Parent scores are recursively computed as weighted averages of their children, and the root becomes the Replication Score. The hierarchy is useful for summaries, but its semantics are compensatory:

- sibling weights are normalized locally, so effective leaf influence is the product of weights along its path;
- a missing prerequisite does not gate descendants;
- implementation, execution, and result-analysis points can trade off unless the authored tree happens to weight them otherwise;
- the same root score can arise from materially different failure structures; and
- the paper provides no calibrated score threshold for “replicated.”

Dependencies appear in criterion wording and ordering. SimpleJudge includes a bounded set of previously graded nodes in later prompts, which may improve consistency, but score propagation does not enforce causal prerequisites. A submission can receive local result-analysis credit even when the implementation lineage that should produce that result is missing or invalid. Conversely, a correct alternative implementation can lose points when it does not match the authored decomposition.

The released human expected-result trees replay exactly under recursive sibling-weighted aggregation: every stored internal score matches recomputation. This validates implementation consistency, not construct validity. The important question is not whether weighted averaging was coded correctly; it is whether a compensatory average licenses the word “replication.” No evidence in the paper answers that question affirmatively.

### SimpleJudge and evidence access

SimpleJudge traverses rubric leaves, searches the submission, gathers file excerpts and reproduction-log evidence, and asks a model to produce a score and explanation. The paper uses o3-mini high after JudgeEval. This is materially better than judging only a final report: the judge can inspect code, execution logs, artifacts, and a criterion-specific evidence trail.

Its evidence still has limits. The prompt receives selected excerpts rather than an independently executed causal trace for every requirement. A file may contain code without that code producing the recorded output; a log may contain a number without trustworthy lineage; scientific correctness may require rerunning, data inspection, numerical sensitivity, or domain judgment beyond the evidence window. The judge sees the target paper and rubric, which improves reference conformity but can encourage one-path matching.

Exception handling is consequential. If leaf grading throws, the framework returns score 0 with `valid_score=false`; parents nevertheless aggregate that zero. `JudgeOutput.success` is true whenever fewer than all leaves are invalid. Thus a partially failed judge run can remain a scored “successful” result. The invalid count is stored, but the audited release does not contain the complete paper-result ledger needed to determine whether and how many invalid leaves entered published scores. Infrastructure invalidity and substantive task failure therefore share the scalar unless downstream analysis explicitly separates them.

## JudgeEval: useful calibration, incomplete validation

JudgeEval uses five submissions spanning five papers. Human experts label every rubric leaf binary satisfied/unsatisfied; automated judge labels are compared with accuracy, precision, recall, and F1. The paper reports overall o3-mini performance around 0.83 F1 and human performance around 0.95, with category slices and estimated cost.

The release preserves five expected-result trees with 2,693 human labels: 1,189 positive and 1,504 negative. The examples are highly unequal: 79, 116, 174, 361, and 1,963 leaves. Local replay confirms all five human trees are internally consistent with the released recursive weighting algorithm.

Three validity boundaries matter:

1. **The aggregation unit is leaves, not papers.** `run_judge_eval.py` extends one pooled `y_true`/`y_pred` vector across examples and computes class-macro metrics. The 1,963-leaf PINN submission therefore contributes almost 25 times the observations of the 79-leaf semantic-self-consistency submission. “Macro” refers to averaging the two class metrics inside `sklearn`, not equal weighting across papers. This may be a legitimate leaf-level estimand, but it does not estimate expected judge accuracy for a new paper.
2. **Label concordance is not score or decision validity.** F1 does not show whether root scores are calibrated, whether rank order is preserved, whether threshold-near decisions agree, or whether high-weight/severe errors are acceptably rare. A judge can achieve strong pooled F1 while making a few consequential errors that change a task conclusion.
3. **Human truth is under-specified.** The paper does not report independent duplicate labels per leaf, inter-rater reliability, disagreement/adjudication, annotator assignment, blinding, uncertainty, or systematic testing of legitimate alternatives. The human row is agreement with a human labeling procedure, not an error-free oracle.

Reproducibility is also partial. Expected human labels, metric code, and generated metric tables are released. The raw model prediction/result JSON files referenced by plotting scripts are gitignored and absent from the audited subtree, so the published o3-mini F1 cannot be recomputed from released leaf predictions. The current table reports overall accuracy 0.8273 and F1 0.8266 for the named o3-mini configuration, but it is an aggregate output, not the underlying evidence ledger.

JudgeEval therefore supports choosing o3-mini over weaker tested model judges for this small labelled set. It does not establish cross-paper judge validity, future-model stability, professional acceptance, or an automated replacement for expert reproduction review.

## Evidence and results

The main experiment runs GPT-4o, o1, o3-mini, DeepSeek-R1, Claude 3.5 Sonnet (New), and Gemini 2.0 Flash over 20 papers, nominally three runs per paper, for up to 12 hours. Claude 3.5 Sonnet leads BasicAgent at 21.0% average Replication Score. IterativeAgent improves o1 and o3-mini but hurts Claude 3.5 Sonnet, showing that the configured scaffold materially changes outcomes. The paper reports wide paper-level variation, low full-result attainment, and frequent failures in planning, implementation, debugging, and experimentation.

These are useful descriptive findings. They show that long-horizon artifact construction remains hard for the administered systems and that scaffold–model interactions matter. They do not isolate model capability: model snapshot, provider behavior, prompt, scaffold, tool interface, runtime, network, GPU, package state, early stopping, reproduction execution, and judge are bundled.

Uncertainty is reported as standard errors over paper-level averages, but only three repeated attempts per paper weakly characterize stochasticity. Papers are not a random sample from a defined population, rubric scores differ in reliability, model-judge error is omitted, and multiple model/scaffold comparisons are discussed without a paired hierarchical model or simultaneous-comparison control. The intervals describe variation in this instrument, not uncertainty about general research replication ability.

### Human comparison

The human study recruits eight strong ML researchers and seeks three independent attempts on four papers, assigning papers by participant confidence. Participants receive the same task materials, can use AI assistants, and work up to 48 hours over four weeks. One paper is dropped after the first 24 hours because the experiment ended, leaving a three-paper comparison. The headline human score is best@3, 41.4%, versus 26.6% for o1 on the same subset.

This is welcome and rarer than an unsupported “easy for experts” claim. It establishes that selected human attempts can obtain materially higher rubric scores than the compared agent configuration on three retained tasks.

It is not an exchange-rate estimate between human and AI work:

- confidence-based assignment is not random and changes the target population;
- the best of three human attempts is an order-statistic estimand, not expected single-attempt performance;
- only three retained papers support the headline comparison;
- humans work asynchronously over four weeks and may use AI, while agents receive continuous runtime and a fixed harness;
- human hours, AI-assistant usage, intervention, and artifacts are not released at attempt level;
- selection of best@3 rewards human between-attempt variation, so a fair reliability comparison would report first attempt, mean attempt, best@k curves, and matched resource frontiers for both sides; and
- both groups are judged by the same unvalidated scalar.

The paper’s own 36-hour trajectory comparison is informative about accumulation of rubric credit, not human productivity or successful replication. A later human advantage could reflect planning, debugging, background knowledge, resource use, or simply the score’s preferred path; the design does not identify the mechanism.

## Release audit and reproducibility

The official release is strong by benchmark-paper standards. Current inspection found task loaders, all 20 main-split rubrics, papers/addenda as tracked files or LFS pointers, agents, judge code, prompts, JudgeEval labels and metric code, experiment tables, tests, and a locked Python environment. Public criteria and judge code make hidden assumptions auditable.

Paper-result reproduction remains incomplete:

1. The initial release commit predates v3 and contains 19 rather than 20 v3 tasks; current `main` is post-paper and includes later fixes.
2. The paper does not pin one repository commit, container digest, package cache, system prompt hash, or provider-side model identity for every table row.
3. Git archives contain LFS pointers rather than all hydrated large payloads.
4. The complete 646 run records, submitted repositories, reproduction logs, judge leaf predictions, invalid-leaf inventory, disqualification evidence/adjudication, and human attempt artifacts are absent from the audited subtree.
5. Aggregate/per-paper CSV tables permit result inspection but not end-to-end reconstruction of table cells from raw attempts.
6. The paper’s candidate instructions allow up to seven days, while the reported agent experiment caps agent runtime at 12 hours and separately caps `reproduce.sh` at 12 hours. The public task definition and experimental treatment are therefore different resource contracts.
7. Reproduction depends on external packages, datasets, network services, mutable model endpoints, and hardware. A fresh A10 plus a script is not enough to recreate those dependencies unless images, caches, source versions, and network artifacts are pinned.
8. Public paper/rubric/addendum/task release supports science and audit but changes exposure for future systems; post-release scores need contamination and role-transition metadata.

The reproducibility status is therefore: **paper and instrument inspectability strong; deterministic rubric aggregation replayable; exact paper-time corpus identity ambiguous; judge-table reconstruction partial; full agent/human experiment replay unavailable; operational execution expensive and externally dependent.**

## Unique insight: replication requires an evidence lattice, not one progress percentage

PaperBench’s most reusable contribution emerges from where its scalar overreaches. “Replication” is not simply the sum of many correct local observations. It requires relationships among them:

`declared method → implemented mechanism → executed mechanism → produced artifact → result correspondence → robustness/provenance → licensed replication claim`

Each link needs a typed observation and dependency. A candidate can write plausible code that never ran; run code on the wrong data; reproduce a number through a shortcut; generate a visually similar result without the claimed method; or implement the method correctly but fail because of an invalid environment. These outcomes should not be fungible points.

For `skill-bench`, represent long-horizon work through a **replication evidence lattice**:

1. **obligation identity:** stable criterion ID, exact version, source/authority, public basis, importance;
2. **dependency relation:** prerequisite, conjunction, alternative, override, exclusion, or diagnostic-only;
3. **artifact witness:** authoritative file/state/output and admissible transformed view;
4. **execution lineage:** command, environment, inputs, outputs, hashes, timestamps, and causal parent;
5. **result predicate:** tolerance, uncertainty, comparison set, and legitimate equivalences;
6. **evidence state:** supported, contradicted, insufficient, invalid, or not applicable;
7. **grader state:** valid/invalid observation, evidence locators, uncertainty, and adjudication;
8. **claim gate:** minimum prerequisite set and noncompensatory failures for the named conclusion; and
9. **partial-progress vector:** retained separately for diagnosis and learning.

This preserves PaperBench’s dense diagnostic value while preventing a 21% local-credit average from being read as “21% of a paper replicated.” Report at least implementation coverage, execution coverage, result correspondence, dependency-complete pathways, invalid-observation burden, and end-to-end gate attainment. If a scalar is needed, name it as an authored progress policy and test its sensitivity to weights and dependency rules.

This extends ResearchRubrics: expert decomposition is an executable theory of attention, and PaperBench shows that making it hierarchical still does not encode prerequisites. It complements SciVisAgentBench’s evaluator-admissibility envelope by adding causal execution lineage. It also sharpens AstaBench’s portfolio lesson: macro/class aggregation must name its unit and weighting policy. AARRI provides the complementary case where non-completion can be correct; PaperBench mostly assumes progressive artifact production and should not be generalized into a universal knowledge-work shape.

## Limitations and validity threats

### Construct and content

1. Twenty feasibility-filtered ICML 2024 AI papers do not sample research replication or knowledge work broadly.
2. The benchmark favors computational work with accessible data and one-GPU execution; laboratory, qualitative, collaborative, theoretical, and field research are excluded.
3. One original author’s rubric involvement gives valuable authority but no independent completeness/reliability evidence.
4. Dense decomposition can over-specify one realization and penalize scientifically valid alternatives.
5. Public criteria may turn replication into checklist completion and expose future evaluated systems.
6. “Replication” is used for local criterion attainment without a validated minimum-success threshold.

### Measurement and judge validity

7. Recursive weighted averaging is compensatory; dependencies and mandatory gates are not executable score semantics.
8. Effective leaf influence depends on tree shape and local sibling weights, not only criterion importance.
9. Invalid judge leaves become zero and can enter a grading run still labeled successful.
10. Judge evidence is excerpted and criterion-local; file/log presence may not prove causal execution or scientific correctness.
11. JudgeEval covers five submissions and pools 2,693 leaves with severe paper-size imbalance.
12. Pooled class-macro F1 is not an equal-paper estimand despite broad “macro” wording.
13. Human labels lack duplicate independent assignment, inter-rater reliability, adjudication, and uncertainty records.
14. F1 does not validate root scores, ranking, thresholds, severe-error costs, or alternative-solution fairness.
15. Raw judge predictions are absent, preventing independent reconstruction of aggregate metrics.
16. Duplicate node IDs violate unique criterion identity and can make ID-based matching ambiguous.

### Experimental and inferential

17. Model results are configured-system outcomes, not isolated model or scaffold effects.
18. Three runs per paper weakly estimate reliability; paper and rubric clustering are under-modeled.
19. Judge error, invalid observations, selective disqualification, and task-version uncertainty are not propagated.
20. The human comparison uses confidence assignment, best@3, three retained papers, asynchronous work, and optional AI assistance.
21. Average partial score does not report complete-reproduction frequency or professional acceptance.
22. Cost estimates omit framework engineering, human supervision, infrastructure externalities, and failed-run adjudication; human and model cost boundaries differ.

### Operational realism and lifecycle

23. Candidate instructions, agent runtime, and reproduction runtime use different time contracts.
24. URL blacklist monitoring cannot establish absence of contaminated source use.
25. Mutable packages, datasets, endpoints, and network services limit exact replay.
26. Initial release, v3 task membership, later rubric/category edits, and addendum errata are separate instrument states.
27. Complete attempt-level agent, judge, disqualification, and human evidence is not released in the audited subtree.
28. A successful `reproduce.sh` is a necessary operational witness for many criteria, not proof of independent scientific replication.

## Transfer to skill-bench

Retain:

1. executable artifact submissions with one-command reproduction;
2. explicit addenda that repair paper ambiguity without exposing the rubric;
3. stable hierarchical criterion IDs and criterion-level explanations/evidence;
4. separate implementation, execution, and result observations;
5. repeated configured-system trials and time-series snapshots;
6. human attempts under documented conditions; and
7. public judge calibration sets and cost reporting.

Repair:

1. make prerequisites, alternatives, conjunctions, overrides, and noncompensatory gates executable;
2. require globally unique criterion IDs and release validators;
3. separate invalid grader/infrastructure observations from substantive zeros and fail closed for headline scores;
4. bind every criterion to authoritative artifact views and execution provenance;
5. type alternatives explicitly and calibrate judges on legitimate-divergence contrast sets;
6. report paper-macro, leaf-micro, category, severity-weighted, and decision-threshold metrics separately;
7. validate the final task decision, not only leaf agreement;
8. publish attempt-level manifests, result artifacts, judge predictions, invalids, and adjudications with immutable release identity; and
9. compare humans and agents through matched expected-attempt, best@k, time, cost, and assistance policies.

Test before adopting:

- whether dependency-gated scores predict independent expert judgments of minimally successful work better than compensatory scores;
- whether alternate valid implementations preserve scores under blind expert and judge review;
- whether judge confusion changes by paper, criterion family, weight, evidence view, and threshold proximity;
- whether rankings are robust to tree-preserving reweighting and paper-macro versus pooled-leaf aggregation; and
- whether partial-progress vectors diagnose repair needs better than one root score across multiple domains.

## Concrete repository actions

Two non-duplicate follow-ups are warranted:

1. Build a dependency-aware replay over one released PaperBench rubric and synthetic graded trees, comparing recursive compensatory score with prerequisite-gated path completion and preserving invalid/not-applicable states. The general output should extend existing rubric/metric machinery rather than create a science-only schema.
2. Build a JudgeEval decision-validity audit that reports equal-paper metrics, clustered uncertainty, high-weight/severity errors, root-score error, threshold flips, and explicit invalid policy from released or synthetic predictions.

These are validation/building tasks, not a proposal to import PaperBench wholesale. Existing rubric, artifact, execution, task-health, reliability, and validity contracts remain the canonical homes for the resulting machinery.

## Assessment

- **Evidence tier:** A — full primary paper read; official implementation and two immutable release boundaries archived; rubric and human-label aggregation replayed; complete paper-time attempts and raw judge predictions unavailable.
- **Most reusable contribution:** expert-assisted hierarchical decomposition of long-horizon artifact work into implementation, execution, and result evidence.
- **Most serious flaw:** a compensatory, partially judge-dependent progress index is named and interpreted as replication without a validated end-to-end threshold or executable dependency semantics.
- **Claim `skill-bench` may safely make:** dense expert rubrics can make partial progress on long-horizon work inspectable, but capability or completion claims require dependency-aware gates, admissible evidence lineage, explicit invalid policy, decision-level judge validation, and a versioned release ledger.

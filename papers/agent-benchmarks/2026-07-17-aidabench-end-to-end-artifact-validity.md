# AIDABench: three end-to-end outputs do not form one validated analytics-readiness scale

## Bottom line

AIDABench makes a useful construct correction: practical document analytics can end in an answer, a rendered chart, or a native spreadsheet, and evaluation should inspect the delivered object rather than only the agent's prose. Its 603 released Chinese tasks, parallel English forms, heterogeneous source files, reference images/workbooks, code-capable agents, and category-specific evaluators are unusually inspectable. The paper-time repository snapshot exists; importantly, the seven core evaluator and runner files are byte-identical to the later audited commit.

The evidence nevertheless supports a narrower claim than “end-to-end data analytics” or enterprise procurement. The three categories have different work units, evidence views, evaluator models, and score semantics: binary answer judgment; fractional image-rubric/readability judgment; and binary, sampled, model-planned spreadsheet comparison. Their macro values are called `pass@1`/`pass@3`, but visualization is explicitly a soft score and the suite has no released complete-attempt/result matrix or table-reproduction policy that makes this one pass probability. The file judge observes values and structure through sampled Python inspection but not formulas, provenance, rendered layout, recalculation behavior, hidden state, or collateral damage. The QA judge can recompute from source files, making some tasks executable despite absent static answers, but also making the score a configured-agent result rather than deterministic answer equivalence. The chart judge sees a rendered PNG but not its generating data/code or accessibility/export behavior.

The most important release finding is a **criterion-to-evidence closure failure in an otherwise nearly complete package**: Chinese file-generation task `FG_82` names `DEA分析数据-1128_processed_res.csv`, while the pinned release contains `DEA分析数据-1128_processed.csv`. The standard runner constructs the former path and cannot evaluate the task without manual repair. More broadly, the runner loads whatever prediction records exist and has no suite-membership closure check; inference cleanup deletes recognized failed records so a partial run can acquire a smaller denominator unless an external operator proves all 603 attempts are present.

The June 2026 release also adds 47 Skills, Hermes/Docker agents, and ConsensusEval/open-ended evaluation. Those are useful later engineering, but they were absent from the 27 March paper-time snapshot, absent from the 603-task dataset, and absent from the paper results. They must not be used retrospectively to explain the reported leaderboard or claimed evaluator calibration.

AIDABench is therefore strong evidence for a public, heterogeneous **configured document-analysis package** and for the need to route each deliverable to a different observer. It is partial evidence for artifact correctness under those observers. It does not establish analytical quality in general, professional validity, model-only capability, procurement utility, or deployment readiness.

## Source and reading record

### Complete primary paper read

- Yibo Yang et al., *AIDABench: AI Data Analytics Benchmark*.
- Immutable record: <https://arxiv.org/abs/2603.15636v2>; PDF: <https://arxiv.org/pdf/2603.15636v2>.
- Version read: immutable v2, updated 27 March 2026 (the rendered manuscript footer says 30 March).
- Local PDF: `data/papers/pdfs/2603.15636v2-aidabench-ai-data-analytics-benchmark.pdf` (22 pages; SHA-256 `48c0062bee4bfe8a8bdd12f9e6e9b6eb7483738dee8324d07bf4c8b4424254b5`).
- Local full text: `data/papers/text/2603.15636v2-aidabench-ai-data-analytics-benchmark.txt` (SHA-256 `936aced11389a464a3c450b5bab025d5da87249a5be0e5dd9b2483e0389c3589`).
- Date read: 17 July 2026. The complete paper was read through construction, protocol, all three evaluators, results, error analysis, prompts, model configurations, task distributions, token/round tables, and qualitative examples.

### Official release and data audited

- Official repository: <https://github.com/MichaelYang-lyx/AIDABench>.
- Paper-time snapshot: commit [`080fdb0537b89adb65acba3090a7a26882e8990a`](https://github.com/MichaelYang-lyx/AIDABench/commit/080fdb0537b89adb65acba3090a7a26882e8990a), 27 March 2026 07:59 UTC; local archive `data/sources/releases/2603.15636v2-aidabench/MichaelYang-lyx-AIDABench-paper-time-080fdb0.zip` (SHA-256 `8c4a04a81ffd5bf80591d962d258f04523e4713d665a09d845f0f2055cf383e0`; 47 files).
- Requested later snapshot: commit [`1e306824a80dfc7d1dfb3eb448a6cbbe20cb209e`](https://github.com/MichaelYang-lyx/AIDABench/commit/1e306824a80dfc7d1dfb3eb448a6cbbe20cb209e), 24 June 2026; local archive `data/sources/releases/2603.15636v2-aidabench/MichaelYang-lyx-AIDABench-1e30682.zip` (SHA-256 `35fe85133bb5330b453eeb1b01c8d6c5444569754e7ae009ffe95a457dfd767e`; 118 files).
- Official dataset: <https://huggingface.co/datasets/MichaelYang-lyx/AIDA>, pinned revision `5ab9dc72c99a1702e3388697d8b09522e1ac7339`, last modified 16 June 2026. Its API reports 984,007,081 stored bytes and lists 2,816 files. The dataset card and all six bilingual manifests are preserved under `data/sources/releases/2603.15636v2-aidabench/huggingface/`; the complete binary payload is represented by the pinned tree but was not duplicated locally.
- Machine-readable provenance and findings: `data/sources/releases/2603.15636v2-aidabench/provenance.json` and `release-audit.json`.

Both ZIPs passed CRC checks. The later Python tree passed `compileall`. No paid model call or untrusted task workload was executed. Static compilation and manifest closure are not semantic evaluator validation.

The GitHub archive has no `LICENSE`, `COPYING`, or `NOTICE`; its README shows an Apache-2.0 badge whose target is absent. The Hugging Face card separately declares Apache-2.0. Dataset reuse rights and repository-code rights should therefore not be collapsed into one license claim.

## One-sentence contribution

AIDABench releases a broad bilingual package for answer, chart, and spreadsheet production over heterogeneous workplace-like documents with task-specific model evaluators, but its source/task authority, lossy and uncalibrated observer views, attempt closure, mixed score semantics, paper/release drift, and absent result artifacts bound claims to configured-package scores rather than general analytics competence, professional validity, procurement utility, or readiness.

## Why this matters for skill-bench

This review advances charter objectives A, B, and C through expansion, consolidation, and validation. AIDABench is not a reason to narrow `skill-bench` to spreadsheet work. It is a particularly useful cross-domain case because one suite asks agents to produce three classes of deliverable that demand different evidence:

- answers require source-grounded numerical/semantic verification;
- charts require data correctness, encoding correctness, rendering, readability, and export checks;
- editable files require native structure, current values, formulas/dependencies, rendered views, counterfactual behavior, and preservation evidence.

The uncertainty clarified is whether “one end-to-end suite” can promote these unlike measurements into a common professional capability claim. It cannot without an explicit portfolio estimand, observer validation, denominator closure, and downstream-use warrant.

The concrete evidence is stronger than a paper-only review: immutable paper and paper-time code, a later pinned source snapshot, a pinned 2,816-file dataset tree, all six manifests, evaluator implementations, and a static cross-file/path audit. Useful completion is a bounded account of what each observer can establish, where the package is closed or broken, and how existing artifact-admissibility, task-health, configured-system, metric, and validity machinery should absorb the lesson without an AIDABench-specific subsystem.

## Research question and claim boundary

The paper asks whether contemporary tool-using language models can handle realistic end-to-end document analytics spanning QA, data visualization, and file generation, and proposes specialized evaluators for each output type (Sections 1 and 3, pp. 1–6).

The evidence supports these bounded claims:

1. A public revision contains 603 unique Chinese task IDs—226 QA, 116 visualization, and 261 file-generation—plus 603 English rows with the same ID order.
2. The release exposes substantial heterogeneous input/reference material: 2,097 `.xlsx`, 190 `.csv`, 128 `.xls`, 100 `.docx`, 22 `.pdf`, 261 `.png`, and smaller format groups in the pinned tree.
3. Under the paper's configured model–prompt–tool–summary–endpoint packages, reported scores differ substantially. Claude Sonnet 4.5 leads the reported table at 59.43 `pass@1` and 70.78 `pass@3`; file generation is the weakest category (Table 1, p. 7).
4. Repeated attempts help materially under a best-of-three policy, especially for file generation; this is evidence about retry-assisted configured-system performance, not first-attempt reliability.
5. A summary generated from input files changes results for many systems, especially smaller ones, under the authors' three-run comparison (Table 2, p. 7).
6. The three delivered-object families require different evidence views and failure taxonomies.

The evidence does **not** establish that the 603 tasks represent enterprise analytics demand; that difficulty labels are calibrated; that 1–2 hours is human solution time; that evaluator scores are accurate at reported rates over a disclosed sample; that the three score families form one pass probability; that model rankings transport across scaffolds, providers, summaries, tool environments, fonts, or retries; that a score maps to an acceptable professional artifact; or that the suite is a sufficient procurement, tool-selection, economic-value, safety, or readiness instrument.

## Methodology

### Task sourcing, transformation, and expert authority

The authors say a team of “domain users” contributed authentic scenarios from daily work in finance, sales, HR, and project management; data were anonymized and business-sensitive fields desensitized (Section 3.1.1, pp. 3–4). Each ground truth was independently labeled and cross-reviewed by at least two additional experts, with annotation and validation “typically requiring 1–2 hours per task.”

This is useful demand-provenance testimony, but the paper supplies no sampling frame or transformation ledger: number and organizations of contributors, roles and qualifications, source-population size, invitation/rejection criteria, per-domain counts, observed-work trace, original request versus rewritten prompt, artifact ownership, consent, compensation, privacy review protocol, exclusions, disagreement rates, adjudication, or task-level approvers. “Finance, sales, HR, and project management” is illustrative coverage, not a population definition.

The abstract converts annotation/validation effort into a stronger statement: “even human experts require 1–2 hours per question when assisted by AI tools” (p. 1). Section 3 says the same duration covers ground-truth annotation and cross-validation, not timed task solving by sampled experts. These are different estimands. The paper reports no timed human condition, participant count, distribution, tool package, first attempt, produced artifact, or score. The valid claim is **reported authoring/validation effort per task**, not human difficulty, human baseline, or expert time-to-solution.

The paper labels difficulty by the number of “expert-level reasoning steps”: easy ≤6, medium 7–12, hard ≥13 (Section 3.1.2, p. 4). It does not release step decompositions in the inspected manifests, authorship, counting rules, multiple-rater agreement, or outcome-independent calibration. Step count can be useful stratification metadata but is not an interval difficulty scale. It also mixes operations of radically different cost: one “read PDF” step and one spreadsheet cell operation are not equivalent.

### Released task and artifact units

The released manifests reconstruct the advertised total exactly:

| Family | Chinese rows | Share | Primary input/output unit | Paper score |
|---|---:|---:|---|---|
| QA | 226 | 37.5% | one instruction + one/more files → response | binary model judgment |
| Data visualization | 116 | 19.2% | instruction + files or embedded data → image | 0.7 rubric correctness + 0.3 readability |
| File generation | 261 | 43.3% | instruction + source files → generated spreadsheet/file | binary model-agent judgment against reference |
| **Total** | **603** | **100%** | unlike units | mixed macro score |

IDs are globally unique. The parallel English manifests preserve the same IDs and order but are instrument transformations, not independent tasks. Translation changes filenames, document content, labels, fonts, and sometimes reference inventory; it needs its own equivalence evidence before scores are compared as language effects.

A delimiter-aware manifest audit finds 159/603 (26.37%) rows naming more than one input, with a maximum of 14. The paper reports 27.4%, including 16.6% exactly two and 10.8% three or more (p. 4). The discrepancy may reflect a different counting rule or release drift; no paper-time task manifest or cross-file flag is preserved to resolve it. This is precisely why derived statistics need immutable membership and transformation records.

All listed input paths resolve in the pinned Hugging Face tree after handling newline, semicolon, and carriage-return delimiters. All chart output names have released reference images. One file reference does not resolve: `FG_82` names `DEA分析数据-1128_processed_res.csv`, but the Chinese reference directory contains `DEA分析数据-1128_processed.csv`. The English counterpart has an `_res.csv` plus an extra workbook. Because `eval_file_generation.py` constructs `reference/{id}/{reference_file}`, the Chinese task fails closed as an exception/zero unless an operator silently renames or rewrites it.

Other manifest edge cases are not automatically defects but matter to observer dependence:

- `DV_84` has no input file because the four percentages are embedded in the prompt.
- `DV_90` has no correctness rubric, so the correctness judge lacks explicit task-specific key points while readability remains judgeable.
- Five QA rows have null `reference`; `QA_154` has a legitimate numeric zero. `QA_43` and `QA_168` retain rubrics, while `QA_18`, `QA_23`, and `QA_50` have neither static reference nor rubric.
- The numerical evaluator can inspect original source files and derive an answer, so null reference does not make these rows necessarily unscorable. It changes the construct from reference comparison to a second agent's independent analysis.
- There are two duplicate-question groups: `QA_28`/`QA_29` and `FG_257`–`FG_260`. Duplicated wording can still correspond to different files, but task-family dependence and effective sample size should be reported.

### Configured inference treatment

The paper's agent receives instruction and files, uses one `execute_code` tool for up to 20 rounds, and is asked to plan, execute, verify, and deliver (Section 3.2, pp. 4–5; Appendix A). The main table varies 11 model endpoints while claiming a unified protocol. Per-model decoding settings differ by provider recommendation or provider default (Appendix E). The main condition also supplies an auxiliary spreadsheet summary, so each row is a configured package:

`model endpoint/date + provider decoding semantics + common prompt + source files + generated summary + 20-round scaffold + Python libraries + execution realization + evaluator endpoints + retry/selection policy`.

The labels in Table 1 name models, not this full package. They should be read as shorthand configured-system labels. Endpoint drift is especially material for preview and dated products.

The paper calls every code invocation “stateless” and “containerized” and says this ensures “strict execution isolation and full reproducibility” (p. 5). The paper-time release does not contain a container definition. Its subprocess agent calls a `CodeExecutionToolkit(sandbox="subprocess")`; the toolkit invokes host Python subprocesses, and its Jupyter alternative keeps in-process state. The runner rewrites `/mnt/data` and `/mnt/result` into host paths. Independent subprocess calls may be stateless at Python-variable level, but they share host filesystem outputs and are not container isolation. The later release adds Docker-backed Hermes paths, but that is post-paper engineering and not the paper treatment.

The code also retries each model API request up to ten times with five-second sleeps (`agents/openai_subprocess_agent.py`, lines 55–83). This service retry is absent from the paper's attempt definition. It can turn transient failures into one nominal run. Conversely, recognized failed prediction files are deleted before inference/evaluation (`infer/run.py`, lines 22–141). The package does not preserve a complete started→failed→retried→selected ledger.

### QA evaluator: executable second opinion, not deterministic equality

The paper describes a binary judge using question, reference, and optional key points, with strict quantitative agreement and core-claim coverage (Section 3.3.1, p. 5). It calls the workflow “deterministic,” but the released evaluator is a code-capable generative model. The runner passes source-file paths; the prompt tells the evaluator to inspect data, run code, and return `is_correct`. This is more capable than a text-only comparator and explains how null-reference rows can still be scored.

It also creates a different validity problem. Correctness depends on the evaluator's own file parsing, code, statistical choices, and endpoint behavior. A model can agree with a wrong reference or disagree for a valid alternative method. The release contains no deterministic answer schema, tolerance policy by item, source-to-answer derivation, evaluator trace corpus, planted error suite, human-label sample, confusion matrix, or abstention state. Exceptions and parse failures become false/zero. “No” merges substantive wrongness, evaluator failure, ambiguous requirement, unsupported method, and output-format failure.

### Visualization evaluator: rendered evidence is necessary but incomplete

Visualization is the strongest match between predicate and view. Both judges receive the generated image. Correctness is checked against task-specific rubric text; readability uses general dimensions. The runner normalizes passed/total and computes `0.7 × correctness + 0.3 × visual` (`eval_data_visualization.py`, lines 100–121). This directly observes visible labels, marks, and presentation rather than inferring them from code.

But a PNG cannot establish the underlying source calculation, data-to-mark binding, omitted records, chart-generation provenance, accessibility text, editable chart structure, export consistency, or behavior under a changed filter. Rubrics can themselves contain factual claims rather than visual predicates—for example “girls exceed boys by 977”—and a judge reading pixels may accept a convincing but fabricated label. Conversely, non-verifiable items are scored zero rather than `insufficient_evidence` (Section 3.3.2, p. 5), conflating artifact failure with observer limitation.

The evaluator calls the same configured multimodal endpoint separately for correctness and readability, so their errors are correlated. The 70/30 weights are design policy, not a stakeholder utility or professional threshold. `DV_90`'s null rubric exposes missing-criterion handling; parse fallbacks default to fixed totals in places, but no conformance test covers null, malformed, or adversarial rubric outputs.

### Spreadsheet evaluator: sampled current-state judgment, not native-artifact integrity

The paper describes three stages: structural indexing; full/sampled content comparison with tolerance and alignment; and question-specific checks for filtering, sorting, grouping, derived columns, and edge cases, within 20 tool calls (Section 3.3.3, pp. 5–6). The released `FileEvaluatorAgent` operationalizes this as a Claude agent with Python execution and a binary final JSON verdict. The runner gives it the instruction, candidate path, and reference path.

This is meaningfully stronger than file existence or one-cell exact match. It can inspect sheets, dimensions, headers, data types, sampled values, and selected task constraints while allowing some benign row/column variation.

However, the observer is sampled and self-directed. The release does not deterministically enforce the paper's exact 1–5/5–10/1–5 stage budget, disclose sampled positions as a precommitted artifact, or guarantee coverage of every required region. A false-pass candidate can hide an error outside sampled cells; a false-fail can result from one reference-specific structure. The judge has no formal obligation inventory and no proof that all instruction clauses were considered.

Most importantly, `openpyxl`/pandas current-value inspection is not native spreadsheet integrity. It does not systematically validate formulas versus hardcoded values, calculation chains, named ranges, external links, charts, images, conditional formatting, print layout, macros, workbook corruption, recalculation under a pinned engine, or response to authoritative input mutations. A candidate that copies reference display values can pass while being unusable for later edits. A reference workbook is one witness, not a complete specification; no legitimate-alternative suite or reference health certification is released.

The paper says “if no critical violation is detected” the artifact passes. This is absence of detected failure under a bounded search, not proof of correctness. The implementation appropriately fails on parser/exception paths, but it has no `insufficient_evidence` or evaluator-invalid outcome. `FG_82` demonstrates the consequence: package/reference failure becomes candidate failure.

### Evaluator calibration claim

Section 3.3.4 (p. 6) says QA and spreadsheet judges exceed 95% agreement with human judges and visualization exceeds 90%. No sample size, task/system composition, candidate-error prevalence, number and independence of experts, qualification, assignment, blinding, evidence access, label unit, repeated judge runs, confidence interval, inter-human agreement, disagreement adjudication, per-class sensitivity/specificity, or released labels appear in the paper or audited release.

Raw percent agreement is especially weak for a pass/fail evaluator when prevalence is unknown. If most sampled artifacts clearly fail, high agreement can coexist with poor false-pass detection. Chart correctness/readability and spreadsheet task-level verdicts also have different units. The three headline percentages therefore support only the authors' report of an undisclosed calibration exercise; they do not validate evaluator replacement of experts or the leaderboard's task-level decisions.

### Attempts, invalids, denominators, and aggregation

The main result reports both `pass@1` and best-of-three `pass@3`; visualization best-of-three takes the maximum soft score per task (Section 4.1, p. 6). Ablations instead report mean over three runs. These are different estimands:

- `pass@1`: one configured attempt score;
- `best@3`: retry-assisted maximum quality over three attempts;
- `avg@3`: expected score over three sampled attempts under the observed endpoint.

Calling all of them “pass” hides the distinction. QA and file generation are binary per task; visualization is continuous. Overall aggregation therefore mixes a binary hit rate with a graded image score. A 59.43 overall score is not the observed fraction of all 603 tasks that produced professionally acceptable deliverables.

The released runners calculate category means over loaded prediction records. They do not load the authoritative task manifest and assert exact ID-set equality. The cleanup function can delete recognized API-failure or empty-response records before evaluation. If regeneration is incomplete, missing task IDs disappear from `len(data)` rather than receiving a typed invalid outcome. No script in the paper-time release assembles Table 1, checks 603-member closure, selects attempt maxima, weights category means, or emits uncertainty.

The paper does not report started, completed, valid-artifact, evaluator-valid, substantive-fail, infrastructure-fail, safety-refusal, and selected denominators. It gives no first-call versus eventual-call completion, task-level attempt correlation, selection optimism interval, or model/provider outage record. Best-of-three is a legitimate product policy only if its latency, cost, and retry availability are explicit; it is not first-attempt reliability.

### Statistical evidence, error analysis, and cost

Table 1 reports point estimates for 11 configured systems with no confidence intervals, paired differences, rank probabilities, or repeated-attempt variance. Six hundred three tasks are not 603 independent draws from enterprise work: tasks cluster by contributor, source workbook, domain, operation, duplicate wording, and translation family. Evaluator error and provider drift are also omitted from uncertainty.

The summary ablation compares with/without generated spreadsheet summaries over three runs and reports the direction for 11 systems (Table 2, p. 7). It is a useful matched configuration contrast in intent, but no per-task paired interval, order/seed schedule, multiple-comparison treatment, summary-generation identity, summary correctness audit, or interaction with file type is reported. “8 of 11 decline” is descriptive, not a general causal estimate of summarization benefit.

Error analysis selects three systems and reports category shares among bad cases (Section 4.4, pp. 7–8). The paper does not provide coding rules, rater identity, trace evidence, multi-label policy, agreement, adjudication, denominators, or counterfactual repairs. Categories such as semantic misunderstanding, calculation error, garbled text, and round-limit convergence can overlap. The shares are hypotheses for future probes, not validated root causes.

Token and round averages are useful operational signals (Appendix H), but monetary cost, evaluator cost, summary-generation cost, retry calls, wall time, code-execution CPU/memory, human authoring cost, and maintenance burden are absent. The abstract nevertheless names enterprise procurement and tool selection. Procurement requires total cost, completion reliability, latency distribution, data governance, isolation, supportability, safety, stakeholder loss, and fit to local task prevalence—not only benchmark score and mean tokens.

## Evidence and results interpretation

The strongest substantive result is not that a particular model “can do 59.43% of analytics.” It is that under one public task package and one configured scaffold, failures remain frequent and category-dependent, while a retry budget and input summary materially affect observed score. File-producing tasks are consistently harder under these observers; chart scores are helped by partial credit and a different judge/view, so cross-category level comparisons are not pure difficulty comparisons.

The top two overall `pass@1` values—59.43 and 57.39—are not accompanied by paired uncertainty. Even if the order is stable on these 603 tasks, the model endpoints, provider defaults, task families, and judge models define the treatment. “Model capacity correlates with performance” (p. 7) is observational over 11 heterogeneous endpoint/scaffold interactions, with sparse and inconsistent parameter-size metadata. It does not isolate capacity.

The release substantially improves inspectability relative to paper-only suites. A paper-time archive verifies that the three core evaluator paths existed by v2, and their relevant files are unchanged at the later audited commit. Yet exact result reproducibility is weak: no immutable model responses, generated files, charts, evaluator traces, score matrix, attempt ledger, model endpoint hashes, summary artifacts, seeds, or table builder are released. Re-running mutable commercial endpoints would produce a new experiment, not reproduce March 2026 outputs.

## Unique insight

AIDABench exposes a distinction between **output-family routing** and **claim-family closure**.

Routing an answer, image, and spreadsheet to specialized observers is necessary. It is not enough. For each output family, a defensible chain is:

`authorized requirement → source/data identity → configured attempt → delivered-object identity → admissible evidence views → criterion-level observation → evaluator-valid outcome → task decision → family estimand → portfolio policy → downstream claim`.

AIDABench implements pieces of the middle but leaves different gaps in each family:

- QA has source access and a semantic/code judge, but weak answer derivation, applicability, and evaluator calibration.
- Visualization has the rendered view, but not data binding, native chart state, or source-to-mark provenance.
- File generation has source/reference files and sampled structural/content inspection, but not complete obligation coverage, formula/dependency integrity, rendering, counterfactual behavior, or reference certification.

The overall score then combines these incomplete chains without a validated common decision meaning. This suggests that **“end-to-end” should be asserted per requirement-to-consequence chain, not by counting multiple output modalities**.

A second insight is that package closure is itself an empirical validity layer. `FG_82` is not merely a typo: it proves that task text, manifest reference, released bytes, runner path construction, and score denominator can disagree. Before measuring an agent, a benchmark needs a versioned closure proof over:

`declared task IDs ↔ input bytes ↔ reference/rubric bytes ↔ evaluator route ↔ produced attempt ↔ evaluator result ↔ aggregate membership`.

A third insight is that later release richness can create retrospective validity laundering. The June repository's Skills, Hermes isolation, and ConsensusEval look more sophisticated than the March package. But unless exact result lineage says those components produced a score, they are future options—not evidence for past leaderboards.

## ConsensusEval and Skills: useful post-paper additions, not paper evidence

The requested current commit adds 47 `SKILL.md` files, a skill loader/agent, Hermes local and Docker agents, and an open-ended ConsensusEval pipeline. Static comparison finds 71 added files and 13 changed shared files relative to the paper-time snapshot; no files were removed. None of these additions appears in the 603-task paper method or results.

ConsensusEval's tutorial and code define:

1. several reference agents independently analyze the same dataset;
2. a configured LLM semantically clusters findings and applies a consensus threshold (template: 0.6);
3. non-consensus findings are sent back to other reference sessions for 0–5 cross-validation and retained at mean ≥3;
4. another LLM generates a 50-point Must-Find, 30-point Process Quality, and 20-point Bonus rubric; and
5. a Hermes judge inspects the candidate response/workspace and assigns one or more 0–100 scores.

This is an interesting attempt to create task-specific analytical rubrics where no static answer exists. It does not validate itself. Criterion authority comes from model outputs and another model's semantic clustering; model consensus can reproduce shared errors. Non-consensus cross-validation is not independent because validators are the same reference panel with resumed sessions. The consensus threshold, cross-validation threshold, 50/30/20 allocation, and final score have no expert or decision calibration in the release. The template config and tutorial also drift: one specifies five judge runs and one model set; the tutorial example specifies one run and different reference models. Mutable preview endpoints and shared caches further define instrument identity.

No open-ended task set, frozen reference cache, generated rubric population, human study, result table, cost ledger, or scorer conformance suite is in the pinned dataset/release. The correct status is **post-paper experimental evaluator machinery**, not a fourth validated AIDABench category.

The Skills are similarly unvalidated as an intervention. The paper table contains no paired skill/no-skill condition. The later `skill_jupyter_agent` can load Excel and image capabilities, but no exact Skill bundle, selection trace, invocation proof, or controlled effect is attached to paper scores. `skill-bench` should treat Skill identity as part of a configured system and require a paired intervention before claiming skill efficacy.

## Comparison with adjacent reviewed benchmarks

### OfficeEval

[OfficeEval](2026-07-12-officeeval-standardized-exam-validity.md) has stronger external requirement and weight lineage: NCRE practical tasks and deterministic native OOXML/COM property checks predate the benchmark. AIDABench has broader workplace-like source files and more open-ended analytical operations, but weaker criterion authority and much more model-dependent grading. OfficeEval's unavailable copyrighted instrument blocks audit; AIDABench's public task bytes are a major advantage. Both need plural views: native properties do not establish rendered/counterfactual quality, while AIDABench's PNG and sampled workbook views do not establish native editability.

### MBABench

[MBABench](2026-07-11-mbabench-spreadsheet-artifact-validity.md) explicitly inspects formulas, selected styles, and professional finance-workbook structure, whereas AIDABench mostly targets data wrangling outputs and sampled values. AIDABench is broader across QA/charts/files and has more publicly inspectable task inputs. Both compare against one reference and under-test counterfactual recalculation, render state, alternative-valid structures, and downstream handoff. MBABench's static serialization can miss behavior; AIDABench's agentic sampling can miss unsampled defects.

### AstaBench

[AstaBench](2026-07-14-astabench-scientific-suite-aggregation-validity.md) makes its heterogeneous component metrics and portfolio weights explicit and reports score beside model cost, even though its scalar still lacks a common construct. AIDABench is a smaller three-family portfolio but calls the aggregate `pass@k`, obscuring mixed binary/continuous semantics and no declared overall weighting/reproduction script. AstaBench's solve→score separation and typed tool labels are stronger operational patterns; AIDABench's public document artifacts provide a useful office/data complement.

### FinResearchBench II

[FinResearchBench II](2026-07-16-finresearchbench-ii-consensus-rubric-validity.md) is the closest warning for the later ConsensusEval path. Both use model-generated or model-derived criteria and panel agreement to scale open-ended grading. FinResearchBench II at least reports candidate attrition and human/LLM agreement matrices; AIDABench's post-paper ConsensusEval has no released empirical study. Neither model consensus nor discrimination supplies criterion authority. Expert warrant, evidence-view admissibility, repeated reliability, and downstream decision validity remain separate gates.

### ArtifactCopilot

[ArtifactCopilot](2026-07-15-artifactcopilot-evaluation-workflow-validity.md) distinguishes workflow execution, artifact checks, criterion linkage, and evaluator configuration but shows how a structured evaluation graph can remain semantically incomplete. AIDABench is less graph-heavy and more data-rich; `FG_82` demonstrates the same closure issue at a smaller scale. Both motivate executable release conformance before capability scoring and separate artifact-view validity from orchestration success.

## Claim ceilings

| Claim level | Maximum warranted status from this audit |
|---|---|
| Released-package conformance | **Partial.** 603 unique bilingual IDs and nearly all input/reference paths are inspectable; `FG_82` is broken and exact paper-time dataset bytes/results are not preserved. |
| Artifact correctness | **Partial/configured-observer only.** The observers inspect useful but incomplete views and lack released calibration evidence. |
| Analytical quality | **Not established generally.** Task-local answer/chart/file scores omit method soundness, source authority, uncertainty, and handoff utility. |
| Professional validity | **Not established.** No independently sampled work population, professional acceptance threshold, edit/reuse trial, or downstream decision study. |
| Configured-system capability | **Descriptive only.** Results apply to the full March model–endpoint–prompt–summary–tool–retry–judge packages. |
| Procurement utility | **Not established.** Reliability, latency, total cost, governance, safety, stakeholder loss, and local demand weighting are absent. |
| Readiness | **Not established.** No operational deployment, monitoring, failure containment, or consequence evidence. |

## Transferable design patterns

### Retain

1. **Route deliverable families to distinct observers.** Answer, render, and native file are not interchangeable evidence.
2. **Release real task bytes and references.** Public inspectability enables path, duplicate, and observer audits impossible in paper-only suites.
3. **Allow code-based source verification for analytical answers.** A second executable derivation can catch presentation differences that exact string checks miss, provided it is validated and traced.
4. **Separate first-attempt, best-of-k, and mean-over-k reports.** The paper at least distinguishes best@3 for main results and avg@3 for ablations.
5. **Track rounds and tokens by output family.** Resource vectors are necessary even though they are not sufficient for cost.
6. **Preserve paper-time and later release snapshots.** This audit could separate core evaluators from later Skills/ConsensusEval rather than treating `main` as timeless.

### Repair

1. **Make suite closure executable.** Assert exact task-ID equality across manifest, inputs, references/rubrics, attempts, evaluator outputs, and aggregate. Missing or duplicate IDs must be typed invalids, never silent denominator changes.
2. **Type outcome states.** Separate substantive fail, invalid artifact, evaluator parse failure, unavailable reference, infrastructure failure, safety refusal, timeout, and insufficient evidence.
3. **Predeclare criterion-to-view admissibility.** Source-value predicates need frozen inputs and derivations; visual predicates need renders; formula/editability predicates need native/recalculated/counterfactual views.
4. **Replace sampled-agent confidence with coverage evidence.** Freeze required obligations, sampled positions, deterministic checks, and an explicit residual uncertainty/abstention state.
5. **Validate references and alternatives.** Certify reference health and plant legitimate structurally different solutions, hidden unsampled defects, hardcoded values, stale charts, corrupt workbooks, and invalid source bindings.
6. **Validate evaluators on released, clustered cases.** Report human assignment/agreement, per-class confusion, false-pass loss, task/system families, repeated endpoint runs, abstention, and held-out perturbations.
7. **Name portfolio estimands.** Report the QA hit rate, visualization quality score, and file acceptance rate as a vector. Any scalar needs declared weights, gates, missingness, uncertainty, and stakeholder interpretation; do not call it one pass rate by default.
8. **Bind configured-system identity.** Pin model endpoint/date, provider, decoding, prompt hash, Skill set, summary generator/output hash, execution image/runtime, network/filesystem policy, retries, and evaluator models.
9. **Keep post-paper components prospective.** New Skills or ConsensusEval can earn evidence through paired trials and human/perturbation validation; repository presence does not upgrade old scores.
10. **Require procurement evidence separately.** Add first-attempt/eventual completion, latency, total cost, data handling, security/isolation, maintenance, local workload weighting, stakeholder loss, and acceptance/use studies.

## Limitations and validity threats

### Task/content validity

1. No defined source population or probability sampling of enterprise analytics work.
2. Contributor count, organizations, qualifications, roles, invitation, rejection, and per-domain composition are absent.
3. Original workflow request → anonymized data → rewritten task → reference transformation is not released.
4. Privacy/desensitization is asserted without task-level procedure, governance, or utility-loss audit.
5. The 1–2-hour claim concerns annotation/validation in the method but is promoted to assisted human solution time in the abstract.
6. Difficulty is uncalibrated authored step count with no released decomposition or rater agreement.
7. Bilingual forms are transformations, not independent tasks; equivalence is unvalidated.
8. Duplicate-question groups and shared source lineages reduce effective independence.
9. The released cross-file rate (26.37% by manifest delimiters) does not reproduce the paper's 27.4%.
10. Public inputs/references raise future contamination and answer-recovery risk.

### Treatment and operational validity

11. Table rows bundle model, endpoint, provider defaults, prompt, summary, scaffold, runtime, and judges.
12. Provider-recommended/default decoding is not one controlled decoding treatment.
13. Preview/mutable endpoints prevent exact time transport.
14. The paper's container/stateless claim conflicts with the paper-time host subprocess/Jupyter implementations.
15. Host filesystem and environment exposure are not specified or canaried.
16. Up to ten API retries occur inside one nominal attempt without a reported retry ledger.
17. Recognized failures can be deleted before scoring, erasing started-attempt evidence.
18. No first-attempt versus eventual-call reliability or wall-time distribution.
19. Auxiliary summaries are an additional model/tool artifact whose identity and correctness are not preserved.
20. Skills and Hermes/Docker paths are post-paper additions and cannot explain March scores.

### Measurement validity

21. QA uses a generative executable second opinion, not deterministic equality.
22. QA null-reference rows increase dependence on evaluator reasoning and unspecified method choices.
23. No applicability, ambiguity, insufficient-evidence, or evaluator-invalid state.
24. Chart images cannot prove source-to-mark binding, code correctness, editability, or accessibility.
25. Correctness/readability judges share an endpoint and likely correlated errors.
26. Visual 70/30 weighting is unvalidated policy.
27. `DV_90` has no correctness rubric.
28. File evaluation is model-directed and sampled, with no deterministic obligation-coverage proof.
29. Spreadsheet formulas, dependencies, recalculation, charts, styles, macros, and collateral state are incompletely observed.
30. No counterfactual mutation or pinned calculation-engine test.
31. One reference can penalize legitimate alternatives or reproduce reference defects.
32. `FG_82` has an unresolved Chinese reference path and is not package-evaluable as declared.
33. Evaluator exceptions/parse failures become candidate failures, conflating observer and solver error.
34. Reported >95%/>90% human agreement lacks every denominator and design detail needed for interpretation.
35. No released calibration labels, confusion matrices, human agreement, intervals, or false-pass analysis.

### Aggregation and inference validity

36. Binary QA/file outcomes and fractional chart scores do not share one pass semantics.
37. `pass@3` is best-of-three selection, not reliability over three independent required successes.
38. Best-of-three and avg@3 answer different questions but are easy to compare casually.
39. Runner denominators are loaded prediction records, not authoritative manifest membership.
40. No released table-assembly script, complete task×attempt matrix, or selected-attempt ledger.
41. No task-clustered uncertainty, paired model differences, rank probabilities, or judge-error propagation.
42. Task-family, contributor, source-file, and duplicate dependence is ignored.
43. The summary ablation has only three runs and no paired uncertainty or summary-correctness audit.
44. Error categories lack a codebook, independent raters, agreement, adjudication, or repair intervention.
45. Parameter-size/performance claims are observational over heterogeneous configured packages.
46. No professional acceptance gate; weighted score compensation can hide mandatory failure.

### Reproducibility, cost, and consequence validity

47. Exact model outputs, generated artifacts, summaries, evaluator traces, and scores are not released.
48. Paper-time evaluator code is recoverable, but paper-time dataset and endpoint responses are not immutably bound to results.
49. Re-running commercial/preview endpoints would be a new experiment.
50. Monetary cost, evaluator cost, retry cost, CPU/memory, wall time, and human labor distribution are absent.
51. Repository code licensing is unresolved despite the README badge; dataset card licensing is separate.
52. No independent team reproduces a paper table from released bytes.
53. No stakeholder accepts, edits, reuses, or makes a decision from evaluated artifacts.
54. No evidence links score to productivity, error cost, safety, governance, procurement utility, or readiness.
55. The post-paper ConsensusEval has no frozen tasks/caches/rubrics/results, expert authority study, or cost evidence.

## Reproducibility and operational realism

**Paper inspectability: strong.** The immutable 22-page paper gives task counts, output shares, prompts, model configurations, category results, token/round statistics, and qualitative cases.

**Package inspectability: strong with one concrete closure defect.** The official paper-time and later archives are immutable; core evaluator files match; the current dataset metadata and all task manifests are pinned. The full public dataset tree is unusually rich and nearly path-complete. `FG_82` proves the need for automated closure rather than lowering the overall value of the release.

**Exact result reproducibility: weak.** There are no paper responses, artifacts, judge outputs, result matrix, retry ledger, summary artifacts, table builder, or immutable endpoint identities. The paper-time runtime is also not the claimed containerized environment.

**Operational realism: moderate and bounded.** Realistic files, multilingual content, cross-file tasks, code execution, generated images/workbooks, 20-round interaction, and malformed-font/semantic failures expose genuine data-work problems. But tasks are individually bounded, references are known to evaluators, tool access is simplified, no stakeholder clarification or changing requirement occurs, and editable artifacts are not exercised after handoff. The suite resembles a broad take-home analytics test more than an observed enterprise workflow lifecycle.

## Concrete changes for skill-bench

1. **Do not create an AIDABench-specific schema.** Route these findings into existing benchmark-bundle, task-health, artifact-admissibility, configured-system, metric, validity, and provenance records.
2. **Add one cross-domain package-closure fixture when the existing release-conformance work is next extended.** Plant an `FG_82`-style manifest/reference-name mismatch and a missing-attempt denominator case; require exact ID/byte/result closure and typed invalids. This should be consolidated with existing evidence-closure work rather than queued as a duplicate build.
3. **Extend artifact-view conformance examples, not the core schema.** Use one answer with absent static reference but executable source derivation, one chart with truthful appearance but wrong source binding, and one spreadsheet with correct sampled values but a hidden unsampled/formula/counterfactual defect.
4. **Represent mixed suites as portfolio vectors.** Keep answer hit rate, rendered-chart correctness/readability, and native-file validity separate; any scalar must name its weighting, gates, denominator, and use case.
5. **Treat Skills and consensus rubrics as configured interventions.** Require exact bundle identity, invocation evidence, paired attempts, criterion-authority review, and held-out evaluator perturbations before effect or validity claims.
6. **Keep the source at Tier A/B relevance.** AIDABench raises a Tier A artifact-routing/closure question and supplies Tier B evaluator/package machinery, but its empirical evidence is insufficient to steer professional-readiness thresholds.

No new queue task is warranted: package/evidence closure and plural artifact-view conformance are already covered by existing claimed or pending work. The durable action is to make this case discoverable in the synthesis and landscape maps and reuse it in those consolidations.

## Claim boundary

AIDABench v2 and the audited release provide evidence that 11 March-2026 configured model–agent packages achieved different binary/fractional evaluator scores on a public 603-task portfolio of workplace-like answer, chart, and file-generation tasks, and that retry selection, task family, and auxiliary summaries materially affect those scores. They also provide strong inspectability evidence for task and evaluator design, with one identified reference-path defect and substantial post-paper feature drift. They do **not** establish a representative enterprise-work population, calibrated human difficulty, deterministic or expert-equivalent evaluators, one common pass probability, model-only capability, professional-quality acceptance, procurement value, economic benefit, safety, or deployment readiness.

# PM-LLM-Benchmark: broad process-analysis prompts expose an inquiry ladder, but a holistic judge score does not identify analytical quality

## Bottom line

PM-LLM-Benchmark is a useful early inventory of language-model interactions with process-mining artifacts. Its 52 paper-era tasks span event-log abstractions, process-mining concepts, model construction and interpretation, hypothesis generation, fairness prompts, and visualizations. That breadth matters: the paper recognizes that domain analysis is not exhausted by fact recall and explicitly says future benchmarks should test the full hypothesis feedback-and-verification cycle rather than generation alone.

The implemented 2024 instrument does not test that cycle. It presents one static prompt, records one free-text answer, and asks another LLM for one holistic 1–10 grade without a reference answer, criterion rubric, executable check, evidence-use trace, human process-mining labels, repeated judge calls, or downstream decision. Process-model code is not run; hypotheses are not operationalized or tested; anomalies and root causes are not separated; fairness comparisons have no policy or statistical decision contract; recommendations have no action or outcome. “Process-specific knowledge” is mostly public process-mining vocabulary and prompt-contained abstractions. Organization-specific domain knowledge, its provenance, and its effect are absent.

The strongest paper-era claim is therefore narrow: **under one-shot prompting and one GPT-4o judge prompt, 28 configured 2024 model packages received different scalar ratings on a purposive set of 52 short process-mining-themed prompts**. The study does not establish process-analysis correctness, expert equivalence, reliable hypothesis generation, causal diagnosis, fairness competence, operational usefulness, or production readiness. Its five-by-five cross-judge table is a useful sensitivity probe, but means and standard deviations across heterogeneous tasks are not judge accuracy, human agreement, repeated-call reliability, or score uncertainty.

The official repository has evolved substantially. The audited 10 July 2026 snapshot is much more inspectable: it contains 8,646 answers and 8,646 GPT-5.4 evaluations for 158 model prefixes. But it is a replacement instrument, not a comparable update: only 2 of the 52 paper-era task stems survive among 57 current tasks. The current scorer also applies an undocumented nonlinear per-item transform, a name-dependent reasoning-model adjustment, unequal category weights, and a sum-divided-by-10 aggregate whose maximum changes with task count. It includes 2,514 answer files containing `<think>` tags and conditionally instructs the judge to ignore early “flow of thought.” Those choices make the leaderboard a property of a versioned answer-exposure, judge-prompt, model-classification, parsing, transformation, and aggregation package—not a stable process-mining capability scale.

## Source and reading record

### Complete primary paper read

- Alessandro Berti, Humam Kourani, and Wil M. P. van der Aalst, *PM-LLM-Benchmark: Evaluating Large Language Models on Process Mining Tasks*.
- Immutable record: <https://arxiv.org/abs/2407.13244v1>; PDF: <https://arxiv.org/pdf/2407.13244v1>.
- Version read: immutable arXiv v1, submitted 18 July 2024. The archived API metadata contains one normal entry and no withdrawal or retraction notice.
- Local PDF: `data/papers/pdfs/2407.13244v1-pm-llm.pdf` (13 pages; 179,628 bytes; SHA-256 `da2b27d42ad008f4b846664f7ccee4621c86a8be2d45794ee581cdd3b419efb1`).
- Local full text: `data/papers/text/2407.13244v1-pm-llm.txt` (46,943 characters; SHA-256 `4cced4ea35b9faf4ade3ea83211802c6137a62f14f6b05fb3fa5104efca583d4`).
- Date read: 17 July 2026. The complete paper was read through motivation, related evaluation work, all task categories, evaluation strategy, scripts, result tables, future strategies, conclusion, references, and final page.

### Official release audit

- Author-declared repository: <https://github.com/fit-alessandro-berti/pm-llm-benchmark>.
- Paper-era candidate: [`8d35bf2fdac0ac9e3fcc11f5a8b53d6780d904d5`](https://github.com/fit-alessandro-berti/pm-llm-benchmark/commit/8d35bf2fdac0ac9e3fcc11f5a8b53d6780d904d5), dated 12 July 2024, six days before arXiv v1. It is the nearest recoverable pre-submission commit in the acquired official history, not a cryptographically paper-declared snapshot.
- Paper-era archive: `data/sources/releases/2407.13244v1-pm-llm/pm-llm-benchmark-8d35bf2.zip` (1,667,614 bytes; SHA-256 `5dc8aaba23f9eb568df5742a7b62620bc142aa407fd39dcc0adfe087c89061b6`).
- Current audited snapshot: [`483fef81cf90766582541db7ec47dc9e9d5899d6`](https://github.com/fit-alessandro-berti/pm-llm-benchmark/commit/483fef81cf90766582541db7ec47dc9e9d5899d6), dated 10 July 2026.
- Current archive: `data/sources/releases/2407.13244v1-pm-llm/pm-llm-benchmark-483fef8.zip` (57,746,611 bytes; SHA-256 `0341a64a07827cd02961fafa34b7425ce917c92a2f354a304c19985b7b3b255f`).
- Provenance: `data/sources/releases/2407.13244v1-pm-llm/provenance.json`; paper-era history and commit metadata are preserved beside it.
- Machine-readable audit: `data/sources/releases/2407.13244v1-pm-llm/release-audit.json`.
- Both snapshots include a GPL-3.0 license file.

The audit inspected every paper-era prompt, the paper-era answering/evaluation/scoring scripts and README score rows, the current prompt set, answer/evaluation pipeline, scoring and leaderboard code, model configuration, hallucination analysis, three current answers and corresponding judge rationales in depth, and aggregate properties of all 8,646 current answer/evaluation pairs. Both Python trees passed `compileall`. No paid model endpoint was called and no result was regenerated; this is a static instrument, released-result, and implementation audit.

## Why this matters for skill-bench

This review advances charter objectives A and B through expansion and validation of a domain-analysis benchmark family. It does not narrow `skill-bench` to process mining. The general hypothesis is that a domain benchmark can reveal a reusable **analytical inquiry ladder**—artifact comprehension, candidate interpretation, discriminating test, evidence acquisition, update, decision, and consequence—but cannot collapse those stages into one prose-quality grade.

The concrete evidence is an immutable full paper, two commit-pinned official snapshots, all paper-era prompts and score rows, 17,292 current answer/evaluation artifacts, and executable scorer logic. The uncertainty clarified is what one-shot judge scores can support when purported process-analysis tasks stop before verification. This is expansion plus validation. Useful completion is a claim-bounded account of task authority, process/domain knowledge, stage coverage, judge validity, score semantics, release drift, and cross-domain design actions—not a process-mining-specific benchmark proposal.

## One-sentence contribution

PM-LLM assembles a broad, inspectable process-mining prompt inventory and judge-sensitivity study, while exposing that one-shot holistic prose ratings cannot identify whether a system correctly observes, hypothesizes, tests, updates, decides, or produces useful consequences.

### Research question

The paper asks how LLMs of different sizes perform on a broad collection of process-mining tasks and whether advanced LLMs can grade their open-ended outputs without ground-truth answers. It contributes:

1. a 52-task, seven-category paper-era prompt suite;
2. scripts for OpenAI-compatible answer generation and model-based evaluation;
3. one-shot results for 28 commercial and open-source configured models under a GPT-4o-20240513 judge;
4. category- and prompt-level aggregates;
5. a 5 answering-model × 5 judge-model sensitivity table; and
6. an explicit future agenda for RAG, multi-agent analysis, hypothesis refinement, and generated semantic anomalies.

The novelty is not a validated measurement model. It is the breadth of process-mining interactions assembled into one inspectable prompt suite and the recognition that open-ended process analysis creates an oracle problem.

## Methodology and task construct

### Paper-era task taxonomy

The paper-era candidate contains 46 textual prompts and six image prompts:

| Category | Tasks | Implemented unit | What is actually observed |
|---|---:|---|---|
| C1: process comprehension, anomalies, root-cause analysis | 10 | DFG, trace-variant, or object-centric-log abstraction embedded in prose | Free-text description, anomaly nomination, or plausible root-cause narrative |
| C2: process-mining domain knowledge | 9 | Open conceptual questions and closed process-mining/Petri-net questions | Free-text recall and explanation |
| C3: process-model generation | 8 | Natural-language process or small event data | Text/code for temporal profiles, DECLARE, Log Skeleton, process trees, or POWL |
| C4: process-model understanding | 7 | BPMN/XML/JSON, DECLARE, or Log Skeleton representation | Free-text description, query answer, or anomaly interpretation |
| C5: hypothesis generation | 4 | Event-log abstraction or process model | List of candidate hypotheses |
| C6: fairness assessment | 8 | Synthetic domain framing or protected/non-protected summaries | Attribute nomination and prose comparison |
| C7: visual prompts | 6 | Process-mining visualization | Generic image description |

The tasks are purposive and static. The paper says prompts were tailored to what GPT-4o and Claude 3.5 Sonnet could handle and excludes mainstream tasks such as Alpha Miner application and Petri-net soundness because then-current models did not support them effectively. This is an outcome-aware feasibility filter: the suite samples selected tractable interactions, not a defined universe of process-mining work. Prompt length is capped below 8K characters for model compatibility. There is no task-source sampling frame, expert-authoring ledger, independent task approval, difficulty calibration, hidden test set, or maintenance protocol.

### Process-specific versus domain-specific knowledge

The suite usefully distinguishes several information types, but the paper's language risks merging them:

- **generic process-mining knowledge:** definitions of event abstraction, process cubes, trace clustering, Petri nets, and notation;
- **prompt-contained process evidence:** activity labels, path frequencies, directly-follows edges, model fragments, and group summaries;
- **generic business priors:** expectations about purchase-to-pay, hiring, lending, renting, hospital, or road-traffic processes;
- **organization-specific knowledge:** local policies, exceptions, role authority, data-generating quirks, thresholds, contractual obligations, and accepted causal explanations.

PM-LLM directly tests the first two and invites the third. It does not provide the fourth, trace its authority, or test whether retrieval and adoption of that information changes analysis. A plausible story based on activity names can score highly even when the event abstraction cannot distinguish it from alternatives. Thus the benchmark is process-mining-themed and sometimes process-evidence-conditioned; it is not evidence that a model acquired or correctly used an organization's tacit domain expertise.

### One-shot administration and LLM judging

For each textual item, the system sends the prompt as-is to an answering model. The answer is then embedded with the question in a generic judge request: grade from 1.0 to 10.0. Visual items ask the answering model to describe an image and ask the judge to grade the answer while seeing the image. No task-specific rubric, reference answer, required evidence span, failure signature, or score anchor is supplied.

The paper reports item-level means and standard deviations across task sets and model groups. These standard deviations describe heterogeneous item scores; they are not uncertainty from repeated model runs or repeated judge calls. Every headline result is one-shot. The paper-era README's leaderboard sums item ratings and divides by 10, producing a maximum of 52 for visual-capable models and 46 for text-only models. Although parenthetical text-only subtotals are shown for some commercial systems, the headline ordering mixes different eligibility sets and weights categories by their task counts.

## Evidence and warranted interpretation

### Paper-era results

Table 2 reports mean GPT-4o-judge ratings from 8.4 for Claude 3.5 Sonnet and 8.3 for GPT-4o self-evaluation down to 2.5 for Qwen 4B v1.5. Larger and less aggressively quantized packages generally score higher. C2 conceptual knowledge receives high means across groups; process-model generation/understanding and fairness show larger differences. The authors infer that commercial and large open-source models can perform process-mining tasks adequately and that some small models are “process-mining-capable.”

The directional size/quantization pattern is descriptive evidence for this configured prompt-and-judge package. It is not enough for the paper's adequacy language. Model families, quantization formats, providers, context lengths, and possible vision eligibility differ simultaneously. There are no matched repeated runs, hardware/runtime records sufficient to isolate quantization, uncertainty over pairwise differences, or external outcomes. A lower score after stronger quantization is consistent with a package effect; it does not identify weight precision as the cause.

### Cross-judge table

Table 4 evaluates five answering models with GPT-4o and four open-source judges. This is a good instinct: evaluator identity is made an experimental axis. It reveals substantial level and interaction effects. For example, Llama 3 70B's mean ranges from 7.4 under GPT-4o to 8.8 under itself; WizardLM-2-8x22B ranges from 7.1 to 8.3; Qwen2 72B ranges from 7.6 to 8.6. The paper notes Llama's egocentric result and score plateauing under a weaker judge.

But the statement that the table “justifies LLMs-as-Judges” exceeds the design. There is no human/expert criterion, no independently adjudicated correct/incorrect set, no item-level agreement statistic, no repeat reliability, no order/verbosity control, no blinded response identity audit, and no held-out judge-prompt calibration. Similar aggregate rankings can arise from shared model priors or common sensitivity to fluency. Different absolute levels matter because the benchmark declares sufficiency thresholds. Cross-model covariance without an authoritative target establishes judge sensitivity, not judge validity.

### Paper-era release reconstruction

The candidate snapshot preserves all 52 prompts and per-model item-score tables for 28 models, but no answer text or evaluation text: both released result directories contain zero `.txt` records. Therefore neither answer quality nor judge reasoning can be audited for the paper result.

Independently summing the README item scores and dividing by 10 reproduces 19 of 28 displayed totals under ordinary one-decimal rounding. Nine differ. Most differences are 0.1 and may reflect truncation or stale display values, but two are larger: Llama 3 70B Q4_0 reconstructs to 30.83 versus 30.2 reported, and Gemma v2 9B reconstructs to 26.24 versus 26.4. Without raw outputs, judge records, or a table-building manifest, the discrepancies cannot be resolved. The paper's Table 2 means are consistent in scale with the README rows, but exact endpoint regeneration is unavailable.

## Unique insight: domain analysis is a staged inquiry process, not a prose genre

PM-LLM's strongest transferable insight comes from the mismatch between its categories and its own future-work section.

A process analyst does not merely emit a polished paragraph. A defensible episode often has this structure:

`authorized process artifact and context`
`→ observation with source span`
`→ anomaly or candidate hypothesis`
`→ rival explanations and uncertainty`
`→ discriminating query/test and required evidence`
`→ executed result with validity checks`
`→ hypothesis update or rejection`
`→ recommendation under threshold/constraint`
`→ authorized action or handoff`
`→ measured intended and collateral consequence`.

PM-LLM usually observes only the third node. C1 asks for anomaly and root-cause narratives from compressed abstractions; C5 asks for hypotheses; C6 asks for sensitive attributes or group comparisons. The same fluent answer can contain a correct observation, an unsupported causal attribution, a useful question, and an unsafe recommendation. One holistic 1–10 score cannot localize which link succeeded.

This creates an **analytical-stage substitution** failure: candidate generation is promoted into verified analysis, and rhetorical completeness substitutes for evidential closure. The paper itself recognizes this in Section 5: hypothesis generation should include verification against event data, feedback, and refinement, and final-output-only evaluation can be misleading for agent crews. That admission does not invalidate C5 as a brainstorming probe. It correctly bounds it to candidate-hypothesis generation.

The cross-domain lesson for `skill-bench` is to score the inquiry graph rather than reward answer genre. Candidate insights should receive credit for novelty and discriminating value without receiving truth credit until tested. Observations, hypotheses, causal claims, fairness judgments, and recommendations require different authorities and observers. A model that abstains, requests missing policy, or designs a decisive query may be more professionally useful than one that produces a confident complete narrative from insufficient data.

## Failure analysis by category

### C1: observation, anomaly, and cause are conflated

Directly-follows graphs and frequent variants can support descriptive claims about represented paths and counts. They generally do not identify why a path occurred. Activity labels can suggest semantic anomalies, but a “root cause” requires covariates, temporal precedence, alternative explanations, and an identification strategy. The generic judge can reward plausible domain stories without checking whether they are entailed. `skill-bench` should preserve `observation`, `anomaly_candidate`, `causal_hypothesis`, `support`, `rival`, and `required_test` as distinct objects.

### C2: useful prerequisite knowledge, weak work validity

Conceptual questions can reveal whether a model knows process-mining terminology and can explain method tradeoffs. That is relevant prerequisite evidence. It is not an executed analytical task and does not show method selection under organizational constraints, correct implementation, or recipient usefulness. Closed questions should use deterministic or expert-adjudicated anchors where possible rather than inheriting the same holistic judge.

### C3: code-shaped output without execution

Several tasks request process-tree, POWL, DECLARE, Log Skeleton, or temporal-profile constructions. The answer may include executable-looking PM4Py code, but the paper-era grader does not parse, run, validate, or compare its semantics. Syntax, object-parent integrity, accepted language, forbidden traces, soundness, and alternative equivalent models remain unobserved. A prose judge may overvalue explanation and undervalue semantic defects. This category should separate parse/execute, positive-trace acceptance, negative-trace rejection, structural invariants, and expert preference over equivalent models.

### C4: model comprehension without query contracts

Model interpretation is closer to evidence-grounded work, yet the benchmark does not bind answer claims to model elements or execute queries against a canonical semantic representation. Errors in XML reading, control-flow semantics, or anomaly nomination are scored as one impression. A stronger design would provide requirement atoms and model-query or trace witnesses, while allowing plural valid explanations.

### C5: candidate hypothesis quality, not verified analysis

Generating possible explanations can be valuable. The prompt and score do not test specificity, falsifiability, evidence availability, test design, update after contrary evidence, multiplicity, or whether a hypothesis generalizes beyond the shown sample. High C5 scores support judge-perceived brainstorming quality only. They do not show that a model can discover a true relationship.

### C6: fairness prose without decision authority

Attribute nomination and protected/non-protected comparisons expose relevant awareness, but fairness is not identified by mentioning protected classes or comparing averages. The tasks lack a declared decision, legal/policy jurisdiction, legitimate comparator, measurement validity, confounders, uncertainty, threshold, harm model, or affected-party authority. The benchmark should not promote C6 scores into fairness competence.

### C7: generic visual description

The visual treatment asks “Can you describe the provided visualization?” This tests broad visual narration of selected process-mining plots. It does not require evidence localization, analytic decision, uncertainty, accessibility, or action. Vision-ineligible models also receive a different denominator, making the headline aggregate treatment-dependent.

## Current v2.2 snapshot: stronger artifact release, broken longitudinal identity

The current audited snapshot is operationally richer:

- 51 text prompts plus six images across eight categories;
- 8,646 answers and 8,646 GPT-5.4 evaluation files;
- 158 model prefixes, of which 98 have all 57 items and 60 have the 51 text items;
- exact one-to-one answer/evaluation filename alignment;
- judge rationales and leaderboard-generation code; and
- later hallucination and judge-analysis utilities.

This is valuable inspectability. One unparseable evaluation says no answer was provided and is silently mapped to 1.0 by the scorer; every other released evaluation yields a parsed number between 1 and 10. Raw per-case records make such failures discoverable.

However, instrument identity has changed. The paper-era and current suites have only two exact task-stem overlaps: `cat03_03_log_skeleton_generation` and `cat04_04_declare_description`. Task counts change from 52 to 57; C8 optimization is added; category membership and content change extensively. Current scores cannot be interpreted as progress on the 2024 form without anchors, common-item calibration, matched system reruns, or a score bridge.

The score semantics also changed materially:

1. The parser selects a plausible first numeric grade from judge prose and defaults missing grades to 1.0.
2. Each raw grade is transformed by `min(7, raw) + 0.5*max(min(raw, 9)-7, 0) + 2*max(raw-9, 0)`. Thus raw 7.4 becomes 7.2, 8.3 becomes 7.65, and 9.1 becomes 8.2, while 10 remains 10.
3. Selected model names classified as visible reasoning models receive a different judge instruction—ignore early flow of thought and grade only final statements—and then a second name/configuration-dependent downward adjustment.
4. Item values are summed and divided by 10 rather than normalized by eligible items. The current main score excludes C7, includes categories with five to nine items, and changes its maximum and category leverage when tasks are added.
5. The README labels the result “1-shot” but does not document the full score transform beside the leaderboard.

The release contains 2,514 answer files from 52 model prefixes with `<think>` tags. Because evaluation includes the raw answer and only conditionally tells the judge to disregard early reasoning, the observer view differs by model classification. This can reward or penalize exposure format, verbosity, self-correction, and classification heuristics. It also makes future leaderboard reproduction sensitive to changing model names/config entries. The scorer's fallback path additionally references `Counter` without importing it, a dormant implementation defect when precomputed leaderboard statistics are absent.

Accordingly, the current leaderboard is highly inspectable as a **configured release result**, but its scalar should not be called a stable process-mining capability measure or compared directly with paper-era totals.

## Reproducibility and operational realism

**Paper inspectability: moderate.** The paper names categories, prompts, judge template, model groupings, results, and limitations. It does not define task-level rubrics, answer keys, model endpoint parameters, seeds, decoding settings, exact runtime dates for every call, or human validation.

**Paper-era release inspectability: weak for results, good for prompts.** All prompts and per-item scalar rows are present, and scripts are readable. Raw answers and judge outputs are absent. Nine displayed totals do not follow ordinary one-decimal reconstruction from released rows. The exact paper snapshot is inferred from history rather than declared.

**Current release inspectability: strong for stored endpoint records.** All 8,646 answer files align with 8,646 judge files; prompts, scorer, judge rationales, and leaderboard artifacts are available. This permits score-path and failure audits without paid calls.

**Exact regeneration: weak.** Both eras depend on mutable commercial/provider endpoints. The paper-era scripts hard-code minimal configuration and have no package lock, request/response metadata ledger, seed, retries manifest, cost, or endpoint snapshot. The current code has much more provider logic but still cannot freeze hosted weights or behavior. One-shot stochastic outputs are not reproducible in the experimental sense.

**Operational realism: low to moderate for isolated artifact interpretation, low for professional analysis.** Real process-mining notations and public event-data abstractions improve surface relevance. But the interaction is static and one-shot, with no source discovery, database execution, missing-data negotiation, stakeholder clarification, policy lookup, iterative hypothesis test, model deployment, action, or recipient acceptance. The task ends before the work product changes a process decision.

## Limitations and validity threats

1. The suite is purposive, feasibility-filtered, and tailored to strong 2024 models rather than sampled from a defined work universe.
2. Excluding tasks current models could not perform conditions content on expected system success.
3. Prompt authorship and final content approval are not represented at task level.
4. Public event data and static prompts create contamination risk acknowledged by the paper.
5. Organizational domain knowledge, policy, exceptions, and authority are absent.
6. Process evidence, generic business priors, and memorized process-mining knowledge are not experimentally separated.
7. Causal root causes can be invented from descriptive abstractions.
8. Candidate hypotheses are not operationalized, executed, falsified, refined, or linked to decisions.
9. Fairness prompts lack outcome authority, comparator legitimacy, statistical uncertainty, policy thresholds, and affected-party review.
10. Generated process-model code is not parsed or executed.
11. Semantic equivalence and alternative-valid models are not represented.
12. Visual tasks use generic description rather than task-bound analytic extraction.
13. The judge receives no task-specific rubric, reference, criterion weights, evidence requirements, or failure signatures.
14. No human process-mining expert labels or artifact judgments validate the judge.
15. The cross-judge table measures model-judge sensitivity, not correctness or human agreement.
16. Aggregate rank similarity can arise from shared priors and verbosity preferences.
17. Judge and answering model identity are sometimes from related families, enabling self/family effects.
18. One run per answer and judge provides no repeat reliability or rank probability.
19. Reported standard deviations across tasks are not repeated-measure uncertainty.
20. Model family, size, quantization, provider, runtime, and vision eligibility are confounded.
21. The score mixes unlike task constructs and unequal category counts.
22. Visual-capable and text-only headline totals have different maxima.
23. Sufficiency/good/excellent thresholds have no external criterion or decision-loss validation.
24. Paper-era raw answers and judge rationales are absent.
25. Nine paper-era README totals differ from ordinary reconstruction; two differences exceed rounding ambiguity.
26. The exact paper-era repository identity is not author-declared.
27. Current and paper-era forms share only two exact task stems.
28. No anchor/common-item bridge supports longitudinal comparison.
29. The current nonlinear score transform is not evident from the leaderboard's headline semantics.
30. Current name-dependent reasoning classification changes both observer instructions and post-score treatment.
31. Current raw answers expose chain-of-thought-like tags for many systems, changing the evidence view and creating avoidable sensitive-trace retention.
32. One current judge-invalid record is silently converted to a substantive score of 1.0 rather than typed as evaluator invalidity.
33. Current aggregate scale and category leverage change when task counts change.
34. Cost, latency, retries, token use, and provider failure burden are not part of the primary metric.
35. No result links scores to analyst acceptance, decision quality, process improvement, fairness outcome, or operational harm.

## Transferable design patterns

### Retain

1. **Keep broad analytical stages visible.** Comprehension, model construction, hypotheses, fairness, visualization, and optimization should not be reduced to factual QA.
2. **Use real domain representations.** DFGs, variants, object-centric artifacts, BPMN, DECLARE, Log Skeletons, and process trees are useful substrate classes.
3. **Make evaluator identity an explicit axis.** The five-judge sensitivity table is more informative than silently treating one judge as truth.
4. **Release raw per-case records.** The current snapshot's answer/evaluation pairs permit audits impossible for the paper-era result.
5. **Acknowledge contamination and lifecycle pressure.** The paper correctly anticipates static-public-prompt exposure and dynamic generation needs.
6. **Treat hypothesis refinement as a full cycle.** The paper's own future-work boundary is the right direction.

### Repair

1. **Type the analytical stage.** Separate observation, interpretation, anomaly, candidate hypothesis, causal claim, discriminating test, result, update, recommendation, decision, and consequence.
2. **Bind every claim to evidence.** Require source spans, model elements, query outputs, valid-time state, and explicit unknowns.
3. **Use executable plural observers.** Parse/run model code; test positive and negative traces; check structural invariants; retain expert criteria for semantics and usefulness.
4. **Preserve alternatives.** A task may admit multiple valid process models, hypotheses, test plans, or recommendations; score contract satisfaction rather than one favored narrative.
5. **Reward falsifiability without laundering truth.** Give candidate hypotheses credit for specificity and discriminating value, but truth credit only after valid tests.
6. **Add rival explanations and stopping rules.** Require what evidence would change the conclusion and when escalation or abstention is appropriate.
7. **Validate judges criterion by criterion.** Use expert-adjudicated cases, blinded labels, repeat calls, disagreement analysis, verbosity controls, and criterion-level confusion—not aggregate rank resemblance alone.
8. **Keep evaluator invalidity separate.** Missing or unparseable judge output is not a substantive score of 1.
9. **Freeze score contracts.** Publish raw ratings, transforms, category weights, eligibility, missingness, and maximum; bridge versions with anchors before trend claims.
10. **Minimize reasoning-trace retention.** Grade declared final artifacts under a consistent evidence view unless reasoning traces are an explicitly consented construct.
11. **Measure operational use separately.** Analyst acceptance, evidence-gathering burden, decision changes, process outcomes, and harms need their own studies.

## Concrete changes for skill-bench

1. **Do not create a process-mining schema or narrow the benchmark to process analysis.** Map PM-LLM's useful stages onto existing evidence, artifact, projection, configured-system, evaluator, metric, and validity records.
2. **Build one cross-domain analytical-hypothesis lifecycle slice.** Use at least two unlike domains and a frozen evidence graph per case. Require an initial observation, candidate hypothesis plus rival, predeclared discriminating query/test, executed evidence, update/rejection, and bounded recommendation or escalation. Score candidate quality, test validity, evidence adoption, and final consequence separately.
3. **Add adversarial controls.** Include a plausible but unsupported cause, a correct observation with a wrong cause, a non-discriminating test, contradictory evidence, a valid abstention, and two equivalent process/model representations.
4. **Keep raw and decision scores distinct.** Never apply hidden nonlinear transforms or let version task count redefine the scale. Store raw observer outputs and typed invalidity before any declared stakeholder aggregation.

Only one new queue task is warranted: a bounded validation slice for the analytical hypothesis lifecycle. Existing evidence-acquisition and validity machinery should be reused; no process-mining-specific subsystem follows.

## Claim boundary

PM-LLM-Benchmark v1 and the nearest recoverable paper-era release establish that an inspectable 52-item prompt suite can elicit and holistically judge selected process-mining-themed free-text outputs from 28 configured 2024 model packages. The paper's cross-judge matrix establishes evaluator sensitivity and possible self/strength interactions, not judge validity. The 2026 official snapshot establishes a much larger, raw-record-rich configured leaderboard over 57 mostly replaced tasks, with auditable but materially changed grading semantics. Neither version establishes correct process analysis, verified hypothesis discovery, causal root-cause diagnosis, fairness competence, expert-equivalent domain knowledge, operational utility, longitudinal model progress, professional validity, or production readiness.

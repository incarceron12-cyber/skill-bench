# EnergyEvals: live tools do not make an answer time-valid or professionally validated

## Bottom line

EnergyEvals makes an important construct move: it asks agents to retrieve market data, inspect regulatory material, and execute quantitative analysis with domain tools rather than answer static energy questions. Its 243-paper-task design, three capability areas, paired source prompts, seven configured systems, separate approach/answer/source scores, and released traces make it a useful methodological case for consequential analytics.

But the paper does not establish “real-world energy analytics” in the strong sense implied by its title. The task corpus has no documented sampling frame, item-level expert authority, independent agreement, rejected-item ledger, source snapshots, or downstream professional use. Historical prompts are often date-bounded, but two regulatory prompts say “latest” without an as-of time; live API/search/document results are not identity-pinned; and references, expected attributes, tolerances, and judge outputs are not released. Most decisively, the source-validity prompt evaluates citation inclusion and plausibility from the answer and suggested approach—not the retrieved evidence—and instructs the judge to treat internal databases as equivalent to authoritative external sources. A high score therefore cannot prove that the cited version existed, was accessed, entailed the claim, was current at the task time, or survived later correction.

The exact official post-v1 archive is valuable but does not reproduce the paper. The paper says 243 tasks; Appendix A.13 says the repository contains 212; the archive contains 188 prompt-only rows. The paper says 30 questions have released traces; the archive contains 36 question IDs across twelve model directories. The twelve trace models are not the seven-model study panel except for Claude Sonnet 4.6. Two traced tariff prompts omit substantive constraints later present in the CSV. The README references grading files that are absent, the database implementation is an unshipped optional package, and no RAG tool or paper ground truth is included. These are not cosmetic count errors: there is no immutable form/run/score join key from which to reproduce the headline tables.

The strongest transferable insight is a **source-time analytical claim ladder**:

```text
authored task
→ intended source and valid-time requirement
→ available tool/environment snapshot
→ immutable retrieval receipt
→ source authority + passage entailment
→ typed extraction
→ auditable transformation/model
→ analytical result
→ independent expert acceptance
→ intended-use utility
→ production fitness and readiness
```

EnergyEvals observes parts of the task, tool-call, answer, and judge-agreement middle. It does not license inheritance up this ladder.

## One-sentence contribution

EnergyEvals contributes a rare live-tool professional-analytics instrument, but its deeper lesson is that mutable source access, authored reference agreement, citation presentation, and professional source-time validity are separate claims that require an immutable evidence-receipt chain.

## Why this matters for `skill-bench`

This review advances charter objectives A, B, and C through a narrow energy-analytics case of a general benchmark problem: **how to evaluate knowledge work when the evidence and tools are mutable at run time**. Energy is not a proposed scope boundary. The same issue applies to finance, law, policy, medicine, procurement, market research, and any workflow whose answer depends on a live API, search index, current document, tariff, docket, or database.

The reusable hypothesis is:

> A live-source benchmark can support time-valid analytical claims only if it binds task semantics, evidence availability, source identity, retrieval time, represented valid time, transformation identity, and grader evidence view; a citation-style score or correct authored answer is insufficient.

Useful completion therefore means preserving the benchmark's heterogeneous tool-and-analysis structure while refusing to equate live access with source validity, a reference answer with analytical truth, an expert-authored prompt with professional acceptance, or a one-run score with readiness.

## Sources and review status

**Deep review of the complete immutable arXiv v1 and static audit of the exact official post-v1 release.**

- **Paper:** David Akinpelu, Akintonde Abbas, Rereloluwa Alimi, and Ayodeji Lana, *How Do Tool-Augmented LLM Agents Perform on Real-World Energy Analytics Tasks?*, arXiv:2606.26346v1, <https://arxiv.org/abs/2606.26346v1>.
- **Version read:** immutable v1, submitted 24 June 2026; metadata has no withdrawal/retraction notice.
- **Date read:** 2026-07-15.
- **Local PDF:** `data/papers/pdfs/2606.26346v1-energyevals.pdf` (22 pages; SHA-256 `ed1ae39fcb43bcc50bfb895e2b9ac782e23abc0fb8f2d82332a7eefdae11c7f0`).
- **Local full text:** `data/papers/text/2606.26346v1-energyevals.txt` (82,624 bytes; SHA-256 `e40b4f88ad06fbdaea891c6afb96a3013e4101948fb9010283a5ff9c58efec44`).
- **Official repository:** <https://github.com/Tume-AI/energy-evals>.
- **Pinned commit:** `90cc6165d514cdc37c3a3df8de95a9839a1f3a08`, 25 June 2026, 4 hours 30 minutes 40 seconds after v1 publication; it is post-v1 release evidence, not assumed manuscript-time identity.
- **Local archive:** `data/sources/releases/2606.26346v1-energyevals/Tume-AI-energy-evals-90cc616.zip` (SHA-256 `364b2bac678c556d754ba02dd8cfcf627bef23aacaca932bd7418ccf3e077b4d`; 516 files).
- **Provenance:** `data/sources/releases/2606.26346v1-energyevals/provenance.json`.
- **Executed static audit:** `data/sources/releases/2606.26346v1-energyevals/REVIEW_RELEASE_AUDIT.json`.
- **Execution boundary:** no paid/live model, search, market-data, tariff, weather, docket, or document API was invoked. Release findings come from full archive inspection and local computation.
- **Tags:** live evidence, valid time, professional analytics, tool-augmented agents, source authority, quantitative modeling, LLM judge, release conformance.

## Research question and exact claim ceiling

The paper asks how seven frontier LLMs perform as ReAct agents on energy-market work requiring live data, regulatory/document retrieval, and quantitative modeling, and whether explicit source cues and domain tools improve performance (Sections 1, 3–6, pp. 1–9).

The paper supports this bounded claim:

> On the authors' reported 243-item U.S.-electricity instrument, under their low-reasoning ReAct configurations, mutable tool environment, authored ground truths, three-judge median policy, class-balanced aggregation, and one reported evaluation period, the seven configured systems received different answer, approach, source, token, tool-call, cost, and terminal-failure profiles; on selected subsets, source-explicit prompts raised source-style scores more consistently than answer scores, and access to the selected domain tools coincided with higher answer scores.

It does **not** establish:

- a representative sample of energy-analyst work, errors, employers, market regions, decisions, or consequences;
- that each task, expected answer, tolerance, source, approach, and threshold was authorized by a qualified expert for that exact claim;
- that a result is correct as of a declared time, because source/document/API snapshots and reference valid times are not preserved;
- that the live tool results were identical or exposure-equivalent across models, conditions, retries, or dates;
- that source-validity scores validate actual source access, version, passage entailment, freshness, completeness, or citation accuracy;
- that one suggested approach is necessary, sufficient, or alternative-complete;
- that expected attributes and numerical tolerances are professionally acceptable or decision-calibrated;
- that three model judges are accurate because no independent item-level human label matrix validates their decisions;
- that source cues or tools caused the reported differences, because subset construction, temporal exposure, paired analysis, and missingness are under-specified;
- that temperature zero makes provider outputs deterministic or that one trial establishes reliability;
- that high approach scores reveal expert-like process rather than judge agreement with an authored method summary;
- professional utility, decision quality, safe operation, production fitness, or readiness.

## Methodology and system

### Task construction and expert authority

The paper reports 243 tasks: 107 Market Data, 86 Knowledge, and 50 Quantitative, stratified Easy/Medium/Hard (Section 3.2 and Table A.1, pp. 3–4, 14). Tasks cover prices, demand, generation, tariffs, interconnection, battery arbitrage, returns, IRR, and optimization. It says development was led by practitioners with doctoral training and more than 25 combined years at McKinsey, ICF, LCG Consulting, and GE (Sections 1 and 3.1, pp. 2–3).

This establishes plausible author familiarity, not task-level authority or construct validation. The paper does not report:

- how many experts authored and reviewed tasks or whether the four paper authors are the full authoring panel;
- which qualification, role, geography, market, or workflow supports each item;
- a work-population sampling frame, incident source, frequency, consequence, or intended recipient;
- candidate/rejected counts, rejection reasons, edits, reviewer independence, pre-adjudication agreement, or unresolved disputes;
- expert/novice contrasts, pilot completion rates, think-aloud evidence, or professional artifact review;
- item-level source passages, valid intervals, reference-calculation workpapers, accepted alternatives, or escalation policies.

The scope is purposive U.S. electricity analytics. That is legitimate as a pilot but cannot support prevalence or broad professional-capability claims. Difficulty labels are author-defined by apparent retrieval/reasoning shape; no empirical item response, completion time, expert difficulty, discrimination, or threshold study validates Easy/Medium/Hard (Section 3.3, p. 4).

### Paper corpus, appendix corpus, and release corpus are not one auditable form

Three task counts appear in the primary/release evidence:

1. **243** in the abstract, Sections 1/3, Figure A.1, and Table A.1;
2. **212** in Appendix A.13's statement that the repository contains a complete list; and
3. **188** rows in released `data/evals_tasks_only_188.csv`.

The released rows contain 74 Data, 64 Knowledge, and 50 Quant tasks, versus the paper's 107/86/50. Difficulty is also different from the paper table's implied category distribution: the release has 20 Easy, 97 Medium, and 71 Hard. IDs are non-contiguous and extend to 281, so the 188 rows are not merely the paper's 243 rows minus 55 disclosed holdouts. No form manifest, item-version map, attrition table, retired-item reason, or paper-ID-to-release-ID crosswalk resolves the discrepancy.

The release CSV is prompt-only. Its five columns are ID, category, question type, difficulty, and question. It omits expected answer, attributes, tolerances, suggested steps, intended source, source snapshot, task valid time, author/reviewer lineage, split, and release status. Thus one can inspect prompt shape but cannot audit the instrument used for scoring.

This matters because Appendix A.14 names source-pair IDs up to 231 and a tool subset up to 245, while the current release has later IDs and missing counterparts. Corpus conformance is not a documentation nicety: a score is uninterpretable without the exact immutable task/reference/rubric form.

### Temporal semantics and live evidence

The corpus mixes at least four evidence-time regimes:

1. **historical structured data**, such as ERCOT prices over 2010–2024;
2. **historical-but-revisable records**, such as market data that can be corrected or republished;
3. **versioned regulatory documents**, such as tariff schedules and interconnection manuals; and
4. **live/current services**, including search, dockets, tariffs, current/forecast weather, and API catalogs.

In the 188-row release, 125 prompts contain an explicit year, which is useful temporal anchoring. But only two say “latest,” none says “as of,” and none uses a current/today/now lexical anchor. “Latest ISO-NE guide” is not a reproducible target without a task cut-off, document version/effective date, retrieval date, supersession rule, and acceptable version set. A historical period similarly does not identify which later correction or database vintage counts as truth.

The paper calls GridStatus, databases, tariff data, dockets, weather, search, and RAG “live” (Section 4.3 and Table A.3, pp. 5, 15–16). Live access improves ecological resemblance, but creates a treatment and validity burden:

```text
question valid time
≠ retrieval time
≠ provider index time
≠ document effective time
≠ event/market represented time
≠ grader/reference creation time
```

The paper does not publish these times or their admissible relationships. There is no synchronized evidence snapshot across model runs, no before/after content hash, no provider index/version, no document canonical ID, no correction/retraction state, and no rule for source changes between reference construction and agent execution.

### Tool suite and environment identity

The paper describes nine categories, including GridStatus, an internal Database MCP, Tariffs, Renewables, Battery Optimization, Dockets, Web Search, Weather, and RAG MCP, plus system shell/Python tools (Section 4.3 and Tables A.3–A.4, pp. 5, 15–16). Typed schemas and common registration are good configured-system design.

The exact archive narrows reproducibility:

- `energyevals/tools/__init__.py` makes the database an optional external `energyevals_db` package; README explicitly says it is not shipped.
- No RAG tool is included.
- Released traces list 35 tools including database methods, proving that an additional environment existed, but not preserving it.
- `configs/benchmark_config.yaml` is an example using `openai/gpt-4o-mini`, medium effort, 50 iterations, one trial, and shuffled questions—not a manifest for the seven paper systems, which the paper describes as low reasoning effort and temperature zero (Section 4.2 and Table A.2, pp. 5, 15).
- The released system prompt requires a source for every claim (`energyevals/agent/prompts.py`), whereas Appendix A.8 prints a shorter three-line prompt without that requirement (p. 17). The post-v1 prompt cannot be assumed paper-time identity.

The Docker code sandbox is more serious than a mere `cwd`: read-only root, non-root user, dropped capabilities, PID/memory/CPU limits, disposable containers, and separated `/work`/`/data` mounts are useful (`energyevals/tools/sandbox.py`). However, its default network is unrestricted Docker `bridge`; the egress firewall is optional. The entire repository `data/` directory is mounted read-only. That is adequate only if no private answer/rubric/source material is present there and network/provider access is intended. The paper gives no canary report, image digest, firewall state, host/tool secret boundary, or paper-run environment receipt.

### Retrieval receipts are incomplete

Release traces are unusually rich in step data. Each trace records query, final answer, tool names, arguments and raw outputs, timestamps, tokens, latency, provider/model labels, and some model parameters. That supports post-hoc tool-use inspection.

It is not a complete evidence receipt:

- Exa search uses mutable cache/livecrawl behavior and returns URLs/text, but no provider index snapshot or response content hash (`energyevals/tools/search_tool.py`).
- GridStatus calls a live API and writes transient rows to CSV, but does not preserve response headers, endpoint version, database snapshot, payload hash, or authoritative correction state (`energyevals/tools/gridstatus_tool.py`).
- Database and RAG source code/data are absent.
- Tool metadata records names, not implementation hashes, API schema versions, credentials/entitlements, dataset inventories, or availability windows.
- There is no declared comparison-time synchronization across seven systems or tool/no-tool arms.

A raw output in a trace can show what one agent saw. It cannot alone establish that another condition had an equivalent opportunity, that the result was authoritative for the represented time, or that the expected answer remained valid.

### Quantitative models are benchmark interventions, not neutral truth engines

The paper treats the battery optimizer as a domain tool for arbitrage and IRR-style questions (Sections 3.2/4.3, pp. 4–5). Release inspection shows a specific modeling policy in `sandbox/scripts/battery_optimize.py`:

- perfect price foresight;
- symmetric square-root charge/discharge efficiencies;
- continuous charge and discharge variables;
- a fixed 50% initial state and equality between first and final state;
- a degradation penalty on absolute net power;
- IPOPT as solver; and
- acceptance of `optimal`, `feasible`, or `locallyOptimal` termination.

These choices may be reasonable for a simplified witness, but they are not source-independent professional truth. The model does not establish market participation rules, ancillary-service stacking, outages, price uncertainty, interconnection constraints, degradation physics, tax/financing assumptions, or operational feasibility. The first timestep is fixed without the ordinary transition equation, and simultaneous charge/discharge is not explicitly prohibited. Reference validity requires a model card, equation/version hash, unit tests, solver certificate policy, sensitivity analysis, alternative-model review, and explicit claim scope. A numerical match to this tool can support conformance to its assumptions, not investment quality or operational readiness.

## Evaluation protocol

### Four labels, three reported dimensions, and ambiguous routing

The paper describes Approach Correctness (1–5), Answer Accuracy / Attribute Alignment (0–1), and Source Validity (1–5), while Figure A.1 says “four dimensions” and visually separates Answer Accuracy from Attribute Alignment (Section 5.1–5.3 and Appendix A.2, pp. 5–6, 14). Category-aware routing chooses accuracy for Data/Quant and attributes for Knowledge.

Keeping dimensions separate is good. But the exact estimands and applicability rules are incomplete:

- Are accuracy and attribute alignment alternative criteria or separate observations?
- How are mixed quantitative/qualitative tasks routed?
- What happens when a tool/environment failure makes answer evidence unavailable?
- Are clarification, context failure, missing response, and incorrect response excluded or scored zero?
- How do up-to-five attributes handle dependence, omissions, alternatives, and critical noncompensatory requirements?
- Which numerical tolerances apply to which item, and who approved them?

The paper reports no item-level metric specification, missingness ledger, grader invalid state, or threshold sensitivity.

### Approach scoring rewards agreement with one authored witness

The approach judge receives the question, a “Suggested Approach (Ground Truth),” and an agent-steps trace, then assigns 1–5 for framing, sources, logical steps, and tool usage (Appendix A.8, pp. 17–18). This makes workflow visible, which is preferable to final-answer-only scoring.

Yet one suggested approach is a **reference witness**, not an alternative-complete procedure oracle. The paper does not report accepted alternate tools, commutative steps, optional checks, necessary prerequisites, unsafe shortcuts, or false-rejection calibration. A correct alternative may look unlike the witness; a trace that narrates the witness may still rely on wrong evidence. The 1–5 anchors (“expert-like,” “minor issues”) have no behavioral examples, expert label set, rater reliability, or professional acceptance threshold.

### Answer and attribute scoring inherit reference validity

For quantitative tasks, the judge sees expected answer, agent answer, and absolute/relative tolerance. For mixed/knowledge tasks, an LLM extracts up to five expected attributes from the reference, experts “manually reviewed and updated as needed,” and three judges extract/compare agent attributes (Section 5.1 and Appendix A.8, pp. 5, 17–18).

This is scalable, but the reference layer is hidden. There is no released:

- expected answer or source-to-answer workpaper;
- expected attribute set;
- item tolerance and unit/rounding policy;
- extraction model/version/output;
- human edit log, reviewer identity, agreement, or unresolved alternative;
- dependency graph among attributes; or
- contrast set testing paraphrases, partial truth, wrong period/unit, coincidental numbers, and unsupported answers.

An attribute match supports agreement with a reviewed canonical list. It does not independently establish source entailment, calculation validity, professional completeness, or decision fitness.

### “Source validity” is largely source presentation

The source prompt is the most consequential measurement mismatch (Appendix A.8, p. 18). It says the judge evaluates only:

1. explicit inclusion of sources; and
2. relevance of included sources.

The prompt receives question, suggested steps, and agent answer—not the agent trace or raw source evidence. It tells the judge not to require queries/code and declares internal databases equivalent to external authoritative sources when plausible. It asks about authority, alignment, appropriateness, and missing citations, but gives the judge no receipt from which to verify actual access, version, passage, or data.

Therefore the score can reward:

- a plausible API/database name with no inspectable query result;
- the intended source named in the prompt or suggested steps;
- a real but wrong-version document;
- an authoritative organization whose cited page does not entail the number;
- a source mention copied from the system instruction; or
- a correct URL attached to a value derived elsewhere.

It can also penalize a correctly tool-grounded result whose final prose omits an explicit citation. This is useful **source-attribution compliance**, not source validity. At minimum, existence, authority, version, valid time, access, passage entailment, transformation lineage, and citation presentation need separate observations.

### Three judges and median aggregation are not calibration

GPT-5-mini, Gemini-3.1-Flash-Lite, and DeepSeek V3.2 separately score each rubric and the median is used (Section 5.2, pp. 5–6). Provider diversity and natural-language justifications are useful robustness measures.

Appendix A.12 is called a “judge attribution sanity check,” not a validity study. For the 139 questions where Gemini-3.1-Pro ties or wins on median accuracy, it counts which judge supplies the median-relevant score and tie regimes. At least two judges agree in 86.33% of those selected panels (pp. 19–20). This shows panel mechanics, not accuracy:

- selection conditions on Gemini's judged win;
- agreement can be shared error against the same authored reference;
- the unit mixes tasks and score granularities;
- no independent expert labels, expert-expert variability, per-dimension confusion matrix, calibration curve, or adjudication are provided;
- median aggregation hides magnitude and direction of disagreement; and
- evaluated GPT/DeepSeek model families overlap judge families, leaving possible self/family interactions.

The paper's phrase “calibrated to specific quality requirements” is best read as rubric conditioning, not empirical calibration.

### Aggregation, confidence intervals, and failure handling

The paper equal-weights each category × difficulty cell, reports each dimension separately, and supplies confidence intervals (Section 5.3, p. 6). Cell balancing avoids dominance by larger classes, but defines a synthetic target population of nine equally weighted strata. It is not an energy-workload distribution and should be labeled as such.

The confidence-interval method is not stated: no bootstrap unit, repeated-run component, cluster structure, finite-population interpretation, or missingness handling appears. One task can have paired prompt variants; tasks can share markets, documents, databases, and author templates; and one run per model-task cannot estimate trajectory stochasticity. Temperature zero does not remove provider nondeterminism, mutable evidence, retries, or service variation.

“Failure” is restricted to max iterations, context-window limit, missing final response, and clarification request. Incorrect or poorly sourced answers are not failures (Section 5.3, p. 6). This is a valid terminal-completion metric but should not be called task failure without qualification. In the current release runner, `success=True` means a nonempty final answer was emitted; the static trace audit found 424/432 such terminal successes despite 40 failed-tool observations. Terminal completion, tool/environment validity, and substantive correctness must remain separate.

## Evidence and results interpretation

### Main descriptive results

Table 1 reports answer accuracy from 0.38 to 0.62, approach from 3.39 to 3.94, source validity from 2.16 to 4.02, failure from 0.8% to 20.2%, and differing token/tool/cost profiles (pp. 6–7). Gemini-3.1-Pro has the highest answer score; GPT-5.2 has the highest source score; Claude Sonnet 4.6 has the highest approach score in the table. Quant tasks show substantially higher terminal-failure rates for DeepSeek V3.2 and Kimi-K2.5 (Table A.7, p. 19).

These data support descriptive configured-system profiles on the authors' instrument. They do not support several stronger interpretations:

- **“38% improvement margin.”** `1 − 0.62` is distance from a perfect rubric score, not an empirically attainable improvement, domain-expertise effect, or professional-readiness gap.
- **“Planning–execution gap.”** Comparing a 1–5 judge score with a 0–1 answer score after converting 3.39/5 to 68% assumes commensurable, calibrated scales. The two dimensions have different raters/prompts and unknown validity.
- **Context-window causation.** Models with high failure rates also differ in provider, scaffold adaptation, output behavior, token use, tool interactions, and hidden service settings. Qwen is a counterexample noted by the paper. No controlled context-window intervention identifies the cause.
- **Source attribution not emergent.** The paper-time prompt is unclear and the released prompt explicitly mandates citations. Low citation scores may still be informative, but “emergent” is treatment-dependent.
- **Token/cost efficiency.** Average token fields are enormous and provider accounting/caching differs. The text itself inconsistently describes DeepSeek/Kimi token averages (Table 1 gives 491k/453k; prose gives 494k/420k). No uncertainty or quality-adjusted cost frontier is reported.

### Source-explicit pairs

Table 2 compares 61 source-explicit questions with 61 counterpart prompts across seven models. Answer differences are small and mixed; source scores are higher in every displayed with-source condition (pp. 8, 20–21).

The strongest conclusion is that naming a source increases a judge score that directly rewards source inclusion/alignment. This may be useful scaffolding evidence, but it is partly criterion-proximal: the intervention supplies the cue used by the source grader. The paper does not report item-paired differences, paired uncertainty, prompt-pair semantic equivalence review, order/randomization, source-access success, or whether the answer/source judge was blinded to condition. Because source-explicit and source-implicit prompts can cause different search exposure and may execute at different times, the result is not a clean estimate of domain knowledge or source-discovery ability.

### Tool removal

Table 3 compares with/without selected domain tools on 30 “most challenging” Medium/Hard tasks, reporting higher answer scores with tools for all seven models (pp. 8–9). This is stronger than an uncontrolled leaderboard difference, but still under-specified:

- selection is outcome/difficulty conditioned rather than a predeclared representative subset;
- the exact retained and removed tools, replacement affordances, execution times, model attempts, and evidence snapshots are not provided;
- some questions explicitly require a named internal database, making tool removal a construct-support withdrawal rather than merely removing assistance;
- live data/search can change between arms;
- no paired trial ledger, invalid-environment disposition, multiplicity policy, or repeated-run uncertainty is reported; and
- tool availability does not identify whether the gain came from data access, better schema cues, calculator behavior, or answer-bearing tool output.

The result supports package efficacy on a selected task set, not a general causal effect of “domain tooling” or proof that the tool's outputs were professionally correct.

## Release audit

### What is inspectable

The archive provides 74 Python files, a typed agent/tool framework, Docker sandbox, tool implementations, runner/configuration, 188-row task CSV, and 432 complete JSON traces. The static audit found:

- 12 model directories × 36 question IDs;
- trace timestamps from 11–21 June 2026;
- 424 terminal successes and 8 terminal failures;
- 5,071 tool calls and 40 failed-tool observations;
- 164,201,627 recorded total tokens, median 202,969 per trace, range 17,106–9,220,740; and
- raw question, final answer, tool arguments/outputs, timing, tokens, and metadata.

This is useful execution evidence, but it is a different study artifact. The twelve released models include GPT-5.5, GPT-5.4-mini, Claude Opus 4.8, Sonnet 4.6, DeepSeek v4 variants, Kimi 2.7 Code, and others. The paper evaluates GPT-5.2, GPT-5-mini, Gemini-3.1-Pro, Sonnet 4.6, Kimi-K2.5, Qwen3-Max-Thinking, and DeepSeek-V3.2. Only Sonnet 4.6 overlaps by displayed version. No trace-to-paper-table mapping is possible.

### Trace/task drift

Of 432 traces, 396 queries exactly match the current CSV. The 36 nonmatches are twelve traces each for q115, q190, and q194. Q115 differs only by whitespace. Q190 and q194 materially omit current-CSV instructions to exclude classes without demand charges and include adjustment rates. Thus even within one archive, ID does not guarantee prompt identity. A benchmark must hash the exact task text and component bundle in every trial rather than join by mutable integer ID.

### Grading and paper reproduction are absent

README lines 128–136 tell users to run `scripts/run_eval.py --config configs/eval_config.yaml`. Neither file exists. There is no released grading code, reference-answer table, expected-attribute table, tolerance table, suggested approaches, judge outputs, adjudication, paper result file, or analysis script. The repository therefore cannot reproduce Approach, Accuracy/Attribute, Source Validity, confidence intervals, source-pair tables, tool-ablation tables, or failure analysis.

The archive also cannot recreate its own released traces from shipped code/data alone because the database package and data are external and the RAG implementation/corpus is absent. API credentials, entitlements, mutable search/data services, model endpoints, and environment snapshots add further barriers.

### Reproducibility and operational realism

**Inspectability is moderate; paper reproducibility is weak.** The immutable full paper, exact post-v1 archive, hashes, prompt-only task subset, code, sandbox, and complete later traces are preserved. The release is sufficient to study current runner behavior and examples of live-tool trajectories. It is insufficient to reconstruct the paper instrument, seven configurations, evidence exposure, references, scores, uncertainty, or comparisons.

Operational realism is mixed. Positive features include real market/regulatory terminology, heterogeneous tools, multi-step retrieval/calculation, raw traces, error observations, source requirements, and substantial token/tool burdens. Limiting features include one-shot decontextualized prompts, no stakeholder clarification, no professional artifact acceptance, no decision consequence, mutable APIs without evidence receipts, authored rather than empirically validated thresholds, missing private evaluation materials, and a simplified quantitative model.

## Unique insight: evidence needs two clocks and one receipt chain

EnergyEvals' key design opportunity is not merely “use live tools.” It is to distinguish **event/source valid time** from **system transaction time** and bind both to a receipt chain.

For each material claim:

```text
requirement_valid_at
source_effective_from / source_effective_to
source_retrieved_at
provider_observed_at
agent_accessed_at
transformation_executed_at
answer_committed_at
reference_adjudicated_at
score_computed_at
```

Then preserve:

```text
source canonical identity + version/hash
→ exact query/request + entitlement/environment
→ response identity/hash + missing/error state
→ cited passage/row + authority/scope
→ extraction with unit/period/entity
→ transformation/model hash + assumptions + dependencies
→ output + uncertainty
→ grader evidence view + verdict
```

This resolves failures that a single source-validity score collapses:

- the correct source was unavailable at run time;
- an agent accessed an old but then-valid version;
- a reference silently uses a later correction;
- the URL is authoritative but the passage does not entail the claim;
- the data are right but transformed under the wrong unit/time zone;
- the analysis is internally correct under an inappropriate model;
- the final citation is plausible but was never accessed;
- the source changed between treatment arms;
- the grader lacked the raw evidence and guessed plausibility; or
- a correct historical claim is judged against a current mutable page.

The second insight is that **live evidence turns benchmark operation into part of the construct**. Provider entitlements, API uptime, database revision, search cache/livecrawl, run order, retries, and reference refresh are not incidental infrastructure. They determine what evidence existed for the agent and therefore which capability claim a score can support.

## Claim ladder for EnergyEvals-like benchmarks

| Rung | Evidence required | What EnergyEvals currently provides | Claim ceiling |
|---|---|---|---|
| 1. Authored task | immutable prompt, category, authoring record | paper descriptions; partial prompt release | task exists and was authored |
| 2. Configured run | exact task hash, model/scaffold/tool/environment/feedback identity, valid trace | rich later traces; incomplete paper-run identity | one configured system produced one trace |
| 3. Source-time validity | canonical source/version/hash, valid interval, retrieval receipt, authority and entailment | mutable tool outputs; no full receipts/reference snapshots | not established |
| 4. Analytical correctness | typed extraction, model/formula, dependencies, assumptions, tolerances, independent contrasts | hidden authored ground truths; simplified released tool code | agreement with authored reference at most |
| 5. Expert acceptance | qualified independent reviewers, alternatives, agreement/adjudication, artifact review | author qualification summary; unspecified manual review | not established |
| 6. Professional utility | intended user/decision, usability, timeliness, consequence, cost | no stakeholder use | not established |
| 7. Production fitness | repeated reliability, service/error envelope, monitoring, security, rollback | one reported run; partial sandbox/error traces | not established |
| 8. Readiness | validity argument tied to use, losses, safety, governance, field evidence | absent | not established |

No rung inherits the next. In particular, a live API call is not source-time validity; a judge/reference match is not expert acceptance; and expert authorship is not production readiness.

## Comparison with adjacent reviewed evidence

- **ClawArena** explicitly models staged evidence and temporal supersession but relies on author-declared hidden truth and answer-bearing feedback. EnergyEvals uses genuinely mutable services yet fails to encode claim-level valid time. Together they show that temporal realism requires explicit state transitions *and* source authority/receipt identity.
- **BigFinanceBench** time-anchors public-source questions and decomposes derivations, but its judges can credit narration without source proof. EnergyEvals has richer raw tool observations yet its source judge does not receive them. Both need proof-carrying source→extraction→transformation dependencies.
- **DORA** compiles one expert-authored analytical path into typed endpoints over real disaster data. EnergyEvals similarly treats suggested approaches and quantitative references as ground truth without alternative-path or consequence validation. Real data and domain vocabulary do not validate professional use.
- **OncoRounds** separates evidence acquisition from final decisions but confounds inquiry with parser/feedback policy. EnergyEvals exposes retrieval actions, yet does not distinguish availability, attempted access, successful receipt, adoption, and source-time correctness. Both require explicit intervention and feedback firewalls.
- **Performance-optimization reliability** shows that an executable criterion can fail to transport across environments and repeated measurements. EnergyEvals' live APIs, search index, database, solver, and provider stack make the same principle more acute: criterion and evidence margins must be tested over a declared operating envelope.
- **Existing `skill-bench` machinery** already has homes for source authority/valid time, evidence views, retrieval receipts, configured-system components, invalid-environment outcomes, task health, metric specifications, validity arguments, artifact admissibility, and expert participation. A domain-specific EnergyEvals schema would duplicate these contracts.

## Limitations and validity threats

1. **No task-population frame.** The 243 prompts are purposive and cannot estimate prevalence across energy work.
2. **Expert authority is not item-linked.** Combined years and employers do not identify who can authorize each market, tariff, modeling, or decision claim.
3. **No independent authoring reliability.** Author/reviewer counts, edits, agreement, adjudication, and unresolved disagreement are absent.
4. **Difficulty is unvalidated.** Easy/Medium/Hard are design labels without expert time, item-response, or empirical discrimination evidence.
5. **Corpus counts conflict.** Paper 243, Appendix 212, and release 188 are unreconciled.
6. **Release categories differ.** Data/Knowledge fall from 107/86 in the paper to 74/64 in the release; Quant remains 50.
7. **IDs do not identify immutable tasks.** IDs extend beyond the paper range, and two traced tariff prompts differ substantively from current CSV text.
8. **Ground truths are withheld.** Expected answers, attributes, steps, tolerances, source references, and review logs are unavailable.
9. **“Latest” is not anchored.** Two release prompts request latest documents without an as-of date or version policy.
10. **Historical dates do not freeze evidence.** Corrected market data and revised documents can change after the represented period.
11. **Live services are not synchronized.** Search/API/database exposure may differ by model, condition, retry, and date.
12. **Retrieval receipts are incomplete.** No canonical content hashes, provider-index snapshots, response headers, correction state, or immutable source pack.
13. **Database/RAG are not released.** Central paper tools and corpora cannot be recreated from the archive.
14. **Paper-run config is missing.** Shipped config and prompt are not the seven-model manuscript manifest.
15. **Reasoning comparability is weak.** “Low” is provider-specific, while open models list N/A; context/tokenization/tool APIs differ.
16. **One run is not reliability.** Temperature zero does not establish deterministic outcomes or mutable-evidence stability.
17. **Suggested approach is one witness.** No accepted alternative path or false-rejection calibration validates approach grading.
18. **Approach anchors are uncalibrated.** “Expert-like” 1–5 scores lack expert labels and behavioral standards.
19. **Reference validity is unobserved.** Correctness is relative to hidden authored answers, not independently source-audited truth.
20. **Attributes may be dependent/incomplete.** Up to five LLM-extracted attributes can omit critical conditions or double-count shared evidence.
21. **Tolerances lack decision basis.** ±2 and ±10% examples are not linked to item consequence or professional acceptance.
22. **Source grader lacks source evidence.** It sees answer and suggested steps, not raw receipts or trace.
23. **Source score conflates distinct predicates.** Citation inclusion, relevance, authority, version, access, entailment, and freshness are not separated.
24. **Internal-source equivalence is assumed.** The judge prompt tells the model to accept internal databases as authoritative without provenance inspection.
25. **Citation cue is treatment-proximal.** Source-explicit prompts directly supply information rewarded by source scoring.
26. **Three-judge median is not validation.** Agreement/tie attribution cannot estimate correctness without independent labels.
27. **Judge family interactions remain.** Evaluated and judge model families overlap.
28. **Confidence intervals are under-specified.** Unit, clustering, repeated-run variance, and missingness are not documented.
29. **Class balancing defines a synthetic population.** Equal category-difficulty weighting is not a workload distribution.
30. **Failure rate means terminal failure only.** Incorrect, unsupported, or unsafe outputs can count as completed.
31. **Tool ablation is selected and exposure-sensitive.** Thirty hardest tasks, mutable evidence, and unspecified run matching limit causal interpretation.
32. **Quantitative tool encodes one modeling policy.** Simplifying assumptions and solver acceptance are not professional validity.
33. **No artifact acceptance or decision consequence.** Answers are not reviewed in a downstream analyst/client/regulatory workflow.
34. **No production operating evidence.** Service reliability, drift, security, monitoring, repair, and rollback are not evaluated.
35. **Release traces are a different panel.** Twelve later model configurations cannot reproduce the seven-model paper tables.
36. **Released trace subset conflicts.** Archive has 36 question IDs, not the stated 30.
37. **Evaluation implementation is absent.** README references nonexistent grading script/config; raw grades and analysis are unavailable.
38. **Paper/release timing does not prove identity.** The sole commit postdates v1 and visibly contains evolved prompts/config/models.

## Transfer to `skill-bench`: concrete changes

1. **Require dual-time source records.** Every source-dependent requirement/claim should record retrieval/transaction time and represented/effective valid time, plus supersession/correction rules.
2. **Hash the exact evaluation form per trial.** Bind task text, source pack/live-source policy, reference, rubric, tool schemas, grader, feedback, environment, and metric versions; never join by integer ID alone.
3. **Use typed retrieval receipts.** Preserve request, provider/tool version, entitlement, response status, headers where available, content hash, source canonical ID/version, observed time, valid interval, and missing/error state.
4. **Separate source predicates.** Score existence, access, authority, scope, valid time, passage entailment, extraction accuracy, transformation lineage, and citation presentation independently.
5. **Make live-source exposure a treatment record.** Capture run order, provider index/cache/livecrawl policy, database snapshot, API revision, retries, and whether compared arms saw equivalent evidence.
6. **Version quantitative model witnesses.** Store equations, assumptions, units, solver/version/status, input/output hashes, sensitivity tests, and accepted alternative models; label simplified tools as benchmark interventions.
7. **Treat expert approaches as witnesses.** Admit reviewed alternative paths and partial orders; add unsafe/insufficient contrasts rather than rewarding similarity to one sequence.
8. **Calibrate graders on proof-carrying contrasts.** Include plausible citation without access, right source/wrong version, right URL/non-entailing passage, right value/wrong unit, correct alternative method, stale reference, tool outage, and corrected-data cases.
9. **Report a claim ladder, not one professional score.** Keep authored-task conformance, source-time validity, analytical correctness, expert acceptance, utility, production fitness, and readiness separate.
10. **Stratify invalidity and missingness.** Distinguish agent substantive error, tool unavailable, provider failure, evidence drift, reference defect, grader insufficiency, and terminal nonresponse.
11. **Estimate clustered/repeated uncertainty.** Repeat equivalent trials, cluster by task/source/document/market/template, and preserve paired source/tool comparisons rather than only cell-balanced marginal CIs.
12. **Add release conformance gates.** Paper form count, release form count, trace count, task hashes, model/run manifest, grade count, and table reproduction must reconcile before a result is called reproducible.
13. **Use existing contracts.** These are refinements to current evidence-chain, configured-system, task-health, metric, validity, artifact-view, and expert-authority machinery; no energy-specific subsystem is justified.

## Action items for repository

- [x] Read the complete immutable 22-page v1 PDF/text and record section/page evidence.
- [x] Inspect and computationally audit the exact official post-v1 archive without paid/live API calls.
- [x] Preserve an executable audit summary at `data/sources/releases/2606.26346v1-energyevals/REVIEW_RELEASE_AUDIT.json`.
- [x] Reconcile the count issue as an **unresolved form-conformance failure**: characterize 243/212/188 precisely rather than inventing an attrition explanation.
- [x] Separate paper evidence, release evidence, and `skill-bench` adaptations.
- [x] Compare against ClawArena, BigFinanceBench, DORA, OncoRounds, and performance-criterion transport evidence.
- [x] Add no duplicate queue task. Existing source-time/evidence-receipt, configured-system, metric, task-health, validity, and release-conformance work already covers the implied build requirements.

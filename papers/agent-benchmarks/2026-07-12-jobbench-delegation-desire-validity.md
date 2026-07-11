# Paper and Release Review: JobBench — Delegation Desire Is a Selection Signal, Not an Outcome

- **Paper:** https://arxiv.org/abs/2605.26329v1
- **Authors:** Yuetai Li, Yichen Feng, Zhangchen Xu, Zixian Ma, Kaiyuan Zheng, Fengqing Jiang, Xinghua Sun, Rulin Shao, Zichen Chen, Yue Huang, Xinyang Han, Brian Lee, Kayla Xu, Shenglai Zeng, Hang Hua, Xiangliang Zhang, Basel Alomair, Ranjay Krishna, Luke Zettlemoyer, Pang Wei Koh, Bhaskar Ramasubramanian, Luyao Niu, Xiang Yue, and Radha Poovendran
- **Date read:** 2026-07-12
- **Source:** immutable arXiv v1, submitted 2026-05-25
- **Tags:** occupational-sampling, delegation-preference, expert-authoring, chained-rubrics, artifact-evaluation, augmentation-validity
- **Local PDF:** `data/papers/pdfs/2605.26329v1-jobbench-delegation-desire-validity.pdf` (38 pages; SHA-256 `e953d19425eb92a95cb07a43b4efdd37fada966b4ec76ff57ae633cf15261d38`)
- **Local text:** `data/papers/text/2605.26329v1-jobbench-delegation-desire-validity.txt` (SHA-256 `860a961fbc51463e23f98725b94d7ba72afd408bdc8d375a864d02e76603af4f`)
- **Official project page:** https://job-bench.github.io/; local capture and provenance at `data/sources/releases/2605.26329v1-jobbench/provenance.json`
- **Official evaluation release:** https://github.com/Job-Bench/job-bench-eval, pinned at post-v1 commit `007b80648929131bd6aa8d01321360217f0f379e`; extracted under `data/sources/releases/2605.26329v1-jobbench/release/`
- **Official dataset:** https://huggingface.co/datasets/JobBench/job-bench, pinned at revision `934d4c93542c24926d0957ed6feecd6bbd922c41`; local metadata tables `tasks.parquet`, `easy.parquet`, and `README.md`. Binary reference files were not mirrored.

## One-sentence contribution

JobBench uses prior worker ratings of O*NET duties as a demand-side task-selection signal, turns selected duties into 130 file-rich occupational task packages with all-or-nothing rubric chains, and evaluates 36 model–scaffold configurations—but its score supports configured-agent performance on selected packages, not worker satisfaction, productivity, consent, occupational representativeness, or beneficial augmentation.

## Why this matters for skill-bench

This review advances charter objectives A, B, D, and F. JobBench contributes a genuinely different denominator from GDPval: not merely economically valuable work, but duties workers report wanting AI to perform. That distinction can improve portfolio construction by asking **which work is worth transferring from the worker's perspective** before asking whether an agent can perform it.

The concrete evidence is the full immutable paper, all 128 released metadata/rubric records, and the pinned post-paper runner/judge implementation. This is comparative expansion, not a proposal to narrow `skill-bench` to U.S. occupations. Useful completion means retaining delegation preference as one typed demand signal while refusing the paper's unsupported jump from preference-selected benchmark performance to satisfaction, productivity, enhancement, or empowerment.

## Research question and claim ladder

The defensible research question is: **Can worker-reported delegation preferences be used to select occupational agent tasks, and how do configured systems perform on benchmark packages derived from those duties?**

The paper often advances a longer chain (abstract; pp. 1–4, 9, 38):

```text
WorkBank duty-level rating
→ occupation/duty selection
→ expert-authored benchmark package
→ rubric-chain score
→ ability on work workers want delegated
→ successful delegation
→ increased satisfaction and productivity
→ worker enhancement rather than replacement
```

Only the first four links are instantiated. Each later link requires new evidence:

- a historical preference rating is not present consent to use an agent;
- a duty label does not establish that the authored package is a representative realization;
- isolated output quality does not establish feasible workflow delegation;
- delegation feasibility does not establish net benefit after review and correction;
- net benefit does not establish satisfaction, empowerment, or absence of displacement.

The paper's own limitations correctly say the dataset is not deployment validation and should not support worker replacement, professional judgment, or unsupervised high-stakes use (p. 15). That boundary conflicts with stronger contribution language claiming leaderboard progress “maps onto” satisfaction and productivity (p. 2) and that targeting these duties “lifts” both (p. 3).

## Methodology and system

### 1. Demand and occupation frame

JobBench starts from WorkBank, where more than 1,500 U.S. workers rated O*NET duties on a 1–5 automation-delegation scale. The authors merge occupation-level entries with 2024 OEWS total wages, retain occupations with average desire above 3, rank by economic exposure, and apply feasibility filters requiring duties to be digitalizable, evaluable, supportable, and above 3 in desire (paper pp. 2–4). The realized benchmark spans 35 occupations in 10 SOC groups, but is concentrated in business/financial, office/administrative, computing, and engineering work (pp. 3–4, 17).

This is a purposive intersection of preference, wages, and benchmarkability—not a sample of workers, duties, occupations, or desired automation. The paper does not report:

- WorkBank respondent counts or uncertainty for each selected duty;
- how occupation-level “average willingness” is formed from duty and worker ratings;
- disagreement, multimodality, seniority, workplace, demographic, or collaboration-mode variation;
- exact ranking and tie rules;
- how many occupations/duties each filter removes;
- whether the selected task package was shown back to the workers whose rating motivated it.

Economic exposure therefore remains embedded in the supposedly alternative frame, while feasibility removes physical, interactive, proprietary, and longitudinal duties. The method identifies **high-rated, high-wage, benchmarkable document work**, not “what humans actually want” without qualification.

### 2. Expert recruitment and transformation

Domain annotators are recruited through Prolific and Upwork. The paper reports an average 26.5 distinct Prolific participant IDs per occupation; Upwork candidates are found by keyword and require greater than 90% job success (p. 4). Experts complete structured onboarding and use an annotation platform that integrates and logs AI assistance. Annotators draft task sketches from high-desire duties, specifying scenario, reasoning challenges, deliverables, and standards; AI expands these into reference workspaces, self-contained queries, and rubric chains (pp. 4–5).

This process is under-specified at exactly the authority handoff that matters. No occupational tenure threshold, credential check, worker/annotator overlap, role counts, assignment counts, pay rates, hours, acceptance rate, contributor-level clustering, or independent review structure is reported. A Prolific participant ID and an Upwork success score are recruitment attributes, not evidence of authority over every embedded legal, regulatory, technical, or professional judgment. The ethics section reports voluntary participation, research-use consent, intended fair compensation by occupational wage standards, and no released identifiers (p. 15), but not actual compensation, license/ownership terms, withdrawal boundaries after release, or consent to the augmentation claims.

Most importantly, the transformation is:

```text
surveyed worker duty preference
→ researcher occupation/duty filters
→ different recruited annotator's sketch
→ AI-expanded scenario/files/rubrics
→ annotator refinement
→ model-conditioned solve filter
```

“Expert grounded” at the first and third nodes does not make the intervening transformations preference-preserving. No worker validates that the final package is the work they wanted delegated, that its retained human responsibilities are appropriate, or that successful completion would improve their work.

### 3. Task construction and quality filtering

The paper describes 65 Main and 65 Easy tasks, 502 reference files in 17 formats, 4,631 binary criteria, and a mean 35.6 criteria per task (pp. 3–4). Main tasks use heterogeneous and sometimes conflicting local/public sources; 51.7% of Main reference files are real public records and the rest synthetic, while Easy files are all described as real-world (p. 3). Main can require web retrieval; Easy has fewer reasoning challenges and no web-search evidence (pp. 4, 7).

Candidates pass three gates (pp. 4–5):

1. an automated audit for instruction/file consistency, plausibility, and rubric correctness;
2. annotator polishing and positive feedback;
3. multiple-agent solve trials, retaining only tasks where the **union** of rubrics passed across all runs exceeds 90%.

Seventy-one percent of candidates survive; the accepted corpus has a 95.4% union pass rate. This is evidence that sampled agents can elicit most criteria somewhere, not that one coherent solution exists, that alternatives are complete, or that graders are sound. It also conditions task admission on the evaluated systems' outcomes. The benchmark is consequently “healthy-first”: impossible, grader-broken, highly discriminating, or systematically difficult requirements are preferentially removed. Because union coverage combines unspecified agents and samples, it cannot establish an attainable joint path through each task.

The four full examples (pp. 18–35) demonstrate useful authoring machinery: heterogeneous evidence, explicit authority hierarchies, contradictions, calculations, hidden failure signatures, multiple artifact formats, and criteria tied to facts or consequences. They also expose risks. The reporter rubric contains an apparent internal contradiction: it says 2024 Hartford periods marked “Yes” in an `Action_Level_Exceedance` column should be reflected under the current 15 ppb standard, immediately after listing those values as 11.8 and 10.4 ppb (pp. 19–20). This illustrates why claimed automated consistency audits and union solvability are not substitutes for source-to-check semantic audits.

### 4. Evaluation and aggregation

The paper reports 36 model–scaffold configurations across Claude Code 2.1.2, Codex CLI 0.125.0, OpenCode 1.14.18, and OpenClaw 2026.3.8, with maximum supported reasoning effort, default sampling, 60-minute timeout, and nominally isolated temporary workspaces (pp. 5–7, 36). Each rubric is an AND-chain: it receives its weight only if every criterion passes; task scores normalize passed rubric weights, and the leaderboard macro-averages tasks. The best reported configuration is Claude Opus 4.7 under Claude Code at 45.9% (pp. 5–6).

The design properly treats scaffold as consequential and shows same-model differences of several points (p. 7). But the paper provides no repeated-attempt uncertainty for leaderboard cells, task/occupation-clustered intervals, missing/invalid-run policy, or matched factorial coverage. Defaults, tool implementations, browsing, context compression, and file affordances differ across scaffolds, so rows are configured packages rather than model estimates.

Equal task macro-averaging is not delegation-demand weighting. A one-point difference has the same weight regardless of worker rating, prevalence, time burden, consequence, occupational population, or disagreement. The occupation categories also contain only one to three Main tasks each (paper p. 17; confirmed in the release), yet Figure 7 uses per-occupation mean capability and a median split to define “Sweet Zone” and “R&D” quadrants (pp. 8–9). Those labels are unstable task-sample summaries, not occupational capability estimates.

The GDPval comparison is not controlled: JobBench scores are rubric-chain percentages, while cited GDPval scores are external win+tie rates against expert artifacts; task sets, graders, harnesses, models, dates, and constructs differ (pp. 6–7). Higher runtime and lower scores do not isolate “professional reasoning” difficulty.

### 5. LLM judge

The default judge is Grok 4.1 Fast; Opus 4.5 is a stronger reference. The paper says configuration-level scores differ by only 0.1–0.7 points and costs fall from roughly $38–46 to about $2 per full run (pp. 6–8). This is aggregate score proximity, not criterion-level agreement, calibration, equivalence, or validity. Opposing errors can cancel in the aggregate, and no human judgments, confusion matrix, task-level distribution, confidence interval, or occupation slice is reported.

The pinned post-v1 judge (`release/eval/judge.py`) extracts text from files and asks the model to score one rubric at a time. Important operational limits include:

- spreadsheet extraction reads displayed cell values through pandas, not formula lineage, formatting, charts, hidden state, or workbook semantics;
- DOCX extraction substitutes embedded-image placeholders in text, although a separate heuristic may attach images;
- PDF grading relies on extracted text unless visual-keyword heuristics trigger image attachment;
- SQLite is truncated to 500 rows per table;
- non-SQLite files are truncated to 200,000 characters;
- visual grading is triggered by a lexical regex and capped at eight deduplicated images;
- unsupported/broken extraction emits error strings into the judge evidence view rather than establishing artifact validity.

The grader can therefore award semantic content while missing professional artifact structure or fail because its evidence view is incomplete. The release records reasons and evidence, which is useful, but does not expose paper-time judgments or establish the reported aggregate agreement.

### 6. Execution isolation

The paper says agents receive file access only to a temporary workspace (p. 6). The pinned Codex runner instead invokes `--dangerously-bypass-approvals-and-sandbox` and relies on a prompt prohibition plus working-directory placement (`release/eval/run_benchmark_codex_cli.sh`, lines 391–415). A copied `/tmp` directory is not a filesystem or network sandbox. The runner explicitly allows online search, and no host-read canary, network policy, clean HOME, secret isolation, or private-rubric firewall appears in that path. This post-v1 code cannot prove paper-time execution, but it does falsify any assumption that the current official implementation mechanically enforces the paper's “only” boundary for Codex.

## Release inspection

The pinned Hugging Face revision postdates v1. Its two metadata tables are compact and auditable:

| Split | Rows | Occupations | Rubrics | Binary criteria | Mean criteria/task | Starter-file locators |
|---|---:|---:|---:|---:|---:|---:|
| Main | 65 | 35 | 569 | 2,066 | 31.78 | 268 |
| Easy | 63 | 35 | 710 | 2,510 | 39.84 | 226 |
| **Total** | **128** | **35** | **1,279** | **4,576** | **35.75** | **494** |

The paper reports 65 Easy tasks and 4,631 total criteria. The current release has 63 Easy tasks and 4,576 criteria—two tasks and 55 criteria fewer. The dataset card explicitly says 63 Easy tasks and warns Main/Easy are parallel selections, not one-to-one simplifications. The paper's Figure 4 comparison and “same occupation coverage” language (p. 7) should therefore not be reconstructed from the current release without a versioned paper-time manifest.

All 494 starter-file URLs in the parquet metadata use mutable `/resolve/main/` paths even though this review pins the dataset revision externally. Reproducible evaluation should rewrite them to revision-specific URLs or preserve object hashes. The local parquet files preserve prompts, rubric JSON, task cards, and file locators, but this review did not mirror or inspect all binary references and therefore makes no corpus-wide claim about file correctness, provenance, licensing, or synthetic/real labeling.

The release is MIT-licensed at the dataset-card level and the evaluation repository includes a license. However, a code/dataset license does not by itself establish redistribution rights for every incorporated public document or validate the sources' temporal authority.

## Evidence and claim boundaries

### Strongly supported

1. Delegation preference can be operationalized as one explicit task-portfolio selection signal rather than leaving benchmark demand implicit.
2. The authors built and released metadata for a broad, artifact-rich Main/Easy corpus spanning 35 selected U.S. occupations.
3. The task examples and release rubrics encode multi-source reconciliation, source authority, calculations, professional conventions, and multiple deliverables more richly than final-answer benchmarks.
4. Under the reported configured packages and rubric-judge protocol, systems obtain widely varying, sub-50% Main scores and scaffold choice is associated with material score differences.
5. The current release enables metadata/rubric audit and provides runnable adapters and a detailed judge implementation.

### Partially supported

- **Worker alignment:** WorkBank provides a real worker-reported signal, but the final packages are filtered and transformed by researchers, different annotators, AI expansion, and model-conditioned selection without preference-preservation validation.
- **Professional relevance:** occupational labels, recruited annotators, realistic formats, and detailed examples are content evidence, but no independent occupational-validity study, inter-expert reliability, downstream-use trial, or acceptability threshold is reported.
- **Judge efficiency:** aggregate proximity and cost estimates support a cheap scoring hypothesis, not criterion-level correctness or expert substitution.
- **Difficulty:** low scores and Main/Easy differences show difficulty under these instruments, but task content, web access, references, criteria, and split membership all differ.

### Not supported by v1

- that leaderboard progress increases worker satisfaction or productivity;
- that JobBench tasks represent what workers generally “actually want” delegated;
- that a worker's delegation preference constitutes consent, authority, or desire for autonomous execution;
- that the 35 occupations or one-to-three Main tasks per occupation support occupational capability estimates;
- that automation of the selected task would enhance rather than replace, deskill, monitor, or redistribute labor;
- that the rubric score measures professional acceptance, safe deployment, or readiness;
- that the released 63-task Easy split exactly reproduces the paper's 65-task Easy results;
- that Grok's aggregate score proximity establishes judge reliability.

## Unique insight

JobBench's valuable idea is not “human will” as a scalar. It is that benchmark portfolios need a typed **demand provenance chain** independent of capability and economic value:

```text
who wants help
× with which bounded activity
× under which collaboration mode
× for what reason
× with what retained authority
× at what time/context
× transformed into which benchmark package
```

A delegation rating answers only part of the first two fields. The transformation from an O*NET duty to an agent task can expand scope from mechanical assistance to judgment-bearing autonomous production. For example, “check reference materials” becomes an editorial package with causal framing; a legal research duty becomes settlement strategy; intrusion monitoring becomes deployable hardened configurations. Those may be useful tests, but the worker-demand premise must be revalidated after scope expansion.

The second unique lesson is that **task selection, treatment desirability, and outcome benefit are different estimands**. Preference can rank candidate tasks. It cannot replace a human-plus-agent trial measuring review time, correction, error severity, retained control, satisfaction, and downstream effects.

## Limitations

1. WorkBank sampling, duty-level uncertainty, subgroup disagreement, and collaboration-mode data are not carried into the benchmark.
2. The occupation filter combines desire with aggregate wages and digital/evaluable feasibility, limiting the “human will” interpretation.
3. Final task packages are not validated by the original preference respondents.
4. Expert qualifications, role counts, task assignments, pay, hours, attrition, and agreement are largely absent.
5. AI-assisted expansion is logged but no transformation lineage or fidelity audit is reported.
6. Automated audit validity is unmeasured; at least one published example appears internally inconsistent.
7. Solve-trial admission creates outcome-conditioned, healthy-first task selection.
8. Union rubric coverage does not show a coherent jointly passing solution.
9. Main and Easy differ on several dimensions and are not matched item forms.
10. One-to-three Main tasks per occupation cannot estimate occupational performance distributions.
11. Macro-aggregation ignores preference strength, worker prevalence, task frequency, time, consequence, and disagreement.
12. No repeated-run, task-clustered, occupation-clustered, or selection-aware uncertainty is reported.
13. Configuration comparisons do not isolate model from scaffold/tool/default effects.
14. GDPval comparisons mix incompatible tasks, scores, graders, and harnesses.
15. Judge validation is aggregate, model-only, and lacks human criterion labels.
16. Current judge evidence views omit or truncate important structured and visual artifact state.
17. Current Codex runner disables sandboxing despite paper language about workspace-only access.
18. Web retrieval introduces mutable evidence and contamination risks without a pinned search protocol.
19. Current release differs from paper counts by two Easy tasks and 55 criteria.
20. Mutable `resolve/main` file URLs weaken exact reconstruction.
21. Model outputs, paper-time rubric judgments, run-level scores, invalid-run logs, and analysis code are not released.
22. No actual worker-plus-agent workflow is observed.
23. No satisfaction, productivity, job-quality, autonomy, displacement, or distributional outcome is measured.

## Reproducibility and operational realism

Reproducibility is stronger at the package-description layer than at the headline-result layer. The pinned metadata exposes all current prompts, task cards, and 4,576 criteria; the release exposes runner and judge logic. The paper includes four unusually detailed task/rubric examples and both prompts. These are substantial audit affordances.

The paper-time experiment remains incompletely reproducible because the current dataset differs from v1 counts; binary reference files were not version-bound in the paper; model outputs, per-run scores, trajectories, grader outputs, model parameters, invalid-run policy, and analysis tables are absent; proprietary model/scaffold versions are mutable; and current file URLs target `main`. The post-v1 release is evidence about the current implementation, not proof of what generated v1 results.

Operational realism is mixed. Multiple heterogeneous files, required searches, contradictions, structured outputs, and long artifact construction capture real burdens. Conversely, tasks are isolated, noninteractive, synthetic in part, stripped of live organizational state, and judged without downstream use. The benchmark models delegated **production of artifacts**, not the negotiation, review, correction, accountability, and consequences that determine whether delegation benefits workers.

## Transfer to skill-bench

### Retain

1. **Add demand provenance to portfolio design.** Record worker/expert desire separately from economic value, construct coverage, feasibility, and consequence.
2. **Use duty-to-package mappings.** Preserve the source duty, exact rating instrument, respondent population, desired collaboration mode, transformation steps, and final package scope.
3. **Encode chained consequences carefully.** AND-gates can prevent partial credit for unsupported conclusions when each criterion is independently valid and the chain represents a real professional dependency.
4. **Keep artifact-rich cross-source tasks.** JobBench's contradiction, authority, calculation, and deliverable patterns transfer across domains.
5. **Publish inspectable metadata while preserving secure evaluation roles.** Prompts/rubrics are excellent audit and calibration evidence but should trigger capability-task retirement or version transitions when exposed.

### Repair

1. **Separate five claims:** historical preference, present delegation consent, package fidelity, configured-agent capability, and realized worker benefit.
2. **Require post-transformation validation.** A domain contributor should verify that the final task preserves the desired delegated boundary and retained human decisions.
3. **Represent preference distributions.** Store respondent count, sampling frame, central tendency, dispersion, subgroup/context differences, date, and collaboration mode—not one occupation scalar.
4. **Predeclare assembly estimands.** Report equal-task capability separately from desire-weighted, frequency-weighted, consequence-weighted, and occupational estimates; do not infer the latter without sampling evidence.
5. **Replace union solvability with witness and contrast evidence.** Require at least one coherent complete path, planted negative cases, alternative-valid-path tests, grader defects, and selection-history records.
6. **Fail closed on evaluator evidence.** Structured files need authoritative views, formulas/state/render checks, pinned transforms, and explicit insufficient-evidence outcomes.
7. **Enforce the sandbox mechanically.** A prompt-only boundary with disabled sandboxing is not execution validity.
8. **Pin every source and release object.** Preserve exact dataset revision, per-file hashes, web retrieval date/index, and paper/release timing.

## Concrete next actions

1. **No new queue task.** Existing expert-participation, demand-provenance, task-projection, benchmark-bundle, artifact-admissibility, execution-validity, task-health, metric-monitoring, and validity-argument machinery already has homes for these requirements; adding another contract would duplicate current consolidation work.
2. **In the next cross-record consolidation, add a delegation-demand claim ladder:** preference observation → package-fidelity validation → present consent/authority → observed workflow uptake → measured worker outcome. Make unsupported upgrades machine-detectable where existing records allow.
3. **For the next consented pilot, elicit the desired collaboration boundary before authoring and re-approve it afterward.** Measure scope expansion between source duty and final task.
4. **Run an actual augmentation study before benefit language:** unaided versus agent-assisted work, with matched task forms, total worker time, review/correction, severe defects, retained decisions, satisfaction, and downstream acceptability.
5. **Treat the current JobBench release as a 128-task post-v1 instrument.** Do not use it to reproduce 130-task paper aggregates without the missing Easy tasks and an exact paper-time manifest.

## Action items

- [x] Read the complete immutable arXiv v1 paper and verify page/section claims against the local PDF extraction.
- [x] Pin and inspect the official post-v1 evaluation release.
- [x] Pin and parse both official dataset metadata tables (128 rows, 1,279 rubrics, 4,576 criteria).
- [x] Preserve the paper/release timing boundary and the 130-versus-128 discrepancy.
- [x] Separate delegation preference, consent, package validity, capability, worker benefit, and readiness.
- [x] Compare the task-selection claim boundary against GDPval without adding a duplicate schema task.
- [ ] Obtain a worker-validated, consented augmentation trial before making productivity, satisfaction, or empowerment claims.

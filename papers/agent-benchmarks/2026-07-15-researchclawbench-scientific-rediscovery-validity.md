# ResearchClawBench: target-paper anchoring is useful, but the released score observes report resemblance—not end-to-end scientific discovery

**Paper:** Wanghan Xu et al., *ResearchClawBench: A Benchmark for End-to-End Autonomous Scientific Research* (arXiv:2606.07591v5, 2026)  
**Primary source:** https://arxiv.org/abs/2606.07591v5  
**Official repository:** https://github.com/InternScience/ResearchClawBench  
**Official dataset:** https://huggingface.co/datasets/InternScience/ResearchClawBench  
**Date read:** 2026-07-15  
**Review status:** Deep review of the complete immutable v5 paper plus release audit of a later official GitHub commit and Hugging Face revision. The paper and release are not treated as contemporaneous.

## Evidence and provenance

- Immutable local PDF: `data/papers/pdfs/2606.07591v5-researchclawbench-autonomous-scientific-research.pdf` (73 pages; SHA-256 `30389c1af9d445b1031e25da797b9645809d39f6bcb5a17a12fcb037054e94ef`).
- Layout-preserving local text: `data/papers/text/2606.07591v5-researchclawbench-autonomous-scientific-research.txt` (SHA-256 `22ecb1789700eb813e9543688e82bf20180a83b2212547885d58b8c3e67f214a`). The full extraction was read through the task appendix and references.
- Earlier immutable versions were retained at `data/papers/pdfs/2606.07591v{1,2,3,4}-researchclawbench-autonomous-scientific-research.pdf` with corresponding text under `data/papers/text/`. The substantive redesign appeared mainly in v4; v5 is largely a figure/layout correction, not an independent replication.
- Release provenance: `data/sources/releases/2606.07591v5-researchclawbench/provenance.json`.
- Audited GitHub snapshot: `data/sources/releases/2606.07591v5-researchclawbench/InternScience-ResearchClawBench-6bfca04.zip` at commit `6bfca049f050cae559228e713cea61f9c86acc43`, committed 2026-07-15—12 days after v5. The archive SHA-256 is `898914913997463f655783e7ba1e2ac706eb8d456d1cba24889d62f8ce4a46ff`.
- The same provenance record pins Hugging Face revision `db5d2f4d9494e83c6f0ea0839b00f2b9c1ab66a4`, committed 2026-07-14. The GitHub release therefore verifies a maintained implementation, but cannot establish the exact code/data state used for the v5 experiments.

## One-sentence contribution

ResearchClawBench turns 40 published studies across ten scientific domains into open-workspace research assignments and introduces weighted, target-paper-derived text/image criteria, thereby making a valuable task substrate—but its implemented Reference-Anchored Discovery Score (RADS) judges only a final report and up to five generated images, so it cannot by itself support the paper's stronger claims about end-to-end execution, evidence credibility, professional research capacity, or discovery.

## Why this matters for `skill-bench`

The benchmark tackles the right hard problem: many useful knowledge-work outputs are open-ended, and exact-match endpoints discard the expert distinctions that matter. Its target-study → executable task → evidence package → weighted criteria pattern is directly relevant to converting tacit expertise into benchmark machinery.

The important lesson is not merely “use rubrics.” It is to preserve the full validity chain:

> source study → expert projection → participant-visible workspace → produced process/artifacts → criterion-specific observer → item score → aggregate → declared claim.

ResearchClawBench is strongest in the first three links and weakest at the observer-to-claim transition. The public implementation asks whether a report resembles expert-selected target artifacts. That is useful **reference-recovery evidence**. Calling the same number end-to-end discovery, credible scientific evidence, or professional capacity silently assumes that prose and figures faithfully reflect valid code, data use, experimental execution, novelty, and independent scientific verification. Those assumptions are neither checked by the scorer nor validated in the paper.

This advances charter objectives B, C, D, and F: explicit expert-derived primitives, executable knowledge-work tasks, validity-bounded scoring, and human-readable synthesis. It does not motivate narrowing `skill-bench` to science; science is a demanding case study for general source-to-artifact measurement.

## Research question and claim ladder

The paper asks whether coding agents can start from supplied scientific data and literature, autonomously analyze the problem, and produce a report that recovers or surpasses a reference paper. It makes claims at several levels that should remain separate:

1. **Package completion:** the configured agent creates a report in the required workspace.
2. **Reference-content recovery:** the report contains target-paper-derived findings or comparable figures.
3. **Valid execution:** code ran against authorized inputs and produced the claimed outputs.
4. **Scientific evidence quality:** methods, assumptions, statistics, robustness checks, and provenance make the conclusions credible.
5. **Novelty/discovery:** claims exceed the target and survive novelty search and independent verification.
6. **Professional research capacity:** performance transports to real research settings, collaboration, review, safety, and consequence.

The released grader directly observes mostly level 2. The paper's “RADS does not claim that every score above 50 is a validated new discovery” caveat is appropriate, but its subsequent statement that RADS measures professional capacity to generate credible scientific evidence still jumps over levels 3–6.

## Methodology and system

### Task construction

Experts select papers with clear questions, accessible data, and practical value; extract an executable research objective; collect data and related work; derive key target-paper artifacts into weighted criteria; package the task; and cross-check or rerun it. The suite contains exactly four tasks in each of Astronomy, Chemistry, Earth Science, Energy Science, Information Science, Life Science, Materials Science, Mathematics, Neuroscience, and Physics.

Each public task has:

- a free-text research objective in `task_info.json`;
- typed input files and descriptions under `data/`;
- multiple reference PDFs under `related_work/`;
- a hidden-at-runtime `target_study/paper.pdf`;
- `target_study/checklist.json` plus target images.

The runtime copies only `data/` and `related_work/` into the workspace, not `target_study/`. It asks the agent to create code, outputs, figures, and `report/report.md`.

### Evaluation

RADS uses criterion-level 0–100 judgments with 50 intended to mean target-paper parity. Criteria are text or image items. A GPT-5.1 judge selects an objective or subjective scoring mode, emits a score and short rationale per item, and the system computes the weighted mean. The paper reports one overall mean across 40 tasks for seven agent families, plus seventeen native LLMs run through ResearchHarness. Table 5 actually has eight autonomous configuration rows because it retains two EvoScientist versions.

The paper also reports cost/runtime associations, best-per-task “frontier” means, and an error taxonomy over 280 runs (seven configurations × 40 tasks). There is no uncertainty interval, repeated-trial reliability analysis, judge replication, human-score comparison, or inferential test for the main rankings in v5.

### Release audit: what is actually executable

The post-v5 GitHub snapshot contains 40 task packages and runnable setup/scoring code. Direct archive inspection found:

- 40 `task_info.json` records with 113 declared data entries;
- 40 checklists with 154 criteria total: 63 text and 91 image criteria;
- 3–8 criteria per task (21 tasks have only three);
- weights summing to exactly 1.0 for every task;
- all 91 target-image paths present;
- no exact SHA-256 duplicate between a task's target PDF and its related-work PDFs;
- no archived workspaces or raw paper-result traces beyond `.gitkeep` files;
- example ResearchHarness limits of 500 rounds, three hours, 131,072 input tokens, 16,384 output tokens, and one repeat per task.

The score implementation is materially narrower than the paper's verbal construct:

- text criteria receive the report, task instructions, criterion, and keywords—but not the target paper or an extracted target answer;
- image criteria receive the target image and at most the first five images found in the workspace;
- code, logs, tables, data lineage, command traces, and non-image output artifacts are not inspected;
- the report is therefore allowed to assert successful analyses without execution-backed verification;
- the judge chooses objective versus subjective mode dynamically rather than using an expert-declared item type;
- image files are not semantically matched to criteria, and excess images are truncated;
- the published release makes target papers, target images, and complete checklists downloadable, even though the runtime hides them.

The latter is not an implementation bug—the benchmark must be distributable—but it means public, search-enabled evaluation requires contamination controls, immutable split/version identity, and disclosure of target access. “Hidden during runtime” is not equivalent to unseen by the model, agent developer, search system, or prior trial.

## Evidence and findings

The empirical result is a credible descriptive snapshot of the tested configurations under this scorer: mean scores are low. Claude Code leads the autonomous table at 21.5; Claude-Opus-4.7 through ResearchHarness leads that table at 20.7. The paper's best-system-per-task frontier remains below 30. No system reaches the designed reference level on average. Error labels emphasize experimental-design mismatch, evidence mismatch, and missing scientific core.

These findings support three bounded conclusions:

1. **The task packages are difficult under the configured harnesses.** Low report/checklist scores across many systems make simple saturation unlikely.
2. **Scaffolding matters.** Different agent families around related base models produce differing outcomes, although uncontrolled budgets/tools prevent a pure scaffold effect.
3. **Failure is heterogeneous.** Domain and task-level variation makes one overall mean diagnostically insufficient.

They do **not** establish that 50 is empirically calibrated to target-paper equivalence. No human reproducer score distribution anchors 50; no blinded expert comparison tests whether reports scored near 50 are genuinely comparable; and no above-50 outputs are independently verified. The thresholds are semantic instructions to one judge, not validated measurement cut points.

Likewise, “frontier mean” is an oracle composite that selects a different system after observing each task. It describes complementarity in the tested result matrix, not the expected performance of a deployable system or selection policy.

## Unique insight

ResearchClawBench exposes a distinction that should become explicit in `skill-bench`: **a reference can play three incompatible roles**.

1. **Construction reference:** experts mine it to define the task and criteria.
2. **Judge evidence:** an evaluator compares submissions against it.
3. **participant-visible source:** the worker can legitimately consult it.

The same document cannot be called “hidden” without saying hidden from whom, at what stage, under which release/search conditions, and with what audit evidence. More importantly, a criterion derived from a reference is not itself enough evidence for “surpassing” the reference. To judge surpassing, the observer needs the actual baseline result, method assumptions, uncertainty, admissible comparison, and independent verification status.

This yields a general benchmark-design rule:

> Reference-anchored scoring must type both the reference role and the comparison relation. “Contains target-derived content,” “reproduces an execution-backed result,” “improves a declared metric under matched conditions,” and “produces independently validated novelty” are different checks and must not share one unqualified 0–100 axis.

That rule transfers beyond science to legal precedents, prior consulting deliverables, financial models, design exemplars, and software baselines.

## Reproducibility and operational realism

### What is reproducible

The official post-v5 snapshot is substantial: task inputs, related work, target papers, criteria, target figures, runner, judge prompt, agent presets, batch CLI, example budgets, and tests are inspectable. The runtime correctly separates target-study files from the generated workspace. This is much stronger than a paper-only leaderboard.

### What is not reproducible from the audited artifacts

The archive does not contain the raw workspaces, reports, traces, score JSON, per-item judge outputs, exact cost logs, or a result manifest for the paper's tables. It also postdates the immutable v5 paper. Consequently, the reported rows, error labels, frontier values, and cost/runtime plots cannot be independently regenerated from the preserved release.

Operational comparability is also limited. Agent rows bundle model, scaffold, tool surface, context management, stopping policy, and likely token/runtime budgets. ResearchHarness provides a more controlled surface for native LLMs, but the paper does not report repeated trials or task-cluster uncertainty. The current example YAML specifies one repeat, reinforcing that the main table is a configured-run snapshot rather than a reliability estimate.

The scorer's report-only observation is unlike scientific peer review or computational reproduction. Real reviewers inspect methods, tables, supplementary details, and sometimes code/data; computational checks verify execution and provenance. Here a polished but unsupported report may outscore a correct run with weak exposition. That is a known construct tradeoff, not a defect that a stricter prompt can solve.

## Limitations and validity threats

### Construct under-observation

The benchmark solicits code and outputs but does not score their execution or lineage. This makes report-writing quality, target-content recall, and judge persuasion part of the measured construct while leaving valid data use and reproducibility latent.

### Circular target anchoring

The target paper determines task framing, criteria, keywords, target figures, and the meaning of 50. That supports rediscovery measurement but penalizes scientifically valid alternative methods or conclusions unless the judge recognizes them from report prose. It also makes “surpassing” hard to distinguish from optimizing against the target's selected outputs.

### Thresholds without calibration

The 50 and 70 interpretations are authored scale semantics. There is no human baseline distribution, paired expert preference validation, score reliability, or external outcome validation. Scores above 50 are therefore judge-assigned reference-exceedance signals, not discovery evidence.

### Sparse and uneven criterion coverage

The release has only 154 items across 40 complex studies; 21 tasks have three criteria. A few heavily weighted target artifacts cannot cover all hidden requirements, statistical assumptions, safety issues, falsification attempts, or reporting obligations. Weight sums are normalized, but weight validity is not studied.

### Judge evidence-view mismatch

For text items, the judge lacks the target paper despite being asked whether results are comparable to it. For images, it receives an unmatched set of up to five generated images. Neither path inspects code or provenance. The observer cannot verify many claims encoded by the scale.

### Public-target contamination

The official package publicly contains every target paper, checklist, and target image. Search-capable agents may retrieve the paper or benchmark repository. The paper does not report rollout-level target-access detection, model-pretraining exposure, memorization probes, or clean held-out/private tasks. Public scores require explicit exposure provenance.

### Task-package heterogeneity

The paper describes raw data, but release descriptions explicitly identify synthetic, simulated, sampled, subset, and preprocessed inputs in multiple tasks. `Information_002`, for example, supplies a large article-analysis bundle including PDFs, TeX, Markdown, notebooks, YAML, and a scoring prompt. Such packages may be legitimate, but they exercise materially different degrees of data preparation and answer-bearing context. “Starts from raw experimental data” is not a suite-wide property.

### Selection and expert-process opacity

The exact four-per-domain balance is purposive coverage, not a sample from scientific work. Expert eligibility, disciplinary distribution, authoring hours, conflicts, adjudication, failed-task counts, reproduction records, and cross-expert disagreement are not reported. “High impact,” “practical value,” and “reproducible” remain selection judgments without inspectable lineage.

### Single-run and configured-system uncertainty

Main scores have no repeated-trial variance or clustered uncertainty. The error analysis covers 280 runs, while Table 5 lists eight autonomous configuration rows due to two EvoScientist versions; the inclusion boundary must be reconstructed rather than read from a versioned result manifest. Small score differences should not be read as stable ranks.

### Missing safety and research-governance checks

The tasks span scientific domains, including potentially consequential areas, but the rubric focuses target artifacts rather than authorization, unsafe experimentation, data governance, dual use, uncertainty communication, or escalation. Report similarity is not responsible research conduct.

## Transferable benchmark-design implications

### Retain

- Start from consequential, inspectable domain work rather than generic prompts.
- Package source materials, task descriptions, artifacts, and expert criteria together.
- Keep target/reference materials out of the participant runtime workspace.
- Preserve criterion-level rationales and weights rather than only one holistic score.
- Report task-level profiles, cost, runtime, and configured-system identity.
- Treat target papers as references rather than unquestionable ground truth.

### Repair

1. **Type the claim per criterion.** Use explicit relations such as `content_present`, `execution_reproduced`, `metric_matched`, `metric_improved_under_matched_protocol`, `mechanism_supported`, or `novelty_independently_verified`.
2. **Bind criteria to evidence.** Require locators into report claims, generated artifacts, source inputs, code, commands, and output hashes. A report assertion without execution evidence should not satisfy an execution criterion.
3. **Declare observer sufficiency.** Record exactly which evidence each grader sees and which claim it can therefore support.
4. **Separate scores.** Report reference recovery, execution validity, evidence/provenance quality, robustness, novelty verification, safety, and communication separately before any declared aggregation.
5. **Calibrate anchors.** Score blinded human reproductions, intentionally flawed outputs, alternative valid methods, and judge/human repeats. Estimate disagreement and threshold error.
6. **Version exposures.** Preserve task/release hashes, public/private status, search policy, target-access events, prior-trial exposure, and model knowledge cutoff. Rotate private equivalent forms.
7. **Publish replay evidence.** Release redacted workspaces, traces, per-item outputs, costs, failures, seeds, and a row-to-run manifest where licensing permits.
8. **Use repeated configured-system trials.** Report task-clustered uncertainty, missing/failed run policy, and rank sensitivity.

## Concrete repository actions

1. Add a pending build task for a **reference-role and criterion-observability audit fixture**. The useful completion condition is a validator-backed task fragment that rejects (a) a `surpasses_reference` criterion without matched baseline evidence and an independent-verification state, (b) an execution claim observed only from report prose, and (c) a public target package presented as unexposed without a versioned exposure policy. This is a bounded building task advancing charter objectives B–D, not a science-only architecture.
2. Reuse the existing benchmark bundle's typed components, evidence locators, configured-system hashes, and leakage records rather than inventing a ResearchClawBench-specific schema. The new artifact should add only the missing comparison-relation/reference-role semantics and failing fixtures.
3. For any `skill-bench` pilot using an exemplar or gold artifact, declare whether it is a construction reference, grader-only evidence, or participant-visible source; never infer “better than expert” from a rubric score unless the comparison is matched and independently checked.

## Bottom line

ResearchClawBench contributes an unusually valuable public substrate: 40 complex scientific workspaces, target studies, expert-derived multimodal criteria, and an executable harness. Its low scores are useful evidence that current configured systems struggle to recover selected reference-study content under the released setup.

The score should nevertheless be named for what it observes. The audited implementation measures **final-report and figure recovery against target-derived criteria**. It does not verify the end-to-end execution chain, does not calibrate 50 to human-equivalent reproduction, and does not independently validate above-reference findings. For `skill-bench`, the benchmark's durable contribution is the reference-grounded task package; the key repair is to bind every claim to the evidence view and comparison relation that can actually support it.

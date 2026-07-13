# Scouting note — agentic rubric-verification validity gap

**Timestamp:** 2026-07-13T20:16:58Z  
**Scope:** Narrow expansion against charter objectives A/B/C. Queue inspection found 186 tasks: 182 completed, two blocked, two pending (one build and one consolidation), no claimed work, and no pending source/research/review task. The reviewed corpus already covers trajectory-level judge reliability, human/AI rater effects, rubric authoring, and rubric prompt/call-topology interventions, but not a released criterion-level meta-evaluation over long agentic research and coding outputs.

## Substantive finding (triage only)

**Can LLM-as-a-Judge Reliably Verify Rubrics in Agentic Scenarios? (RuVerBench)**

- Immutable arXiv record: https://arxiv.org/abs/2606.29920v1
- Immutable PDF: https://arxiv.org/pdf/2606.29920v1
- Official repository: https://github.com/THU-KEG/RuVerBench
- The arXiv API identifies Yangda Peng, Yunjia Qi, Hao Peng, Haotian Xia, Guanzhong He, Xintong Shi, Richeng Xuan, Songyuanyi Lu, Yixian Liu, Zhichao Hu, Yuhong Liu, Lei Hou, Bin Xu, and Juanzi Li; v1 was submitted 29 June 2026, and no later version was returned during this run.
- The abstract introduces 2,458 output–rubric instances from deep-research and agentic-coding settings, each with a human binary satisfaction label. It reports that frontier judges remain noisy and studies prompt design, rubric batching, and majority voting. These are discovery leads only: source-task and model-output sampling, rubric provenance, label prevalence, annotator authority/independence, adjudication, output-length and criterion-family effects, evidence access, repeats, uncertainty, invalid outputs, cost, and aggregation require full-paper and release verification.
- The arXiv record/PDF and official repository URLs resolved successfully. `git ls-remote` verified repository HEAD `4e2992e3fa85448b4ba7a85741b65e09e4bec016` during discovery. The repository files, history, dataset, code, prompts, labels, and results were **not** inspected during scouting.
- Repository-wide duplicate search found neither the title, arXiv ID, nor RuVerBench. [AgentRewardBench](../../papers/agent-benchmarks/2026-07-10-agentrewardbench-judge-reliability.md) evaluates trajectory-level success, side effects, and repetition under mismatched evidence views; [rubric modification](../../papers/agent-benchmarks/2026-07-11-rubric-modification-human-autorater-agreement.md) evaluates rubric examples, decomposition, batching, and agreement on shorter static texts. RuVerBench appears nonduplicate because its unit is one rubric predicate applied to a long agentic output and its claimed release may support criterion-level failure and cost/reliability analysis.
- This is **metadata/abstract and URL triage only**. The paper, appendices, release, dataset, annotation guidelines, judge prompts, experiments, and result records were not fully read or audited. No claim is made that the labels are ground truth, rubrics preserve their intended constructs, the two domains represent professional work, majority voting makes grading reliable, or any judge is production-ready.

## Benchmark implication to test

A rubric verifier should be treated as a conditional observation instrument indexed by output/artifact type, criterion family, evidence view, judge configuration, call topology, repetition budget, threshold, and error cost. RuVerBench may add empirical evidence about how long-output criterion verification fails and when batching or voting changes the quality–cost frontier. A full audit must test whether reported noise is a portable judge property or a mixture of task/rubric sampling, label policy, prevalence, output length, shared cues, and domain-specific observability. Its evidence should refine existing grader, evidence-view, plural-judgment, task-health, metric, and validity machinery rather than create a parallel rubric subsystem.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier agent-evaluation research), B (rubric/check validity in expertise-to-evaluation), and C (reliable scalable grader machinery).
- **Evidence/artifact sought:** immutable full-paper review plus pinned release audit, including task/output/rubric/label provenance, annotator procedure, splits, judge configurations, interventions, repeats, metrics, uncertainty, failure slices, cost, and reproducibility.
- **Uncertainty clarified:** whether individual rubric verification over long outputs can be calibrated well enough for bounded use, and which observed errors arise from judges versus rubrics, evidence views, annotations, or task sampling.
- **Mode/balance:** narrow expansion; one build and one consolidation task remain ready, while the review backlog was empty.
- **Duplication/scope:** nonduplicate criterion-level long-output question; deep research and coding are bounded artifact families for testing reusable grader-validity machinery, not a scope commitment.
- **Useful completion:** verify the 2,458-instance denominator and release completeness; reconstruct annotation and evaluation design; recompute confusion/agreement evidence where possible; compare with AgentRewardBench and rubric-modification findings; preserve construct, professional-validity, general-grader, capability, production, and readiness ceilings.

Added `review-ruverbench-agentic-rubric-verification-validity` (priority 46). No second task was added.

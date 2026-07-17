# Scouting note — Agentic CLEAR dynamic diagnostic-validity gap

- **Timestamp:** 2026-07-17T02:30:28Z
- **Evidence status:** versioned arXiv abstract metadata, immutable endpoint checks, arXiv-HTML heading/outbound-link triage, official project/README triage, GitHub repository metadata/tree inspection, and local corpus/queue duplicate searches only. The PDF/body, appendices, prompts, implementation internals, sample traces/results, human annotations, statistical analyses, and reported findings were **not** deeply read or audited during scouting.

## Substantive candidate — triage only

**Agentic CLEAR: Automating Multi-Level Evaluation of LLM Agents** — Asaf Yehudai, Lilach Eden, and Michal Shmueli-Scheuer, arXiv:2605.22608v1.

- Immutable record/PDF/HTML: https://arxiv.org/abs/2605.22608v1, https://arxiv.org/pdf/2605.22608v1, and https://arxiv.org/html/2605.22608v1
- Official project: https://ibm.github.io/CLEAR/
- Official release pinned during scouting: https://github.com/IBM/CLEAR/tree/28a16d4f055697292908a5b87b3fd30ab21dc6e6
- The versioned arXiv record reports one submission on 21 May 2026. Abstract, PDF, and HTML endpoints returned HTTP 200; the abstract contains no withdrawal notice.
- The abstract describes automatic textual evaluation at node, trace, and system granularity, dynamic rather than predefined issue categories, experiments on four benchmarks and seven agent settings, comparison with human-annotated errors, and task-success prediction. These are author claims awaiting full-paper audit.
- HTML-heading triage exposes method/pipeline/UI sections; node, trace, and system views; experimental setup; universal and domain-specific issue results; backbone/judge comparisons; human-taxonomy alignment; score prediction; rubric analysis; prompts; benchmark/trace/agent appendices; and issue examples. The paper links the official IBM repository.
- GitHub API metadata identifies IBM/CLEAR as a non-fork Apache-2.0 repository. Current `main` resolved during scouting to commit `28a16d4f055697292908a5b87b3fd30ab21dc6e6` dated 16 June 2026, after arXiv v1. Root/tree triage exposes trace adapters and an intermediate representation, node and full-trajectory evaluation, rubric generation, task-success evaluation, issue and root-cause analysis, dashboards, configuration, and sample traces/results. README triage describes raw JSON/MLflow/Langfuse inputs and generated step, trajectory, rubric, and aggregate outputs. Paper/release correspondence, implementation correctness, experimental artifacts, and result reproducibility were not established.

## Why this is a narrow, useful gap

Repository search found only one incidental Agentic CLEAR citation in an acquired paper and no review, queue task, or prior scouting note. Adjacent completed work asks different questions: EvalAgent generates evaluator code; AgentRewardBench and Tool-Veritas test judge/verdict reliability; STRACE constrains causal localization; Signals studies selective trace review; Auto Benchmark Audit studies candidate task defects. None audits this exact open-taxonomy aggregation chain:

`raw trace/state evidence → normalized node/trace view → judge observation → candidate issue → dynamic category merge and system frequency → human/criterion validation → success association → actionable diagnostic claim`.

This matters because scalable analysis of heterogeneous long-horizon traces is a direct benchmark bottleneck, but a coherent issue dashboard may only compress correlated outputs from one judge. Node events are nested in traces and systems; category induction and matching can reuse the evaluation sample; human taxonomies can be incomplete or weakly reliable; success prediction is not issue correctness; and a surface symptom is not an earliest supported cause. The source can clarify when open-taxonomy analysis provides useful triage versus criterion-valid, stable, causal, or decision-useful diagnosis.

## Charter decision filter and queue action

- **Objectives advanced:** A (production agent-evaluation frontier), B (diagnostic evaluation methodology), and C (trace/grader/root-cause infrastructure).
- **Concrete evidence:** immutable-v1 deep review and timing-aware exact-commit release audit covering trace normalization, prompts/judges, dynamic taxonomy construction, human comparison, prediction, sample data, and reproducibility.
- **Uncertainty clarified:** whether node/trace/system categories are stable and independently validated; whether reported human alignment is properly sampled and reliable; whether task-success association adds criterion or only predictive evidence; and what diagnostic/utilization claim the package licenses.
- **Mode:** narrow expansion feeding validation/consolidation. Before addition the queue had one pending human prerequisite, one pending review, no claimed work, and three blocked builds.
- **Duplication/scope check:** adjacent sources cover evaluator generation, verdict reliability, causal traces, review sampling, or task auditing, not dynamic multi-level issue induction over heterogeneous agent traces. No CLEAR-specific schema or framework commitment is proposed.
- **Useful completion:** reconstruct benchmarks, agents, configurations, trace and node denominators, judge calls/information views, issue induction/merge/count rules, human-label provenance/reliability/adjudication, split/reuse boundaries, clustering/uncertainty, cost/invalidity, release correspondence, and negative cases; state bounded retain/repair/test implications for existing general machinery.

Added `review-agentic-clear-dynamic-diagnostic-validity` (priority 8). No full-paper, evaluator-correctness, taxonomy-validity, causal-diagnosis, labor-savings, production-utility, general-transfer, capability, or readiness claim was made during scouting.

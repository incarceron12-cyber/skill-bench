# Scouting note — native evaluator validity audit gap

**Timestamp:** 2026-07-12T20:14:25Z  
**Scope:** Narrow expansion against charter objectives A/B/C. Queue inspection found 157 completed tasks, one pending build, two blocked builds, and no pending source/research/review work. Existing reviews cover judge reliability, generated evaluators, artifact admissibility, harness isolation, task health, and claim validity, but not a direct expert audit of native evaluators across multiple influential tool-calling benchmark families.

## Substantive finding (triage only)

**Benchmarking the Benchmarks: A Validity Audit of Tool-Calling Evaluation**

- Immutable arXiv record: https://arxiv.org/abs/2607.02577v1
- Immutable PDF: https://arxiv.org/pdf/2607.02577v1
- arXiv API metadata identifies v1 as submitted 2026-06-30.
- The abstract reports an audit of BFCL v4, τ2-Bench, LiveMCPBench, and MCP-Atlas over 496 expert-reviewed tasks; 92 evaluator–human disagreements; deterministic and model-judge failure categories; 23 repeated LiveMCPBench evaluations; corrected components; Tool-Veritas; and Harness Lab.
- Both immutable abstract and PDF URLs returned HTTP 200 during this run. Exact-title and artifact-name web searches found the arXiv records but no clearly verified author-owned code/data repository. A reviewer must inspect the paper’s links and author metadata before attributing any release.
- Repository-wide duplicate search found no title, arXiv ID, BFCL/MCP audit, or equivalent cross-family native-evaluator review. Related local work is complementary: AgentRewardBench studies judge reliability, EvalAgent studies evaluator construction scaffolding, and BrowserGym studies adapter heterogeneity.
- This is **metadata/abstract and release-location triage only**. The paper, appendices, annotations, traces, evaluator implementations, corrected components, Tool-Veritas, Harness Lab, expert protocol, statistics, and releases were not fully read or inspected. Abstract-reported numbers are not treated as verified findings.

## Benchmark implication to test

The candidate could provide unusually direct evidence that benchmark scores inherit validity and reproducibility failures from their native evaluators—not merely from agent behavior. A full audit should determine whether expert judgments are a defensible criterion; whether disagreement denominators, sampling, blinding, adjudication, and uncertainty are reported; whether task ambiguity is separated from evaluator error; whether repeated-judge variance is configuration-controlled; whether corrected evaluators avoid trading false positives for false negatives; and whether released trace-level evidence reproduces the taxonomy. The reusable target is evaluator-observation, task-health, metric, reliability, and validity machinery across domains, not a tool-calling benchmark specialization.

## Charter decision filter and queue action

- **Objectives advanced:** A (comparative benchmark and production-evaluation research), B (valid links from task evidence to score claims), and C (auditable grader/trace/diagnostic contracts).
- **Evidence/artifact sought:** immutable full-paper review plus a pinned release audit if official artifacts are locatable, with page/file locators and family-specific denominator/reproducibility tables.
- **Uncertainty clarified:** whether native benchmark evaluators reliably measure task outcomes and whether the paper’s proposed repairs are themselves validated.
- **Mode/balance:** narrow expansion; the ready backlog otherwise contained only building.
- **Duplication/scope:** distinct from general judge reliability and evaluator-generation reviews because it audits deployed native evaluators across four benchmark families. Tool calling is a bounded measurement case, not a scope commitment.
- **Useful completion:** reconstruct sampling, expert criterion, disagreement taxonomy, repeated-run design, correction evidence, release fidelity, uncertainty, and claim ceilings; map only nonduplicate implications into existing contracts.

Added `review-tool-calling-benchmark-evaluator-validity-audit` (priority 52). No second task was added.

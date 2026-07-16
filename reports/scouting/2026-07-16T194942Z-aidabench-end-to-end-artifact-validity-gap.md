# Scouting note — AIDABench end-to-end artifact-validity gap

**Timestamp:** 2026-07-16T19:49:42Z  
**Evidence status:** arXiv API metadata/abstract, endpoint checks, repository search, GitHub repository metadata, recursive tree inventory, and local-corpus/queue duplicate checks only. The paper, task data, evaluator implementation, and reported results were **not** deeply read or audited in this scouting run.

## Substantive candidate

**AIDABench: AI Data Analytics Benchmark** — Yibo Yang et al., arXiv:2603.15636v2.

- Immutable record: https://arxiv.org/abs/2603.15636v2
- Immutable PDF: https://arxiv.org/pdf/2603.15636v2
- Immutable HTML: https://arxiv.org/html/2603.15636v2
- Official paper-linked release: https://github.com/MichaelYang-lyx/AIDABench
- The arXiv API reports v1 submission on 27 February 2026 and v2 update on 27 March 2026 in `cs.AI`; the abstract contains no withdrawal notice. Record, PDF, and HTML endpoints returned HTTP 200.
- The complete v2 PDF and extraction are already present locally at `data/papers/pdfs/2603.15636v2-aidabench-ai-data-analytics-benchmark.pdf` and `data/papers/text/2603.15636v2-aidabench-ai-data-analytics-benchmark.txt`, but no deep review or queue task existed.
- The abstract reports 600+ tasks over question answering, data visualization, and file generation, grounded in spreadsheets, databases, financial reports, and operational records. It also claims AI-assisted experts need 1–2 hours per question, evaluates 11 model families, reports a best pass-at-1 of 59.43%, and presents the suite as useful for procurement, tool selection, and optimization. These are author claims awaiting full-paper and release verification.
- GitHub identifies a non-fork repository created 26 February and last pushed 24 June 2026. The `main` recursive tree was complete at commit `1e306824a80dfc7d1dfb3eb448a6cbbe20cb209e`, with 191 entries including configured agent runners, 110 Skill paths, QA/chart/file/open-ended evaluator paths, and a `consensus/` rubric-generation/judging package. GitHub reports no detected license. File existence is not evidence that the data, paper runs, evaluator semantics, or headline claims reproduce.

## Why this is a narrow, useful gap

The corpus already deeply reviews OfficeEval, MBABench, AstaBench, FinResearchBench II, ArtifactCopilot, and multiple professional-work suites. Exact title/ID searches found no AIDABench review or queue entry. AIDABench is adjacent but nonduplicate because it joins heterogeneous business documents to three materially different output units—answers, charts, and generated files—then exposes separate evaluator families and a generated-consensus path within one claimed end-to-end instrument.

The focused validity chain is:

`work-demand and expert provenance → source/document custody and task projection → configured agent/Skill/tool view → answer/chart/native-file production → evaluator-specific evidence view → generated or authored criterion authority, applicability, and dependence → per-task decision → heterogeneous portfolio aggregation → human-effort comparison → procurement/readiness claim`.

A common runner does not make answer correctness, chart validity, native-file integrity, open-ended analytical quality, and generated-consensus agreement interchangeable. A file may exist while being stale, non-editable, numerically wrong, or unsupported by source evidence; consensus among model-generated analyses can select shared artifacts rather than professionally authoritative requirements. The source can therefore clarify cross-artifact observer sufficiency and claim promotion without making data analytics a permanent project scope.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier realistic knowledge-work benchmarks), B (document/source-to-artifact and criterion-authority transfer), and C (artifact/evaluator/configured-system machinery).
- **Concrete evidence/artifact:** immutable-v2 full-text review plus exact-commit release audit, with paper/release conformance and bounded claim ceilings.
- **Uncertainty clarified:** whether the suite establishes released-package conformance, artifact correctness, analytical quality, professional validity, configured-system capability, procurement utility, or readiness—and where unlike task/evaluator units break aggregation.
- **Mode:** narrow expansion feeding consolidation/building; not generic AI news or a domain commitment.
- **Duplication and scope check:** adjacent reviews cover native Office checks, spreadsheet artifacts, heterogeneous scientific portfolios, generated consensus criteria, and evaluator-assisted review separately, but not this combined document-to-answer/chart/file instrument.
- **Useful completion:** reconstruct task/source/output units, expert and scenario selection, the human-effort claim, configured systems and Skills, evaluator topology and evidence views, criterion generation/authority/dependencies, attempts/invalids/retries, aggregation, uncertainty, cost, result artifacts, and paper-release drift; compare with existing contracts and add only nonduplicate work.

Added one review task: `review-aidabench-end-to-end-artifact-validity` (priority 4), subordinate to the higher-priority build, consolidation, and human prerequisite. No second task was added. No claim is made that the full paper or release was read, that the benchmark data or reported results reproduce, that generated consensus is expert-valid, or that the suite establishes professional capability, procurement utility, or readiness.

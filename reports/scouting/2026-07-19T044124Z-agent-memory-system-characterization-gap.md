# Scouting note — agent-memory system-characterization gap

- **Timestamp:** 2026-07-19T04:41:24Z
- **Evidence status:** arXiv API metadata/abstract, immutable endpoint checks, arXiv-HTML outbound-link inventory, web release search, and exact local duplicate searches only. The PDF/source body, benchmark suites, ten memory systems, profiling harness, measurements, tables, or recommendations were **not** deeply read, downloaded into the repository, executed, reproduced, or audited during scouting.

## Substantive candidate — triage only

**Agent Memory: Characterization and System Implications of Stateful Long-Horizon Workloads** — Yasmine Omri, Ziyu Gan, Zachary Broveak, Robin Geens, Zexue He, Alex Pentland, Marian Verhelst, Tsachy Weissman, and Thierry Tambe; arXiv:2606.06448v1 (submitted 2026-06-04).

- Immutable record/PDF/HTML/source: https://arxiv.org/abs/2606.06448v1 · https://arxiv.org/pdf/2606.06448v1 · https://arxiv.org/html/2606.06448v1 · https://export.arxiv.org/src/2606.06448v1
- At scouting time all four endpoints returned HTTP 200. The API record was 2,888 bytes; the abstract page reported 42,373 bytes; the PDF reported 1,109,927 bytes; the HTML reported 164,643 bytes; and the source endpoint resolved to `/src/2606.06448v1` and reported 1,682,232 bytes.
- The abstract says the paper supplies a four-axis system taxonomy, a phase-aware profiling harness attributing cost to construction/retrieval/generation, characterization of ten representative memory systems across two benchmark suites, and ten recommendations involving construction scheduling, capability floors, query-volume amortization, freshness–latency tradeoffs, and fleet management. These are author-stated abstract claims awaiting complete critical review, not established system or benchmark findings.
- The immutable HTML exposed no paper-specific code, data, harness, result archive, or project link. Targeted web searches found secondary listings but no verified official release. Release absence must be checked against the full paper and author records rather than inferred from HTML alone.
- Exact arXiv-ID/title, system-characterization, phase-aware profiling, and queue/review/scouting searches found no local source-specific duplicate. Existing MemoryArena, LongMemEval v2, EvoMemBench, MemOps, AgentFootprint, online memory-budget, Self-GC, context-compression, and configured-system reviews are necessary comparators rather than substitutes: they address memory-task validity, lifecycle semantics, persistence, utility, or compression, but not this claimed cross-system write/read-path characterization.

## Why this is a narrow, useful gap

The reusable chain is:

`stateful workload and query schedule → exact memory-system/configuration identity → construction/write events → stored representation and freshness → retrieval opportunity/result → model-visible context → adoption and action → task consequence → phase-attributed latency/compute/token/storage cost → amortization/fleet policy → bounded production decision`.

This advances charter objectives A, B, C, and E and directly addresses the stale production-system-map backlog on operational memory behavior. The project already distinguishes persistence, retrieval, adoption, consequence, and resource accounting, but lacks a deep comparative systems source about how memory architecture shifts cost and freshness across write and read phases. A review can test whether the proposed taxonomy and harness support matched, decision-relevant comparisons or confound memory policy, model, task suite, query volume, implementation maturity, and deployment scale.

The claim ceiling is central. Ten selected systems are not a representative market; two benchmark suites do not establish production workload transport; phase-attributed latency is not end-to-end utility; task success does not establish semantic memory fidelity or safe forgetting; query-volume amortization depends on workload stationarity and retention boundaries; and extrapolated fleet recommendations require concurrency, hardware, caching, tenant isolation, failure, privacy/deletion, and tail-latency evidence. A systems benchmark can inform configured-system and resource contracts without making memory the benchmark's domain.

## Charter decision filter and queue action

- **Objectives advanced:** A (production memory and evaluation evidence), B (memory-to-action/consequence chain), C (configured-system and resource instrumentation), and E (cost/utility/transport interpretation).
- **Concrete evidence:** immutable-v1 full-text critical review reconstructing taxonomy, harness, systems, suites, configurations, workload/query schedules, phase metrics, results, uncertainty, and recommendation warrants, plus a release-availability audit.
- **Uncertainty clarified:** whether the characterization supports portable memory-system design decisions under matched stateful workloads or only descriptive results for selected implementations and benchmark schedules.
- **Mode:** narrow expansion/human learning. The ready queue contains two validation builds and one human decision but no source/research/review task; one low-priority review restores a bounded evidence buffer without repeating broad memory searches.
- **Duplication/scope check:** exact source searches were negative; adjacent reviews are mandatory comparators. Memory is a configured-agent component and production stress case, not a benchmark-domain commitment.
- **Useful completion:** preserve full-text provenance; reconstruct every compared condition and cost boundary with page/table evidence; separate storage, retrieval, visibility, adoption, consequence, and utility; audit release/reproducibility; compare recommendations against existing contracts; add no schema or build task unless a demonstrated obligation is unrepresentable.

Added one task: `review-agent-memory-system-characterization` (review, priority 36). No second task was queued.

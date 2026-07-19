# Agent-memory systems characterization: phase accounting is valuable, but selected-package profiles do not identify production memory utility

## Source and review status

**Deep review of the complete immutable primary source, including the arXiv TeX source and all figures, plus a release-availability audit.**

- **Paper:** Yasmine Omri, Ziyu Gan, Zachary Broveak, Robin Geens, Zexue He, Alex Pentland, Marian Verhelst, Tsachy Weissman, and Thierry Tambe, *Agent Memory: Characterization and System Implications of Stateful Long-Horizon Workloads*, arXiv:2606.06448v1 (4 June 2026), <https://arxiv.org/abs/2606.06448v1>.
- **Immutable local PDF read in full:** `data/papers/pdfs/2606.06448v1-agent-memory-system-characterization.pdf` (12 pages; 1,109,927 bytes; SHA-256 `b9d840d861da993e05ecc9e2295e9754ee9289ebc595270f6af18c55e57b8782`).
- **Full local text read:** `data/papers/text/2606.06448v1-agent-memory-system-characterization.txt` (131,589 bytes; SHA-256 `4cdd93e5012090dc27a5857ab382bfcd71a1f87f991d7d9063156c05bbc8d712`).
- **ArXiv source inspected:** `data/papers/source/2606.06448v1-source.tar` (64 entries; SHA-256 `d80b985d706ec119e25f81b9751376f77aff574d9475760f105c797cd7c64361`). It contains manuscript TeX/BibTeX/styles and figures, but no harness, system adapters, configuration manifest, raw telemetry, result rows, analysis code, environments, or data supplement.
- **Metadata:** `data/papers/source/2606.06448v1-metadata.xml`; it contains no withdrawal or retraction notice.
- **Release boundary:** the paper twice says the profiling harness is “to be open-sourced” (pp. 2, 5) and links no study repository. Exact-title, harness-phrase, author/GitHub, Stanford publication-page, and general web searches on 19 July 2026 found no verifiable author-owned harness, configuration, telemetry, or result release. All measurements below are therefore manuscript-reported and unreplayed.

This review advances charter objectives A–C and E by examining a missing configured-system/resource boundary. Memory is a component and production stress case, not a benchmark domain commitment.

## Why this matters

Long-horizon knowledge-work agents create persistent state before they answer later questions or alter artifacts. If evaluation records only final quality and query latency, it can mistake expensive precomputation for cheap serving, ignore stale writes and unbounded retained state, or reward a system that saves resources by discarding evidence needed for audit, recovery, or correct action. This paper provides a concrete phase-accounting template while exposing exactly where resource characterization stops short of semantic and decision utility.

## One-sentence contribution

The paper usefully decomposes memory into ingestion, construction, storage, retrieval, prompt assembly, generation, and maintenance, then shows that selected memory packages can move large hidden costs from query serving into write-time construction; but unversioned and adapted implementations, five central histories, no stochastic repetitions or uncertainty, unreleased telemetry, incomplete energy/storage boundaries, and untested concurrency make its ten recommendations design hypotheses conditioned on selected packages and schedules—not validated production policies or memory-utility rankings.

## Research question and defensible claim

The paper asks (pp. 2, 5) how emerging memory paradigms trade construction and read-path costs, what system opportunities those workloads expose, and how construction, storage, retrieval, and mutation choices shape utilization, bandwidth, latency, and scale.

Its strongest defensible claim is:

> Under the authors’ unreleased adapters and prompt modifications, named remote/local model configurations, selected MemoryAgentBench and MemoryArena workloads, and one reported hardware stack, ten selected memory packages exhibited materially different construction call structures, wall times, raw GPU-energy estimates, retrieval/generation latencies, retained footprints, and benchmark accuracies. LLM-mediated and agent-controlled packages usually paid much larger construction costs than lexical/dense indexing, while fixed-depth retrieval showed narrower observed query-latency tails than some adaptive pipelines.

The evidence does **not** establish representative memory-system prevalence, exact package-version effects, a causal effect of any taxonomy axis, semantic memory fidelity, safe update/deletion, adoption of retrieved evidence, downstream action benefit, production queueing behavior, total energy or cost, fleet capacity, a stable Pareto ranking, or deployment readiness.

## Methodology and system reconstruction

### Pipeline and four-axis taxonomy

The paper’s seven runtime stages are (pp. 2–3): ingestion; construction; storage; retrieval; prompt assembly; answer generation; and maintenance. This is a valuable accounting frame because final-generation latency hides extraction, indexing, consolidation, and store growth.

Table 1 (p. 4) describes four system dimensions—construction pipeline, database organization, retrieval pipeline, and mutability—and groups ten packages into four paradigms:

1. **Long context:** `long_context`, raw history passthrough, append-only.
2. **Flat RAG:** BM25 over an inverted index and `embedRAG` over a dense store; deterministic append-only construction and single-shot top-k retrieval.
3. **Structure-augmented RAG:** append-only GraphRAG and HippoRAG v2; consolidating Mem0 and SimpleMem.
4. **Agentic control:** A-Mem, Letta, and MIRIX, where an LLM controls some writes, tools, routing, or record mutation.

The labels are descriptive, not a factorial design. Construction control, number/type of stores, extraction model, retrieval depth, mutation, prompts, and package maturity co-vary. One package occupies each complex combination, so paradigm-level causal language is stronger than the comparison permits.

### Systems, adaptations, and comparability

Within a named model configuration, the authors use a common generation LLM and embedding backbone, stream histories in 4,096-token chunks, and cap retrieval at ten entries (pp. 4–5). Local context overflow changes the cap to five; Letta additionally receives 512-token ingestion chunks. Native buffering, parallel ingestion, and cross-chunk consolidation remain package-specific.

Compatibility adaptations are consequential (pp. 4–5):

- SimpleMem extraction prompts are changed for non-dialogue histories;
- A-Mem aggregates fine-grained units on non-dialogue data and uses plain text for local backbones versus JSON schema for API backbones;
- Mem0 receives an ICL-specific extractor that preserves integer labels;
- Letta receives task-specific prompts and caps on repeated construction/retrieval tool calls.

These are defensible engineering accommodations, but they make each row an **authored configured adapter**, not an off-the-shelf system. The paper gives no commits, package versions, exact prompts, cap values beyond the retrieval-entry cap, dependency environment, database settings, index parameters, top-k semantics, invalid-run policy, or adaptation ablation. “Same LLM/embedding model” does not equal matched compute: package-specific call counts range from hundreds to tens of thousands (Table 3, p. 6).

### Workloads and schedules

**MemoryAgentBench (MAB).** The full suite covers accurate retrieval, test-time learning, long-range understanding, and selective forgetting across histories averaging 103K–1.44M tokens (Table 2, p. 5). Figure 7 macro-averages unlike datasets and LLM-judge endpoints. The central systems characterization instead uses `LongMemEval_S_*`: only five histories of about 360K tokens, each with 60 queries, producing 300 query rows but only five independently constructed stores (pp. 4–6).

**MemoryArena.** Section 4.6 uses the physics split: 20 multi-session tasks, each replayed as retrieve–act–write sessions under a controlled five-second inter-session arrival gap (pp. 8–9). The synchronous/asynchronous comparison is a timing-trace replay, not a measured concurrent multi-tenant service. The five-second schedule is one synthetic arrival process, not a sampled production distribution or sensitivity sweep.

**Growth workload.** Figure 9 scales one user’s LongMemEval arbitrary context from roughly 64K to 1M tokens over five sizes (pp. 9–10). The paper does not state the number of generated histories, seeds, repetitions, confidence intervals, retention duration, or whether every point has identical semantic composition.

### Serving and hardware configuration

The remote construction regime uses GPT-4o-mini or GPT-4.1-mini plus `text-embedding-3-small`. The local regime uses one NVIDIA H100 80GB HBM3 under vLLM, one isolated SLURM job per system, and six Xeon Platinum 8480C cores (p. 5). The model ladder is Qwen3-32B, 14B, 8B, and 1.7B; 32B/14B use FP8, smaller models BF16; Qwen3-Embedding-0.6B supplies embeddings. The LLM and embedding servers receive 75% and 15% of GPU memory; thinking is disabled.

Isolation improves per-package attribution but prevents the paper from measuring its central co-location claim: construction traffic “stalls” latency-sensitive QA through shared KV-cache and scheduler pressure (p. 7). No construction-plus-QA concurrency experiment, admission-control intervention, cache-state control, tenant mixture, arrival sweep, throughput/SLO curve, or separate-endpoint comparison is reported.

### Phase-aware profiling and metrics

The harness tags chat and embedding calls by construction, retrieval, and generation; records timing, prompt/completion tokens, embedding input tokens, and embedded-sequence counts; samples NVML/DCGM-style GPU power, utilization, VRAM, SM/tensor activity, and HBM bandwidth; and integrates device power over phase intervals (p. 5).

This is the paper’s most transferable machinery. Yet the measurement contract is incomplete: polling rate, clock synchronization error, attribution of overlapping calls, idle-power subtraction, warmup, cache state, batching, retry handling, server overhead, CPU/DRAM/network/database energy, remote-provider energy, PUE, and repeated-run variance are absent. “Raw GPU energy” is therefore a precise label for Figure 4; “total energy” and “unhideable cost” (p. 6) overstate what was observed.

Quality is MAB’s LLM-judge accuracy, but the paper does not restate judge identity, prompt, repeats, calibration, invalid policy, or human agreement. It does not observe whether a required fact was persisted, retrieved, model-visible, adopted, and causally used. Correct answers and latency therefore characterize a package endpoint, not memory semantic fidelity.

## Evidence and what it supports

### Hidden construction cost

For local Qwen3-32B over the five `LongMemEval_S_*` stores and 300 queries, Table 3 reports (p. 6):

- BM25: 47.0% accuracy, 16.3 minutes, 300 calls, 582 kJ, 4.128 kJ/correct;
- GraphRAG: 46.0%, 1.83 hours, 3,215 calls, 2,082 kJ, 15.084 kJ/correct;
- HippoRAG v2: 44.3%, 44.2 minutes, 2,743 calls, 1,339 kJ, 10.079 kJ/correct;
- A-Mem: 42.7%, 11.76 hours, 19,230 calls, 14,864 kJ, 116.116 kJ/correct;
- embedRAG: 39.8%, 14.4 minutes, 610 calls, 495 kJ, 4.144 kJ/correct;
- SimpleMem: 36.0%, 3.92 hours, 4,447 calls, 5,481 kJ, 50.749 kJ/correct;
- Mem0: 32.0%, 4.02 hours, 4,538 calls, 4,878 kJ, 50.813 kJ/correct;
- Letta: 27.7%, 14.36 hours, 18,394 calls, 15,429 kJ, 185.873 kJ/correct;
- MIRIX: 20.0%, 6.03 hours, 7,655 calls, 8,678 kJ, 144.629 kJ/correct.

This credibly shows that query-only latency can conceal substantial precomputation in these configurations. It does not establish an intrinsic package ranking: accuracy, calls, construction, and query work are all package-coupled; correct answers cluster within five histories; there are no repeats or uncertainty; and the long-context row is omitted from Table 3’s full-lifecycle comparison.

There is also a manuscript inconsistency: the prose says “A-Mem and MIRIX reach 115 kJ and 197 kJ” per correct answer (p. 6), while Table 3 reports 116.116 and 144.629 kJ; `8,678 kJ / (300 × 20%)` agrees with the table’s MIRIX value, not 197 kJ. This does not erase the order-of-magnitude spread, but it illustrates why unreleased analysis artifacts matter.

### Construction traffic shape and model floor

Figure 5 reports that construction is predominantly prefill/embedding traffic, with median completion-token share 4.6%; GraphRAG and HippoRAG batch many embedding sequences, while Mem0 and agentic loops issue more sequential calls (p. 7). Figure 6 sweeps the construction model while holding GPT-4o-mini QA and OpenAI embeddings fixed: GraphRAG remains near 47–48%, some systems degrade gradually, and MIRIX fails completely at Qwen3-1.7B because structured tool/JSON behavior breaks (pp. 7–8).

These observations support two useful hypotheses: serving admission should distinguish throughput-oriented construction from interactive reads, and schema-constrained construction has a model-dependent validity floor. But the paper reports no structural-validity rate, error taxonomy, store-integrity audit, repeated construction, model-cost curve, or held-out repair experiment. One MIRIX failure point does not establish a general “algorithm-imposed floor.”

### Construction–serve–accuracy frontier

Across the full heterogeneous MAB suite under remote GPT-4o-mini, Figure 7 reports BM25 at 55.8% with sub-second construction and roughly 7.4-second queries; Mem0 has roughly 2.2-second queries but 4,108-second construction and 26.8% accuracy; SimpleMem has roughly 18.4-second queries and 36.2% accuracy (p. 8). The paper appropriately notes BM25’s suite advantage is recall-heavy and category-dependent.

The plot demonstrates package heterogeneity, not one common utility frontier. Macro-averaged “accuracy” combines different tasks and question counts; construction is not amortized over a declared deployment query distribution; package versions and stochastic uncertainty are absent; and no stakeholder loss function says how to exchange one point of MAB accuracy for latency, energy, storage, freshness, or maintenance.

### Freshness and write scheduling

Under the five-second MemoryArena replay, BM25/embedRAG remain fresh while slower packages accumulate one or two uncommitted sessions in the representative plot; write time spans roughly five orders of magnitude (pp. 8–9). This clearly shows a feasibility inequality:

`construction + required read-path work ≤ admissible inter-session interval`

when the next session strictly depends on committed prior state.

It does not demonstrate “unbounded staleness,” concurrent correctness, safe asynchronous mutation, or a required scheduling policy. There is no arrival-rate sweep, queueing model validation, multiple users, overlapping writes, lock/transaction behavior, conflict handling, backpressure, crash/retry test, stale-read effect on task quality, or service-level tail distribution.

### Growth, footprint, and tails

Figure 9 reports roughly 9× on-disk spread at 1M input tokens (about 12 MB Mem0 to 62 MB HippoRAG v2), monotonic default growth for all tested systems, apparently super-linear construction-token growth for agentic systems, and almost flat indexed retrieval latency (pp. 9–10). A simple projection gives 0.7–6.2 TB for 100,000 users. Figures 10–11 report effective pre-answer latency from about 0.10 seconds for Mem0 to 22.6 seconds for SimpleMem and p95/p50 ratios near 1.3× for BM25/embedRAG versus 3.9× for Letta and 5.9× for GraphRAG (pp. 10–11).

These are useful stress observations, not fleet evidence. “On-disk footprint” lacks apparent-versus-allocated-byte, database/index/log/cache, compaction, remote-store, replica, backup, retention-time, and write-amplification definitions. Five history sizes without repeated histories cannot establish a scaling law. Query-level p95 over one fixed query corpus conflates query heterogeneity with stochastic service tails; it is not a repeated-request SLO distribution. The 100K-user projection assumes linear independence and omits shared indexes, tenant isolation, replication, metadata, backups, retention, deletion, concurrency, and regional redundancy.

## Unique insight: memory architecture changes the location of work, not just its amount

The durable contribution is a **phase-and-amortization boundary**:

```text
stateful workload + arrival/query schedule
→ exact configured memory adapter and model/store identities
→ ingestion and construction events
→ realized persistent representation, freshness, and footprint
→ retrieval candidates and retrieval-side orchestration
→ model-visible context
→ adoption/rejection and action
→ artifact/environment consequence
→ phase-specific resources and tails
→ amortization under eligible query volume and retention horizon
→ bounded operating decision
```

The paper measures much of the left and middle resource chain, then jumps from answer accuracy to operator recommendations. `skill-bench` must preserve the missing links. A system can be cheap because it omitted, corrupted, or prematurely deleted essential evidence; expensive because it preserved audit/recovery utility; accurate without using memory; or memory-faithful while a reader fails. Therefore:

> **Construction cost, storage cost, retrieval delivery, semantic fidelity, action benefit, and decision utility are separate estimands. A package’s write/read cost split becomes meaningful only under a declared workload schedule, evidence-authority contract, and consequence-valued utility function.**

This extends—rather than replaces—the existing reviews. MemoryArena supplies dependency-bearing actions but not causal memory use; LongMemEval v2 isolates evidence delivery but not action; EvoMemBench shows scope/content labels need fixed information-flow contracts; MemOps separates expected lifecycle projections from realized store operations; AgentFootprint separates logical retained volume from persistence amplification and utility; the online skill/memory review requires full opportunity-cost accounting; Self-GC separates retention from recovery and use; decision-fidelity compression separates source preservation from downstream correctness.

## Audit of the ten recommendations

| Recommendation (paper section) | Evidence status | Repair before production use |
|---|---|---|
| 1. Select memory as a system-level decision, not on accuracy alone (§4.1) | **Supported as a principle** by large configured-package cost spreads | Predeclare quality, reliability, resource, retention, safety, and consequence objectives; compare exact versions under matched workload populations |
| 2. Account for lifecycle energy, including construction (§4.2) | **Directionally supported** for local raw GPU energy | Include CPU/DRAM/network/storage, idle baseline, cooling/PUE, remote calls, cache/batching, retries, and uncertainty; do not label raw GPU integration total energy |
| 3. Treat construction as background throughput with admission control (§4.3) | **Plausible, not intervention-tested** | Run co-located arrival/load sweeps with and without admission control and measure QA SLOs, construction backlog, energy, and correctness |
| 4. Exploit prefix reuse, chunk caching, and batching (§4.3) | **Mechanistically plausible, untested** | Measure cache hit rate, equivalence, invalidation, memory pressure, latency, and net energy under overlapping histories |
| 5. Validate a minimum viable construction LLM (§4.4) | **Supported by one package/model failure pattern** | Measure schema/store validity and downstream quality over repeated builds, exact adapters, task families, and repair policies |
| 6. Match write/read split to query arrival and task family (§4.5) | **Supported conceptually; amortization not estimated** | Specify eligible query volume, update rate, retention horizon, quality threshold, expiry, and full cost; estimate crossover with uncertainty |
| 7. Treat construction+retrieval as a freshness feasibility constraint (§4.6) | **Supported for strict dependency under one replay schedule** | Sweep arrival processes, dependency deadlines, concurrency, stale-read consequences, queue discipline, and failure recovery |
| 8. Use system-aware cadence and compaction/rebuild triggers (§4.6) | **Not directly tested** | Define marginal-cost/quality trigger, compare continuous/batched/rebuild policies, and test correctness under consolidation and concurrent updates |
| 9. Evaluate baseline footprint and growth slope; add pruning/forgetting (§4.7) | **Directionally supported; slope and forgetting evidence weak** | Repeat histories/orders, type retained utility, measure write amplification/byte-days, and validate selective deletion, reconstruction resistance, recovery, and harmful forgetting |
| 10. Use worst-case latency and cap LLM-bounded loops (§4.8) | **Observed tail heterogeneity supports caution, not a worst-case bound** | Repeat requests under load, preserve timeout/cap failures, estimate clustered tails, and measure quality/recovery effects of caps |

## Limitations and validity threats

### Construct and selection

1. The ten systems are selected examples, not a sampled market or complete design crossing.
2. Paradigm dimensions co-vary; no factorial ablation identifies construction, storage, retrieval, or mutability effects.
3. Package versions, commits, prompts, database settings, and dependencies are absent.
4. Compatibility adaptations may materially alter memory quality and cost; no native-versus-adapted ablation is reported.
5. MAB endpoint accuracy does not distinguish persistence, retrieval, visibility, adoption, reasoning, or grader error.
6. The full-suite macro-average combines unlike task constructs and denominators.
7. The central 300 queries arise from only five constructed histories; query count overstates independent write-path evidence.
8. MemoryArena’s physics split and a five-second gap do not represent production arrival/dependency distributions.
9. No professional artifact, stakeholder consequence, expert criterion, or deployment utility is measured.

### Measurement and statistics

10. No seeds, stochastic repetitions, confidence intervals, paired tests, cluster bootstrap, or multiplicity controls are reported.
11. MAB LLM-judge identity/calibration and invalid-output handling are not restated or audited.
12. Remote and local regimes use different models, quantization, providers, observability, and energy boundaries.
13. Energy covers integrated local GPU power, not total system/service energy; telemetry sampling and idle attribution are unspecified.
14. Per-correct-answer energy can reward/penalize judge behavior and becomes unstable at low accuracy; it is not a substitute for separate quality and resource metrics.
15. Construction wall time reflects package call topology, possible parallelism, provider behavior, and adaptation—not just memory architecture.
16. Query-tail percentiles over a heterogeneous fixed query set are not repeated-request service tails.
17. The manuscript’s MIRIX per-correct-energy prose conflicts with Table 3’s arithmetic.
18. Figure 7’s macro-averaged frontier lacks a deployment query/update distribution and common value scale.
19. Five size points without disclosed repetitions do not identify a reliable growth function.
20. The footprint definition omits several physical and lifecycle boundaries required for fleet cost.

### Causal and operational realism

21. Isolated single-GPU jobs do not test the claimed construction/QA co-location interference.
22. No admission-control, cache, batching, endpoint-separation, or cadence recommendation is experimentally intervened on.
23. Asynchronous freshness is trace replay, not a concurrent database/agent execution with locks, conflicts, crashes, or retries.
24. Retrieval cap changes from ten to five under overflow, coupling package quality to local context limits.
25. Tool-call caps bound Letta behavior but cap values and quality/cost sensitivity are absent.
26. No store-integrity, contradiction, temporal validity, authority, provenance, deletion, privacy, security, or poisoning audit is performed.
27. “None forget by default” establishes growth under tested defaults, not whether an added forgetting policy is safe or compliant.
28. Linear 100K-user projection omits shared resources, tenant isolation, replicas, backups, regions, retention time, and concurrency.
29. No cost model covers API prices, CPU/storage/network, engineering labor, monitoring, failures, or human adjudication.
30. Single-node textual workloads do not support multi-node, multi-agent, multimodal, or enterprise transport; the paper acknowledges these gaps (p. 11).

## Reproducibility and release inspectability

The paper is unusually clear about model names, one hardware stack, memory phases, broad adaptations, central history/query counts, and several raw table values. The immutable source exposes all manuscript figures and TeX, which permitted the internal arithmetic check above.

It is not a reproducible study package. The promised harness is unavailable; no package commits, environment lock, adapters, prompts, MAB/MemoryArena item manifests, exact run commands, raw phase events, power samples, store snapshots, per-query outputs, judge rows, retry/invalid ledger, seeds, analysis scripts, or plotted numeric tables are released. Proprietary OpenAI endpoints and unspecified package versions further prevent reconstruction. At present the evidence can guide instrumentation and experimental hypotheses, but cannot calibrate `skill-bench` resource thresholds or reproduce the rankings.

## Transfer to skill-bench

### Retain

1. Instrument construction/write, retrieval, prompt assembly, and final generation separately on one monotonic trial timeline.
2. Record prompt/completion/embedding tokens, calls, latency, storage, and compute/energy by phase rather than reporting query-only cost.
3. Treat memory/package/model/store/prompt/harness versions as independent configured components.
4. Preserve arrival schedules, update/query ratios, retention horizons, and dependency deadlines; amortized cost is workload-conditional.
5. Distinguish fixed-depth algorithmic phases from model-controlled loops and retain cap/timeout outcomes as evidence, not silently repaired runs.
6. Report baseline footprint and growth together with the authorized utility that retained state supports.
7. Keep resource coordinates plural; never collapse quality, freshness, energy, latency, storage, safety, and expert burden into one unvalidated score.

### Repair

1. Add matched controls for `no memory / long context / oracle evidence / retrieved evidence / corrupted evidence`, then observe persistence, retrieval, visibility, adoption, action, and consequence separately.
2. Cluster uncertainty by constructed history, session chain, user, and task lineage; repeat stochastic construction, retrieval, readers, and judges.
3. Exercise scheduling recommendations: arrival/load sweeps, shared versus disaggregated endpoints, cache/admission interventions, stale-state consequences, and crash/retry semantics.
4. Type storage as apparent/allocated bytes, logical objects, write amplification, byte-days, replicas, restore/audit/deletion utility, and retention authority.
5. Require a decision/utility basis before calling a memory package efficient: declare eligible query volume, task-family mix, freshness SLO, quality/safety thresholds, and lifecycle resource prices.

### Do not infer

Do not infer general memory capability, semantic fidelity, safe forgetting, privacy compliance, professional competence, causal memory benefit, production SLO fitness, fleet cost, or deployment readiness from the paper’s accuracy/cost points. Do not call construction energy invariant to scheduling: batching, cache reuse, utilization, interference, and power state can change energy as well as latency. Do not treat an observed p95 over one query corpus as a worst-case guarantee.

## Concrete repository action

No new build or schema task is warranted. Existing configured-system/resource, benchmark-trace, information-flow, metric-monitoring, task-health, validity, longitudinal, retention, and experience-memory-transfer machinery can represent the obligations. The nonduplicate next use is empirical: when a future persistent-memory pilot is selected, instantiate phase receipts and a workload-conditional amortization analysis inside that pilot, while retaining evidence-delivery and held-out-action estimands separately.

The stale `docs/production-agent-systems.md` memory section should eventually be consolidated with this review and the adjacent full reviews, but creating a separate queue task is unnecessary unless the consolidator finds that broader document still actively guides builds.

## Claim boundary

This source provides credible manuscript evidence that memory-system choice can shift substantial work into construction and produce large configured differences in call topology, local raw GPU energy, query latency, footprint, and benchmark accuracy. Its phase-aware accounting frame and freshness feasibility inequality are directly useful for `skill-bench`.

It does **not** show that the compared packages are version-reproducible, that taxonomy dimensions cause the observed differences, that rankings are statistically stable, that raw GPU energy is total lifecycle energy, that queueing/caching/cadence recommendations work, that memories are semantically correct or safely deletable, that retrieved evidence is adopted, or that any package improves consequential knowledge work. The right transfer is phase- and workload-conditioned instrumentation—not a memory leaderboard or production prescription.

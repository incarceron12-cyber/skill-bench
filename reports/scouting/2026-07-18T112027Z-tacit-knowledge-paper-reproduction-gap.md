# Scouting note — tacit-knowledge recovery in paper reproduction

- **Timestamp:** 2026-07-18T11:20:27Z
- **Evidence status:** arXiv API metadata/abstract, immutable endpoint checks, targeted web/GitHub release search, and exact repository duplicate searches only. The PDF/source body, tasks, paper graph, official implementations, prompts, traces, outputs, analyses, code, or data were **not** deeply read, downloaded into the repository, reproduced, or audited during scouting.

## Substantive candidate — triage only

**What Papers Don't Tell You: Recovering Tacit Knowledge for Automated Paper Reproduction** — Lehui Li, Ruining Wang, Haochen Song, Yaoxin Mao, Tong Zhang, Yuyao Wang, Jiayi Fan, Yitong Zhang, Jieping Ye, Chengqi Zhang, and Yongshun Gong; arXiv:2603.01801v1.

- Immutable record/PDF/source: https://arxiv.org/abs/2603.01801v1 · https://arxiv.org/pdf/2603.01801v1 · https://export.arxiv.org/e-print/2603.01801v1
- The arXiv API reports immutable v1 submitted and last updated 2 March 2026 in `cs.AI`; its summary contains no withdrawal or retraction notice. The record and PDF returned HTTP 200 in this check, with 42,319 HTML bytes and 11,801,939 PDF bytes. The e-print endpoint reached HTTP 200 but the HTTP/2 transfer terminated after 1,048,576 bytes, so source acquisition is unresolved rather than absent.
- The abstract argues that automated paper reproduction is bottlenecked by omitted tacit knowledge and divides that knowledge into **relational**, **somatic**, and **collective** forms. It proposes relation-aware aggregation over target/citation-neighbor implementation units, execution-feedback refinement from runtime signals, and graph-level induction across papers with similar implementations. On an author-described extended ReproduceBench of 3 domains, 10 tasks, and 40 recent papers, it reports an average 10.04% performance gap against official implementations and a 24.68% improvement over the strongest baseline. These are author-stated claims awaiting full-paper verification; the abstract does not make the denominators or percentage semantics sufficient for interpretation.
- The v1 abstract says code will be released upon acceptance and that the repository link will appear in a final version. Targeted exact-title, arXiv-ID, author-page, web, and GitHub repository searches found no credible official implementation/data release. This is a time-bounded unresolved release observation, not proof of nonrelease.
- Exact ID/title/mechanism searches found no local review or queue task. Existing PaperBench, paper-replication workspace, DeployBench, ReasFlow, AFTER/procedural-memory, and rubric meta-evaluation work covers adjacent scientific execution, decomposition, source-derived procedure, and transfer boundaries, but not this paper's explicit three-part claim that implementation evidence and debugging recover tacit knowledge.

## Why this is a narrow, useful gap

The reusable chain is:

`target paper and authorized source graph → omitted implementation requirement hypothesis → relation/cluster-derived candidate knowledge → runtime failure evidence → refinement/adoption → executable artifact → official-implementation comparison → independently supported scientific reproduction → reusable tacit-transfer claim`.

This directly advances charter objectives A, B, C, and E. The paper could clarify whether tacit expertise can be operationalized through relations among prior artifacts and execution feedback, but its labels may also conflate human experiential knowledge with information recoverable from public implementations, citations, model inference, and iterative debugging. That distinction is central to `skill-bench`: source enrichment, oracle access, search, debugging, procedural induction, and expertise transfer are different interventions and claims.

A full review should test source/target split integrity; whether official target code or near-equivalent citation implementations leak the intended solution; graph-edge and implementation-unit provenance; shared-paper/task clustering; task selection; feedback, attempt, tool, token, and compute parity; stopping and best-of-run selection; ablations; metric direction and normalization; whether an official implementation is a valid scientific oracle; and whether reproduction means execution, numerical agreement, artifact closure, or scientific equivalence. The three domains are a bounded mechanism case, not a benchmark scope commitment. A selected public-paper graph cannot establish tacit expertise, cross-domain transfer, scientific correctness, professional utility, or readiness without additional authority and validity evidence.

## Charter decision filter and queue action

- **Objectives advanced:** A (realistic scientific-agent evaluation), B (expertise-to-evaluation method), C (executable evidence/feedback machinery), and E (clear separation of evidence from expertise-transfer claims).
- **Concrete evidence:** immutable-v1 full-paper/source review and time-bounded release audit reconstructing task/paper sampling, graph provenance, feedback and induction mechanisms, comparator access, ablations, denominators, uncertainty, and score semantics.
- **Uncertainty clarified:** whether the method measures transfer of tacit knowledge or a configured search/debugging package that recovers omitted implementation constraints under selected papers and official-code-relative scoring.
- **Mode:** narrow expansion. One autonomous consolidation task and one human-decision task were pending, while the review backlog was empty; this avoids repeating broad landscape searches.
- **Duplication/scope check:** exact duplicate searches were negative and adjacent reviews cover different links. Reuse evidence, source-pack, procedural-skill, execution, artifact, trace, metric, task-health, configured-system, and validity machinery; add no paper-reproduction-specific subsystem absent stronger evidence.
- **Useful completion:** source-locate every intervention and result denominator, audit release and leakage/feedback boundaries, compare adjacent mechanisms, and preserve strict claim ceilings.

Added one task: `review-tacit-knowledge-paper-reproduction-validity` (review, priority 51). No second source was queued.

# MemoryArena: interdependent sessions test memory-conditioned execution, but do not isolate experience-to-action causality

**Source:** Zexue He et al., *MemoryArena: Benchmarking Agent Memory in Interdependent Multi-Session Agentic Tasks*, arXiv:2602.16313v1 (18 February 2026), 29 pages; https://arxiv.org/abs/2602.16313v1.  
**Immutable paper:** `data/papers/pdfs/2602.16313v1-memoryarena.pdf` (SHA-256 `379c6eb30b30b2e6a4643ea34c2e9d714a68e7b8ff39860110b38ffeb950d76c`)  
**Local text read in full:** `data/papers/text/2602.16313v1-memoryarena.txt` (SHA-256 `8f51c13dc040e36426b29b1d501582fd489cf109db4529a016aa09dfffdefa2b`)  
**Official release inspected:** commit `6cd9de14b71915e39ac742a20dc33785e14b6aab`, tree `e566a1c02e1f40bc94148848c7f8afee32ffc1a8`  
**Release provenance:** `data/sources/releases/2602.16313v1-memoryarena/provenance.json`

## Review status and charter fit

This is a **deep review** based on the complete immutable v1 paper and the complete 205-file official repository snapshot. The only observed release commit was authored 31 May 2026, over three months after v1, and the README labels it a preview; release behavior is therefore post-v1 evidence, not paper-time implementation evidence.

The review advances charter objectives A–C by examining the missing bridge between retained experience and consequential later action. Its four domains are methodological probes, not a proposal to narrow skill-bench to memory systems, shopping, travel, search, or formal reasoning.

## One-sentence contribution

MemoryArena makes retained interaction evidence consequential by evaluating memory-conditioned action over explicitly dependent sessions, while leaving the causal contribution of memory entangled with feedback, agent, environment, and grader treatments.

## Why this matters

It supplies the action-side complement to retrospective experience-memory benchmarks: a later professional artifact or environment state can depend on earlier evidence, but valid attribution requires observing every link between that evidence and the consequence.

## Contribution and research question

MemoryArena asks whether an agent memory system can preserve information acquired through interaction and make it useful in later, explicitly dependent sessions. Its distinctive construction is a sequence of separately prompted subtasks where later choices refer to earlier purchases, plans, search candidates, or intermediate derivations. The paper reports 766 tasks, 6.9 subtasks and 57 actions per task on average, across bundled shopping, group travel, progressive search, and mathematical/physical formal reasoning (pp. 2–5).

This is a stronger target than retrospective recall: memory is placed inside a repeated memory–agent–environment loop. Yet the benchmark evaluates the **configured pipeline**—task model, memory write policy, memory retrieval/presentation, feedback, environment, and grader—not memory in isolation.

## Methodology and system reconstruction

### Task construction

- **Bundled shopping:** 150 six-step chains are generated from WebShop category trees, hand-authored forward/reject maps, three compatible candidates plus incompatible distractors, and a price/rating preference that selects a unique item. Humans inspect chains and prompts (pp. 3–4, 16–17).
- **Group travel:** 45 base itineraries are expanded into 270 groups by adding five to eight travelers with `JOIN` or relative constraints over prior travelers. The underlying database is designed to yield a unique solution and dependency depth up to four (pp. 4–5).
- **Progressive search:** 256 BrowseComp-Plus items survive a model-based “not answerable in one interaction” filter and human decomposition into causally ordered subqueries. Each new query adds a condition; the final answer must satisfy accumulated conditions (pp. 4, 19–20).
- **Formal reasoning:** senior PhD-level math/physics annotators decompose papers into ordered intermediate statements with supplied background and expert answers, yielding 40 math and 20 physics chains (p. 5).

The data sources and supervision differ sharply: templated constraints, database-derived plans, web-answer decomposition, and expert mathematical derivations do not form one validated latent construct.

### Session, state, feedback, and memory policy

For each task, memory begins empty; interaction traces from a completed session are written to persistent memory, then queried for later sessions (pp. 5–6). The paper formalizes `RETRIEVE` at each action and `UPDATE` after each subtask, but Appendix B says experiments usually retrieve once per subtask to reduce cost, with action-level retrieval merely configurable (pp. 6, 17). Shopping is the notable exception described as injecting memory before each decision (p. 20).

The official release confirms domain-specific—not unified—semantics:

- travel initializes memory with the **ground-truth base plan**, grades every traveler, and can write the resulting judge text into memory; in the no-memory path it explicitly accumulates previous plans and judge feedback (`run_travel.py`, lines 190–241, 258–368);
- formal reasoning judges every intermediate answer but by default excludes reward from the memory entry; a configuration can include it (`run_math.py`, lines 154–215);
- progressive search writes each query, trace, and prediction, while the final prompt includes prior results and judgements (paper pp. 19–20; release `run_search.py` and `agent/search.py`);
- shopping exposes optional environment feedback and can include full history independently of the selected memory system (`run_shopping.py`, config fields around lines 220–297).

Thus “experience” is not a stable intervention: depending on domain/condition it may include raw traces, generated answers, exact grader feedback, seeded canonical plans, or cumulative history.

### Systems, scoring, and evidence

The main table uses GPT-5.1-mini as task model and compares long-context buffers, four external-memory systems, and four RAG systems; additional long-context task models are also shown. Progress score is the macro-average fraction of passed subtasks. Task success means all shopping/travel constraints pass, but only final-subtask correctness for search/formal reasoning (pp. 6–8). Travel adds soft constraint credit because hard scores are nearly zero.

The paper reports average task success from 0.12 to 0.23 and shows success-at-depth decay. Long context averages 0.06 shopping SR, 0.00 travel, 0.04 search, 0.23 math, and 0.46 physics; RAG often helps search/reasoning but not shopping/travel (Table 3, pp. 7–8). External memory roughly doubles latency over some long-context models, though no full cost accounting is given (Tables 4–5, pp. 8, 21).

These results support a bounded claim: under these configured systems, later performance is poor and varies with memory representation. They do not establish that memory failure is the earliest cause, that any memory method transfers a learned skill, or that depth causes decay.

## Unique insight

MemoryArena's most useful idea is **dependency-bearing action evaluation**: later artifacts and state changes can require facts or decisions produced earlier, so memory usefulness is assessed by consequences rather than a detached recall quiz.

But its design exposes a more important identification boundary:

> An interdependent sequence makes prior information relevant; it does not prove that the agent retrieved, adopted, and causally used that information, nor that the information arose from experience rather than privileged feedback or repeated task structure.

A final success/failure conflates at least six links: earlier observation quality, memory write fidelity, later retrieval, evidence presentation, agent adoption/reasoning, and grader validity. MemoryArena records enough outputs to score the endpoint but does not report link-level interventions or counterfactual traces that distinguish these mechanisms.

## Limitations and validity threats

### Construct and task validity

1. **Interdependence is authored, not experimentally demonstrated.** A later prompt refers to earlier state, but no oracle/no-history/irrelevant-history intervention measures how often the answer is obtainable from prompt cues, parametric knowledge, database search, or repeated templates.
2. **Dependency depth is confounded with task position and accumulated difficulty.** SR@k decay can arise from survival selection, compounding agent errors, longer context, harder later subtasks, or stricter conjunction—not memory drift alone. No equivalent-form depth randomization or reset crossover is reported.
3. **Domains instantiate different transfer claims.** Shopping/travel mostly require carrying forward exact selected values; progressive search accumulates entity constraints; formal reasoning may reuse answers or domain reasoning patterns. Calling all of these “new skill” acquisition overstates what exact-state carryover demonstrates.
4. **Outcome-conditioned search admission.** Progressive-search items are retained after a large-model agent fails in one interaction, coupling benchmark admission to one configured baseline and making “memory required” partly a model-relative property.
5. **Human validation is under-specified.** Shopping reports manual inspection; search reports human verification; formal reasoning names senior PhD-level experts. Counts, recruitment, independent agreement, adjudication, costs, and error rates are absent.

### Treatment and causal attribution

6. **Feedback is privileged and condition-dependent.** The paper's generic equations store observations/actions, but prompts include judgements and the release can write judge feedback—or even seeded ground-truth plans—into memory. Later success may therefore measure answer-feedback reuse rather than learning from ordinary environment consequences.
7. **No clean no-memory counterfactual.** The published table compares memory architectures, not matched reset/no-memory/oracle-memory conditions. Release no-memory travel explicitly carries prior plans and cumulative judge feedback, so it is not an absence-of-cross-session-information arm.
8. **Memory families are not treatment-isolated.** They differ in providers, indexing delays, abstraction, retrieval, prompting, and sometimes task model/context handling. “0D/1D/2D” is descriptive, not a randomized structural factor.
9. **No access/adoption evidence.** Case studies infer retrieval failure or “lost in the middle” from visible outputs, but no protocol codes whether required evidence was available, model-visible, cited, adopted, and causally necessary.
10. **Environment state is mostly reconstructed rather than naturally persistent.** Separate sessions receive prompts and retrieved records; shopping state and travel plans are carried through benchmark machinery. This is legitimate instrumentation, but not evidence that real heterogeneous applications preserve state similarly.

### Grading and statistics

11. **Non-equivalent success semantics are averaged.** Shopping/travel success is a global conjunction; search/formal success is final-answer correctness. Their unweighted “All Task Avg SR” does not estimate one common construct.
12. **Travel grader is brittle and not constraint-semantic.** The released evaluator uses `difflib.SequenceMatcher` with threshold 0.7 against one canonical plan. Alternate valid descriptions or plans can fail, while superficially similar strings can pass (`env/.../travel_planner_env/eval.py`, lines 10–109).
13. **Search and formal graders include model/exact-answer dependencies.** Search uses a proprietary LLM judge with no reported human agreement; formal answers are evaluated per step, but paper/release do not provide judge calibration or alternate-proof handling.
14. **No uncertainty or repeats.** The paper gives point estimates, default sampling for shopping, temperature 0.1 for search, and temperature 0 for formal reasoning, but no run counts, confidence intervals, seeds, paired estimands, or cluster-aware uncertainty. Tasks share source datasets, templates, papers, and chains.
15. **Latency is incomplete.** Reported completion time omits setup/indexing, storage, API cost, retries, sleep-based indexing waits, hardware utilization, and grader labor. The release contains 50–60 second Mem0 waits, making service behavior part of the result.

### Reproducibility and operational realism

The release is substantial but not a frozen reproduction package. It contains runners, environments, memory adapters, configs, and graders, but labels itself preview code and depends on Hugging Face datasets, external APIs, hosted memory services, H100s, and mutable model endpoints. It has one post-v1 commit, no paper-time tag, no lockfile spanning all environments, no paper result tables or per-item predictions, and no reported seeds/repeats. Shopping code can download tasks/data and bootstrap services; search depends on a decrypted corpus and embeddings; formal/travel depend on external datasets.

Release inspection also finds implementation hazards: `run_math.py` invokes `main(json_config)` once before a second guarded invocation (lines 298–305), potentially duplicating a full paid run; travel's “waiting 10s” message sleeps 50 seconds; and config defaults/feedback paths differ by runner. These do not disprove the paper's results, but prevent treating the snapshot as an exact, inexpensive reproduction.

## Comparison with LongMemEval-V2

LongMemEval-V2 cleanly exposes a bounded **experience-to-evidence** interface: memory returns evidence to a fixed reader, but does not test later action. MemoryArena supplies the missing downstream-action shape, but weakens attribution because write content, feedback, consumer behavior, and graders vary by domain and are not separated.

Together they imply a two-estimand design:

1. **evidence delivery:** did the memory preserve and return sufficient, scoped evidence from prior experience?;
2. **action benefit:** under a matched intervention, did that evidence improve a held-out artifact or environment consequence without harmful transfer?

Neither score substitutes for the other. The existing experience-memory conformance slice already tests this bridge synthetically; MemoryArena supports strengthening its dependency and intervention records rather than creating another schema.

## Transfer to skill-bench

### Adopt

- author explicit dependency edges from earlier observation/artifact/state to later public requirement and private consequence;
- record session resets, persistent state, memory write payload, feedback authority/visibility, retrieval event, presented evidence view, adoption, action, and check outcome separately;
- score intermediate dependency edges and final consequential outcomes as separate families;
- include oracle-memory, no-memory/reset, irrelevant-memory, corrupted-memory, and evidence-only conditions so retrieval, reasoning, and harmful transfer can be distinguished;
- use equivalent-form held-out actions so success cannot be explained by repeated task templates or direct answer reuse;
- preserve domain-specific construct labels rather than averaging unlike conjunction, final-answer, and proof criteria.

### Do not infer

Do not infer general memory ability, longitudinal learning, professional competence, or deployment readiness from low/high endpoint success. Do not label a missing gold item in retrieved text as the root cause without showing model-visible evidence sufficiency and adoption. Do not call judge feedback ordinary experience unless its authority and deployment availability are explicit.

## Concrete repository changes

No new queue task is warranted. The completed experience-memory transfer conformance slice and existing longitudinal, trace, evidence-chain, metric, and validity contracts already cover the nonduplicate requirements. The next empirical use should refine that slice or a future pilot by:

1. adding a declared dependency DAG and one `reset / raw-experience / answer-feedback / oracle-evidence / corrupted-evidence` matched set;
2. measuring evidence availability, access, adoption, intermediate action, final consequence, harmful transfer, and cost separately, with repeated runs clustered by dependency chain.

## Bottom line

MemoryArena advances beyond recall benchmarks by making earlier interaction relevant to later consequential action across separately executed sessions. Its evidence credibly shows that current configured memory–agent pipelines struggle on these authored chains and that representation choices interact strongly with task structure and latency. It does **not** isolate experience-to-action causality: feedback, write policy, retrieval, model reasoning, task depth, and grader behavior remain entangled, with no matched reset/oracle/corruption interventions or uncertainty. For skill-bench, the reusable contribution is the dependency-bearing session design—not a scalar memory score or proof of learned competence.

# Copy-on-Write scoring isolates selected PostgreSQL writes—not the application or the validity claim

## Source and review status

**Deep review of the complete immutable arXiv v1 paper and pinned official releases.** I read the full 15-page paper, including methods, equations, all appendices, workflow prompts, result tables, and sample traces. I inspected the complete pinned `agent-cow-python` library, the complete pinned Plane fork, and every released session- and operation-level result CSV.

- **Paper:** Joanna Roy and Sven Hölzel, *Copy-on-Write Scoring: Application-Specific Agent Evaluations*, arXiv:2607.14336v1, <https://arxiv.org/abs/2607.14336v1>
- **Local PDF:** `data/papers/pdfs/2607.14336v1-copy-on-write-application-evaluation.pdf` (15 pages; SHA-256 `760a39a1d9a7918206dcb520c0fbe703d80330a7a471e4e53ff35e86748a16ad`)
- **Local text:** `data/papers/text/2607.14336v1-copy-on-write-application-evaluation.txt` (SHA-256 `431c45bad0e5a01d58b82e560cb5ba69bc66aa8e7ddfe23ffe89c2f2edf8e7a2`)
- **Library:** <https://github.com/trail-ml/agent-cow-python>, commit `3376d3e06b8855c2e1a2d62606725ef7512d21b6` (30 April 2026), local archive `data/sources/releases/2607.14336v1-copy-on-write-application-evaluation/trail-ml-agent-cow-python-3376d3e.zip` (SHA-256 `3f5c4a782f73da3b77e2b60282c840bc19d12ccb3becf818886cd52ab450bc3b`)
- **Plane fork:** <https://github.com/JoannaRoy/plane-cow>, commit `46d48a94029ce097e3331875bd6714b37ea3ae70` (7 May 2026), local archive `data/sources/releases/2607.14336v1-copy-on-write-application-evaluation/JoannaRoy-plane-cow-46d48a9.zip` (SHA-256 `be4630aa9c1ab1e587e476ee9c521a289997ceceb6158f78f964c069051e4549`)
- **Released results:** `data/sources/releases/2607.14336v1-copy-on-write-application-evaluation/results.zip` (SHA-256 `d13b42f3b605c0b6826c7a5b8d2604b764c25094ea4c116c4e2ea01411765c9c`)
- **Machine-readable audit:** `data/sources/releases/2607.14336v1-copy-on-write-application-evaluation/release-audit.json`
- **Provenance:** `data/sources/releases/2607.14336v1-copy-on-write-application-evaluation/provenance.json`
- **Date read:** 2026-07-17

> **Version boundary.** Both official code snapshots and `results.zip` predate the 15 July arXiv submission by more than two months. The manuscript links the projects but does not name these commits or a paper tag. They are the requested official preview revisions, not cryptographic proof of exact paper-run code. The pinned Plane fork requires `agent-cow==0.1.7` but imports `agentcow.postgres.adapters.django`, which is absent from the pinned public library tree; source-only reproduction from the two archives is therefore not self-contained.

## One-sentence contribution

Copy-on-Write (CoW) Scoring is a valuable application-local observation mechanism that stages selected PostgreSQL row writes by session and operation and compares them with one human-approved witness state, but it neither freezes a complete application world nor proves that row matching, operation deltas, the pre/post tool intervention, or the observed database region establish workflow correctness, causal repair, safe isolation, professional validity, or production readiness.

## Why this matters for skill-bench

This review advances charter objectives A, B, and C through a cross-domain infrastructure question:

> Can a benchmark evaluate an agent directly against a real application's state without maintaining a drifting replica, while retaining isolation, reset, alternate-path acceptance, and diagnostic evidence?

CoW offers a strong partial answer for synchronous PostgreSQL-backed writes. Its unique value is not Plane or project management. It makes one layer of the application state cheap to fork and query, preserving operation IDs and collateral database writes that narrow task predicates might miss. That machinery can strengthen stateful pilots across domains.

Its limits are equally reusable. “Same application” is not “same world”; “all CoW rows” is not “all side effects”; “same final rows as one witness” is not “professional success”; and a large before/after score jump is not a causal estimate of one interface fix. This is expansion and validation of state-observation machinery, not a scope commitment to SaaS or database agents.

## Research question and defensible claim boundary

The paper asks whether application teams can evaluate agent workflows directly inside their software, avoiding replica cost and drift, and use session/operation scores to diagnose and improve model-facing tool surfaces (pp. 1–4).

The strongest supported question is narrower:

> For 20 fully specified, author-approved Plane write workflows, under one discover/execute harness and selected model configurations, how closely do the PostgreSQL rows staged by each agent session resemble the rows staged by one canonical recording, under a configurable matcher that ignores selected fields?

The source supports:

1. a concrete PostgreSQL view/trigger implementation for session-tagged row overlays;
2. an inspectable scoring implementation over matched/missing/extra final rows and operation-attributed writes;
3. an application fork exposing authenticated management endpoints and scoring exclusions;
4. 300 released session records and 3,109 operation rows across three run waves;
5. descriptive evidence that low-scoring traces exposed vocabulary/search and extra-write symptoms, followed by higher scores in a later tool-surface wave for some configurations.

It does **not** establish complete application isolation; transactionally frozen parent state; scorer soundness/completeness; workflow or professional correctness; causal failure localization; causal benefit from the interface intervention; exact-task reliability; production safety; runtime-guard efficacy; representative usage; economic value; cross-application transport; or deployment readiness.

## Methodology and system

### 1. Unit of work and ground-truth construction

The empirical suite contains 20 Plane workflows over three seeded projects, seven users, 63 work items, 26 labels, and 15 states (Appendix C, pp. 9–12). Ground-truth sessions contain 5–32 mutating API calls, 292 total. Prompts prescribe bulk state, label, priority, and assignee changes, often including exact UUIDs and color values.

Ground truth is not a sampled human work trace. Claude Opus 4.6 read the codebase and seeded dump, generated and executed candidate workflows, and drafted prompts. The two authors then checked prompt self-containment and literal agreement between prompt and operations (p. 9). This is useful internal conformance review, but it supplies no practitioner task-demand evidence, independent expert authority, alternative-path elicitation, disagreement record, frequency/severity weights, or downstream stakeholder acceptance.

The “GT session” is one feasible witness. Because prompts are deliberately fully specified, the experiment favors final-state reproducibility and excludes the paper's own acknowledged real condition: underspecified requests with several acceptable outcomes (p. 4). The suite therefore tests execution of benchmark-shaped bulk updates more strongly than domain judgment.

### 2. Parent and overlay state identity

Enabling CoW renames each table to `*_base`, creates a structurally similar `*_changes` table with session/operation metadata, and places a view at the original table name. `INSTEAD OF` triggers redirect inserts, updates, and deletes into the changes table when PostgreSQL session variables are set (Section 2.1; Appendix A, pp. 2, 6; `agentcow/postgres/cow_sql_functions.py`). Reads merge the current base row with the latest visible session row.

This provides real strengths:

- base database writes are avoided for correctly tagged requests;
- concurrent CoW sessions are logically separated by `session_id`;
- final staged rows are queryable without parsing an agent's prose;
- operation IDs permit selective visibility, commit/discard, and post-hoc attribution;
- untouched base state is shared, avoiding full up-front copies.

But the parent is **not a frozen snapshot**. Each overlay continues reading the current base table. A concurrent non-CoW write can change what a running session observes, and GT and agent sessions can be rooted in different effective states unless base mutation is separately prohibited and attested. “Started with the same application state” (p. 3) is an experimental assertion, not an invariant enforced by a state root or snapshot ID.

The SQL projection also has a serious unvalidated semantic boundary. Existing base columns are read as `COALESCE(change, base)`. An intentional update from a non-null value to SQL `NULL` can therefore appear as the old base value rather than the staged null. Trigger construction similarly uses `COALESCE(NEW.column, default)` in generated values. Shared lineage does not guarantee faithful PostgreSQL semantics for nullable updates.

Within one `(session, operation, primary key)`, the changes-table primary key and upsert overwrite earlier writes, so intra-operation sequence is compressed. Across operations, ordering uses `_cow_updated_at`; the scorer calls this “topological” but its implementation sorts operations by earliest timestamp and UUID, not by a full causal dependency DAG (`scoring/extraction.py:26–33`). The library can derive foreign-key operation edges for review/commit, yet `score_sessions` does not use those edges to order utility.

### 3. Isolation envelope

The mechanism intercepts only writes that pass through enabled PostgreSQL views on a connection with the correct transaction-local variables. It does not automatically isolate:

- reads, failed API calls, or discover/search traffic;
- excluded PostgreSQL tables;
- sequences, advisory locks, notifications, or other database-global effects;
- cascade and PostgreSQL-specific trigger behavior, explicitly left for future work (Appendix A, p. 6);
- background jobs and writes on connections that do not inherit the CoW context;
- caches, queues, email, webhooks, network calls, analytics, files, secrets, or external services;
- browser/session state or irreversible recipient effects.

The Plane middleware is fail-open: when `x-agent-session-id` is absent, it is a no-op, so an adapter/harness omission can permit ordinary base writes. If `x-operation-id` is omitted, one is generated, weakening correspondence with the intended tool-call identity. `/api/cow/` bypasses staging so management calls can act on base state. The endpoints require authentication, but the inspected views show no session-owner or role-specific authorization before an authenticated caller can commit a supplied session ID (`apps/api/plane/cow/core/views.py:50–149`). These are application-policy obligations, not properties supplied by database CoW.

The pinned library also includes an S3/blob CoW backend, and 72 blob tests pass locally, but the paper's Plane experiment and score do not include that backend. A complete application-isolation claim would need a resource inventory and fail-closed coverage proof over every mutable channel.

### 4. Session-level scoring

The scorer reduces both sessions to the latest row per `(table, primary key)`. It greedily pairs each GT row with the best unused agent row in the same table and deletion class, runs a second pass after deriving a UUID mapping, and labels unpaired rows missing or extra (Appendix B, pp. 6–8; `scoring/matching.py`). Structural score is:

`matched / (matched + missing + extra)`.

Content is mean field similarity over matched rows. Text uses `SequenceMatcher`, JSON deep equality, most other fields exact equality; primary keys, timestamps, configured fields, and mapped foreign-key IDs are ignored or remapped. The paper's overall score is `0.5 * structural + 0.5 * content` (Equation 5, p. 8).

This admits alternate action paths and UUIDs better than exact trajectory matching. It also creates several validity problems:

1. **A structural match is not a semantic match.** The greedy routine pairs a same-table/same-delete candidate even when similarity is zero. If GT and agent change equal numbers of rows in a table, structurally wrong rows can all count as matched while content absorbs only selected field disagreement.
2. **Greedy UUID alignment is order dependent.** First-pass pairings create the UUID map used in the second pass. There is no global assignment optimization, ambiguity score, tie policy, or adversarial matching test.
3. **Content conditions on matching.** Missing and extra rows do not enter the content denominator. One correct matched row can yield content 1.0 despite many absent obligations; only the separate structural term penalizes them.
4. **Text similarity is not criterion validity.** Lexical closeness can reward semantically wrong descriptions, while legitimate paraphrases or domain equivalences need custom comparators.
5. **Ignored fields erase consequences.** Plane ignores creator/updater identities and timestamps. This may remove incidental variance, but it can also erase ownership, accountability, chronology, or SLA-relevant evidence.
6. **One witness defines expected cardinality.** Legitimate extra audit records, normalized representations, side-effect rows, or alternative entity decompositions can be penalized without an equivalence policy.
7. **No observer-coverage proof exists.** Scoring all dirty enabled tables is broader than a narrow verifier, but exclusions and non-database resources remain invisible; no expected-versus-observed mutation manifest is published.

The scalar is therefore a similarity measure to one selected database-write witness—not a calibrated fraction of workflow value, safety, or professional completion.

### 5. Operation-level utility and causal diagnosis

For each timestamp-ordered agent operation, structural utility is the change in cumulative structural score; content utility is mean final-match similarity for rows whose last surviving write is attributed to that operation (Section 2.2.2, p. 3; Appendix B, pp. 6–8).

This is useful descriptive localization: it can show which operation first added a matched row or an extra row. It is not a causal contribution estimator:

- the delta depends on operation order and the greedy match at that prefix;
- an enabling read has no utility because reads are unobserved;
- an early write can enable a later foreign-key child but receive an unstable or incomplete value assignment;
- a later correction gets final-row content while the erroneous precursor may disappear from final matching;
- create/delete cycles may be dropped with `collapse=True`, hiding risky transient effects;
- correlated multi-row operations receive one aggregate delta;
- failed calls, retries, latency, discovery, and external effects are absent.

Calling these values “useful” operations or dense rewards is therefore a hypothesis. Before optimization, the score needs contrast tests showing that positive/negative deltas align with independent criterion and safety judgments, and that gaming the matcher does not improve reward.

### 6. Configured systems and intervention

The harness embeds Plane's OpenAPI specification in a vector store and exposes `discover` and `execute`, with a nominal 50-operation limit. Five named models receive two initial trials per workflow (200 sessions). After diagnosing vocabulary mismatch between “issues” and “work items,” the authors update the tool surface and run one later trial per cell (100 sessions) (Sections 3–4, pp. 3–4).

This is a useful iterative engineering case, not a controlled intervention:

- all treated trials occur later; there is no concurrent unchanged-tool control;
- tool changes are described selectively rather than released as an exact treatment diff;
- models/providers are mutable and no decoding seeds or request bytes are released;
- there are only two pre and one post attempts per exact cell;
- regression to the mean is likely when changes target observed failures;
- failed-run handling is not predeclared;
- the effect is highly heterogeneous and near ceiling for several models.

Table 1 reports GPT-4.1 `0.32 → 0.79` and Gemini 2.5 Pro `0.43 → 0.98`, while other models improve by `0.01–0.03`. This supports “later configured runs scored higher, especially where the observed interface mismatch mattered.” It does not isolate vocabulary repair, establish expected future benefit, or show that the repaired system is professionally correct.

## Released evidence audit

`results.zip` is materially better than an aggregate-only paper: it contains 15 session CSVs, 15 operation CSVs, 300 unique evaluation rows, and 3,109 operation rows over all 20 workflows. However, it is not a replay package.

### Denominators and missingness

The archive contains 297 `complete` and three `failed` evaluations: two Gemini Flash-Lite pre-intervention failures and one GPT-4.1 post-intervention failure. The paper reports 38/40 completion for Flash-Lite but labels figures and Table 1 with nominal `n=40` or `n=20`. The released files leave failed rows unscored. Whether headline means treat them as zero, omit them, or use another run artifact is not defined tightly enough for exact recomputation.

### Score-definition drift

The pinned library's `default_score_fn` is `0.5 * structural + 0.3 * content + 0.2 * efficiency`, whereas paper Equation 5 defines overall as `0.5 * structural + 0.5 * content`. The CSVs expose both `metric.default_overall` and `metric.structural_content`, but neither released file-mean series exactly reproduces every reported table value. This is not evidence that the qualitative findings are false; it is evidence that score name, formula, scorer commit, and missingness policy are not paper-locked.

### Treatment identity drift

The 300 rows contain nine distinct `candidate_config` strings, including provider/model aliases, one Gemini `request_limit=30` condition, and configurations with no recorded request limit, despite the methods describing a shared 50-operation limit. Run IDs, timestamps, statuses, candidate config, scores, and operation summaries survive; raw model requests/responses, discovery index, tool schemas, harness code, seeded database snapshot/root, GT and agent change rows, scorer hash/config, analysis code, tokens, cost, and human-review records do not.

### Execution attempts

- `uv sync --extra dev` succeeded after dependencies were acquired.
- The initial full test collection failed first for missing optional dependencies; after adding `psycopg-binary`, PostgreSQL tests still could not run because this host has no Docker, PostgreSQL server, `postgres`, `initdb`, or `psql` executable. The documented live PostgreSQL CoW/scoring path was therefore **not reproduced**, and no substitute result is claimed.
- The independent blob test surface executed successfully: **72 passed in 1.81 seconds**. This validates that pinned blob tests pass on this host, not the paper's PostgreSQL experiment.
- The pinned tree has no tests under `agentcow/scoring`, so matcher and scalar conformance are not release-tested there.

## Evidence interpretation

### What is supported

1. Database-level staged writes can expose richer final-state deltas than agent self-reports or narrow task predicates.
2. Session IDs and operation IDs provide useful provenance for selected PostgreSQL rows.
3. Final-state comparison can admit different action sequences and generated UUIDs.
4. Extra writes are diagnostically valuable; the released/paper examples of dozens of unexpected label/assignee rows show why success-only predicates are unsafe.
5. Tool vocabulary and discoverability are part of the configured system and can dominate outcomes.
6. Direct application instrumentation can reduce replica drift for the observed substrate.

### What is not supported

The evidence does not show that CoW captures every application effect, starts from a frozen production state, preserves every PostgreSQL semantic, safely commits selected operations, maps row similarity to user intent, identifies causal root failures, provides valid dense reward, improves future runs under a controlled intervention, predicts real usage, lowers total cost, or makes deployment safe.

The paper reports no integration/runtime cost beyond approximate code lines, no execution cost, no model tokens, no latency, no infrastructure burden, no human recording/review time, and no comparison with snapshot/replica alternatives. “Inexpensive” is therefore a plausible engineering characterization, not a measured cost-effectiveness result.

## Unique insight: an application-local fork needs a typed observation and commit envelope

CoW's central lesson is stronger when separated into three identities:

```text
parent identity
  = database/schema/base-state root + start boundary + concurrent-writer policy

overlay identity
  = session + enabled resources + context propagation + operation ordering

observer identity
  = extracted resource/read set + exclusions + comparator/matcher + score formula

commit identity
  = selected operations + dependencies + authorization + conflict policy + review evidence
```

The paper mainly records session and operation UUIDs. Without the other identities, “directly in the application” can hide four different gaps:

1. the parent changes while the trial runs;
2. writes escape the overlay through an untagged connection or uninstrumented resource;
3. the scorer cannot see a relevant consequence;
4. a later commit applies stale or incomplete changes to a new base state.

For `skill-bench`, copy-on-write should be treated as an **observer/intervention mechanism**, not inherited validity. Every stateful trial needs an envelope manifest with:

- immutable or attested parent root and concurrent-mutation policy;
- complete mutable-resource inventory and interception status;
- context-propagation canaries, including background workers;
- required, forbidden, preserved, and unobserved state regions;
- operation/dependency ledger and intra-operation sequence policy;
- scorer read set, exclusions, matcher ambiguity, accepted alternatives, and version hash;
- pre/post state and non-database side-effect evidence;
- commit/rollback authorization, conflict detection, stale-base policy, and append-only adjudication;
- explicit claim ceiling.

This generalizes beyond PostgreSQL to files, spreadsheets, object stores, tickets, notebooks, APIs, and mixed workspaces.

## Comparison with adjacent reviewed systems

- **AutomationBench** creates a fresh synthetic in-memory world for each task, making parent/reset identity cleaner and all modeled transitions inspectable, but production transport remains unvalidated. CoW uses real application/database code and sees broad dirty-row deltas, repairing substrate fidelity for PostgreSQL while weakening snapshot determinism and leaving non-database effects outside the model.
- **WorkArena L1** runs against native ServiceNow and uses selected state/UI validators with task-specific teardown. CoW avoids a narrow predicate-only observer by comparing all included dirty rows, but its GT matcher still defines a projection and it lacks WorkArena's task-owned lifecycle hooks; neither proves complete collateral preservation or representative knowledge work.
- **WorkArena++** composes setup, actions, validators, and teardown into longer workflows. CoW is path-invariant at session level and therefore better admits alternate sequences, but operation “utility” lacks WorkArena++'s explicit subtask structure and can mistake timestamp order for causal dependency.
- **SaaS-Bench** uses per-run application containers and 1,304 heterogeneous checks over 23 real-code apps. Its parent isolation is heavier but broader; CoW is lighter and directly exposes row deltas, yet both need run-attributable pre/post state, dependency-aware criteria, plural invalidity, and observer coverage. A dirty-row union is not automatically a professional-progress denominator.
- **Synthetic transition-transport work** shows that executable transitions require matched conformance against a trusted reference. CoW skips a replica by using application SQL, but its view/trigger layer itself changes database semantics and therefore needs differential tests for nulls, defaults, triggers, cascades, constraints, retries, concurrency, and background jobs.
- **Production selective re-evaluation** separates invalid evaluator attempts from valid substantive outcomes. CoW results similarly need failed/invalid environment and scoring records to remain in the denominator; omitting three failed evaluations can make later means look like complete observations.

No approach dominates. CoW's defensible niche is **low-copy, operation-attributed observation of selected PostgreSQL write deltas in an instrumented application**.

## Limitations and validity threats

1. Twenty generated, author-reviewed Plane workflows are not a usage or occupational sampling frame.
2. Fully specified bulk-update prompts suppress ambiguity, clarification, approval, exception handling, and stakeholder judgment.
3. One canonical recording is a feasibility witness, not a complete set of acceptable outcomes.
4. The parent base is live rather than content-addressed or transactionally frozen across sessions.
5. Missing CoW headers fail open to ordinary writes.
6. Session variables must propagate on the same transaction/connection; background-worker and connection-pool coverage is not demonstrated.
7. Only selected PostgreSQL writes are isolated; reads, files, queues, caches, webhooks, network effects, email, and external services are outside the score.
8. Excluded tables and ignored fields are application-authored and lack an independent consequence audit.
9. Cascade and PostgreSQL-specific triggers are explicitly unsupported future work.
10. `COALESCE(change, base)` risks losing intentional null updates.
11. Intra-operation repeated writes to one primary key are collapsed.
12. Operation sorting uses earliest timestamps, not the claimed full topological dependency relation.
13. Greedy matching can pair zero-similarity same-table rows and is order/tie dependent.
14. UUID mapping inherits first-pass greedy ambiguity.
15. Content scoring excludes missing/extra rows and uses lexical text similarity by default.
16. Ignored creator/updater/timestamp fields may erase professionally relevant accountability and chronology.
17. Operation deltas are path/order-dependent descriptive changes, not Shapley values or causal effects.
18. `collapse=True` can hide transient create/delete harm if used without a separate safety ledger.
19. Authenticated commit endpoints show no inspected per-session ownership/role policy.
20. Selective commit occurs against the current base; stale-base conflict semantics and review adequacy are not evaluated.
21. Two pre and one post trial per exact cell are insufficient for reliability or stable treatment effects.
22. The pre/post tool change lacks randomization, concurrent controls, exact treatment diff, and outcome-independent selection.
23. Three failed evaluations create unresolved missingness/denominator semantics.
24. Paper and release score formulas/configurations drift, blocking exact table reproduction.
25. The Plane and library snapshots are not self-contained together because the pinned public library lacks the imported Django adapter package.
26. No PostgreSQL scoring tests exist in the pinned scoring module, and the live database path could not run on this host.
27. Raw trajectories, state rows, prompts-as-sent, tool surface, database root, and analysis code are not released.
28. Model/provider aliases and request-limit differences weaken configured-system identity.
29. No human baseline, independent expert acceptance, grader error study, alternate-state contrast set, or downstream utility study is reported.
30. No tokens, cost, latency, integration hours, review burden, commit burden, or alternative-method comparison supports cost claims.
31. A single PostgreSQL application does not establish portability to other schemas, stores, workflows, authority regimes, or professional artifacts.
32. Runtime-safeguard, safety, production-fitness, and readiness claims exceed the evaluated score-only intervention.

## Reproducibility and operational realism

**Instrument inspectability: high.** The paper describes the mechanism and equations; the pinned library exposes SQL generation, overlay reads, commit/discard, extraction, matching, comparators, and score reducers; Plane exposes exclusions, ignored fields, middleware, recording models, and management endpoints; aggregate session and operation CSVs are public.

**Exact paper reproduction: low to moderate.** All 300 aggregate evaluations are present, but exact scorer identity/formula, harness, tool index, seeded database, raw CoW rows, model traces, analysis code, and failed-run policy are missing or inconsistent. The official snapshots are pre-paper and not named by commit in v1. The pinned release pair is not source-self-contained.

**Operational realism: mixed.** Real Django/Plane/PostgreSQL code, schemas, foreign keys, API calls, extra writes, failed calls, vocabulary mismatch, and commit/discard concerns are credible application operations. Seeded fictional data, narrow bulk updates, one app, no live concurrent base changes, no background/resource coverage study, and absent organizational consequence bound the realism.

**Execution verification: bounded.** Blob tests passed. PostgreSQL reproduction was blocked by absent host infrastructure and is not claimed. The release audit records this failure rather than substituting synthetic output.

## Transfer to skill-bench

### Retain

1. Operation- and session-tagged state deltas independent of agent self-report.
2. Final-state scoring that can admit alternate action sequences.
3. Explicit extra-write detection, not only required-state checks.
4. Separate structural and content observations before aggregation.
5. Selective visibility for diagnosis and safe review experiments.
6. Application-local instrumentation as a complement to replicas/simulators.
7. Paired GT/agent witnesses as feasibility and regression tools, with a bounded claim ceiling.
8. Released operation-level evidence rather than aggregate scores alone.

### Repair

1. Bind every trial to a parent state hash/snapshot, schema/app version, start boundary, and concurrent-writer policy.
2. Require a fail-closed context canary: every mutating route and background path must prove session/operation propagation before a trial is valid.
3. Inventory PostgreSQL and non-PostgreSQL resources; emit observed, excluded, unsupported, and escaped effects separately.
4. Replace implicit greedy matching with criterion-aware keys or a versioned global assignment plus ambiguity/tie diagnostics.
5. Preserve complete mutation history even when final-state scoring collapses it; never use net intent as the safety ledger.
6. Add differential database conformance cases for null/default updates, sequences, triggers, cascades, constraints, retries, concurrent base writes, stale commits, and operation reorderings.
7. Treat GT as one accepted witness; maintain expert-approved alternatives, invariants, forbidden regions, and `insufficient_evidence` outcomes.
8. Separate scorer evidence from workflow, professional, safety, and readiness claims through existing validity arguments.
9. Use matched randomized interface interventions or crossover runs with unchanged controls, repeated exact cells, frozen model/provider settings, and predeclared missingness.
10. Report task/model/harness/tool/scorer/app/database identities, failed/invalid denominators, family clusters, uncertainty, tokens, cost, latency, and human review burden.
11. Gate commit on authorization, dependency closure, stale-base conflict detection, full side-effect review, and a rollback plan; evaluation sessions should default to discard.

## Action items

1. **Validation, non-duplicate:** extend the existing transition/observer conformance work rather than adding a CoW-specific schema. Add one resource-envelope fixture with parent root, mutable-resource inventory, fail-closed context canary, complete mutation log, scorer read set, exclusions, escaped effects, and stale-commit policy. Plant null update, untagged background write, sequence increment, cache/blob effect, same-table wrong-row matching, concurrent base change, and failed evaluation cases.
2. **Causal validation, non-duplicate:** when the next tool-surface ablation runs, use repeated randomized or counterbalanced baseline/treatment cells and preserve unchanged controls, exact tool diff, all invalid attempts, and paired task-level estimates. A passing fixture or one pilot contrast must not be promoted to professional capability or production readiness.

No new queue task is added because these requirements refine existing benchmark-bundle state/trace, execution-isolation, transition-transport, task-health, metric-monitoring, and validity-argument machinery.

## Claim ceiling

The immutable paper and pinned releases establish an inspectable method for staging selected PostgreSQL writes, tagging them by session/operation, comparing final dirty rows with one canonical recording, and producing descriptive operation deltas. They also establish 300 released Plane evaluation records and a later-run score increase after a tool-surface revision. They do not establish complete application isolation, frozen production state, faithful handling of all database semantics, valid workflow/professional scoring, causal repair benefit, reliability, runtime safety, cost-effectiveness, production fitness, or deployment readiness. The strongest licensed claim is **application-local conformance to a versioned selected-PostgreSQL-write witness under a named configured system**.

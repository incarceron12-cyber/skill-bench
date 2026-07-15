# MSE-Bench: execution scope is worth measuring, but its oracle is not a minimum

## Source and review status

**Deep review of the complete immutable arXiv v1 paper and the full official commit-pinned release.** I read the complete 27-page paper, inspected the deterministic simulator, task generators, policy implementations, cost/aggregation code, tests, generated tables, LLM-Case tools/tasks/oracles/prompts, all retained live-run rows, and representative trajectory records. I also independently executed all four deterministic policies over the 121 tasks and constructed shorter passing trajectories against the released simulator.

- **Paper:** Junjie Yin and Xinyu Feng, *Do AI Agents Know When a Task Is Simple? Toward Complexity-Aware Reasoning and Execution*, arXiv:2607.13034v1, https://arxiv.org/abs/2607.13034v1
- **Version read:** immutable v1, submitted 14 July 2026; API metadata contains no withdrawal/retraction notice
- **Date read:** 2026-07-15
- **Local PDF:** `data/papers/pdfs/2607.13034v1-msebench.pdf` (27 pages; SHA-256 `67006621d473ad33cf3268da46cabeed6565c3db89904b438981bf9962675aef`)
- **Local text:** `data/papers/text/2607.13034v1-msebench.txt` (SHA-256 `c8848f13d3b2eb26748b2e7491a6f7da4ab1708c3096e04661ea0f21a179b252`)
- **Official release:** https://github.com/eejyin/Do-AI-Agents-Know-When-a-Task-Is-Simple-Toward-Complexity-Aware-Reasoning-and-Execution/tree/44e2bfd438a39ad81e6135851f5c691c61179460
- **Release provenance:** `data/sources/releases/2607.13034v1-msebench/provenance.json`
- **Pinned archive:** `data/sources/releases/2607.13034v1-msebench/repository.zip` (SHA-256 `4e0511b6eda65c5e9214a63e87cffb520b93b2089e80ad6e9b14613dfe20169e`; 135 files)
- **Paper/release boundary:** the pinned commit predates v1 publication by about one day and contains the reported result tables and transcripts. This is strong correspondence evidence, not proof that every manuscript input was produced from exactly that tree.
- **License boundary:** the pinned project has no repository-level license or GitHub-detected license. The vendored `toml` package has its own MIT license, but project-code redistribution/reuse rights remain unverified.
- **Execution boundary:** a clean dependency installation failed with `Disk quota exceeded`, so the documented pandas-dependent test command could not be completed. A dependency-light audit with inert import stubs executed the released task, environment, oracle, and policy classes directly; results are recorded below. This distinguishes an environment failure from a release test failure.
- **Tags:** within-trial efficiency, minimum sufficient execution, execution scope, tool cost, oracle validity, adaptive expansion, configured-system comparison

## One-sentence contribution

The paper makes execution-scope estimation a first-class agent-evaluation construct and demonstrates, in a deterministic authored simulator, that a hand-coded estimate–execute–expand policy can preserve simulator success while using fewer modeled resources—but the released `C_min` is a canonical authored witness rather than a proven minimum, ACRR therefore does not measure exact redundancy, and the 45-run live-model case is too small and treatment-confounded to establish a reliable E3 advantage.

## Why this matters for skill-bench

This review advances charter objectives A, B, and C through a cross-domain instrumentation question: realistic knowledge-work agents can waste time and context by opening every source, invoking every tool, or repeatedly verifying low-risk steps. Current `skill-bench` machinery records trial resources, configured components, traces, task health, and metric estimands, but it should distinguish:

```text
successful artifact/state
+ valid execution envelope
+ raw resource ledger
+ declared sufficient witness path(s)
+ admissible alternative paths
+ reliability target and loss boundary
→ bounded execution-efficiency diagnostic
```

The key transferable insight is **not** the paper's coding-specific three-level policy. It is that task success and execution economy are separate constructs, and economy should be judged relative to the task's legitimate solution set and risk—not relative to the largest available context or one author-preferred path.

The key repair is equally important: **“minimum sufficient” is a validity claim about an optimization problem, not a name that an author can assign to a trajectory.**

## Research questions and defensible claim boundary

The paper asks (Section 1, pp. 2–3):

1. Can the effort a task ought to require be formalized and actual effort compared with it?
2. Can an agent cheaply estimate required execution scope before acting?
3. Can starting minimally and expanding after failed verification preserve success while reducing cost versus maximal-context collection?

The strongest defensible paper/release claim is:

> In the released deterministic environment, over 121 procedurally generated edit records, the authored E3 policy passes every checker and has lower mean modeled scalar cost than the authored Adaptive Retrieval and Max-Context-First policies under almost all sampled nonnegative weight vectors; its progressive expansion recovers the 18 deliberately under-scoped template cases.

The evidence does **not** establish:

- that the released oracle is the cheapest passing trajectory under the simulator's own action semantics;
- that ACRR is exact, nonnegative excess over a true minimum, or stable across alternative valid paths;
- that the three authored task tiers represent natural execution complexity outside these templates;
- that verification failure is an unbiased or answer-free scope-expansion signal;
- a reliable causal effect of the E3 prompt on live-model success, cost, or latency;
- generalization across models, harnesses, repositories, artifact classes, or knowledge-work domains;
- professional validity, reliability, production fitness, safety, or readiness.

## Methodology and system

### Formal objective

A task is `τ=(q,E,V)` and a trajectory is a sequence of tool actions. Cost is a weighted sum of modeled latency, tokens, tool calls, and fully inspected files:

`C(π)=αT_lat + βN_tok + γN_tool + δN_file`.

The paper defines `π*` as the cheapest trajectory meeting success probability `1-ε`, calls its cost `C_min`, and defines ACRR as `(C_actual-C_min)/C_min` for successful runs only (Section 3, pp. 7–8). This formulation is useful because it separates resource use from success. But the experiments do not solve that constrained optimization problem or estimate success probability. They execute one hand-authored oracle once in a deterministic environment.

### MSE-Bench task generator

The benchmark contains 121 records (Section 5, pp. 10–11; `e3/benchmark.py`):

- 41 Level-1 records: one direct site;
- 40 Level-2 records: two literal direct sites;
- 40 Level-3 records: two literal sites plus one authored indirect alias/re-export site;
- 18 Level-3 records receive localized “deceptive” wording.

The 120 parametric records come from one archetype per level, with randomized identifiers, filler, and five-to-eight distractor files. The Gmail-icon example supplies the additional Level-1 record. This is repeated template instantiation, not 121 independent task designs. Identifiers and filler change surface form; they do not create 121 independent complexity mechanisms.

The paraphrase test changes instructions while keeping repositories, sites, oracle, levels, and checker unchanged. It usefully breaks selected estimator keywords, but it is not a held-out task distribution or independent paraphrase sample: the alternative templates are authored in the same release specifically to avoid the estimator's listed cues (`e3/benchmark.py`, lines 18–26, 132–266).

### Capability-controlled environment

The in-memory environment exposes directory listing, literal search, partial/full read, dependency trace, edit, reasoning, and verification (`e3/environment.py`). Direct sites become editable merely when their file name has been observed by search; indirect sites require a full inspection. `_apply_reachable_sites` then makes every reachable correct replacement without agent uncertainty (`e3/policies.py`, lines 55–63).

This cleanly controls edit capability, but also embeds the task solution into environment semantics:

- search need only reveal a filename/count before a direct correct edit can be applied;
- dependency tracing is an authored one-hop graph lookup;
- the policy never chooses replacement content or an alternative patch;
- the checker tests the exact author-listed sites;
- modeled “latency” and “reasoning tokens” are deterministic charges, not measurements;
- verification returns a scalar pass/fail over the same hidden site list.

Thus MSE-Bench measures the resource consequences of four hand-written control flows over a small transition system. It does not measure whether an LLM knows a task is simple.

### Policies and intervention

The four policies are implemented as Python functions (`e3/policies.py`):

- **Max-Context-First** lists directories, reads every file, adds 1,200 reasoning tokens, edits all reachable sites, and runs heavy verification.
- **Fixed ReAct** searches, adds 200 tokens, partially reads hits, edits reachable sites, and verifies once; it cannot reach any indirect site.
- **Adaptive Retrieval** searches, fully reads hits, traces dependencies whenever there is more than one hit, fully reads new importers, edits, and runs heavy verification.
- **E3** uses lexical rules plus at most one search to choose level 1–3, executes that level, and increments scope after a failed checker.

The policies differ in more than “scope estimation.” They have different fixed reasoning charges, partial/full-read choices, verification heaviness, dependency triggers, retries, and action orders. The E3-versus-Adaptive-Retrieval contrast is narrower than E3-versus-MCF, but still bundles estimation with read granularity, verification policy, reasoning charges, and an expansion controller.

### Live LLM-Case

LLM-Case uses five edits over vendored `toml` 0.10.2, three system prompts, gpt-4o, six tools, hidden per-task pytest graders, and three attempts per cell (Section 7.7, pp. 17–20). The 45 retained rows are inspectable in `llm_case/results/openai_r3/llm_runs.csv`.

This is more realistic than the simulator, but the treatment remains a prompt package:

- MCF instructs the model to list every directory and read every source file;
- ReAct instructs a brief reason–act loop;
- E3 explicitly states the three complexity classes, limits the initial probe, orders reads, and says to expand only after tests fail (`llm_case/llm_case/prompts.py`).

Prompt length, task decomposition, risk posture, and tool-use rules all differ. The study measures three prompted configured packages, not an isolated latent ability to estimate complexity.

## Evidence and independent release audit

### Deterministic results reproduce at the policy layer

The dependency-light audit directly executed every released policy over `build_benchmark()` and reproduced the paper's central totals:

| Policy | Passing records | Mean modeled cost |
|---|---:|---:|
| MaxContextFirst | 121/121 | 122.851 |
| FixedReAct | 81/121 | 17.158 |
| AdaptiveRetrieval | 121/121 | 22.076 |
| E3 | 121/121 | 18.551 |

These results confirm that the checked-in implementation generates the reported simulator ordering. They do not validate the cost model or oracle.

### The released `C_min` is not minimal

The most consequential audit result is an executable counterexample inside the released environment.

For the first Level-2 record (`L2_000`):

- released oracle: `search → read_range ×2 → edit ×2 → verify`, cost **10.28**;
- shorter passing trajectory: `search → edit ×2 → verify`, cost **7.68**.

It passes because `search` marks both direct-site files observed, and `_apply_reachable_sites` permits correct edits once a direct file is observed. The two partial reads in the oracle are unnecessary under the simulator's own capability contract.

For the first Level-3 record (`L3_000_dec`):

- released oracle cost: **19.98**;
- passing trajectory that searches, traces, fully inspects only the known indirect-site file, applies all three edits, and verifies: **19.22**.

The released oracle partially reads all three sites even though search already grants editability for the two direct sites. The smaller trajectory uses author knowledge to select the indirect importer, just as the released oracle uses author knowledge to enumerate all sites.

Level 1 happened to tie at **6.00** for the audited search/edit/verify alternative and the released read/edit/verify oracle. Therefore this is not a universal issue with every row, but it falsifies the statement that every task's `C_min` is exact. No search algorithm, lower-bound proof, dominance enumeration, or independent expert-path adjudication is supplied.

Consequences:

1. `C_min` should be renamed a **canonical sufficient witness cost**.
2. ACRR is “excess relative to that witness,” not exact redundancy.
3. ACRR can depend on which valid witness the author selected.
4. Weight sensitivity cannot repair a wrong feasible-set minimum; it only reweights observed policy vectors.
5. The paper's central normalization claim is weaker than its raw policy-cost comparison.

### Cost-weight robustness is conditional, not construct validation

The 4,000 weight vectors are sampled independently from author-chosen boxes and applied to mean resource vectors (Section 7.5, pp. 15–16; `e3/metrics.py`, lines 100–160). This shows the observed mean E3 vector usually has a favorable linear projection within those ranges. It does not show:

- that the axes are complete or commensurable;
- that file count should be additive with cumulative prompt tokens;
- that task-specific risk changes the weights;
- that repeated reads, cached context, memory pressure, energy, human review, or consequence loss are represented;
- that the sampled box corresponds to any user population;
- that the oracle remains minimal under each weighting.

The paper says ACRR is scale-free in overall weight magnitude. That is true for common scalar multiplication, but ACRR is not invariant to relative weights, because both numerator and denominator depend on trajectory-specific axis mixtures.

### Verification is both safety mechanism and privileged signal

E3 expands after the authored checker fails. In MSE-Bench that checker exactly recognizes whether every hidden author-listed replacement has occurred. This is a strong and unusually cheap signal. Real knowledge work often has:

- delayed or destructive consequences;
- graders that cannot run during the task;
- partial, noisy, or abstaining verification;
- hidden checks that must not reveal private answer structure;
- alternative valid artifacts;
- safety obligations where “try minimal, then expand after failure” is unacceptable.

The simulator does not reveal the missing filename in its Boolean return, so it does not directly leak an answer string. But the pass/fail gate still supplies privileged, perfectly aligned evidence that further scope is required, and repeated execution is free of contamination or state damage. The E3 guarantee is therefore conditional on a sound, complete, cheap, repeatable verifier and bounded monotone scope ladder.

### Live-model evidence is small and nonuniform

The retained 45 rows show:

- ReAct: 15/15 passing;
- E3: 14/15 passing, with one provider 429;
- MCF-thorough: 12/15 passing, with three Level-3 failures (one 429, one max-step exhaustion, and one finished wrong patch).

On Level-1/2, all conditions pass, but E3 is cheaper on the large comment-decoder task and more expensive on the array-separator task. On the Level-3 task, ReAct passes 3/3, E3 passes 2/3 with one 429, and MCF passes 0/3. The paper appropriately calls this a case study, yet “effectively equal task success” and “leanest reliable policy” remain stronger than the sample supports.

Important statistical and operational limits:

- one model, one provider organization/rate limit, one ten-file library, five closely related rename/version tasks;
- three attempts per cell and no paired seeds or randomization evidence;
- no task-clustered interval, paired effect, or provider-failure estimand;
- mean cost includes failed trajectories, while ACRR excludes them;
- provider 429 is not an agent edit error, but it is an operational consequence of cumulative context and belongs in a separately typed availability/resource outcome rather than being dropped from reliability reasoning;
- all five task instructions disclose much of the required final state, and the hidden graders enforce specific rename behavior;
- run-level prompt tokens are cumulative provider input usage, while the “measured oracle” uses one estimated instruction-plus-file token pass with zero model output/reasoning tokens.

The LLM-Case `C_min` is especially misnamed. Its oracle reads every gold file, applies gold replacements directly in Python, adds an estimated one-pass token floor, and runs tests (`llm_case/llm_case/tasks.py`, lines 103–147). It is not an attainable trajectory for the evaluated LLM agent under the same model-turn process, nor is it proven cheapest. Comparing cumulative multi-turn provider tokens with this synthetic one-pass floor makes live ACRR values (roughly 8–30 on passing rows) a distance from an engineered lower witness, not measured cognitive redundancy.

## Unique insight

The paper's genuinely useful contribution is a missing coordinate in agent evaluation:

> **Execution scope is a decision made during a trial, not merely a cost observed after it.**

A resource ledger says how much was spent. An execution-scope record explains why the agent widened or stopped:

```text
initial scope hypothesis
+ evidence available before action
+ risk and confidence
+ minimal planned path
+ verification admissibility
+ expansion trigger
+ newly admitted evidence/tool/artifact scope
+ stop reason
+ final quality and resource vector
```

This differs from earlier `skill-bench` evidence:

- [Efficient Benchmarking of AI Agents](2026-07-09-efficient-benchmarking-ai-agents.md) reduces the **number of benchmark items** while trying to preserve rankings.
- [Partial agent-benchmark decisions](2026-07-15-partial-agent-benchmark-decision-validity.md) reduces the **number of revealed task outcomes** while trying to preserve one completed-record pairwise decision.
- [ACON](2026-07-13-acon-context-compression-validity.md) reduces **agent-visible state** through a lossy transformation.
- MSE-Bench targets **within-trial search/read/tool scope** while holding a task and nominal end-state checker fixed.

These efficiencies have different denominators and validity threats. A small benchmark panel can contain wasteful trials; a lean trial can run on an invalid panel; compressed context can reduce tokens while corrupting state; and a canonical witness path can be cheap without being minimal.

## Limitations and validity threats

1. `C_min` is assigned by one authored trajectory rather than identified by optimization, proof, or exhaustive dominance checking.
2. Executable counterexamples are cheaper than the released oracle on Level-2 and Level-3 records.
3. Success probability and reliability target `1-ε` appear in the formal definition but disappear in the deterministic implementation.
4. The simulator embeds correct edit capability and exact replacement content outside the policy.
5. Task, oracle, checker, estimator cues, policy, and cost model are co-authored, creating favorable structural alignment.
6. The 121 records instantiate three archetypes; random names and filler do not provide independent complexity diversity.
7. Complexity level is author-defined by required site pattern, not validated against human effort, agent cost, error risk, or alternative paths.
8. The 18 deceptive cases are deterministic template assignments, not naturally occurring hidden complexity.
9. Paraphrases are authored to break known lexical rules over unchanged repositories and are not a held-out task/form sample.
10. E3 and baselines differ in reasoning charges, read granularity, verifier choice, retries, and action ordering, not only estimation.
11. Max-Context-First is an explicit mechanical upper bound, not observed frontier-agent behavior.
12. Adaptive Retrieval's dependency trigger (`len(hits)>1`) is tailored to the generated task structure.
13. File cost increments on every full inspection action despite documentation calling it distinct-file count; repeated full reads can therefore be mislabeled as distinct files in the simulator ledger.
14. Modeled latency/tokens are fixed charges; they are not empirical resource measurements.
15. Weight sensitivity samples a chosen box and cannot validate missing axes, oracle minimality, or user utility.
16. ACRR excludes failures, so it cannot be compared or aggregated without a separate reliability estimand and loss basis.
17. Perfect cheap verification makes optimistic expansion safer than in many consequential workflows.
18. Boolean verifier failure may still act as privileged scope evidence unavailable during real task execution.
19. LLM-Case has only five related coding tasks, one model, one provider, and three attempts per cell.
20. Prompt treatments bundle strategy, decomposition, constraints, and prompt length.
21. The live “thorough” model does not comply with “read every source file,” weakening treatment realization.
22. Provider 429, max-step exhaustion, and wrong edit are distinct outcomes but are pooled into task success summaries.
23. Mean live costs include failed runs while ACRR is success-only, producing incompatible populations.
24. LLM-Case's oracle uses direct gold edits and estimated one-pass tokens, not the evaluated model/harness's attainable minimum.
25. The public test dependency set is unpinned; full documented tests could not be rerun in this environment because installation exceeded disk quota.
26. The release has no project-level license, so inspectability does not imply permission to reuse or redistribute its code.
27. No human engineer baseline, expert path diversity, professional-quality review, or consequential-risk study is provided.
28. Coding edits are a bounded instrumentation case, not evidence of transport to cross-domain knowledge work.

## Reproducibility and operational realism

**Simulator reproducibility: high at the implementation/output layer, low at the construct-minimum layer.** The release preserves deterministic generators, policies, seeds, cost tables, result CSVs, tests, and figure inputs. Direct execution reproduced all four policies' success totals and mean costs. However, reproducing an authored number does not validate its interpretation as a true minimum or cognitive redundancy.

**LLM-Case reproducibility: moderate for artifact inspection, low for independent result replication.** The release includes tool code, five tasks, acceptance modules, oracle tables, 45 result rows, and transcripts. It does not pin the exact gpt-4o snapshot, provider service state, organization rate limit, dependency lock, or randomized run schedule. The retained evidence supports an audit of what happened, not exact re-execution.

Operational realism is mixed. Real files, pytest, hidden acceptance modules, cumulative provider usage, wrong patches, step exhaustion, and rate limiting are valuable. Yet the task family is tiny, the repository is vendored and static, tools have no network, tests are cheap and aligned, changes are reversible, and no human/expert artifact judgment is required. Real knowledge work needs source authority, contradiction handling, multiple legitimate workflows, delayed checks, review costs, and asymmetric failure consequences.

## Transfer to skill-bench

### Retain

1. **Record scope estimates as trace events.** Capture estimated difficulty/scope, confidence, risk, cheap probes, planned files/tools/evidence, and rationale before major execution.
2. **Separate raw resource axes.** Keep wall time, provider usage, tool calls, artifact/source reads, full-context bytes, retries, grader calls, and human-review minutes separate from any scalarization.
3. **Record expansion causally.** Link each scope increase to a typed trigger: verifier failure, contradiction, missing authority, invalid artifact, tool error, low confidence, or safety requirement.
4. **Use fail-closed stopping.** A low-cost stop counts as efficient only if the artifact/state, required evidence views, and critical checks are valid.
5. **Compare against adaptive baselines.** “Read everything” is a stress bound, not sufficient evidence of useful efficiency.
6. **Preserve service failures.** Provider throttling can be a real cost consequence even when it is not an agent reasoning failure.

### Repair

1. **Rename unproven minima.** Use `canonical_sufficient_witness_cost`, not `C_min`, unless the action space and success constraint admit a lower-bound proof or exhaustive/solver-backed search.
2. **Represent multiple witness paths.** Record alternative valid procedures, artifact conventions, resource vectors, authority, and evidence of sufficiency. Compute a Pareto frontier before scalarizing.
3. **Add oracle-admissibility evidence.** State whether the witness uses hidden task author knowledge, gold edits, private graders, impossible model state, or unavailable tools.
4. **Test dominance automatically.** For bounded simulators, enumerate or search shorter trajectories and reject “minimum” labels when any passing path dominates the oracle on all declared axes or under the chosen scalar cost.
5. **Bind efficiency to reliability and loss.** Report quality/reliability at fixed resource budgets or resource use at fixed valid-quality targets; do not average efficiency only over survivors without the failure denominator.
6. **Factor the E3 treatment.** Compare estimate-only, progressive expansion without an explicit estimate, verifier policy, read granularity, and prompt-length/decomposition controls.
7. **Vary verifier observability.** Test exact deterministic checks, partial checks, abstention, delayed review, noisy model graders, and unavailable-at-runtime private checks.
8. **Use cross-domain execution mechanisms.** Examples include source-authority lookup in a memo, dependency tracing in a spreadsheet, evidence reconciliation in research, and compliance review in a workflow state—not coding labels copied wholesale.
9. **Estimate path diversity.** Expert sessions should elicit multiple legitimate sufficient paths and context-dependent escalation rules rather than one canonical “expert minimum.”
10. **Predeclare cost utilities.** Scalar weights should be claim/use specific, include consequence and reviewer burden, and be sensitivity-tested over justified ranges.

### Existing contract homes

No new coding-specific schema is warranted. The implications refine existing machinery:

- benchmark bundle/traces: scope estimate, expansion trigger, resource ledger, verifier visibility;
- artifact admissibility: what evidence views can support stop/expand decisions;
- task health: witness-path validation, oracle defects, saturation, revision without score rewriting;
- metric monitoring: eligible successful/invalid/service-failure populations, units, clustering, uncertainty, and scalarization basis;
- validity arguments: distinguish canonical-witness-relative economy from minimum-relative redundancy and from professional efficiency;
- expertise transfer: provenance and context limits for expert-elicited sufficient paths.

## Action items

1. In the next execution-efficiency consolidation, add a terminology rule: `minimum` requires optimization/proof evidence; otherwise use `sufficient witness`, record oracle privilege, and preserve alternative-path/Pareto information.
2. When repeated cross-domain pilot trials exist, derive an execution-scope analysis from real traces: quality-valid attempts only for conditional efficiency, all attempts for joint utility/reliability, typed provider failures, and task-family-clustered uncertainty.
3. Add a bounded oracle-dominance mutation to an existing task-health or benchmark-bundle conformance suite when that contract is next revised: plant an authored witness with unnecessary reads and require detection of a cheaper passing path. This is a refinement, not a new queue task.
4. Do not adopt ACRR as a headline metric until the denominator has an admissibility class and the claim says exactly whether it is a proof-backed minimum, empirical best-known path, expert witness, or author reference.

## Bottom line

MSE-Bench correctly identifies a neglected evaluation dimension: agents should be judged not only on whether they finish, but on whether they choose a task-appropriate execution scope and expand for evidence-backed reasons. Its deterministic release is unusually inspectable, and the raw E3-versus-authored-policy cost ordering is reproducible. The strongest interpretation fails, however, inside the released simulator: cheaper passing trajectories exist than the object called `C_min`. ACRR is therefore reference-witness-relative overhead, not exact cognitive redundancy. The live gpt-4o case further shows that real agents are much less extreme than the simulator's MCF bound and that E3's small, nonuniform advantage is not yet reliable. `skill-bench` should adopt scope-estimate and expansion-event instrumentation, preserve plural resource/reliability outcomes, and require proof or dominance evidence before calling any expert- or author-provided path “minimum.”

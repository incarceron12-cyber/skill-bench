# WorkBench Revisited: longitudinal progress, instrument drift, and tail-risk validity

**Deep review of full primary sources and pinned releases**

The local PDFs and complete local text extractions listed below were read in full; release claims were then checked against both pinned official archives.

- Styles, O. and Miller, S. (2026), *WorkBench Revisited: Workplace Agents Two Years On*, arXiv:2606.13715v2, immutable PDF: https://arxiv.org/pdf/2606.13715v2
- Styles et al. (2024), *WorkBench: a Benchmark Dataset for Agents in a Realistic Workplace Setting*, arXiv:2405.00823v2 / COLM 2024, immutable PDF: https://arxiv.org/pdf/2405.00823v2
- Local paper evidence: `data/papers/pdfs/2606.13715v2-workbench-revisited.pdf`, `data/papers/text/2606.13715v2-workbench-revisited.txt`, `data/papers/pdfs/2405.00823-workbench.pdf`, and `data/papers/text/2405.00823-workbench.txt`
- Official release evidence: `data/sources/releases/workbench-2026/WorkBench-da6f8ee8.zip` at commit `da6f8ee8d9f8efc87b2f5f3cc9edc1befdac726e`; near-publication 2024 snapshot `data/sources/releases/workbench-2026/WorkBench-42f1b6dc-2024-snapshot.zip` at `42f1b6dc18986f47701ca83de2d63dd4f95c59a0`; provenance and timing limits in `data/sources/releases/workbench-2026/provenance.json`

## Bottom line

WorkBench Revisited is unusually useful because it exposes benchmark maintenance as part of the measurement rather than pretending the 2024 instrument remained fixed. It shows two genuine facts: current configured systems perform very well on the **corrected 2026 WorkBench**, and incorrect state-changing actions are much rarer among the strongest systems than among weaker systems on that same instrument. It does **not** identify how much of the 2024–2026 headline gain comes from model capability, native tool calling, benchmark repairs, public-task exposure, or changed serving conditions. The paper itself concedes the strongest point: a 2026 score is not directly comparable to a 2024 score (Appendix A.1.1, pp. 6–7).

The distinctive lesson for `skill-bench` is therefore not “benchmarks saturate.” It is that a benchmark needs two simultaneous products: a **frozen longitudinal anchor** for trend claims and a **maintained operational form** for fair current-system measurement. Corrections should create explicit bridges, not retroactively make old and new scores look homogeneous. Tail harms also need severity and opportunity denominators: WorkBench's binary side-effect rate usefully separates harmless failure from changed state, but it collapses an extra plot, a wrong CRM update, and an irreversible email into one event class.

## One-sentence contribution

WorkBench Revisited provides an inspectable current cross-section of deterministic workplace state-transition performance and, more importantly, documents why repairs to tasks, graders, tools, and harnesses prevent its 2024 and 2026 headline scores from forming one clean longitudinal estimand.

## Why this matters

The paper is a rare primary-source lifecycle case in which benchmark maintainers preserve old ground truth, disclose defects, quantify a correction bridge, and explicitly bound over-time claims. That combination directly tests `skill-bench`'s task-health, versioning, validity, reliability, and renewal machinery.

## Research question

The original paper asks whether tool-using agents can execute common workplace requests in a deterministic sandbox and proposes outcome-centric evaluation: compare the final state of five databases against a generated target state rather than matching a prescribed action sequence (2024 §§3–4, pp. 3–9). The revisit asks how performance, unintended state changes, cost, and failure modes have changed after two years of model and harness progress (2026 §§1–4, pp. 1–5), while documenting benchmark corrections (Appendix A, pp. 6–7).

The contribution is threefold:

1. a 690-task, 69-template benchmark over email, calendar, analytics, CRM, project management, and cross-domain workflows;
2. a deterministic final-state evaluator that admits alternate and repaired action paths;
3. a 24-model current cross-section plus a candid instrument-change audit and committed per-task results.

The revisit is strongest as a **current cross-sectional evaluation and lifecycle case study**, not as a clean longitudinal causal study.

## Methodology and system

### Task universe and environment

The universe remains 690 generated instances: 120 analytics, 110 calendar, 80 CRM, 90 email, 80 project-management, and 210 multi-domain tasks, ten instances per 69 manually written templates (2024 §3.2 and Table 3, pp. 5–6). The sandbox contains fixed tables of 300 calendar events, 500 emails, 500 analytics records, 200 customers, and 300 project tasks, exposed through 26 read/write tools (2024 §3.1 and Table 4, pp. 4–7; 2026 §1, p. 2). Tasks may require up to 12 state-changing actions; 122/690 require no state change after retrieval and condition checking (2024 Appendix A.4, p. 17).

This is reproducible and diagnostically useful, but only thinly “workplace realistic”: no human baseline, stakeholder study, occupational sampling frame, multi-turn clarification, collaboration, permissions, long histories, spam, or downstream organizational consequences are measured (2024 §5, pp. 9–10; 2026 §4, p. 5).

### Configured systems

The 2024 results used a LangChain ReAct loop with free-text action parsing, up to 20 iterations and 120 seconds, with malformed/no-action cases retried up to five times at temperature 0.5 for GPT-4's reported 43% all-tools result (2024 §§4.2–4.4, pp. 8–9; pinned old `scripts/inference/generate_results.py`). Some systems could not fit all tool descriptions in context, producing 0% all-tools values; the paper also reports required-domain-tools conditions.

The 2026 experiment gives every model all 26 tools, uses native structured tool calls, allows up to 20 steps, and sets temperature zero where supported (2026 §2.1, p. 2). The release routes requests either directly to vendors or through OpenRouter and records provider, base URL, model ID, tool-selection policy, structured-output status, and ground-truth version in per-domain metadata sidecars (`README.md`; current `src/evals/agent.py` and `src/evals/inference.py`). These records improve reproduction, but provider route and model snapshot remain part of the treatment; “same modern harness” does not make proprietary serving conditions immutable.

### Scoring

A trial is correct when executing its predicted write actions yields the same final state as the target actions, after some normalization. A harmful side effect is counted when the prediction changes any sandbox state and does not reach the correct final state (2024 §4.1, p. 8; current `src/evals/metrics.py` and `src/evals/evaluation.py`). Thus each task falls into correct, incorrect with no state change, or incorrect with state change.

This is an excellent **state-transition predicate**, but “harmful” is an interpretation layered on top. The implementation is not a harm model: it has no severity, reversibility, actor, affected party, exposure duration, or opportunity normalization. Correct completion can itself involve consequential actions, while an unnecessary reversible plot is counted with a wrong-recipient email. Failed tool calls that do not change state are harmless by definition even if they reveal confidentiality or consume resources outside the simulated state.

Cost is estimated from string lengths at four characters/token, adds about 7,000 repeated prompt/schema tokens per call, applies published uncached rates, and divides total run cost by all 690 tasks (2026 §2.1, pp. 2–3). It is an upper-bound ordering, not billed spend; the release says traces needed to recreate costs are omitted for size (`README.md`).

## Evidence

On the corrected 2026 form, Table 1 reports Fable 5 at 674/690 correct (97.7%) and 13/690 side effects (1.9%); Opus 4.8 at 96.2%/2.5%; Gemini 3.1 Pro at 95.5%/2.9%; and a range down to GPT-3.5 at 31.3%/38.7% (2026 §2.2, p. 3). The committed `retro/data/model_results.json` ties model totals to six per-domain result files and records the ground-truth version. This makes headline counts substantially more inspectable than many agent benchmarks.

The best remaining failures involve condition overreach, incomparable-unit reasoning, and treating a capped five-item search as complete (2026 Appendix B, p. 7). These are credible reusable failure signatures: threshold semantics, dimensional consistency, and evidence-completeness tracking.

However:

- every 2026 model appears to receive one attempt per task; there are no repeated trials, confidence intervals, paired bootstrap intervals, or template-clustered uncertainty;
- the 690 rows are only 69 generated template clusters, so treating them as 690 independent workplace situations overstates precision and construct breadth;
- the paper describes the capability–side-effect relationship visually/descriptively and reports no adjusted model across template difficulty, model family, harness, or state-change opportunity;
- per-model safety rates are divided by **all** 690 tasks, not tasks presenting comparable irreversible-action opportunities;
- no human validation or severity coding is reported for the claimed residual irreversible harms.

The inverse completion/side-effect pattern is partly mechanical: correct trials cannot be side-effect trials under the mutually exclusive outcome definition. A more informative safety comparison would estimate harmful-state-change risk conditional on failure, on action opportunity, and by severity. For Fable 5, 13 side effects among 16 failures means the remaining errors are mostly state-changing even though the all-task rate is low; this materially differs from the reassuring “1.9%” framing.

## 2024/2026 instrument crosswalk

| Layer | 2024 instrument | 2026 instrument | Comparability implication |
|---|---|---|---|
| Task count/templates | 690 instances, 69 templates, six domain groups | Same declared counts/groups | Stable labels do not imply identical task text or target semantics. |
| Task text | Original generated query files | Corrected top-level v2 task/outcome files | Local exact-text audit finds 627/690 shared task strings: analytics 120/120, calendar 109/110, CRM 73/80, email 80/90, multi-domain 182/210, project management 70/80. Sixty-three old strings are replaced by 63 new strings. |
| Ground truth | Original answer/action files; no sidecars | Versioned `v1` snapshot plus current `v2`; sidecars select the scorer | This preserves old-score reproduction. Among exact shared task strings, the serialized outcome is unchanged; changed semantics sit primarily in renamed/rewritten rows and evaluator acceptance rules. |
| Scoring | State comparison with order-sensitive and data/ground-truth defects | Corrections, order-independent grading, alternate plot end date, fixed CRM/data logic | Paper's “hard floor” is 56 tasks (8%); broader pass-affecting scope is about 90–95 (14%) (2026 Appendix A.1.1, pp. 6–7). |
| Tool contract | Search caps and enum rules incompletely disclosed; project search capped at five | Clearer enum/cap docs; project search raised to 200 for counting tasks | The task affordance and information treatment changed, not just bookkeeping. |
| Harness | Free-text ReAct parsing, malformed-action retries, mixed temperatures | Native structured calls, maximum 20 steps, temperature zero where possible | Removes a major measured failure source; this is scaffold progress, not model-only progress. |
| Model bridge | GPT-4 all-tools 43%; required-tools 49%; retry policy involved | Paper says GPT-4 moved from 49% old to 57% corrected when “resampled the same way” | The eight-point bridge estimates correction effect for one configured system, but it is not the displayed 43% baseline and no native-tool-call GPT-4 bridge is reported. |
| Repetitions/uncertainty | One main run per task, retry on format failure | One run per model-task; no reported repeated-run uncertainty | Per-task transitions cannot be cleanly separated from stochastic serving variation. |
| Exposure | Public after 2024; no private holdout | Same public tasks/answers | Post-release systems may have seen tasks and answer keys; 2026 calls trend an upper bound on capability progress (2026 §4, p. 5). |
| Cost | Not reported | Estimated uncached dollar cost/task | No true longitudinal cost bridge; old GPT-4 costs are reconstructed under assumptions, not comparable billed telemetry. |

The release deserves credit for retaining `v1` ground truth and result-version routing. Yet the crosswalk shows why “43% to 98%” is not one estimand. The cleanest claims are (a) 2026 configured-system differences on v2 and (b) the specific same-output rescore bridge for GPT-4. A model-generation trend requires a frozen common form or a calibrated bridge design.

## Unique insight

The paper's most important sentence is not its headline; it is “a model's 2026 score isn't directly comparable to its 2024 score” (Appendix A.1.1). A maintained benchmark faces a three-way tension:

1. freeze defects to preserve longitudinal comparability;
2. repair defects to preserve fairness and current measurement validity;
3. refresh public content to preserve resistance to contamination and saturation.

No single score series can optimize all three. `skill-bench` should therefore maintain linked forms:

- **anchor form:** immutable tasks, environment, graders, and harness envelope for trend continuity;
- **operational form:** corrected current tasks with explicit migration events;
- **renewal form:** equivalent or bridge-calibrated private/recent tasks for contamination and ceiling control.

A release should publish a transition matrix at the task/check level: old pass/new pass under frozen trial outputs, reason for change, affected claim, and bridge eligibility. WorkBench approximates this with prose and one GPT-4 rescore; the release's versioned ground truths are the right substrate, but it lacks the full transition evidence.

## Limitations and validity threats

1. **Longitudinal causal identification fails.** Model, harness, tool documentation, scorer, task wording, target state, provider, and exposure all change.
2. **The headline uses an unmatched baseline.** The displayed 43% is 2024 ReAct/all-tools/v1, while the correction bridge starts from 49% and reaches 57%; neither isolates native tool calling.
3. **Public contamination is uncontrolled.** Tasks, generation code, and answers have been crawlable since 2024; no private holdout or canary analysis exists.
4. **One run per cell hides reliability.** Temperature zero is not determinism across proprietary services, and clustered task generation requires cluster-aware uncertainty.
5. **Safety is definition-coupled to correctness.** Correct and side-effect outcomes are mutually exclusive, mechanically inducing a negative relationship.
6. **No severity or opportunity model.** The 1.9% all-task rate can hide a high share of harmful failures, and “irreversible harm” is not independently coded.
7. **Generated tasks are not independent work samples.** Ten instances per template mostly test parameter variation, not 690 separately elicited activities.
8. **No professional-validity evidence.** “Common business activities” is author judgment; no worker sampling, expert review, human baseline, acceptance study, or consequence study is reported.
9. **Outcome-only grading misses process harms and read-only work.** Privacy exposure, unauthorized reads, inefficient loops, and answer quality can escape state comparison; pure retrieval is unscored.
10. **Cost is not reproducible from the public release.** The approximation and prices are documented, but traces are absent and caching/provider discounts are ignored.
11. **Release timing is imperfectly pinned.** The archived 2024 commit is a reproducible near-publication snapshot, not proven experiment code; the repository has no tags.
12. **Near-ceiling mean obscures local tails.** Sixteen Fable failures are too few for a broad mean but enough to matter if concentrated in irreversible-action classes; there is no severity-weighted confidence bound.

## Reproducibility and operational realism

Reproducibility is good for task data, scorer code, and committed per-task outputs. The current archive contains versioned ground truths, result sidecars, model-level derived counts, tests, and routing metadata. It is weaker for exact inference replay: proprietary model snapshots and serving stacks are mutable, traces are omitted, the 2024 experiment commit is uncertain, and some model names in a 2026-dated paper may not be independently verifiable beyond the supplied artifacts.

Operational realism is moderate at the action-state layer and weak at the work-system layer. The benchmark captures wrong recipients, wrong records, tool limits, multi-domain dependencies, no-op conditions, recovery, and irreversible writes. It omits identity/authorization, approvals, multi-user concurrency, communications consequences, history scale, ambiguous goals, collaboration, artifact quality, and organizational loss. Its scores support claims about deterministic sandbox state transitions under a specified configured system—not autonomous workplace readiness.

## Relation to existing `skill-bench` evidence

- **LiveBench** shows that rolling content can reduce static exposure but grader and pool renewal complicate time comparisons. WorkBench contributes the complementary repair problem: even a fixed nominal pool changes when unfair prompts and graders are corrected.
- **Task-health machinery** already separates task versions, witnesses, adjudications, revisions, and retirements. WorkBench shows why a repair must include a score bridge and why saturation and defect correction are distinct transition reasons.
- **Agent Reliability Profile** argues for repeated trials, severity, recovery, and operational denominators. WorkBench's single binary side-effect rate demonstrates precisely what a reliability profile repairs.
- **Workplace-validity reviews** (TheAgentCompany, OSWorld 2.0, workplace simulation work) show that recognizable office substrates do not establish occupational or deployment validity. WorkBench adds deterministic final-state strength but does not cross that validity boundary.

## Transfer to `skill-bench`

### Retain

1. Final-state grading that permits alternate paths and recovered mistakes.
2. Separate successful, failed-harmless, and failed-state-changing outcomes rather than hiding harm in average completion.
3. Immutable old scorer/task versions and explicit result-to-ground-truth version routing.
4. Per-task outputs and failure examples, not just leaderboard aggregates.
5. Explicit admission that current-form and old-form scores are not automatically comparable.

### Repair

1. Add a benchmark-version bridge record: changed task/check/environment/tool/harness loci, reason, old/new trial rescoring, transition matrix, and licensed comparisons.
2. Report side effects by severity, reversibility, affected party, action opportunity, and conditional-on-failure denominator alongside all-task prevalence.
3. Use repetitions and template-clustered uncertainty; separate serving failure from substantive agent failure.
4. Freeze a longitudinal anchor while operating corrected and renewed forms separately.
5. Treat public exposure, scorer changes, and harness changes as explicit threats in each validity argument.
6. Preserve read events, authorization checks, and process-side effects in traces so unchanged final state does not imply harmlessness.
7. Bind cost claims to actual usage records, pricing timestamp, cache policy, failed-run policy, and uncertainty.

### Test

A useful internal validation is a three-form bridge experiment on one pilot:

- run matched configured systems on frozen anchor, corrected operational, and private renewal forms;
- repeat each task enough to estimate local flakiness;
- rescore identical trial outputs under old and new graders where executable;
- report transition cells and changed-locus attribution;
- stratify action opportunities and severity;
- license trend claims only on stable or empirically bridged subsets.

Useful completion means the system can answer “did the agent improve, did the instrument become fairer, or did the harness remove a failure mode?” without collapsing these into one delta.

## Concrete repository actions

1. **No new build task.** Existing task-health, metric-monitoring, validity-argument, execution-validity, longitudinal-stream, reliability, and benchmark-bundle contracts already provide homes for the evidence. Creating another lifecycle schema would duplicate completed machinery.
2. Add this review to the next benchmark-lifecycle consolidation and require its explicit anchor/operational/renewal distinction plus task-level bridge matrix in canonical guidance.
3. When a current pilot is revised, exercise the existing contracts with a real old/new rescore transition and severity/opportunity report rather than adding synthetic fields.

## Claim ledger

Supported:

- the strongest tested configured system completed 674/690 tasks on the corrected v2 instrument;
- across the tested 2026 configured systems, higher completion coincided descriptively with fewer incorrect state-changing outcomes;
- the instrument and harness changed materially, and the release preserves v1/v2 ground-truth routing;
- frontier mean completion is near the ceiling while a small set of substantive failures remains.

Not supported:

- a model-only capability gain from 43% to 98%;
- a causal claim that capability improvements produced safety improvements;
- a universal capability–safety complementarity;
- professional workplace readiness or a 1.9% real-world harm probability;
- benchmark independence from training exposure;
- exact cost savings from billed production use;
- saturation as grounds for retirement without tail, reliability, contamination, and claim-coverage analysis.

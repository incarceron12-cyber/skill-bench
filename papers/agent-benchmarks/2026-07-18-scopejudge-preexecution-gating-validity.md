# ScopeJudge shows request-conditioned call classification, not validated online harm prevention

## Source and review status

**Deep review of the complete immutable primary source; claimed release unavailable.** I read the full 22-page arXiv v1 paper and appendices, checked the PDF against the complete text extraction and official arXiv source, and rechecked the paper, source, author/Dreadnode GitHub surfaces, Hugging Face, and targeted web results for the claimed dataset. No author-provided ScopeJudge dataset, harness, labels, predictions, costs, or table builder was locatable as of 18 July 2026. The paper repeatedly says the calibration corpus is released but supplies no artifact URL. That blocks row-level reproduction; it is not evidence that an artifact will never appear.

- **Paper:** Shane Caldwell et al., *ScopeJudge: Cost-Aware Pre-Execution Gating for Offensive Security Agents*, arXiv:2607.07774v1 (8 July 2026), <https://arxiv.org/abs/2607.07774v1>.
- **Local PDF:** `data/papers/pdfs/2607.07774v1-scopejudge.pdf` (22 pages; SHA-256 `efbd4239742bf1e1beb33dd51507bbb22d1a620dccead5a291a3758e46b109cc`).
- **Full text read:** `data/papers/text/2607.07774v1-scopejudge.txt` (SHA-256 `116f7ad8a4eadc92d8eecda6b67760939880aa1cf5ca2870b078e1d2095f9b3d`).
- **Official arXiv source:** `data/papers/source/2607.07774v1-source.tar.gz` (SHA-256 `d08804d20a705d93d60033778686b2d6d63773c795a20e81432b389917af0a42`).
- **Acquisition record:** `data/papers/index.json`, entry `arxiv:2607.07774v1`.

The source confirms that `\NumGraders` is **five**, not three: five professional penetration testers labeled every call. The manuscript gives no separate adjudication step.

## Relevance, charter fit, and decision filter

This review advances charter objectives A and B by testing a cross-domain boundary: **when does contextual expert agreement about a proposed action support a pre-effect gate, and what additional evidence is required before calling the gate safe or operationally useful?** It is narrow expansion into authority, observer evidence, asymmetric decision loss, and human-review burden. Offensive security is a mechanism case, not a benchmark scope commitment.

The concrete evidence is an audit of the chain `request and engagement scope → proposed call → monitor evidence view → expert labels/disagreement → offline decision → hypothetical gate → executed or withheld effect → recovery and consequence`. Useful completion means retaining request-conditioned evidence views and call-level disagreement while refusing to promote offline label imitation into prevented harm, useful-work preservation, production fitness, or readiness.

## One-sentence contribution and assessment

ScopeJudge's real contribution is a clean five-condition evidence-view experiment over the same proposed calls, showing that eight tested judges detect almost none of the authors' task-specific scope labels when the user request is deliberately withheld and substantially more when it is supplied; however, its 4,897 heavily dependent offline call prefixes were never gated, rejected, regenerated, or followed to consequences, the calibration sampling and expert-label lineage are under-specified, invalid outputs change denominators, uncertainty is absent, and the claimed release is unavailable, so v1 supports a request-conditioned **classification** result—not a validated pre-execution control system or deployment recommendation.

## Research question and intended construct

The paper asks how much context a cheaper fixed judge needs to classify each tool call proposed by a stronger, swappable security agent as within or outside the scope declared by the current request, and at what API cost (paper §§2–3, pp. 4–8). Its formal deployment loop is:

1. the user request supplies the task objective and engagement-specific scope;
2. a source agent proposes a tool call;
3. a transcript strategy selects what a judge sees;
4. the judge returns `allow=true/false` before execution;
5. an accepted call executes; a rejected call should cause revision or human escalation.

The five evidence views are: global static policy plus proposed call; add request intent; add prior calls; add summaries of prior outputs; or provide the full prefix, including outputs and agent reasoning. This is a useful construct: authority is not an intrinsic property of `curl`, `bash`, a host, or a state-changing method. It is request-, target-, parameter-, time-, and context-conditioned.

But the empirical construct is narrower than the formal loop. The experiment replays completed ungated trajectories and independently classifies each original call. It measures agreement with an authored majority label under five projections of an already-realized prefix. It does not execute Algorithm 1.

## Methodology and evidence

### Tasks, trajectories, and sampling

ScopeBench contains 30 engineered tasks/environments whose direct solution path tempts an agent to touch an excluded host, perform a forbidden action, or access excluded data (paper §4.1, pp. 8–9). The paper says a compliant agent may solve within bounds, refuse, or report without crossing the line.

The calibration set has 100 trajectories and 4,897 calls. Trajectory length ranges from 6 to 170 calls (median 38.5; mean 49.0). Five source-model families contribute 27 Claude Sonnet 4.6, 23 Qwen3.6 Plus, 19 Kimi K2.5, 18 Gemini 3.1 Flash Lite, and 13 GPT-5.4-mini trajectories (Table 1, p. 9). Two source models also serve as judges for some rows, an acknowledged but unanalyzed overlap.

The authors describe a much larger trajectory pool and say the 100 were drawn “representatively,” preserving a 7.7% natural call-level violation rate while stratifying the task × model grid. This claim is not auditable. The paper does not give the source-pool size, cell inventory, randomization, inclusion/exclusion rules, selected task counts, selected trajectory IDs, unsuccessful-generation handling, or call/violation distribution by task and source agent. “Natural” here means natural **within deliberately temptation-engineered ScopeBench rollouts**, not a production prevalence estimate. With only 100 rows for a nominal 30 × 5 grid, many cells must be absent or represented once unless trajectories are defined differently; the split graph is not published.

There is no train/development/evaluation split for selecting judge, strategy, or recommendation. The same 100-trajectory calibration corpus supplies human agreement, all judge comparisons, the Pareto frontier, and the two recommended operating points.

### Expert labeling and reference construction

Five professional penetration testers, described only as having web-penetration-testing or bug-bounty experience, independently label every proposed call (paper §4.3–4.4, pp. 9–10). They see the static policy, user request, full prior call/output history, agent reasoning, and proposed call. A label applies only to that call; an earlier violation does not automatically contaminate later labels.

Reported agreement is:

- Fleiss' κ = 0.64 across five raters;
- mean pairwise Cohen's κ = 0.64, with pairs from 0.50 to 0.76;
- 88.1% unanimous calls and 11.9% contested calls;
- mean grader F1 = 0.78 (range 0.63–0.89) when each grader is scored against the majority of the other four.

This is valuable evidence that call scope is not purely mechanical and that disagreement should remain visible. It is not an expert “ceiling.” The automated judges are scored against the majority of **all five**, while each human reference score uses a different leave-one-out target. A model optimized to majority convention can exceed an individual rater without becoming more professionally correct. Conversely, the majority can be wrong, especially when all five author-affiliated graders share instructions, task authorship context, or organizational convention. The paper reports no grader IDs/qualifications beyond a broad role, training or calibration cases, label rubric beyond the judge policy, time/order/blinding, rationale records, confidence, duplicate checks, disagreement reasons, adjudication, task-author independence, or independent affected-party authority.

Calling the majority label “ground truth” and the full view “fully informed” is therefore too strong. Full transcript access does not establish complete engagement authority, external state, target ownership, side-effect semantics, or the correct professional response. The contested 11.9% is not analyzed separately, so a judge's gains may reflect easy unanimous cases rather than resolution of genuine boundary ambiguity.

### Judge experiment and accounting

Eight API judges—four open-weight through OpenRouter and four proprietary—are crossed with five transcript strategies (Table 2, pp. 10–11). Each call is judged once at temperature zero. Reasoning is enabled where supported at provider-default effort. Outputs are short JSON, but no output-token cap is set. For the summarized-output view, the same judge model separately summarizes each prior output, with summaries cached per trajectory and their cost included.

The nominal sweep is 8 × 5 × 4,897 = 195,880 decisions. Only 194,482 parseable decisions are scored; 1,398, or about 0.71%, are excluded without retry (paper §5.4, p. 12). The paper does not report invalid counts by judge, strategy, class, task, or prefix length. Thus configurations can have different effective denominators, and exclusion can affect recall and cost. “No context window was exceeded” does not establish that failures are ignorable.

Costs use provider-reported input/output tokens and June 2026 list prices. The reported sweep cost is about $812. This is a useful realized inference ledger, but it does not include expert labeling, task/trajectory generation, harness development, human escalation, false-rejection recovery, delayed work, or the expected loss of an accepted violation. Provider defaults, model endpoints, tokenizer/accounting behavior, OpenRouter routing, prompts, raw usage, and prediction rows are not released or pinned beyond manuscript names and month.

### Results and what they license

The strongest result is the within-call evidence-view contrast (Table 3 and Figure 4, pp. 13–16):

- for seven of eight judges, static-policy recall is 0–4.5%, with median about 0.5%; GPT-5.4-mini is the outlier at 24.9%;
- adding the user request raises recall to 59.9–94.2%;
- the best F1 is GLM-5.2 with the full prefix, 0.656 at $6.01 per 1,000 calls;
- GLM-5.2 with intent plus calls reaches precision 0.501, recall 0.872, F1 0.637, and flags 13.3% at $3.22 per 1,000;
- Claude Opus 4.8 with intent only reaches precision 0.386, recall 0.942, F1 0.547, and flags 18.8% at $4.20 per 1,000;
- the human leave-one-out reference is mean F1 0.78.

The evidence supports: for these models, labels, prompts, and engineered calls, supplying the task request is necessary to recover most positive labels relative to a condition intentionally deprived of all task scope. It also supports a descriptive cost/label-agreement frontier as of the recorded June 2026 endpoints.

It does **not** establish the stronger claim that a fixed policy is structurally incapable of scope enforcement. The static condition is defined to omit the request-specific scope; an external parser, typed authorization manifest, request-to-policy compiler, capability token, target allowlist, or deterministic parameter guard is not tested. The experiment shows missing task information cannot be recovered reliably from the proposed call alone—not that learned monitoring is superior to request-conditioned formal specification.

The context ordering is not monotonic in either information or causal safety. Full prefixes include agent reasoning and raw target output; summarized prefixes add a second same-model transformation. Both can leak task progress, post-violation state, agent intent, answer-correlated cues, and prompt injection. The paper names adversarial robustness as future work and correctly says higher-context accuracy is an upper bound absent attack testing.

## Unique insight: evaluate the gate as a longitudinal authority-and-consequence intervention

The paper's most reusable contribution is not its model ranking. It is the separation of a stable generic floor from a request-specific authority surface and the explicit variation of monitor evidence. For `skill-bench`, this should become a longitudinal gate record:

```text
versioned request / authority source / affected party
→ proposed operation, target, parameters, pre-state, reversibility, and first-effect boundary
→ observer entitlement and exact evidence projection
→ independent labels, rationales, confidence, disagreement, and adjudication
→ predeclared threshold and false-accept / false-reject / delay / review losses
→ allow / deny / clarify / stage / escalate decision
→ actual executed or withheld operation
→ state delta and affected-party consequence
→ agent revision, safe progress, repeated evasion, recovery, and completion
→ burden, cost, reliability, and bounded validity claim
```

ScopeJudge observes the middle classification edge only. A benchmark should execute the whole intervention under matched conditions. Offline prefixes are especially dangerous evidence: if a live gate had rejected call *j*, the agent would receive feedback and every later proposal and prefix could change. Replaying call *k* from the ungated trajectory therefore does not estimate the online policy induced by the gate. It cannot reveal whether the agent safely revises, repeatedly paraphrases the forbidden call, exploits the judge, stalls, escalates correctly, or still completes useful work.

A proper test should pair each forbidden proposal with a matched permissible control differing only in authorization, target, parameter, or state; run no-gate and gate arms from the same pre-state; preserve proposed and actually executed calls; and score prohibited effects, allowed-work completion, false-escalation burden, recovery, and repeated attack. That combines ScopeJudge's request conditioning with AgentAbstain's matched act/withhold idea and the existing four-part action contract: eligibility, correct execution, trigger-relative restraint, and recovery communication.

## Limitations and validity threats

1. **Offline replay is not online gating.** No judge decision changes execution, state, future prefixes, agent behavior, or consequence.
2. **False negatives are not observed executed violations under the tested gate.** The paper equates a classification miss with production execution, but it only scores a recorded proposed call.
3. **False positives are not “mere” escalations.** No human review, delay, fatigue, denial of useful work, abandonment, or recovery cost is measured.
4. **No matched authorization controls.** Benign and violating calls are naturally different call types and trajectory stages; no same-operation in-scope/out-of-scope pair isolates request conditioning from content cues.
5. **Engineered prevalence is not deployment prevalence.** The 7.7% call rate comes from tasks designed to tempt violations and an undocumented selected trajectory pool.
6. **Calibration-set selection is opaque.** Source pool, task/model cells, draw rule, selection failures, and IDs are unavailable.
7. **No held-out recommendation set.** Strategies and deployment points are selected and described on the same corpus used for all comparisons.
8. **Calls are pseudoreplicates.** Thousands of overlapping prefixes cluster within 100 trajectories, 30 tasks, five source models, and shared environment templates; no clustered uncertainty is reported.
9. **One run per cell.** Temperature zero and provider defaults do not eliminate inference, routing, summarization, or service nondeterminism.
10. **Different scored denominators.** 1,398 unparsable outputs are excluded, with no per-cell/class missingness ledger or failure sensitivity analysis.
11. **Majority convention is not ground truth.** Rater authority, training, rationales, confidence, independence, and disagreement adjudication are under-specified; all graders are among the authors.
12. **The “expert reference” is not a ceiling.** Human and model F1 use non-identical consensus targets, and majority imitation differs from independent correctness.
13. **Contested calls are hidden by pooled scores.** The 11.9% non-unanimous subset receives no separate confusion, rationale, severity, or evidence-view analysis.
14. **History leaks consequences of ungated behavior.** Later calls can expose outputs and reasoning produced after earlier scope violations that a real gate should have prevented.
15. **Prompt-injection resistance is untested.** Raw outputs, same-model summaries, and reasoning traces expand an adversarial channel.
16. **Source-agent overlap is uncontrolled.** Claude Sonnet and GPT-5.4-mini judge trajectories generated by the same model family in some rows.
17. **Binary decisions collapse legitimate continuations.** Deny, clarify, request authority, safe-subset execution, reversible preview, and human escalation have different costs and value.
18. **No severity or reversibility model.** A scan, data read, destructive write, and lateral move receive the same positive label and F1 weight.
19. **Recommendations lack an explicit loss function.** “Cost-sensitive” and “recall-first” are post-hoc labels, not optimizers under quantified false-accept, false-reject, review, delay, and harm losses.
20. **The high-stakes recommendation contradicts its premise.** A configuration with 94.2% recall still misses about 5.8% of labeled violations; it is not suitable evidence for a setting where one miss is unacceptable.
21. **Model and price identities are mutable.** API defaults, endpoint revisions, routing, and prices are incompletely pinned.
22. **Claimed release is unavailable.** Labels, trajectories, prompts as instantiated, predictions, invalid rows, tokens, costs, and analysis code cannot be audited or replayed.
23. **Operational and professional validity are absent.** Controlled synthetic environments and author-graders do not establish legal authorization, real client impact, preserved productivity, production fitness, or readiness.

## Reproducibility and operational realism

The manuscript is unusually clear about its formal gate, five evidence projections, constant judge prompt, source/judge model rosters, headline denominators, temperature, invalid-output policy, token-price date, cost inclusion, and complete 40-cell scoreboard. The arXiv source is internally inspectable and confirms five graders.

That transparency does not make the empirical result reproducible. No dataset locator is present despite repeated release claims. ScopeBench tasks, selected trajectories, full labels, rater assignments/rationales, judge requests/responses, invalids, token rows, prices, environment versions, and scripts are absent. Table-level values cannot be reconstructed or stratified. The larger source pool is reserved, not released.

Operational realism is mixed. Request-specific authorization, target-sensitive calls, long prefixes, heterogeneous source agents, and review-cost tradeoffs are real deployment concerns. But the task suite is engineered, environments are controlled, all calls come from ungated runs, the gate never causes a revision, no human is escalated, no state consequence is compared, and no allowed-work utility is measured. This is best treated as an offline monitor-calibration study.

## Transfer to skill-bench

### Retain

1. Separate a generic policy floor from request-/case-specific authority and version both.
2. Record the exact observer evidence projection; judge identity without evidence-view identity is incomplete.
3. Label proposed operations before first effect, at target/parameter granularity.
4. Preserve expert disagreement rather than collapsing immediately to one oracle.
5. Report precision, recall, flag rate, invalid rate, and cost separately under asymmetric stakes.
6. Treat raw outputs, summaries, and reasoning as different information and attack surfaces.
7. Keep source agent, monitor, harness, request, task, environment, and provider identities independently swappable.

### Repair before adoption

1. Run the gate online in matched gate/no-gate arms; log proposal, decision, execution, state delta, revision, completion, and recovery.
2. Add matched permissible/impermissible controls for the same operation and pre-state.
3. Define authority from versioned source records and affected-party rights, not only benchmark-author intent.
4. Use blinded independent raters, typed expertise, criterion-level rationales, confidence, and explicit adjudication; report contested cases separately.
5. Freeze development and untouched evaluation tasks by environment and authorization pattern.
6. Analyze at trajectory/task/environment clusters and repeat configured cells; retain intention-to-evaluate and infrastructure-clean estimands.
7. Count invalid judge output as fail-closed operational behavior in the primary gate estimand, with alternate policies as sensitivity analyses.
8. Predeclare a loss function including severity, reversibility, false rejection, delay, escalation load, repeated attempts, and denied useful work.
9. Compare learned monitors with formal request-conditioned controls: typed scopes, target/parameter allowlists, capability tokens, and deterministic state guards.
10. Test prompt injection, adversarial paraphrase, repeated evasion, stale authority, conflicting instructions, and safe recovery.

## Concrete cross-domain validation

Use two unlike existing pilots with consequential state transitions. For each, create matched cases where one version authorizes a target/parameter/action and another changes only the authority fact. From a frozen pre-state, run: no gate; deterministic typed-authority gate; intent-only model gate; calls-only history gate; and full-evidence model gate. Cross clean and adversarial output histories. Measure expert label agreement, actual prohibited state deltas, correct allowed transitions, task completion, clarification/escalation quality, repeated evasion, latency, tokens, human review minutes, and recovery. Analyze matched pairs with task/environment clusters and a predeclared severity-weighted loss. This tests the general hypothesis that request-conditioned monitors add value beyond formal controls without narrowing the benchmark to security.

## Comparison with adjacent reviewed evidence

- **AgentAbstain** contributes matched act/withhold counterfactuals and trigger phases but weak endpoint checks. ScopeJudge contributes call-level request conditioning and expert disagreement but no online intervention. Together they require matched authority changes plus consequence-level action, restraint, and recovery grading.
- **Expert Disagreement in Human Feedback** explains why contested judgments, authority, and adjudication policy are part of the construct rather than noise. ScopeJudge reports useful agreement statistics but then hides disagreement in one majority label.
- **AgentRewardBench** shows that grader evidence views, invalid outputs, class imbalance, and expert-label lineage materially affect judge reliability. ScopeJudge varies evidence views explicitly but omits per-view missingness and contested-case diagnostics.
- **Action-safety and intervention-timing work** requires a first-effect boundary and observed pre/post state. ScopeJudge formalizes pre-execution timing but evaluates only offline proposals, leaving restraint realization and recovery unobserved.
- **Metric monitoring and validity arguments** require a declared eligible population, clustering, missingness, threshold/loss basis, and claim ladder. ScopeJudge's post-hoc “cost-sensitive” and “high-stakes” choices are descriptive configurations, not validated deployment decisions.

## Concrete repository action

No new queue task is warranted. Existing authority, action-safety, observer/evidence-view, metric-monitoring, task-health, plural-judgment, configured-system, intervention-timing, and validity-argument machinery already covers the requirements, while AgentAbstain-derived work already supplies matched action-boundary tasks. The nonduplicate action is to require online gate/no-gate consequence trials and matched authority controls when that machinery is next consolidated or exercised.

## Claim boundary

ScopeJudge v1 supports a useful and robustly interpretable descriptive result: across eight June 2026 judge endpoints and one engineered, author-labeled calibration corpus, withholding the request-specific scope causes near-zero violation recall for seven models, while supplying the request substantially raises agreement with the five-rater majority. It also contributes a valuable evidence-view taxonomy and transparent table-level cost/accuracy comparison.

It does **not** establish that a static request-conditioned specification cannot work; that the 7.7% rate represents deployment; that majority labels are independent professional truth; that 0.78 is an expert ceiling; that more transcript history is causally safer; that recommended configurations optimize a declared operational loss; that any rejected call would be safely withheld; that any missed label becomes realized harm; that useful work, escalation, repeated evasion, recovery, or affected-party outcomes improve; that the claimed dataset is currently inspectable; or that ScopeJudge is adversarially robust, professionally validated, production-fit, or ready for deployment.
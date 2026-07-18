# Cost-aware security-agent evaluation: priced execution is not operational cost or risk

## Source and review status

**Deep review of the complete immutable arXiv v1 paper and appendices, the complete arXiv source archive, the official paper/figure repository at a pinned post-v1 commit, and the paper-linked website.** I read the full 19-page primary source. The official repository is a manuscript and chart repository, not the source evaluation release: it explicitly excludes raw Inspect logs and datasets, points to a private local `~/projects/inspect-cyber-eval/` checkout, and reconstructs most dense trajectories by pixel-digitizing frozen PNGs. The paper-linked site currently serves a generic company landing page rather than the claimed interactive results. The quantitative study therefore cannot be replayed from public artifacts.

- **Paper:** Paul Kassianik, Blaine Nelson, and Yaron Singer, *Beyond Success Rate: Cost-Aware Evaluation of Offensive and Defensive Security Agents*, arXiv:2607.15263v1 (16 July 2026), <https://arxiv.org/abs/2607.15263v1>.
- **Local PDF:** `data/papers/pdfs/2607.15263v1-cost-aware-security.pdf` (19 pages; SHA-256 `86ba6e9faf5ce0fbe3d3a0cc015ade3ddc0162a0a6518cdf5acbd3280822860f`).
- **Full text:** `data/papers/text/2607.15263v1-cost-aware-security.txt` (58,174 bytes; SHA-256 `71d2f49cd2e4eec816196459a4d8d4f510c525a496ed0d2db4b69e64a1803a51`).
- **Metadata:** `data/papers/source/2607.15263v1-metadata.xml` (SHA-256 `e5693f9366ea74e3bfc5257e6359ed888cb15b01788f154d05067e40fdf6c964`).
- **Complete arXiv source:** `data/papers/source/2607.15263v1-source.tar.gz` (SHA-256 `7fe94eb636f85848745b60297d09bcc83d4fd6dc7b4834e9238ea73bdc46898e`).
- **Official paper repository:** <https://github.com/paulkass/bots-cybench-eval>, archived at commit `bcd6b1b32b769a72bea2906c23e55369c3a72b79` as `data/sources/releases/2607.15263v1-cost-aware-security/paulkass-bots-cybench-eval-bcd6b1b.zip` (SHA-256 `42bf41da8b12959287fdbe12e60165c08dff12d9228c34569db2df4df4934df2`). The commit is 23.98 hours after arXiv v1 and is not silently treated as the exact manuscript-time state.
- **Release and website provenance:** `data/sources/releases/2607.15263v1-cost-aware-security/provenance.json`.

## One-sentence contribution

The paper makes the useful move from unconstrained success to **task-level success under declared execution budgets**, but its dollars cover only model inference and selected enrichment requests, its defensive score is mostly recoverable without telemetry on two tested models, and its observational cross-model/tool-volume comparisons do not establish analyst discipline, operational fit, defender burden, realized security value, or risk.

## Why this matters for `skill-bench`

This review advances charter objectives A, B, C, and D through a cross-domain measurement question:

> When may an artifact score and a partial execution ledger support an efficiency, utility, operational-fit, or safety claim?

The answer is not “once dollars are attached.” A consequential knowledge-work evaluation needs a typed chain:

```text
configured task and resource policy
→ eligible trial and outcome
→ consumed resources with price basis
→ omitted and transferred costs
→ stakeholder consequence and loss
→ uncertainty at the deployment unit
→ bounded efficiency / utility / risk claim
```

The paper measures the first three incompletely. It does not observe analyst review, infrastructure, response action, prevented loss, attacker/defender interaction, collateral effects, or downstream harm. Its strongest transferable insight is therefore a **cost-boundary discipline**: preserve success and each resource family separately before attaching prices, ratios, or operational claims.

This security case does not narrow `skill-bench` to cybersecurity. The same distinction applies to research, finance, medicine, software, and office work: API charges are not total cost; rubric points are not stakeholder value; low tool count is not disciplined work; and cost per passing item is not return on investment.

## Research question and construct

The paper asks how offensive and defensive language-model security agents compare when success is conditioned on a per-sample budget and when inference and selected paid tools are costed separately (pp. 1–4). It contrasts:

- offensive Cybench CTF tasks, where additional reasoning and command execution may buy more attempts; and
- defensive Splunk BOTS v1 questions, where the authors hypothesize that telemetry navigation and selective enrichment matter more than raw inference spend.

The strongest defensible construct is **configured benchmark score under a partial priced-resource envelope**. The evidence does not measure:

- total cost of ownership;
- analyst time or review burden;
- defender workload displaced or created;
- exploit impact, incident loss, containment, recovery, or harm;
- production SOC quality, reliability, or readiness;
- causal efficiency of any reasoning or tool-use policy; or
- an offensive-versus-defensive scaling law.

The title is appropriately about “cost-aware evaluation,” but the abstract and conclusion go further by invoking “economic efficiency,” “operational fit,” “practically useful,” and defensive success depending on disciplined tool use (pp. 1, 19). Those stronger terms require evidence absent from the design.

## Methodology and system

### Common harness, noncommon configured treatments

All runs use Inspect with a ReAct-style agent and automatic context compaction at 90% of the model context window (p. 4). OpenAI and Anthropic models use direct APIs; other models use OpenRouter with one primary and two fallback providers. Provider-native compaction, cache behavior, pricing, model defaults, and reasoning effort vary. OpenRouter costs use the **average advertised price across three providers**, not necessarily the provider and cache state that realized each trajectory (p. 4).

The harness is common, but the comparison is not model-only. Configured-system differences include provider, routing/fallback behavior, model family, reasoning effort, prompt caching, compaction realization, cost ledger quality, prospective cap, retries, and policy refusal. The paper acknowledges that the run matrix is observational (p. 12), yet phrases several cross-row patterns as properties of offense or defense.

### Offensive unit: Cybench hard

Cybench contributes 39 sandboxed CTF challenges over cryptography, web exploitation, reversing, forensics, and exploitation (pp. 4–5). Agents receive bash, Python, and a submit tool. A case-insensitive substring match against a hidden flag determines success. Each challenge has three epochs and up to three submissions; the paper averages epoch correctness per challenge and then across challenges.

This yields a valid selected-suite flag-recovery measure if sandbox and trial records are intact. It does not measure exploit consequence, stealth, persistence, remediation, attacker cost outside model inference, or safety. Bash, Python, and command execution are assigned zero marginal cost, so the primary offensive interaction resource appears in tool-call and token views but not in dollars (pp. 5–6).

### Defensive unit: BOTS v1 follow-up questions

The authors implement BOTS v1 in Inspect because no public implementation was found. They exclude the warm-up and retain 31 questions worth 10,300 official points (pp. 5, 19). Twenty-three questions receive transitive official prerequisite question/answer context. Correct answers earn official points minus hint penalties; the paper also reports binary answer inclusion. Three epochs are mean-reduced back to one 10,300-point scale.

This is closer to **follow-up CTF question answering over a known case state** than end-to-end incident investigation. It does not require the agent to reconstruct all earlier findings, produce an analyst artifact, cite evidence, assess uncertainty, recommend or execute response, avoid collateral action, communicate with stakeholders, or withstand expert review. Official competition points are an inherited game scoring policy, not a validated utility or loss function for SOC work.

The tool surface is richer: Splunk discovery/search/event inspection, bash, Python, DNS, live WHOIS/RDAP, VirusTotal, Brave Search, and WhoisXMLAPI. Brave is limited to five calls; VirusTotal and WhoisXMLAPI to three. Strict keyword filtering is said to prevent writeup/solution leakage, but the implementation, filter vocabulary, false-positive/negative tests, and blocked requests are absent from the public release.

### Refusal accounting

A heuristic detector NFKC-normalizes text and matches apology, inability, policy, or fabrication patterns when an assistant turn contains nonblank text and no tool call; provider `content_filter` also counts. One detection aborts the sample (pp. 5–6; release `tables/provenance.md`, lines 104–116).

Cybench counts only refused-and-unsolved epochs and leaves them as failures. BOTS reports any detected event as secondary context even if a later/retried attempt earns points. Thus “refusal” has different event definitions and score relations across benchmarks. It is useful diagnostic context, but not a comparable policy-safety metric. Fable’s 0% Cybench result, for example, is a configured policy-filter outcome, not evidence of no latent offensive ability (p. 7).

### Cost accounting

The declared dollar boundary is explicit (pp. 5–6):

- model inference from provider ledgers or reconstructed token rates;
- Brave Search at $0.005/request;
- WhoisXMLAPI preview at $0.0258/request;
- WhoisXMLAPI purchase at $1.29/request;
- cached WhoisXMLAPI responses charged as if newly purchased.

The following are priced at zero or excluded:

- bash, Python, Splunk discovery/search/event inspection;
- VirusTotal public API, DNS, live WHOIS/RDAP;
- Kubernetes, Splunk infrastructure, storage, network, orchestration, and engineering;
- analyst review, adjudication, escalation, remediation, and downstream response;
- latency, service failures, security controls, and externalities.

This is a defensible **model-plus-selected-enrichment price convention**, not total operational cost. Hypothetical cache-independent prices can estimate an expected procurement schedule, while direct provider ledgers estimate realized spend; mixing the two without a typed price basis obscures whether the number is observed, reconstructed, list-price, amortized, or counterfactual.

A budget cap aborts a sample that overruns and treats it as failed. Some main rows, however, lack the stated prospective cap, combine retries, reconstruct costs, or normalize a missing challenge. Table 2 itself records these exceptions (p. 7). The denominator and cost policy therefore need to be read row by row rather than as one clean fixed-budget experiment.

### Retrospective budget replay

For selected prior runs, completed trajectories are replayed under a $0.80 cap. Cybench marks an epoch failed once cumulative model-call cost crosses the cap; BOTS zeroes points if model-plus-priced-tool cost exceeds it. Task IDs are resampled in paired descriptive bootstraps (pp. 10–12, 18).

This answers a useful historical question:

> Which retained successful trajectories completed within the lower ledger threshold?

It does **not** estimate how an agent would behave under a known lower budget. The agent was unaware of dollar/token limits, only selected tool-call limits; a prospective cap can alter stopping, verification, exploration, and tool selection. Retrospective zeroing also cannot recover an alternative answer or policy that would have emerged under early interruption. The contrast is within-trace budget headroom, not a causal test-time-compute treatment effect.

The official paper repository creates an additional ambiguity. Its provenance says the DeepSeek Flash $0.80 table row is the same $2.10 trace under retrospective replay, but a later Cybench provenance row lists a separate `$0.80` “Phase-B autocompact run” (`tables/provenance.md`, lines 56, 86, 90, 118–125). Because the source logs and transformation code are unavailable, a reader cannot resolve which artifact generated each displayed number or curve.

## Evidence and results

### What the paper reports

For Cybench, the latest main table reports GPT-5.5 at 94.1% and $1.16 per solved-equivalent challenge; DeepSeek v4 Flash at 86.4% and $1.45/solve under the $2.10 row; and lower GPT-5.6/Fable results dominated by refusal outcomes (p. 7). A selected earlier-run replay reports additional headroom above $0.80 of:

- GPT-5.5: +2.6 percentage points, interval [0.0, 6.0];
- June Claude Opus 4.8: +18.8 [10.3, 29.1];
- DeepSeek v4 Flash: +10.3 [4.3, 17.1];
- DeepSeek v4 Pro: +0.0 [0.0, 0.0] under a prospectively low trace (p. 11).

These support heterogeneous **within-retained-trace headroom**. They do not establish a general offensive scaling curve, because models, caps, retries, providers, and run dates differ and only selected prior rows receive uncertainty.

For BOTS v1, Claude Opus 4.8 leads the reported table at 9,666.7/10,300 points and $2.98 per 1,000 points, followed by GPT-5.6 Terra and Sol (p. 8). The direct DeepSeek Flash $4.20-versus-$2.10 comparison changes score by +0.9 percentage points with interval [-4.9, 6.9]. It also makes 488 more tool calls, but total reported model-plus-tool cost is paradoxically **$4.21 lower** ($39.29 versus $43.50). That is possible across stochastic independent runs, but it shows that cap assignment is not consumed spend and that this pair does not identify a monotone cost treatment.

### No-tools probes undermine absolute defensive interpretation

The most important result is the paper’s own contamination control (pp. 8–9):

- Claude Opus 4.8 scores 74.8% with prerequisite answers and 50.0% from question text only;
- GPT-5.5 scores 62.1% and 54.9%, respectively;
- all four no-tools rows are single-epoch, while full-agent baselines use three epochs.

The post-v1 repository provenance adds no-tools rows for newer model variants, ranging from 13.1% to 77.2%, but these are not in arXiv v1 and must not be folded into its empirical claims.

The controls establish substantial **direct answer recoverability without live telemetry** for two tested models. They do not identify whether the mechanism is memorization, training overlap, generic domain knowledge, clues in question text, official prerequisite answers, or reasoning. Nor do they decompose the full-agent uplift: tools, prompt length, interaction, retries, and additional context all change together. Still, a benchmark where one model obtains three quarters of official points without tools cannot support clean claims about telemetry navigation or live investigative ability.

### Tool volume is not discipline

Figure 6 and the prose emphasize that high BOTS tool volume often accompanies lower score. Across the published table, mean non-submit tool calls range from about 3.32 to 53.10 per question-epoch. This is descriptive configured-system heterogeneity. It does not show that fewer calls are better, that specific calls were relevant, or that “disciplined” use caused success.

A useful discipline estimand would require at least:

- opportunity and eligibility for each tool;
- evidence state before the call;
- expected information value or declared purpose;
- retrieved evidence and semantic adoption;
- answer/decision change attributable to the evidence;
- redundant, invalid, failed, or harmful calls;
- latency and reviewer burden; and
- a matched policy or within-model intervention.

Raw count cannot distinguish a concise correct investigation from cached answer recall, premature guessing, an incomplete evidence view, or a tool that bundles many operations per call.

### Uncertainty is narrow and descriptive

The bootstrap resamples 39 Cybench challenge IDs or 31 BOTS question IDs while retaining three epochs and BOTS point weights (p. 18). Paired contrasts retain common IDs. This is better than treating 117/93 epochs as independent.

It remains descriptive because:

- the task sets are authored benchmark inventories, not probability samples of offensive or SOC work;
- BOTS questions share two incidents and explicit prerequisite-answer chains, so question IDs are not independent deployment units;
- variants, providers, retries, dates, and configurations are not randomized;
- only a subset of model rows receives intervals;
- no repeated environment/provider realization is modeled; and
- no multiplicity or family-level inference supports broad rankings.

The paper appropriately calls these robustness checks rather than population inference (p. 12). “Scaling regimes,” “practically useful,” and workflow-level operational conclusions should remain equally bounded.

## Unique insight

The paper’s unique and durable insight is that **budget must be part of configured-system identity and score interpretation**, not merely reported as one aggregate after the fact. A success curve indexed by a declared resource envelope is more decision-relevant than an unconstrained leaderboard.

The release audit sharpens that insight: resource accounting itself needs provenance and admissibility. Four dollar concepts must not be mixed:

1. **realized spend:** charged resources in the retained trial;
2. **reconstructed spend:** token/tool quantities multiplied by a versioned rate sheet;
3. **counterfactual price:** what cached/free resources would cost under another procurement policy;
4. **total stakeholder cost:** infrastructure, labor, delay, failure, review, remediation, and externality costs.

Likewise, four ratios answer different questions:

- cost per attempted trial;
- cost per valid scored trial;
- cost per success under a fixed envelope;
- expected total cost per accepted stakeholder consequence.

Only the first three can be approached from benchmark ledgers, and only when retries, invalid runs, failures, denominator rules, and price bases are consistent. The fourth requires downstream evidence.

## Limitations and validity threats

1. **Partial cost boundary:** core Splunk/search infrastructure, shell execution, storage, orchestration, engineering, and human review are zero-priced or omitted.
2. **No operational value:** CTF flags and BOTS points are benchmark outcomes, not prevented loss, containment quality, analyst acceptance, or readiness.
3. **No realized safety consequence:** offensive capability and refusal are observed only through sandbox flags/policy events; harm, exploit impact, defender burden, and collateral effects are absent.
4. **Public-answer recoverability:** tested models obtain 50.0–74.8% BOTS points without tools, blocking clean live-investigation claims.
5. **Weak contamination identification:** no-tools/no-context probes detect direct recoverability but cannot distinguish memorization, prompt inference, prior knowledge, or leakage.
6. **Follow-up context treatment:** 23/31 BOTS questions receive transitive official prior Q&A, reducing cold-start reconstruction and introducing dependency.
7. **Game-derived weights:** BOTS point values and hint penalties lack validation as SOC severity, effort, information value, or loss.
8. **Observational matrix:** models differ in provider, routing, reasoning effort, caching, cap, retries, compaction, and refusal policy.
9. **Retrospective cap ceiling:** replay estimates whether retained traces finish under a threshold, not behavior under prospective budget knowledge.
10. **Selective retry accounting:** some cost rows aggregate failed retries, others use one run, and one successful ledger is reconstructed.
11. **Cap/spend confusion:** higher-cap DeepSeek Flash BOTS consumes less total reported spend than the lower-cap run; cap is not treatment dose.
12. **Average OpenRouter pricing:** averaging three provider prices disconnects reconstructed dollars from realized provider/cache state.
13. **Mixed price semantics:** cached Whois calls receive hypothetical fresh prices while some other free-tier resources are zero.
14. **Tool-count confounding:** lower calls can reflect efficiency, recall, refusal, premature stopping, or coarser tool granularity.
15. **Outcome-only defensive grader:** answer inclusion and official points do not assess evidence support, source authority, uncertainty, response action, or artifact quality.
16. **Refusal heterogeneity:** benchmark-specific event and scoring rules prevent a common safety interpretation.
17. **Message censoring:** high-volume DeepSeek rows hit a 250-message limit; truncation is configuration-dependent.
18. **Question dependence:** BOTS bootstrap treats incident-linked, prerequisite-connected questions as resampling units.
19. **Selective uncertainty:** newest GPT-5.6/Fable/latest Opus rows lack the robustness analyses shown for older rows.
20. **No task-population inference:** 39 CTFs and 31 questions do not define offensive or defensive professional-work populations.
21. **Unreleased evaluator:** BOTS implementation, scoring code, leakage filter, refusal code, and exact source checkout are absent.
22. **Unreleased trials:** raw logs, task rows, costs, tool records, retries, invalid records, and bootstrap inputs are unavailable.
23. **Raster-derived evidence:** public chart regeneration pixel-digitizes frozen PNGs for most trajectories instead of rebuilding from rows.
24. **Internal provenance contradiction:** the public provenance describes the DeepSeek $0.80 Cybench row both as retrospective replay and as a separate Phase-B run.
25. **Broken claimed interface:** the paper-linked interactive-results URL currently serves a generic landing page.
26. **Post-v1 release drift:** the audited repository commit is nearly 24 hours after v1 and includes newer no-tools results not in the immutable paper.
27. **No cost uncertainty:** prices, provider routing, cache policy, rate changes, and infrastructure variability have no sensitivity analysis.
28. **No time or latency metric:** dollars and calls omit wall-clock delay, queueing, timeouts, and analyst wait cost.
29. **No adverse-side-effect ledger:** repeated queries, noisy searches, external enrichment, or offensive actions are not scored for operational side effects.
30. **No utility threshold:** cost-per-point has no stakeholder loss function, acceptance threshold, or decision rule.

## Reproducibility and operational realism

**Paper inspectability: high.** The immutable manuscript explains task counts, tools, caps, point rules, refusal logic, cost inclusions/exclusions, run dates, and bootstrap unit unusually clearly.

**Empirical replayability: low.** The official 38-entry archive contains the manuscript, styles, figures, one chart generator, compact additions, and detailed path-level provenance. It does not contain the evaluation implementation or source data. Its README says raw logs and datasets should not be added. Its chart README states that the canonical evaluation checkout is unavailable in that workspace. Most dense trajectories are recovered from raster pixels, which may reproduce appearance but cannot audit sample eligibility, costs, failures, or uncertainty.

**Operational realism: mixed.** Splunk telemetry, query iteration, event inspection, hints, external enrichment, tool prices, caps, and sequential context are structurally realistic. But an old public CTF dataset, answer-inclusion grading, official prior-answer injection, no analyst artifact, no response action, zero-priced primary infrastructure, no human review, no latency, and no downstream consequence prevent production SOC inference.

The right release claim is therefore: an unusually transparent paper-level accounting design with incomplete public empirical artifacts—not a reproducible cost benchmark or operational security evaluation package.

## Transfer to `skill-bench`

### Retain

1. Declare the per-trial resource envelope as part of configured-system identity.
2. Keep inference, tool, infrastructure, human, and externality quantities separate before pricing.
3. Count budget-aborted and refusal-affected trials in explicit eligible/invalid/failure denominators.
4. Use same-task paired budget views where possible.
5. Run no-tool/no-context or equivalent information-ablation controls on public tasks.
6. Report cost curves and task-level uncertainty rather than one unconstrained score.
7. Preserve run dates, retry lineage, ledger reconstruction status, and price versions.

### Repair

1. Add a typed `price_basis` for each resource observation: realized ledger, reconstructed rate, list price, cached counterfactual, amortized infrastructure, or human estimate.
2. Separate budget assignment, consumed quantity, charged spend, and total stakeholder cost.
3. Record all retries and invalid trials; compute both campaign cost and retained-valid-trial cost.
4. Pair retrospective replay with prospective budget arms and explicitly label the former as within-trace completion headroom.
5. Treat public-answer recoverability as a claim blocker until fresh/private or perturbed equivalents reproduce the tool-dependent effect.
6. Replace raw tool count with evidence-purpose/adoption/consequence records.
7. Use incident/case clusters—not dependent question IDs—as the uncertainty unit for SOC-like work.
8. Require stakeholder artifacts and consequences before claiming operational fit, professional value, or safety.
9. Fail the release gate if public charts cannot be regenerated from immutable rows and code.

### Existing artifact homes

No new queue task is warranted. The requirements map into already implemented machinery:

- `schemas/metric-monitoring.schema.json`: eligible population, missing/invalid handling, units, aggregation, uncertainty, thresholds, and action semantics;
- `schemas/benchmark-bundle.schema.json`: configured-system identity, traces, tools, costs, artifacts, checks, and execution outcomes;
- `schemas/task-health.schema.json`: public contamination, saturation, task role, defects, revision, and retirement;
- `schemas/validity-argument.schema.json`: claim ceiling from score to capability/readiness/decision;
- `schemas/trial-accounting.schema.json`: campaign attempts, retries, invalid records, and reconciliation;
- `schemas/CLEAN_RELEASE_GATE.md`: public artifact closure and replayability;
- `schemas/LONGITUDINAL_EVALUATION.md`: prospective resource treatments and persistent-state controls.

The nonduplicate consolidation need is human-facing: integrate **resource quantity → price basis → transferred/omitted cost → consequence → claim** into the canonical cost-aware synthesis when the current pending consolidation backlog clears. Creating another schema would duplicate the existing metric and trial-accounting contracts.

## Action items

1. Add this review to the next safety/cost canonical synthesis as a Tier B design source and Tier C empirical-release source: retain explicit partial accounting and contamination controls; reject operational-fit and risk claims.
2. Exercise the existing metric/trial-accounting fixtures with a planted case where a higher cap consumes less spend, failed retries are selectively omitted, and cached resources use counterfactual prices; require the report to preserve all four distinctions rather than forcing one cost rank.
3. For the next knowledge-work pilot, report at least model tokens/calls, tool operations, wall time, invalid/retry burden, human review time, and artifact acceptance separately. Do not compute “cost per useful result” until useful consequence and denominator policy are validated.
4. Add a public-answer-recoverability negative control to any reused public source pack: no-source, question-only, stale-source, and fresh equivalent forms should block capability claims when direct recovery is high.
5. Require release replay from immutable trial rows, not chart pixels or prose tables, before treating cost curves and uncertainty as auditable evidence.

## Bottom line

This paper improves the evaluation question by putting a budget on the x-axis and by admitting that an old public defensive benchmark is answer-recoverable without telemetry. Those are valuable design moves. Its evidence supports selected-suite score and within-trace completion headroom under a partial model-plus-enrichment price convention. It does not show that low-call agents investigate more intelligently, that BOTS points represent defensive value, that cost per point measures economic efficiency, or that any system is operationally fit or safe. `skill-bench` should adopt the typed resource ledger and decontamination controls while enforcing a strict ceiling: **priced benchmark execution is not total cost, benchmark points are not stakeholder value, and neither is realized risk.**

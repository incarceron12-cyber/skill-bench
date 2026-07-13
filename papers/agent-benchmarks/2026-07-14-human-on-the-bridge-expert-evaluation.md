# Paper Review: Human-on-the-Bridge — Reusable Evaluation Policy Without Demonstrated Expert Validity

- **Paper:** https://arxiv.org/abs/2606.16871v1
- **Author:** Fouad Bousetouane
- **Date read:** 2026-07-14
- **Venue / source:** arXiv preprint; work supported by ProofAI LLC and presented as part of the ProofAgent.ai open-source initiative
- **Version read:** immutable v1, 15 June 2026
- **Local PDF:** `data/papers/pdfs/2606.16871v1-human-on-the-bridge.pdf` (33 pages; SHA-256 `1f047297db1f5496ec2168f05c9a4f1af335f48159d855beb73395c9a582d134`)
- **Local text:** `data/papers/text/2606.16871v1-human-on-the-bridge.txt` (SHA-256 `c9093d20e922972caa6ccd7738499a7cd8c373b6d8a171c8eb43e342e2e0ef49`)
- **Official release inspected:** https://github.com/ProofAgent-ai/proofagent-harness at paper-time commit `424053ca1749051fe03c67534fc909fe63e1cc83` and post-v1 acquisition commit `95ec9e42b7d1e571493dbe3e691d75fa1eed1187`
- **Release provenance:** `data/sources/releases/2606.16871v1-human-on-the-bridge/provenance.json`
- **Tags:** expert-curation, adversarial-evaluation, multi-turn-agents, llm-judge, trace-audit, fallback, cost, release-audit

## One-sentence contribution

Human-on-the-Bridge (HOB) proposes a useful organizational pattern—have humans author reusable adversarial scenarios, juror perspectives, scoring rules, trace checks, and recovery policies, then execute them repeatedly—but the paper does not identify who the experts were, how their authority was established, how the evaluation intelligence was authored or validated, or release the 470 reported runs, so it demonstrates an inspectable evaluation-policy engine and reports a large execution episode, not scalable preservation of expert judgment or calibrated evaluation quality.

## Why this matters for skill-bench

HOB addresses a central `skill-bench` question: where can scarce domain-expert effort have compounding leverage? Its answer is upstream authoring rather than per-run review. That is directionally compatible with charter objectives B, C, and F: an expert can contribute a critical incident, fair consequence, evidence requirement, decision threshold, or escalation policy once, and the benchmark can reuse that contribution across configurations and versions.

The paper's most important lesson is also its main validity gap: **reuse scales whatever was encoded, including unsupported authority, brittle policy, hidden obligations, and grader bias**. A trap library is not “expert intelligence” merely because it is detailed. A persona is not an independent juror. A trace-linked quote is not proof that a criterion is legitimate or that a detector found every violation. Amortization lowers marginal execution cost only after the upstream instrument has earned a validity claim and remains current.

The official release makes this distinction unusually concrete. The paper-time snapshot contains 183 detailed trap manifests, three persona prompts, scoring skills, deterministic defect heuristics, a multi-turn conductor, consensus code, reporting, and tests. It therefore supports inspection of how evaluation policy is encoded. Yet all 183 trap manifests lack author, expert, citation, provenance, version, and review metadata; the documentation says their composite attack chains were generated from per-family templates. Neither archived snapshot contains the exact 47 completed configurations, 470 runs, 23,500 turns, reports, score records, expert-curation records, or cost ledger claimed in the paper. The result is a strong case for separating **evaluation-policy artifacts**, **authority/validation records**, and **empirical execution evidence**.

This is a cross-domain evaluation-method case, not a proposal to narrow `skill-bench` to finance, healthcare, code safety, or red teaming.

## Research question and claim boundary

The paper asks whether human expertise can be moved from repeated Human-in-the-Loop review into reusable “evaluation intelligence” that an automated harness executes across agents, domains, versions, and evaluator tiers. It also asks whether smaller Harness LLMs can expose objective behavioral failures in frontier-LLM-based agents and whether fallback policies preserve evaluation continuity (Sections 1, 3, and 4, pp. 3–28).

The paper supports bounded claims that:

- HOB defines an intelligible placement model for human input: domain context plus traps, juror personas, scoring guidelines, audit rules, and fallback policies (`D,T,J,S,R,F`; pp. 11–17);
- the released paper-time software can generate multi-turn adversarial interactions, capture declared tool/retrieval fields, ask one LLM under three persona prompts to score five metrics, re-vote when score spread exceeds a threshold, aggregate scores, and record fallback accounting;
- the manuscript reports 47 completed domain–agent–Harness-LLM configurations, each summarized from ten 50-agent-turn runs, for 470 runs and 23,500 agent turns (Tables 1–2, pp. 18–20);
- the reported episode includes examples of claimed-but-unobserved tool actions, missing required logging calls, non-resolving refusal, and 414 evaluator-pipeline recovery events (Sections 4.7–4.8, pp. 26–28).

It does **not** establish that human domain experts authored or approved the released artifacts; that the traps represent real work or relevant risk populations; that juror scores agree with qualified humans; that objective detectors are sensitive, specific, or model-tier invariant; that smaller evaluator models discover the same failures as larger models; that the selected configurations support agent or evaluator rankings; that fallback preserves the same measurement transaction; that costs are lower than expert review; or that HOB is professionally valid, safe, production-ready, or general across domains.

The paper itself concedes two major limits: subjective juror scores are not calibrated against human expert judgment, and the selected sweep is non-factorial with sparse cells (Section 4.9 and Section 5, pp. 28–30). The release audit adds a more severe ceiling: the empirical records needed to verify even the reported descriptive comparisons are absent.

## Methodology and system reconstruction

### HOB's four pillars and the missing authority layer

The paper calls four components the HOB pillars (Section 3.1, pp. 13–15):

1. **Red-Team Traps** encode pressure conditions and anticipated failure modes.
2. **Juror Personas** encode scoring perspectives such as safety, compliance, task success, privacy, and manipulation resistance.
3. **Scoring guidelines and audit rules** connect judgments to observable turns, tool calls, omissions, policy violations, refusals, and claims.
4. **Fallback policies** classify evaluator-pipeline failures and prescribe retry, reroute, incomplete-run, or human-escalation behavior.

The formalization is a component inventory, not an empirical model. `IHOB=(D,T,J,S,R,F)` names the inputs; `O=(τ,s,Φ,ρ)` names trajectory, score vector, detected failures, and report. It does not specify contributor qualifications, evidence provenance, review independence, criterion applicability, uncertainty, instrument versioning, or the warrant connecting a score to a decision.

The paper repeatedly says “human experts curate” this intelligence, but gives no number of experts, professions, qualifications, recruitment method, compensation, authoring time, conflict policy, assignment, review protocol, agreement measure, correction process, or mapping from expert claims into traps and rules. The sole author is affiliated with ProofAgent.ai and the University of Chicago; the acknowledgments state ProofAI LLC support (p. 32). This does not invalidate the system, but it means commercial authorship, community feedback, evaluation-engineering expertise, and domain-professional authority cannot be treated as interchangeable.

### Released trap library

The paper-time repository contains 183 Markdown trap manifests across 11 families. Local complete-archive inspection found:

- 24 social-engineering, 22 factuality, 21 prompt-injection, 20 compliance, 16 data-exfiltration, 16 verbal-abuse, 14 business-logic, 14 tool-misuse, 13 policy-drift, 12 code-safety, and 11 bias traps;
- all 183 specify family, metrics, name, severity, and tags;
- 157 are declared universal and 26 have domain lists;
- 162 include pass criteria and 161 include fail criteria;
- none contains provenance-like frontmatter for source, citation, author, expert, version, creation/update time, or approval.

The manifest specification explicitly makes only basic identity/severity/metric/reach fields and a Pattern section mandatory. Pass/fail criteria are recommended rather than required, and the runtime loader is intentionally permissive while the validator warns about quality. This is reasonable extensibility engineering, but it permits executable scenarios whose public basis, professional legitimacy, expected behavior, and scorer evidence have never been established.

The released `unauthorized_tool_call` trap illustrates both value and risk. It specifies forbidden tools, multi-call composition attacks, least-privilege behavior, pass/fail criteria, and a cumulative-disclosure threat model. This is substantially richer than a generic jailbreak prompt. But it cites no incident, policy, regulation, subject-matter expert, or validated environment. Some tool names and approval assumptions are synthetic. The artifact can test compliance with its authored policy; it cannot by itself establish that the policy is correct for a real organization.

The documentation also states that the 183 composite attack chains are generated from per-family templates and injected at dataset-build time. Thus “human-curated” describes at most upstream template/content authorship; it should not be read as 183 independently elicited expert critical incidents.

### Multi-turn execution and evidence contract

The planner chooses traps and lays out turn specifications. The conductor uses the same configured Harness LLM to craft one user message per turn from the trap pattern, first seed, pass criteria, role/business case, recent history, and optional follow-up/callback directives. Only the four most recent turns are included in ordinary history, although a callback can retrieve one targeted earlier exchange. If question generation fails, the release falls back to the first seed verbatim.

The Agent Under Test returns text plus declared `tools_called`, `retrievals`, `memory_snapshot`, and optional reasoning. The harness records these in a `Turn`. This is a useful trace contract, but it trusts the adapter-supplied fields; the paper does not show that tool records are independently reconciled with environment state or provider logs. A false empty list, incomplete adapter, or fabricated tool result can therefore become evaluator “ground truth.”

Deterministic heuristics flag exact forbidden/expected tool names, a dictionary of action-claim phrases with empty `tools_called`, vague refusals without predefined anchor strings, and possible prompt-echo strings. These checks are inspectable and can be valuable regression detectors. They are not complete semantic verifiers. For example, “I’ve updated the working note” can trigger a phantom-action heuristic, but linguistic variants can evade it; conversely, a legitimate statement about an external action may match a phrase. The financial example's denominator—40 “substantive financial” turns requiring logging—is semantically classified, not self-evidently objective merely because tool-call presence is mechanically countable.

Jurors see the transcript plus the planner's expected behavior, trap pass/fail criteria, operational fail signals, the Agent Under Test's system prompt, knowledge, and tool schema when available. This makes scoring evidence-rich, but also exposes answer-bearing evaluation policy. It measures compliance with a disclosed-to-the-judge authored instrument, not an independent discovery of professional correctness. Context can be truncated; the release drops oldest transcript turns when budgets are exceeded and emits a truncation event. The paper reports no truncation rates or score sensitivity.

### Multi-juror topology is prompt diversity, not observer independence

The paper describes multi-juror scoring and disagreement resolution. In the paper-time implementation, one Harness LLM endpoint is invoked under three persona prompts—rigorous, lenient, and contrarian—for each of five metrics. All personas share the same model, rubric, transcript, expected-behavior text, deterministic defect flags, and calibration prompt. Round one calls are separate and parallel, but the observers are not independent in model family, training, evidence, policy, or implementation.

The persona design intentionally manufactures location differences. The rigorous persona says it should score at least one and typically two points below the lenient persona, uses a default around six, and applies detailed tone deductions. Persona spread is therefore partly a treatment imposed by the prompts, not an estimate of naturally occurring evaluator uncertainty. Median consensus can cancel the designed extremes without showing correctness.

For `delphi` and `debate`, any metric with a round-one max–min spread above one point is re-scored. Each persona receives the other personas' names, scores, and reasoning; the user message nevertheless labels these peer scores “anonymized.” Final consensus uses round-two scores when available and computes “confidence” as `1 - spread/10`. This is convergence, not calibrated confidence. Shared-model social convergence can reduce spread while preserving a common error.

The inspected code treats `delphi` and `debate` identically in consensus routing: both trigger the same one-round re-vote based on the same spread rule. No distinct debate protocol appears in the paper-time source, despite the README describing debate as the strictest and more expensive mode. This release-level mismatch reinforces the need to bind every empirical result to exact code and configuration.

### Scores, aggregation, and certification

The five subjective metrics are task success, hallucination resistance, safety, instruction following, and manipulation resistance. Each persona emits per-turn categorical audit entries and a 0–10 score. Median, mean, or minimum can aggregate personas per metric; mean is the default final aggregation across metrics. The paper instead says its reported configuration score is the median across the five per-metric medians over ten runs (Section 4.2, p. 21), so the exact paper analysis path must be distinguished from library defaults.

The release contains authored hard caps and thresholds. For example, one failed turn can cap scores, a missing system prompt or tools can impose metric ceilings, and final scores map to `GOLD`, `SILVER`, `NEEDS_ENHANCEMENT`, or `NOT_READY`. These are policy choices, not empirically calibrated decision thresholds. Calling them certification labels risks laundering one author's score rules into readiness claims. The manuscript appropriately says its experiment is not intended to issue certification labels (p. 18), but the software's public schema does issue them.

The paper reports only aggregated medians and selected examples. It does not report score distributions, run-level values, intraclass correlation, variance components, uncertainty intervals, juror agreement, objective-detector confusion matrices, missingness, truncation, retry counts by stage, or severity-label reliability.

### Experimental sampling and denominators

The reported unit “evaluation configuration” is one domain–agent–Harness-LLM setting. The manuscript names three domains (code generation, financial advisory, medical triage), four frontier backbone families (GPT-4.1, GPT-5.5, Claude Opus 4.7, Claude Opus 4.8), and five Harness LLM tiers (4B Gemma, 8B Llama-3.1, 32B Qwen-3, 70B Llama-3.3, 120B GPT-OSS). Each completed configuration has ten claimed “independent” 50-agent-turn runs. The selected sweep planned 50 configurations and completed 47; three were excluded for persistent provider unavailability (pp. 18–20).

This is not a full factorial. Most domain–agent–tier cells appear once, and the selection rule is described only as balancing coverage, cost, and availability. Consequently:

- Harness-tier medians pool different agents/domains;
- agent-backbone medians pool different harness tiers/domains;
- metric differences across evaluator tiers can reflect configuration composition rather than evaluator strictness;
- three dropped configurations create availability-conditioned missingness;
- ten runs stabilize one selected configuration but do not repair sparse cross-configuration comparison;
- “independent” is not operationalized through seeds, generated trap schedules, endpoint state, or shared context.

The 23,500 denominator is arithmetically `47 × 10 × 50` agent turns, not 23,500 independent tasks, users, critical incidents, or expert judgments. Turns nest within generated trajectories, runs, configurations, domains, agent implementations, and evaluator policies. The paper provides no cluster-aware intervals.

### Symmetric and asymmetric evaluation

The paper defines symmetric evaluation as comparable capability between Harness LLM and Agent Under Test backbone and asymmetric evaluation as a smaller evaluator testing a stronger agent. It operationalizes “amplification” as surfacing trace-verifiable failures rather than achieving higher subjective scores (pp. 18 and 22–23).

This is a defensible target but the experiment does not identify it. There is no no-curation ablation, no matched smaller-versus-larger evaluator detection table on the same trajectories, no human-labeled failure inventory, no recall denominator, and no false-positive analysis. The paper's own roadmap calls for removing traps, jurors, and audit rules to isolate their contribution (p. 30). Without that ablation, the study cannot distinguish:

- a small model generating the adversarial turn;
- a deterministic heuristic flagging a string/tool mismatch;
- a shared trap making the expected answer obvious;
- a larger/fallback model rescuing an invalid output;
- and a qualified expert judging the behavior.

Once a candidate phantom call is pointed out, checking an empty tool list may be easy. The hard evaluation problem is whether the right pressure was generated, the tool log is complete, the requirement applies, the linguistic claim really asserts completion, and all relevant failures—not merely selected examples—were found. HOB's claim shifts from evaluator strength to orchestration quality, but that orchestration was not independently validated.

### Fallback and continuity

The paper reports 414 recovered pipeline events: 220 content-policy blocks, 138 JSON parse errors, 49 secondary JSON parse errors, six authentication errors, and one other event (Table 7, p. 27). It says blocked or malformed juror output is retried or rerouted and not scored as agent failure.

The release confirms meaningful engineering: fallback receives the original prompt rather than the primary's broken response, uses separately tracked token/call counters, and can route transport or JSON failures to another model. Tests cover these behaviors. However, recovery is not measurement invariance. Switching model, provider, prompt compactness, output-token cap, or endpoint changes the configured observer. The release itself adds a stricter compact-output system message and smaller token cap for fallback. A recovered score should therefore retain fallback lineage and belong to a different grader realization unless equivalence is demonstrated.

The paper does not report how many calls were attempted, which stages/configurations/metrics triggered fallback, how often the stronger model supplied the final score, whether recovered and unrecovered cases differ, or whether rerouting altered score distributions. “No completed configuration was lost” establishes continuity, not validity. It also sits beside three configurations omitted for provider unavailability; the distinction may be stage or persistence, but exact failure records are absent.

### Cost model and evidence

The paper gives an algebraic break-even model:

`CHITL(N)=N·Ch`

`CHOB(N)=Cc+N·Ce+rN·Cr`

with break-even `N*=Cc/(Ch-Ce-rCr)` when the denominator is positive (pp. 17–18). This correctly states the conditions under which amortization would occur. It does not estimate any term. There are no expert-curation hours, expert rates, execution tokens, provider prices, latency, fallback share by configuration, audit burden, flagged-review rate, maintenance cost, or measured HITL comparator.

The release can record primary/fallback tokens and estimated cost for new runs, but neither snapshot contains the paper's ledger. Therefore “reduced operational and token cost,” “cost-efficient asymmetric evaluation,” and “production-scale” are hypotheses/prescriptions, not empirical results of v1.

## Evidence and result interpretation

### Subjective score tables do not rank agents or evaluators

Harness-tier median configuration scores range from 7.76 for 4B Gemma to 6.27 for 120B GPT-OSS (Table 3, p. 22). The paper interprets lower larger-model scores as stricter judging, while explicitly warning that magnitude is not evaluation strength. That caution is correct. But “stricter” is still not identified: the tiers do not necessarily score a balanced matched configuration set, and no human criterion establishes that lower scores are more accurate.

Per-agent medians similarly place Claude Opus 4.8 highest on four defensive dimensions and GPT-4.1 highest on task success (Table 4, p. 23). The paper calls these indicative. Even that description should be bounded by unknown configuration mixtures, agent skills/tools/grounding, endpoint realization, and missing uncertainty. These are configured-system observations, not base-model profiles.

The Opus 4.8 versus 4.7 paired table is stronger because it claims matched Harness tier, persona, domain, and seed (Table 5, p. 24). Yet the number of matched pairs per tier is mostly absent except the explicit `n=1` rows, agent implementation differences beyond backbone are unspecified, run-level paired values are unreleased, and no interval or paired cluster test is reported. It can motivate a regression investigation, not establish a robust version effect.

### Failure examples are useful demonstrations, not detector validation

The phantom-tool example (8/50 turns) and mandatory-log example (10 calls for 40 substantive financial turns) illustrate why final text alone is insufficient. They support the design requirement that claims and required actions be reconciled with trace/state evidence. They do not establish prevalence, severity, or detection accuracy. Only selected cases are shown; there is no sampling rule for 103 severity-graded findings, independent adjudication, false-positive review, or missed-failure audit.

The non-resolving-refusal example shows the value of keeping task completion separate from safety/manipulation resistance. Its task-success score of 4 remains one model-judge observation under an uncalibrated rubric, not objective proof of operational failure.

### The empirical headline is not reproducible from the release

Section 4.1 says exact model snapshots/access dates, decoding parameters, random seeds, curated traps/personas/rubrics, and every reported configuration are released so configurations can be re-executed and detections re-derived (pp. 18–19). Complete inventories of both archived official snapshots contradict that broad release claim. They contain framework code and content libraries but not:

- the domain-by-agent-by-Harness-LLM matrix;
- exact paper-run model/request manifests;
- 470 run records or 23,500 turns;
- evaluation reports or evidence-linked findings;
- per-run/per-configuration score tables;
- paired-version records;
- fallback event ledger;
- token/cost accounting;
- expert identities, authoring records, or approvals.

The paper-time snapshot is the closest implementation evidence. The later snapshot, committed 28 days after v1, expands observability/governance code and personas but cannot be treated as paper-time code. Neither can reproduce or falsify the headline empirical comparisons.

## Unique insight

HOB's deepest transferable insight is a **human-effort placement hypothesis**: expert effort can compound when transformed into versioned, executable evaluation policy rather than spent only on repeated terminal labels. But the proper object is not an undifferentiated “evaluation intelligence” bundle. It is an authority-preserving chain:

`expert/source claim → scoped critical incident → public requirement or fair consequence → pressure realization → required evidence view → detector/judgment policy → calibrated observation → bounded validity claim → maintenance/reconsent trigger`.

Every arrow can fail. HOB currently makes the middle executable while largely assuming the beginning and end. Its release proves that trap, conductor, juror, audit, consensus, and fallback machinery can be encoded. It does not prove that expert authority entered the chain, survived template generation and prompt transformation, or licensed the final scores.

This yields a sharper scaling law for `skill-bench`: **the reusable unit is a governed evaluation-policy module whose marginal execution can scale only within a validated scope**. It needs contributor authority, evidence provenance, public-basis classification, transformation lineage, observer admissibility, calibration evidence, version dependencies, and expiry/incident triggers. Reuse outside that envelope is policy copying, not expertise scaling.

A second insight is that evaluator diversity must be decomposed. Three persona calls to one model create **perspective variation**, not three independent raters. Deterministic trace checks create **method diversity**, but only for predicates their evidence view can decide. Qualified human adjudication creates **authority diversity** when roles and independence are real. These should not be collapsed into “multi-juror confidence.”

## Comparison with existing project evidence

- **ResearchRubrics** documents a three-role human author/reviewer/final-review pipeline and over 2,800 reported human hours for 101 prompts and 2,593 criteria. Its authority, atomicity, agreement, and aggregation remain limited, but it at least exposes an authoring workflow and released criterion corpus. HOB adds reusable adversarial execution, traces, personas, and fallback; it supplies almost no expert-labor or approval evidence. HOB therefore cannot inherit ResearchRubrics' stronger authoring evidence merely by calling artifacts expert-curated.
- **EvalAgent** shows that evaluation-engineering skills improve first-run generation of executable, non-vacuous evaluator artifacts, while not establishing construct validity. HOB is the same boundary at the execution layer: runnable traps and judges are conformance evidence, not evidence that their requirements are professionally correct.
- **AgentRewardBench and RuVerBench** directly compare configured model judges with plural or adjudicated human labels and expose evidence-view, prevalence, parser, prompt, batching, and judge-specific error surfaces. Their human authority is imperfect, but they measure observer agreement. HOB reports no human–juror calibration at all; its persona spread and convergence cannot substitute for a labeled calibration set.
- **Many-Facet human/AI rater analysis** shows that severity, task, criterion, and rater interactions can differ even when aggregate agreement looks acceptable. HOB intentionally shifts persona severity and pools selected configurations, but fits no rater/task model. Its tier and persona differences are therefore treatment mixtures, not calibrated evaluator effects.
- **ELAIPBench** makes expert roles, adversarial authoring incentives, and evidence/answer verification explicit, while omitting important labor and mechanism histories. HOB omits even contributor counts and role records. Both show why final artifacts cannot validate the claimed participation mechanism without candidate, revision, rejection, time, and payoff/authority lineage.
- **Harness-Bench** treats the complete model–harness pairing as the reporting unit and warns that configuration variation is not a causal mechanism effect. HOB should do the same: planner, conductor, trap schedule, persona prompts, rubric, endpoint, fallback, adapter evidence, context truncation, and aggregation jointly define the evaluator. Its “small Harness LLM” claim cannot be attributed to model size alone.

Together these sources suggest a valid experimental sequence HOB has not yet completed: preserve qualified authoring lineage; construct independent planted/held-out cases; compare no-curation versus curated policy; cross evaluator tiers on identical frozen trajectories; retain raw predictions and invalid/fallback states; obtain blinded plural expert labels; estimate clustered errors and cost; then test whether conclusions transfer to new traps, domains, and agent versions.

## Limitations and validity threats

1. **Expert identity and authority are absent.** No contributor count, qualification, domain matching, role, or approval is reported.
2. **Authoring methodology is absent.** There is no elicitation, incident-sampling, source review, drafting, review, disagreement, or revision protocol.
3. **Commercial conflict is material.** The sole author is affiliated with ProofAgent.ai, ProofAI LLC supported the work, and the paper evaluates its own framework; no independent evaluation is reported.
4. **Trap provenance is absent.** All 183 paper-time manifests lack author, source, citation, expert, version, or approval metadata.
5. **Template generation weakens the curation claim.** Composite attack chains are generated by per-family templates, not demonstrated independent expert incidents.
6. **Trap reach is mostly asserted universal.** 157/183 manifests declare universality without evidence of cross-domain applicability.
7. **Public basis is not recorded.** Hidden pass/fail expectations can encode surprise obligations or author preferences.
8. **Trace authority is adapter-dependent.** Declared tool/retrieval fields are not independently reconciled with environment state.
9. **Detectors are narrow heuristics.** String/tool-name checks have unmeasured false positives and false negatives.
10. **Semantic applicability is mislabeled objective.** Determining whether discussion is substantive or a tool is mandatory can require judgment.
11. **Three personas are one model.** Shared endpoint, evidence, rubric, and prompting create correlated observers.
12. **Persona disagreement is designed.** Explicit severity offsets manufacture spread that cannot estimate natural uncertainty.
13. **Consensus is not correctness.** Median and re-vote convergence can preserve common-mode error.
14. **Confidence is uncalibrated.** `1-spread/10` is a dispersion transform, not empirical probability.
15. **Delphi/debate release behavior is indistinguishable.** Both use the same spread-triggered re-vote in the inspected paper-time code.
16. **Jurors receive answer-bearing policy.** Expected behavior and trap criteria make scoring policy compliance easier than independent professional verification.
17. **Context truncation is unreported.** Older turns and evidence can disappear from the judge view.
18. **Five metric scales are not validated.** Definitions, hard caps, tone deductions, and thresholds reflect authored policy.
19. **Certification labels are unsupported.** Software thresholds map uncalibrated scores to readiness-like labels.
20. **Configuration selection is opaque.** The 50 planned cells are purposively selected for coverage, cost, and availability without a released matrix.
21. **The design is non-factorial.** Agent, domain, evaluator tier, tools, skills, and grounding are confounded.
22. **Missing configurations are availability-conditioned.** Three cells are dropped with no intent-to-evaluate ledger.
23. **Runs are clustered.** 23,500 turns are nested observations, not an independent sample size.
24. **Run independence is undefined.** Seeds, trap schedules, generated turns, provider state, and retries are unreleased.
25. **No clustered uncertainty.** Tables report medians/min/max but no task/configuration bootstrap, hierarchical model, or confidence intervals.
26. **No human calibration.** Subjective scores have no expert agreement, severity, or decision-validity evidence.
27. **No detector validation.** Objective findings lack sensitivity, specificity, recall denominator, or blinded adjudication.
28. **No curated-intelligence ablation.** The effect of traps/personas/rules is not separated from the base Harness LLM.
29. **No matched tier detection analysis.** Smaller and larger evaluators are not compared on identical frozen trajectories against ground truth.
30. **Agent-backbone labels are insufficient.** Skills, tools, grounding, scaffold, provider snapshots, and policy differ or are not disclosed.
31. **Fallback changes the evaluator.** Model/provider/prompt/token-cap substitutions are treated as continuity rather than a new grader realization.
32. **Fallback denominator is missing.** 414 events cannot be interpreted without total calls, affected stages, configurations, and final-source lineage.
33. **Cost is algebra, not measurement.** No term in the break-even model is estimated.
34. **Severity findings are opaque.** The 103 findings lack selection, rubric, adjudication, and release records.
35. **Selected examples can overstate coverage.** Three vivid cases do not establish prevalence or systematic discovery.
36. **No contamination or policy memorization control.** Public traps and expected language may be familiar to agent/evaluator models.
37. **No maintenance evidence.** Regulatory and domain claims can expire, but no source-validity or reapproval lifecycle is evaluated.
38. **Release claim is contradicted by inspection.** Exact configurations and empirical artifacts promised on pp. 18–19 are absent.
39. **Post-v1 code cannot fill paper-time gaps.** The later snapshot changes implementation and still lacks empirical records.
40. **Generalization is unsupported.** Three author-chosen domains and one framework do not establish a domain-independent scalable-expert mechanism.

## Reproducibility and operational realism

Reproducibility is **strong for inspecting and running the general framework, moderate for deriving new synthetic trace checks, and weak for reproducing the paper's experiment or claims**. The immutable paper, paper-time code snapshot, post-v1 snapshot, trap library, persona prompts, scoring skills, schemas, and tests are preserved. The archives make evaluator-policy implementation unusually inspectable.

Exact replay is blocked by the missing configuration matrix, target-agent code/configuration, endpoint snapshots/access records, trap schedules, prompts, trajectories, raw juror outputs, fallback ledger, score tables, analysis code, and cost records. The paper-time commit predates v1 by seven days but is not pinned by the manuscript; the later commit postdates v1 by 28 days. Even a fresh run would be a new experiment under mutable providers.

Operational realism is mixed. Multi-turn pressure, callbacks, explicit tool traces, failure typing, pipeline recovery, and evidence-bearing reports are relevant to production agent evaluation. But the tests are generated from authored traps rather than sampled operational work; tool evidence is adapter-supplied; observer prompts reveal intended outcomes; no real domain-expert approval or downstream decision is observed; and recovery can silently substitute the evaluator. The framework is a plausible evaluation workbench, not evidence that its released policies measure real professional readiness.

## Transfer to skill-bench

### 1. Treat reusable evaluation policy as a governed module

A reusable module should bind:

- contributor and source authority, qualifications, scope, consent, and conflicts;
- exact claim/incident/evidence locators;
- public requirement versus private fair consequence;
- trap/pressure text, variants, generation transformations, and hashes;
- applicable domains/configurations and explicit exclusions;
- required evidence views and authoritative state sources;
- deterministic, model, and human observation policies;
- calibration set, error surface, claim ceiling, and decision threshold;
- dependencies, expiry, incident triggers, reapproval, supersession, and rollback.

The existing expertise-transfer, participation, benchmark-bundle, task-health, validity, and compounding-lesson contracts already provide these homes. HOB does not justify a new monolithic “evaluation intelligence” schema.

### 2. Separate four kinds of evaluation diversity

Record independently:

1. **policy perspective** (safety, completion, compliance, usability);
2. **observer realization** (model, prompt, parser, evidence view, call topology);
3. **method** (deterministic state check, semantic judge, qualified human judgment);
4. **authority** (who may license which interpretation).

Three persona prompts to one model are three policy realizations with strongly shared error, not three independent jurors. Consensus confidence must be calibrated against held-out labels or outcomes, not inferred from prompt-induced spread.

### 3. Make fallback a typed substitution, not invisible recovery

Every failed call should retain stage, primary request/response, failure class, retry, substitute model/provider/prompt/token budget, final observation source, tokens/cost/latency, and equivalence status. A substituted observer creates a new grader realization unless held-out evidence supports equivalence. Missing or invalid observations should remain separate from agent failures and from negative criterion labels.

### 4. Validate the amplification hypothesis causally

A minimal design should freeze trajectories or use matched seeds and cross:

- no authored policy / generic prompt;
- traps only;
- traps plus deterministic rules;
- traps plus personas/rubrics;
- small versus large evaluator;
- no fallback versus typed fallback.

Use independently planted and qualified-human-adjudicated failures, preserve false positives/negatives and unresolved cases, cluster by trajectory/configuration, and measure tokens, cost, latency, and human audit. This distinguishes discovery, verification, and rerouting from one another.

### 5. Preserve plural outcomes and claim ceilings

Keep trace predicate, criterion applicability, subjective score, task resolution, safety, and pipeline health separate. An exact tool-call mismatch can support a narrow trace-consistency finding. It cannot alone support a domain-compliance, professional-quality, safety, or deployment-readiness claim. “Evidence-linked” describes observability, not the authority or completeness of evidence.

### 6. Test reuse and decay rather than assume them

The key HOB hypothesis is longitudinal: one upstream contribution remains useful over many runs and versions. Measure reuse count, marginal review time, false-alert rate, newly discovered misses, source/policy drift, reapproval burden, and transfer to held-out tasks/domains. Compare expert-authored modules with analyst-authored and model-generated modules under blinded review. This directly tests whether authority-preserving reuse saves effort without freezing stale or idiosyncratic policy.

## Concrete repository implications

1. No new schema task is warranted. The existing participation/authority, expertise-transfer, bundle/evidence-view, task-health, validity-argument, metric-monitoring, and fallback/configured-system records already cover the nonduplicate requirements.
2. A future real expert-contribution pilot should use HOB as a **placement hypothesis**, not a validity claim: obtain one consented expert critical incident, preserve its source and decision boundary, derive one pressure module, and compare repeated automated execution with blinded expert review on held-out cases.
3. Existing plural-grader validation should classify persona diversity separately from independent observer/authority diversity and reject spread-derived “confidence” without calibration.
4. Existing trial records should treat fallback model/prompt/token-cap changes as grader-version substitutions and preserve invalid/missing states.
5. Any benchmark report should state denominators at task, trajectory, turn, criterion, observation, and qualified-review levels; `turns` must never be presented as an effective independent sample size.
6. No build or consolidation queue item is added: these findings refine existing contracts and future expert/grader calibration work rather than reveal a distinct executable gap.

## Action items completed

- [x] Read the complete immutable v1 paper, including methodology, tables, discussion, acknowledgments, and references.
- [x] Verify paper claims against the local immutable PDF/text and preserve exact hashes and paths.
- [x] Inspect complete paper-time and post-v1 official repository archives with explicit timing boundaries.
- [x] Audit all 183 paper-time trap manifests for family, domain, criteria, and provenance metadata.
- [x] Trace representative trap, conductor, juror, consensus, aggregation, schema, calibration, and fallback implementations.
- [x] Separate the four-pillar prescription, reported empirical episode, release-supported implementation evidence, and unsupported commercial/production claims.
- [x] Reconstruct configuration/run/turn denominators, aggregation, symmetric/asymmetric thesis, paired comparison, fallback accounting, and cost model.
- [x] Compare nonduplicatively with ResearchRubrics, EvalAgent, AgentRewardBench/RuVerBench, many-facet rater evidence, ELAIPBench, and Harness-Bench.
- [x] Map implications to existing repository contracts without creating a duplicate task.

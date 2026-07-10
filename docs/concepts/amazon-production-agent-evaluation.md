# Production metrics are measurement contracts, not labels

## Source and review status

- **Primary source:** Yunfei Bai, Allie Colin, Kashif Imran, and Winnie Xiong, “Evaluating AI agents: Real-world lessons from building agentic systems at Amazon,” AWS Machine Learning Blog, published 2026-02-18: <https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-real-world-lessons-from-building-agentic-systems-at-amazon/>
- **Full local source:** `data/sources/aws-evaluating-ai-agents-real-world-lessons.md`
- **Provenance:** `data/sources/aws-evaluating-ai-agents-real-world-lessons.provenance.json`
- **Local extraction:** 29,706 bytes; SHA-256 `c0460153c8a9ad91b1832419048723fffd3e3f0ba7732bb3c9765b39047152be`.
- **Read and verified:** 2026-07-10. The complete official article extraction, including all three use cases, was read. A fresh fetch of the canonical page returned 1,068,380 bytes and contained the article’s “thousands of agents,” historical-log-derived golden dataset, planning-score, and continuous-production-evaluation claims. Its SHA-256 (`66a33a96e648e84da09209ace288f4b7be90b99598529caadf231ccdc19e88c3`) differs from the provenance-time raw HTML hash despite identical byte count and upstream `Last-Modified`, so the local extraction is the reviewed evidence object.
- **Evidence type:** official production experience and prescription. It is not a controlled study, released evaluation suite, or quantitative incident report.

## Charter fit and useful completion

This review advances charter objectives A–C by examining production evaluation across shopping, customer service, and seller-assistance systems and translating it into a cross-domain measurement requirement. It is **consolidation of production evidence**, not a proposal to make `skill-bench` an Amazon, customer-service, or multi-agent benchmark. The concrete artifact is this source-grounded measurement note. It clarifies whether a list of metric names plus per-trial check scores is enough to support diagnosis and production monitoring. Useful completion means retaining Amazon’s operational decomposition while explicitly blocking the unsupported inference from a named metric to a valid, reproducible measure.

## Contribution and research question

The article asks how Amazon teams can evaluate heterogeneous production agents through one framework without reducing them to final-answer quality or locking evaluation to an agent framework. Its contribution has three parts:

1. a four-step workflow from offline/online traces through a metric library, result storage/dashboarding, and audit/alerts/HITL (source lines 25–43);
2. a three-layer decomposition of foundation model, agent components, and end-to-end outcome/business effects (lines 43–51); and
3. three production narratives covering large tool catalogs, intent routing, and multi-agent coordination (lines 109–149), followed by prescriptions to measure quality, performance, responsibility, cost, business outcomes, and production drift (lines 151–165).

The article reports that thousands of agents have been built across Amazon organizations since 2025 (lines 11–15), but it does not say how many systems used this framework, how evaluation changed their outcomes, or how the examples were selected. “At scale” is therefore context for the authors’ experience, not a measured sample size for the framework.

## Methodology and system described

The source is an experience synthesis. No search protocol, case inclusion rule, trial design, baseline, observation period, or statistical method is reported. The proposed system nevertheless exposes a useful operational architecture:

- **Inputs:** completed offline traces or online traces, submitted through a unified access point (lines 33–36).
- **Measurement:** default and custom evaluators at model, component, and whole-system layers (lines 37–51).
- **Persistence and presentation:** results in S3 or dashboards alongside trace observability (lines 39–40).
- **Decision loop:** rules and alerts for degradation, remediation, and scheduled human audits of sampled traces/results (lines 41–42).
- **Metric inventory:** final-response correctness/faithfulness/helpfulness/relevance/conciseness; goal success/accuracy; tool selection/parameters/errors/sequences; memory retrieval; topic adherence/refusal; grounding/reasoning consistency; and safety outcomes (lines 53–107).
- **Operational dimensions:** latency, throughput, resource use, direct and indirect cost, customer or business outcomes, and production drift (lines 153–161).

Three cases instantiate parts of the architecture:

1. **Shopping/tool use.** Amazon describes hundreds or thousands of APIs, cross-organizational interface/description standards, LLM-generated tool schemas, and golden regression datasets generated synthetically from historical query–API invocation logs. Evaluation uses tool selection, parameter, and multi-turn call metrics (lines 113–123).
2. **Customer-service routing.** An LLM simulator drives virtual personas over anonymized historical query/ground-truth-intent pairs. The evaluator compares predicted intent and routing with ground truth, then also measures final resolution and topic adherence/refusal (lines 125–137).
3. **Seller-assistance multi-agent coordination.** A planner decomposes and assigns work; specialists return states, results, or escalations; an orchestrator resolves dependencies and synthesizes. The article names planning, communication, and collaboration-success scores and says humans inspect decomposition, handoffs, contradictory recommendations, and consistency with business objectives (lines 139–149).

## Evidence actually offered

The strongest evidence is architectural specificity: the article identifies real transformation chains, observables, and failure consequences. Poor tool descriptions are linked to irrelevant calls, context expansion, latency, and cost; wrong intent is linked to wrong routing, irrelevant responses, human escalation, and operational cost; multi-agent decomposition is linked to handoff and contradiction risks (lines 123, 127, 149). These are plausible production failure signatures with concrete trace loci.

The article does **not** report the quantities needed to evaluate effectiveness:

- no task, trace, agent, customer, or team counts for the cases;
- no metric formulas, scales, denominators, thresholds, confidence intervals, or missing-data rules;
- no before/after comparison for schema standardization or API self-onboarding;
- no synthetic-to-real fidelity or label-agreement study for the golden datasets and virtual personas;
- no alert precision/recall, false-alarm burden, detection delay, remediation rate, or rollback outcome;
- no human sampling strategy, reviewer qualifications, inter-rater reliability, judge-human agreement, or audit cost;
- no release of traces, datasets, evaluators, judge prompts, dashboards, or incident records.

Accordingly, “significantly improved efficiency,” “objective assessment,” “critical,” and “indispensable” are author reports or prescriptions, not effect estimates demonstrated in the post. The claim that historical query–intent pairs are “ground truth” is also asserted rather than supported by labeling and adjudication evidence.

## Unique insight: a metric must bind an observation to a population and a decision

Amazon’s inventory demonstrates why metric labels are insufficient. “Tool selection accuracy” could mean exact agreement with one logged tool, acceptance of any tool in an expert-approved set, successful completion conditional on tool availability, or a judge’s semantic rating. “Communication score” is described only as inter-agent messages for subtask completion; counting messages could reward verbosity, while checking message entailment requires a reference and judge. “Collaboration success rate” is defined as successful subtask completion, but that can hide decomposition quality, dependency-critical failures, retries, and the fact that a poor plan can create easy but irrelevant subtasks.

A reproducible measurement therefore needs a contract:

```text
construct and intended decision
  -> unit of analysis and eligible population
  -> observable and evidence locator
  -> evaluator/version/reference policy
  -> numerator, denominator, missing/invalid-run rules
  -> aggregation, weighting, uncertainty, threshold
  -> subgroup/slice and drift baseline
  -> action, owner, audit, and rollback
```

This adds a needed boundary to the existing `skill-bench` stack. A trial check says what happened in one attempt. A task-health record says whether an instrument remains fit for an operational role. A validity argument says which interpretation and use the evidence licenses. A **metric specification** says how observations become a population statistic and a trigger. Without it, dashboards create false precision: identical labels can compute different estimands, and a threshold can cause operational action without a declared loss model or audit burden.

The production bridge is also causal, not merely hierarchical. Amazon’s three layers should not be summed into one score. Model quality may affect planning; tool-schema quality may affect selection; provider or tool availability may affect execution; successful execution may affect customer resolution; and resolution may affect business outcomes. Component metrics are diagnostic candidates. They become supported root causes only through trace evidence or interventions that distinguish upstream agent capability from interface, data, environment, and evaluator defects.

## Critical transfer issues

### 1. Synthetic golden data has a transformation boundary

The shopping case’s chain is historical query/API logs → LLM-generated examples → golden regression set. The customer-service case adds historical query/intent labels → virtual persona simulation → orchestration behavior. Each transformation can alter ambiguity, prevalence, language, tool alternatives, and error modes. “Historical” does not make generated cases representative; “golden” does not make synthetic labels authoritative. `skill-bench` should reuse its existing provenance and transformation-authority rule: generated cases retain source lineage, generator/configuration hashes, acceptance/rejection evidence, target-population scope, and held-out real/expert validation. This refines the queued participation/task-health work rather than requiring a duplicate synthetic-data schema.

### 2. Tool descriptions are part of the configured treatment

The source correctly treats tool signatures, parameter validation, output contracts, descriptions, and usage constraints as governance objects (line 123). These change agent opportunity and should be versioned alongside tools, not treated as incidental documentation. A tool-selection result without the candidate catalog, catalog size, descriptions, availability, and permitted-equivalence policy cannot separate model failure from discoverability/interface failure.

### 3. Multi-agent success needs edge and graph checks

Per-agent averages miss failures at decomposition, assignment, handoff, dependency, escalation, conflict resolution, and synthesis boundaries. Preserve node outcomes and typed edge observations separately. Planning quality should test whether the decomposition covers the parent goal and respects dependencies, not merely whether an assignment occurred. Communication should test required state transfer and contradiction handling, not message volume. Subtask success must not compensate for failure of a critical dependency or the parent objective.

### 4. Continuous monitoring changes the sampling problem

Offline benchmark tasks are curated; online traffic is policy- and time-dependent. Production monitoring therefore needs an eligible-event definition, sampling and privacy policy, traffic/version windows, subgroup coverage, delayed labels, missingness, seasonality, intervention history, and a frozen comparison baseline. Otherwise “agent decay” can be traffic drift, instrumentation change, tool outage, judge drift, or actual configured-system regression.

### 5. HITL must be an inspectable measurement process

The source gives humans four roles: audit automated results, create labels, calibrate model judges, and evaluate hard coordination/judgment dimensions (lines 23, 41, 149, 159). These roles have different sampling and authority requirements. A periodic audit estimates evaluator error only if selection probabilities and disagreements are retained; expert adjudication supplies a decision but not necessarily a population estimate. Human effort and error remediation must be reported as costs, as the source itself recommends at line 155.

### 6. Reasoning labels require observable boundaries

The post repeatedly proposes evaluating chain-of-thought coherence and faithfulness (lines 47, 91–97, 159). Hidden reasoning may be unavailable or unfaithful. `skill-bench` should score observable plans, messages, actions, tool calls/results, state transitions, artifacts, and declared rationales. It should not represent latent reasoning correctness as observed fact.

## Limitations and threats to transfer

1. **Selection and success bias.** Three favorable examples are presented without a sampling frame or failed comparison cases.
2. **Vendor coupling.** The generic workflow is described alongside AgentCore Evaluations, but there is no comparison showing framework independence or equivalent behavior across evaluators.
3. **Undefined metrics.** Most names lack operational definitions; some overlap (`correctness`/`goal accuracy`, two faithfulness concepts, grounding/context scores) or mix process and outcome.
4. **No quantitative production evidence.** Scale claims concern agents built, not evaluated runs or demonstrated gains from this framework.
5. **Unvalidated synthetic fidelity.** Historical provenance is invoked, but generation, acceptance, deduplication, coverage, and real-traffic validation are absent.
6. **No causal attribution method.** The layer decomposition helps locate symptoms but does not establish the earliest supported cause.
7. **No uncertainty or denominator policy.** Rates are uninterpretable without eligible events, invalid/missing handling, clustering, repeated users/tasks, and confidence estimates.
8. **No threshold governance.** Alerts and remediation are recommended without detection targets, false-positive costs, owner response times, or rollback criteria.
9. **No privacy/security protocol.** Historical interactions, traces, memory, tool parameters, and customer data are central inputs, but retention, redaction, access, and evaluator leakage are not specified.
10. **Business outcome validity is asserted.** The text links technical metrics to customer satisfaction, cost, and ROI but reports no evidence that those proxies predict those outcomes.

## Reproducibility and operational realism

The source is operationally realistic in recognizing many-tool catalogs, evolving APIs, multi-turn state, routing cascades, multi-agent boundaries, production drift, latency/cost tradeoffs, indirect remediation cost, and human oversight. Its four-step loop is a useful control-plane sketch.

It is not reproducible as an evaluation result. There are no executable artifacts or sufficient metric definitions to regenerate a score. The production narratives should therefore motivate failure hypotheses and data contracts, not validate a metric, threshold, synthetic-data method, root-cause label, or professional-readiness claim.

## Concrete transfer to `skill-bench`

### Preserve existing boundaries

Do not duplicate the current task/trial/grader/trace schema, score-family separation, configured-system hashes, root/surface/causal-slice labels, task-health lifecycle, validity argument, execution-validity record, or participation/transformation lineage. Amazon independently reinforces those choices but does not empirically validate them.

### Add one metric-specification and monitoring bridge

After the current pilot, validity, and task-health gates, add a small operating-layer contract that references—not embeds—immutable tasks, checks, graders, configured systems, and validity claims. Minimum fields:

- metric ID/version, construct, score family, and prohibited interpretations;
- unit of analysis, eligible population/event, inclusion/exclusion, sampling window, and clustering unit;
- observable/evidence paths, evaluator and reference versions, numerator/denominator or scale semantics;
- invalid, missing, delayed-label, retry, and duplicate-event handling;
- aggregation/weighting, uncertainty method, subgroup slices, and minimum support;
- baseline/comparator, drift/intervention windows, threshold and decision-loss basis;
- action, owner, audit sample, alert outcome, remediation, rollback, and expiry;
- transformation lineage for simulated/synthetic evaluation populations and fidelity evidence to the target population.

Semantic tests should reject (a) “tool selection accuracy” without an eligible candidate catalog and equivalence policy, (b) a production alert derived from pooled scores with no version/window or invalid-run rule, and (c) a synthetic golden set labeled representative without target-population fidelity evidence. A positive fixture can compute a narrow planted-failure detection rate from the LH pilot while explicitly prohibiting production- or professional-capability claims.

### Empirical tests implied by the source

1. **Tool-interface perturbation:** hold model/task constant, vary description quality and catalog distractors, and measure selection, parameter, latency, token, and outcome effects. This separates tool discoverability from model capability.
2. **Synthetic-fidelity audit:** compare historical/expert-labeled and LLM-generated cases by intent/tool distribution, ambiguity, disagreement, failure-type yield, and configured-system ranking. Treat generation as useful only within validated strata.
3. **Multi-agent boundary fixture:** plant one assignment, one missing handoff field, one unresolved contradiction, and one critical-dependency failure; verify that node averages cannot mask parent-goal failure and that diagnosis identifies the earliest evidenced boundary.
4. **Alert backtest:** replay versioned trial windows with planted grader, environment, traffic, and agent shifts; measure detection delay, false alarms, human review burden, and correct remediation routing.

These are project proposals derived from the source, not practices demonstrated by Amazon’s article.

## Concrete next actions

1. Add one non-duplicate queued build task for the metric-specification/monitoring bridge, dependency-gated after the existing pilot, validity, and task-health work.
2. During canonical consolidation, replace the taxonomy’s “AWS deep review remains pending” status with this note and preserve its evidence limit: production architecture and failure hypotheses, not measured effectiveness.
3. Do not add a separate synthetic-data or multi-agent schema task yet. First test whether the metric bridge plus existing provenance, configured-system, trace, and task-health contracts can represent the three proposed fixtures.

## Bottom line

Amazon’s article is most valuable not for its long metric list, but for exposing the path from traces to operational decisions across component, system, and business layers. Its cases reveal that every production score depends on a candidate tool universe, transformed evaluation population, workflow graph, traffic window, and action threshold. None is fully specified in the source. For `skill-bench`, the defensible transfer is to make those dependencies explicit: metric names become versioned measurement contracts, component failures remain hypotheses until causally supported, and monitoring statistics cannot license decisions without population, uncertainty, threshold, and audit semantics.
# AlphaEval: production provenance is not transformation validity

## Source and review status

**Deep review.** I read the complete immutable arXiv v1 PDF/text and inspected the complete official repository snapshot pinned below.

- Paper: Pengrui Lu et al., *AlphaEval: Evaluating Agents in Production*, arXiv:2604.12162v1 (14 April 2026), https://arxiv.org/abs/2604.12162v1
- Local PDF: `data/papers/pdfs/2604.12162v1-alphaeval-production-grounded-evaluation.pdf` (26 pages; SHA-256 `a153dcc5cb9977dc5886c8b4bfaa2bdaefa627508c4e7d3b63c56db6641c0f3b`)
- Local text: `data/papers/text/2604.12162v1-alphaeval-production-grounded-evaluation.txt` (SHA-256 `97e782068421702320f13ab812b12354591415331fefa28a95745f59b653bdf3`)
- Official repository: https://github.com/GAIR-NLP/AlphaEval at commit `754efe2d3939fdfab85f64ef23cbd12647a462da`, tree `b733f7591d1af76486c8790f03321d64d4e54c43`
- Archive: `data/sources/releases/2604.12162v1-alphaeval/GAIR-NLP-AlphaEval-754efe2.tar.gz`
- Provenance: `data/sources/releases/2604.12162v1-alphaeval/provenance.json`

The inspected commit is roughly three days after v1 submission, so it is later release evidence. It contains 89 tracked files, six evaluation templates, five explicitly fictional examples, runners, and Docker adapters—but not the 94 production task packages, source requirements, refinement histories, benchmark outputs, or full meta-evaluation labels. Paper results therefore remain reports rather than independently auditable release results.

## One-sentence contribution

AlphaEval contributes a four-stage, partner-mediated pipeline for turning company requirements into 94 executable tasks across six occupational labels and evaluates 14 commercial model–scaffold packages, but neither production provenance nor automated execution establishes that the formalized task, grader, score, or economic-value claim preserves the original production decision.

## Why this matters

This directly advances charter objectives A, B, and D. The project needs ways to convert real demand into benchmark artifacts without treating “came from production” as a validity shortcut. AlphaEval is valuable because it reports a prospective, month-long elicitation and refinement process rather than retrospective artifact mining. Its deeper lesson, sharpened by the release gap, is that requirement acquisition, benchmark transformation, evaluation automation, and claim licensing are separate evidence problems.

## Research question and claim ladder

The paper asks whether authentic company requirements can be rapidly converted into reproducible automated evaluations that better expose agent-product performance and economic value. Its implicit chain is:

```text
partner with paying-customer workflow
→ discover and scope a requirement
→ co-construct ground truth
→ package prompt/files/metadata/rubric
→ iterate with frontier agents and partner
→ automated score
→ domain/overall score
→ score × estimated human replacement cost
→ production gap, labor value, and agent-selection guidance
```

The paper meaningfully instantiates the middle pipeline. The endpoints are much weaker. A company origin supports **demand provenance**; it does not by itself support faithful requirement projection, representative occupational coverage, grader validity, production readiness, or realized value.

## Methodology and system

### Partner selection and requirement elicitation

Seven partners are selected to satisfy “as many as possible” of five criteria: authentic long-horizon requirements, revenue-integral agents, multimodal inputs, available domain expertise, and willingness to share anonymized data (paper p. 6). This is purposive access sampling, with no candidate-partner denominator, rejection log, company/task allocation, customer population, contributor counts, role authority, consent/ownership terms, or within-company task sampling frame.

Engagement lasts approximately one month through online meetings and site visits. Workflow discovery expands initial descriptions; scope negotiation selects self-contained segments; ground truth is extracted from real decisions or validated by experts; meetings occur at least weekly (pp. 5–6). The clinical example—“Word to JSON” becoming temporal phase identification, trigger extraction, field mapping, and constraint validation—is good evidence that elicitation changes the task model. But no interview protocol, raw requirement, decision log, disagreement record, source-to-task delta, or acceptance sign-off is released.

### Formalization and iteration

Partners receive a package contract: `query.md`, `task.yaml`, `files/`, `.eval/rubric.py`, and optional `ground_truth.json` (p. 6). The paper says the prompt preserves original specification while partners populate authentic content. Frontier-agent runs and partner verification average three to four refinement cycles per company, and some partners raise standards as systems improve (pp. 6–7).

This is a credible co-design workflow, not evidence of semantic invariance. Scoping can remove coordination and state; formalization can turn tacit conventions into hidden checks; agent-conditioned refinement can select tasks or thresholds around observed systems; changing quality bars can make scores across versions noncomparable. The paper reports cycles per company rather than per task, gives no before/after examples, and does not identify whether prompt, files, oracle, criterion, weight, environment, or acceptance threshold changed.

### Task portfolio

The 94 tasks are grouped as HR 11, Finance/Investment 22, Procurement/Operations 23, Software Engineering 11, Healthcare/Life Sciences 16, and Technology Research 11 (pp. 6–7). O*NET codes label domains, but O*NET does not provide the sampling distribution: one representative code per broad group cannot make 11–23 purposively contributed tasks representative of an occupation. Company clustering is not reported, so apparent domain breadth may partly reflect seven partner-specific task families.

Tasks include resume selection, investment reports, constrained BOM optimization, full-stack applications, clinical date calculations, policy analysis, and technology research. This is useful artifact and grader diversity. It remains a convenience portfolio selected for self-containment, anonymizability, automation, partner access, and sandbox feasibility.

### Evaluation and configured systems

Fourteen selected model–scaffold packages cover six models and four commercial CLIs. Pairings are selected for reported adoption and cost rather than a full factorial; defaults are left to each scaffold; Codex versions differ by model for API compatibility (pp. 8, 17). Thus same-model scaffold differences describe package outcomes but do not isolate a scaffold causal effect: adapter, CLI version, default parameters, tools, prompt policy, and model-serving path may all differ.

Tasks compose reference matching, formal/code checks, rubric evaluation, execution/UI tests, and an Opus 4.6 judge; the paper reports at least two leaf types per task and 2.8 on average (pp. 7, 18). A weighted sum produces each task score, task means produce domain scores, and equally weighted domain means produce the overall score (pp. 7, 16). Equal domain weighting is a policy choice—not evidence that each domain is equally important—and collapsing gates, correctness, subjective quality, and artifact validity into one scalar obscures failure severity and scale comparability.

The release makes the automation boundary concrete. `TASK_CREATION_GUIDE.md` recommends 10–20 answer-bearing rubric points and preserving ambiguity, while also advising domain context be placed in files. The LLM rubric implementation truncates responses at 30,000 characters, asks one judge a binary coverage question per point, and sums weights; it does not inspect source files, citations, structured artifact state, criterion dependence, or uncertainty. The generic semantic judge silently uses a text heuristic after JSON parse failure (`scripts/llm_judge.py`, lines 115–121). The HR example computes F1 against one shortlist, turning an actual hiring decision into ground truth without showing decision reliability, acceptable alternatives, fairness, or downstream success. These examples are fictional and cannot be projected onto every private task, but they refute any claim that the released interface alone validates production automation.

### Reliability and analysis

Only the best configuration is repeated three times. Table 4 labels intervals “95% CI,” but every endpoint is exactly mean ± reported standard deviation—for example overall 64.41 ± 1.83—not a 95% confidence interval for three independent runs (p. 10). Repeating only the winner cannot confirm that 14-configuration rankings are reproducible; selection of the apparent winner can also bias its reported stability. Tasks, companies, task families, judges, and repeated runs are nested, but no clustered uncertainty or multiplicity analysis is reported.

Meta-evaluation samples 20 LLM-judged tasks, five configurations, and 1,000 rubric-point judgments. Two experts have different strictness and agree with the judge at κ 0.697 and 0.780; three-way Fleiss κ is 0.720 (p. 10). This is useful point-level concordance evidence, but the paper omits expert credentials/domains, rubric-point sampling, prevalence/class balance, assignment and blinding, evidence views, adjudication, item dependence, and task/domain intervals. Agreement on answer coverage does not establish that criteria are complete, fair, independent, professionally consequential, or correctly weighted.

Failure analysis identifies plausible patterns—cascade errors, subjective collapse, retrieval failures, cross-section inconsistency, constraint misinterpretation, and format failures (pp. 10, 20–23). Yet coding method, analyst count, codebook, source sample, denominator, agreement, and adjudication are absent. Approximate percentages and quantitative claims such as 26% overruns or mapping errors rising from ~5% to ~25% therefore read as exploratory observations, not reproducible prevalence estimates.

## Evidence and what it supports

**Supported by the paper:**

1. The authors operationalized sustained partner engagement into a common task/evaluator package for 94 reported tasks.
2. The portfolio spans multiple professional artifact classes, modalities, and grader families.
3. Under the reported selected package matrix, scores vary substantially across package and domain.
4. Two human raters and one model judge show substantial reported point-level agreement on a sampled subset.
5. Production-oriented authoring surfaces requirement ambiguity, implicit conventions, environment fidelity, rubric decomposition, confidentiality, and criterion drift as practical tensions.

**Partially supported:**

- **Production authenticity:** company provenance and recurring partner engagement are meaningful demand evidence, but source requirements, transformations, approvals, and task samples are private.
- **Automated evaluation utility:** multiple grader types and point-level agreement support further use and calibration, not complete professional-quality measurement.
- **Configured-system dependence:** package scores differ, but the nonfactorial/default-config design does not identify scaffold effects.
- **Stability:** three runs estimate one selected configuration's short-run variation, not ranking reproducibility.

**Not supported by v1:**

- a general “research–production gap,” because no matched research-task control isolates production grounding from domain, difficulty, tools, budget, or grading;
- production readiness, because the benchmark removes live systems, organizational interaction, consequences, monitoring, and acceptance/rework;
- occupational representativeness, because O*NET is used for labeling rather than probability sampling;
- grader automation validity for all 94 tasks;
- $70K–$165K of labor “delivered,” because score is multiplied by estimated replacement cost without a validated quality-to-value function;
- configuration ranking reproducibility or causal scaffold effects.

## Unique insight: production-to-benchmark transfer needs a four-ledger transformation record

AlphaEval improves on benchmark provenance by starting with current demand, but it exposes four ledgers that must not be collapsed:

1. **Demand ledger:** who needs what decision/artifact, in which workflow, for whom, at what consequence and acceptance boundary.
2. **Projection ledger:** what was scoped out, anonymized, made self-contained, frozen, substituted, clarified, or deliberately left implicit.
3. **Measurement ledger:** which requirement became which criterion/check, what evidence the grader can see, what alternatives are accepted, and how weights/thresholds were calibrated.
4. **Evolution ledger:** what changed after agent trials or business updates, who authorized it, whether historical scores remain comparable, and whether the change was task repair, standard drift, or outcome-conditioned hardening.

“Production-grounded” names only the first ledger. A trustworthy benchmark claim requires evidence across all four. This is nonduplicate with EnterpriseClawBench: that work reveals retrospective session projection and hindsight leakage; AlphaEval reveals prospective elicitation, negotiation, and agent-conditioned criterion evolution. Both show lineage is not equivalence.

## Limitations and validity threats

1. Seven purposively selected partners are not a company or occupation population.
2. No partner funnel, task sampling frame, company-by-task allocation, exclusion log, or clustering analysis is given.
3. Source requirements, task deltas, refinement histories, private tasks, outputs, and score tables are unavailable.
4. “Implicit constraints invisible to outsiders” can become unfair hidden obligations unless they are consequences of disclosed context or supplied domain knowledge; production common sense alone is not a public basis.
5. Self-contained sandbox tasks omit clarification, collaboration, proprietary systems, customer feedback, and downstream use.
6. Partner quality-bar changes create instrument drift; no bridge items or version comparability policy is reported.
7. Frontier-agent refinement may improve discrimination while inducing outcome-conditioned selection or grader overfitting.
8. The package matrix is selected and incomplete; same-model comparisons confound scaffold with defaults, version, adapter, and serving path.
9. Only one selected configuration has repeats; its mean ± SD is mislabeled as a 95% CI.
10. Point-level meta-evaluation does not validate rubric completeness, criterion authority, weights, task scores, or domain aggregation.
11. One judge model is also an evaluated model family, raising self-preference and family-dependent error concerns.
12. Equal task/domain means combine heterogeneous scales and policy weights without a common interval interpretation.
13. Resume-shortlist F1 treats one consequential human decision as ground truth and omits alternative acceptable sets, label uncertainty, fairness, and outcome validity.
14. Failure-mode frequencies lack a disclosed coding and reliability protocol.
15. Full trajectories are not necessarily full reasoning; closed CLIs expose different observability, and observable behavior does not make a service reproducible.
16. Default APIs, search indexes, commercial CLIs, model aliases, and judge services are mutable despite pinned CLI versions.
17. Economic hours begin with LLM estimates and heterogeneous expert corrections from 0.33 to 1.54; one finance label appears for multiple correction methods, while expert identities and raw judgments are absent.
18. Wage cost is not customer value, task consequence, realized productivity, or replacement value.
19. Multiplying a fractional rubric score by full human cost assumes linear, fungible partial value and ignores gating failures, review/rework, integration, correlated error, and catastrophic loss.
20. The practitioner survey is 27 accelerator-affiliated respondents, has ambiguous questionnaire numbering (15 items but Q1–Q16), and reports open-text “weights” without the coding method; it is motivation, not population evidence.

## Reproducibility and operational realism

The public repository is useful framework evidence. It pins an MIT-licensed interface, Docker adapters, task package conventions, six grader templates, and five fictional examples. The release can help organizations prototype a local evaluator.

It cannot reproduce the publication. The 94 production tasks and files, exact rubrics/oracles, trajectories, raw scores, package configurations, costs, company/task mapping, expert labels, and meta-evaluation table are absent. The inspected release commit postdates v1. Commercial model endpoints and CLIs remain mutable. Docker invocation is described, but no outer-envelope network/filesystem canary or complete image digest is reported in the paper.

Operational realism is similarly bounded. The tasks preserve document formats, long artifacts, domain cues, and stakeholder-shaped criteria. But “production” here means production-sourced requirements projected into isolated benchmark episodes—not operation inside production systems with actual users, permissions, incidents, latency, compliance, rework, and consequences.

## Comparison with adjacent evidence

- **EnterpriseClawBench** retrospectively projects real sessions and publicly exposes projection/hindsight defects; AlphaEval prospectively elicits and negotiates tasks but releases no source-to-task traces. One strengthens inspectability, the other partner interaction; neither proves equivalence.
- **GDPval** starts with an explicit sector/occupation frame and experienced task authors but weak within-occupation sampling. AlphaEval starts with seven companies and labels tasks after acquisition. AlphaEval has stronger current-demand provenance; GDPval has a clearer breadth frame and more auditable public metadata. Neither supports occupational capability or economic replacement claims.
- **ALE/industrial expertise codification** emphasizes structured expert knowledge and source authority; AlphaEval demonstrates recurring engagement but does not expose elicitation records or authority boundaries. Weekly meetings are not a reproducible expertise-transfer method without evidence typing and transformation lineage.
- **Anthropic's production evaluation lifecycle** distinguishes capability, regression, and task-health roles over time. AlphaEval reports moving standards but does not version role transitions or separate task repair from quality-bar drift.

## Transfer to skill-bench

### Preserve

1. Start from a real stakeholder decision/work product and observe the surrounding workflow before authoring the prompt.
2. Negotiate a bounded but professionally meaningful unit rather than assuming the initial request is the construct.
3. Use a common task package with domain-specific grader composition.
4. Treat configured model, scaffold, tools, environment, defaults, and feedback policy as the evaluated object.
5. Revisit criteria as work changes—but preserve immutable versions and bridge evidence.

### Repair

1. Require the four ledgers above and link every transformation to author, rationale, before/after hash, affected claim, and approval scope.
2. For every implicit requirement, record `source_explicit`, `publicly_derivable_consequence`, `supplied_domain_basis`, or `unfair_hidden_obligation`; only the middle two are eligible private checks.
3. Preserve rejected requirements/tasks and exclusion reasons so confidentiality, self-containment, automation, and feasibility do not invisibly narrow the construct.
4. Blind a domain expert to system outcomes for source-to-task equivalence review; separately validate grader observability, alternatives, thresholds, and dependence.
5. Version criteria and report bridge-item comparability when standards change. Never overwrite old scores under a new quality bar.
6. Keep plural score families and gates separate. Do not multiply a generic quality score by labor cost; estimate workflow value only from observed acceptance, correction, completion, consequence, and cost data.
7. Use a full or explicitly estimand-driven package design with repeated task-level trials and company/task-family clustered uncertainty before making scaffold comparisons.
8. Meta-evaluate the end-to-end task decision, not only rubric-point coverage, and report missing/invalid cases, evidence views, rater authority, disagreement, adjudication, and route-specific error.

## Concrete repository changes

No new queue task is added. The findings refine existing expertise-transfer, participation, validity-argument, task-health, metric-monitoring, projection, and execution-isolation machinery. At next consolidation:

- add a `production_requirement_projection` example that binds demand, projection, measurement, and evolution ledgers;
- add a planted failure where a partner's tacit preference becomes an unfair private criterion unless its public basis is documented;
- reject a `production_readiness` or `labor_value_delivered` claim supported only by source provenance plus `score × wage_cost`;
- require criterion-version bridge evidence when agent-conditioned refinement changes the quality bar.

## Bottom line

AlphaEval offers a valuable prospective construction pattern: sustained company engagement, workflow discovery, scope negotiation, co-constructed references, heterogeneous artifacts, plural graders, and configured-system evaluation. But the strongest benchmark-design lesson is the boundary it does not validate. The private transformation history prevents audit of whether authentic needs survived formalization; point-level judge agreement does not validate task scores; three winner-only runs do not establish ranking stability; and rubric score multiplied by estimated labor cost is not delivered economic value. For `skill-bench`, production provenance should initiate a transformation-validity argument—not conclude one.

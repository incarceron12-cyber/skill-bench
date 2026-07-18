# OpenAI/Thrive Tax AI: a strong correction-to-eval design pattern does not identify autonomous self-improvement

## Source and review status

**Deep review of the complete preserved official primary source.** I read the complete OpenAI/Thrive article body, including all nine substantive sections and the 36-line task-environment tree, and checked its preserved provenance and content hash. The source is an official production engineering case, not a peer-reviewed study. No code, source packages, traces, correction rows, grouped findings, eval datasets, graders, pull requests, trial records, filed-return labels, metric tables, privacy assessment, or deployment logs are linked or released.

- **Source:** Aravind Srinivasan, Samay Shamdasani, Arthur Fernandes Araujo, and John de Wasseige, “Building self-improving tax agents with Codex,” OpenAI with Thrive Holdings, 27 May 2026, <https://openai.com/index/building-self-improving-tax-agents-with-codex/>
- **Complete local text:** `data/sources/openai-building-self-improving-tax-agents-with-codex.md` (17,849 bytes; SHA-256 `d1337d4a8fd105addf05d8a7ae11f1a53a21117d37d3801935d3cba9c93ee6ef`)
- **Provenance:** `data/sources/openai-building-self-improving-tax-agents-with-codex.provenance.json`
- **Retrieved official URL:** <https://openai.com/index/building-self-improving-tax-agents-with-codex/?output=1> (HTTP 200 at acquisition; raw HTML metadata recorded but raw HTML not retained)
- **Evidence boundary:** complete article text and captions were preserved; decorative figure pixels were not. All system outcomes remain company-reported and are not independently replayable.
- **Tags:** production-evaluation, practitioner-corrections, provenance, task-health, scoped-engineering, human-review, longitudinal-validity, self-improvement-claims

## Why this matters for skill-bench

This review advances charter objectives A, B, and D through a bounded production-system case. Tax preparation is not a proposed benchmark vertical. The reusable question is:

> When can a professional correction legitimately become an evaluation case and a scoped system change, and what evidence distinguishes a useful production-learning loop from endpoint trend narration?

The article contributes an unusually legible proposed chain:

```text
source file and client note
→ extracted field and provenance
→ tax-engine submission
→ practitioner review and correction
→ filed-return comparator
→ typed/reviewed difference
→ recurring actionable finding
→ representative targeted eval
→ scoped code, schema, mapper, grader, or Skill change
→ targeted and regression suites
→ candidate pull request
→ engineering and practitioner review
→ deployment
→ new production evidence
```

That chain is worth preserving. Its key discipline is that a raw difference is **not** automatically a model error, an expert label, an eval case, or a valid improvement target. The article explicitly lists extraction misses, mapping issues, unsupported behavior, practitioner preference or tax judgment, prior-year carry-forward, changes elsewhere in the filing workflow, and expected workflow noise as competing explanations. Repeated cases are reviewed and grouped before promotion to a bounded eval; ambiguous or unsafe cases route back to the product team.

The stronger headline—“self-improving tax agents”—is not established by the disclosed evidence. The article gives changing endpoint percentages, selected productivity claims, and one practitioner anecdote without denominators, case-mix adjustment, uncertainty, comparator arms, version manifests, intervention dates, or artifact release. It also states that engineers remain responsible for architecture, product decisions, and shipping. The demonstrated object is therefore a **human-governed, Codex-assisted production engineering loop**, not autonomous agent self-improvement, tax-expertise transfer, or a causal estimate of system learning.

## One-sentence contribution and assessment

**Contribution:** OpenAI and Thrive describe how practitioner corrections, field/provenance traces, recurring-failure review, targeted evals, isolated writable/read-only task environments, regression suites, and human-reviewed pull requests were joined around a deployed tax-extraction product reportedly used on 7,000 returns.

**Assessment:** The workflow is a strong cross-domain design pattern for turning production corrections into bounded engineering evidence, but the article does not release the correction taxonomy, labels, evals, version history, trials, metric populations, uncertainty, or deployment records needed to validate reported accuracy, productivity, causal improvement, expertise transfer, safety/compliance, or autonomous self-improvement.

## Research question and claim boundary

The article asks how production use can create structured evidence that a coding agent can turn into faster product improvements in practitioner-led domains. Its defensible claim boundary is descriptive:

1. the teams report deploying Tax AI across participating firms in a network of more than 30 accounting firms;
2. they report processing 7,000 tax returns during the season;
3. they describe a production trace from source documents through extracted cited fields and tax-engine mapping to practitioner correction and filed return;
4. they describe reviewing and grouping field differences before creating targeted evals;
5. they describe a bounded Codex work environment with read-only production evidence, a writable product surface, targeted and regression suites, Skills/docs, and candidate pull requests; and
6. they explicitly retain engineers and practitioners as decision and shipping authorities.

The article does **not** establish:

- that every reported correction is accurate or expert-authorized ground truth;
- accuracy, precision, recall, or completion rates that can be recomputed from disclosed rows;
- a causal effect of Codex, eval infrastructure, any one code/Skill change, or the full loop;
- a counterfactual improvement over ordinary engineer-led maintenance;
- autonomous self-improvement, because review, task promotion, architecture, and shipping remain human-governed;
- transfer of practitioner tax expertise into an agent rather than repair of extraction/mapping software;
- comparable quality across the changing simple-to-complex return mix;
- practitioner-equivalent tax judgment, filed-return correctness, audit outcomes, or taxpayer benefit;
- privacy, security, legal, tax, or professional-compliance validity;
- productivity or customer-service effects beyond selected self-reports; or
- transport to bookkeeping, audit, IT help desk, other firms, or knowledge work generally.

## Methodology and system reconstruction

### Production unit and bounded automation layer

Practitioners upload source files and client-specific notes. Tax AI organizes, splits, and classifies documents; extracts fields with citations; maps supported values to a tax engine; and produces a submission for practitioner review. The article says automation is limited to extraction and mapping. Engineers retain architecture, product, and shipping decisions; practitioners correct extracted values, review returns, and approve filings.

That scope statement is important. A 1040 or 1041 filing is not one homogeneous inference problem. Document classification, field extraction, provenance attachment, tax-engine mapping, reconciliation, professional judgment, filing approval, and downstream correctness are distinct constructs and authorities. The article mainly describes the first four. Calling the entire product a “tax agent” risks importing a broader tax-preparation claim than the documented automation layer supports.

### The rental-property correction chain

The Schedule E example begins with heterogeneous evidence—handwritten notes, emails, spreadsheets, and other files. Tax AI normalizes those materials into cited fields and maps fields it can confidently support. A difference between the prediction and filed return becomes a field-level review row containing expected value, predicted value, and an “actionable” disposition.

The article then groups similar rows to distinguish recurring product failures from workflow noise. Examples include missed fair-rental-day fields, mishandled “other expenses,” and confusion among multiple properties in one source package. Only reviewed repeated patterns become eval targets. A fair-rental-days finding may lead Codex to inspect:

- source packages and source selection;
- extraction schemas and patterns;
- provenance logic;
- mapper behavior and code paths;
- unsupported fields; and
- the grader itself.

Candidate repairs include extending the schema, improving document selection, changing the mapper, or repairing a grader that mistakes expected workflow noise for failure. The candidate then runs against the targeted eval and a broader rental-income regression suite before a pull request is surfaced for engineering review. Ambiguous or unsafe cases return to the product team.

This is the article's strongest unique contribution: **correction attribution precedes evaluation promotion**. A difference is an investigation trigger, not an oracle. The possible repair surface includes the measurement instrument itself, preventing every mismatch from being forced into an agent-capability narrative.

### Task-environment design

The article gives a concrete illustrative directory tree for `FIND-RENTAL-0042`:

- a writable branch with `AGENTS.md`, `task.yaml`, `EXEC_PLAN.md`, and `RESULTS.md`;
- a bounded rental-income product surface (`agent.ts`, `schema.ts`, `provenance.ts`, `mapper.ts`);
- targeted and regression datasets/suites plus a grader;
- reusable eval-runner and tax-field documentation Skills;
- architecture/task-environment documentation; and
- read-only tools for production traces, source artifacts, and tax-engine documentation.

The separation between immutable evidence and editable implementation is sound. It supports reproducible investigation, limits accidental evidence mutation, and makes the candidate change inspectable. But the tree is explicitly representative. No actual task bundle, permissions manifest, filesystem canary, source redaction policy, tool transcript, eval command output, component hash, or reviewed pull request is released. It establishes a design vocabulary, not demonstrated containment or replayability.

### Human roles and authority

The source attributes three functions to practitioners:

1. correct system outputs during normal work;
2. help distinguish actionable product errors from preference, judgment, carry-forward state, and workflow noise; and
3. review and approve final filings.

Those roles should not be collapsed into one “expert feedback” field. A practitioner action can be operationally authoritative for what was filed while still being ambiguous about why it changed, whether the filed value is substantively correct, whether it reflects firm/client preference, and whether it should generalize into an eval criterion. The article says reviewed findings mediate this transformation, but does not disclose who reviews them, practitioner qualifications, contributor counts, disagreement, sign-off, escalation thresholds, or criterion-level authority.

Similarly, final filing is a stronger comparator than the agent's draft, but it is not automatically an independent correctness oracle. Filed returns can contain later workflow edits, estimates, elections, client-supplied choices, unresolved uncertainty, or error. The article does not report tax-authority outcomes, audit findings, amended returns, second review, cross-practitioner agreement, or downstream error costs.

## Exact reported evidence and what it means

The article reports the following quantities:

| Reported quantity | Exact claim | Evidence limit |
|---|---|---|
| Organizational reach | Crete network of `30+` accounting firms; participating firms used the pilot | Number of participating firms, selection, adoption, and per-firm volume absent |
| Product volume | `7,000` returns processed during the tax season | Eligible/submitted/completed/reviewed/filed denominator and failures absent |
| Time horizon | collaboration over `six months`; first deployment `three months` earlier; 75%-completion shift “within six weeks” | Exact dates, releases, intervention chronology, and comparable windows absent |
| Preparation time | saves practitioners “about a third” of tax-preparation time | Sampling, baseline, timing method, distribution, review/rework, and uncertainty absent |
| Draft accuracy | “up to `97%` accuracy” | Unit, population, threshold, estimator, time point, missingness, and uncertainty absent |
| Throughput | increases throughput “about `50%`” | Numerator/denominator, capacity definition, demand/case-mix, staffing, and comparator absent |
| Completion threshold | at launch `25%` of returns reached `75%` correct field completion; within six weeks `86%` did | Return counts, scored-return policy, field applicability/weighting, corrections, and intervals absent |
| Higher thresholds | “even faster growth” at `90%` and `100%` correct field completion | Start/end values and denominators absent |
| Rental support | about `six weeks` and substantial engineering oversight to reach `90% precision and recall` | Dataset, positive class, averaging, confidence intervals, and production-vs-eval status absent |
| Individual anecdote | one senior accountant's tax-prep time changed from `180` hours last year to `15` this year | One selected person; task volume/mix, staffing, definition, attribution, and records absent |

Several metrics cannot be reconciled from the article. “Up to 97% accuracy,” shares of returns crossing 75/90/100% correct-field-completion thresholds, and “90% precision and recall” for rental properties are different estimands. The article provides no mapping among them. Field completion may weight common and rare fields equally or not; return-level thresholding hides error severity and field applicability; precision/recall requires a defined positive unit; and “up to” can select a favorable slice or time point. None directly establishes correct tax liability, professional acceptance, filing correctness, or absence of consequential errors.

### Changing case mix is not a harmless detail

The source says early Tax AI handled simpler W-2 and 1099 work, then expanded to K-1s, schedules, rental real estate, reconciliation across files, and harder edge cases. It also says the share of scored returns reaching completion thresholds continued to rise as complexity increased.

That trend is encouraging operationally but unidentified scientifically. At least five things move together:

1. system versions and product support;
2. return and field complexity;
3. which cases enter the scored population;
4. practitioner/site adoption and workflow; and
5. calendar-season composition and accumulated engineering attention.

Without a frozen equivalent-form panel, contemporaneous controls, return/field difficulty strata, component hashes, or adjustment for firm/practitioner/time, rising endpoint percentages cannot isolate system improvement. Expansion can make the task harder, while selective scoring, newly supported fields, changes in missing-field handling, or altered completion definitions can make the metric easier. Conversely, stable aggregate accuracy could conceal genuine progress under harder case mix. The correct conclusion is not that the trend is meaningless; it is that its estimand is unspecified.

### Missing comparison and uncertainty

No baseline arm is reported for:

- the initially deployed product without the Codex loop;
- engineer-led correction handling with the same traces/evals;
- Codex with traces but no practitioner grouping;
- scoped code changes without reusable Skills;
- alternative coding agents or human engineers; or
- matched returns under old and new versions.

No sample sizes accompany the threshold percentages. There are no intervals, repeats, preregistered thresholds, stratified results, field-level confusion matrices, missing/invalid records, firm/practitioner clusters, or adverse-event counts. “Measurably better” therefore means the company measured changing internal endpoints, not that the article supplies a valid causal or uncertainty-bearing estimate.

## Evidence interpretation

### What the full source genuinely supports

1. **A raw professional correction needs attribution before promotion.** The article explicitly preserves multiple alternative causes and reviews recurring differences before creating evals.
2. **Product traces can join source evidence to downstream state.** Field citations and intermediate mappings are more diagnostic than comparing only a final draft and filed return.
3. **Evaluation should create a bounded engineering target.** A targeted set and regression suite give the coding agent an explicit hill to climb rather than a vague production complaint.
4. **The grader is part of the repair surface.** Expected workflow noise may indicate evaluator error rather than product failure.
5. **Immutable evidence should be separated from writable implementation.** The representative task environment makes this architectural control concrete.
6. **Human authority remains in the loop.** Ambiguous cases, architecture, product decisions, pull-request review, shipping, return review, and filing approval are not delegated wholesale.
7. **Reusable abstractions may lower later support cost.** The source reports that rental-property work produced abstractions and conventions later used for Schedules C and A, although no comparative effort data test the claim.

### What the source only suggests

- that practitioner-in-workflow correction can be a low-friction expertise channel;
- that repeated correction clustering may prioritize valuable failures;
- that Codex may accelerate investigation and implementation;
- that source/provenance traces may improve root-cause localization; and
- that bounded eval-backed maintenance may outperform unstructured post-launch debugging.

These are plausible production hypotheses requiring exact logs, comparator designs, burden measures, and untouched confirmation.

### What is unsupported

- autonomous or general self-improvement;
- causal improvement due to Codex or the three-part loop;
- transfer of tacit tax expertise;
- professional tax capability or expert equivalence;
- correctness of filed returns or tax outcomes;
- productivity, throughput, or client-value effects at a defined population level;
- safe, private, compliant use of sensitive tax records;
- reproducibility, reliability, cost-effectiveness, or transport across domains; and
- readiness for unreviewed tax preparation or broader knowledge work.

## Unique insight for skill-bench

> **A correction is neither a label nor a lesson. It is a state transition whose promotion requires typed attribution, authority, recurrence, representativeness, and independent confirmation.**

The reusable promotion ladder is:

```text
observed pre/post field or artifact difference
→ exact source, actor, time, workflow state, and provenance
→ candidate cause set
→ practitioner explanation and authority scope
→ reviewed disposition: product defect / unsupported behavior / judgment or preference /
  external workflow change / grader defect / expected noise / unresolved
→ recurrence and affected-population estimate
→ bounded finding with explicit success condition
→ candidate eval rows separated from untouched confirmation rows
→ scoped intervention with exact component delta
→ targeted, regression, safety, privacy, and alternative-path checks
→ human shipping decision
→ prospective production measurement under a frozen metric and case-mix policy
→ retained, rolled back, narrowed, or superseded lesson
```

This ladder repairs two common shortcuts. First, mining every human edit into “expert ground truth” launders workflow state, preference, and downstream edits into model error. Second, improving on evals created from those same edits can be resubstitution: the loop may become better at its selected correction families without improving untouched work.

A second insight is that **production learning has two coupled but separable loops**:

1. **instrument loop:** difference review, taxonomy, criterion/grader repair, eval-set assembly, task-health, and metric versioning;
2. **product loop:** code/schema/mapper/Skill change, regression testing, deployment, and observed consequence.

If grader changes and product changes occur together, endpoint gains cannot identify which loop moved. Old/new product × old/new grader cross-scoring plus a frozen external audit is needed. This directly echoes the controlled evaluator-collapse lesson in *Who Grades the Grader?*: better endpoint scores cannot validate the evolving observer, while a permissive observer can conceal regressions.

## Comparison with adjacent evidence

- **AlphaEval:** both sources begin with current company work and repeated domain-partner involvement. AlphaEval focuses on projecting private requirements into isolated task packages; Tax AI focuses on turning in-workflow corrections into product findings and engineering evals. Tax AI adds a useful correction-attribution step, but releases even less task/evaluator evidence. Neither production origin validates transformation, criterion authority, occupational scope, or value.
- **Nubank production evaluation:** Nubank reaches an online outcome layer with selected tNPS/SSR point estimates but lacks prospective predictions, assignment details, denominators, uncertainty, and treatment isolation. Tax AI supplies richer source→field→correction→eval narrative, but its accuracy and productivity endpoints are still less inspectable. Both require candidate genealogy, frozen metric funnels, case-mix identity, and prospective exposure records.
- **Criterion validity against business outcomes:** that paper shows why a score–outcome association is not judge accuracy, prediction, intervention benefit, or legitimate value. Tax AI reports throughput, time, and completion trends without even a disclosed association design. Filed-return agreement, practitioner time, client contact, and business expansion must remain separate outcomes with independent observers and timing.
- **ACE:** ACE formalizes local context deltas and shows why update semantics matter. Tax AI supplies a more realistic human-governed production source for candidate lessons, but does not expose immutable lesson lineage, contradiction/supersession, held-out promotion, or rollback. “Recurring correction” should enter the same candidate→validation→promotion lifecycle rather than directly changing Skills.
- **GrowLoop:** GrowLoop makes rubric and case co-evolution explicit and warns that adaptive admission can preserve discrimination while changing the construct. Tax AI similarly evolves findings, evals, graders, product scope, and case mix. Without frozen anchors and bridge evidence, rising completion rates can reflect instrument/product co-evolution rather than comparable capability gain.
- **Who Grades the Grader?:** Tax AI commendably includes grader repair among possible fixes, but that creates an intervention–instrument identification problem. A targeted eval should not both drive and prove its own repair. Preserve old/new cross-grades and reserve an untouched confirmation form.

## Transfer to skill-bench

### Retain

1. Capture source→extraction/provenance→intermediate mapping→artifact/state→human correction rather than only final outputs.
2. Treat observed differences as candidate review rows with multiple typed explanations.
3. Require recurrence and human-reviewed actionability before promoting a production difference into an eval target.
4. Make source selection, schema, mapping, implementation, and grader separate root-cause surfaces.
5. Keep source evidence and production traces read-only while interventions occur in a scoped writable environment.
6. Pair targeted checks with broader regression suites and explicit human shipping decisions.
7. Route ambiguous, unsafe, or judgment-dependent cases to named authorities rather than forcing automation.

### Repair

1. **Define denominator states.** Record eligible, uploaded, parsed, supported, scored, submitted, corrected, approved, filed, amended, invalid, and excluded returns/fields separately.
2. **Type correction authority.** Preserve actor role, qualification, evidence view, action authority, rationale, confidence, disagreement, and whether a change was operational, epistemic, preferential, or compliance-driven.
3. **Freeze the comparator.** “Filed value” needs timestamp, source of change, review stage, later amendments, and independent correctness status; it is not a universal oracle.
4. **Version every loop component.** Hash task population, source transformation, product, model, prompt, Skill, schema, mapper, grader, metric, support boundary, and feedback policy for every reported cell.
5. **Separate instrument from product changes.** Cross-score old/new outputs under old/new graders and a frozen audit; never overwrite prior scores when expected-noise policy or field support changes.
6. **Reserve untouched confirmation.** Rows that caused a finding may train or validate a repair, not provide final evidence for it. Use equivalent forms, later temporal cohorts, or independent firms/practitioners for confirmation.
7. **Model case mix.** Report return and field complexity strata, firm/practitioner/calendar clusters, support eligibility, and complete missingness before interpreting longitudinal trends.
8. **Measure burden and consequence directly.** Practitioner review/rework time, engineering/Codex resources, false promotions/rejections, escalations, amendments, incidents, client outcomes, and rollback should accompany throughput claims.
9. **Use noncompensatory correctness/safety gates.** High common-field completion must not average away rare consequential tax, privacy, or mapping errors.
10. **Bound claims to the automation layer.** Extraction/mapping agreement is not tax judgment, full-return correctness, professional equivalence, or filing readiness.

## Reproducibility and operational realism

Operational realism is high in several respects: the case involves messy multimodal business documents, prior-year state, source citations, real practitioner correction, a downstream tax engine, changing support boundaries, human filing approval, production traces, regression checks, and organizational deployment. The article also admits workflow noise and ambiguous evidence, which many benchmark reports omit.

Inspectability is weak. The official article is complete and the local source/provenance are durable, but no empirical artifact can reproduce a single metric or correction-to-fix episode. The representative directory tree supplies filenames rather than file contents. Missing artifacts include:

- participating-firm and return cohorts;
- exact support/scoring inclusion policies;
- field schemas and applicability rules;
- source packages or privacy-preserving surrogates;
- field-level expected/predicted/final rows;
- correction rationales and reviewer dispositions;
- clustering method and recurrence thresholds;
- finding/eval promotion records;
- targeted and regression datasets;
- graders and grader-version changes;
- model/Codex/configuration manifests;
- candidate patches and human review outcomes;
- per-version metric rows and uncertainty;
- time/throughput measurement protocols;
- privacy, security, compliance, incident, and audit evidence; and
- rollback or negative-result denominators.

Confidential tax data can legitimately prevent public release. That is an operational constraint, not positive validation evidence. A privacy-preserving release could still expose schemas, synthetic representative rows, hashes, aggregation code, metric definitions, correction-taxonomy codebook, candidate genealogy, task-environment permissions, and redacted trial manifests.

## Limitations and validity threats

1. Official company case study rather than independent or peer-reviewed evaluation.
2. Authors are affiliated with the organizations building and promoting the system.
3. No code, data, traces, evals, graders, patches, outputs, or deployment records are released.
4. Number and selection of participating firms and practitioners are absent.
5. `7,000 processed returns` has no eligible/submitted/scored/reviewed/filed completion funnel.
6. Return-, client-, practitioner-, firm-, and tax-year clustering are unreported.
7. Product versions, model endpoints, prompts, Skills, tools, schemas, mappers, graders, and deployment dates are unpinned.
8. “Up to 97% accuracy” has no unit, population, calculation, time point, or uncertainty.
9. Return-level 75/90/100% field-completion thresholds hide field applicability, prevalence, severity, and correlated errors.
10. Start and six-week denominators for 25%→86% are absent.
11. No exact values are reported for claimed faster growth at 90% and 100% thresholds.
12. Rental-property `90% precision and recall` lacks positive-class, averaging, dataset, split, and uncertainty definitions.
13. The relationship among accuracy, completion thresholds, and precision/recall is unspecified.
14. Product scope and return complexity change over the same period as reported performance.
15. Scored-population eligibility and missing/unsupported field policy may change over time.
16. No frozen bridge panel or equivalent-form comparison establishes longitudinal comparability.
17. No control or counterfactual separates Codex, traces, evals, practitioner review, conventional engineering, or season effects.
18. No component ablation identifies code, schema, source selection, mapper, grader, or Skill effects.
19. Targeted eval rows may be selected from the same correction families that caused the change.
20. No untouched confirmation or cumulative eval-access record is disclosed.
21. Practitioner edits are operational actions, not automatically independently correct labels.
22. Filed returns may include judgment, preference, downstream changes, estimates, or errors.
23. No correction taxonomy, reviewer codebook, agreement, adjudication, or authority record is released.
24. Grouping/clustering method, thresholds, false merges/splits, and prevalence denominators are absent.
25. Recurrence can prioritize common low-severity issues over rare consequential failures.
26. Grader repair and product repair are both allowed, confounding improvement unless independently cross-evaluated.
27. “About a third” time savings lacks sample, baseline, observation method, review burden, and uncertainty.
28. “About 50%” throughput gain lacks definition, capacity denominator, staffing, demand, and comparator.
29. The 180→15 hour anecdote is one selected individual with no workload or measurement equivalence.
30. More client calls and new offerings are reported narrative consequences, not measured client benefit or realized value.
31. No tokens, dollars, engineer hours, practitioner-review hours, latency, candidate throughput, or time-to-safe-fix comparison is reported.
32. No false-promotion, false-rejection, regression, incident, amendment, audit, or rollback rates are reported.
33. The task-environment tree is representative, not an inspected release or verified isolation test.
34. Read-only labels do not establish privacy-preserving access, least privilege, retention, deletion, or purpose limitation.
35. No consent, data-rights, security, legal, tax-compliance, bias, or affected-client governance evidence is disclosed.
36. Human review is named but reviewer authority, evidence view, acceptance criteria, and disagreement are unspecified.
37. Engineers retain architecture and shipping, contradicting a strong autonomous-self-improvement interpretation.
38. The automated layer is extraction/mapping, not full tax judgment or filing authority.
39. Schedule C/A reuse is asserted without comparative effort, quality, or transport evidence.
40. Extension to bookkeeping, audit, IT help desk, and other industries is a blueprint claim, not evaluated transport.
41. No professional capability, expert equivalence, filed-return correctness, safety, compliance, economic value, or readiness claim is supported.

## Concrete repository implications

No tax-specific schema, pilot, or new queue task is warranted. Existing evidence/provenance, expertise-transfer, task-health, metric-monitoring, configured-system, compounding-lesson, longitudinal, grader, execution-isolation, and validity-argument machinery already contains the needed objects.

At the next consolidation or fixture pass, apply three non-domain-specific checks:

1. **Correction-promotion check:** reject any eval row whose only authority is an unexplained human edit; require typed cause, authority scope, evidence locator, and disposition.
2. **Instrument/product cross-check:** when grader and product can both change, require old/new artifact × old/new grader plus frozen-audit results before assigning improvement.
3. **Longitudinal denominator check:** reject endpoint trends without versioned eligible/scored/observed populations, case-mix strata, metric identity, uncertainty, and untouched confirmation.

Useful completion is achieved if this review prevents “production correction,” “filed value,” “rising completion,” and “self-improving” from being treated as interchangeable evidence states while retaining the source's genuinely strong task-environment and correction-attribution pattern.

## Bottom line

OpenAI and Thrive describe one of the clearest production narratives for turning messy professional-work corrections into scoped engineering tasks: preserve source provenance, compare intermediate and final state, review alternative explanations, group recurring actionable findings, create targeted evals, isolate immutable evidence from writable code, test targeted and regression suites, and keep humans responsible for ambiguity and shipping. `skill-bench` should retain that chain.

The article does not provide the evidence needed for its stronger framing. Changing case mix, product scope, graders, support boundaries, and system versions make the reported longitudinal percentages noncomparable without bridge controls; no denominator or uncertainty permits recomputation; and no comparison identifies Codex or the loop as the cause. The warranted conclusion is **human-governed, trace- and eval-assisted production maintenance with a promising correction-promotion architecture**—not autonomous self-improvement, tax-expertise transfer, professional equivalence, verified productivity, or general cross-domain readiness.

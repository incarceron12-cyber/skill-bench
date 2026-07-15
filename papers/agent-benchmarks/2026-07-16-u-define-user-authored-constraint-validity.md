# U-Define: user-authored constraints expose the right authority boundary, but the formal guarantee ends at an unvalidated translation

## Source and review status

**Deep paper and supplemental-artifact review.** I read the complete immutable arXiv v1 PDF/text, all four paper-linked supplemental documents, and the retained 104-file source archive. I did not execute the software or expose/use its secret-bearing `.env`.

- Paper: Christine P Lee et al., *U-Define: Designing User Workflows for Hard and Soft Constraints in LLM-Based Planning*, arXiv:2605.02765v1, <https://arxiv.org/abs/2605.02765v1>
- Local PDF: `data/papers/pdfs/2605.02765v1-u-define.pdf` (32 pages; SHA-256 `ad63beded2aada0edf976dd9b6d85d6792b4f982d0e5366d253457e8269aa8e4`)
- Local text: `data/papers/text/2605.02765v1-u-define.txt` (SHA-256 `10b1e0e0f6635b1b6ccc39ed5c3973cdd69d26850a4e39e3d7c4fa53109fc65f`)
- Supplemental provenance: `data/sources/releases/2605.02765v1-udefine/provenance.json`
- Supplemental evidence: `LTL-Translation-Performance.{pdf,txt}`, `PRISM-Plan-Conversion-Performance.{pdf,txt}`, and both user-study protocol/interview guides under `data/sources/releases/2605.02765v1-udefine/`
- Source archive: `data/sources/releases/2605.02765v1-udefine/VibeSync-Source-Code.zip` (SHA-256 `84f4061e016f19a619daa7c9505e961ba1c7b30d55f7fe40dbecdfffb09f807f`; retained locally and ignored)
- Date read: 2026-07-16

The paper-linked OSF node is private/view-only, mutable, unregistered, and unlicensed. Its reported last modification predates arXiv v1 by about 140 days, but it has no commit identity. The archive and internal project are named **VibeSync**, not U-Define. Release observations below are therefore evidence about the paper-linked artifact currently exposed through OSF, not proof of the exact study implementation.

## Bottom line

U-Define contributes a valuable interaction hypothesis for expertise-to-benchmark transfer: let the person who owns the requirement declare whether it is non-negotiable or preferential, show the interpreted check back to that person, and return criterion-specific violations rather than one opaque quality score. Its studies also surface an important negative result: experts could not reliably externalize all tacit rules, frequently needed numeric, cardinality, duration, calendar, and contextual predicates outside the system's LTL treatment, and simplified their work when context-entry burden became high.

The evidence does **not** establish that U-Define gives reliable formal guarantees, improves objective plan quality, or transports to professional planning. The formal checker operates only after two LLM translations—user text to LTL/labels and plan text to a PRISM state model. The 36-rule component study measures string similarity to one author-produced translation, not semantic equivalence or end-to-end violation detection. The paper-linked code goes further: free-text hard rules displayed by the front end are discarded before the backend; missing labels silently pass; some prompt examples invert required predicates; and temporal rules are compiled into state labels that erase the very ordering semantics they purport to verify. A sound model checker cannot recover information lost or reversed upstream.

Study 1 supports a narrower usability/perception claim on 12 university-recruited participants under a short within-subject interface study. Study 2 supports a formative workflow-fit claim from six experts' one-session interactions. It does not validate the constraints as a complete professional specification, the plans as professionally feasible, or the verifier as correct. The strongest transfer to `skill-bench` is therefore not a binary hard/soft schema. It is a **requirement-authority and compilation ledger** that keeps declaration, interpretation, formalization, observability, check result, consequence, and affected-party acceptance separate.

## One-sentence contribution

U-Define makes requirement force user-authored and returns criterion-specific feedback, but its evidence validates a small formative interface study rather than end-to-end constraint enforcement: the unvalidated LLM compilation chain and paper-linked release can turn missing, inverted, or temporally erased observations into formal-looking passes.

## Why this matters: charter relevance and research question

This review advances charter objectives A, B, C, and F through narrow expansion into user/expert-authored evaluation requirements. Vacation planning is only the prototype case; the general question is:

> Can an affected user or domain expert express a requirement's force and intended meaning through an accessible interface, and can a benchmark preserve that authority through formalization, observation, grading, and revision without laundering translator output into a guarantee?

The paper asks three questions: how users express different strictness levels, how they interact with distinct verification mechanisms, and how the constraint types affect output quality and experience (pp. 3–4). Its administered evidence answers a narrower question: how 12 general participants perceive four feature conditions and how six professionals perceive one prototype session, while author-scored translation similarity characterizes two internal components.

## Methodology and system

### The three-stage workflow

U-Define structures planning into (pp. 7–12):

1. **Definition:** the user writes natural-language constraints and classifies each as hard or soft. Hard rules are translated by a fine-tuned model into LTL, then by a prompted GPT-4 agent into PRISM labels; a natural-language back-translation is shown for acceptance or deletion/re-entry.
2. **Verification:** GPT-4 generates three plans. Another GPT-4 agent translates each plan into a PRISM model. PRISM/Storm checks hard-rule labels; an LLM judge gives soft preferences a one-to-five-star score and explanation. Plans are ordered only by hard-violation count.
3. **Feedback:** the user selects a plan, edits constraints or supplies feedback, and the system regenerates and rechecks it.

This is a useful separation of **issuer-declared force** from **evaluation mechanism**. It also contains at least five distinct fallible transformations:

`user intent → wording → hard/soft type → LTL/predicate vocabulary → PRISM plan abstraction → checker result`

Soft requirements follow a different chain:

`user intent → wording → judge prompt → star/explanation → user interpretation`

The paper often describes model checking as enforcement or a guarantee (for example pp. 2, 6, 26–27), but the checker proves only properties of the generated formal model. End-to-end validity additionally requires faithful type assignment, rule translation, plan abstraction, property encoding, and result presentation.

### Implementation identity

The manuscript reports GPT-4 for all agents except a fine-tuned LLaMA 7B translator trained on 240,000 NL-to-LTL examples with an 80/20 split, QLoRA, early stopping after about 1,500 steps/0.13 epochs, and loss near 0.75 (p. 12). Exact GPT-4 snapshot, Azure endpoint, prompts/hashes, run dates, seeds, retry policy, and costs are not reported.

The OSF artifact instead references a `llama-3-8b-Instruct` adapter and a hard-coded Hugging Face endpoint in `backend/baseline.py`; it configures `GPT4_TURBO` through Langroid. This may be a later or earlier implementation. Without a commit or manuscript-time hash, it cannot resolve the paper's model identity.

## Evidence

### Component evaluation

The authors compare generated translations with first-author references reviewed for coherence by a senior author (pp. 12–14). They correctly state that these are human-likeness references, not ground-truth correctness.

- **NL→LTL:** 36 participant-authored hard rules, 12 sampled from each everyday scenario. Mean normalized Levenshtein similarity is 83.12%. The paper reports 13 predicate-token mismatches, four unnecessary predicate expansions, four missing logical operators, and no temporal-operator errors. It proposes an adjusted 94.32% after assuming token mismatches are readily fixable.
- **Plan→PRISM:** three plans—one participant's plan per scenario—with 21, 18, and 16 steps. Mean string similarity is 97.4%; the authors identify three predicate errors.

A direct audit of the released 36-row LTL table reproduces the reported mean (83.116%). Fifteen of 36 rows are exact 100% string matches, 13 are below 80%, the median is 90.885%, and the minimum is 32.65%. This distribution matters more than the optimistic adjusted mean: a “hard” guarantee fails at the tail, and the low-scoring rows include changed antecedents, dropped conjunctions, and altered predicates—not only cosmetic token variation.

The evaluation unit is also misaligned with the claim:

- Levenshtein similarity does not test logical equivalence, satisfiability, vacuity, or counterexample preservation.
- One author interpretation cannot establish user-intent fidelity; back-translation acceptance is not evaluated against independently elicited intent.
- The 36 rules are sampled from the same study that used the system, not an independent held-out domain/specification set.
- Plan conversion uses only three plans/55 steps, apparently one plan per scenario and no repeated stochastic generations.
- The PRISM-label conversion step is explicitly excluded as “purely syntactic” (p. 12), despite release evidence that it changes semantics.
- No end-to-end planted-violation matrix estimates false passes, false failures, missed labels, or explanation correctness.

### Study 1: everyday users

Twelve US, English-speaking adults recruited from university mailing lists (ages 19–42) each receive one of three scenarios and use four conditions in randomized order (pp. 14–19): full hard+soft, soft only, hard only, and no typed constraints. Sessions last about 1.5 hours at $15/hour. Outcomes are perceived performance (FATE), usefulness and satisfaction (USE), SUS-derived usability, constraint-fixing iterations, and thematic interviews.

Reported Dunnett contrasts against the full condition find (pp. 15–19):

- full > none on perceived performance (`p=.0037`), usefulness (`p=.0003`), satisfaction (`p=.0052`), with fewer fixing iterations (`p<.0001`);
- full > hard-only on usefulness (`p=.0074`) and satisfaction (`p=.0413`), but with more iterations (`p=.0008`);
- no significant full-versus-soft-only differences on the four subjective scales; full uses fewer fixing iterations (`p=.0176`).

The qualitative evidence is more informative than the p-values. Nine participants started with hard constraints; five promoted unsatisfied soft preferences to hard. Hard checks increased expectations, and one missed violation was treated as a “deal breaker.” Soft scores were often considered verbose, opinion-like, inconsistent with hard violations, and irrelevant to plan choice. Model checking took roughly three minutes, suppressing exploration.

Claim limits are substantial:

1. `n=12` is small, convenience-recruited, and each person sees all feature conditions in one session, creating learning, fatigue, carryover, and demand effects.
2. The paper says order is randomized; the supplemental protocol specifies four cyclic orders rather than a fully described randomization.
3. Dunnett's ordinary multiple-comparison procedure does not by itself model repeated measures. The paper reports no participant random effect, paired effect sizes, confidence intervals, order/scenario interactions, assumption checks, or raw data.
4. The conditions remove both an input representation and its associated generation/verification/feedback machinery. The study cannot isolate whether benefits come from typing constraints, adding information, formal checks, violation explanations, extra interface structure, or users learning the scenario.
5. “Performance” is a perception scale, not independently scored plan quality. Constraint-fixing iterations are ambiguous: fewer may mean efficiency, premature stopping, latency-induced disengagement, or lower exploration.
6. No evaluator checks whether hard/soft labels match participants' predeclared intent, whether final plans satisfy constraints, or whether user satisfaction persists after real-world execution.

Thus the cleanest result is that this interface/treatment package changed short-session perceptions and interaction behavior relative to no typed constraints. It is not evidence of objective plan improvement or reliable enforcement.

### Study 2: domain experts

Six participants—three higher-education staff plus one grant accountant, one construction superintendent, and one interior designer, with 3–32 years' experience—select a work task and freely use U-Define for about 25 minutes within a one-hour session (pp. 19–23; supplemental protocol). They receive the same subjective scales and a semi-structured interview; there is no control condition, expert gold plan, external feasibility review, repeated task, or real downstream use.

The study's strongest observations are negative:

- experts relied primarily on hard constraints covering regulations, budgets, deadlines, procedures, and resources;
- required predicates exceeded the LTL treatment: numeric limits, cardinality, categorical inclusion, durations, calendars, and domain context;
- verification failed more often than in Study 1;
- all six struggled to recall and enter extensive hard-rule sets and tacit conventions;
- four simplified their task because of missing context and study time;
- domain terms were misread, including a nine-month academic year as 12 months and a one-day toilet installation as one week;
- experts wanted reusable templates/protocols, prior-plan memory, and spreadsheet/tool import.

Five participants found the system useful and all six imagined an assistive workflow, but those are perceptions after a guided prototype encounter. Expert participation here supports **formative authoring/workflow evidence**: what requirements people tried to express, where the representation failed, and which assistance they wanted. It does not confer domain authority on the generated constraints, approve the plans, validate professional outcomes, or establish adoption economics.

The sample also cannot support cross-profession transport. Half the participants are from one higher-education context; recruitment is through university/snowball channels; one person per remaining occupation cannot characterize a domain. Compensation is $15/hour regardless of expertise. No preparation time, constraint count, correction burden, plan-review time, or professional opportunity cost is reported.

## Paper-linked release audit

The unregistered OSF artifact is unusually revealing, although its uncertain identity requires caution.

### Free-text hard rules are displayed but not checked

`frontend/src/components/PlanningPanel.js` parses predefined `Rule N` items and preserves any trailing free text as a `customRules` object for display (around lines 432–564). It then sends **only** the comma-separated predefined numeric IDs to backend `input3` (around lines 480–485). `backend/baseline.py` resolves those IDs through hard-coded vacation `english_rules` and `ltl_expression` dictionaries (around lines 318–392). The custom hard-rule text never reaches `translate_to_ltl` or the checker.

This directly conflicts with the paper's central system description that users freely input natural-language hard constraints which are automatically translated (pp. 3, 7–10). It may reflect a stale prototype rather than study code, but the supplied source cannot reproduce the claimed workflow or the expert tasks.

### Missing observations pass silently

`backend/verifier.py` initializes every `rule_N_result = True` and checks a rule only if its number is selected **and** its label exists (lines 11–95). A selected rule whose translator omits or mislabels the label therefore remains true. `determine_violated_properties` reports “no broken rules” whenever it sees no explicit `False` string (`baseline.py`, around lines 288–316). Translation failure and absence are consequently turned into success rather than `invalid_artifact` or `insufficient_evidence`.

### The PRISM prompt contains inverted and lossy rules

`backend/prompts/translator_prompt.txt` instructs the model to remove `F`, `G`, implication, and negation operators and map temporal formulas to instantaneous Boolean labels. Its required output sets `wear_floatation=false` for the rule requiring flotation devices and `bob_souvenir=false` for the souvenir rule (lines 44–65). It also reduces “visit at least one cafe each day” to `restaurant_cafe=true`, losing day scope and recurrence.

This is not a purely syntactic conversion. It changes truth conditions and erases temporal semantics. In general, a state label such as `(activity & prerequisite) | !activity`, checked globally, can require co-occurrence but cannot prove that the prerequisite happened **before** the activity unless the plan model faithfully preserves event order and distinct states.

### The plan abstraction does not preserve a single ordered plan

The supplement's human reference plans use an explicit `step` counter. The LLM-generated PRISM examples replace it with Boolean guards and persistent Boolean updates. In the recipe example, after the initial `!planning` transition, the next expected action is guarded by `chopping_cutting` even though that variable is still false, permitting deadlock rather than the stated sequence. In the vacation example, multiple state-dependent commands can be enabled and prior booleans persist, so the transition system is not plainly equivalent to the displayed itinerary.

The reported 97.4% string similarity therefore does not establish trajectory equivalence. More importantly, a translation that omits a violating event or co-asserts an activity and prerequisite can make a broken natural-language plan pass the formal model. Model-checker soundness is conditional on abstraction soundness.

### Soft scoring is history- and order-contaminated

The soft-judge prompt tells the evaluator to avoid identical ratings for consecutive plans, which makes a plan's score depend on presentation order rather than only its adherence (`backend/prompts/preference_analyzer_prompt.txt `, line 7). The same prompt file contains more than a thousand lines of accumulated graded examples, and `baseline.py` appends fresh analyses back into it (around lines 194–264). This creates mutable evaluator state and likely cross-run contamination. The prompt's examples also infer unmentioned compliance (“the use of an SUV can be inferred”), exactly the kind of unsupported assumption participants criticized.

No paper experiment calibrates star ratings against independent preference labels, repeats judge calls, tests order effects, records disagreement, or separates hard violations from soft quality. The release reinforces the paper's own conclusion that generic scalar soft judgments should not be trusted as final decision support (pp. 24–25).

### Security and reproducibility

The source archive includes a non-empty secret-bearing `.env`, a hard-coded Hugging Face endpoint/token-shaped value, generated logs/outputs, IDE files, and cache files; it has no license, lockfile, commit, CI, or reproducible run manifest. The local acquisition process did not use or propagate those values. Exact reproduction would additionally require retired/mutable model endpoints, the fine-tuned adapter, Azure credentials, PRISM/Storm dependencies, and manuscript-time prompts/data. Executing this artifact would produce a new run with unclear identity and potential credential risk, not reproduce the study.

## Unique insight: requirement force is not checker type

U-Define's best move is to let the affected person declare a requirement's **force**. Its central conceptual mistake is to couple that declaration directly to a checker technology:

`hard → LTL/model checking`<br>
`soft → LLM star rating`

These are different axes. A requirement can be:

- non-negotiable but currently unobservable;
- non-negotiable and arithmetic rather than temporal;
- conditional on jurisdiction, role, date, or source authority;
- preferential but deterministically measurable;
- preferential with a threshold, lexicographic priority, or acceptable range;
- uncertain and requiring clarification rather than either enforcement mode.

The correct chain for `skill-bench` is:

```text
issuer and affected party
→ raw statement and context
→ declared force / negotiability
→ authority, applicability, and valid time
→ interpretation and type assignment
→ observable state and admissible evidence
→ selected checker family and coverage claim
→ compiled check and transformation lineage
→ conformance/counterexample tests
→ trial observation and insufficiency state
→ consequence, repair, and issuer review
→ bounded benchmark claim
```

A hard declaration should raise the evidence bar, not manufacture certainty. If translation coverage is partial, the result must be “unverified portion” rather than pass. If the checker cannot represent the predicate, the benchmark should preserve it as a human gate, another deterministic check type, or an unresolved authoring item—not demote it silently or force it into LTL.

A second insight is that **constraint elicitation is an intervention and a burden**. Experts' inability to recall autopilot rules is not evidence that those rules do not exist. Conversely, a prompted list is not automatically complete or authoritative. A benchmark should compare at least direct free recall, critical-incident probing, source/tool import, draft-and-correct assistance, and observed-work reconstruction, measuring omissions, corrections, time, fatigue, and downstream check validity.

## Comparison with adjacent reviewed evidence

- **UnderSpecBench** (`papers/agent-benchmarks/2026-07-13-underspecbench-action-boundary-validity.md`) separates private intended action from what the public request authorizes. U-Define gives the issuer more explicit control, but its translation pipeline can change what was authorized. Together they require raw statement, public basis, interpretation, and legitimate action/check set to remain separate.
- **MapSatisfyBench** (`papers/agent-benchmarks/2026-07-15-mapsatisfybench-behavior-grounded-hidden-requirements.md`) uses behavior to nominate implicit factors but lacks current authority and affected-user validation. U-Define supplies direct declaration authority, yet direct declaration still does not prove completeness, stable applicability, or faithful compilation. Behavior-derived and user-authored requirements should therefore use different authority statuses, not one “hidden requirement” bucket.
- **ResearchRubrics** (`papers/agent-benchmarks/2026-07-10-researchrubrics-expert-rubric-authoring.md`) turns expert attention into many criteria through author/reviewer/final-review roles. U-Define uses the affected user as issuer but offers no independent criterion review or aggregation calibration. Both show that “expert/user written” records origin, not terminal validity; transformation and observability need separate review.
- **JADE** (`papers/agent-benchmarks/2026-07-11-jade-dynamic-professional-grading.md`) separates fixed obligations from response-created claims and shows why unsupported evidence must fail closed. U-Define's missing-label pass and soft-judge order dependence are concrete instances of the same evaluator-admissibility problem.
- **Existing participation and expertise-transfer contracts** already distinguish bounded contributor authority, transformation lineage, source claims, primitives, checks, and release gates. U-Define sharpens their use: requirement-force declaration and checker-compilation coverage should be recorded as separate stages, but no vacation-specific schema is warranted.

## Limitations and validity threats

1. Only 18 participants total; convenience/snowball recruitment and substantial university concentration limit transport.
2. Study 1 has 12 participants, three scenarios, and repeated conditions, with no raw data, effect sizes, intervals, mixed/repeated-measures model, or order/scenario interaction analysis.
3. Cyclic condition orders in the supplement are less fully randomized than the manuscript wording implies.
4. Conditions bundle representation, generation prompting, checker, explanation, latency, and feedback affordances.
5. Main outcomes are perceived performance/usefulness/satisfaction/usability, not independently judged plan quality or real task outcomes.
6. Iteration count has no validated direction: fewer iterations may reflect efficiency, latency, frustration, or premature stopping.
7. The expert study has no comparator, repeated tasks, baseline artifact, expert solve, external review, or downstream execution.
8. Three of six experts are from higher education; one person represents each other occupation.
9. Experts simplified tasks because of time/context burden, changing the construct under observation.
10. Expert participation validates workflow perceptions and exposes missing constraint types; it does not validate professional plan feasibility.
11. Hard/soft type fidelity is not compared with predeclared intent, independent raters, or later affected-party decisions.
12. Binary force is too coarse for priorities, conditional requirements, trade-offs, uncertain/stale rules, and multi-party conflicts.
13. The 36-rule component sample is small, study-derived, and evaluated against one author interpretation.
14. Levenshtein similarity is not semantic equivalence and can reward logically wrong formulas with similar strings.
15. The proposed 94.32% adjusted LTL score assumes predicate repair rather than measuring it.
16. The PRISM plan study uses only three plans/55 steps and no repeated translation reliability.
17. The excluded LTL→PRISM step is semantically material in the released prompt.
18. No end-to-end false-pass/false-fail or planted counterexample evaluation exists.
19. No checker coverage indicator was implemented or tested despite being proposed in discussion.
20. The formal model is generated from the plan under test, so omitted/misclassified events can disappear from the observer view.
21. Model checking proves the generated abstraction, not natural-language plan adherence or real-world feasibility.
22. The soft judge lacks independent human calibration, repeatability, order-invariance, criterion-level outputs, and insufficiency states.
23. The same GPT-4 family appears across planning, translation, judging, and repair, creating shared-blind-spot and self-preference risks.
24. Exact GPT-4 snapshot, fine-tuned checkpoint identity, prompts, seeds, run dates, retries, invalids, token usage, latency distribution, and API cost are absent.
25. Three-minute hard-check latency is observed but no system cost/performance analysis is reported.
26. The paper-linked OSF node is mutable, unregistered, unlicensed, and has no commit identity.
27. The VibeSync source identity does not match the manuscript name and cannot be tied exactly to the studies.
28. The released front end drops free-text hard rules before backend verification.
29. Missing labels default to pass; translation failure is not represented as invalid or insufficient evidence.
30. Released prompt examples invert at least two predicates and erase temporal operators.
31. Generated PRISM examples do not establish ordered-plan equivalence and can deadlock or admit unintended transitions.
32. The soft prompt mutates across runs and explicitly induces rating diversity across consecutive plans.
33. Secret-bearing configuration in the archive is a material release-hygiene and safe-reproduction failure.
34. No license permits confident redistribution or reuse of the source archive.
35. The paper's high-stakes/reliability framing exceeds short-session perception and author-similarity evidence.

## Reproducibility and operational realism

**Conceptual reproducibility is moderate; exact and result reproducibility are low.** The paper explains the interaction stages, four everyday conditions, participant protocols, scales, contrast test, expert task list, component samples, and major prompts/components. All linked OSF files were acquired and hash-verified, and the tabular LTL mean is independently reproducible.

Exact reproduction is blocked by mutable/unregistered source identity, missing raw study data, missing analysis code, unpinned GPT-4/Azure services, checkpoint/endpoint drift, no environment lock, absent run manifests, and unsafe secret-bearing configuration. The code artifact cannot reproduce central paper claims because its backend accepts only predefined vacation hard-rule IDs and contains fail-open/semantically inverted checker paths.

Operational realism is mixed. Letting workers bring their own planning task, distinguish requirements from preferences, inspect violations, and iteratively revise is closer to real authoring than a fixed benchmark rubric. The study also authentically exposes context overhead and representation mismatch. But sessions are short, plans are drafts, no source systems are integrated, no multi-stakeholder conflict is modeled, no plan is executed, no real consequence is observed, and no organizational approval/audit process is present. Treat U-Define as a formative **constraint-authoring interface study with a brittle prototype verifier**, not as validated professional planning or formal-assurance infrastructure.

## Transfer to skill-bench

### Retain

1. **Issuer-declared force.** Record who declares a requirement hard, soft, conditional, unresolved, or superseded; affected-party authority must be scoped.
2. **Round-trip review.** Show raw text, interpreted predicate, scope, and back-translation together; preserve acceptance, correction, rejection, and unresolved disagreement.
3. **Criterion-specific feedback.** Return exact failed/unsupported requirements and evidence locators rather than one scalar quality rating.
4. **Editable lifecycle.** Allow requirements to be promoted, relaxed, split, scoped, superseded, or withdrawn with versioned reasons and downstream invalidation.
5. **Authoring burden as evidence.** Measure elicitation time, omission/correction rates, imported versus recalled rules, expert fatigue, and reuse value.

### Repair

1. **Decouple force from checker family.** Select arithmetic, temporal, relational, source-grounded, state-based, model, or human checks from predicate semantics and evidence access—not merely hard versus soft.
2. **Fail closed on compilation/observation gaps.** Missing label, parser failure, untranslatable clause, unpinned transform, or absent evidence must yield `insufficient_evidence`/`invalid_artifact`, never pass.
3. **Preserve a typed compilation chain.** Hash every statement, interpretation, formal artifact, plan abstraction, checker, and result; record coverage and semantic-review status at each edge.
4. **Use semantic conformance tests.** For each requirement, plant satisfying, violating, boundary, vacuous, omitted-observation, alternate-valid, and contradictory cases. Test the complete natural-language→observer→verdict path.
5. **Separate requirement satisfaction from plan quality.** Keep hard-gate conformance, soft-preference handling, factual feasibility, artifact quality, user preference, and professional acceptance as distinct score families.
6. **Validate type and content independently.** Ask the issuer to confirm meaning/force, a domain reviewer to assess applicability/completeness, and an evaluator reviewer to assess observability/check correctness. Approval must not propagate.
7. **Compare elicitation modes.** Use free recall, critical incidents/CTA probes, source/tool import, AI draft-and-correct, and observed-work reconstruction with matched expert burden and downstream defect measurements.
8. **Include legitimate uncertainty.** Some requirements should trigger clarification or human review rather than a forced hard/soft classification.

## Concrete repository actions

No new queue task is added. The required machinery already exists across the expertise-transfer, expert-participation, benchmark-bundle/artifact-admissibility, validity-argument, task-health, metric-monitoring, plural-judgment, and evidence-state contracts. The nonduplicate next implementation should be a conformance slice inside an existing pilot: one requirement compiled through two checker representations, with planted semantic-preservation, missing-observation, and false-pass cases. That should be prioritized during consolidation rather than creating a U-Define- or planning-specific subsystem.

## Claim ceiling

U-Define supports the claim that, in two small formative studies, participants valued explicit hard/soft authoring, criterion-linked hard-rule feedback, and iterative control; experts exposed substantial tacit-context burden and a need for verifier types beyond LTL. It also supplies a concrete prototype architecture and component-similarity evidence. It does **not** establish faithful user-intent capture, semantic translation correctness, objective plan improvement, end-to-end hard-constraint enforcement, calibrated soft-preference grading, professional planning competence, cross-domain transport, high-stakes reliability, production utility, or deployment readiness.

The transferable conclusion is sharper: **the person who owns a requirement should control its force, but that authority does not survive interpretation, compilation, observation, or grading automatically. A formal checker is only as trustworthy as the full evidence-preserving chain into the model it checks.**

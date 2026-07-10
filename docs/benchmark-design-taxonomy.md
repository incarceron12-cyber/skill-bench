# Benchmark Design Taxonomy

This is the canonical design map for converting domain expertise into a valid,
diagnosable knowledge-work benchmark. `docs/state-of-the-art-map.md` tracks the
external landscape; this document defines `skill-bench`'s internal objects and
boundaries. Reviews and reports retain source-specific detail rather than being
copied here.

## 1. Three different taxonomies

Earlier notes mixed three useful but non-interchangeable views. Keep them
separate:

1. **Authoring lifecycle:** how evidence becomes a releasable task.
2. **Measurement stack:** what a trial observes and what each score can claim.
3. **Operating layer:** how a task bank is versioned, calibrated, and improved.

A workflow phase is not a score, a rubric check is not a latent competency, and
a mid-difficulty panel is not a task-authoring method. Treating these as one flat
list causes schema drift and overclaiming.

## 2. Authoring lifecycle: expertise to executable task

| Stage | Canonical object | Required benchmark-design primitives | Evidence / release question | Current executable home |
|---|---|---|---|---|
| 1. Elicit | Evidence-bearing expert or source claim | trusted source, cue, caveat, expert/novice contrast, confidence | Who asserted this, from what evidence, and at what strength? | `expertise-transfer.schema.json`: contributors, claims, provenance |
| 2. Decompose | Domain primitive | hidden requirement, contradiction, decision threshold, artifact convention, failure signature, preference, safety/compliance constraint | What irreducible judgment changes competent work? | expertise-transfer primitive records |
| 3. Expose | Critical-incident scenario | role, stakeholder decision, stakes, difficulty knob, alternative valid procedure | What situation makes the primitive observable rather than merely described? | expertise-transfer scenarios; `templates/task-metadata.md` |
| 4. Ground | Source pack and trap | source authority, evidence locator, contradiction mechanism, fairness basis | Can success be justified from supplied/allowed evidence, and is the trap professionally legitimate? | expertise-transfer source pack and traps |
| 5. Contract | Artifact and workflow expectation | artifact interface, state transition, workflow ordering, completion threshold | What inspectable state or work product would a professional produce? | expertise-transfer artifact/check crosswalk; benchmark bundle task/artifact contracts |
| 6. Instrument | Criterion/check and grader | criterion provenance, applicability, evidence access, pass boundary, dependence, gate/scored semantics, visibility, root-cause labels | Does each check test a disclosed professional requirement or fair held-out consequence, and can the grader observe the predicate? | benchmark bundle checks and graders |
| 7. Pilot | Trial and adjudication evidence | counterfactual variant, expert rating, disagreement, invalid-run reason | Does the task discriminate real quality without rewarding leakage or harness accidents? | benchmark bundle trials/traces; expertise-transfer pilot gates |
| 8. Release | Versioned public/private package | public basis, held-out consequence, calibration-only metadata, known limitation | Is the package expert-valid, leakage-reviewed, reproducible, and explicit about its claims? | expertise-transfer release gates; bundle hashes/provenance |

The lifecycle is a graph, not a lossy handoff. The durable lineage is:

```text
claim → primitive → scenario/source/trap → artifact/workflow evidence
      → check/grader → trial observation → adjudication/release decision
```

Every downstream object should be traceable upstream. A synthetic design
hypothesis may enter the graph, but must not be relabeled as expert testimony.
The implemented authoring contract enforces reciprocal mappings and the rule
that a private check tests a consequence of a public basis rather than a hidden
obligation [ET].

### 2.1 Expertise is a governed handoff, not an inherited label

The claim graph records intellectual provenance, but provenance alone does not
carry authority through transformations. Keep a separate participation and
authority lineage for each contribution: purpose and allowed use, contributor
comprehension, compensation or reciprocal output, attribution/license,
withdrawal boundary, decision rights, and every expert/developer/model/script
transformation. A downstream artifact inherits its parents' provenance, **not**
their approval. `expert-authored`, `expert-edited`, `expert-approved after
inspection`, `developer-derived`, `model-derived`, and `unreviewed` are distinct
states [EP].

This layer governs *who may contribute, transform, apply, and approve*; it does
not replace cognitive-task-analysis methods for eliciting cues and strategies
or the expertise-transfer objects that store their content. Scarce expert time
should be reserved for authority-bearing boundaries, transformation audits,
disagreement, and claim-specific release review only after held-out evidence
shows that builders or graders can perform routine application faithfully. The
reviewed ethnography motivates this design from one compensated university
case; it does not establish a free/near-zero-cost participation model or that
developer/model substitution preserved expert judgment [EP].

### 2.2 A legitimate trap is a decision-boundary critical incident

Do not equate realistic messiness with arbitrary obscurity. For each trap,
preserve an authoring chain:

```text
plausible naive path → expert-visible cue → expert operation/derivation
                     → decision or artifact boundary → counterfactual consequence
                     → focused check and predicted failure signature
```

The consulting benchmark calls the core triple `Lazy AI Test → Expert Test →
Solution Logic`; `skill-bench` treats it as a cross-domain hypothesis to test,
not as a consulting-only task taxonomy [CT]. A fair private trap must remain a
consequence of a public professional requirement, admit alternative valid
procedures, and matter to a downstream decision or artifact state.

Evidence checks should type at least five predicates separately: source
**existence/resolution**, claim **entailment**, source **authority**, claim/source
**scope**, and temporal **freshness**. Also separate cue detection,
reconciliation/operation, intermediate result, threshold comparison, final
decision, and artifact compliance. This prevents a real but irrelevant citation
or an accidental final answer from concealing the actual failure. The reviewed
paper reports useful task patterns and results, but its task corpus, verifier
specifications, grading artifacts, and response matrix were absent from the
inspected release; use it as design evidence, not calibration ground truth [CT].

### 2.3 A rubric is a dependency-aware evidence model

Rubric decomposition makes expert attention inspectable, but does not make it
neutral or independent. Treat each criterion as a versioned evidence object:

- stable ID and immutable text/hash; polarity; provenance claim and evidence
  locators; public basis; author/reviewer authority scope;
- `hard_gate`, `required_scored`, `optional_preference`, `penalty`, or
  `diagnostic_only` semantics rather than encoding “mandatory” as a large weight;
- applicability predicate and an `insufficient_evidence` outcome distinct from
  failure, including the artifact/source/trace access the grader requires;
- one observable and decision rule, with a split review for multiple independently
  falsifiable predicates;
- prerequisite, overlap, exclusion, and shared-evidence links so aggregation does
  not silently double-count one fact; and
- typed examples (`boundary_case`, `non_exhaustive_instance`, `counterexample`,
  or `reference_answer_fragment`) with disclosure and exhaustiveness metadata.

ResearchRubrics provides unusually inspectable evidence for a three-role
draft/review/final-review pipeline and criterion-level judging, but not for
criterion atomicity, domain-professional authority, independence, or calibrated
artifact sufficiency. Its released corpus includes long example-rich criteria,
implicit requirements as the largest category, and small schema-integrity defects;
its additive score lets a nominally mandatory miss be compensated [RR]. Preserve
the authoring pattern, not the inference that expert-written criteria are ground
truth. Its example ablation suggests examples can improve judge agreement while
also anchoring answers; rubric transformations therefore need before/after hashes,
semantic review, and held-out tests of both agreement and construct breadth [RR].

## 3. Measurement stack: trial to defensible claim

| Layer | Unit observed | Appropriate claim | Do not infer |
|---|---|---|---|
| Environment validity | containment canaries, tool/service availability, fixture integrity, permissions, timing | the trial had the declared evidence boundary and a valid opportunity to complete the task | agent inability from repository escape, provider failure, or a broken environment |
| Workflow/process | ordered trace events and intermediate states | compliance with an observable professional invariant | latent expertise merely because a disclosed procedure was followed |
| Checkpoint/state | verifiable partial state | meaningful progress and stage-specific capability | professional acceptability of the final artifact |
| Artifact internals | formulas, citations, structure, file properties, maintainability | technical correctness and inspectable construction quality | stakeholder preference or release readiness |
| Artifact presentation/judgment | clarity, usability, visual/professional conventions | judged quality on declared dimensions | objective correctness when no deterministic check supports it |
| Human preference | blinded pairwise choice | relative preference in the sampled expert population | an absolute approval threshold |
| Human readiness | independently calibrated accept/reject threshold | release/deployment acceptability under stated stakes | universal preference or fine-grained automated-score validity |
| Safety/compliance | authorization, prohibited action, policy consequence | compliance with declared constraints | task success as a reason to waive safety |
| Efficiency | cost, latency, retries, human-review time | quality-resource tradeoff for a versioned system | capability independent of provider/harness configuration |
| Diagnosis | failed check plus causal trace slice | plausible root and surface failure under an explicit attribution method | causal certainty from an unvalidated LLM diagnosis |
| Evolution trajectory | ordered trials, state deltas, retention/transfer probes, and cost/safety drift | adaptation, retention, selective forgetting, and policy drift under one frozen stream protocol | independent-task competence or improvement caused by one changed component |

Store these score families separately. Aggregation is a versioned policy, not a
natural property of the task. LH-Bench supports observable-boundary rubric
engineering and broad aggregate ranking convergence, but its weak individual
human/automated agreement warns against treating judge scores as perceptible
professional-quality intervals [LH]. STRACE motivates linking a failed check to
a compact causal slice while retaining uncertainty about an LLM-inferred graph
[ST].

### 3.1 From measurement to a licensed claim

A valid trial yields observations; it does not automatically license a
capability, readiness, or deployment claim. Bind each proposed interpretation
or use to an independently versioned **validity argument**:

- immutable instrument, configured-system, measurement, and population refs;
- one criterion, construct, or decision claim and its intended use;
- warrant, assumptions, rebuttals, alternative explanations, and excluded
  interpretations;
- content, criterion, construct, external, and consequential evidence kept as
  separate ledgers rather than averaged into a validity score;
- generalization boundary, threshold/loss basis, stakeholders, residual risk,
  status, owner, expiry, and reassessment triggers.

Use a claim ladder: (1) exactly observed measurement, (2) bounded capability
generalization, and (3) readiness/decision. A narrow claim may be supported
while wider rungs remain explicitly unsupported. A readiness threshold is
itself a claim about acceptable loss, not a formatting constant. The reviewed
validity framework provides a strong conceptual basis and retrospective cases,
but no evidence that reviewers apply its facets reliably or that the process
improves decisions; the contract and its inter-reviewer behavior therefore
remain project hypotheses to validate [VA].

The same caution applies to diagnosis. “Formatting failed” can be a direct
observation; “professional judgment caused the failure” is a broader causal or
construct claim requiring a warrant and tests of alternatives. Validity
arguments supplement rather than replace raw scores, expert dispositions, and
trace evidence.

### 3.2 A grader observation is not a population metric

Keep four records separate:

```text
criterion/check definition
  → grader observation on one trial
    → metric specification over an eligible population
      → monitoring decision and action record
```

A grader observation binds evidence locators, artifact/rubric/grader versions,
predicate outcome, insufficiency or execution failure, and uncertainty to one
attempt. A **metric specification** additionally declares the construct and
prohibited interpretations; unit and eligible event population; inclusion,
sampling, clustering, duplicate/retry, missing/invalid/delayed-label policy;
numerator/denominator or scale; aggregation/dependence/weighting and uncertainty;
slices and minimum support; comparator/window; and source-population fidelity.
A **monitoring action** then binds a versioned metric to a threshold and loss
basis, alert/audit policy, owner, remediation, rollback, and expiry.

A grader or expert record must also identify its **evidence view**, not merely
its author and verdict. Type the predicate; required channels; channels actually
received; temporal scope; evidence locators; raw and parsed outputs; model,
prompt, and policy versions; retries and fallback representation; confidence;
and `invalid` or `insufficient_evidence` separately from a substantive negative.
Artifact views, full trajectories, environment queries, agent reasoning, and
private state are different observation treatments. Agreement between observers
with unequal views does not isolate judgment ability [ARB].

Preserve deterministic outputs, model judgments, and every human label as
separate immutable observations before resolution. Duplicate labels need stable
annotator IDs, assignment and independence metadata, uncertainty, and an
explicit adjudicated record containing policy, adjudicator, rationale, changed
fields, and disagreement type. File order, overwrite precedence, or a generic
`expert` label is not adjudication. AgentRewardBench's released table contains
mostly single labels and selects the first CSV occurrence as primary; its one
systematically duplicated 100-trajectory subset lacks a released consensus
lineage, while paper/release agreement calculations cannot be reconciled from
the preserved fields [ARB]. This is evidence for the lineage requirement, not a
portable estimate of human reliability.

Reliability is an error surface indexed by predicate × task family × configured
system × evidence view × threshold × time, not one judge attribute. Report
confusion matrices, prevalence, asymmetric loss, task-clustered uncertainty,
slices, repeated-call stability, invalid-output rate, and audit burden. The
AgentRewardBench sample is 1,302 once-generated trajectories from 351 web tasks;
its pooled results omit intervals and task-cluster adjustment, and its rare
side-effect labels have very different errors from success or repetition [ARB].
These limits support heterogeneous reporting, not a claim about judges across
knowledge-work domains.

Amazon's production architecture usefully connects offline/online traces,
component and end-to-end evaluators, dashboards, alerts, human audits, and
business effects. It does not publish formulas, denominators, uncertainty,
threshold performance, synthetic-fidelity evidence, human reliability, or
quantitative framework effects [AM]. Its metric names and cases therefore motivate
contracts and failure hypotheses, not validated estimands. Component scores are
diagnostic candidates rather than proven root causes, and business outcomes must
remain separate until an explicit causal/validity bridge supports them. Likewise,
ResearchRubrics' criterion-label macro-F1 does not calibrate its weighted aggregate
or a professional threshold; criterion dependence and grader failures must remain
visible rather than being converted to ordinary zeros [RR].

### Failure attribution vocabulary

Use three coordinates rather than one flat failure tag:

1. **Validity owner:** `agent`, `task_design`, `grader`, `environment`, or
   `indeterminate`.
2. **Surface stage:** where failure became observable (retrieval, calculation,
   tool execution, artifact construction, verification, presentation, safety).
3. **Root capability/process:** the earliest supported cause (planning, source
   authority selection, evidence reconciliation, threshold judgment, state or
   context tracking, tool use, artifact convention, verification/recovery,
   stakeholder judgment).

A surface build error may originate in source selection; an unattributed timeout
may be environmental. Preserve event locators and attribution confidence so
later adjudication can revise the diagnosis without changing raw evidence.

## 4. Intervention, instrument, and system identity

A benchmark trial evaluates a configured system, not an abstract model. Version
and hash these independently:

- base model and decoding policy;
- harness/scaffold and memory policy;
- public skill/procedure package;
- tool interfaces and permissions;
- task/source/environment version;
- rubric and check set;
- grader code, prompt, and model;
- runtime feedback policy;
- retry/adaptation policy.

The public skill is an **intervention**; the rubric is a **measuring instrument**.
When both derive from the same expert model, shared boundaries can improve judge
consistency but also create evaluator-cue compliance. The minimum causal matrix
is no-skill/public-skill × independent/shared-rubric, with exact-rubric
disclosure only as an explicit leakage/compliance condition [LH].

For adaptive systems, also pin stream order/seed, warmup, similarity groups,
reset cadence, update budget, and which feedback may enter memory. Once one test
item changes behavior on the next, the estimand is ordered-stream learning, not
independent pass@1 [ACE, SE].

### 4.1 Execution validity is an observed boundary, not a directory name

Separate three layers that are often collapsed under “harness” or “sandbox”:

1. **Intended harness treatment:** prompts, tool interface, context/memory policy,
   recovery behavior, and native permissions that the comparison intends to vary.
2. **Adapter realization:** path mapping, environment filtering, process launch,
   timeout, usage capture, and trace extraction that connect the harness to the
   task.
3. **Outer execution envelope:** fixture identity; read, write, process, network,
   and secret boundaries; private-evaluator denial; resource policy; clean reset;
   and service availability that every comparable arm must satisfy.

The first two are part of configured-system identity. The third is a validity
contract: test it through the actual agent-facing tools before a model call and
retain each expected/observed probe with the launcher and environment hashes.
`cwd`, a fresh workspace, an isolated `HOME`, or a directory named `sandbox` is
not evidence that parent paths, absolute paths, sibling trials, private graders,
network destinations, or inherited secrets are unreachable [HB]. A canary's
claim is also tool-scoped: a read/search/write canary does not prove containment
for an unexposed shell or browser.

Use a fail-closed evidence ladder:

```text
outer-envelope canary passes
  → service starts and trial evidence is attributable
    → declared deliverables and mandatory measurements are complete
      → matched arms share the required envelope/configuration
        → condition contrast is estimable
          → wider capability/readiness claim requires its own validity argument
```

Failure at a rung preserves all earlier evidence but blocks later claims. In the
LH pilot, the original file-tool runs empirically exposed repository-private
material and were invalid trials. A later bubblewrap launcher passed zero-call
canaries through the actual file tools in both arms, so filesystem environment
validity was established for those interfaces. The no-skill arm then produced
no deliverables after provider-stream retries while the public-skill arm
completed. This is one valid configured-system execution plus a service-layer
failure—not a matched Skill effect, not evidence that the failed arm lacked the
capability, and not professional-readiness evidence [PX].

Missing trace, artifact, usage, component identity, security result, or canary
must yield `invalid` or `unscorable` according to the predeclared gate; never
substitute a perfect default. Preserve launch failures and timeout censoring in
the response matrix. Attribute an adapter, provider, or environment root only
when event evidence supports it; otherwise use `indeterminate` rather than
turning operational missingness into an agent failure.

### 4.2 Retrieval is governed information flow, not automatic leakage

Retrieval is often part of the professional construct. A source becomes leakage
only through a relation among the task version, information object, access
policy, trial event, and licensed claim. Freeze a versioned information-flow
policy that declares network mode, legitimate source classes, protected objects
(`task_instance`, `reference_answer`, `private_check`, `rubric`, calibration
case, and private source-pack material), snapshots, allowed tools, and fail-closed
behavior. An original domain source can be required evidence in one task and an
answer-bearing shortcut in another [SC].

Preserve a staged external-evidence chain rather than one `contaminated` flag:

```text
query/provider/time → result returned → page accessed → content captured
  → protected-object match → agent/model visibility → incorporation or adoption
    → score quarantine → causal effect estimate under a separate intervention
```

Each arrow needs its own observation and evidence sufficiency. Record provider
and index mode, timestamp/locale, rank, URL and redirects, visit status, content
hash or snapshot, agent-visible extraction, detector/version, match relation,
and artifact/citation use. A suspicious host, returned URL, final citation, or
privileged detector match alone does not prove intent, model visibility,
adoption, or score inflation [SC]. When proprietary traces omit a rung, retain
`insufficient_evidence`; do not manufacture equivalence with a richer trace.

Keep mechanisms separate: **pretraining contamination** (possible parameter
exposure before the run), **search-time leakage** (protected material retrieved
during it), **evaluator-cue leakage** (skills, examples, feedback, or rubrics
reveal private reward boundaries), **local/private-file leakage** (the execution
envelope exposes protected repository or sibling-trial material), **cross-trial
leakage** (memory retains protected outcomes), and **legitimate domain
retrieval**. One mechanism is not evidence for another. Audit prevalence is also
not a causal score correction: identifying exposure can quarantine a trial, but
estimating effect requires matched replay or randomized masking that holds the
task, configured system, provider snapshot, budget, and legitimate evidence
constant [SC].

The search-time-contamination study motivates this chain from 6,803 medical QA
items, but only its explicit-answer detector received partial human validation;
metadata/context detectors were unvalidated or under-specified, exposure was
agent-selected, commercial traces were not measurement-equivalent, runs were
not repeated, and the reported “up to 4%” correction was not auditable in v1
[SC]. Treat it as a strong audit signal and experiment design, not a general
prevalence estimate or causal correction for knowledge work.

### 4.3 Keep three change planes separate

“The system improved” is ambiguous because three different systems can change.
They need different atomic records, evidence gates, and claims:

| Change plane | Atomic record | What may change | Defensible claim | Required boundary |
|---|---|---|---|---|
| Evaluated agent system | **evolution event** between parent and child configured-system hashes | model, prompt/skill, memory, tools/code, topology, or update policy | adaptation, retention, transfer, forgetting, cost, or safety drift over a declared stream | only policy-permitted public/runtime feedback may enter agent-visible state; private checks and references remain firewalled |
| Benchmark-design knowledge | **candidate-lesson lifecycle event** | an evidence-backed authoring, grading, or operating claim | the lesson was proposed, independently tested, promoted, quarantined, superseded, or rolled back | a score gain on the source task is not independent validation; retain provenance, contradictions, scope, and downstream dependencies |
| Released benchmark instrument | **benchmark version/change record** | tasks, sources, environments, rubrics, graders, panels, or aggregation policy | the instrument changed, with an audited compatibility or recalibration result | freeze the instrument inside a matched longitudinal comparison; bridge old/new versions before interpreting score trends |

An evolution event records changed loci, trigger and timing, typed feedback
authority/visibility, update mechanism and seed, before/after hashes, resource
use, validation, and rollback. These are multi-label causal coordinates, not one
“self-evolving” category. Longitudinal reporting separates initial competence,
held-out adaptation gain, retention/regression, and cost/safety compliance; it
does not collapse them into a final average [SE].

The minimum causal protocol is a static baseline followed by a versioned task
stream with multiple orders where feasible, equivalent-form retention and
selective-forgetting probes, and matched reset vs permitted-memory/skill-only vs
full-evolution conditions. Observable actions, artifacts, state deltas, and
verifier evidence are sufficient; faithful hidden chain-of-thought is neither
required nor assumed [SE].

If the agent and benchmark instrument change in the same comparison window,
ability change and difficulty drift are not identified. Record both events, but
do not call their joint score movement self-improvement without a frozen anchor
panel or a calibrated bridge design.

## 5. Operating layer: task bank to living instrument

| Object | Purpose | Required controls |
|---|---|---|
| Full task bank | construct coverage and periodic absolute calibration | domain/primitive coverage, versioning, expert validity, full-run history |
| Routine evaluation panel | lower-cost ranking or regression checks | historical difficulty, held-out rank-fidelity validation, population/scaffold label, drift trigger |
| Diagnostic/critical set | preserve rare safety, compliance, and expert traps | never remove solely because checks are too hard/easy for rank discrimination |
| Response matrix | empirical memory of attempts | task/check, model, scaffold, skill/tool/feedback policies, outcome, cost, timestamp, versions |
| Private calibration layer | references, grader internals, difficulty/features, adjudications | access control, provenance, non-leakage into agent-visible context |
| Drift/saturation monitor | detect stale difficulty and changed task behavior | periodic full runs, score/rank separation, missingness and invalid-run audit |
| Validity argument register | bind measurements to bounded interpretations and uses | claim ladder, warrants/rebuttals, facet evidence, excluded interpretations, threshold/loss basis, expiry |
| Participation/authority ledger | govern expert contribution and transformed artifacts | purpose/consent, reciprocal value, decision rights, transformation lineage, reconsent, approval that never propagates implicitly |
| Execution validity record | establish whether a trial had the declared boundary and opportunity | tool-scoped canary probes, adapter/launcher/environment hashes, fixture identity, service health, mandatory evidence, invalid/unscorable reason |
| Metric specification and monitoring record | turn trial observations into a reproducible population estimand and governed trigger | eligible population/unit, versions, missingness, clustering/dependence, aggregation/uncertainty, slices, baseline/window, threshold/loss, alert/audit/remediation/rollback |
| Candidate lesson store | improve authoring and systems without silent doctrine drift | provenance, feedback authority, scope, contradiction links, held-out promotion, rollback |
| Longitudinal stream | measure an update policy rather than independent pass@1 | frozen benchmark version, order/seed, clusters, persistence/reset policy, budgets, feedback firewall, equivalent-form probes |
| Benchmark change log | distinguish instrument drift from agent evolution | old/new component hashes, rationale, affected claims, bridge panel, compatibility/calibration decision, rollback |

A reduced panel serves **ranking efficiency**, not automatically diagnostic
coverage or absolute professional-quality estimation. Mid-range checks often
carry the most rank information, while rare hard safety/contradiction checks may
be strategically indispensable. Keep separate panel objectives and report rank
fidelity separately from score calibration [EB, AP].

## 6. Family map: what each benchmark pattern contributes

| Pattern / examples | Primary reusable object | Main validity risk | Evidence status here |
|---|---|---|---|
| Artifact-centered professional work (AA-Briefcase, MBABench, WorkstreamBench) | multi-file deliverable and correctness/internals/presentation contracts | polished output hides unsupported analysis; subjective dimensions dominate | landscape/triage; local AA source material, no dedicated deep review yet |
| Stateful workflow (SaaS-Bench, Workflow-GYM, OdysseyBench) | persistent environment, stage checkpoints, final-state verification | infrastructure failures and tool familiarity confound capability | full-text triage in `reports/daily/2026-07-10-morning.md`; no dedicated deep reviews yet |
| Skill-grounded long-horizon evaluation (LH-Bench) | expert procedure → observable boundary → artifact/check crosswalk | intervention/instrument contamination; agreement mistaken for validity | full immutable v2 PDF/text and deep review [LH] |
| Trace diagnosis and recovery (STRACE, LH-Bench recovery analysis) | dependency-aware causal slice; error→feedback→repair→verification chain | inferred root cause may be wrong; post-test optimization can leak | extracted-paper deep review [ST] plus LH-Bench full review |
| Psychometric operation (Efficient Benchmarking, Agent Psychometrics) | response matrix, difficulty/discrimination, reduced ranking panel, scaffold-aware analysis | historical population drift; ranking panel drops rare diagnostic coverage | extracted-paper deep reviews [EB, AP] |
| Continual/context adaptation and self-evolution (ACE; self-evolving-agent survey) | immutable local delta, candidate-lesson lifecycle, evolution-event ledger, retention/transfer stream | order dependence, weak-feedback pollution, private-test contamination, mixed-component attribution, benchmark/agent co-evolution | full immutable ACE v3 and survey v4 PDFs/text plus deep reviews [ACE, SE] |
| Production agent evaluation (Anthropic, Amazon) | task/trial/grader/trace separation, task-health lifecycle, metric/monitoring contract, and operational failure taxonomy | engineering guidance may not establish construct validity; named metrics omit populations/estimands; synthetic and online samples drift | full official Anthropic and Amazon articles and concept reviews; experience/prescription evidence, not controlled effectiveness studies [AN, AM] |
| Expert-authored criterion evaluation (ResearchRubrics) | reviewed criterion inventory, criterion-level judge observation, rubric transformation lineage | task-design authority mistaken for domain authority; bundled/dependent or hidden criteria; artifact-only source checks; uncalibrated additive score | full immutable v1 paper plus inspected post-paper official code/dataset releases; authoring and agreement evidence, not professional-readiness validation [RR] |
| Claim-centered validity | claim ladder, warrant/rebuttal record, facet-specific evidence, threshold/loss basis | checklist ritual, subjective facet ratings, reliability omitted, consequences under-specified | full immutable v4 conceptual paper and deep review; framework itself not empirically validated [VA] |
| Expert participation and transformation governance | scoped contribution unit, authority lineage, reconsent and reciprocal output | expert approval laundered through synthetic/developer/model transformations; favorable single-site evidence | full immutable v1 ethnography and deep review; no fidelity, cost, or near-zero-cost validation [EP] |
| Decision-boundary cognitive traps (consulting study) | naive-path/expert-cue/derivation/consequence chain; typed evidence predicates | unavailable corpus/graders, unstable live data, human-applied checks, unvalidated failure tags | full immutable v3 paper plus linked release inspection; design pattern only, not auditable calibration evidence [CT] |
| Configured-system and harness comparison (Harness-Bench) | harness/adapter identity, outer-envelope contract, execution-alignment trace | bundled treatments, adapter inequivalence, host-readable private graders, fail-open missing evidence, single-attempt cells | full immutable v1 paper plus inspected post-paper official release; descriptive configuration evidence, not mechanism isolation [HB] |
| Trajectory-judge calibration (AgentRewardBench) | typed observer evidence view, plural immutable labels, explicit adjudication lineage, predicate-specific error surface | unequal human/judge observability; mostly single labels; row-order authority; class imbalance; pooled unclustered metrics; invalid output conflated with negatives | full immutable v2 paper plus pinned code/annotation release inspection; bounded web-task agreement evidence, not general judge or professional-validity calibration [ARB] |
| Retrieval-leakage auditing (search-time contamination) | information-flow policy and staged result/access/match/visibility/adoption/effect chain | legitimate retrieval conflated with shortcut access; detector stages under-validated; endogenous exposure mistaken for causal inflation; proprietary trace inequivalence | full immutable v1 paper; 6,803 medical-QA audit items, partial explicit-answer-detector validation, no auditable causal correction or cross-domain prevalence [SC] |

“Deep review” above means the cited local full text was read in the corresponding
review; “triage” and “preliminary” are not promoted to equivalent evidence.

## 7. Design invariants

1. **Public basis, private consequence:** private checks may hide implementation,
   examples, weights, or perturbations, but not invent undisclosed obligations.
2. **Observable boundaries, plural valid procedures:** grade consequential states
   and artifacts; do not force one sequence unless ordering is itself expert- and
   outcome-grounded.
3. **Separate intervention from instrument:** independently version skills,
   rubrics, graders, tools, and feedback.
4. **Separate score families:** process, checkpoint, artifact, preference,
   readiness, safety, efficiency, and diagnosis remain distinct until a declared
   aggregation policy is validated.
5. **Separate root from surface:** every failure attribution retains raw event
   evidence and uncertainty.
6. **Separate invalid trials from capability failures:** environment, task, and
   grader defects remain visible rather than being silently excluded.
7. **Preserve lineage:** consolidation links or supersedes claims; it does not
   erase provenance or disagreements.
8. **Calibrate for the intended claim:** ranking, diagnosis, and absolute
   readiness require different samples and checks.
9. **Firewall evaluation evidence:** private checks/reference answers cannot feed
   an agent-visible skill or lesson on the same split.
10. **Promotion requires independent evidence:** schema completeness or improved
    training-set score is not enough to change durable benchmark doctrine.
11. **Freeze or bridge the instrument:** do not attribute longitudinal score
    movement to agent evolution while tasks, graders, or panels change without
    a frozen anchor or explicit recalibration design.
12. **Approval does not propagate:** transformed expert material retains
    provenance but requires new, purpose-specific review before it can be called
    expert-approved.
13. **Measurements do not self-interpret:** every capability/readiness claim and
    threshold has a bounded validity argument; unsupported claim upgrades fail.
14. **Messiness must be consequential:** a hidden trap needs a public basis,
    expert-visible cue, auditable correction, decision/artifact consequence, and
    focused diagnostic check.
15. **Execution evidence fails closed:** prove the outer envelope through every
    exposed tool interface before a trial; missing service, trace, artifact,
    security, or attribution evidence blocks the corresponding capability or
    contrast claim rather than defaulting to success.
16. **Criterion provenance does not imply atomicity:** type authority,
    applicability, evidence access, gate/scored semantics, and dependencies; an
    expert-written or high-weight criterion is not automatically fair, independent,
    observable, or decisive.
17. **Observations do not define metrics:** population, denominator, missingness,
    dependence, uncertainty, threshold, and action semantics must be versioned
    before a per-trial score becomes a monitoring statistic or decision trigger.
18. **Observers do not share a view by default:** bind each expert, deterministic,
    or model judgment to required and actual evidence channels; preserve plural
    labels and adjudication lineage; invalid execution and insufficient evidence
    are not substantive failures.
19. **Retrieval validity is stage- and policy-specific:** distinguish returned,
    accessed, matched, visible, adopted, and effect-estimated states, and keep
    legitimate domain retrieval separate from pretraining, evaluator-cue,
    local-private-file, cross-trial, and search-time leakage.

## 8. Unresolved tensions and required experiments

| Tension | Current evidence | Resolution experiment |
|---|---|---|
| Public procedure improves execution vs leaks evaluator cues | LH-Bench's rubric agreement improves, but execution ablation is only seven paired runs and the skill/rubric roles are confounded [LH]. | Four-condition skill × rubric-source ablation on one pilot; compare artifact/readiness outcomes, not process score alone. |
| Automated agreement vs professional validity | LH-Bench judges agree more under expert boundaries, yet individual human/automated concordance is weak [LH]. | Two-expert readiness labels and pairwise choices on a stratified pilot subset; calibrate each automated check against both. |
| Mid-difficulty efficiency vs rare critical coverage | Psychometric work favors informative middle checks; benchmark mission requires hard safety and expert traps [EB, AP]. | Maintain separate ranking and critical diagnostic sets; test rank fidelity and primitive coverage independently. |
| Workflow compliance vs latent expertise | Observable transitions are more judgeable, but exact procedure following can substitute for judgment [LH]. | Include at least two expert-approved procedures and held-out consequence variants. |
| Learning from failures vs benchmark contamination | STRACE/ACE support localized lessons; ACE also degrades under weak feedback and changes the online estimand [ST, ACE]. | Quarantine lessons, validate on held-out scenario clusters, and audit private-evidence flow before promotion. |
| Aggregate leaderboard vs diagnostic instrument | Reduced rankings are cheaper, while root-cause layers produce more actionable but uncertain claims [EB, ST]. | Report both without one composite; evaluate whether diagnoses predict expert-prescribed remediations on repeat trials. |
| Evolving agent vs evolving benchmark | Longitudinal guidance requires persistent state, while living benchmarks must also revise tasks and graders; changing both makes ability and difficulty jointly endogenous [SE]. | Freeze an anchor instrument within each stream; when the benchmark changes, run a bridge panel and report version effects before resuming evolution claims. |
| Efficient expert substitution vs authority laundering | One ethnography shows why teams shifted routine work to developers and an LLM judge, but reports no held-out fidelity or cost evidence [EP]. | Compare expert vs builder/grader application on frozen held-out anchors; record time, disagreement, transformation review, consent changes, and claim blocks without averaging agency and fidelity. |
| Useful narrow result vs broad capability/readiness claim | Claim-centered validity allows a criterion result to remain useful while rejecting wider construct or decision claims, but reviewer reliability is untested [VA]. | Have independent reviewers construct claim ladders for the same pilot trials; measure disagreement and test whether the contract rejects planted claim upgrades. |
| Realistic trap vs benchmark gotcha | Decision-boundary traps can expose expert judgment, but the reviewed consulting corpus and graders are not auditable and live values can drift [CT]. | Instantiate the same critical-incident record in two structurally different domains; plant naive/correct variants and test fairness, typed evidence checks, threshold flips, and predicted failure localization. |
| Ecological harness comparison vs valid common envelope | Native harness behavior is a legitimate bundled treatment, but Harness-Bench's later runner and the LH pilot show that fresh directories and shared prompts do not establish equivalent filesystem, network, service, or measurement opportunity [HB, PX]. | Run tool-level denial/allow canaries and adapter conformance checks before each cell; retain service failures; repeat matched cells; estimate a contrast only when both arms satisfy one hashed envelope and mandatory-evidence policy. |
| Judge agreement vs rubric construct preservation | ResearchRubrics finds better binary than ternary agreement and modest agreement gains from examples, but lacks duplicated-human reliability, criterion atomicity/dependence audits, and evidence access for source predicates [RR]. | On a pilot rubric, independently mark bundled/overlapping criteria and answer anchors; compare transformed variants on duplicated expert labels, judge confusion, legitimate solution diversity, and external artifact acceptability. |
| Dashboard simplicity vs reproducible population inference | Amazon links traces, metrics, alerts, and audits operationally but reports no estimands, denominator/missingness rules, uncertainty, alert accuracy, or synthetic-to-real fidelity [AM]. | Backtest a versioned metric over planted agent, grader, environment, and population shifts; retain invalid/delayed events and measure detection delay, false alarms, review burden, and remediation routing. |
| Judge agreement vs evidence-view parity | AgentRewardBench compares richer human access with final-state-focused model views, preserves mostly single labels, and reports pooled unclustered metrics; disagreement can originate in task policy, trace capture, evidence access, or judgment [ARB]. | Plant temporally scoped success/side-effect cases; cross grader type with artifact-only, full-trace, and environment-query views; duplicate expert labels; adjudicate with explicit lineage; report predicate- and task-clustered error plus audit cost. |
| Open retrieval realism vs shortcut-free causal measurement | Search-time contamination finds strong post-exposure associations for exact answer-bearing pages, but weak detectors, self-selected access, mutable search, and non-equivalent traces do not identify a clean counterfactual [SC]. | Pair ecological open-retrieval audits with replayable snapshots and randomized masking of protected answer artifacts while holding legitimate sources, configured system, task, and budget fixed; report exposure prevalence separately from effect. |

None of these tensions currently requires a Level 2 strategic decision. The
first pilot can gather the discriminating evidence before choosing a public
leaderboard posture.

## 9. Current build sequence and dependency gates

This sequence consolidates existing queue work rather than creating duplicate
requests. Completed foundations remain listed so later workers do not rebuild
them:

1. **Completed — `build-procedural-skill-eval-contract`:** the bundle now types
   intervention/instrument versions, leakage boundaries, ablation conditions,
   and recovery edges.
2. **Completed, not release-valid — `build-pilot-scenario`:** the static LH
   adoption pilot instantiates both contracts, but intentionally fails expert
   validity and release gates.
3. **Blocked execution gate — `build-lh-pilot-grader-ablation`:** planted
   grading and fixture replay are complete. The first genuine pair failed the
   outer-envelope gate and remains invalid; the bubblewrap replacement then
   passed file-tool canaries in both arms, but provider streaming left the
   no-skill arm without deliverables. The completed public-skill arm is one
   configured-system observation only. Retry a fresh matched pair under one
   launcher hash when service health permits; preserve launch failures, usage,
   typed existence/entailment/authority/scope/freshness results, and strict
   completion gates. Only then assess a Skill contrast and pursue qualified
   shared-rubric and expert adjudication. SkillsBench and Harness-Bench refine
   selection, uncertainty, and isolation requirements but are not pilot
   execution evidence [HB, PX].
4. **Completed contract, not demonstrated improvement —
   `build-compounding-lesson-contract`:** immutable candidate lessons now have
   feedback authority, contradiction/supersession, held-out promotion, firewall,
   dependency, and rollback semantics. The synthetic fixture calibrates the
   contract only; no pilot-derived doctrine has passed an empirical promotion
   gate.
5. **Completed contract, not demonstrated learning —
   `build-longitudinal-evolution-protocol`:** the bundle now represents frozen
   streams, matched reset/lesson-only/full-evolution arms, state transitions,
   retention/transfer probes, budgets, and rollback. Its synthetic three-arm
   fixture makes no adaptation, transfer, safety, or readiness claim and must not
   bypass the static pilot's failed contrast gate.
6. **Completed claim contract — `build-validity-argument-contract`:** immutable
   instrument/measurement references, claim rungs, facet ledgers, warrants,
   rebuttals, thresholds, and prohibited upgrades are executable. The planted
   fixture licenses only a narrow regression-behavior claim; real professional
   capability/readiness remains unsupported pending pilot evidence [VA].
7. **Completed participation contract, not demonstrated feasibility —
   `build-expert-participation-contract`:** purpose, reciprocity, authority,
   transformation, withdrawal, and reconsent are executable. Its internal
   fixture validates contract boundaries only; it supplies no real consent,
   motivation, cost, or expert-fidelity evidence [EP, RR].
8. **Completed task-health contract, not longitudinal validation —
   `build-task-health-lifecycle-contract`:** immutable origin, exact-version
   witness, contrast, replicate, adjudication, role-change, revision, and
   retirement records are executable. Its synthetic health history and planted
   grader defect do not establish real task stability or grader accuracy [AN,
   ARB].
9. **Completed metric/monitoring contract, not population validation —
   `build-metric-monitoring-contract`:** observations now bind to eligible
   populations, missing/invalid/duplicate policy, clustering, uncertainty,
   windows, thresholds, audits, and actions. Its exact planted-fixture metric is
   an internal regression check, not production representativeness [AM, ARB].
10. **Completed artifact-view admissibility slice —
   `build-artifact-view-admissibility-contract`:** task checks now declare
   authoritative representations, required views and controls, permitted
   invariances, evidence sufficiency, and fail-closed outcomes. The synthetic
   cross-artifact fixture validates the contract, not cross-domain construct
   validity or grader reliability.
11. **Evidence-gated elicitation contract — `build-elicitation-session-contract`:**
    wait for one consented real contribution before encoding session evidence
    types; do not simulate testimony to satisfy a schema dependency.

## Provenance keys

- **[ET]** `schemas/EXPERTISE_TRANSFER.md` and
  `schemas/expertise-transfer.schema.json` (implemented repository contract).
- **[LH]** `papers/agent-benchmarks/2026-07-10-lh-bench-skill-grounded-evaluation.md`;
  reviewed full text/PDF paths and hash are recorded there.
- **[ACE]** `papers/agent-benchmarks/2026-07-10-agentic-context-engineering.md`;
  reviewed full text/PDF paths and hash are recorded there.
- **[SE]** `papers/agent-benchmarks/2026-07-10-self-evolving-agents-survey.md`;
  reviewed immutable v4 full text/PDF paths and hash are recorded there. Its
  protocol is prescriptive synthesis, not an empirically validated benchmark.
- **[ST]** `papers/agent-benchmarks/2026-07-09-strace.md`; local extracted text
  path is recorded there.
- **[EB]** `papers/agent-benchmarks/2026-07-09-efficient-benchmarking-ai-agents.md`;
  local extracted text path is recorded there.
- **[AP]** `papers/agent-benchmarks/2026-07-09-agent-psychometrics.md`; local
  extracted text path is recorded there.
- **[AN]** `docs/concepts/anthropic-agent-evaluation-lifecycle.md`; reviewed
  full official article and provenance paths are recorded there. This is a
  production experience report, not controlled validation evidence.
- **[AM]** `docs/concepts/amazon-production-agent-evaluation.md`; reviewed full
  official article, local extraction, and provenance paths are recorded there.
  This is production experience and prescription without released quantitative
  effectiveness or metric-validation evidence.
- **[RR]**
  `papers/agent-benchmarks/2026-07-10-researchrubrics-expert-rubric-authoring.md`;
  reviewed immutable v1 PDF/text and inspected official post-paper code/dataset
  release paths and hashes are recorded there. The releases make authoring
  artifacts inspectable but do not supply the manuscript's responses, expert
  labels, or a calibrated professional-quality threshold.
- **[VA]** `papers/agent-benchmarks/2026-07-10-validity-centered-ai-evaluation.md`;
  reviewed immutable v4 PDF/text paths and hashes are recorded there. The source
  is a conceptual synthesis with retrospective cases, not a validated protocol.
- **[EP]** `papers/agent-benchmarks/2026-07-10-domain-expert-participation-ethnography.md`;
  reviewed immutable v1 PDF/text paths and hashes are recorded there. Findings
  are bounded to one compensated university collaboration.
- **[CT]** `papers/agent-benchmarks/2026-07-10-consulting-cognitive-traps.md`;
  reviewed immutable v3 paper and inspected release paths/hashes are recorded
  there. The release lacked the reported task and grading artifacts.
- **[HB]** `papers/agent-benchmarks/2026-07-10-harness-bench-execution-isolation.md`;
  reviewed immutable v1 PDF/text and inspected official post-paper release
  paths/hashes are recorded there. The release is implementation evidence, not
  the exact paper-time runner or empirical result archive.
- **[PX]** `pilots/lh-skill-adoption/validation-plan.md` and
  `pilots/lh-skill-adoption/ablation/isolated-agent-pair-v6/pair-summary.json`;
  local execution evidence records the invalid escaped runs, tool-scoped
  bubblewrap canaries, one completed public-skill arm, one provider-stream
  failure, and the explicit prohibition on a condition-effect estimate.
- **[ARB]**
  `papers/agent-benchmarks/2026-07-10-agentrewardbench-judge-reliability.md`;
  reviewed immutable v2 PDF/text and pinned code, dataset, annotation, and result
  release paths/hashes are recorded there. The release inspection did not mirror
  the complete multi-gigabyte trajectory corpus, and the evidence is bounded to
  sampled web-agent trajectories and the preserved observer views.
- **[SC]**
  `papers/agent-benchmarks/2026-07-10-search-time-contamination.md`; reviewed
  immutable v1 PDF/text paths and hashes are recorded there. Its medical-QA
  audit provides association and partial detector-validation evidence, not a
  reproducible causal inflation estimate or general knowledge-work prevalence.

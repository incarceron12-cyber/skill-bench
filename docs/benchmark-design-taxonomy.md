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

Traceability is necessary but not sufficient. Each arrow is a defeasible
**warrant**: state why the upstream object should support the downstream one,
what evidence supports or contradicts that relation, its scope, owner, and what
claim is blocked when support is absent. Preserve `supported`, `provisional`,
`unsupported`, and `contradicted` states rather than turning a connected set of
schema-valid references into an affirmative validity argument. ECBD makes this
edge-level discipline explicit, but its three purposive, dependent NLP cases,
paper-only evidence view, consensus process without retained coder reliability,
and lack of prospective use mean the discipline remains a design hypothesis to
test—not a certification procedure [ECBD]. The LH cross-record audit demonstrates
the value of the distinction internally: immutable links exist while the
response-view warrant, professional check→calibration-metric bridge, suite
sufficiency, expert validity, matched Skill effect, and readiness remain
unsupported or blocked [EA].

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

### 2.1a Elicitation is an instrumented intervention, not a neutral transcript

An expert statement is conditioned by what the elicitor made salient. Preserve
an unprompted opportunity window before structured or model-generated probes,
then retain an event lineage for candidate generation, priority/randomization,
display, answer, skip/rejection, revision, withdrawal, and follow-up context.
Bind each statement to the source view and stable target shown, question origin,
prompt/model/context identity, contributor confirmation, and correction or
supersession lineage. `responsive_to_question`, textual consistency, contributor
capture approval, source corroboration, scope review, transformation review, and
downstream benchmark utility are separate states [DT].

Data Therapist makes this selection process unusually visible, but its one
expert per condition in three reported domains, internally inconsistent
participant/totals inventory, non-runnable release, and knowledge-difficulty
measure do not identify a tool effect, tacit-knowledge capture, burden reduction,
or downstream validity. Annotation count, topic overlap, specialist scope, and
professionally consequential yield therefore remain separate estimands. A model
may assist dialogue management; it does not inherit authority to verify truth or
approve a benchmark primitive [DT].

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

### 2.4 Evolving evidence is a typed state transition, not a changed answer key

A task's private basis must not collapse every event, source statement, and
professional inference into one omniscient `hidden_truth`. Preserve at least six
separable layers:

1. **world or workflow state:** an event, file, record, policy, or decision and
   the interval in which it holds;
2. **source claim:** who or what asserted a proposition, when, through which
   channel, and with what evidence locator and confidence;
3. **applicability rule:** authority, population/scope, valid time, jurisdiction,
   condition, and whether another claim contradicts, corrects, retracts, or
   supersedes it;
4. **evidence emission and availability:** which task event made the claim
   available to the configured system, without assuming that it was accessed;
5. **access, adoption, and belief delta:** what the trace supports about reading,
   citing, incorporating, retaining, or revising the claim; and
6. **consequential state:** the decision, artifact field, workflow action, or
   check that should change—and the predicates that should remain unchanged.

An authored assumption, motive attribution, expert judgment, policy rule,
objective event, unresolved dispute, and permissible conclusion therefore have
different evidence types. This prevents an author-declared interpretation from
being laundered into objective state while still permitting deterministic
internal calibration cases [CA]. It also refines the retrieval chain in §4.2:
`available`, `accessed`, `visible`, `adopted`, and `effect-estimated` remain
distinct whether evidence arrives over the network, through a message, or as a
workspace mutation.

Use typed update events rather than a generic context append. At minimum,
distinguish an underlying world/workspace mutation, a newly emitted claim about
unchanged state, a correction, a retraction, a temporal supersession, a
policy-version change, and a condition becoming applicable. Static
contradiction, temporal supersession, conditional compatibility, authority
conflict, and non-conflict synthesis are different relations. An update-to-check
crosswalk should bind the prior conclusion, new evidence, changed predicate,
expected belief delta, affected artifact/check, and invariant predicates.
Matched unchanged checks are needed to detect indiscriminate revision.

ClawArena makes persistent evidence emission and workspace updates unusually
inspectable across 337 released rounds, but its truth is internally authored,
its 14-category taxonomy is absent from round records, every round supplies
answer-bearing feedback, preferences are mostly explicit, and most artifact
checks are syntactic. Its one-run, order-sensitive results therefore motivate
this transition contract; they do not validate professional truth, implicit
preference learning, stochastic reliability, or causal skill effects [CA].

### 2.5 A task IR needs independently tested projection obligations

For generated or templated tasks, preserve a versioned compiler lineage:

```text
expert/source evidence → requirement-bearing task IR → sampled instance
  → public instruction + source/environment affordance
  + valid witness consequence + checker predicate
  → cross-projection conformance evidence
```

Shared ancestry is insufficient. Require bidirectional coverage: each public
requirement atom maps to an evidence-backed affordance, at least one valid
witness consequence, and one or more checks; each scored/private predicate maps
back to a fair public basis; each score-relevant environment variable is
disclosed or intentionally discoverable; and legitimate alternative
representations are named as invariances. Hash the IR, sampler, projectors,
dependencies, and rendered outputs separately so drift is localizable rather
than hidden by a shared task ID.

Conformance evidence should include end-to-end witnesses, negative contrasts,
requirement/affordance/witness/check mutations, metamorphic tests for legitimate
equivalence, and adversarial verifier cases. Keep the claims in this chain
separate:

```text
formal feasibility/optimum ≠ executable witness
  ≠ instruction-equivalent witness ≠ verifier completeness
  ≠ professional correctness or deployment readiness
```

Anchor demonstrates a substantial shared-lineage compiler and 300 released ERP
packages, but its CP-SAT model, templates, setup, replay, and large generated
checkers remain distinct hand-maintained translators. No-op and oracle replay
exercise two states, not verifier soundness/completeness; its small expert study
does not adjudicate expert, instruction, UI, and checker failures [AK]. The
implemented optional `task.projection_manifest` therefore treats the IR as an
evidence-backed hypothesis, recomputes projection hashes, enforces four-way
coverage and public basis, and keeps capability/readiness evidence false in its
internal conformance fixture.

### 2.6 Frame, content, assembly, and inference have different denominators

Do not infer suite validity by adding healthy tasks or broad labels. Preserve
four nested but non-equivalent populations:

1. **frame:** eligible domains, occupations, workflows, stakeholders, source
   version, exclusions, and intended weights;
2. **content pool:** represented task families, primitives, artifacts, stakes,
   authors, and gaps within that frame;
3. **administered assembly:** eligibility/exclusion history, selection mechanism
   and seed, lineage clusters, order/replication, intended and realized mixture,
   weighting, missing/invalid policy, cost/stopping rule, and precision target;
4. **inference population:** the configured systems, work, people, organizations,
   decisions, and time period to which the reported interpretation is bounded.

Each transition needs an edge warrant and evidence. Report task-, family-, and
domain/occupation-level estimands separately; compare equal-cell and justified
population-weighted views; cluster repeated samples, criteria, authors, and
shared source lineages; retain ungradable and invalid cases in coverage and
missingness evidence; and test estimate/rank sensitivity to legitimate alternate
assemblies. A reduced panel may preserve rankings while failing construct,
critical-case, or absolute-score coverage.

GDPval demonstrates that broad acquisition is operationally possible—1,320
expert-authored artifact tasks across 44 selected U.S. occupations, with a later
220-task release—but its sector/occupation rule is a frame rather than a
probability sample of work; gold selection is undocumented; five equal-quota
tasks per occupation do not represent occupational frequency or economic
weight; and one human witness plus pairwise preference does not establish an
expert-population ceiling or acceptance threshold [GDP]. Its post-v1 pinned
release is valuable artifact/rubric evidence, not paper-time identity, and most
binary artifacts were not mirrored. ECBD independently identifies assembly as a
missing warrant, but supplies no sampling, cluster, stopping, or sensitivity
machinery and does not estimate how common the omission is [ECBD]. Thus GDP,
wage, duration, frequency, consequence, and equal-task weights are different
estimands; none may be appended after scoring to manufacture economic validity.

The current LH audit makes the boundary concrete: one convenience task, one
source/builder lineage cluster, no alternate assembly, no precision target, and
no cross-domain sample can support suite sufficiency even when its constituent
records validate structurally [EA]. Existing task-health histories hold pool and
selection events, metric specifications hold populations/weights/missingness and
uncertainty, and validity arguments bound inference. Connect these records; do
not add a parallel suite schema until a real multi-task assembly exposes an
unrepresentable obligation.

### 2.7 Professional work is an initial-state-to-consequence contract

Artifact and workflow tasks share one boundary that final-state scoring can
hide. Represent the required work as a sparse transition system:

```text
pinned initial state → public requirement and stage precondition
  → admissible action or artifact mutation → stage postcondition
    → downstream affordance → final decision/artifact consequence
```

For every consequential stage or artifact mutation, preserve: initial absence
or value; required delta and preserved state; alternative valid paths; the
native, executable, rendered, trace, or environment view needed to observe it;
necessity/sufficiency and dependency relations; and invalid-environment versus
substantive-failure semantics. A reference procedure or artifact is one
solvability witness, not proof that its path, layout, formula positions, or
residual state are normative. Process evidence is required only when the stage
itself is part of the construct or the final consequence cannot identify it.

For editable artifacts, static fidelity and counterfactual integrity are
different claims. A workbook, notebook, visualization, or linked report may look
correct now while failing after an authoritative input changes. Its behavioral
contract is:

```text
authoritative mutation → pinned execution/recalculation
  → dependency propagation → changed and invariant checks
    → updated native/rendered views with provenance preserved
```

Record inherited complexity, required mutation surface, preserved regions, and
final complexity separately. Exercise a small set of expert- or source-grounded
metamorphic changes; declare formula/layout equivalence classes; and treat
engine, external-link, circularity, cached-value, chart, and print behavior as
versioned evidence. MBABench's released judge usefully inspects cells, formulas,
and styles, but does not systematically mutate/recalculate artifacts or render
charts and print layouts; one traced dashboard inherits over 20,000 formulas
while adding only 12, and one reference retains external-link residue [MB].
Workflow-GYM independently shows why final state is insufficient: an official
showcase encounters a pre-existing required Anki profile and another exposes
ambiguous `Input`/`input` paths, while the 338-task package, graders, and result
inventory remain unreleased [WG]. These are evidence for transition, residual-
state, and admissibility controls—not finance/GUI scope commitments or portable
professional-capability estimates.

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

### 3.2a Disagreement can be evidence about the instrument or the construct

Before averaging or forcing consensus, follow an identification ladder:

```text
item/evidence defect → rubric comprehension → within-rater stability
  → prospectively declared framework and replicated framework-by-item effect
    → stakeholder decision rule → licensed claim
```

Keep observer judgments, framework-conditioned rationales, aggregation policy,
and professional/readiness claims as different objects. Aggregation must declare
stakeholders, intended use, weights or vetoes, error-loss basis, dissent, and
whether any observer endorses the result. Distinguish resolved specification or
evidence defects from `unresolved_systematic_disagreement`,
`framework_stratified`, `policy_selected_with_dissent`, and
`unresolved_value_conflict`; call disagreement irreducible only after repeat,
framework, context/rubric, and outcome tests fail to explain it [ED].

The reviewed mental-health study is a useful existence proof: three fully
crossed psychiatrists produced very low agreement and coherent directional
patterns on 360 synthetic responses. Three purposively different people, no
repeat ratings, post-hoc framework interviews, a novel mixed rubric, and one
clinical setting cannot identify framework causality or general prevalence.
The synthetic plural-judgment fixture validates policy/lineage machinery only;
it does not establish professional consensus, construct validity, or readiness
[ED, PJ].

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

### 4.3 Workspace evidence is a typed relation, not a path co-occurrence

A persistent workspace has at least seven independently evidenced layers:

1. **availability:** a versioned artifact exists in the declared inventory;
2. **placement and opportunity:** the overlay, path, permission, tool, and valid
   time made it reachable to the configured system;
3. **relevance:** an authored, contestable hypothesis connects the artifact to a
   requirement or decision;
4. **provenance/derivation:** content or state descends from a source through a
   recorded transformation;
5. **observed use:** trace evidence supports access, write, citation, or other
   typed interaction under a declared evidence view;
6. **causal use:** an intervention or sufficiently discriminating evidence
   supports that the source changed a decision or artifact; and
7. **integrity:** pre/post state establishes authorized mutation, protected-state
   preservation, unauthorized additions/deletions, and successful cleanup.

Do not upgrade inventory→access, access→semantic use, or read/write
co-occurrence→causal use. Relevance and dependency graphs are authoring
hypotheses, not cognitive ground truth: type authority, scope, valid time,
contradiction/supersession, conditional branches, and legitimate alternative
paths. Separate relevant-file discovery, interpretation, decision quality,
artifact consequence, and integrity scores. Process claims require trace/state
views; source-content and structural checks require their authoritative artifact
views; missing channels yield `insufficient_evidence`, not failure.

Workspace-Bench motivates this decomposition with 388 authored tasks and a large
simulated file substrate, but its role-skewed convenience assembly, one apparent
run per Lite task/configuration, uncalibrated co-authored graphs/rubrics, mutable
post-v4 implementation, graph/placement defects, and absent result inventory do
not identify workspace learning, causal dependency use, professional validity,
human parity, or Lite fidelity [WB]. Its inspected task 3 has 37 task-local input
files but no verifiable base-workspace placement or execution trace; existence
and an authored graph cannot establish discovery or use [WB].

The optional `task.workspace`/`trial.workspace` records and inert conformance
fixture now pin inventory, placement, permissions/network, mutable/protected
zones, typed relations, trace evidence, mutation authorization, alternative
paths, and cleanup [WC]. Mutation tests reject placement drift, protected or
unauthorized mutation, missing process evidence, causal overclaim, and failed
cleanup. This establishes internal contract behavior only—not expert validity,
capability, causal use, workspace learning, or readiness.

### 4.4 Action safety is an authority-to-consequence chain

An ordinary source may be legitimate to inspect without being authorized to
govern a consequential action. Preserve the chain rather than one attack-success
bit:

```text
source placement and authority → exposure → interpretation/adoption
  → attempted action → interceptor decision → realized state
    → severity/reversibility → detection/recovery/residual harm
      × benign utility
```

Each source/action pair needs an authority rule, allowed and prohibited
consequences, corroboration/escalation policy, and evidence locators. Each action
needs a target, authorization status, tool event, containment decision, and
pre/post state. Non-exposure, safe refusal, blocked attempt, partial harm,
realized harm, repaired harm, secure useful completion, benign-task failure, and
invalid execution are distinct outcomes. Report safety and utility separately;
an unavailable tool or blanket refusal is not evidence of secure useful work.

Containment is part of execution validity: synthetic credentials, mock-only
targets, denied egress, protected-state boundaries, and interceptor behavior
must pass agent-facing canaries before a trial. ClawSafety motivates this model
but its reported ASR lacks utility and an auditable result/scorer inventory; its
post-v2 partial release includes mutable/live Gmail and unrestricted-egress
paths, so the headline rates are not calibration targets [CS]. The repository's
eight-case inert fixture and static preflight demonstrate only contract behavior
for placement/exposure/adoption/attempt/mock realization/recovery and separate
safety/utility counts. They do not probe a live sandbox or establish expert
validity, capability, real-world safety, or readiness [AC].

### 4.5 Keep three change planes separate

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
| Evidence-state transition record | separate evolving world state, emitted claims, applicability, access/adoption, belief revision, and artifact consequence | authority/scope/valid-time, contradiction/supersession, update-to-check crosswalk, changed and invariant predicates |
| Task projection manifest | detect drift among public requirements, affordances, witnesses, and checks | evidence-backed requirement atoms, IR/sampler/projector/output hashes, bidirectional coverage, declared invariances, solver/validity separation, conformance tests |
| Suite assembly argument | distinguish a broad frame and healthy pool from the administered sample and licensed population inference | frame/content exclusions, eligible pool, selection/seed/order, lineage clusters, intended/realized mixture, weights, precision/stopping, invalid/missing policy, alternate-assembly sensitivity, bounded claim |
| Persistent-workspace record | distinguish file presence and authored relevance from observed or causal use while preserving state integrity | inventory/overlay hashes, placement and valid time, permissions/network, typed and alternate relations, evidence-view-bound access/write, protected/mutable zones, pre/post mutations, cleanup |
| Sparse workflow-transition record | distinguish one witness path and final state from run-attributable stage completion | pinned initial state, pre/postconditions, alternative paths, necessity/sufficiency, state delta, evidence views, downstream consequence, invalid-environment policy |
| Counterfactual artifact record | establish editability and behavioral integrity rather than current-value similarity | native/executable/rendered/trace views, pinned engine, initial-to-final mutation surface, authoritative perturbations, dependency propagation, invariants, permitted formula/layout equivalence, witness health |
| Action-safety record | distinguish source presence, attempted behavior, realized consequence, recovery, and useful completion | authority matrix, placement/exposure/adoption evidence, tool event, interceptor, pre/post state, severity/reversibility, residual harm, containment canaries, separate safety/utility outcomes |

A reduced panel serves **ranking efficiency**, not automatically diagnostic
coverage or absolute professional-quality estimation. Mid-range checks often
carry the most rank information, while rare hard safety/contradiction checks may
be strategically indispensable. Keep separate panel objectives and report rank
fidelity separately from score calibration [EB, AP].

## 6. Family map: what each benchmark pattern contributes

| Pattern / examples | Primary reusable object | Main validity risk | Evidence status here |
|---|---|---|---|
| Artifact-centered professional work (AA-Briefcase, MBABench, WorkstreamBench) | plural native/executable/rendered views, initial-to-final mutation surface, counterfactual integrity, and professional judgment | reference imitation, static-value coincidence, inherited-size inflation, unobservable charts/layout, engine drift, and weighted score mistaken for readiness | MBABench full immutable v4 paper plus inspected post-v4 code/data and two workbook traces [MB]; other family members remain landscape/triage |
| Stateful professional workflow (SaaS-Bench, Workflow-GYM, OdysseyBench) | pinned initial state, sparse consequential stage transitions, alternative paths, final-state and artifact checks | residual/pre-satisfied state, stage bypass, canonical-path bias, environment/harness defects, and final consequence mistaken for complete workflow evidence | Workflow-GYM full immutable v3 paper plus post-v3 official showcase/trajectory inspection, with full dataset/VMs/graders/results unavailable [WG]; SaaS-Bench has a separate full review; OdysseyBench remains landscape-level |
| Adversarial authority and action safety (ClawSafety) | source-authority matrix, exposure/adoption/action-state ledger, containment, recovery, and benign utility | source placement or token match mistaken for adoption/realized harm; refusal or tool failure counted as safety; mutable/live side effects | full immutable v2 paper plus complete post-v2 partial-release audit [CS]; internal inert conformance fixture/preflight validates contract behavior only [AC] |
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
| Evolving-information workspace evaluation (ClawArena) | evidence-emission/update map, persistent workspace state, and update-to-check crosswalk | authored omniscience, untyped claim transitions, answer-bearing feedback, explicit preferences, mostly syntactic checks, unsafe shell execution, one-run order effects | full immutable v2 paper plus inspected official v1.0.0 and later release with timing boundaries; 337 rounds and 327 checker scripts audited, not professional-truth or reliability evidence [CA] |
| Single-specification task generation (Anchor) | versioned task IR, four projection types, solver witness, and cross-projection conformance tests | omitted professional rules propagate consistently; translator drift; canonical witness mistaken for completeness; public oracle/check leakage; mutable environment | full immutable v1 paper plus inspected one-day-post-v1 official release; all 300 packages statically audited and two lineages traced, not semantic-equivalence or professional-validity proof [AK] |
| Evidence-centered design (ECBD) | edge-level intended-use→construct→content/treatment→assembly→response/score warrants | completed worksheet mistaken for support; paper-only evidence view; assembly named without sampling machinery; reviewer consensus mistaken for reliability | full immutable v1 paper and complete pinned worksheets; three purposive dependent NLP cases, no prospective framework validation or independent-review reliability [ECBD] |
| Occupational artifact portfolio (GDPval) | explicit occupational frame, expert acquisition pipeline, multimodal witness artifacts, separate frame/content/assembly/inference denominators | equal task quotas laundered into work/economic representativeness; one witness treated as expert ceiling; pairwise preference treated as acceptance or productivity | full immutable v1 paper plus parsed 220-task post-v1 pinned release and one workbook pair; no probability sample, gold-selection record, augmentation trial, expert-population baseline, or release license [GDP] |
| Persistent file workspace (Workspace-Bench) | workspace identity/placement, typed relevance and provenance hypotheses, alternate paths, observed-use and integrity records | scale or authored graph treated as causal use; task-local injection/placement ambiguity; judge-view mismatch; unclustered single runs and mutable releases | full immutable v4 paper plus pinned post-v4 code/data audit and 37-file targeted task trace; no base-workspace replay, immutable result inventory, professional validation, Lite-fidelity, or workspace-learning identification [WB] |

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
20. **Hidden truth is decomposed and defeasible:** objective state, source claims,
    authority/scope/valid-time rules, authored assumptions, expert judgments, and
    unresolved disputes remain distinct; an update changes only the predicates
    supported by its typed relation and evidence.
21. **Shared generation lineage is not conformance:** every requirement,
    affordance, witness consequence, and check has bidirectional coverage and
    independently hashed/tested projections; solver or oracle success does not
    license verifier completeness, professional correctness, or readiness.
22. **Breadth has explicit denominators:** frame, content pool, administered
    assembly, and inference population remain separate; labels, equal quotas, or
    a healthy task count do not establish occupational, economic, cross-domain,
    or readiness generalization.
23. **Dependency graphs are hypotheses, not cognition:** separate availability,
    placement, relevance, provenance, observed use, causal use, alternatives, and
    integrity; a path read/write match cannot silently promote a causal claim.
24. **Human artifacts and judgments have distinct authority:** one expert witness
    can establish a feasible route and one pairwise judgment can establish a
    preference observation; neither is an expert-population ceiling, an
    acceptance threshold, or an economic-value estimate.
25. **Final state does not prove the transition:** pin initial state and grade
    sparse consequential deltas with alternative paths and admissible views;
    inherited or pre-satisfied state, stage bypass, and environment ambiguity do
    not become agent progress.
26. **Editable artifacts are behavioral systems:** current values and formula
    presence do not establish counterfactual integrity; independently test native,
    executable/recalculated, rendered, and trace views under declared mutations
    and equivalence classes.
27. **Safety retains both consequence and utility:** source placement, exposure,
    adoption, attempt, interception, realization, recovery, and benign completion
    remain separate; refusal, non-exposure, blocked action, and invalid execution
    are not interchangeable evidence of safe useful work.
28. **Elicitation provenance is part of the evidence:** spontaneous testimony,
    human/model/framework probes, revisions, rejections, and withdrawals remain
    distinguishable; responsiveness or annotation volume is not corroboration.
29. **Consensus is not the default truth operation:** test evidence, rubric,
    stability, and framework explanations before aggregation; any policy-selected
    result retains dissent, stakeholders, loss basis, and claim limits.
30. **Memory QA is not action transfer:** separate storage, retrieval,
    representation, reader, and grader effects from held-out behavioral benefit;
    stale or failed-run lessons require scope, contradiction, harm, and rollback
    evidence before promotion.

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
| Stable belief vs justified revision under evolving evidence | ClawArena operationalizes staged messages/files and reversals, but authored truth, detailed forward feedback, fixed order, and absent claim-level transition records confound retrieval, adoption, revision, and transfer [CA]. | Plant typed correction, supersession, conditional-applicability, and irrelevant-update cases; log availability/access/adoption; require changed and invariant checks; cross feedback policy with reset and held-out equivalent forms. |
| Single-source coherence vs propagated specification error | Anchor's compiler aligns generated identifiers and accepts its oracle, but omitted rules and translator/checker assumptions can remain consistently wrong [AK]. | Mutation-test each projection edge, include legitimate alternate witnesses and adversarial partial-credit states, obtain independent expert adjudication, and report formal, executable, instruction-equivalent, verifier, and professional-validity gates separately. |
| Broad frame vs representative suite and bounded inference | GDPval operationalizes broad occupational acquisition, while equal quotas, undocumented gold selection, restricted one-shot digital artifacts, and unobserved task frequency do not support occupational/economic inference; ECBD identifies the assembly warrant but does not supply estimators [GDP, ECBD]. | On a multi-domain pool, predeclare frame/content exclusions, lineage clusters, intended weights and precision; compare equal-cell and population-justified estimands under alternate assemblies, retain invalid/ungradable cases, and measure task/family/domain uncertainty before claim upgrades. |
| Workspace dependency score vs evidence use and integrity | Workspace-Bench makes large workspaces and authored graphs inspectable, but graph matching confounds availability, canonical relevance, harness observability, alternate paths, and causal use; post-v4 release defects also leave placement and reset uncertain [WB]. | In a persistent pilot, plant authoritative/obsolete/distractor/alternate/protected paths; canary placement and clean state; cross observed access with source masking or matched alternatives; grade decision consequence and protected-state integrity separately [WC]. |
| Connected record graph vs supported validity argument | The LH evidence-chain audit resolves immutable nodes yet finds unsupported response-view and claim bridges, a contradicted professional-check→synthetic-metric edge, and no suite sufficiency [EA]. | Have independent reviewers audit a real multi-task, expert-reviewed pilot; retain initial edge states, disagreements, time, defects and false alarms, then test whether edge auditing contracts claims beyond existing validation [ECBD]. |
| Static artifact fidelity vs counterfactual integrity | MBABench catches formula and structural defects that value-only grading misses, but its judge does not systematically perturb/recalculate workbooks or observe charts and print layout; references and engines also contain residue and differ [MB]. | For one editable artifact, predeclare authoritative mutations and invariant regions; execute them under pinned engines; compare native, dependency, recalculated, and rendered views; include equivalent formulas/layouts and fallible-reference cases. |
| Final-state success vs valid professional transition | Workflow-GYM supplies long expert witness paths but no released task/check package, and its official showcases expose a pre-existing required object and ambiguous input placement [WG]. | Canary initial absence, unique placement, and clean output; define sparse stage pre/postconditions and alternative paths; compare stage evidence with final consequences while quarantining invalid environments. |
| Binary attack success vs safe useful completion | ClawSafety measures completed harm without benign utility and its partial post-v2 release lacks an executable ASR scorer while retaining live/mutable side-effect paths [CS]. The internal action fixture proves only inert contract behavior [AC]. | Cross source authority and exposure with mock-only action opportunities; retain attempt/interception/realization/recovery and utility separately; repeat under agent-facing containment canaries and expert-reviewed consequence thresholds. |
| Elicitation yield vs valid expertise transfer | Data Therapist increases inspectable candidate production, but expert identity, probe/interface treatment, unsupported model checks, and absent downstream tests confound quality and utility [DT]. | In one consented session, preserve unprompted then probed phases and the full event ledger; compare corroborated, scope-valid, consequence-bearing primitives and correction/review burden rather than annotation count. |
| Consensus label vs plural professional judgment | One three-psychiatrist panel shows strong systematic disagreement but cannot separate person, framework, rubric, or context effects; the internal fixture proves only aggregation-contract behavior [ED, PJ]. | Repeat held-out ratings, prospectively declare frameworks, replicate experts within framework, vary context/rubric evidence, and compare explicit stakeholder policies while preserving dissent and claim blocks. |
| Retrospective memory QA vs consequential action transfer | LongMemEval-V2 cleanly evaluates bounded evidence delivery but representation/reader/grader effects remain treatment components and no acting agent uses the memory [LM]. | Compare no-memory, evidence-only, and provenance-gated lessons on equivalent-form QA and held-out artifact/state action; plant stale, failed-attempt, contradiction, safe-alternative, harmful-transfer, and rollback cases. |

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
   `build-artifact-view-admissibility-slice`:** task checks now declare
   authoritative representations, required views and controls, permitted
   invariances, evidence sufficiency, and fail-closed outcomes. The synthetic
   cross-artifact fixture validates the contract, not cross-domain construct
   validity or grader reliability.
11. **Evidence-gated elicitation contract — `build-elicitation-session-contract`:**
    wait for one consented real contribution before encoding session evidence
    types; do not simulate testimony to satisfy a schema dependency.
12. **Completed projection-conformance slice —
    `build-task-projection-conformance-slice`:** the optional task projection
    manifest now hashes requirement atoms, IR, sampler, four projector/output
    pairs, and enforces bidirectional coverage, public basis, declared
    invariances, selection history, and typed conformance evidence. Its Anchor-
    grounded fixture and mutation tests establish internal contract behavior
    only, not expert validity, verifier completeness, capability, or readiness
    [AK].
13. **Completed cross-record application, not ECBD validation —
    `build-lh-ecbd-cross-record-audit`:** `pilots/lh-skill-adoption/evidence-chain-audit.json`
    links immutable intended-use→construct→requirement/affordance→response-view→
    grader→metric→claim records and fails closed on unsupported and contradicted
    edges. The one-task suite, response-view sufficiency, expert validity,
    matched Skill effect, cross-domain generalization, and readiness remain
    unsupported or blocked [EA].
14. **Completed persistent-workspace conformance, not workspace capability —
    `build-persistent-workspace-conformance-slice`:** optional task/trial records
    now exercise inventory, placement, typed and alternate dependency relations,
    trace-supported access/write, mutation authorization, protected state, and
    cleanup. The inert fixture and mutation tests establish contract behavior
    only; causal use, workspace learning, expert validity, capability, and
    readiness remain false [WC].
15. **Completed inert action-safety conformance, not real-world safety —
    `build-adversarial-action-conformance-slice`:** optional action-safety records
    now separate authority, placement, exposure, adoption, attempted/mock-realized
    action, recovery, residual harm, invalidity, and benign utility. The eight
    synthetic cases and static preflight establish validator/adapter behavior
    only; they do not probe a live host boundary or establish expert validity,
    capability, safety, or readiness [AC].
16. **Completed second pilot package and one bounded execution —
    `build-second-cross-domain-pilot` / `build-vendor-incident-isolated-agent-trial`:**
    the vendor-incident package reused bundle, expertise-transfer, workspace,
    action-safety, and evidence-chain machinery without a schema fork. One pinned
    isolated attempt passed its preflight and preserved protected state, but its
    invalid-time judgment exposed a possible task/grader validity defect. This is
    one diagnostic observation, not reliability, cross-domain generalization,
    professional validity, treatment effect, real-world safety, or readiness.
    Preserve the original score and use the queued versioned adjudication/retest
    rather than interpreting the behavior as capability evidence.
17. **Completed plural-judgment conformance, not professional consensus —
    `build-plural-judgment-conformance-slice`:** framework-indexed observations,
    explicit policy aggregation, dissent, and blocked claim upgrades are
    executable. The synthetic cases establish validator behavior only [ED, PJ].
18. **Pending evidence-to-action bridge —
    `build-experience-memory-transfer-conformance`:** connect trajectory-derived
    evidence to both equivalent-form QA and held-out action while testing stale
    or harmful transfer and rollback. Reuse existing contracts; LongMemEval-V2
    does not itself supply action-transfer evidence [LM].

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
- **[CA]**
  `papers/agent-benchmarks/2026-07-10-clawarena-evolving-information.md`;
  reviewed immutable v2 PDF/text and inspected official v1.0.0 plus later
  release paths/hashes are recorded there with explicit timing boundaries. The
  review audited all 337 round records and 327 checker scripts; this is
  instrument evidence, not expert validation of its authored hidden truth.
- **[AK]**
  `papers/agent-benchmarks/2026-07-10-anchor-artifact-drift-generation.md`;
  reviewed immutable v1 PDF/text and inspected one-day-post-v1 official release
  paths/hashes are recorded there. All 300 task packages were statically audited
  and two projection lineages traced; shared lineage and oracle replay do not
  establish semantic equivalence, verifier completeness, or professional
  validity.
- **[ECBD]**
  `papers/agent-benchmarks/2026-07-10-ecbd-evidence-centered-benchmark-design.md`;
  reviewed immutable v1 PDF/text and complete pinned worksheet release paths and
  hashes are recorded there. The three purposive, dependent NLP cases expose
  missing design warrants but do not validate the framework prospectively,
  estimate prevalence, or establish independent-review reliability.
- **[GDP]**
  `papers/agent-benchmarks/2026-07-10-gdpval-occupational-task-validity.md`;
  reviewed immutable v1 PDF/text plus the pinned post-v1 220-task release and
  workbook inspection are recorded there. Most binary artifacts and paper-time
  results were not mirrored/released; the evidence does not establish task-
  frequency sampling, expert-population parity, economic impact, augmentation,
  or deployment readiness.
- **[WB]**
  `papers/agent-benchmarks/2026-07-10-workspace-bench-file-dependency-validity.md`;
  reviewed immutable v4 PDF/text plus pinned post-v4 code/dataset and targeted
  task-3 release paths/hashes are recorded there. The release is not manuscript-
  time identity, and no base-workspace replay, stable result inventory, causal
  dependency-use estimate, Lite-fidelity proof, or professional validity exists.
- **[EA]** `pilots/lh-skill-adoption/evidence-chain-audit.json`; internal
  builder-authored cross-record audit with pinned local artifact hashes and
  explicit unsupported/contradicted edges. It calibrates audit structure, not
  ECBD effectiveness, expert validity, Skill efficacy, suite validity, or
  readiness.
- **[WC]** `schemas/README.md` (Persistent-workspace conformance),
  `tests/fixtures/valid-persistent-workspace-conformance.json`, and
  `tests/test_validate_benchmark.py`; inert internal fixture and mutation tests
  grounded in [WB]. They establish validator behavior only, not causal use,
  workspace learning, professional capability, or release readiness.
- **[MB]**
  `papers/agent-benchmarks/2026-07-11-mbabench-spreadsheet-artifact-validity.md`;
  reviewed immutable v4 PDF/text plus inspected post-v4 code, pinned 38-task
  dataset manifest, and two workbook traces are recorded there. Raw attempts,
  expert labels, perturbations, results, and paper-time implementation were not
  released; static criterion evidence does not establish editability or
  professional readiness.
- **[WG]**
  `papers/agent-benchmarks/2026-07-11-workflow-gym-professional-state-validity.md`;
  reviewed immutable v3 PDF/text plus the official post-v3 project-site snapshot
  and 24 showcase trajectories are recorded there. The 338 tasks, VMs,
  initialization, graders, scores, and result inventory were unavailable.
- **[CS]**
  `papers/agent-benchmarks/2026-07-10-clawsafety-cross-domain-injection-validity.md`;
  reviewed immutable v2 PDF/text and complete post-v2 partial-release inspection
  are recorded there. Reported ASR denominators and results are unauditable from
  the release, which does not supply an executable safety scorer or inert-only
  side-effect boundary.
- **[AC]** `schemas/README.md` (Inert adversarial-action conformance),
  `tests/fixtures/valid-adversarial-action-conformance.json`, and
  `tests/fixtures/action-safety-preflight-report.json`; eight builder-authored
  synthetic cases and static preflight grounded in [CS]. They establish internal
  contract behavior only, not a live sandbox, expert validity, agent capability,
  real-world safety, or release readiness.
- **[DT]**
  `papers/agent-benchmarks/2026-07-11-data-therapist-tacit-knowledge-elicitation.md`;
  reviewed immutable v3 PDF/text and inspected paper-linked OSF materials are
  recorded there. The source exposes mixed-initiative elicitation mechanics but
  does not identify capture fidelity, burden reduction, or benchmark utility.
- **[ED]**
  `papers/agent-benchmarks/2026-07-11-expert-disagreement-human-feedback-validity.md`;
  reviewed immutable v3 PDF/text and complete pinned rating release are recorded
  there. The three-rater clinical panel establishes bounded instrument
  instability, not universal or irreducible expert disagreement.
- **[PJ]** `schemas/PLURAL_JUDGMENT.md`,
  `schemas/fixtures/plural-judgment-conformance.json`, and
  `tests/test_plural_judgment.py`; internal synthetic conformance evidence only.
- **[LM]**
  `papers/agent-benchmarks/2026-07-11-longmemeval-v2-environment-experience-memory.md`;
  reviewed immutable v1 PDF/text plus pinned code and dataset release are
  recorded there. Results concern retrospective evidence QA, not held-out action
  benefit, stale-memory safety, professional competence, or readiness.

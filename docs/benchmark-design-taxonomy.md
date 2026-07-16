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

### 2.1a Authority gates and nulls apply at claim level

A contributor's role is not blanket authority over a workflow. For each claim,
record the knowledge layer and decision right it requires; the contributor's
scope, protocol relationship, evidence basis, and allowed use; and an explicit
`unknown`, `not_authorized`, `disputed`, or `not_applicable` state when the gate
is not met. A protocol operator may be authoritative about an execution symptom
while unauthorized to infer design rationale or approve a consequential hidden
check. Missing authority must remain null rather than being plausibly completed
by an interviewer, model, graph editor, or benchmark author [LWT].

Preserve the complete projection chain rather than attaching only a contributor
name to the final assertion:

```text
testimony/source span + prompt/probe + channel
  → claim wording, type, context, valid time, and disagreement
    → correction/transformation/approval events
      → graph or other intermediate view
        → task requirement/public basis → artifact/check projection
          → trial observation → bounded interpretation
```

Every edge needs its own author, timestamp, evidence locator, disposition, and
purpose/consent/use boundary. Provenance, correction, approval, and permission
to reuse testimony in an agent-visible intervention or private evaluator are
non-substitutable. A query that returns an encoded edge establishes
representational executability, not the claim's truth, completeness, currency,
consensus, causal validity, or professional use [LWT].

The laboratory workflow-twin study supplies a useful role-gated extraction
design and mandatory null pattern, but its evidence is four reported assay
sessions in one department, with proprietary prompts/load files and no released
transcripts, claim-level transformations, graph instances, independent ground
truth, operational outcome study, or cross-domain transfer test. Its language-
derived confidence values are therefore neither calibrated probabilities nor
benchmark weights [LWT]. Existing expertise-transfer, participation, evidence-
state, projection, and validity records are the implementation homes; this does
not justify a graph ontology or professional-validation claim.

### 2.1b Elicitation is an instrumented intervention, not a neutral transcript

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

A simulated interlocutor is the same class of intervention, not a substitute
expert, client, or ground truth. Preserve challenge/profile provenance and
sampling, simulator prompt/model/settings, requested and realized resistance,
utterance-linked expert statements, skips/deletions/revisions, stopping reason,
actual burden, and every downstream transformation. Begin with an unprompted
incident before disclosed `SIMULATED_PROBED` friction such as a failed prior
attempt, conflicting constraint, adverse consequence, or request for when not to
use the advice. Contributor read-back must separate representative cues from
role-play artifacts [SI]. Dialogue length and fluency are not expertise yield;
participation value, privacy/consent, grounded novelty, correction burden, and
held-out task/check utility are different outcomes. SimInstruct's 18 paid experts,
123 retained dialogues, and randomized persona effect establish instrument
reactivity and bounded feasibility in one higher-education network—not tacit-cue
capture, burden reduction, near-zero-cost recruitment, or real-user validity [SI].

### 2.1c An artifact edit is evidence of a delta, not an approved domain claim

Before/after native artifacts can expose expertise that an interview misses, but an
edit is not self-interpreting. Preserve immutable objects and dispositions along:

```text
artifact versions + interaction mode → exact delta + contributor rationale
  → model/analyst candidate interpretations → contributor accept/correct/reject
    → scope, authority, valid time, contradiction, and allowed use → promotion
      → selection/delivery → recipient adoption or justified rejection
        → changed artifact/action → independent consequence and burden
```

Type direct edits, participant prompt intent, model-generated deltas, and
model/analyst inferences separately. A direct edit may encode style, local
preference, factual correction, experiment, or deletion; a prompt-regenerated
artifact is jointly produced. Neither source proximity nor an `expert` role prompt
transfers contributor authority to an interpretation. Keep capture denominators
(eligible edits through accepted/promoted claims) separate from use denominators
(opportunities through delivery, adoption, effect, regression, expiry, and burden).

The reviewed five-person fixed-order study supports storage of artifact deltas and
model-generated candidate entries only. Pending expertise verification, absent
contributor approval and executed context/trace evidence, confounded accumulation,
and a partial mutable OSF snapshot block extraction-validity, tacit-transfer,
quality, burden, and cross-domain claims [CMDA]. Existing expertise-transfer,
participation, intervention, longitudinal, metric, and validity records are the
implementation homes; do not create an edit-memory subsystem.

### 2.1d Participation mechanisms need realized treatment and welfare evidence

A formal payment or allocation rule is a design object, not evidence that experts
participated, exerted the intended effort, or produced a more valid benchmark. Keep
five non-inheriting layers:

```text
declared mechanism and assumptions → immutable implementation witness
  → realized assignment/pay/audit/appeal treatment → participant behavior and burden
    → independently adjudicated contribution quality → benchmark validity and use
```

For every contribution unit, bind eligibility and consent; information and action
rights; assignment probability; complete payoff, penalty, audit, appeal, and
withdrawal rules; observed opportunity and effort proxies; accepted/rejected/revised
artifacts; payment and time; disputes, attrition, concentration, and reciprocal
value. A theorem over latent effort and noisy scores requires an **instantiation
witness** that maps every variable and assumption to versioned implementation and
event records. An audit cannot be both an unrecorded treatment change and the
outcome authority used to attribute a pay effect.

KINA's bonus-on-bar tournament states useful sufficient assumptions, but the actual
system adds audits, penalties, appeals, scarcity pricing, and a whitelist, while its
flat-versus-tournament comparison also changes audit regime and time. Scores, costs,
assignments, payments, audits, contributor histories, and welfare are unreleased
[KINA]. ELAIPBench supplies a realized writer–verifier contest but no formal game or
fixed-pay contrast; neither source establishes an incentive effect, contributor
benefit, affordability, or retained-item validity. **Invariant:** mechanism claims
stop at the strongest realized and independently observed link. **Validation
experiment:** only after a consented real contribution is authorized, preregister
comparable units randomized between fixed audit plus adequate base pay and the same
audit plus a validity-gated bonus; preserve independent quality, false challenge,
minutes, earnings, burden, attrition, disputes, and cost. Existing participation,
expertise-transfer, task-health, metric, and validity records are the durable homes;
no synthetic participant or incentive schema follows.

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

### 2.2a Problem recognition is staged inference, not final-artifact failure

Some professional work begins before a named workflow: the agent must notice that
the surface request or apparent state is incomplete, anomalous, or governed by a
different problem. Preserve the chain as independently observable stages:

```text
surface situation → decisive and disconfirming cues → candidate/alternate frames
  → targeted inquiry → action selection → artifact or state consequence
```

Do not infer the first stages from the last. A failed artifact can reflect domain
knowledge, execution, tool, or grader failure; a correct artifact can arise from a
template or indiscriminate skepticism. Each private candidate-problem record
therefore needs cue provenance, scope/severity, competing frames, positive and
negative near neighbors, alternate-valid-path policy, and stage-specific checks.
Use matched situation-only, minimal-frame, and fully specified conditions with
repeated, task-clustered analysis. The situation-only→minimal-frame contrast is a
**recognition intervention**; procedural guidance and evaluator/rubric disclosure
are separate treatments and must remain independently versioned [KW].

KWBench makes this missing construct explicit and usefully designs backward from
plausible wrong path to cue and consequence. Its cold condition nevertheless
mixes recognition, inquiry, domain judgment, action, and artifact execution; its
single model judge, best-of-three selection, opaque expert provenance, and absent
framed/near-neighbor/human conditions do not isolate recognition [KW]. The
internal six-cell replay exercises staged labels, positive/negative neighbors,
and invalid-environment abstention, but all responses and expected outcomes are
builder-authored and deterministic. It establishes instrumentation behavior only,
not expert validity, agent capability, a treatment effect, prevalence, or
cross-domain generalization [PR].

#### Targeted inquiry includes an interface-realization boundary

Do not score an evidence request as if the agent's latent information need moved
directly into its context. Preserve the independently observable chain:

```text
available evidence graph → selected evidence target → expressed request and scope
  → parser/router interpretation → access decision and realized release
    → model-visible payload → adoption or rejection → stop/action → consequence
```

The parser, aliases, request schema, clarification behavior, access delay/denial,
and budget charges are configured environment components. A semantically relevant
free-text request can fail at expression or deterministic routing even when the
target was appropriate; a structured syntax can constrain expression but still be
unrealizable against a private parser vocabulary, while a menu can leak the
candidate set or answer. Therefore record raw request, intended target and
expected-value basis, parser identity/version, mapped candidates and confidence,
access transition, released content locator, adoption evidence, and endpoint
separately. Ambiguous, malformed, synonym, multi-target, and negative-control
requests must fail closed rather than silently map to one evidence atom. Compare
interfaces prospectively on frozen evidence graphs, budgets, policies, configured
systems, and graders before attributing endpoint differences to inquiry quality.

The internal matched evidence-acquisition slice retained 12/12 valid configured-
agent attempts across two purposive synthetic shapes [EAI]. Both active
vendor-disposition attempts routed two requests, adopted both released records,
and passed; both active segment-release attempts failed the six-check endpoint
instrument after the deterministic free-text parser mapped controlling-metric
requests ambiguously (one attempt later obtained one of two required records).
All eight supplied-information controls passed. This demonstrates that the
contract can preserve request→parser→access→adoption→endpoint evidence and exposes
a candidate interface failure; with two repeats per cell, different synthetic
shapes, and no matched interface ablation, it does **not** identify agent inquiry
ability, parser causality, an information-supply effect, expert/professional
validity, cross-domain generality, safety, or readiness.

The prospective v2 interface study then retained 8/8 valid attempts in a frozen
two-shape × two-interface × two-repeat active-only matrix [ERI]. Across the four
structured attempts, all six emitted requests were syntactically valid, but all
six were unmatched by the undisclosed frozen exact-synonym map; no evidence was
released. Across the four natural-request attempts, eight requests produced five
matches and three ambiguous parses, five releases, and five terminal citations to
released IDs. Citation is an adoption proxy only. Preserve the shape-specific
endpoints rather than pooling: vendor-disposition natural requests passed at 1.0
quality with zero decision loss in both repeats, whereas structured requests scored
0.667 with decision loss one in both; segment-release natural requests scored
0.833/zero and 0.667/one, while structured requests scored 0.667/one and 0.833/zero.
Thus endpoint direction was stable only within the purposive vendor shape and was
not a measure of inquiry quality.

This result separates an agent's selected and expressed topic from whether that
topic is realizable in the configured interface vocabulary. It observes parser and
access consequences, not the semantic quality of topic selection, a counterfactual
under another structured vocabulary, belief adoption beyond terminal citation, or
a stable interface effect.

The subsequent frozen v3 study implemented the proposed non-answer-bearing
interpretation receipt and one bounded repair while retaining the natural-request
condition, same semantic parser, byte-identical scenarios, budget, release rules,
six-check endpoint grader, and two purposive repeats per shape [ERR]. All 8/8
attempts replayed as service-, environment-, and artifact-valid. In
vendor-disposition, both conditions emitted two matched requests, released and
terminally cited the same permit and insurance records, and passed at 1.0 quality
with zero decision loss in both repeats; the receipt condition needed no repair. In
segment-release, each receipt/repair attempt first combined two topics, received an
`ambiguous` receipt, then repaired once to the adjusted-quality audit. Both natural
and receipt/repair conditions nevertheless released and terminally cited the same
single audit record and scored 5/6 (0.833) with zero decision loss in both repeats;
all four omitted the metric dictionary.

This is evidence that a receipt can make the parser's interpretation observable and
that the bounded recovery transition is executable, **not** that it improves
evidence access or endpoints. Keep request, receipt, repair, release, terminal-
citation proxy, stopping, endpoint, and cost separate: reported dollar cost was
zero, but the retained attempts consumed 14,757–34,980 tokens each (213,223 total),
and receipt/repair used more tokens in every matched pair. Do not pool the two
purposive shapes or infer inquiry quality from the shared endpoints. Across v2 and
v3, structured syntax, interpretation feedback, and repair are distinct configured-
interface interventions; none establishes semantic selection quality, belief
adoption, a stable causal interface benefit, capability, expert/professional
validity, population or cross-domain generality, compliance, safety, production
fitness, deployment, or readiness.

### 2.2b Professionally correct non-completion is a counterfactual action contract

A request to produce an artifact is not always an obligation to complete it.
Represent stop, refuse, escalate, clarify, revise, preserve, and proceed as
first-class terminal actions when disclosed evidence and professional duties make
them legitimate. Author the decision boundary as:

```text
apparent action + requesting authority → observable disqualifying evidence
  → threshold and legitimate alternatives → selected substantive action
    → required state/communication consequences + prohibited collateral harm
```

The record must preserve the action that would have been appropriate absent the
disqualifying evidence; evidence locator, visibility, authority, and strength;
decision threshold and uncertainty; permissible alternatives; abstention or
escalation conditions; state that must change or remain unchanged; recipient and
communication obligation; and prohibited cost, disclosure, fabrication, or other
harm. Keep decision correctness, rationale evidence, artifact-state preservation,
communication quality, resource use, and collateral harm as separate observations.
Substantive refusal is not a keyword match, and a well-worded dissent does not
prove that the prohibited action was avoided.

Every stopping form needs a matched case where persistence is correct; every
dissent form needs a matched case where compliance with legitimate authority is
correct. Vary evidence strength and authority legitimacy so the estimand is
calibrated action selection rather than generic caution or contrarianism. Admit
professionally equivalent realizations and test lexical or model graders with
positive paraphrases, semantically wrong keyword-bearing negatives, and retained
false-accept/false-reject adjudications. AARRI supplies 82 inspectable authored
research episodes and directly demonstrates one regex false rejection, but no
sampling frame, contributor inventory, expert/novice contrast, human baseline,
agreement, repeated trials, clustered uncertainty, verifier-wide audit, exact
configuration record, contamination-safe split, environment canaries, or
paper-pinned release [AA]. Treat its incidents and action categories as design
hypotheses, not validated researcher-quality measures or a research-domain scope
commitment.

**Invariant:** a completion score must never encode professionally correct
non-completion as ordinary failure, and no lexical check may stand in for the
substantive action or preserved consequence. **Validation experiment:** construct
matched persist/stop and comply/dissent forms, cross authority legitimacy and
evidence strength, then measure action, state, communication, harm, lexical-grader
confusion, and semantic adjudication separately with task-clustered repeats.
Existing task/check, artifact/state, action-safety, trace, task-health, metric, and
validity records are the implementation homes; this evidence does not justify a
parallel schema or pilot.

#### Authorization ambiguity is not evidence insufficiency

A fixed private intended transition may cease to be justified when a prompt hides
the action, object, scope, or environment attributes that publicly license it.
Record `private_intent`, `public_authorization`, `resolvable_uncertainty`, legitimate
terminal actions, attempted action, realized effect, observer coverage, and verdict
independently. `insufficient_evidence` means the observer cannot support a verdict;
`authorization_ambiguous` means the agent-visible basis does not license one unique
action. Neither is ordinary failure, and neither makes the other true [US].

Cross specificity with authority completeness and consequence/permission policy.
Include matched cases where inspection resolves uncertainty, clarification is
required, conservative action is licensed, refusal/escalation is required, and
unnecessary asking has cost. Report useful completion, calibrated clarification,
over-refusal, wrong target, excess scope, invalid execution, and acted-run quality
separately. UnderSpecBench's fixed-world matrix motivates this contract, but its
unvalidated transformations, fixed private oracle, single permissive policy,
apparent one-shot cells, and unavailable release support only a synthetic stress-
test pattern—not professional or deployment safety [US]. Existing authority,
action-safety, trace, evaluator-observation, metric, and validity records suffice.

### 2.2c Framing ambiguity is a public-set intervention, not a hidden-answer test

An executable package can still leave several consequential interpretations
compatible with the public evidence. Do not let one private reference framing
silently become the only correct answer. Represent the intervention as:

```text
full public package + admissible-framing set
  → immutable ambiguity edit and projection hashes
    → unresolved variable and decision-relevant consequences
      → resolvable inspection or authority-dependent clarification
        → recognition → disclosure → question → authority routing
          → answer/evidence uptake → commitment/action → artifact/state consequence
```

Before trials, blind-review at least two public-basis-compatible framings and show
that resolving the omitted variable changes a target, objective, threshold,
artifact semantics, cost, safety boundary, or stakeholder consequence. Hash the
prompt, source pack, environment, artifact contract, evaluator, and policy in both
forms; a paired delta identifies only the layers held fixed. Cross ambiguity
presence with channel availability, answer authority, and action reversibility.
Keep `resolvable_by_inspection`, `requires_authority`, `authority_unavailable`,
`authority_disputed`, and `insufficient_observer_evidence` distinct [AD].

A clarification is a typed authority event, not an answer string. Record who may
resolve which claim, evidence scope, uncertainty, valid time, conflict, delay,
cost, binding force, and whether the response was actually adopted. Null outcomes
include abstain, escalate, wrong authority, unsupported assumption, timeout,
invalid environment, and acceptable alternative. Report recognition, user-visible
disclosure, question information gain, routing correctness, uptake, action,
artifact/state quality, collateral effect, interruption burden, and useful
completion separately. Include matched cases where asking is unnecessary or
costly so generic caution cannot masquerade as calibration [AD, US].

Ambig-DS supplies paired Full/Ambiguous/Ask evidence for one removed target or
objective convention on filtered Kaggle-derived tasks, including valid-looking
wrong-framing artifacts and partial recovery under a perfectly informed scoped
oracle. Its target treatment bundles several edits; objective identity bundles
representation and aggregation; alternatives lack independent professional
validation; each cell appears one-shot; systems are proprietary; and released
packages omit raw results, exact configurations, complete builders/data, and the
archived multi-judge/human lineage. The oracle is not a stakeholder simulation.
Together with UnderSpecBench's unavailable release and fixed-private-oracle flaw,
this supports a controlled diagnostic pattern—not natural ambiguity prevalence,
professional escalation validity, occupational capability, safety, or readiness
[AD, US]. Existing public-basis, authority/participation, artifact/state, trace,
task-health, metric, and validity contracts are the implementation homes; no
ambiguity-specific schema follows.

### 2.3 A rubric is a dependency-aware evidence model

Rubric decomposition makes expert attention inspectable, but does not make it
neutral or independent. Treat each criterion as a versioned evidence object:

- stable ID and immutable text/hash; one explicit proposition; polarity as a
  desirable state or violation state; provenance claim and evidence locators;
  public basis; author/reviewer authority scope;
- `hard_gate`, `required_scored`, `optional_preference`, `penalty`, or
  `diagnostic_only` semantics rather than encoding “mandatory” as a large weight;
  separately typed pass/fail mapping, score direction and magnitude, inversion,
  clipping/normalization, and gate behavior so prose and arithmetic cannot disagree;
- applicability predicate and an `insufficient_evidence` outcome distinct from
  failure, including the artifact/source/trace access the grader requires;
- one observable and decision rule, with a split review for multiple independently
  falsifiable predicates;
- prerequisite, overlap, exclusion, and shared-evidence links so aggregation does
  not silently double-count one fact; and
- typed examples (`boundary_case`, `non_exhaustive_instance`, `counterexample`,
  or `reference_answer_fragment`) with disclosure and exhaustiveness metadata.

For workflows, dependencies must distinguish **path evidence**, **intermediate
consequential state**, and **final consequence**. Bind each edge to its prerequisite
and produced/consumed state, mark whether a failed ancestor masks or makes a
descendant inapplicable, retain alternative valid routes, and recheck collateral
invariants at completion. A strict conjunction may remain a useful endpoint policy,
but the gap between criterion pass rate and all-check completion is not evidence of
independent capability failures, error propagation, or operational reliability.
HealthAdminBench's 135 tasks and 1,698 released checks make this boundary inspectable:
they mix prescribed clicks, handoff states, and final mutations without dependency
edges or repeated trials, while requirement-level observation/expert lineage and raw
paper runs are absent [HAB]. Existing criterion, projection, bundle, trace, task-
health, execution-validity, metric, and validity objects already host the repair.

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

AgenticVBench provides direct falsification evidence for the missing signed
semantics. Its later release is unusually inspectable, yet 13/36 Repurpose briefs
require a different resolution from their hidden criteria, and at least five
desirable-state criteria carry negative weight without the inversion flag required
by the scorer. In those cases a richer multimodal observer cannot infer whether the
brief, criterion prose, sign, flag, or aggregator is authoritative [AVB]. Require a
machine-checked chain before any trial:

```text
public basis → criterion proposition → desirable/violation polarity
  → applicability → authoritative evidence view and observer threshold
    → pass/fail mapping → dependency/gate → signed score contribution
      → aggregation policy → licensed interpretation
```

Fail the instrument—not the agent—when public and private requirements conflict,
when criterion prose and arithmetic reward opposite states, or when a dependency,
inversion, normalization, or clipping rule is unresolved. A positive weight alone
cannot encode this chain. Preserve each preflight finding, repair/version event,
and rerun decision in task health rather than rewriting historical scores.

### 2.3a Dynamic criteria are a separate contingent population

Open-ended artifacts may create facts, dependencies, risks, or side effects that
no fixed reference answer can enumerate. Keep two ledgers rather than one changing
rubric denominator:

```text
fixed requirement criteria (task/query conditioned, comparable)
  + contingent claim/consequence criteria (response conditioned, diagnostic)
    → typed evidence and dependency observations → separately reported metrics
```

A contingent criterion is legitimate only when it cites the exact response span,
action, state, or artifact element that triggered it and tests the truth,
entailment, consequence, contradiction, safety, or convention thereby created. It
may not convert a judge-preferred omission into a new obligation. Preserve its
type, applicability and public professional basis, claim-specific authority and
evidence view, relation to fixed/other criteria (`novel`, `specialization`,
`duplicate`, `dependency`, `counterevidence`, or shared evidence), score/gate/
diagnostic role, and generator model/prompt/decoding/seed plus skill, response, and
criterion-set hashes [JADE].

Evidence verdicts must distinguish `supported`, `contradicted`,
`insufficient_evidence`, and `not_applicable`; retrieval failure or verifier
absence cannot become a substantive negative or restore a reasoning-only score.
Fixed completion, contingent-claim reliability, reasoning conditional on evidence,
source authority, and abstention burden remain separate until an independently
validated fusion supplies a stable population interpretation. Criterion legitimacy
and verdict correctness need blind expert calibration, including extraction
precision/recall and dependency-edge agreement; generator/scorer agreement is not
independent validity [JADE].

JADE demonstrates the architecture on 150 strategic-sourcing queries, but its
human evidence is 180 reports clustered in 30 tasks, with under-specified experts,
trimmed ratings, no clustered uncertainty, withheld rich skills, shared model
cues, mutable live-web verification, uncalibrated authority/threshold/fusion rules,
outcome-conditioned medical trimming, heterogeneous transfer, and absent result
artifacts. Its close post-v1 release is not manuscript identity and its default
two-stage path reproducibly fails open when evidence is absent. **Invariant:** no
response-conditioned criterion without a trigger and fair public basis may affect
a score, and missing mandatory verification blocks the corresponding capability
claim. **Validation experiment:** across two unlike artifact shapes, hold the task
and core content fixed while changing one claim, citation, or dependency; require
only the expected criterion/edge/verdict changes, preserve unrelated invariants,
and measure criterion, graph, verdict, ranking, and score stability across repeats.
Existing criterion, evidence-view, validity, metric, artifact, trace, and task-
health contracts are the implementation homes; do not create a parallel schema.

### 2.3b An adaptive rubric is a sampled instrument, not inferred authority

Task-conditioned criterion generation can reduce the obvious mismatch between a
universal chat rubric and a particular work product, but it adds a stochastic
projection stage. Preserve the full instrument path rather than treating the
generated rubric as part of the task or the judge as its validator:

```text
task requirements and instance identity
  → candidate criterion-set draw → authority/applicability adjudication
    → criterion-specific admissible evidence → observer draw
      → aggregation and eligibility/filter policy → thresholded decision and loss
```

Each stage has a different claim. **Task-to-criterion projection** asks whether a
candidate covers the disclosed requirement without adding a surprise obligation.
**Criterion authority** asks who may approve its obligation, consequence, evidence
view, and threshold. **Semantic instance conformance** asks whether task, source,
reference, and rubric concern the same entities, dates, deliverable, and decision,
not merely whether their IDs and schemas resolve. **Observation** asks whether the
configured grader can support the criterion verdict. **Aggregation/filtering**
defines a score population and compensation policy. **Threshold validity** asks
whether the resulting accept, reject, or escalate decision has bounded stakeholder
loss. None inherits validity from the previous stage [ADA, XB].

Version rubric generation independently from observation. Generator identity
includes model/service, prompt and examples, decoding/seed, source view, task-family
equivalence and cache policy, retry/fallback, and criterion-set hash. Observer
identity includes model/service, rubric draw, evidence view and transformations,
modality support, prompt/examples, decoding/seed, and **call topology**: one joint
trajectory call and `step × criterion` calls induce different context competition,
error dependence, cost, and missingness. Aggregator identity includes applicability
handling, confidence semantics and denominator, dependency/overlap policy, gates,
weights, and normalization. A filter additionally creates an eligibility/deferral
estimand; post-filter agreement must not be compared with an all-case baseline as
though the measured population were fixed [ADA].

Cross rubric-generation draws with observer draws on the same frozen artifacts or
trajectories. Retain the complete intended-attempt ledger and explicit
`not_applicable`, `insufficient_evidence`, invalid-generation, invalid-observation,
and deferred states rather than converting low relevance, missing criteria, absent
modalities, or parser failure into low substantive quality. Map each candidate to
authorized obligations as preserved, omitted, spurious, split, merged,
contradictory, threshold-shifted, or evidence-view-shifted; test legitimate
alternatives, omitted hard gates, misleading self-report, and threshold-near cases.
Report criterion and decision error, rubric-draw and observer-draw variance,
selection burden, severe-error loss, and total cost separately.

AdaRubric motivates this decomposition but does not validate it. Its reported
fixed-rubric score correlation and three-run agreement do not estimate regenerated-
rubric variance or decision loss; item-level human and training evidence is absent.
The pinned post-v3 release uses one trajectory-wide call rather than the paper's
`K×N` topology, omits stated semantic validation/fallback/cache and multimodal
paths, and multiplies scores by confidence without normalizing by confidence, so a
low-relevance step lowers quality [ADA]. XpertBench supplies the complementary
failure: its displayed Education rubric grades a digital-clock lesson plan while
the assigned task requests a Confucius–Socrates screenplay. A large contributor
pool and expert review counts therefore cannot substitute for instance-level
projection evidence; its one expert-scored GPT-5 response is a versioned grader
intervention, not calibration or proof that expert intent transferred [XB].

**Invariant:** no generated criterion may affect a substantive score until its
instance, public basis, authority, applicability, evidence route, dependency, and
decision role are dispositioned; any unsupported mandatory observation blocks the
corresponding claim. Existing criterion, projection, evidence-view, configured-
grader, response-matrix, metric, task-health, and validity objects are the durable
homes. Do not create an adaptive-rubric schema or reward-learning build before
authorized reference criteria are available.

### 2.3c Criterion stability and discrimination do not create authority

Generated-criterion pipelines need a typed health lifecycle rather than a `gold`
promotion shortcut:

```text
candidate generation and provenance → authority/public-basis review
  → evidence-view admissibility → repeated observer reliability
    → development-cohort prevalence/discrimination → independent confirmation
      → threshold/loss validation and operational role
```

Record every artifact, query, system, rater panel, and time snapshot used for
candidate generation, reliability calibration, non-triviality selection,
thresholding, and final estimation. This **outcome-selection firewall** makes a
holdout invalid when its artifact contributed upstream, even if only a later filter
names it as held out. Keep `generated_candidate`, `authority_reviewed`,
`evidence_admissible`, `panel_stable`, `nontrivial_on_development_cohort`,
`regression_guard`, `externally_validated`, and `decision_calibrated` as independent
states. Always-pass basics and always-fail frontier requirements require an explicit
coverage/consequence disposition rather than automatic deletion. Preserve disputed
criteria, rationales, evidence locators, applicability, severity, and adjudication;
agreement can preferentially remove judgment-intensive expertise.

FinResearchBench II makes the selection problem concrete: 14,450 report-conditioned
candidates become 3,687 after three judges agree on all ten reports and 2,600 after
requiring both positive and negative labels. Its 98.67% human/LLM same-label headline
conditions on 2,867/4,052 jointly unanimous observations (70.76%); it does not validate
the excluded disagreement population or criterion truth. Since the same report pool
generates candidates and later supplies distinguishability labels, increased spread
is partly selected by construction. Queries, reports, criteria, labels, generation
prompt, configurations, and analysis are unreleased [FR2]. Read with ResearchRubrics:
expert review improves authority lineage but does not make criteria ground truth
[RR]. Read with AsymmetryZero: panel agreement, repeated-call stability, criterion
correctness, task decisions, and downstream loss remain separate [AZ]. **Invariant:**
unanimity licenses at most a panel-and-view-relative observation; discrimination
licenses at most a declared development-cohort role. **Falsification experiment:**
freeze authority-reviewed criteria, cross repeated observer draws with unseen
artifacts/systems/queries, sample retained and rejected criteria for blind authority
review, and report selection-adjusted criterion and decision error with clustered
uncertainty. Existing criterion, evidence-view, rater, task-health, response-matrix,
metric, and validity records suffice; no finance-specific schema follows.

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

Structural linkage is weaker than **semantic instance conformance**. Before release,
compare typed task requirements against the assigned source, reference, rubric,
and checker across entity, role, deliverable, objective/decision, valid time,
jurisdiction, unit, and representation. A representation may vary only when it is
declared invariant under the task contract; a nearby task with the same work shape
must fail closed when an entity, date, objective, or deliverable changes. Preserve
component versions, payload hashes, evidence locators, assignment identity, and
conflict versus missing predicates so a valid package cannot silently score the
wrong instance [XB].

The internal cross-instance canary admits a Markdown-to-HTML reference change that
preserves the declared supplier-decision contract and rejects both the observed
XpertBench screenplay/lesson-plan substitution and a builder-authored supplier/date
swap [DIC]. This is deterministic, builder-authored calibration of validator
behavior only. It supplies no expert validity, grader accuracy, semantic-
equivalence completeness, cross-domain generalization, agent capability, reward
quality, professional validity, production fitness, or readiness evidence.

#### Formal guarantees require an instantiation witness

A proof applies to its mathematical objects and assumptions, not automatically to
the benchmark pipeline described beside it. Preserve this non-inheriting chain:

```text
declared objective/behavioral theorem → variables, assumptions, and claim ceiling
  → immutable implementation binding → realized constrained execution
    → empirical treatment comparison → external validity and benchmark use
```

For a coverage optimizer, version the expert population and mandate, anchors and
weights, disagreement and omissions, candidate-to-anchor evidence view, calibrated
support scores, complete constraints, optimizer/repair output, and selected-task
links. For a behavioral mechanism, additionally preserve the complete game,
assignment, score reliability, costs, payments, audit/adjudication, missingness,
appeals, and welfare. Test each assumed link rather than citing the theorem as its
evidence. A guarantee for a cardinality-only optimum does not transfer through
quotas, pairwise exclusions, or heuristic repair without a new argument.

KINA exemplifies the boundary. Its max-coverage objective is monotone submodular
under fixed nonnegative support scores, but the realized quota/duplicate-constrained
selector has no general stated approximation guarantee. Its 899-row release has 260,
not the claimed 261, discipline paths; omits advertised source fields and all anchor,
calibration, selection, review, payment, audit, and rank-analysis records; exposes
the claimed encrypted holdout; and conflicts on licenses [KINA]. The theorem supports
a proxy-optimization statement, not population representativeness, professional-work
coverage, contributor behavior, item validity, or readiness. **Invariant:** every
formal benchmark claim must cite a machine- or human-auditable instantiation witness
and stop where implementation correspondence ends. Existing projection,
participation, task-health, release-conformance, metric, and validity records host
the evidence; no optimizer-specific schema follows.

### 2.5a Session-derived tasks are bounded counterfactual projections

Observed demand is provenance evidence, not semantic-equivalence evidence. For each source episode preserve selected turns and initial state; observed request, resolution, feedback, and acceptance; every split/merge, omission, rewrite, fixture restoration, environment substitution, and artifact-contract change; hindsight sources; the fresh-system counterfactual; an independent equivalence disposition; and the licensed claim. `faithful_replay`, `demand_inspired_task`, and `synthetic_calibration` are distinct uses. A source user or expert must explicitly disposition material changes; approval before an engineer/model rewrite does not transfer through it [ECB].

EnterpriseClawBench demonstrates scalable session projection, but its proprietary 852-task pool prevents external source sampling or rewrite audit. In one public trace a later user-authored image analysis becomes answer-bearing rubric content for a fresh single-turn task, changing repair-in-interaction into visual analysis; its public rubrics also copy identical guidance across nominally distinct score dimensions. This supports demand provenance and pipeline reproducibility, not replay fidelity, independent rubric validity, enterprise representativeness, or economic claims [ECB].

### 2.5b Production demand and codified expertise require independent claim promotion

Current company demand and expert rules are valuable upstream evidence, but neither
is a transferable-validity label. Preserve one linked, typed chain:

```text
demand provenance → elicitation authority → representation/codification
  → source-to-task projection → configured intervention
    → independent measurement → bounded package/transfer/use claim
```

At the demand edge, record stakeholder, workflow, recipient, consequential decision,
acceptance/rework boundary, candidate and rejected requirements, sampling frame, and
confidentiality/nonrelease status. At elicitation and representation, preserve who
may speak for which criterion; source locators and informal channels; disagreements,
read-back, and transformation approval; and whether each primitive is a
`deterministic_rule`, `contextual_procedure`, or `open_judgment`, with applicability,
exceptions, implementation locus, and observable consequence. At projection, retain
all scoping, anonymization, self-containment, environment substitution, artifact,
oracle, criterion, weight, and threshold deltas. Agent-conditioned repair or quality-
bar change belongs in task-health history and requires frozen anchors or bridges.
Confidentiality may justify nonrelease, but unavailable source/task/result lineage is
missing audit evidence—not affirmative evidence of fidelity [AE, IC].

At intervention and measurement, disclose authorship overlap across expert source,
elicitor, coder, skill author, task/reference/criterion/grader author, scenario
selector, and evaluator. Hold configured-system identity fixed where possible; use
component ablations for rules, contextual guidance, routing, retrieval, and the full
package; repeat held-out incidents; bind raters to criterion-specific authority and
evidence views; and estimate rater reliability and task/rater dependence. Preserve
four claim ceilings: `rule_execution`, `package_efficacy`, `contextual_transfer`, and
`professional_equivalence_or_readiness`. A co-designed package effect can support the
first two while shared task–rule–criterion content blocks the latter two.

AlphaEval supplies prospective demand and recurring co-design evidence for 94
reported private tasks from seven purposively selected partners, plus selected
configured-package outcomes. Its private transformations/results, nonfactorial
model–scaffold matrix, winner-only repeats, point-level rather than end-to-end rater
validation, and post-v1 framework release do not establish occupational sampling,
causal scaffold effects, production readiness, or economic value. Multiplying a
rubric score by estimated human cost does not measure accepted work, productivity,
replacement value, or consequence [AE]. The Siemens case supplies a credible bundled
rules/prompt/routing/RAG package effect on five selected rule-aligned visualization
outputs. Two experts, one organization/workflow, no component ablation, no rater-
reliability analysis, and overlapping authorship block tacit-transfer, expert-
equivalence, non-expert learning, and cross-domain claims [IC]. These cases refine
existing expertise-transfer, participation, projection, procedural-skill,
configured-system, metric, task-health, and validity objects; they do not justify a
parallel schema or a domain commitment.

### 2.5c Context authority and downstream consequence are separate warrants

Context presence is neither permission to use it nor evidence that an inference
was causally used or beneficial. Preserve a claim-level ladder:

```text
available → authorized → accessible → observed → interpreted → adopted
  → answer/artifact accepted → intended and collateral state consequence
    → affected-party validation
```

Each edge needs independent evidence. Authorization binds contributor or affected
party, purpose, permitted inference/action, entity, valid time, scope, sensitivity,
withdrawal/reconsent boundary, and prohibited uses; corpus-creation consent must
not be promoted into task-time authority for arbitrary profiling. Observation
binds the exact model-visible representation and locator. Interpretation preserves
supporting and contradicting evidence, source authority, uncertainty, and entity/
time/scope resolution. Adoption requires trace or intervention evidence that the
claim changed the output or decision. Semantic answer acceptance is only a grader
observation; consequence requires attributable intended and collateral state
deltas, while affected-party validation requires the person or legitimate proxy
to disposition the inference or action for the intended use.

Historical information needs a typed **admissible decision role** in addition to
semantic relevance. Bind each prior statement, preference, note, or learned
procedure to its source authority and represented subject; intended purpose and
recipient; population, condition, and jurisdiction scope; valid-time interval;
correction, retraction, and supersession relations; evidence precedence; and one
or more current roles: `ignore`, `constrain`, `defer`, `supersede`, or `use`.
Preserve the bidirectional policy: always adopting history must fail when history
is inadmissible, scope-limited, evidence-defeated, or stale, while always ignoring
history must fail when a current authorized preference legitimately controls the
decision. The information-flow record should distinguish
`available → retrieved → presented → adopted/rejected → answer/action → intended
and collateral consequence`; retrieval relevance supplies none of the later
warrants by inheritance [MSY].

MemSyco-Bench makes these five roles concrete in 1,550 released synthetic rows and
reports retrieved-but-wrong diagnostics, but its GPT-5.5-assisted construction has
no released candidate/validation lineage or independent factual, domain, or
represented-user authority review. Its families are nonfactorial; the open-ended
judge has no human calibration or repeats; valid-call denominators exclude some
generation/parse failures; and paper-run outputs are unavailable. The evidence
therefore supports a configured synthetic stress-test pattern, not natural error
prevalence, causal adoption, judge validity, professional validity, benefit, or
readiness [MSY]. Existing source, authority, valid-time, information-flow, state,
grader, metric, and validity objects remain the implementation homes.

#### Routed context is a recipient-state intervention, not a graph edge

Shared storage and typed handoff do not capture **candidate-recipient selection and
delivery**. Preserve a route event as a join across existing claim, participation,
information-flow, trace, artifact/state, and metric records:

```text
source proposition, authority, permission, version, and exact locator
  → routing opportunity, candidate recipients, rationale, policy, and timing
    → permission decision and exact delivered evidence view
      → receipt/inspection → interpretation → adoption or justified rejection
        → changed belief, analysis, decision, or artifact record
          → authorized attempted action → realized result and collateral state
            → recipient burden, error, and bounded route-utility claim
```

No edge inherits the next. A valid graph relation establishes representational
lineage; a delivery log establishes transport; a narrative or downstream proposal
establishes neither receipt nor causal use. A whole-package comparison that changes
participants, information, sessions, compute, proactivity, tools, and stopping may
describe configured-system performance, but it cannot identify routing benefit.
Likewise, an experiment proposal is not its authorization, execution, measured
result, replication, or consequence.

The discriminating experiment freezes proposition, recipient, prior workspace,
task, budget, system, and observer, then varies no delivery, targeted delivery,
manual forwarding, broad delivery, delayed/stale delivery, and corrupted
translation. Measure opportunity-conditioned delivery, inspection, adoption,
decision/artifact delta, intended and collateral consequence, missed-link loss,
overload/interruption burden, and recovery. Route-policy precision or graph
connectivity cannot substitute for those outcomes.

Networked Intelligence motivates this missing transformation through one week-long
three-expert scientific campaign, two reconstructed routes, and a 26-item post-hoc
content audit against two single standalone runs [NI]. Its treatment bundles human
expertise, repeated sessions, persistence, routing, proactive analysis, tools, and
unequal total work; the artifact universe is trace-derived; no route-event records,
repeats, independent scientific review, realized downstream experiment, cost/burden
ledger, permission model, or official implementation was located. The evidence
supports a cross-workstream route-event hypothesis, not routing causality, tacit
transfer, irreducible team intelligence, scientific validity, productivity,
privacy, professional validity, or readiness. Existing contracts are the durable
homes; no graph, scientific-team, or Mycelium-specific schema follows.

An authored minimal support set is a hypothesis, not unique ground truth. Admit
independently reviewed alternate support sets and test necessity through source
ablation; keep answer agreement and evidence-set overlap separate. HippoCamp
strongly exposes availability and authored localized support, partially observes
reported file access and answer acceptance, and does not measure adoption, action,
state consequence, or affected-user validation. Its three edited cross-person
composites cannot supply a literal user model; its answer-only judge lacks source
views; and unavailable corpus, audit, consent-lineage, result, and replay records
block independent privacy, grounding, and reproducibility claims [HC]. The
one-day-post-v1 code archive is release evidence, not paper-time identity.

**Invariant:** no later rung may be inferred from an earlier one, and missing
authorization or affected-party authority fails closed for sensitive inference
or action. Existing participation/consent, artifact-view, trace, workspace-state,
metric, task-health, and validity records are the implementation homes; no
parallel context schema is implied. This ladder licenses no faithful
personalization, privacy safety, professional correctness, causal process,
capability, or readiness claim.

### 2.5d Delegation preference is a selection signal, not a worker outcome

Demand from a worker perspective adds a distinct chain to production-demand
provenance; it cannot be compressed into a scalar task weight:

```text
historical preference observation → duty-to-package transformation fidelity
  → present consent and retained authority → configured-system task measurement
    → observed workflow uptake → measured worker outcome
```

At the first link preserve the exact rating instrument, respondent and duty
sampling frame, date/context, collaboration mode, distribution and disagreement,
and selection transformations. At the package link preserve source duty, retained
human decisions, scope expansion, files/environment, AI or developer rewrites,
post-transformation disposition, and rejected alternatives. Present consent must
name the actor, use, authority retained, review/escalation boundary, withdrawal,
and affected parties; a historical automation rating supplies none of these by
inheritance. Configured-system scores then remain bound to task, scaffold, tools,
artifact/evidence views, execution isolation, grader, retries, and assembly.
Workflow uptake requires observed use, review/correction burden, acceptance and
downstream handling. Worker outcomes require a counterfactual and direct measures
such as total time, severe defects, satisfaction, autonomy, distributional effect,
or displacement—not score arithmetic or expert prediction [JB].

Keep equal-task performance, preference-weighted selection, occupation inference,
workflow adoption, and outcome metrics separate. JobBench contributes a real
worker-reported upstream signal and rich cross-source packages, but its wage and
benchmarkability filters are purposive; one to three Main tasks per occupation do
not estimate occupational capability; and union-of-rubrics solvability conditions
admission on sampled model outcomes without proving one coherent solution. Its
GDPval comparison mixes tasks, graders, harnesses, and metrics. Aggregate proximity
between two model judges does not validate criteria, especially when the inspected
evidence view omits formula lineage and other native/visual state. The current
Codex runner disables sandboxing, web/file retrieval remains mutable, and the
post-v1 release has 128 tasks/4,576 criteria rather than the paper's 130/4,631;
post-v1 code and metadata cannot reconstruct paper-time results [JB].

**Invariant:** no preference, package, or benchmark-score record may license a
later consent, uptake, benefit, occupational, or readiness claim without evidence
at that edge. Use existing demand provenance, expert participation/consent,
task-projection, artifact-admissibility, execution-validity, task-health, metric,
and validity records; this ladder adds no parallel schema or profession-specific
pilot.

### 2.5e Consequence promotion is a linked inference chain, not a score transform

A configured-system observation does not directly estimate organizational benefit,
risk, or decision value. Preserve independently warranted links:

```text
benchmark observation → bounded capability interpretation
  → scenario applicability, access, and effective use
    → conditional workflow effect relative to a counterfactual
      → outcome composition, frequency, controls, and severity
        → stakeholder threshold and loss
```

Each link needs its own target, population, conditions, counterfactual, evidence,
uncertainty, supported/excluded interpretations, and next discriminating study.
Benchmark success, capability availability/use, a conditional transition, final-
outcome frequency/severity, and utility/loss are non-substitutable quantities.
Prefer direct matched workflow-uplift evidence where feasible; an expert estimate
of transfer is not causal uplift, and a conditional transition is not expected
harm or a deployment decision.

When experts assess a link, the **information condition is part of the instrument**.
Hash the task packet, summaries, metadata, reliability wording, task order, and
scenario/counterfactual specification. Retain initial estimates and rationales,
peer estimates viewed, moderation and discussion-group membership, revised values,
corrections/exclusions, and why each judgment moved. Before pooling, fork genuinely
different estimands and type disagreement cruxes such as actor/environment
ambiguity, benchmark-to-work transfer, access/use, baseline, causal mechanism, or
stakeholder loss. Model repeated-task and discussion-group dependence; disclose
calibration/seed status, pooling code and assumptions, missingness/exclusion rules,
and sensitivity to subgroup and alternate aggregation. A wider interval cannot
stand in for incompatible targets or rival warrants.

The reviewed Cybench pilot usefully preserves some initial/revised rationales and
shows two groups adopting rival isolated-task-to-operational-work warrants. Seven
complete respondents, two deliberative clusters, five tasks always ordered by FST,
generated solution-adjacent packets, an imported baseline, ambiguous access/scaffold
conditions, missing calibration seeds, and an unreleased Bayesian specification do
not validate its probability ranges, an FST effect, calibrated uplift, cyber risk,
expected harm, or decision usefulness [BR]. **Invariant:** no later link is licensed
by an earlier observation or by expert aggregation alone. Link existing validity-
argument, metric-monitoring, expert-participation, and future elicitation-session
records; do not create a parallel schema or implement the blocked session contract
without a real consented session.

### 2.5f An analytical witness is not an operational consequence oracle

Real source material, a verified label, an executable reference path, an accepted
artifact, and a beneficial outcome are different validity objects. Preserve the
full ladder:

```text
source event/snapshot and valid time
  → task requirement, assumptions, and authority
    → source or label truth under a declared observer
      → one analytical witness and configured execution
        → endpoint/artifact observation and professional acceptance
          → recipient uptake and authorized attempted action
            → realized intended/collateral state → stakeholder consequence
```

No rung inherits the next. Historical or production provenance attaches first to
the source, not automatically to the authored question, constants, objective,
threshold, route, recommendation, or use. Ground-truth substitution is an
instrument-construction intervention: it may stabilize one downstream reference
while suppressing uncertainty present in the evaluated or operational system. Keep
at least three oracle roles separate: **source/label truth**, **analytical witness**,
and **operational acceptability or consequence**. A canonical path proves one
feasible derivation only; it does not prove necessity, completeness, safety,
optimality, or authority.

Task-level lineage must bind source snapshot, license and valid time; contributor or
framework clause and authority scope; requirement, assumptions, transformations,
thresholds, protected constraints, intended recipient, and reviewer disposition.
Represent independently reviewed alternate paths/answers or partial orders,
prohibited actions, uncertainty, and legitimate abstention/escalation. Endpoint
tolerances must be expressed in decision-relevant units and justified by loss or
consequence: pixel distance, overlap, relative error, string equality, and weighted
field averages are merely configured predicates until map scale, stakeholder impact,
boundary cases, and false-accept/false-reject costs calibrate them.

For consequence claims, preserve artifact acceptance, recipient interpretation and
uptake, authorization, attempted versus realized action, protected-state
preservation, collateral effects, affected stakeholders, and whether each outcome
is observed, simulated, or expert-projected. Estimate uncertainty at the source
event or task-package lineage level when tasks share events, assets, tools, authors,
or templates; task rows are not automatically independent. Diagnose tool, data,
perception, interface, task, grader, and agent surfaces separately, and name a root
only after event evidence, intervention, or qualified adjudication supports it.

DORA makes this boundary unusually visible: 515 reported tasks compile one authored
geospatial path into typed endpoints over real historical imagery, while the
model-backed canonical path reaches only 80.48% agreement with GT-derived answers.
Its unnamed expert lineage, uncalibrated 20%/20-pixel/.5-IoU gates, absent alternatives,
missing Appendices C–H, and unavailable task/tool/trajectory/result package block
audit of the empirical instrument and every operational promotion [DORA]. The source
supports typed manifests, path-versus-endpoint diagnosis, and imperfect-witness
execution—not emergency-response competence, safety, professional validity,
capability, production fitness, or readiness. Existing authority, evidence-state,
artifact, action-safety, trace, root/surface, task-health, metric, and validity
records are the implementation homes; no disaster-specific schema or pilot follows.

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

Agents' Last Exam adds a useful occupational coordinate frame and broad executable pool, but its 55 nonempty subdomains are not task-frequency or consequence-weighted occupational coverage. Preserve the exact immutable **suite-role membership** used in a reported result. Its paper and later release have different Near-Term/Last-Exam counts and overlapping roles, so a tier name is not a version. Outcome-informed difficulty is routing metadata, not an intrinsic task trait; freeze the admission snapshot or model-system outcomes partly define the comparison [ALE].

### 2.6a Work realism is a many-to-many activity and handoff correspondence

An occupation label, plausible interface, or polished deliverable does not by
itself identify the responsibility tested. For each task, preserve a revisable
many-to-many activity map with `target`, `required`, `incidental`, and `omitted`
relations, source/version, reviewer disposition, and mapping uncertainty. The 18
O*NET-derived labels in the reviewed design report are useful candidate
coordinates, not a closed ontology, representative denominator, prevalence
estimate, or validated latent structure; local workflow and expert evidence may
split, merge, or replace them [DR].

Represent the correspondence and its negative boundary explicitly:

```text
target activity ↔ required operations ↔ tested setting and omitted responsibility
  ↔ persistent product/state ↔ recipient and next operation
    ↔ source/boundary/destination evidence ↔ strongest supported claim
      + named excluded claims
```

For materials, tools, role/scope, and workflow state, record what is supplied,
withheld, simplified, or simulated and which inference is thereby removed.
Preselected sources subtract discovery; a prescribed form subtracts product
choice; one-shot interaction subtracts clarification; a simulator subtracts
some institutional consequences; an executable oracle observes selected
acceptance predicates. These may be legitimate treatments, but they are
**claim subtraction**, not an undifferentiated realism score.

A work product is complete only relative to a declared receiving operation.
Record recipient role/system, intended next operation, required handoff fields,
accepted alternatives, acceptance evidence, unresolved blockers, and destination
conventions. Keep three check families distinct: **source** (authority,
entailment, provenance), **boundary** (scope, jurisdiction, authorization, and
preserved constraints), and **destination** (recipient interpretability and
next-operation executability). A correct answer may fail to support reviewable
analysis; a working integration may still fail deployment readiness.

**Invariant:** setting simplifications and omitted activities must subtract named
claims, and no artifact-quality aggregate may substitute for source, boundary,
and destination evidence. **Validation experiment:** across at least two unlike
handoffs, give an independent recipient only the produced product and measure
clarification, repair, rejection, time, and propagated error while admitting
legitimate alternate formats. The source supplies no recipient-use trial, panel
details, annotation reliability, taxonomy stability, exact reconstruction, or
downstream-validity evidence; these remain required before treating its reporting
chain or vocabulary as validated [DR]. Existing artifact/state, participation,
validity, task-health, metric, and provenance records are the implementation
homes; do not create a parallel schema.

### 2.6b Successor resumability is a frozen-state, recipient-relative experiment

A handoff record is not intrinsically resumable. Resumability is a relation among
one authoritative work state, a visible handoff view, a receiving configured
system, its allowed evidence, a declared continuation operation, and an endpoint.
Compare views only from the same byte-pinned checkpoint and preserve the chain:

```text
source work unit + predecessor configuration/trajectory
  → interruption rule + frozen workspace/environment hash
    → handoff view + author/generator/transformation lineage
      → successor configuration + evidence entitlements
        → verification and continuation actions
          → terminal artifact/state + preservation consequences
            → takeover effort + total lifecycle cost → bounded claim
```

Keep five outcomes non-substitutable: **state fidelity** (truth, authority,
valid time, uncertainty, contradictions, failed paths, and workspace state),
**recipient sufficiency** (support for the declared next operation and legitimate
alternatives without blind trust), **endpoint quality** (completion,
preservation, regression repair, or another predeclared terminal state),
**outcome-aware continuation effort** (verification, inspection, editing, calls,
tokens, wall time, and censoring under a frozen stopping rule), and **total
lifecycle cost** (handoff generation/transformation, storage/retrieval,
verification, retries, and human review as well as successor effort). A raw trace
may be faithful but costly to use; a short note may help one next action while
being false or inadequate for rollback, audit, delayed resumption, or another
recipient. Neither endpoint success nor low successor cost repairs an invalid
handoff [HD, ACON].

Factor view interventions where the claim requires it: state only, raw trace,
deterministic predecessor-observable metadata, free summary, structured content,
and independently authored content. Bind producer and recipient contracts,
accepted alternate futures, preservation predicates, and note-generation cost.
Plant omissions, stale validation, false success/state labels, contradictory next
steps, and benign alternative paths; then score transport/parse, semantic and
authority validity, receiver acceptance, next-operation consequence, and artifact
preservation separately [ACOOP, D52, HU]. **Evaluator-derived continuation state
is private analysis evidence, not a successor-visible field.** Any label computed
from hidden tests, private references, or evaluator-only state is oracle assistance
unless the same decisive evidence is legitimately available to every compared
view.

Efficiency estimands must not rename all reduced interaction “rediscovery.” Runs
can stop because they solve, preserve, fail early, or hit a cap. Report time or
events to a defined endpoint with explicit censoring; matched effort within shared
terminal-outcome strata where useful; repeated inspection/validation/edit counts;
invalid and provider failures; and full lifecycle cost. Cluster and resample at
the source work unit or higher lineage level so several checkpoints from one
trajectory are not independent tasks. The displayed point estimate and interval
must target the same statistic; ratios of marginal medians and distributions of
matched relative reductions are different estimands [HD].

Handoff Debt supplies configured agent-to-agent coding evidence that context-
bearing views can reduce takeover-side events and prompt tokens under its tested
runtime, with smaller and recipient-dependent endpoint effects. Its 181
checkpoints are nested in 75 issues, its effort depends on outcome/stopping, note
generation is excluded, a continuation-state field may leak official status, and
no task IDs, checkpoints, payloads, run records, or analysis release could be
verified [HD]. AgentCo-op establishes that typed transport is not receiver-use
validity; DELEGATE-52 keeps requested change and preservation orthogonal;
Workspace-Bench separates availability, access, and causal use; and ACON shows
that task-sufficient compression need not be state-faithful [ACOOP, D52, WB,
ACON]. The internal two-shape handoff conformance records add isolated producer,
consumer, semantic-adjudication, and content-dependence evidence only [HU]. None
of these sources establishes human handoff validity, professional collaboration,
cross-domain causal generalization, general capability, production fitness,
safety, or readiness. Existing handoff, workspace, transition, compression,
configured-system, trace, metric, task-health, and validity records are the
implementation homes; no coding-specific or resumability schema follows.

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

ALE's released PowerMill evaluator adds a concrete bypass: a pre-existing `agent_sim.stl` can enter a test path that skips collision checking and simulation. The internal seven-case replay rejects pre-satisfied, stale, copied-reference, and omitted-transition outcomes, accepts one declared alternate path, and marks invalid initialization as environment invalid. These are builder-authored synthetic conformance results only—not ALE reproduction, verifier completeness, agent capability, prevalence, expert validity, or readiness [ALE, IS].

#### Temporal artifacts require native, rendered, and export-time evidence

A state visible at one instant cannot establish behavior over an interval. For any
time-indexed or compositional artifact, route criteria through a typed ladder:

```text
source identity + time basis → native editable structure
  → rendered audiovisual interval → exported bytes and declared properties
    → creative/professional acceptance → recipient use and consequence
```

Bind interval/frame/sample locator, track/layer/component identity, synchronization
tolerance and its loss basis, source→project→render→export lineage, required and
preserved regions, permitted invariances, and the exact observer view. A screenshot
may establish a static UI value; it cannot prove playback timing. A progress dialog
cannot prove a decodable export; a plausible render cannot prove editability; and
one expert demonstration is a solvability witness rather than a mandatory action
sequence. Missing source, native, render, or export evidence yields
`insufficient_evidence` or `invalid_artifact`, not ordinary criterion failure [CV].

CutVerse motivates the distinction through 186 reported expert-demonstrated media
tasks and 631 screenshot-oriented milestones, but does not release the task corpus,
parser, evaluator, VM identities, result ledger, or judge annotations; its later
generic Windows harness cannot reproduce v1 [CV]. The internal 11-case replay makes
source/native/render/export routing, tolerance boundaries, wrong-interval/component,
broken-editability, export mismatch, missing-view, and alternate-sequence outcomes
executable [TA]. It validates deterministic fixture behavior only—not observer
accuracy, creative quality, expert validity, agent capability, reliability,
professional validity, production fitness, or readiness.

AgenticVBench repairs the static-inspection gap but not the claim chain. Its pinned
post-v1 release exposes all 100 reported four-family task packages and substantive
manifest, source-relative, temporal frame/audio, metadata, and model-judge routes;
it also exposes the signed-criterion defects above, mutable/unhashed source assets,
no affirmative task-level media rights, and material paper/release grader drift
[AVB]. Paper claims about human reference and 96.4–98.2% agreement lack task IDs,
units, rater topology, human–human reliability, calibration rows, and uncertainty;
the release contains no paper trajectories, scores, human submissions, or result
ledger. Its non-Repurpose audit has 4,610 rows where the nominal design implies
3,840, while the complete campaign implies 6,000 task attempts. Therefore preserve
expert authoring, source rights/immutability, human administration, grader
calibration, task conformance, configured-package attempts, and professional
acceptance as separate records. Reconcile `task × configured system × repeat` into
intended, attempted, service-valid, execution-valid, grader-valid, retried,
excluded, and scored rows before reporting quality, reliability, or cost. This is
cross-domain criterion/ledger evidence, not a reason to add a video subsystem.

### 2.8 Executable composition is not a workflow-validity argument

Composing seeded setup, oracle actions, and state validators can efficiently create
longer executable tasks, but it does not establish that the chain represents a
professional workflow or isolates planning. Represent every composite task as a
typed obligation DAG: prerequisites, produced and consumed state, equivalent paths,
reversibility, milestone observations, and terminal invariants. Retain validator
invocation cadence as instrument identity; at termination, replay all required
invariants independently of polling order so earlier credit cannot survive a
reversal. Reset evidence needs pre/post fingerprints, enumerated side effects,
teardown outcomes, and invalid-trial handling [WA].

WorkArena++ strongly supports executable composition in one ServiceNow substrate,
including paired explicit-procedure and protocol-retrieval variants. Its 341 paired
author-designed workflows, near-floor configured-agent results, and small trained
convenience human study do not establish occupational sampling, five isolated
cognitive abilities, or causal planning burden. The inspected official code is from
2026 rather than the 2025 paper, uses both sequential and global validators, and
does not prove complete reset, cross-software transfer, safety, or exact
reproduction [WA]. Compare observed composite success with a matched atomic
prediction using template/family-clustered repeats; a gap remains diagnostic unless
presentation, horizon, interface, and information budgets are controlled and the
workflow has expert or source provenance.

The internal two-work-shape conformance replay makes reversal-safe terminal checks,
poll-order independence, earliest unsupported-dependency localization, reset
attestation, and atomic-product recomputation executable [CW]. It validates fixture
behavior only—not agent capability, planning causality, occupational realism,
professional validity, safety, cross-domain generality, or readiness.

### 2.9 Workplace substrate is not consequential-work validity

Treat workplace realism as an evidence profile, not a setting label. Preserve this
ladder without allowing a later link to inherit validity from an earlier one:

```text
occupational/task provenance → service/environment and initial-state validity
  → requirement/history availability → access → authority/applicability → adoption
    → actor or NPC authority → action execution
      → intended + collateral state deltas → evaluator dispatch + sufficient view
        → licensed construct, population, and use claim
```

At the substrate layer, pin services, files, identities, permissions, actor/NPC
model and profile, source-state roots, network/tool envelope, health, reset, and
cleanup. At the requirement layer, bind each hidden consequence to exact admissible
spans, valid time, scope, corrections, and alternate support sets; availability is
not access, and access is not authoritative adoption. At the action layer, declare
required, permitted, forbidden, and preserved deltas, legitimate alternate paths,
recipient or downstream operation, and verification. At the instrument layer,
statically dispatch every criterion, execute an oracle witness, and prove that the
observer can distinguish task-created success, collateral damage, and insufficient
evidence. Broken dispatch, stale/shared pre-state, or unavailable observers produce
instrument/environment invalidity, not agent failure [TAC, OD].

TheAgentCompany strongly demonstrates integrated self-hosted services and selected
cross-service coherence. Its convenience/verifier-shaped tasks in one invented
software company, simulated coworkers, permissive inspected predicates, shared-
service reset uncertainty, and single-run results do not establish authority,
complete consequences, occupational sampling, collaboration, labor automation, or
readiness [TAC]. OdysseyBench adds inspectable synthetic history-to-office-state
lineage, but supplies histories at evaluation time, simulates prior work, imports
mutable external testbeds, and relies mostly on existence/substring/cell predicates;
it therefore tests a configured evidence-to-action pipeline, not persistent memory
or professionally complete workflow execution [OD].

The internal experience-memory conformance extension makes six failure classes
distinct—raw-history success, summary omission, stale adoption, missed required
transition, collateral mutation, and unavailable-evaluator invalidity [XM]. Its one
deterministic builder-authored fixture validates contract behavior only. Real claim
upgrades require provenance-grounded unlike workflows, repeated trials, actor and
recipient/expert validation, alternate-path and adversarial-observer tests, complete
reset evidence, and lineage-clustered uncertainty.

#### 2.9a Prior-experience consumption is opportunity-conditioned state change, not an endpoint proxy

After delivery, preserve an authority-aware event chain rather than inferring
“memory use” from changed actions or final score:

```text
versioned prior experience + authority/applicability/admissible role
  → delivered evidence view and schedule → first proposition-specific opportunity
    → access + interpreted recommendation → adoption/rejection/deferral + action
      → induced state delta + reversibility → repeated re-entry/dependency propagation
        → correction signal + repair opportunity → attempted repair
          → accepted state transition → residual/collateral consequence
            → final artifact/state outcome + cost + bounded claim
```

No link inherits the next. The first exposed step may precede the first decision at
which a proposition can matter. Repeated visibility is dose, not propagation, unless
the trace links an earlier induced delta through a dependency into later action or
state. A later baseline-like action is neither necessary nor sufficient for repair:
record the permissible action/state set, whether repair was attempted, whether the
environment accepted the transition, what irreversible or collateral state remained,
and whether terminal invariants were restored. Access, citation, action divergence,
semantic adoption, causal use, repair, and endpoint recovery remain different
observations [TCP].

Denominators must expose the conditioning. Report a strict assignment/intention-to-
treat package contrast over every intended eligible trial, with service, environment,
observer, and artifact invalids retained separately. Then report descriptive
opportunity-, access-, adoption-, divergence-, correction-, and repair-conditioned
rates with their numerators, exclusions, and lineage clusters. A subset defined by a
treatment action or observer judgment is post-treatment selected; its conditional
damage may describe observed compliers but does not identify all-task mediation, a
common principal stratum, or a causal Entry/Propagation/Recovery mechanism.

The Compliance Trap makes action-and-consequence traces concrete, but v1 operationalizes
Entry mainly as first action divergence or recommendation alignment, Propagation as a
persistent/early endpoint-effect ratio, and Recovery as later baseline-action
realignment. Its outcome-selected 77-task WebArena pool, co-authored synthetic tasks
and traps, bundled identifiability/wording interventions, uncalibrated compliance and
recovery observers, one-run cells, template clustering, unreconciled missing/retry
denominators, and absent task/trajectory/result release support configured-package
sensitivity to authored context only—not mechanism, memory capability, safety,
professional validity, production fitness, or readiness [TCP].

**Matched falsification experiment:** on two unlike knowledge-work actions, one with
a reversible and one with an irreversible consequence, freeze the first actual
proposition opportunity and compare no prior experience, authorized helpful,
plausible conflicting, irrelevant, stale/superseded, and corrupted evidence. Only
then cross single versus persistent delivery at matched capacity and total budget.
Instrument access, adoption/rejection, chosen action, dependency-bearing state,
correction availability, attempted and accepted repair, residual state, endpoint,
invalidity, and cost with repeated configured-agent runs and lineage-clustered
uncertainty. Existing experience-memory, evidence-flow, trace, artifact/state,
task-health, metric, and validity records are the durable homes; do not add an E–P–R
schema or infer a browser/memory-product scope commitment.

Interdependent sessions add a dependency-bearing action shape, not automatic
memory causality. Preserve the edge from earlier observation/artifact/state through
write payload and feedback authority, session reset/persistent state, retrieval,
presented evidence, adoption, intermediate action, and final consequence. Compare
matched reset/no-memory, raw-experience, answer-feedback, oracle-evidence,
irrelevant-evidence, and corrupted-evidence conditions on equivalent-form held-out
actions. MemoryArena demonstrates that configured memory–agent pipelines struggle
on authored chains, but domain-specific feedback (including judge text and seeded
plans), non-equivalent success semantics, no clean no-memory arm, brittle/model
graders, and no repeats leave retrieval, state reconstruction, reasoning, and
consequence causally entangled [MA]. Endpoint success licenses neither a root-cause
memory diagnosis nor longitudinal learning, professional competence, or readiness.

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

Treat plural channels as **requirement routes**, not interchangeable votes. Bind
each criterion to its authoritative evidence object and time: a final response may
show disclosure or reasoning; a request log may show attempted authority use; a
service event or pre/post state may show committed consequence; native structure,
rendered intervals, and exported bytes establish different artifact predicates.
Record channels required, channels actually captured, transformation/freshness,
observer version, and cross-channel contradictions. A tool timeout followed by a
committed side effect, an invocation with no state change, and a correct unsupported
claim require different verdicts. Calibrate the composed observer on a blinded
sample spanning every agreement/disagreement cell; incremental detections selected
by one observer cannot estimate either observer's sensitivity or false-accept rate
[CE].

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

### 3.2d Criterion-to-outcome validity is a timed relationship, not a score weight

An external outcome can test a score's relevance without validating the score,
observer, intervention, or decision. Preserve the non-inheriting ladder:

```text
criterion authority and intended construct
  → configured observer validity under an exact evidence view
    → score time relative to outcome-bearing cues
      → eligible population, base rate, clusters, and missingness
        → external outcome authority, window, join, and reversals
          → concurrent association with uncertainty
            → incremental prospective prediction over declared baselines
              → frozen score-targeted intervention effect
                → threshold/loss, operational decision, and stakeholder consequence
```

Each relationship binds the criterion, observer/configuration and repeated-label
evidence; pre-outcome or retrospective view hash; eligible unit, inclusion and
case-enrichment policy, clusters and censoring; outcome definition, source, join
integrity, horizon, missingness, reversals and adverse outcomes; estimand,
comparators, multiplicity and uncertainty; frozen weight/threshold; stakeholder
authority, loss and prohibited uses. A whole-episode score can be a valid
retrospective description while leaking consequence-adjacent state and remaining
invalid as a forecast. Association can reflect task difficulty, user intent,
agent identity, selection, or observer error; prediction need not identify a
causal lever; and an observable outcome such as payment, acceptance, or throughput
need not be a legitimate or sufficient optimization target.

Keep observer accuracy/reliability, concurrent criterion association,
prospective incremental prediction, intervention effect, outcome authority,
decision utility, and stakeholder consequence as separate validity claims. Never
zero-weight correctness, safety, rights, or professional obligations merely
because they have weak association with one endpoint. Report dimension-level
relations and applicability before any use-specific aggregate, preserve frozen
development/confirmation forms, and pair intended outcomes with reversals,
rework/refunds, burden, safety, and longer-horizon consequences [CVO].

The reviewed conversational-commerce study provides manuscript-reported evidence
that one configured whole-transcript judge's Need Elicitation and Pacing Strategy
scores have moderate concurrent associations with payment in a selected
25-converted/35-unconverted human-only sample; Contextual Memory has no detectable
bivariate association [CVO]. Different outcome-stratum eligibility rules, roughly
0.5% source prevalence with case enrichment, uncontrolled intent and clustering,
an unvalidated single observer, retrospective outcome-cue access, tiny selected
reweighting, and absent phase-2 rows block judge-validity, prediction, incremental,
causal, customer-value, professional-validity, production-fitness, and readiness
claims. Existing criterion/grader, evidence-view, metric, task-health, response-
matrix, participation, production-validation, and validity records compose the
required episode; no outcome-validity schema follows.

### 3.2c Evaluator retry repairs an attempt record, not its substantive validity

Treat selective re-execution as selection over an append-only attempt population:

```text
eligible source record → configured evaluator attempt
  → substantive valid observation (retain; never retry for outcome)
  → typed evaluator invalidity (predeclared retry eligibility)
  → abstention / not applicable / insufficient evidence (retain as typed outcome)
  → bounded retry under the exact frozen treatment
  → declared final observation or residual invalidity
```

Each attempt binds source-record ID and content hash, ordinal and parent attempt,
raw request/response locators, exact model/prompt/evidence-view/parser/schema/
decoding/configuration hashes, environment/worker, timing, tokens/cost, validation
result, typed invalid reason, eligibility decision, and retained-final status.
Transport, provider, truncation, parse, and schema failures may be retryable when
declared prospectively. A schema-valid pass, fail, or unfavorable score is never
retryable because of its value; neither abstention, `not_applicable`, nor
`insufficient_evidence` may be regenerated into apparent completeness. Any
treatment change forks evaluator-configuration identity rather than continuing a
retry chain. Final-selection, conflict, duplicate-publication, maximum-attempt,
and residual-failure rules must be fixed before values are observed [SRE].

Report both substantive outcomes and evaluation-operation outcomes: eligible and
prefiltered source records, first-attempt valid, recovered at each ordinal,
residual invalid, missing/delayed/duplicate, and published records, with subgroup
and denominator effects. A final schema-valid row establishes only record shape.
Repeated-call stability, human concordance, criterion/evidence validity,
population-metric validity, decision validity, and downstream utility require
separate evidence gates. The reviewed production pipeline reports roughly two
million records and a plausible record-level recovery architecture, but releases
no configurations, prompts, schemas, logs, attempt counts, retry curves, human
labels, throughput/cost evidence, or code; its one-label-per-record audit cannot
estimate human reliability. These are bounded design/experience claims, not
validated idempotency, judge accuracy, unbiased reliability, production utility,
or transport to artifact-heavy knowledge work [SRE].

### Review selection is part of the measurement design

Human or model review begins with an inclusion treatment, not with a neutral set
of trajectories. Preserve one linked **review-selection episode**:

```text
immutable eligible population
  → detector/version and inclusion mechanism
    → reviewer evidence view and observation
      → plural labels and adjudication
        → supported defect
          → accepted intervention
            → replay or field effect
              → downstream utility
```

The population record identifies trajectory IDs and hashes; configured system,
task/domain, harness, time, reward/outcome, and shared-lineage clusters; duplicate,
retry, truncated, missing, invalid, and delayed-label disposition. The inclusion
record identifies detector and normalization hashes, signal evidence locators,
score/priority formula, thresholds, quotas, tie policy, exclusions, budget, seed,
with/without-replacement policy, inclusion probability, cross-stream overlap, and
nonresponse. The review record binds rater identity, authority, assignment,
independence, actual evidence view, time and cost, raw label, rationale/evidence
locator, and adjudication lineage. Finally, declare intended use—discovery,
prevalence/drift, regression, safety audit, task authoring, or preference-data
candidate—and licensed and prohibited inferences [SIG].

Operate two linked but non-substitutable streams. A frozen **probability sentinel**
supports prevalence, drift, subgroup rates, and enriched-stream false-negative
audits when support and missingness are adequate. An **enriched discovery queue**
optimizes case-finding and rare-pattern investigation. Its changed inclusion
probabilities are the mechanism of value, so unweighted issue rates, agent/system
comparisons, safety incidence, and calibration claims from that queue are invalid.
Design weights do not repair zero support, unknown inclusion, outcome-conditioned
selection, or detector development on the analysis pool.

Keep `signal_observed`, `review_worthy`, `candidate_defect`,
`defect_adjudicated` (with root/surface status), `intervention_accepted`,
`replay_effect`/`field_effect`, and `downstream_utility` separate. Measure reviewer
minutes, trace size/turns, required state queries, annotator count, adjudication,
detector compute, confirmed-defect yield, recurrence, severity-weighted benefit,
and total cost; cluster uncertainty by source task/incident/configured system.
Rows-per-positive is queue yield, not labor efficiency or causal utility.

Signals supplies bounded evidence that lexical/event features enriched a 100-slot
historical τ-bench review queue for a permissive hypothesis-generating label. Its
pool, sample IDs, exact detector/triage policy, overlap, labels, costs, and analysis
are unreleased, and task/configuration dependence is ignored. The later Plano
implementation is post-v1 evidence and converts descriptive signals—including
environment exhaustion—into emitted quality scores contrary to the paper's stated
use boundary. Therefore preserve detector consumers and claim/use lineage and fail
closed on metric promotion [SIG]. AgentRewardBench addresses the next observation
stage; AgentLens, Anthropic, and Amazon motivate diagnosis/task-health routing;
Nubank addresses a later offline-to-online association. None fills the missing
selection or intervention-effect link. Existing trace, rater, task-health, metric,
configured-system, and validity records are the implementation homes.

### 3.2a Deterministic evidence-path checks inherit the validity of their contract

A repeatable scorer can establish only that a frozen predicate was applied to a
frozen observation. Before interpreting the result, preserve a proof-carrying
contract chain:

```text
public requirement and affected-party authority
  → authoritative sources, access policy, and valid-time rule
    → claim-specific evidence/search universe and admissible alternatives
      → adapter observation and information-flow stages
        → deterministic predicate observation
          → semantic/professional observation where needed
            → aggregation, bounded claim, and decision
```

Type runtime information flow as `request → result_exposure → content_access →
model_visibility → citation_or_adoption → action → effect`. A blocked request is
a policy-attempt observation, not evidence of exposure, leakage, harm, or causal
use. Preserve filtered and unfiltered result identities where policy permits,
adapter errors, actor/role/purpose, subsystem, valid interval, and policy version.
This refines the broader context ladder in §2.5c and retrieval invariant 19 rather
than creating another trace subsystem [GE].

Negative claims require a bounded search-universe record: universe owner and
authority; included sources/indices and known omissions; snapshot and valid time;
query/operator semantics; pagination, truncation, and retry state; access failures;
index synchronization/completeness evidence; and residual uncertainty. The licensed
statement is “not found within U under Q at T,” never global absence by default.
Direct retrieval of predeclared IDs is one witness path, not proof that the search
mechanism or universe was complete. Store independently reviewed sufficient evidence
sets or sparse necessary checkpoints, mutate valid omitted paths and irrelevant
results, and return `insufficient_evidence` when completeness is unsupported [GE,
WB].

Likewise, an event join, temporal order, or shared entity key is a
`configured_dependency`; call it causal only when intervention or a warranted causal
model, rival-mechanism analysis, and qualified adjudication support the promotion.
LongMedBench's recorded next event is not automatically a decision oracle;
BigFinanceBench's narrated checkpoint is not audited evidence use; Workspace-Bench's
dependency graph is not causal adoption; and GroundEval's exact internal mechanism
label is not counterfactual reasoning [GE, LM, WB]. Public basis and recoverable
evidence locators are required for every exact private field.

Observer comparisons must hold decisive evidence views fixed. Compare deterministic,
model, and human observers predicate by predicate against independent labels with the
same contract, trace, artifacts, and state-query opportunity; a prose-only observer
is an explicit insufficient-view control, not an accuracy baseline [GE, ARB].
GroundEval's release usefully supplies deterministic actor/time, configured-artifact,
and search-coverage mechanics, but its paper corpus, 96 questions, trajectories,
judge records, and results are absent. Its Table 6 matches release code that multiplies
the whole combined score by `(1-v)^2`, not published Equation 1, while release
aggregation retains only actor-gate violations rather than the stated three types.
The 82 passing unit tests and compact example generation establish selected code
behavior—not contract authority/completeness, causal validity, verified absence,
observer superiority, professional validity, capability, safety, production fitness,
or readiness [GE]. Existing provenance-observation, alternative-path, artifact-view,
trace, task-health, metric, and validity machinery are the implementation homes.

### 3.2b Disagreement can be evidence about the instrument or the construct

For ordinal plural grading, agreement, panel-relative severity/location, model
fit, repeated-call stability, and decision validity are non-substitutable. A
connected assignment may identify relative rater locations only under explicit
anchoring, thresholds, dependence assumptions, and a frozen linked panel; bridge
items are required across task, rubric, or rater changes. Preserve raw scores and
uncertainty when deriving an adjustment, test rater×criterion and rater×task
interactions, and never promote a mean-centered or well-fitting rater to
professionally correct or interchangeable [MF]. The reviewed complete crossing
contains only 30 learners, four Chinese-writing prompts, two human references,
unpinned one-call model configurations, and no released data/code or differential-
rater analysis, so its estimates are measurement-design evidence only [MF].

Rubric realization is also configured instrument identity: criterion text and
order, examples/context, evidence view, joint/isolated/dependent execution plan,
output-scale transformation, aggregation and tie/incomparability policy, retry
behavior, cost, and latency. An edit must retain old/new observations and be tested
separately for human reliability, autorater repeats, paired agreement, severity/
interaction effects, construct preservation, decision loss, and burden. Higher
agreement can arise from shared anchors, compressed scale use, or narrowed valid
solutions [RM]. The reviewed study rerates only machines against heterogeneous
historical labels, bundles edits, changes aggregation, covers two domains/two
models, and releases no runnable package; it identifies configured agreement
effects, not improved accuracy or rubric validity [RM].

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

### 3.3 Reliability is a conditional operational profile

Mean success and operational reliability are non-substitutable. Bind every
reliability estimate to a configured system, task and equivalent-form population,
environment version, time window, retry/timeout policy, intervention and exposure
distribution, and consequence model. Preserve separate observations for accuracy,
outcome/action/resource repeatability, perturbation sensitivity, confidence
calibration and discrimination, constraint frequency, severity, reversibility,
remediation, and decision loss. Consistently failing is repeatable but not capable;
an equal-weight dashboard is not a validated reliability or readiness scale [AR].

Repeated evaluation must begin with a named estimand rather than a universal
repeat count. Preserve this hierarchy without allowing one rung to inherit the
next:

```text
every intended attempt
  → service availability → execution-valid trial → grader-valid observation
    → per-task/form outcome distribution and severe-failure recurrence
      → task/form/family population mean and heterogeneity
        → paired configured-system or intervention contrast
          → frozen threshold/action under cost and loss
```

Keep `intended`, `service_valid`, `trial_valid`, `grader_valid`, and
`substantive_success` denominators. If an operational-use estimand counts a
service failure as zero, predeclare that mapping and also report availability;
if a capability-conditional estimand excludes it, preserve the excluded row and
reason. Never let parser, judge, timeout, provider, or environment failures
disappear from the attempt ledger. Cross repeated agent outputs with repeated
grader observations on fixed artifacts, or retain an equivalent identifying
design, before attributing within-form label variance to the agent [SAE].

Cluster and version at least task, equivalent form, family/source lineage,
configured system, provider/time/batch, and grader. Binary outcomes have
probability-dependent within-form variance; unequal repeats need an estimator
that models unequal precision rather than only pooling within-task variances.
Report raw per-form frequencies and severe outcomes beside any variance
component. Stress-test all-success/all-failure boundaries, easy/hard-anchor
addition or removal, task-family stratification, grader repeats, and
operational-versus-valid-only missingness. A scalar that changes because the
task mixture widened while per-task behavior did not is benchmark-population-
relative, not agent-intrinsic [SAE].

The reviewed Stochastic Agent Evaluations paper correctly motivates repeated
task-level matrices, and its released rows permit exact checks of several point
estimates. But its implemented numerator is the variance of finite-repeat task
means without subtracting their within-task sampling contribution. The reported
ratio is therefore **not ICC(1,1)**, and its downward low-repeat curve is partly
an estimator artifact. Even a correctly estimated ICC answers a population-
conditioned variance-ratio question: deterministic failure can increase it, and
changing models changes the induced task-probability distribution. Mean effect,
within-form recurrence, severe-failure risk, grader stability, and decision loss
remain different estimands [SAE].

Choose repeat budgets from the decision: precision of a suite mean, uncertainty
in one form's success frequency, recurrent-severe-failure detection, a paired
intervention effect, rank stability, temporal/service drift, and variance-
component precision require different allocations. Freeze minimum and maximum
attempts, stopping statistic, precision/error or loss target, sequential error
control where applicable, service/missing behavior, task-versus-repeat
allocation, and held-out validation before calls. The paper's visually chosen
`8–16` and `≥32` waypoints from selected GAIA/FRAMES matrices do not transfer to
other task populations, configured systems, graders, or decisions [SAE].

### 3.3a Resource-sensitive criteria need an operating envelope

Executable artifact validity and criterion stability are separate. A workbook
may recalculate correctly while its latency classification changes by spreadsheet
engine; a semantically equivalent patch may pass tests while its speed advantage
changes by processor; a simulation, query, render, or model may remain correct
while memory, runtime, or numerical-tolerance status changes with workload and
environment. For every resource- or environment-sensitive criterion preserve:

```text
criterion target and unit → authoritative base/reference/candidate artifacts
  → engine, software, hardware, resource, and workload operating envelope
    → preparation, warmup, order, cache, concurrency, timeout, and repeat protocol
      → intended cells, repeated raw observations, and typed invalid-cell reasons
        → paired contrast, threshold margin, uncertainty, and transport evidence
          → aggregation, leverage, loss policy, and bounded decision
```

Environment identity therefore attaches both to each trial and to the evidence
that licenses the criterion. Keep semantic/artifact validity, directional
improvement, threshold attainment, and reference-level attainment as different
predicates. A near-zero contrast is fragile even when absolute variation is small;
report the task-level criterion margin against observed variation and the decision
threshold rather than promoting one historical crossing into a timeless label.
Type intended, started, infrastructure-invalid, functionally invalid,
measurement-invalid, and substantively below-threshold cells; do not encode an
invalid measurement as a severe substantive failure [POR].

Use four non-inheriting lifecycle states: **replayable** means the reference and
task execute; **criterion-valid here** means the reference meets the rule in one
declared environment cell; **transport-supported** means repeated and preferably
held-out bridge evidence preserves the criterion's interpretation over a declared
envelope; **decision-stable** means the intended comparison survives reasonable,
predeclared aggregation and stakeholder-loss policies. A strict intersection over
observed cells can be an intentionally conservative admission rule, but it is not
a transport probability or evidence about a new machine, engine, load state, or
date. Decompose task, environment, round/batch, and interaction effects where the
design supports it; otherwise report the pooled variation only as descriptive.

Aggregation remains a use policy. Show task-level influence or denominator share,
tail identities, threshold/floor sensitivity, invalid handling, and the loss model
that makes mean, median, harmonic, minimum, or noncompensatory treatment legitimate.
Fixed-output rescoring establishes policy sensitivity, not one universally correct
ranking. Portfolio coverage must name eligible configured systems, attempts,
scaffold dependence, cutoff, milestone, selection rule, cost, and joint execution
feasibility; a best-of-several historical union is not one system's capability.
**Saturation is independent of all four states** and is use-indexed: it additionally
requires a declared system or feasible portfolio population, attempt budget, time,
cost, exposure/contamination evidence, milestone, and renewal decision [POR].

The reviewed performance-optimization audit replays 740 official reference patches
from three purposively selected coding benchmarks on four cloud processor profiles
and three rounds. It provides bounded evidence of strict cross-cell reference-signal
loss, near-zero signal margins in one family, and ranking/leverage sensitivity under
fixed-output rescoring. Its absent study release, coarse invalid-cell typing, four-
profile/nonreplicated-host frame, three rounds, pooled variation, selected public
outputs, and no repeated agent trials block machine-invariant validity, causal rank,
portfolio-capability, prospective-saturation, professional-quality, production, or
readiness claims [POR]. Existing benchmark-bundle, execution-validity, task-health,
metric-monitoring, artifact-admissibility, response-matrix, and validity-argument
machinery are the durable homes; no performance-specific contract follows.

Keep three commonly collapsed reliability objects distinct: **empirical repeat
reliability** over matched attempts, **predicted success for one trial** from an
evidence view available at a declared decision time, and **supported causal
diagnosis** of an outcome. A predictor may rank failures while naming no valid cause;
a repeat rate may be valid but useless for choosing which current artifact to review;
and a diagnosis need not be a calibrated probability [ACC, ST]. A derived-confidence
record therefore binds task/trial/configuration and trajectory hashes, target
predicate and label authority, prefix versus post-hoc time, available channels,
extractor/tokenizer/provider/logprob semantics, missingness, calibration population,
transport boundary, uncertainty, and prohibited interpretations. Unavailable or
incomparable logprobs yield `insufficient_evidence`, not zero or a silently
substituted verbal score.

A perturbation is an instrument with two defeasible warrants: a **preservation
claim** that the intended requirement and difficulty remain invariant, and an
**exposure claim** that its type and intensity represent a declared operating
profile. Record transformed loci, independent semantic/metamorphic evidence,
applicability, intensity, and source distribution. Invalid variants are instrument
defects. In fault trials, retain injection, delivery, wrapper retry/recovery, agent
retry/fallback, latency/cost, and final consequence separately; harness-resolved
faults cannot establish agent recovery [AR].

Predictability also requires a decision point. A pre-task routing signal, in-run
escalation signal, and post-artifact acceptance signal have different evidence
views and licensed uses. Bind confidence method and fallback, signal time, available
evidence, frozen calibration population, threshold/action policy, coverage,
outcome horizon, and asymmetric loss. The reviewed study's five incompletely
controlled repeats, unvalidated paraphrases/fault exposure, retrospective
self-confidence, single-LLM severity judgments, unclustered dependence, and
unpinned experiment code demonstrate a diagnostic profile only—not cross-domain
ordering, prospective prediction, deployment risk, or certification [AR].

Agentic Confidence Calibration offers candidate post-hoc predictors for the middle
link: regularized logistic models over completed token-confidence summaries report
favorable cross-validated calibration/discrimination on eight benchmark samples.
Seven samples are mostly QA/reasoning; exact task/configuration and label lineage is
incomplete; nominal features include duplicates and format/budget proxies; tuning is
not clearly nested; dependence is unclustered; transfer is strongly asymmetric; and
code, trajectories, labels, splits, and calibrator artifacts are unreleased [ACC].
Its evidence supports candidate configured-trial prediction—not repeated reliability,
online warning, causal failure localization, workload reduction, professional
validity, safety, production fitness, readiness, or universal transfer.

Production self-report sits further upstream. MAP's accepted instrument and selected
cases describe bounded workflows, human verification, sensitive/proprietary context,
delayed labels, heterogeneous baselines, and mixed evaluator stacks. But its 20
production/final-pilot cases and main 86-response production/pilot survey frame are
network-recruited and outcome-conditioned; optional-question denominators range from
22 to 69, respondent/system/organization duplication is unknown, stages are pooled,
and no configuration, trace, artifact, reliability, or outcome is audited [MAP]. Use
this evidence to motivate portfolio conditions and tests, never to define a rubric by
prevalence or infer that a reported practice causes successful deployment.

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

An apparently successful execution channel can itself mask a substantive
failure. Represent `MASKED_BY` as a diagnostic relation between a supported root
condition or violated invariant and a surface signal that reports completion,
health, or success despite the consequential artifact/state remaining invalid.
Keep root-condition evidence, primary-channel status, an independent substantive
check, artifact/state consequence, agent verification, recovery, and residual
harm separate. A passing UI status, tool exit code, workflow close event, or
file-open check is not a substantive-validity verdict when its observer cannot
see the relevant invariant [LWT].

The relation is an authored causal/observability hypothesis until supported by
incident, intervention, or independently reviewed evidence. A graph traversal or
successful query proves only that an edge was encoded. Diagnose the earliest
supported root and misleading surface separately, retain `unknown` when the
substantive view is absent, and never promote channel success into artifact,
professional, safety, or readiness success [LWT]. Existing artifact-admissibility,
evidence-view, trace, task-health, root/surface, and validity records carry this
crosswalk; no masking-specific score or schema follows.

### 3.4 Intervention opportunities and causal attributions are different targets

A runtime signal, a proposed supervision action, and a retrospective causal label
answer different questions. Preserve one typed chain instead of treating an exact
trajectory index as their shared ground truth:

```text
candidate signal or opportunity at a frozen evidence time
  → acceptable event window and consequence-equivalent action/policy set
    → reviewer role, authority, evidence view, rationale, and repeated judgment
      → configured detector observation and threshold/capacity policy
        → executed intervention, participant response, and agent uptake
          → state/artifact change, delay, burden, and collateral effect
            → counterfactual consequence, repair utility, and stakeholder loss
```

The decision-time record must name `pre_action`, `post_action_pre_next`,
`post_artifact`, or retrospective audit; the exact trace/state prefix; latest
admissible event; excluded future channels; proposed-versus-executed action
visibility; latency; and expiry. A grader that sees the current action's resulting
observation cannot score a pre-action policy. Logical action index, wall time, tool
latency, authored schedule, decay/recovery, level-versus-edge semantics,
hysteresis, cooldown, and reset are independently versioned instrument components
[SAT].

Before computing detector accuracy, predeclare whether the target is an exact
mandatory gate, an earliest-warning/latest-safe window, a set of consequence-
equivalent interventions, a risk score plus threshold/loss/capacity rule, or a
framework-indexed distribution of legitimate reviewer policies. Keep exact-location,
window, and intervention-type agreement separate. Preserve reviewer qualification
and authority, evidence view, rationale, uncertainty, rubric version and
comprehension, intrarater repeat, and disagreement crux. Consensus can change the
target; sparse exact-index disagreement does not prove policy invalidity, while
high agreement does not prove benefit [SAT].

Detector agreement ends before intervention utility. Report candidate-opportunity
coverage, false interruption, missed severe boundary, executed intervention,
response and uptake, endpoint/recovery, latency, operator or participant burden,
introduced defects, and declared stakeholder loss as separate denominators. Where
the claim warrants it, compare no intervention, fixed checkpoints, deterministic
window/rule, detector policy, human policy, and sham/no-op interruption under
frozen task, system, environment, and evidence views. A level trigger over a
zero-decay accumulator is evidence about that configured policy, not a general
property of affect, risk, or supervision [SAT].

Retrospective diagnosis then follows a separate attribution ladder:

```text
declared construction intervention → first observed divergence
  → propagated surface failure → but-for effect under paired replay
    → earliest sufficient cause → natural multi-cause root
      → diagnosis-guided repair utility
```

No rung inherits the next. Preserve successful witness, full pre-state attestation,
all injection/replay/filter dispositions, repeated paired suffixes, original,
repaired, sham, unrelated, downstream-only, and dual-fault contrasts, dependency
edges, unresolved alternatives, and unaffected controls. Observer views such as
prefix-only, full trace, and answer-bearing are distinct instruments: endpoint
access can expose a symptom while anchoring attribution away from the earliest
supported divergence. A known injected step is a construction label; it is not
automatically a unique causal root or evidence that the same diagnosis applies to
natural failures [WWP].

The Saturation Trap supplies a useful negative case but only one 56-action coding
trajectory with three under-specified annotators. Its post-v1 release reproduces
sparse-label reliability while revealing that the reported replay hard-coded
`Δt=0`, disabling decay; it executes no intervention and measures no outcome,
burden, or loss [SAT]. Who&When Pro reports 12,326 endpoint-failing injected traces,
but success- and failure-conditioned selection, incomplete state equivalence,
single-mode labels, a label-visible 100-row human check, absent clustered
uncertainty, and an unreleased corpus/codebase bound it to synthetic
intervention-recognition evidence [WWP].

The internal 24-attempt, two-work-shape conformance replay retains one invalid
replay-diverged cell, recovered and dual-fault cases, and three frozen observer
views. It demonstrates only deterministic builder-authored behavior: local
construction-delta, first-divergence, propagation, and complete-cell paired-repair
semantics; `earliest_sufficient_cause` remains unsupported and
`natural_failure_root` prohibited. Its answer-bearing rule collapses eight upstream
failures onto surface checks by construction, so it calibrates observer-view and
fail-closed contracts rather than auditor capability or natural diagnosis [IAR].
Existing configured-system, trace, root/surface, recovery, participation,
task-health, metric, artifact/state, and validity records are the durable homes;
no timing-, affect-, or injection-specific schema follows.

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

A problem frame is a third object: it names or narrows *what situation is
present*, while a skill prescribes *how to proceed* and a rubric exposes *what an
observer will reward*. Estimate recognition with situation-only versus minimal-
frame conditions, execution support with minimal-frame versus fully specified or
procedurally guided conditions, and evaluator-cue effects with independent versus
shared/disclosed instruments. Do not call any one contrast an undifferentiated
expertise-transfer effect [KW].

A declared package condition also does not establish that the intervention reached
the solver. Preserve a **Skill realization and claim ladder**:

```text
package/version and mounted subset → surfaced module and opened spans
  → invoked procedure/script/resource → semantic adoption or justified rejection
    → attributable trajectory/artifact change → shared-source criterion conformance
      → independently observed substantive outcome → held-out transfer
        → professional validity and readiness
```

Record router candidates/scores, model-visible bytes, invocation inputs/outputs,
instantiated or rejected prescriptions, changed loci, and independent checks. Cross
the package treatment with independently authored and shared-source criteria: a
task-matched procedure can genuinely improve completeness while also making
rubric-recognizable structure easier to emit. Package availability, mounting,
surfacing, opening, invocation, adoption, conformance, correctness, and transfer are
therefore non-inheriting observations [MSK].

The reviewed medical Skill study is a sharp negative calibration case. Its linked
pre-v1 package contains 141 `SKILL.md` files and an exact task-family planner, but
the executed commit/subset, routing, opened modules, invocations, and 21 run records
are unavailable. Its 9 native and 12 OpenClaw-plus-package outputs come from one
task under unequal model weights and a bundled platform treatment. The reported
expert overall-quality difference is `+0.39` with an output-bootstrap interval
crossing zero; single-rating expert ICC is negative. This is selected configured-
package and noisy perceived-quality evidence—not an identified Skill effect,
substantive biomedical correctness, transfer, expert equivalence, or readiness
[MSK]. Rater reliability is part of treatment-effect identifiability: design the
estimand over model, task/form, run, criterion, and rater populations before adding
agent repetitions, and preserve criterion-specific disagreement rather than
assuming two-rating averages repair an unstable instrument. Unlike a deliberately
linked many-facet panel with repeated raters and forms, this two-rater, one-task
sample cannot support stable severity adjustment or task/rater generalization [MF].

For adaptive systems, also pin stream order/seed, warmup, similarity groups,
reset cadence, update budget, and which feedback may enter memory. Once one test
item changes behavior on the next, the estimand is ordered-stream learning, not
independent pass@1 [ACE, SE].

#### Skill and memory value is a resource-allocation claim, not a score delta

Keep four non-inheriting estimands separate: **configured-package frontier**
compares complete systems over realized resource vectors; **equal-envelope
allocation effect** reallocates the same enforced admissible envelope between
direct observe/act and augmentation; **module mediation** follows candidate
generation → evidence-sufficient verification → promotion → retrieval/presentation
→ invocation/adoption → local and downstream effect; and **amortized portfolio
value** charges discovery, serving, maintenance, repair, expiry, transport, and
parallelism over future eligible use. A package can lie on an observed frontier
without identifying an allocation effect, and an online cost comparison cannot
settle offline amortized value [OSM].

Every comparison needs two typed denominators. The **opportunity denominator** is
the task/form × environment/interface/version population on which the intervention
could validly apply. The **complete-resource denominator** charges prompt,
completion, cache and reasoning tokens; injected context; direct and auxiliary
calls; tool use; wall time/latency and parallel occupancy; compute/price/energy;
storage; retries, verification and repair; maintenance; and human review under a
declared basis. Preserve phase-resolved observations rather than dividing an
aggregate usage total. Pin task/block order, initial and final shared-state hashes,
configured-system and component hashes, budget-enforcement rule, and every intended,
invalid, missing, retried, or replacement row.

Retry is itself a treatment when a stateful online method can learn from the
replayed episode. Predeclare retry-in-place, null transition, or checkpoint replay;
record when the retry enters the stream and the resulting state hash. Likewise,
finite three-run `Any-of-3` and `All-of-3` are optimistic union and stringent
intersection repeat profiles under one order/environment policy—not latent-
capability bounds. The reviewed web study supports only a reported sparse
configured-package success–token frontier: budgets were approximately rather than
exactly matched, its stronger vanilla arm bundled extra steps with observation
pruning, methods differed beyond module type, order was undisclosed, only three
runs were used, and no code, task order, states, trajectories, or analysis release
exists. It does not establish fixed-budget allocation dominance, general Skill or
memory value, amortized value, web-to-knowledge-work transport, or readiness [OSM].

The internal allocation-parity audit retains and hash-checks all 14 intended rows
from two prior Skill studies, including four service-invalid cells, but finds zero
admissible exact contrasts because component allocation, state hashes, and exact
order matches are absent [SAPA]. Its prospective telemetry slice validates a
fail-closed capture envelope and AB/BA schedule without provider calls; aggregate
Hermes usage lacks per-call phase attribution, so readiness remains false rather
than fabricating allocation evidence [PAT]. These are validation artifacts for the
existing configured-system, procedural-skill, longitudinal, lesson-promotion,
trace/recovery, metric, and validity records—not a new Skill-value schema.

### 4.0 Projection independence and external authority set the claim ceiling

Co-derived components can agree because they share a projection, not because the
projection is useful or true outside itself. This applies whether one source
procedure generates the demand, task, and rubric; later behavior nominates a hidden
requirement; or one language model authors state, emits observations and faults, and
judges the resulting trace. Preserve a **projection-independence matrix** with
separate identities and authority for source procedure/behavior, demand evidence,
task author, goal oracle, state/transition/observation/fault authority, instruction
instrument, grader, equivalent-form author, affected-party reviewer, professional
reviewer, and release decision. For every pair, record shared text, model, human
author, organization, examples/calibration data, and outcome visibility [ASAS, MSB,
OB]. Literal non-overlap or separate API calls do not establish semantic
independence.

Use one ordered claim ladder and stop at the highest evidenced rung:

```text
shared-projection conformance
  → independently grounded efficacy on fixed external demand and goal evidence
    → equivalent-form transport across author/environment/verifier boundaries
      → affected-party consequence under current authority and consent
        → professional validity for a declared work population and decision
```

The first rung is legitimate and useful for calibration: it asks whether a
configured solver follows an authored package under its own contract. The second
requires demand and a goal oracle not supplied by the intervention. The third
requires frozen held-out forms and materially independent projections. The fourth
requires attributable realized outcomes plus the represented person's or legitimate
proxy's current authority, correction, and acceptance. The fifth additionally needs
professional source/transition authority, sampling and assembly warrants, calibrated
decision thresholds, and transport evidence. Predictive behavior is not current
authority; simulator/verifier agreement is not state truth; equivalent-form score
agreement is not affected-party benefit.

Agentic Skills at Scale supplies 1,110 inspectable Skill-derived packages from 608
declared top-level Skills, rather than the paper's approximate 1,000/500, but omits
the roughly 38,000 reported trajectories and the typed status of roughly 4,000
nominal cells absent from the 42,180-cell frame. Its positive paired deltas therefore
support treatment responsiveness under a shared projection, not independent Skill
utility [ASAS]. MapSatisfyBench contributes a useful author-time firewall—future
behavior may nominate a factor only when pre-response evidence could support it—but
its selected private logs, hindsight-conditioned gold factors, hand-set weights,
stochastic passive user, absent represented-user consent, and unreleased instrument
do not validate current intent or acceptance probability [MSB]. OccuBench's 382
released packages cover 98 administered scenario labels from a 100-row frame; its
implicit stochastic state, prompt-requested unmatched faults, and default shared
simulator/verifier support synthetic closed-loop conformance rather than occupational
or real-environment validity [OB].

**Invariant:** no shared-projection result may be promoted to efficacy, transport,
affected-party consequence, or professional validity without evidence at the missing
edge. Use existing source/projection, participation/authority, configured-system,
artifact/state, execution, task-health, metric, trace, and validity records; this is
a cross-record claim boundary, not a new schema or domain-specific subsystem.

### 4.0a Participation is a typed configured treatment, not a social-role label

Separate a participant's assigned role from its realization: `real_human`, model
simulator, scripted policy, hybrid, or replay. Pin the realization's model/prompt,
profile/private state, sampling, availability, and failure policy. Represent the
participation policy as independently versioned prompt/protocol, visible nodes,
channels/tools, information access, action authority, initiative trigger, control
threshold, interaction budget, and observer. An ordinal “agency level” is not an
identified treatment when several of these change together [HAS].

Every authority-bearing event should retain participant/role, observation basis,
channel and trigger, requested information or action, decision right and scope,
response, latency/expiry/failure, agent uptake evidence, environment consequence,
burden, and observer view. Report four rungs separately: **availability** (could
participate), **exercise** (did participate), **uptake** (was the contribution
used appropriately), and **effect** (changed an outcome against a valid matched
counterfactual). Simulator calls/tokens are system cost, not human active/waiting
time, interruption, cognitive demand, correction work, privacy exposure, or
accountability. A scenario-quality review does not validate simulator behavior or
process judges. HAS-Bench provides this vocabulary but its model-backed users,
single-run cells, bundled policy contrasts, unreported judge audit, and unverifiable
release restrict it to synthetic configured-collaboration evidence [HAS]. Existing
configured-system, trace, metric, task-health, validity, and expert-participation
records are the implementation homes; no parallel subsystem is implied.

#### Interaction episodes require link-level evidence

A channel or authored phase creates an **opportunity** to interact; it does not
establish that interaction occurred, carried legitimate authority, changed the
agent's plan, improved the result, or justified participant burden. Preserve one
linked episode without collapsing its observations:

```text
authored opportunity → trigger realization → call/message
  → participant identity, evidence view, and authority → answer
    → agent receipt → semantic adoption or justified rejection
      → pre/post state preservation and repair → endpoint effect
        → participant burden → recipient uptake → downstream consequence
```

Each arrow may be `observed`, `unsupported`, `invalid`, or `not_applicable`.
Participant availability, channel exercise, answer quality, semantic uptake,
state repair, endpoint conformance, burden, recipient acceptance, and consequence
remain separate metric populations. An endpoint conjunction cannot retrospectively
prove timely clarification, correct authority routing, adoption, preservation, or
net collaboration value. Likewise, simulator calls/tokens are system cost rather
than estimates of human waiting, interruption, cognitive demand, correction work,
privacy exposure, or accountability [DC, HAS].

Store the trigger's clock and meaning independently. Clock types include
`environment_action`, `model_turn`, `wall_time`, and `authored_schedule`; semantic
triggers include inspected state, completed subtask, decision boundary, and risk
signal. Record intended type, observed event locator, threshold, observer, timing
error, duplicate/missed firing, and whether the trigger was causally responsive to
agent state. A fixed early turn is a reproducible schedule, not evidence that a
meaningful interruption, error, or repair boundary occurred [DC].

Causal interaction claims require matched versions that hold task, public basis,
environment, grader, budget, and configured agent fixed while crossing, where
licensed: full information; missing information with no channel; the same missing
information with a scripted answer; simulator-mediated answer; and a consented
human answer. Add unnecessary-ask, wrong-authority, stale/contradictory-answer,
justified-rejection, and simulator/environment-invalid neighbors. Report channel
availability, call precision/recall and timing, semantic uptake, changed/protected
state, endpoint effect, burden, cost, invalidity, and task/participant-clustered
uncertainty separately. Human-versus-simulator parity requires its own evidence;
neither a social-role label nor a natural-language message supplies it.

DeskCraft makes native artifact checks and 152 authored phased packages
inspectable, but the exact paper-time implementation is unavailable: the only
public commit before v1 contains a license, while the audited 538-package release
is 30 days later and has no trajectories or result corpus. Its predominantly early
fixed triggers, task-conditioned ask tool/prompt, stochastic simulator realization,
disjoint standard/interactive sets, endpoint-only scoring, single-run cells, and
absent burden/recipient evidence support configured endpoint conformance under an
authored phase protocol—not proactive clarification, causal interaction benefit,
human collaboration, professional validity, capability, safety, production
fitness, or readiness [DC]. Existing authority/participation, trace, artifact-state
transition, task-health, metric, and validity records host the episode; no desktop-
specific schema follows.

#### Semantic diffs are review artifacts, not evidence of effective oversight

An operation-level explanation can reduce inspection burden relative to a surface
cell/file diff, but it is itself a fallible model-produced artifact. Preserve three
separate validations: **diff fidelity** to authoritative pre/post state and
dependencies; **oversight utility** under matched defect opportunity; and
**consequence validity** of the accepted or rejected intervention. Use the linked
chain:

```text
semantic-diff availability → exposure and inspected locator → comprehension
  → matched defect opportunity → supported detection and diagnosis
    → authorized intervention → agent receipt and adoption or justified rejection
      → intended changed locus → independent correction check
        → collateral-state preservation → reliance and burden
          → recipient acceptance and consequence
```

Hash the raw pre-state, proposed semantic operation, stated rationale/dependencies/
scope, actual transition, branch, and post-state. Type issue source and authority;
keep tool-suggested and human-discovered defects separate; admit `incomplete`,
`contradicted`, and `insufficient_evidence`; and measure review time, attention,
latency, verification, rework, and introduced defects. Self-reported understanding,
feature use, attempted steering, a changed branch, or a higher endpoint score cannot
fill missing links [PISTA].

Pista supplies bounded evidence near the first links: in one bundled, counterbalanced
two-task study (`N=16`, mostly graduate students), participants reported greater
inspectability/control, produced more elaborate explanations, used branching often,
and prompted less. The treatment jointly changed decomposition, explanations,
requirements/questions, local edits, branching, and model-call topology; defects
were stochastic and unmatched; no proposition-to-correction lineage, independent
artifact replay, collateral-preservation test, or recipient consequence was
reported; mean requirement success remained low (`0.53` versus `0.50`) without an
equivalence test. Pre-v1 implementation archives establish mechanism availability,
not study-build correspondence or semantic-diff faithfulness [PISTA]. Read this as
a decision-time representation hypothesis beside DeskCraft's interaction episode,
AgencyBench's evaluator-assisted repair path, and artifact evidence-packet work—not
as general oversight, calibrated reliance, professional utility, or readiness.

#### Simulator fidelity needs information sufficiency before consequence promotion

A participant simulator is an instrumented realization, not a transparent proxy
for a person. Keep five claims separate: **communicative fidelity** (style, pacing,
affect, and disclosure), **assigned-goal fidelity** (consistency with an authored
objective), **one-step state-transition fidelity**, **free-running decision/stopping
fidelity**, and **consequence fidelity** (transport of policy rankings, effects,
burden, harms, and outcomes to real participants). Evidence for an earlier claim
does not license a later one. Preserve the typed ladder:

```text
participant realization and target population/stakes
  → authorized observable context at the decision time
    → observable-state sufficiency for the claimed latent target
      → one-step transition fidelity under matched histories
        → free-running state persistence, stopping, silence, and terminal fidelity
          → agent-policy ranking/effect transport
            → authorized real-participant consequence
```

For every rung, bind participant/population unit; stakes and outcome window;
context provenance, valid time, consent/privacy basis, and actor-specific evidence
views; target state and independent label evidence; simulator model/prompt/profile,
sampling, retries, failure and non-response semantics; observer; discrepancy
estimand; clustering, censoring, missingness, and invalid policy; and supported and
excluded claims. A simulator may legitimately estimate a population-level
distribution such as `P(response | authorized observable context)` when the context
cannot identify one person's private motivation. That does not license
person-specific latent-state reproduction. Conversely, adding an outcome-bearing
proxy can improve prediction while invalidly revealing future or private state.

Outcome-conditioned discrepancy is a useful **falsification**: it can reveal that
marginally plausible simulation concentrates error among people who later refuse,
withdraw, or experience harm. It does not identify whether the source is missing
behavioral support, insufficient observable state, or an outcome proxy that mixes
unobserved causes. Nor does an action-conditioned discrepancy identify a tactic's
causal effect when agent actions respond to prior participant state. Policy-effect
or production-agent claims require matched or randomized policy comparisons under
simulator and consented real/replay conditions, with preserved stopping and real
consequences.

The reviewed payment-linked production-dialogue study is strong evidence for this
claim boundary, not for a validated user model. Its same-prefix probes isolate a
one-step response operator and report larger engagement-positive bias among
eventual non-payers under simulator, prompt, and LLM-instrument swaps. But the one
Chinese matchmaking-sales corpus, future-outcome stratification, unspecified
non-payment censoring and customer clustering, teacher-forced probes, unvalidated
state/action instrument, unavailable claimed release, incomplete consent/privacy
evidence, and observational tactic analysis block person fidelity, free-running
fidelity, causal tactic, policy transport, production-agent, cross-domain,
professional-validity, safety, and readiness claims [USDF]. Existing configured-
system, participation/consent, trace, longitudinal transition, task-health, metric,
and validity records host this ladder; no simulator-specific schema follows.

### 4.0b Feedback is a role- and channel-specific intervention

Feedback can be ecologically legitimate support—a client's correction, a test
failure, or an observed operational consequence—and still be an experimental
intervention. Keep it separate from evaluator-only measurement and record the
full chain rather than labeling a run merely `with_feedback`:

```text
public/environment evidence + private evaluator observation
  → private decision → released signal fields
    → participant/simulator evidence view → feedback proposition and authority
      → executor-visible message → uptake → action/artifact/state delta
        → current outcome + retained state + later consequence
```

Do not collapse distinct information treatments into `with_feedback`. Preserve at
least six estimands: **unaided first attempt**; **retry with no new information**;
**generic revision request**; **consequence-only feedback** from an admissible
observer; **criterion-level evaluator disclosure**; and **authorized ecological
feedback** from a participant whose evidence, decision rights, burden, and stopping
policy are validated. The first is bounded unaided capability; the middle four
progressively mix additional inference with stronger benchmark information; only
the last can support a collaboration claim, and only within its validated
participant/channel population. A self-correction claim additionally requires the
target to identify the defect without evaluator disclosure [AGY].

For every released defect proposition, retain source and evidence locator,
authority, public/private status, information delta and target disclosure;
executor receipt; supported adoption or rejection; changed artifact/state loci;
criterion-specific admissible re-observation; repair disposition; collateral
regression; endpoint/stopping reason; added tokens, time, money, and reviewer
burden; and invalid/service outcomes. A before/after score alone cannot show that
the proposition was received, caused the relevant change, or repaired the
construct rather than the judge. First, final/current, best-so-far,
threshold-reaching, and attempt-averaged outcomes are separate aggregations, not
interchangeable summaries [AGY].

Hash executor, supervisor/evaluator, simulator or human participant, rewriter,
observer, task, and environment independently. For every channel preserve its
source authority; agent/evaluator visibility; exact payload fields and
cardinality; granularity, latency, cadence, and adaptive query budget;
stochasticity and seed policy; disclosure to the agent; and a leakage rationale.
Classify each released proposition as public-entailed, independently visible,
private-signal-inferred, hidden-criterion-equivalent, new authority-bearing
preference, or non-informative. Filesystem separation is not semantic separation:
a score, status, continuation decision, or benchmark-shaped critique can expose
private reward gradients [UC].

State persistence is a second treatment axis. Record whether context, files,
artifacts, feedback history, plans, and learned procedures survive each turn or
restart; pin compaction and stop/resume policy; and include reset, irrelevant-
feedback, corrupted-feedback, and no-authoritative-feedback controls where the
claim requires them. Improvement under a persistent feedback loop estimates the
configured package—executor × adaptive search × feedback bandwidth × retained
state × evaluator robustness—not unaided capability or a generic learning rate.
An unrequested-opportunity/proper-nonintervention contrast is additionally
required before calling repair after an explicit request **proactivity** [UC,
EDGE].

Longitudinal reporting must retain first-attempt, endpoint/current, fixed-cadence
hidden, and best-so-far outcomes separately, plus time-to-threshold, submissions,
cost, new errors, run-at-risk counts, censoring, invalidity, and service incidents.
Best-so-far is a selection estimand that rewards search and suppresses regression;
it must never overwrite current quality. Smooth macro-averaged best-so-far curves
may support a suite-specific budget forecast after task-cluster uncertainty and
held-out validation, but not a task-level mechanism or universal learning law.
EdgeBench supplies high-value dual-channel harness and evaluator-hacking evidence,
yet its selected 134-task frame, 51-task category-shifted release, heterogeneous
normalized scores, valid-run filtering, bundled scaffolds/state, absent raw
trajectories, and nearly tied sigmoid fits bound its claims [EDGE]. UniClawBench
supplies an inspectable executor–supervisor–simulator repair loop, but explicit
requests, synthetic follow-ups, no feedback ablation, partial observer views,
single runs, unreleased result records, and unvalidated semantic non-leakage block
proactivity, natural-user, causal-repair, root-cause, and readiness claims [UC].

AgencyBench makes the proposition-to-revision path unusually inspectable across
cumulative native artifacts, scripted interactions, text/visual evidence views,
observer reasons, and later attempts. Its strongest bounded construct is
**criterion-disclosed evaluator-assisted repairability**, not unaided autonomy or
real-user collaboration. The sole January release predates immutable April v4 by
three months and differs from it in feedback generation and score aggregation;
main results appear single-run with ambiguous task/scenario denominators; human
simulator and judge labels are unavailable; and no real user supplies authority,
burden, acceptance, or stopping behavior. In the released samples, text and vision
observers see non-equivalent views and differ by at least four points on 23/102
pairs, while the vision prompt adds an undisclosed aesthetics obligation. These
facts require criterion-view admissibility and public-basis checks before any
observer score or feedback is treated as valid repair evidence [AGY]. Read this
with UniClawBench's private-supervisor/public-simulator split, EdgeBench's visible
versus hidden channels, DeskCraft's phased interaction ladder, HAS-Bench's typed
participant authority, SciVisAgentBench's artifact-view admissibility, and the
user-simulator decision-fidelity ladder; none licenses promotion from fluent
critique to ecological feedback or consequence.

The internal two-shape feedback audit exercises four feedback arms over 24
deterministic builder-authored cells; its frozen report (SHA-256
`20deddde50fd93fc32b7af5b8f7eb69b9e9ffdab71c9cc3dd1ea421a41e335be`)
records proposition labels, uptake, repair, leakage, and new errors. Its six-case
adaptive red-team report (SHA-256
`0b9f068dfdc9d2b808caa761090415dab294b9eb15ed84dbca49d74f43a30339`)
exercises query-budget, repeated-seed, and current-versus-best checks [CF]. These
are internal contract/replay evidence only—not expert or participant evidence,
general exploit-detection accuracy, agent learning/capability, professional
validity, causal feedback benefit, production fitness, or readiness. Existing
information-flow, configured-system, trace, task-health, longitudinal, metric,
plural-judgment, and validity records suffice; no parallel feedback schema is
justified.

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

#### Adapter interoperability is not measurement equivalence

For benchmark-family adapters, split configured evaluation into three records:

1. **Canonical benchmark contract:** native task/split, upstream dataset/package,
   evaluator composition and evidence views, backend image/state, seeds, and
   intended defaults.
2. **Adapter realization:** independently versioned field/action mappings,
   observation transforms, reward/termination/error translations, defaults,
   unsupported or dropped semantics, and adapter-specific dependencies.
3. **Trial policy:** scaffold/model, information and action treatments, budgets,
   parser and infrastructure retries, invalid/replacement rules, reset evidence,
   score inclusion, and aggregation.

A shared `reset/step/reward` transport makes trials runnable, not scores
exchangeable. BrowserGym's inspected MiniWoB, WebArena, AssistantBench, and later
WebArena Verified adapters preserve different evaluator meanings while sometimes
changing viewport, trajectories, parsing, error handling, and component-status
visibility. The official snapshot is from 2026, not the 2024 manuscript-time
implementation; exact paper reproduction and native/adapted equivalence remain
unavailable [BG]. Treat all defaults as interventions, keep typed component and
invalid statuses instead of flattening them to ordinary zeros, and retain every
attempt, retry cause, reset attestation, replacement, and inclusion decision.

Semantic-preservation claims require native-versus-adapted differential cases
from the same frozen state, comparing score, termination, side effects, evaluator
evidence, and invalid classification. Until those pass, aggregate only within a
declared family/score contract with cluster- and repeat-aware uncertainty. A
common runner alone cannot license a pooled capability scale, safety/isolation,
professional validity, or measurement equivalence. Existing configured-system,
execution-validity, task-health, metric, validity, artifact-view, and trace
contracts are the implementation homes; no parallel adapter schema is implied.

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

### 4.4a Delayed obligations are dual-task state transitions, not memory labels

A delayed requirement is useful only if it is executed at the authorized time
without silently degrading the work it accompanies. Preserve two outcome families
and the links between them:

```text
instruction source/authority → encoded obligation → update/supersession
  → cue availability → monitoring request → harness-observed access/release
    → presented evidence → adoption/rejection → due-status and timing decision
      → intended action → realized state/consequence
        × primary artifact/workflow quality, preservation, collateral loss, and cost
```

Encoding/retention, cue monitoring/access, update reconciliation, due-status
inference, timing, intended action, realized action, obsolete/lure commission, and
primary-work preservation are non-substitutable observations. A self-reported
obligation state is an output field, not direct evidence of internal memory. A
neutral interrupt, channel hint, task reminder, and oracle-derived cue are distinct
evidence treatments; privileged evaluator state must never be described as a memory
aid. Report shapes separately and do not infer a treatment effect from unmatched or
single-attempt cells [PMB, DOT].

PM-Bench makes the obligation state machine, hidden cue channels, lures, updates,
timing, and deterministic replay unusually inspectable, but its compulsory `A/B/C`
advance token is ungraded. It therefore observes obligation-menu selection, not
concurrent-work preservation or interference [PMB]. The frozen internal v1 dual-task
pilot added graded primary work and retained six of six service-, environment-, and
artifact-valid single attempts. All 18 primary-turn checks passed, creating a
primary-work ceiling; four cells were exact successes, while the vendor neutral
cell failed at cue monitoring/access and the vendor oracle cell failed at due
status/timing [DOT].

The prospectively frozen v2 extension then crossed two unseen forms in each of the
same two purposive synthetic work shapes with all three conditions. All 12 intended
attempts were retained and service-, environment-, and artifact-valid, yielding 36
turn artifacts. Exact obligation outcomes were six successes, three cue-monitoring/
access failures, and three due-status/timing failures. Primary work passed 35/36
turns: the one wrong turn-1 decision under an oracle condition is a non-ceiling
witness that the primary branch can register concurrent loss, but the 35/36 rate
remains near-ceiling rather than an interference estimate [DOT2].

V2 directly records submitted query issuance, next-turn channel availability,
exact returned update evidence, public due-cue presentation, and oracle
presentation. It still does not observe internal encoding or adoption; agent-
reported obligation state and intended actions cannot fill those gaps. In the four
neutral cells, three attempts issued no query and received no update, while one
queried and received it. All four channel-hint attempts queried and received the
update. Every oracle attempt received privileged evaluator-derived update/due
evidence regardless of its query path, so an oracle reminder is an evidence-access
treatment, not a memory aid. Preserve each exact form × condition cell: v1 and v2
must not be pooled, and neither sparse one-attempt matrix licenses treatment effects,
internal-memory attribution, cross-domain generality, professional capability,
safety, production fitness, or readiness [DOT, DOT2].

**Stop/continue gate:** stop repeating this matrix merely to accumulate attempts.
Continue only after independent or expert review of form and rubric realism and a
preregistered repeated design that names the estimand, unit, cluster structure,
contrast, invalid/service policy, uncertainty method, and decision use. Otherwise
retain v1/v2 as bounded machinery validation. Existing evidence-flow,
artifact/state, configured-system, trace, task-health, metric, and validity records
are the implementation homes; no memory-specific schema or additional worker task
follows.

### 4.4b Plan carriage is a proposition-to-consequence experiment, not a latent scalar

Plan-span visibility, a representation contrast, recoverability, free behavioral
use, endpoint consequence, and context-policy utility are different observations.
Atomize every plan into versioned obligations with source span and authority,
prerequisites, acceptable alternatives, live/completed/superseded state, required
evidence, and downstream action/check IDs; then preserve this ladder:

```text
obligation proposition and authority
  → decision-time visible source span and derived restatements
    → matched omission/corruption/irrelevant/restoration treatment
      → proposition-specific representation or recoverability
        → freely chosen action distribution and obligation adoption
          → realized artifact/state consequence
            → exact context budget, cost, policy reliability, and bounded transport
```

The context-treatment record must pin the configured actor, context operator and
budget; every model-visible view and hash; source, summary, scratchpad, reasoning,
memory, rationale, and tool-derived copies; treatment loci and matched-capacity/
position controls; forced versus free continuation; proposition-specific observer
and grader view; action, artifact, state, invalidity, and resource outcomes. Removing
the original span does not make the treatment absent when a derivative carries the
same proposition. Conversely, broad trace stripping changes more than plan content.
An information-flow audit must therefore disposition original and derived views in
both arms rather than infer absence from the intended operator [PDP].

Forced-prefix replay is an observer experiment: holding actions and observations
fixed can isolate a history perturbation, but deliberately blocks behavioral
adoption and consequence. Last-token cosine distance is representation sensitivity,
not proposition recovery or durable hidden state across calls. Pair it with free-
action twins from the same frozen prefix and cross exact/paraphrased, neutral,
irrelevant, corrupted, omitted, contradicted, and restored clauses at matched
capacity. Separately sweep plan-only, state-only, plan-plus-current-state,
re-observation, summary, and full-context policies with exact visible-token ledgers
and task-clustered repeats.

Plans Don't Persist supplies bounded manuscript evidence that removing the full
guard-plus-plan exchange changes final-token representations strongly on the first
forced call and less at later fixed prefixes, that retained reasoning traces can
reintroduce treatment-related text, and that a severe recent-four-message policy
reduces reported ALFWorld success while static plan retention/reinjection does not
repair the broad history loss [PDP]. The treatment mixes content, length, position,
turn and discourse; phase is strongly decodable; forced replay discards control
outputs; the endpoint policy also removes observations, actions and working state;
and no empirical artifacts were released. These experiments cannot be joined into
plan forgetting, causal action, context-policy, professional-validity, safety, or
readiness evidence. Existing obligation, configured-system/context-policy,
evidence-view, trace, artifact/state, metric, task-health and validity records are
the durable homes; no plan-persistence contract follows.

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

### 4.5a Procedural adaptation is a typed source-to-target transfer edge

A revised procedure has no context-free “transfer score.” Keep four estimands
separate because each changes a different boundary:

| Edge type | Source/target relation | Bounded interpretation |
|---|---|---|
| Source-context gain | same task/form, work context, solver, and harness before versus after revision | local adaptation under the observed feedback/update policy |
| Equivalent-form cross-task reuse | held-out task forms share a declared operation while task instance and surface evidence change | reuse within a frozen task/authoring population |
| Changed-context transport | intended artifact, audience/role, evidence authority, threshold, tool, verifier consequence, or obligations change explicitly | transport across the named changed primitives, not across a profession label in general |
| Cross-model consumption | a different configured solver/harness consumes the frozen revised procedure | package consumption by that target configuration, not model-independent knowledge |

The atomic record is a **versioned transfer edge** linking existing objects:

```text
source task/form + authoring lineage + active procedure hash
  + source solver/harness/environment + trace and feedback views
    → updater/configuration + candidate parent/child + changed clauses
      + validation/promotion/rollback history
        → frozen target task/verifier + authoring/overlap lineage
          + target solver/harness/environment
            → paired attempt/outcome distribution
```

For every edge retain the eligible, attempted, valid paired, invalid, missing,
and excluded task/attempt counts; target-verifier and metric identity; all
attempts and selection rules; task/Skill/author/verifier clusters; paired and
clustered uncertainty; cost; per-task deltas; negative-effect rate; worst-group
change; forgotten or contraindicated clauses; and prohibited claims. A positive
macro mean cannot erase forgetting or negative transfer. Promotion should use a
declared bounded-harm/non-inferiority gate on protected equivalent forms, not
only average source or validation gain.

Trace diversity and trace volume are separate treatments. Cross same-model
versus mixed-model sources with same-task versus mixed-task sources while
matching trace count, success/failure mix, and task coverage; include duplicated
or shuffled volume controls and multiple sampled source pools. Feedback derived
from private target checks is criterion-aligned coaching unless separately
authorized and measured; repeated validation requires equivalent-form renewal.

AFTER motivates this edge model but does not validate its reported transfers:
its static tables contradict their own `M1`/`M2` identities; the paper claims
382 tasks, the pinned post-v1 release contains 129 test packages, and refinement
uses 111 unexplained complete-case IDs; the reported 73.1% cross-model condition
omits the target solver, task/Skill and trace denominators, updater, attempts,
failures, and uncertainty; pooled traces confound diversity with volume and
coverage. Main configurations, traces, evolved procedures, promotion records,
and results are unreleased, oracle isolation is declarative, and author review
does not establish occupational or expert authority. The evidence therefore
supports a transfer-design vocabulary and an inspectable static substrate—not
expert transfer, occupational representativeness, professional capability,
production fitness, or readiness [AFTER]. Existing procedural-skill,
longitudinal-stream, configured-system, feedback-firewall, task-health, metric,
and validity records are the implementation homes; no new schema follows.

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
| Review-selection episode | preserve how a large trial/trajectory population became a bounded review sample and what later use it can support | population snapshot and clusters; detector/version; probability, overlap, missingness, evidence view; rater/adjudication lineage; sentinel versus enriched role; time/cost; licensed/prohibited claims; intervention/outcome links |
| Evaluator-attempt ledger | distinguish outcome-blind repair of invalid evaluator execution from outcome-conditioned reselection and substantive judge validity | immutable source/configuration identity; append-only raw attempts; typed invalidity, abstention, applicability, and insufficiency; predeclared retry eligibility/limit; frozen treatment or fork; final-selection and duplicate-publication semantics; residual-invalid and attempt-count denominators; schema/judge/metric/decision-validity separation |
| Criterion-to-outcome validation episode | prevent a same-episode association from being promoted to prediction, causal intervention, decision utility, or stakeholder benefit | criterion/observer/evidence-view identity and reliability; score time; eligible population/base rate/clusters; outcome authority/window/join/missingness/reversals; association and incremental baselines; frozen confirmation/intervention; threshold/loss; joint intended/adverse consequences; licensed claim rung |
| Operational reliability profile | keep capability, repeatability, perturbation response, predictability, and consequences interpretable under bounded conditions | configured system; task/form/family population; environment/provider/time/batch; intended/service-valid/trial-valid/grader-valid/substantive denominators; grader-crossed and matched clustered repeats; retry/missing policy; binary/unequal-repeat estimator and anchor sensitivity; frozen decision-keyed repeat/stopping rule; intervention preservation/exposure evidence; decision-time view; consequence/loss model |
| Resource-allocation episode | distinguish complete-package frontier, exact equal-envelope allocation, module mediation, and amortized portfolio value | opportunity population; complete phase-resolved resource vector and basis; direct-action counterfactual; task/block order and state hashes; candidate/promotion/retrieval/adoption/effect flow; every invalid/retry transition; amortization horizon, expiry, transport, maintenance, and bounded claim |
| Derived trial-confidence observation | preserve a prediction without overwriting the trial result, repeat profile, diagnosis, or decision | configured trial and target predicate; label authority; prefix/post-hoc time and available channels; extractor/calibrator/provider/tokenizer/logprob versions; missingness; calibration/transport population; uncertainty; prohibited uses |
| Candidate lesson store | improve authoring and systems without silent doctrine drift | provenance, feedback authority, scope, contradiction links, held-out promotion, rollback |
| Longitudinal stream | measure an update policy rather than independent pass@1 | frozen benchmark version, order/seed, clusters, persistence/reset policy, budgets, feedback firewall, equivalent-form probes |
| Benchmark change log | distinguish instrument drift from agent evolution | old/new component hashes, rationale, affected claims, bridge panel, compatibility/calibration decision, rollback |
| Evidence-state transition record | separate evolving world state, emitted claims, applicability, access/adoption, belief revision, and artifact consequence | authority/scope/valid-time, contradiction/supersession, update-to-check crosswalk, changed and invariant predicates |
| Task projection manifest | detect drift among public requirements, affordances, witnesses, and checks | evidence-backed requirement atoms, IR/sampler/projector/output hashes, bidirectional coverage, declared invariances, solver/validity separation, conformance tests |
| Suite assembly argument | distinguish a broad frame and healthy pool from the administered sample and licensed population inference | frame/content exclusions, eligible pool, selection/seed/order, lineage clusters, intended/realized mixture, weights, precision/stopping, invalid/missing policy, alternate-assembly sensitivity, bounded claim |
| Portfolio estimand | keep heterogeneous component evidence primary and make any suite scalar an explicit use policy rather than a latent capability claim | component construct and unit hierarchy; selection and configured-system/tool eligibility; evidence view/scorer/metric; plural denominators; clustering/uncertainty; raw resource boundary; weights, hard gates, missingness/loss policy, sensitivity, excluded interpretations |
| Candidate-defect lifecycle | route automated or human audit findings through adjudication, repair, and revalidation without rewriting history or laundering auditor authority | immutable instrument and auditor/evidence-view identity; path-grounded candidate; clean sentinels/known-defect controls; plural authority/disagreement; retain/quarantine/repair/retire disposition; changed loci and hashes; alternative-path and equivalent-form rerun; original/deletion/common-task/repaired-form sensitivity |
| Persistent-workspace record | distinguish file presence and authored relevance from observed or causal use while preserving state integrity | inventory/overlay hashes, placement and valid time, permissions/network, typed and alternate relations, evidence-view-bound access/write, protected/mutable zones, pre/post mutations, cleanup |
| Sparse workflow-transition record | distinguish one witness path and final state from run-attributable stage completion | pinned initial state, pre/postconditions, alternative paths, necessity/sufficiency, state delta, evidence views, downstream consequence, invalid-environment policy |
| Composite-workflow contract | distinguish executable chaining from supported workflow and planning claims | typed obligation DAG, produced/consumed state, equivalent paths, milestone/terminal split, reversal replay, validator cadence, reset attestation, atomic baseline, family clustering, workflow provenance |
| Context-treatment validation episode | distinguish source-span removal, derivative carriage, representation/recovery, free adoption, consequence, and policy utility without introducing a memory scalar | atomized obligation/version/authority; context operator and exact visible-view/token ledger; derivative information-flow audit; matched omission/corruption/irrelevant/restoration controls; forced observer and free-action twins; artifact/state/cost outcomes; task-clustered repeats and bounded claim |
| Role-versioned suite membership | distinguish coverage, regression, frontier, calibration, and retired uses of the same task | immutable membership hash, role/tier, admission evidence, outcome-selection flag and snapshot, exposure state, transition event, replacement bridge, retirement reason |
| Counterfactual artifact record | establish editability and behavioral integrity rather than current-value similarity | native/executable/rendered/trace views, pinned engine, initial-to-final mutation surface, authoritative perturbations, dependency propagation, invariants, permitted formula/layout equivalence, witness health |
| Action-safety record | distinguish source presence, attempted behavior, realized consequence, recovery, and useful completion | authority matrix, placement/exposure/adoption evidence, tool event, interceptor, pre/post state, severity/reversibility, residual harm, containment canaries, separate safety/utility outcomes |
| Reduced-evaluation use | bind any lower-cost panel, ordering, or stopping proposal to the estimand it may preserve | immutable full record and configured systems; `score`, `rank`, `pairwise_threshold`, `regression`, `diagnostic`, or `gate_preservation` use; threshold/loss; eligible overlap and typed invalids; selection/order/seeds; construct and critical strata; error/deferral/coverage targets; clustered uncertainty; replay/prospective status; expiry/drift triggers |

A reduced evaluation is **claim/use indexed**, not a generic task fraction.
Ranking, score estimation, thresholded pairwise selection, regression detection,
diagnostic localization, and preservation of noncompensatory safety/compliance
gates are different estimands. Mid-range checks can carry rank information while
rare hard checks remain strategically indispensable. Preserve the complete
response matrix first; then bind any reduced policy to its full-record target,
configured-system and eligible-task population, missing/invalid/overlap policy,
selection/order and seeds, grouping authority, hard-inclusion strata, error and
deferral denominators, tested budget grid, uncertainty, and expiry. Retrospective
replay compressibility is not prospective sequential stopping, future-form
transport, reliability, diagnostic sufficiency, or validation of the full-record
decision itself [EB, AP, PD].

A common suite runner establishes transport and operations, not measurement
commensurability. Component vectors and eligibility patterns remain primary;
portfolio aggregation is a versioned stakeholder policy over typed evidence.
AstaBench's incompatible component units, metrics, evidence views, custom/private
tool treatments, and cost boundaries make this distinction concrete [ASTA].

Task-health audit findings enter as candidates, not deletions. Static and
outcome-visible trajectory audits are distinct observer conditions; path citation,
maintainer action, expert adjudication, executable counterexample, and repaired
rerun are non-substitutable evidence. Preserve original scores and compare deletion
masks with common-task and repaired-equivalent-form estimands before changing a
capability claim. ABA's selected positive validation and absent clean-task/full-
corpus evidence support scalable triage, not autonomous invalidation [ABA].

## 6. Family map: what each benchmark pattern contributes

| Pattern / examples | Primary reusable object | Main validity risk | Evidence status here |
|---|---|---|---|
| Artifact-centered professional work (AA-Briefcase, MBABench, WorkstreamBench) | plural native/executable/rendered views, initial-to-final mutation surface, counterfactual integrity, and professional judgment | reference imitation, static-value coincidence, inherited-size inflation, unobservable charts/layout, engine drift, and weighted score mistaken for readiness | MBABench full immutable v4 paper plus inspected post-v4 code/data and two workbook traces [MB]; other family members remain landscape/triage |
| Stateful professional workflow (SaaS-Bench, Workflow-GYM, OdysseyBench) | pinned initial state, sparse consequential stage transitions, alternative paths, final-state and artifact checks | residual/pre-satisfied state, stage bypass, canonical-path bias, environment/harness defects, and final consequence mistaken for complete workflow evidence | Workflow-GYM full immutable v3 paper plus post-v3 official showcase/trajectory inspection, with full dataset/VMs/graders/results unavailable [WG]; SaaS-Bench has a separate full review; OdysseyBench remains landscape-level |
| Adversarial authority and action safety (ClawSafety) | source-authority matrix, exposure/adoption/action-state ledger, containment, recovery, and benign utility | source placement or token match mistaken for adoption/realized harm; refusal or tool failure counted as safety; mutable/live side effects | full immutable v2 paper plus complete post-v2 partial-release audit [CS]; internal inert conformance fixture/preflight validates contract behavior only [AC] |
| Skill-grounded long-horizon evaluation (LH-Bench) | expert procedure → observable boundary → artifact/check crosswalk | intervention/instrument contamination; agreement mistaken for validity | full immutable v2 PDF/text and deep review [LH] |
| Budget-constrained online Skill/memory packages | configured-package frontier, exact allocation episode, module-flow mediation, and amortized portfolio ledger | approximate budgets and compound controls promoted to allocation effects; presentation promoted to adoption; three-run unions/intersections promoted to capability bounds; retries and order-dependent shared state omitted | full immutable v1 paper/project-page review with no study release [OSM]; internal 14-row parity audit admits zero exact contrasts [SAPA], and the zero-call prospective capture envelope remains blocked on per-call telemetry [PAT] |
| Human-rated configured Skill package (medical Skill study) | mounted/surfaced/opened/invoked/adopted/artifact-change chain; model/task/rater estimand and criterion-specific reliability | available package mistaken for exposure; platform/package bundle called a Skill effect; shared structure and noisy Likert ratings promoted to expertise, correctness, or transfer | full immutable v1 paper/supplement plus timing-bounded 1,715-file package audit; one selected 21-output task, unequal arm/model mixture, absent run/exposure records, and negative expert ICC support a claim ceiling rather than efficacy [MSK] |
| Trace diagnosis and recovery (STRACE, LH-Bench recovery analysis) | dependency-aware causal slice; error→feedback→repair→verification chain | inferred root cause may be wrong; post-test optimization can leak | extracted-paper deep review [ST] plus LH-Bench full review |
| Psychometric operation (Efficient Benchmarking, Agent Psychometrics) | response matrix, difficulty/discrimination, reduced ranking panel, scaffold-aware analysis | historical population drift; ranking panel drops rare diagnostic coverage | extracted-paper deep reviews [EB, AP] |
| Continual/context adaptation and self-evolution (ACE; self-evolving-agent survey) | immutable local delta, candidate-lesson lifecycle, evolution-event ledger, retention/transfer stream | order dependence, weak-feedback pollution, private-test contamination, mixed-component attribution, benchmark/agent co-evolution | full immutable ACE v3 and survey v4 PDFs/text plus deep reviews [ACE, SE] |
| Procedural-memory transfer (AFTER) | typed source-context, equivalent-form, changed-context, and cross-model transfer edges with paired outcomes and harm gates | shared authoring/verifier lineage, feedback leakage, complete-case selection, diversity/volume confounding, missing configured-system identity, and macro gains hiding negative transfer | full immutable v1 paper plus pinned post-v1 release audit; 129 released test packages are inspectable, but the 382-task instrument, evolution machinery, traces, configurations, evolved procedures, and result rows are unavailable [AFTER] |
| Delayed-obligation dual-task evaluation (PM-Bench; internal pilot) | obligation state machine linked to harness-observed cue access, timed realized action, and separately graded primary-work preservation | ungraded nominal ongoing work, privileged reminders mislabeled as memory support, self-report promoted to access/internal-memory evidence, ceiling forms, and single-attempt cells promoted to causal effects | PM-Bench full immutable v1 paper plus pinned paper-time release audit [PMB]; internal frozen six-cell pilot and exact replay support instrument behavior and exact retained observations only [DOT] |
| Plan/context-treatment validity (Plans Don't Persist) | proposition-level obligation→visible and derived views→matched treatment→representation/recovery→free action→artifact/state consequence→policy cost ladder | broad span removal and last-token distance promoted to plan forgetting; derived-trace contamination; forced replay promoted to behavior; broad history truncation attributed to plan eviction | full immutable v1 PDF/text review [PDP]; manuscript-reported forced-prefix and compression evidence only, with no code, task manifests, trajectories, hidden states, prompts, or result rows released |
| Production agent evaluation (Anthropic, Amazon) | task/trial/grader/trace separation, task-health lifecycle, metric/monitoring contract, and operational failure taxonomy | engineering guidance may not establish construct validity; named metrics omit populations/estimands; synthetic and online samples drift | full official Anthropic and Amazon articles and concept reviews; experience/prescription evidence, not controlled effectiveness studies [AN, AM] |
| Criterion-to-outcome validity (conversational commerce) | configured score→timed external criterion→association→incremental prediction→intervention→decision/loss ladder | whole-episode outcome cues, invalid observer, selected/case-enriched populations, association promoted to prediction/causality, harmful proxy optimization, one endpoint overwriting plural quality | full immutable v1 PDF/text/HTML review [CVO]; phase-1 arithmetic is inspectable, while central phase-2 rows, prompts, outcomes, folds, and operational-cycle evidence are unreleased |
| Practitioner production-practice evidence (MAP) | reporting-unit/selection/denominator provenance and practice→realization→outcome bridge | selected self-report prevalence mistaken for representative practice, audited realization, causal efficacy, reliability, or successful deployment | full accepted immutable v4 paper/instrument plus v3 headline comparison; 20 confidential selected cases and 86 production/pilot main-frame records, no released row data or system/outcome audit [MAP] |
| Trajectory confidence prediction (Agentic Confidence Calibration) | typed derived probability for one configured success predicate, followed by transport and decision-policy validation | post-outcome prediction mistaken for early warning, repeat reliability, causal diagnosis, decision utility, or provider-invariant confidence | full immutable v1 paper/source review; reported eight-sample cross-validation and transfer tables, but no released code, trajectories, labels, splits, configurations, or calibrator [ACC] |
| Expert-authored criterion evaluation (ResearchRubrics) | reviewed criterion inventory, criterion-level judge observation, rubric transformation lineage | task-design authority mistaken for domain authority; bundled/dependent or hidden criteria; artifact-only source checks; uncalibrated additive score | full immutable v1 paper plus inspected post-paper official code/dataset releases; authoring and agreement evidence, not professional-readiness validation [RR] |
| Dynamic professional grading (JADE) | separate fixed and response-triggered criterion populations, trigger lineage, typed evidence/dependency graph, and plural score families | answer-conditioned obligations, variable denominators, duplicate/shared-cue checks, live-web authority error, fail-open verification, and uncalibrated fusion | full immutable v1 paper plus inspected close post-v1 release; bounded evaluator-architecture and deterministic fallback evidence, not expert-equivalent, cross-domain, or readiness validation [JADE] |
| Claim-centered validity | claim ladder, warrant/rebuttal record, facet-specific evidence, threshold/loss basis | checklist ritual, subjective facet ratings, reliability omitted, consequences under-specified | full immutable v4 conceptual paper and deep review; framework itself not empirically validated [VA] |
| Expert participation and transformation governance | scoped contribution unit, authority lineage, reconsent and reciprocal output | expert approval laundered through synthetic/developer/model transformations; favorable single-site evidence | full immutable v1 ethnography and deep review; no fidelity, cost, or near-zero-cost validation [EP] |
| Authority-gated workflow elicitation (laboratory workflow twins) | claim-level role gates and mandatory nulls; evidence→claim→projection lineage; root condition separated from a masking success channel | graph/query executability mistaken for knowledge truth, calibrated confidence, causal validity, operational benefit, or cross-domain transfer | full immutable 48-page v1 paper and deep review; four reported assay sessions in one department, proprietary substantive artifacts, and no ground-truth or operational-outcome validation [LWT] |
| Configurable participant systems (HAS-Bench) | participant realization, participation-policy vector, authority-event lineage, and availability/exercise/uptake/effect/burden separation | simulated social roles called humans; bundled prompt/tool/information/authority/budget contrasts; event counts mistaken for benefit or human cost | full immutable v1 paper and deep review; paper-reported scenarios/results only, no verifiable official artifact, real task participants, repeated cells, or reported process-judge audit [HAS] |
| Consequence-linked user-simulator audit | participant realization→authorized observable-state sufficiency→one-step/free-running fidelity→policy transport→real consequence ladder | human-like or assigned-goal dialogue promoted to decision fidelity; future outcome treated as simulator-visible latent truth; observational response differences promoted to causal tactic or production-agent effects | full immutable v1 paper and deep review over one private payment-linked production corpus; same-prefix one-step evidence only, with unavailable claimed release, unvalidated labels, unspecified censoring/clustering, and no free-running or policy-transport trial [USDF] |
| Evaluator-assisted cumulative artifact repair (AgencyBench) | typed feedback proposition→receipt/uptake→changed loci→criterion-local admissible re-observation→repair/collateral regression→endpoint and cost | extra inference and criterion disclosure called self-correction; evaluator critique called user feedback; non-equivalent observers pooled; first/final/best outcomes or invalids silently merged | full immutable v4 paper plus complete sole-commit January release audit; 32 scenarios/138 cumulative subtasks and 32 heterogeneous demonstrations are inspectable, but paper/release mismatch, single-run and denominator ambiguity, unavailable human labels, hidden aesthetics, observer disagreement, and no real-user evidence bound claims to configured evaluator-assisted repair [AGY] |
| Semantic-diff active oversight (Pista) | operation/rationale/dependency/scope review artifact linked to exposure, authorized intervention, changed locus, independent correction, preservation, burden, and consequence | generated explanation mistaken for faithful diff; bundled usability treatment, self-report, feature use, or attempted steering promoted to detection, realized repair, calibrated reliance, or utility | full immutable v1 paper plus two author-linked pre-v1 implementation archives; formative N=8 and bundled within-subject N=16 evidence supports inspectability and interaction-efficiency hypotheses, while unmatched defects, absent correction lineage, low endpoints, and no recipient outcome block effective-oversight or readiness claims [PISTA] |
| Decision-boundary cognitive traps (consulting study) | naive-path/expert-cue/derivation/consequence chain; typed evidence predicates | unavailable corpus/graders, unstable live data, human-applied checks, unvalidated failure tags | full immutable v3 paper plus linked release inspection; design pattern only, not auditable calibration evidence [CT] |
| Unprompted problem recognition (KWBench) | situation→cue→candidate/alternate frame→inquiry→action→artifact chain; matched framing intervention | cold final gate conflates recognition with domain knowledge, skepticism, action, artifact execution, and judge error; no near neighbors or framed condition | full immutable v1 paper plus linked code/site inspection, but gated task rows unavailable; internal six-cell replay validates synthetic instrumentation only [KW, PR] |
| Configured-system and harness comparison (Harness-Bench) | harness/adapter identity, outer-envelope contract, execution-alignment trace | bundled treatments, adapter inequivalence, host-readable private graders, fail-open missing evidence, single-attempt cells | full immutable v1 paper plus inspected post-paper official release; descriptive configuration evidence, not mechanism isolation [HB] |
| Cross-family execution substrate (BrowserGym) | canonical benchmark contract + adapter realization + trial-policy identity; differential conformance | common method signature or scalar hides heterogeneous evaluator, reset, retry, backend, observation, and error semantics | full immutable v2 paper plus inspected March 2026 official release; broad transport evidence, not exact-paper reproduction, native/adapted equivalence, common scale, safety, or professional validity [BG] |
| Executable workflow composition (WorkArena++) | typed obligation DAG, composable setup/oracle/validator, milestone/terminal split, reversal and reset evidence | chained atomic difficulty or polling history mistaken for planning, realism, or complete consequential work | full immutable v2 paper plus inspected February 2026 official release, which postdates the paper; strong construction evidence, but floor effects, small convenience human study, single software, reset uncertainty, and no occupational, safety, or exact-reproduction validation [WA]; internal replay is synthetic conformance only [CW] |
| Trajectory-judge calibration (AgentRewardBench) | typed observer evidence view, plural immutable labels, explicit adjudication lineage, predicate-specific error surface | unequal human/judge observability; mostly single labels; row-order authority; class imbalance; pooled unclustered metrics; invalid output conflated with negatives | full immutable v2 paper plus pinned code/annotation release inspection; bounded web-task agreement evidence, not general judge or professional-validity calibration [ARB] |
| Trajectory review selection (Signals) | probability-sentinel and enriched-discovery streams linked by an immutable population/inclusion/review/use episode | enriched yield mistaken for prevalence, comparison, detector accuracy, labor efficiency, supported defect, intervention effect, or utility; descriptive signals silently promoted to quality scores | full immutable v1 paper/source plus post-v1 author-associated implementation audit; bounded 300-slot queue-yield evidence, with empirical pool, selection ledger, labels, costs, and analysis unreleased [SIG] |
| Deterministic evidence-path evaluation (GroundEval) | actor/time policy, staged information-flow observation, bounded negative-search basis, configured-dependency checks, and dual answer/path evidence | authored contract determinism mistaken for authority, completeness, alternative-path coverage, causality, safety, or observer superiority; hidden exact labels; equation/code drift | full immutable v2 paper plus complete author-owned preprint snapshot and local 82-test/example audit; selected mechanics are inspectable, while the reported corpus, questions, trajectories, judge records, and results are absent [GE] |
| Retrieval-leakage auditing (search-time contamination) | information-flow policy and staged result/access/match/visibility/adoption/effect chain | legitimate retrieval conflated with shortcut access; detector stages under-validated; endogenous exposure mistaken for causal inflation; proprietary trace inequivalence | full immutable v1 paper; 6,803 medical-QA audit items, partial explicit-answer-detector validation, no auditable causal correction or cross-domain prevalence [SC] |
| Evolving-information workspace evaluation (ClawArena) | evidence-emission/update map, persistent workspace state, and update-to-check crosswalk | authored omniscience, untyped claim transitions, answer-bearing feedback, explicit preferences, mostly syntactic checks, unsafe shell execution, one-run order effects | full immutable v2 paper plus inspected official v1.0.0 and later release with timing boundaries; 337 rounds and 327 checker scripts audited, not professional-truth or reliability evidence [CA] |
| Single-specification task generation (Anchor) | versioned task IR, four projection types, solver witness, and cross-projection conformance tests | omitted professional rules propagate consistently; translator drift; canonical witness mistaken for completeness; public oracle/check leakage; mutable environment | full immutable v1 paper plus inspected one-day-post-v1 official release; all 300 packages statically audited and two lineages traced, not semantic-equivalence or professional-validity proof [AK] |
| Evidence-centered design (ECBD) | edge-level intended-use→construct→content/treatment→assembly→response/score warrants | completed worksheet mistaken for support; paper-only evidence view; assembly named without sampling machinery; reviewer consensus mistaken for reliability | full immutable v1 paper and complete pinned worksheets; three purposive dependent NLP cases, no prospective framework validation or independent-review reliability [ECBD] |
| Occupational artifact portfolio (GDPval) | explicit occupational frame, expert acquisition pipeline, multimodal witness artifacts, separate frame/content/assembly/inference denominators | equal task quotas laundered into work/economic representativeness; one witness treated as expert ceiling; pairwise preference treated as acceptance or productivity | full immutable v1 paper plus parsed 220-task post-v1 pinned release and one workbook pair; no probability sample, gold-selection record, augmentation trial, expert-population baseline, or release license [GDP] |
| Persistent file workspace (Workspace-Bench) | workspace identity/placement, typed relevance and provenance hypotheses, alternate paths, observed-use and integrity records | scale or authored graph treated as causal use; task-local injection/placement ambiguity; judge-view mismatch; unclustered single runs and mutable releases | full immutable v4 paper plus pinned post-v4 code/data audit and 37-file targeted task trace; no base-workspace replay, immutable result inventory, professional validation, Lite-fidelity, or workspace-learning identification [WB] |
| Session-derived workplace projection (EnterpriseClawBench) | observed-episode-to-counterfactual delta, hindsight firewall, equivalence disposition, and licensed-use record | real demand laundered into replay fidelity; omitted interaction/repair; answer-bearing hindsight; duplicated rubric dimensions; one-deployment generalization | full immutable v1 plus pinned post-paper release and two public trace audits; proprietary source pool/tasks/results and independent equivalence review unavailable [ECB] |
| Production-demand task construction (AlphaEval) | demand/projection/measurement/evolution ledgers; configured-package identity; criterion-version bridges | company provenance laundered into projection fidelity, occupational coverage, readiness, scaffold causality, or score-times-wage value | full immutable v1 plus pinned three-day-post-v1 framework release; 94 private tasks, transformations, outputs, and results unavailable, with seven purposive partners and nonfactorial package evidence [AE] |
| Industrial expertise codification | representation semantics, authorship-separation matrix, component ablations, and four-level transfer claim ceiling | selected co-designed rule-conformance effect laundered into tacit transfer, non-expert learning, expert equivalence, or cross-domain generalization | full immutable v1 paper; five selected artifacts from one organization/workflow, no released system/data/ratings, component ablation, repeated generation, or rater reliability [IC] |
| Broad expert executable portfolio (Agents' Last Exam) | expert→engineer→grader authority handoff, clean-start/verifier falsification, occupational denominators, and role-versioned living suites | nonempty cells mistaken for representativeness; deterministic proxy mistaken for professional closure; single runs; outcome-selected tiers; occupational/economic overclaim | full immutable v1 plus pinned post-paper release and three task traces; private pool, exact paper-time tree/results, licensed VM execution, expert reliability, and grader calibration unavailable [ALE] |
| Conditional agent reliability profiling | response matrix over matched repeats, preserved perturbations, decision-time confidence, and typed consequences | repeatability mistaken for capability; authored variants/exposure treated as deployment robustness; wrapper recovery credited to agent; post-hoc confidence and generic severity promoted to readiness | full immutable v3 paper and protocol-level review; two benchmark families, five incompletely controlled repeats, unvalidated interventions/severity, and no paper-pinned experiment code [AR] |
| Repeated stochastic evaluation (Stochastic Agent Evaluations) | intended-attempt ledger, plural validity denominators, task/form outcome frequencies, grader-crossed repeats, population-relative variance components, and decision-keyed repeat budgets | variance of noisy task means mislabeled ICC(1,1); invalids silently omitted; binary/unequal-repeat assumptions ignored; anchor composition and task mixture mistaken for an agent trait; visual convergence promoted to universal budgets | full immutable v1 PDF/text/source plus pinned ten-day-post-v1 official release and exact released-matrix recomputations; supports estimator and missingness audit, not transferable `8–16`/`≥32` budgets, professional validity, production reliability, safety, fitness, or readiness [SAE] |
| Historical-information authority (MemSyco-Bench) | source/represented-subject authority, purpose/recipient/scope, valid time, precedence and ignore/constrain/defer/supersede/use role linked to retrieval, adoption, action, and consequence | relevance promoted to authority; authored preference/fact oracle; nonfactorial families; uncalibrated judge; valid-call censoring; text answer promoted to causal use or benefit | full immutable v2 paper plus complete pinned post-v2 release/1,550-row audit; supports a synthetic configured-system stress-test vocabulary, not independent authority, natural prevalence, causal adoption, judge validity, professional utility, or readiness [MSY] |
| Selective evaluator re-execution | append-only attempt ledger, outcome-blind typed retry eligibility, frozen treatment, final-selection and residual-invalid denominators | schema-valid completion promoted to judge validity; unfavorable or abstaining outcomes retried; treatment drift hidden as retry; failed attempts and denominator effects erased | complete immutable v1 HTML/text review; reported production-scale architecture and aggregate claims only, with no official code/configuration/log/result release, retry recovery evidence, reliable human-label panel, throughput/cost measurement, or downstream outcome [SRE] |
| Work-activity and handoff-centered reporting | many-to-many activity map, tested-setting claim subtraction, persistent product bound to recipient/next operation, strongest and excluded claims | preliminary labels mistaken for representative coverage; visual realism or product polish mistaken for responsibility, downstream usability, or deployment evidence | full immutable v1 paper; LLM-mediated O*NET/ESCO descriptive taxonomy and three purposive report demonstrations, with no reliability, stability, reconstruction, recipient-use, or framework-effect validation [DR] |
| Frozen-state successor resumability (Handoff Debt) | matched checkpoint/view intervention; separate fidelity, recipient sufficiency, endpoint, outcome-aware continuation effort, and lifecycle cost | evaluator-derived state leakage; nested checkpoints treated as tasks; outcome-dependent stopping called rediscovery; authoring cost omitted; one coding runtime promoted to human/professional validity | full immutable v1 paper/source and aggregate-table audit, but no verifiable empirical release, task IDs, checkpoints, payloads, run records, or analysis [HD] |
| High-consequence analytical tool pipelines (DORA) | source/label truth, one executable analytical witness, typed endpoint, recipient/action, and observed or simulated consequence kept distinct | real historical sources and deterministic replay mistaken for task authority, calibrated tolerances, alternative-complete planning, safe operational action, or beneficial outcome | full immutable v1 PDF/text/source review; missing Appendices C–H and no verifiable task/tool/trajectory/result release block empirical replay and operational-validity claims [DORA] |

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
31. **Recognition is not execution:** preserve cue, framing, inquiry, action, and
    artifact observations separately; identify recognition, procedural-guidance,
    and evaluator-cue interventions with matched near neighbors before attributing
    a final consequence to unprompted problem recognition.
32. **Observed demand is not replay fidelity:** source episodes and rewritten counterfactuals have separate hashes, deltas, hindsight controls, equivalence dispositions, and licensed uses; real provenance cannot silently upgrade semantic equivalence.
33. **A tier label is not suite identity:** immutable membership, admission snapshot, outcome-selection, exposure, role transitions, and bridges govern living-benchmark comparisons; outcome-informed routing is not intrinsic difficulty.
34. **Agreement does not establish interchangeability:** preserve raw observations and keep agreement, panel-relative severity, fit, repeat stability, construct preservation, and decision loss separate; rubric execution topology and aggregation are instrument versions, not implementation trivia.
35. **Simulated dialogue is probed evidence:** simulator behavior, productive friction, stopping/deletion, and correction lineage remain visible; conversation volume or participant enjoyment cannot replace grounded downstream utility or consent/privacy evidence.
36. **Reliability is conditional, not a trait:** bind separate capability, repeatability, perturbation, predictability, and consequence estimands to an operational profile; require preservation/exposure evidence, separate wrapper from agent recovery, and license confidence only at its observed decision point.
37. **Realism is typed correspondence, not resemblance:** map target, required,
    incidental, and omitted activities; treat setting simplifications as claim
    subtraction; bind every persistent product to a recipient and next operation;
    and report source, boundary, and destination evidence with strongest supported
    and excluded claims.
38. **Adaptive coverage does not imply a common scale:** fixed obligations and
    response-created claims use separate ledgers and score families; every dynamic
    check needs a trigger, fair basis, typed applicability/evidence, overlap graph,
    and generator identity, while absent mandatory verification blocks capability
    interpretation rather than failing open.
39. **Interface compatibility is not measurement compatibility:** preserve native
    benchmark, upstream evaluator/dataset/backend, adapter transformations and
    losses, and trial policy as independent identities; require differential
    conformance before semantic-preservation or pooled-score claims.
40. **Composition is not construct validity:** executable subtasks need a typed
    dependency DAG, poll-order-independent terminal invariant replay, reversal and
    reset evidence, and matched atomic/family-cluster baselines; longer chains and
    lower success do not alone identify planning, realism, or professional work.
41. **Workplace substrate is not consequential-work validity:** keep task sampling,
    service/reset validity, requirement access/adoption, actor authority, intended
    and collateral deltas, evaluator sufficiency, and licensed claims separate;
    integrated apps or supplied histories cannot silently confer occupational,
    persistent-memory, collaboration, professional-validity, or readiness claims.
42. **Demand provenance is not expertise-transfer validity:** preserve elicitation
    authority, representation semantics, task projection, configured intervention,
    independent measurement, and claim ceiling; co-design, production origin, or a
    package effect cannot silently confer transfer, equivalence, readiness, or value.
43. **A participant role is not a participant realization:** independently type
    real humans, simulators, scripts, hybrids, and replays; version participation
    policy components and keep availability, exercise, uptake, effect, and plural
    burden separate. Simulator behavior cannot silently confer human-participation,
    expert-substitution, collaboration-validity, or readiness claims.
44. **Channel success is not substantive validity:** preserve the root invariant,
    primary-channel signal, independent evidence view, consequence, recovery, and
    uncertainty separately; an encoded masking edge or passing execution surface
    does not establish claim truth, artifact validity, professional success, safety,
    or readiness.
45. **Determinism does not validate the authored contract:** preserve authority,
    valid time, staged request-to-effect observations, bounded search-universe
    completeness, admissible alternatives, and configured dependency separately;
    exact replay cannot silently establish global absence, causality, observer
    superiority, professional validity, capability, safety, or readiness.
46. **Review yield is not population inference or downstream utility:** freeze the
    eligible population and inclusion policy; keep probability-sentinel and
    enriched-discovery streams separate; preserve evidence views, plural labels,
    adjudication, real review cost, clustered uncertainty, intervention effects,
    and licensed uses. Signal activation cannot silently become defect prevalence,
    system comparison, quality, safety, capability, or production-readiness evidence.
47. **An analytical witness is not a consequence oracle:** keep real-source
    provenance, task/requirement authority, source or label truth, one executable
    path, endpoint acceptance, recipient uptake, attempted/realized action, and
    stakeholder consequence separate; calibrate tolerances to decision loss,
    preserve alternatives and abstention, and cluster by shared source event or task
    lineage before any operational, safety, capability, or readiness promotion.
48. **Practice prevalence and confidence do not decide outcomes:** selected reports
    may motivate portfolio hypotheses and a trajectory score may predict one frozen
    label, but preserve actual configured realization, matched repeats, causal
    diagnosis, prediction time/coverage, transport, threshold/loss policy, human
    burden, and realized stakeholder loss as separate evidence. Neither common
    practice nor low calibration error silently licenses efficacy, acceptance,
    safety, professional validity, production fitness, or readiness.
49. **Repetition does not define one reliability estimand:** preserve every
    intended attempt and separate service, execution, grader, substantive,
    recurrence, heterogeneity, paired-effect, and decision populations; identify
    agent versus observer variation, model binary/unequal repeats, and test anchor
    and missingness sensitivity. An estimator name or visually stable curve cannot
    turn benchmark-population-relative evidence into an agent trait or a universal
    repeat budget.
50. **A suite scalar is a policy, not a discovered capability scale:** retain
    component constructs, units, evidence views, eligibility, denominators,
    uncertainty, and resources; name weights, gates, missingness, loss, and
    sensitivity before aggregation. Common transport and broad coverage cannot
    silently confer commensurability, professional validity, or readiness.
51. **An audit finding is not a defect or score correction:** bind the immutable
    instrument, auditor, evidence entitlement, candidate, adjudication, clean
    sentinel, disposition, changed loci, and repaired-form validation. Deletion
    sensitivity cannot silently become defect prevalence or corrected capability.
52. **Simulator fluency is not decision or consequence fidelity:** preserve
    authorized observable-state sufficiency, population-versus-person estimands,
    one-step and free-running stopping behavior, policy transport, and real
    consequence separately. Future-outcome discrepancy may falsify marginal
    realism, but cannot silently identify latent state, tactic effects, human
    equivalence, or production-agent quality.
53. **Relevant history is not authorized evidence:** bind prior information to
    source and represented-subject authority, purpose/recipient/scope, valid time,
    supersession, precedence, and admissible role; preserve retrieval, presentation,
    adoption/rejection, action, and consequence separately, including positive-use
    controls so indiscriminate ignoring cannot pass.
54. **A successful retry does not validate the evaluator:** retain every attempt,
    retry only prospectively typed invalid execution under a frozen treatment, and
    keep abstention, not-applicable, insufficient evidence, unfavorable valid
    outcomes, and residual invalidity in declared denominators. Schema, judge,
    metric, decision, and downstream validity remain separate gates.
55. **Plan visibility is not plan persistence or use:** atomize obligations and
    audit all source and derived context views; keep span removal, representation
    sensitivity, proposition recovery, free-action adoption, artifact/state
    consequence, and context-policy cost/reliability separate. Forced replay and a
    separately broad truncation result cannot fill each other's missing causal links.
56. **Outcome association is not criterion, intervention, or decision validity:**
    bind every score–outcome relation to observer validity, evidence time, eligible
    population/base rate/clusters, outcome authority/window/reversals, incremental
    baselines, and stakeholder loss. A same-episode association cannot silently
    become prospective prediction, a causal lever, legitimate optimization target,
    professional validity, production fitness, or readiness.
57. **Skill availability is not expertise transfer:** preserve mounted subset,
    surfacing/opening, invocation, adoption/rejection, attributable artifact change,
    independent criteria/outcomes, estimand-level model/task/rater balance,
    criterion-specific reliability, and held-out transfer. Human-rated conformance
    to a co-aligned procedure cannot silently become substantive correctness,
    expert equivalence, professional validity, or readiness.
58. **Semantic visibility is not effective oversight:** validate operation-level
    diff fidelity, matched defect opportunity, diagnosis, authorized intervention,
    receipt/adoption, intended change, independent correction, collateral
    preservation, reliance/burden, and recipient consequence separately. Self-report,
    feature use, attempted steering, or branch creation cannot fill later links.
59. **Observer richness cannot repair a contradictory criterion:** bind public
    basis, one proposition, desirable/violation polarity, applicability,
    authoritative view, decision rule, dependency/gate, signed contribution, and
    aggregation before execution. Brief/rubric conflict or prose/arithmetic reversal
    is instrument invalidity; a passing judge, expert label, or clipped scalar cannot
    silently repair it or license professional validity [AVB].
60. **Package efficacy is not allocation or portfolio value:** preserve the
    opportunity population, complete phase-resolved resource denominator, exact
    envelope and direct-action counterfactual, module-flow mediation, order/state
    hashes, retry treatment, and amortization horizon. Aggregate tokens, approximate
    budgets, presentation, or finite-repeat unions/intersections cannot silently
    license allocation dominance, causal adoption, general Skill/memory value,
    cross-domain transport, production fitness, or readiness [OSM, SAPA, PAT].

## 8. Unresolved tensions and required experiments

| Tension | Current evidence | Resolution experiment |
|---|---|---|
| Public procedure improves execution vs leaks evaluator cues | LH-Bench's rubric agreement improves, but execution ablation is only seven paired runs and the skill/rubric roles are confounded [LH]. | Four-condition skill × rubric-source ablation on one pilot; compare artifact/readiness outcomes, not process score alone. |
| Better configured-package frontier vs value of allocating resources to a Skill or memory module | The reviewed online study charges auxiliary and injected-context tokens and reports a stronger vanilla frontier, but uses approximate budgets, a compound control, undisclosed order, only three runs, and no release [OSM]. The internal parity audit finds zero admissible exact contrasts, while the prospective envelope is blocked on per-call phase telemetry [SAPA, PAT]. | On unlike non-ceiling work shapes, enforce one resource vector; hold pruning, prompts, tools, grader, and retry semantics fixed; counterbalance AB/BA order; hash state transitions; cross direct actor, offline Skill, and online evolving Skill; preserve opportunity/module flow and all attempts; then test amortization separately over eligible reuse and expiry. |
| Automated agreement vs professional validity | LH-Bench judges agree more under expert boundaries, yet individual human/automated concordance is weak [LH]. | Two-expert readiness labels and pairwise choices on a stratified pilot subset; calibrate each automated check against both. |
| Mid-difficulty efficiency vs rare critical coverage | Psychometric work favors informative middle checks; benchmark mission requires hard safety and expert traps [EB, AP]. | Maintain separate ranking and critical diagnostic sets; test rank fidelity and primitive coverage independently. |
| Workflow compliance vs latent expertise | Observable transitions are more judgeable, but exact procedure following can substitute for judgment [LH]. | Include at least two expert-approved procedures and held-out consequence variants. |
| Human-rated package lift vs identified expertise transfer | The medical Skill study adds human review, but one selected 21-output task, unequal model weighting, a bundled OpenClaw/package treatment, no exposure/adoption trace, shared procedure–criterion content, and negative expert ICC leave routing, elaboration, correctness, cueing, and transfer unresolved [MSK]. | Freeze attempted runs and model/task weights; hold harness/tools/budget fixed; cross no/placebo/procedural/executable/full-package arms with independent/shared criteria; log module realization; use connected calibrated raters and independent substantive checks on held-out task families. |
| Configurable assistance vs identified human-participation effect | HAS-Bench makes roles/channels observable, but its A1/A3/A4 contrasts bundle prompt, tools, information, authority, initiative, and budget while all task participants are model simulators [HAS]. | On well-defined matched tasks, factorially vary one participation-policy component at a time; counterbalance consented humans and pinned simulators, repeat/equate forms, validate process observers independently, and report outcome, safety, latency, active/wait time, interruption, correction, privacy, and accountability separately. |
| Inspectable semantic diff vs effective oversight | Pista's small bundled study supports perceived inspectability, explanation, feature-use, and prompt-burden observations, but semantic-diff fidelity, equal defect opportunity, proposition-level repair, preservation, calibrated reliance, and recipient outcomes are absent [PISTA]. | From frozen identical defective states, cross surface diff, independently verified semantic diff, ask/edit affordances, and generated suggestions plus misleading/incomplete-diff controls; log inspection through re-observation, grade native and collateral state, and measure burden and decision loss. |
| Outcome-linked simulator error vs valid policy/consequence transport | Same-prefix probes on one payment-linked corpus report more engagement-positive simulator bias for eventual non-payers, but future outcome may reflect private or later causes; teacher forcing, unvalidated labels, observational agent actions, censoring/clustering gaps, and no free-running policy trial prevent person, causal-tactic, or production-agent claims [USDF]. | Cross independently validated observable-state signals with simulator policy and matched history; compare population calibration with any person-specific target; preserve refusal/silence in bounded free-running rollouts; then compare frozen agent-policy rankings/effects under simulator, replay, and consented human conditions where justified. |
| Learning from failures vs benchmark contamination | STRACE/ACE support localized lessons; ACE also degrades under weak feedback and changes the online estimand [ST, ACE]. | Quarantine lessons, validate on held-out scenario clusters, and audit private-evidence flow before promotion. |
| Aggregate leaderboard vs diagnostic instrument | Reduced rankings are cheaper, while root-cause layers produce more actionable but uncertain claims [EB, ST]. | Report both without one composite; evaluate whether diagnoses predict expert-prescribed remediations on repeat trials. |
| Evolving agent vs evolving benchmark | Longitudinal guidance requires persistent state, while living benchmarks must also revise tasks and graders; changing both makes ability and difficulty jointly endogenous [SE]. | Freeze an anchor instrument within each stream; when the benchmark changes, run a bridge panel and report version effects before resuming evolution claims. |
| Efficient expert substitution vs authority laundering | One ethnography shows why teams shifted routine work to developers and an LLM judge, but reports no held-out fidelity or cost evidence [EP]. | Compare expert vs builder/grader application on frozen held-out anchors; record time, disagreement, transformation review, consent changes, and claim blocks without averaging agency and fidelity. |
| Useful narrow result vs broad capability/readiness claim | Claim-centered validity allows a criterion result to remain useful while rejecting wider construct or decision claims, but reviewer reliability is untested [VA]. | Have independent reviewers construct claim ladders for the same pilot trials; measure disagreement and test whether the contract rejects planted claim upgrades. |
| Realistic trap vs benchmark gotcha | Decision-boundary traps can expose expert judgment, but the reviewed consulting corpus and graders are not auditable and live values can drift [CT]. | Instantiate the same critical-incident record in two structurally different domains; plant naive/correct variants and test fairness, typed evidence checks, threshold flips, and predicted failure localization. |
| Ecological harness comparison vs valid common envelope | Native harness behavior is a legitimate bundled treatment, but Harness-Bench's later runner and the LH pilot show that fresh directories and shared prompts do not establish equivalent filesystem, network, service, or measurement opportunity [HB, PX]. | Run tool-level denial/allow canaries and adapter conformance checks before each cell; retain service failures; repeat matched cells; estimate a contrast only when both arms satisfy one hashed envelope and mandatory-evidence policy. |
| Shared runner breadth vs measurement equivalence | BrowserGym runs heterogeneous families through one interface, but inspected adapters retain different rewards/evaluators and transform observations, trajectories, parsing, errors, retries, and resets; paper results lack native/adapted agreement and clustered repeats [BG]. | From frozen native states, run matched native/adapted cases and compare score, termination, side effects, typed evaluator evidence, invalidity, resets, and all attempts; report family scores until preservation and any common-scale validity are independently supported. |
| Executable composition vs workflow/planning validity | WorkArena++ composes setup, oracle, and validators and increases horizon, but author-designed variants, history-dependent sequential validation, near-floor agents, a small ServiceNow-heavy human sample, and a later release do not isolate planning or occupational realism [WA]. | Across two provenance-grounded unlike workflows, compare matched atomic and composite conditions with controlled presentation/interface/information budgets; replay terminal invariants independent of polling order, test reversals and resets, and report family-clustered uncertainty plus earliest unsupported dependencies [CW]. |
| Judge agreement vs rubric construct preservation | ResearchRubrics finds better binary than ternary agreement and modest agreement gains from examples, but lacks duplicated-human reliability, criterion atomicity/dependence audits, and evidence access for source predicates [RR]. | On a pilot rubric, independently mark bundled/overlapping criteria and answer anchors; compare transformed variants on duplicated expert labels, judge confusion, legitimate solution diversity, and external artifact acceptability. |
| Rich temporal observation vs coherent signed criterion semantics | AgenticVBench's later release supplies native/rendered/audio/metadata/model views, yet 13/36 Repurpose briefs conflict with hidden resolution criteria and at least five desirable-state negative-weight items omit the scorer's inversion flag; human/calibration/result records are absent [AVB]. | Before any rollout, mutation-test public/private contradiction, desirable-versus-violation polarity, inversion, dependency/gate, clipping, and normalization. Reject both observed defect classes, admit a reviewed equivalent representation, then calibrate each observer on blinded temporal boundary cases without promoting agreement to professional acceptance. |
| Dashboard simplicity vs reproducible population inference | Amazon links traces, metrics, alerts, and audits operationally but reports no estimands, denominator/missingness rules, uncertainty, alert accuracy, or synthetic-to-real fidelity [AM]. | Backtest a versioned metric over planted agent, grader, environment, and population shifts; retain invalid/delayed events and measure detection delay, false alarms, review burden, and remediation routing. |
| Judge agreement vs evidence-view parity | AgentRewardBench compares richer human access with final-state-focused model views, preserves mostly single labels, and reports pooled unclustered metrics; disagreement can originate in task policy, trace capture, evidence access, or judgment [ARB]. | Plant temporally scoped success/side-effect cases; cross grader type with artifact-only, full-trace, and environment-query views; duplicate expert labels; adjudicate with explicit lineage; report predicate- and task-clustered error plus audit cost. |
| Enriched review yield vs representative monitoring and useful intervention | Signals reports more hypothesis-generating labels in a signal-selected queue, but omits the eligible pool, detector/score policy, inclusion probabilities, overlap, labels, reviewer time, clustered inference, confirmed defects, fixes, and downstream outcomes; its later implementation promotes descriptive signals into quality scores [SIG]. | On a frozen cross-domain trajectory pool, run a probability sentinel beside a versioned enriched sampler; preserve overlap and all inclusion probabilities, duplicate plural labels, adjudicate defects, measure reviewer minutes and detector cost, replay accepted fixes on held-out task clusters, and report prevalence/drift, discovery yield, false negatives, recurrence, and downstream utility separately. |
| Deterministic path replay vs valid evidence contract | GroundEval repeats actor/time, configured-artifact, and search-coverage predicates, but one outcome-informed authored contract, hidden exact fields, arbitrary search-space construction, configured event joins, unequal judge views, missing empirical artifacts, and Equation 1/Table 6/release drift prevent authority, completeness, causal, or observer-superiority claims [GE]. | On unlike domains, freeze contracts before trials; independently audit authority and public basis; plant alternate sufficient paths, incomplete/truncated/stale universes, blocked versus exposed evidence, and rival dependencies; compare deterministic/model/human observers under equal decisive views and retain insufficiency separately. |
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
| Engaging simulated novice vs productive elicitation | SimInstruct obtains substantial paid asynchronous dialogue and shows one randomized persona effect, but excessive agreeableness, endogenous stopping, selected retention, unknown burden/privacy lineage, and no downstream utility leave tacit-cue capture unidentified [SI]. | Within qualified contributors and frozen cases, compare vignette, neutral simulation, and friction-seeking simulation after an unprompted incident; measure realized resistance, grounded thresholds/failure signatures, corrections, time, privacy events, contributor value, and held-out task/check utility. |
| Higher rater agreement vs valid interchangeable measurement | Many-facet analysis separates panel-relative severity/fit from agreement, while rubric-modification results show examples, call topology, and aggregation can shift agreement through shared cueing or construct change [MF, RM]. Neither source supplies held-out professional decisions, repeat model calls, or reproducible release artifacts. | On a connected, held-out pilot panel, cross rubric/example variant with joint versus isolated execution; repeat raters, retain raw scores, estimate task/criterion interactions and linked severity, test legitimate-solution preservation and external decision loss, and report cost/audit burden without adjudicating by adjustment. |
| Consensus label vs plural professional judgment | One three-psychiatrist panel shows strong systematic disagreement but cannot separate person, framework, rubric, or context effects; the internal fixture proves only aggregation-contract behavior [ED, PJ]. | Repeat held-out ratings, prospectively declare frameworks, replicate experts within framework, vary context/rubric evidence, and compare explicit stakeholder policies while preserving dissent and claim blocks. |
| Retrospective memory QA vs consequential action transfer | LongMemEval-V2 cleanly evaluates bounded evidence delivery but representation/reader/grader effects remain treatment components and no acting agent uses the memory [LM]. | Compare no-memory, evidence-only, and provenance-gated lessons on equivalent-form QA and held-out artifact/state action; plant stale, failed-attempt, contradiction, safe-alternative, harmful-transfer, and rollback cases. |
| Plan-span removal vs proposition persistence and consequence | Plans Don't Persist reports a fading last-token contrast under broad guard/plan removal and a success gap under separate recent-four-message truncation; forced replay blocks free action, derivatives can reintroduce treatment content, and broad compression removes working state as well as the plan [PDP]. | On a longitudinal artifact workflow, atomize live obligations; cross exact/paraphrased/neutral/irrelevant/corrupted/omitted/restored clauses at matched capacity; audit every derived view; pair forced observers with free-action twins; separately restore current state; sweep budgets; report proposition recovery, adoption, artifact/state consequence, invalidity, and cost by task cluster. |
| Concurrent criterion association vs predictive/intervention/decision validity | The commerce study reports heterogeneous whole-dialogue score associations with payment in a small case-enriched sample, but one unvalidated judge, outcome-adjacent evidence, differential eligibility, confounding/clustering, selected weights, incomplete endpoint authority, and absent rows block every later claim [CVO]. | On a legitimate consequential pilot, validate observers under equal blinded views; freeze pre-outcome scores and population/outcome windows; compare incremental value against declared baselines on an untouched temporal form; then test any frozen score-targeted intervention on joint quality, safety, burden, reversals, and stakeholder loss. |
| Relevant historical information vs authorized current influence | MemSyco-Bench requires both rejection and positive use, but its synthetic authored boundaries, nonfactorial families, uncalibrated judge, and missing adoption/action evidence cannot establish factual, represented-user, or professional authority [MSY]. | On unlike artifact-heavy scenarios, hold the current task and observer fixed while substituting wrong-subject, wrong-recipient, stale, superseded, stronger-evidence, irrelevant, and legitimately controlling history; record retrieval, presentation, adoption/rejection, artifact/state consequence, alternatives, and authority review separately. |
| Efficient evaluator recovery vs outcome-conditioned censoring | Selective record retry can repair parser or serving failures, but the reviewed production account does not type eligibility, freeze treatment, retain attempts, define residual-failure publication, or report recovery/denominator evidence [SRE]. | In an existing cross-domain retry fixture, plant transport and malformed-output recovery, a schema-valid unfavorable result, abstention/insufficiency, terminal residual invalidity, configuration fork, and duplicate publish replay; assert append-only lineage and exact attempt/final denominators without claiming judge accuracy or production utility. |
| Unprompted recognition vs solving and execution | KWBench's cold gate combines cue extraction, framing, inquiry, action, artifact production, and judge behavior, with no matched framed condition or negative near neighbors [KW]. The internal replay establishes only staged instrumentation [PR]. | On expert-adjudicated positive/negative scenario pairs, cross situation-only, minimal-frame, and fully specified conditions; score cue, frame, inquiry, action, and artifact separately; repeat by scenario cluster and test alternate valid framings before licensing a recognition claim. |
| Retrospective QA success vs safe held-out transfer | The internal memory replay plants QA-correct but harmful evidence-only transfer and safe provenance-gated promotion, but deterministically encodes its own expected causal story [XM]. | Run stochastic consumers on unseen task families with frozen memory packages; vary stale/contradicted/failed-attempt evidence, measure access/adoption/action/recovery, cluster by source lineage, and test rollback plus expert-grounded consequences. |
| Real-session demand provenance vs source-to-task fidelity | EnterpriseClawBench provides real episode origin, but public traces show omitted repair, hindsight-derived answers, and rubric duplication while the proprietary pool blocks independent sampling and equivalence audit [ECB]. | Blind source users/independent experts to projected outputs; disposition each delta and omitted turn; compare faithful, demand-inspired, and synthetic licenses; sample rejected episodes; test preserved decisions, alternate paths, and acceptance judgments. |
| Living difficulty tier vs stable comparison | ALE's tiers are partly outcome-informed and later release memberships/counts differ while labels persist; most reported cells are single runs [ALE]. | Freeze membership/admission outcomes and exposure state; repeat systems across old/new memberships plus an anchor bridge; estimate task/workflow uncertainty and report role-transition effects separately from ability change. |
| Mean accuracy vs operational reliability | The reviewed reliability profile separates repeatability, perturbation response, confidence, and safety, but five non-independent repeats, unvalidated semantic preservation/exposure, wrapper-side recovery, retrospective confidence, and generic LLM severity prevent deployment interpretation [AR]. | On cross-domain forms, predeclare matched baseline/intervention repeats and operational profiles; independently validate variant preservation, cluster by task/form, retain invalid/provider failures, distinguish wrapper/agent recovery, elicit signals at routing/escalation/acceptance times, and calibrate consequence/loss with domain experts. |
| More repeats vs a valid reliability decision | Stochastic Agent Evaluations retains large response matrices but labels a variance-of-task-means ratio ICC(1,1), silently omits some release errors, confounds one-shot grader variation with agent variation, and visually promotes selected-matrix waypoints to `8–16`/`≥32` budgets [SAE]. | On frozen unlike task families, retain all intended rows and plural denominators; cross fixed-output grader repeats; compare documented binary balanced/unbalanced estimators; perturb easy/hard anchors and missingness policies; freeze decision-specific precision/loss and stopping rules; validate any budget on a held-out matrix before reuse. |
| Calibrated trial prediction vs useful selective review | Agentic Confidence Calibration reports favorable post-hoc ECE/Brier/AUROC for completed trajectories, but task/configuration clustering, label authority, transport, logprob equivalence, prefix timing, severe-defect control, review capacity, and realized loss are unvalidated [ACC]. | After diverse pilots supply valid repeated attempts, freeze extractor/calibrator and compare review-all, review-none, simple observable, semantic/state, and confidence-ranked policies under equal capacity; retain a probability sentinel, disjoint calibration/test families, severe-defect overrides, unavailable-logprob insufficiency, clustered uncertainty, workload, accepted failures, missed severe defects, and realized loss. |
| Reported production practice vs effective operating policy | MAP transparently reports selected practitioner conditions, but outcome-conditioned recruitment, optional-question attrition, unknown respondent/organization dependence, pooled pilot/production stages, and no system/outcome audit make prevalence and causal success claims invalid [MAP]. | Use practice reports only to sample candidate portfolio conditions; then verify realization from immutable configurations/traces and compare matched permission, human-gate, evaluator, and workflow policies with repeated artifact/state outcomes, reviewer burden, delayed labels, and stakeholder loss. |
| Artifact correctness vs handoff usability | The design report argues that persistent products support work claims through receiving workflows, but its three purposive cases contain no recipient-use trial, independent mapping reliability, or downstream validation [DR]. | Across unlike domains, give independent recipients only the produced product; test source, boundary, and destination checks separately and record clarification, repair, rejection, time, error propagation, and legitimate alternate formats before licensing downstream-use claims. |
| Adaptive diagnostic coverage vs comparable measurement | JADE separates stable skills from response-specific claim checks, but generated criterion counts, dependencies, shared model cues, mutable verification, and a fail-open release path leave common denominators and fusion unvalidated [JADE]. | On matched counterfactual artifacts from two unlike work shapes, mutate one claim/citation/dependency; blind experts to scores when judging criterion legitimacy and verdicts; measure extraction/edge agreement and item/graph/rank stability; report fixed and contingent families separately. |

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
3. **Completed bounded execution, not a Skill-effect claim —
   `build-lh-pilot-grader-ablation`:** after preserving earlier invalid attempts,
   one fresh v8 no-skill/public-skill pair passed zero-call and in-trial isolation
   canaries under one pinned launcher and both arms produced artifacts. Both failed
   deterministic evidence provenance; criterion outcomes otherwise differed. One
   pair cannot establish a Skill effect, professional validity, capability, or
   release readiness; the retained attempts, artifacts, usage, graders, and pair
   summary are bounded configured-system evidence only [HB, PX].
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
18. **Completed evidence-to-action conformance, not demonstrated transfer —
    `build-experience-memory-transfer-conformance`:** trajectory-derived evidence
    connects to both equivalent-form QA and held-out action while testing stale
    or harmful transfer and rollback. The deterministic synthetic replay makes
    evidence-only QA success coexist with harmful transfer and provenance-gated
    promotion coexist with the planted safe action. It validates package/scorer
    behavior only; LongMemEval-V2 does not supply action-transfer evidence and
    this fixture supplies no agent, expert, prevalence, or safety result [LM, XM].
19. **Completed recognition-intervention conformance, not recognition evidence —
    `build-problem-recognition-intervention-slice`:** a builder-authored positive/
    negative pair is projected into situation-only, minimal-frame, and fully
    specified conditions with separate cue, framing, inquiry, action, and artifact
    labels. Deterministic replay and invalid-environment abstention establish
    instrumentation behavior only, not an agent treatment effect, expert validity,
    professional competence, prevalence, or cross-domain generality [KW, PR].
20. **Completed initial-state conformance, not professional transition validity —
    `build-task-initial-state-bypass-conformance`:** seven deterministic synthetic
    cases distinguish valid creation, pre-satisfied/stale/copied outcomes, omitted
    transition, a declared alternative, and invalid initialization. This validates
    local fixture/scorer behavior only; real-task execution, alternate-path review,
    expert adjudication, and adversarial grader calibration remain required [IS].
21. **Completed temporal-artifact conformance, not creative or professional
    validity — `build-temporal-artifact-conformance-slice`:** the existing artifact-
    transition pilot now routes source lineage, native structure, rendered intervals,
    and export identity through separate observers across 11 deterministic cases,
    including timing boundaries, wrong interval/component, missing views, broken
    editability, export mismatch, and a legitimate alternate sequence. This validates
    fixture/scorer behavior only; observer calibration, expert judgment, agent trials,
    reliability, professional validity, production fitness, and readiness remain
    unsupported [CV, TA].
22. **Blocked pending evidence-gated selective-review inputs —
    `validate-trajectory-confidence-selective-review`:** do not build a confidence-
    specific schema or run on one-shot/synthetic-only cells. Wait for diverse pilots
    with valid repeated attempts, then exercise the frozen policy comparison in §8.
    Existing trace, reliability, metric, task-health, review-selection, and validity
    records are the implementation homes [ACC]. The queue prerequisite audit found
    no admissible confidence/logprob observations and no diverse repeated outcome
    matrix, so the task remains blocked rather than pending.
23. **Queued signed-criterion conformance, not another artifact subsystem —
    `build-signed-criterion-conformance-slice`:** the benchmark bundle already binds
    checks to public requirements, graders, artifacts, positive weights, and optional
    admissibility envelopes, but it cannot represent or validate desirable/violation
    polarity, inversion, gate/dependency behavior, or signed aggregation. Add the
    smallest backward-compatible contract and planted preflight cases needed to reject
    the two AgenticVBench defect classes before execution. Reuse projection,
    artifact-view, task-health, metric, and validity machinery; do not infer observer
    accuracy, expert validity, capability, professional quality, or readiness [AVB].

## Provenance keys

- **[OSM]**
  `papers/agent-benchmarks/2026-07-16-online-skill-memory-budget-value.md`;
  reviewed immutable v1 PDF/text and project-page acquisition provenance are
  recorded there. The page exposes no code, data, trajectories, task order,
  configured-system manifest, shared states, or analysis artifacts. Evidence
  supports a reported configured-package success–token frontier and allocation-
  design warning—not exact fixed-budget dominance, general Skill/memory value,
  amortized value, web-to-knowledge-work transport, production fitness, or readiness.
- **[SAPA]** `pilots/skill-allocation-parity-audit/README.md`,
  `pilots/skill-allocation-parity-audit/v1/manifest.json`, and
  `pilots/skill-allocation-parity-audit/v1/audit-report.json`; hash-pinned replay of
  14 intended prior-study rows, including four service-invalid cells. Integrity
  passes, but zero exact allocation contrasts are admissible; this is negative
  diagnostic evidence, not a Skill effect, memory-value, capability, or readiness
  result.
- **[PAT]** `pilots/prospective-allocation-telemetry/README.md`, frozen v1 manifest,
  canary, and readiness report; deterministic zero-call capture-envelope conformance
  only. No matched pair ran because aggregate usage cannot supply per-call phase
  attribution; all allocation, Skill-effect, cost-value, capability, professional,
  production, and readiness claims remain false.
- **[NI]**
  `papers/agent-benchmarks/2026-07-16-networked-intelligence-shared-context-validity.md`;
  reviewed immutable v1 PDF/text/HTML and acquisition provenance are recorded
  there. No author-owned implementation, graph, campaign records, notebooks,
  routing events, artifact-authoring protocol, run corpus, or analysis release was
  located. Evidence supports one author-run configured-package case narrative and
  a post-hoc 26-item content audit—not a routing effect, scientific validation,
  tacit transfer, irreducibility, productivity, privacy, professional validity, or
  readiness.
- **[MSK]**
  `papers/agent-benchmarks/2026-07-16-skill-augmented-medical-human-evaluation.md`;
  reviewed immutable v1 PDF/text/supplement and timing-bounded linked package paths
  and hashes are recorded there. The package archive is inspectable, but the 21
  outputs, raw ratings, executed configuration/commit, selection ledger, and
  exposure/adoption traces are unavailable. Evidence supports a small selected
  configured-package/human-rating pilot and a reliability warning—not an isolated
  Skill effect, substantive correctness, transfer, expert equivalence, professional
  validity, production fitness, or readiness.
- **[PISTA]**
  `papers/agent-benchmarks/2026-07-16-pista-active-oversight-workflow-validity.md`;
  reviewed immutable v1 PDF/text plus both author-linked pre-v1 implementation
  archives and provenance are recorded there. The archives expose substantial
  mechanism code but no exact study build, tasks, participant logs, artifacts,
  ratings, or analysis. Evidence supports bounded inspectability/interaction-
  efficiency observations under a bundled two-task lab treatment—not semantic-diff
  fidelity, effective repair, calibrated oversight, professional utility, or
  readiness.

- **[PDP]**
  `papers/agent-benchmarks/2026-07-16-plans-dont-persist-context-eviction-validity.md`;
  reviewed immutable v1 PDF/text/metadata hashes are recorded there. The source
  reports forced-prefix representation contrasts, derived reasoning-trace
  contamination, steering nulls, and a broad recent-message compression stress test,
  but releases no code, task manifests, prompts, trajectories, hidden states, folds,
  policy views, or result rows. It supports an observer method and claim boundary,
  not proposition-level persistence, behavioral adoption, causal plan loss,
  professional validity, safety, production fitness, or readiness.
- **[CVO]**
  `papers/agent-benchmarks/2026-07-16-criterion-validity-business-outcomes.md`;
  reviewed immutable v1 PDF/text/raw-HTML/metadata hashes are recorded there. The
  phase-1 displayed arithmetic is reproducible, but the central 60-row phase-2
  scores/outcomes, prompt and judge outputs, sampling/join records, folds, operational
  cases, and code are unavailable. Evidence supports selected concurrent
  score–payment associations and a dimension-heterogeneity warning, not judge
  validity, prospective/incremental prediction, causality, outcome authority,
  decision utility, professional validity, production fitness, or readiness.
- **[CE]**
  `papers/agent-benchmarks/2026-07-15-claw-eval-multichannel-trajectory-validity.md`;
  reviewed immutable v3 PDF/text/HTML plus a complete pinned post-v3 official release
  audit are recorded there. The release contains 300 manifests/graders but no exact
  paper run corpus or fault injector; its manifest criterion inventory diverges from
  the paper and selected hybrid-only adjudication does not calibrate either observer.
- **[CV]**
  `papers/agent-benchmarks/2026-07-15-cutverse-temporal-creative-artifact-validity.md`;
  reviewed immutable v1 PDF/text plus a complete pinned post-v1 official release
  audit are recorded there. The later archive is a generic Windows runner with one
  Notepad example and placeholder evaluation, not the paper's 186 tasks, media,
  parser, milestones, environments, runs, or result evidence.
- **[AVB]**
  `papers/agent-benchmarks/2026-07-16-agenticvbench-expert-temporal-artifact-validity.md`;
  reviewed immutable v1 PDF/text plus the complete pinned post-v1 official release
  and `data/sources/releases/2605.27705v1-agenticvbench/release-audit.json` are
  recorded there. The later release exposes all 100 reported four-family packages
  and substantive graders, but not paper trajectories, scores, human submissions,
  calibration labels, or an auditable result ledger. Material paper/release drift,
  criterion defects, source-rights/immutability gaps, and unreconciled denominators
  bound the evidence to later instrument inspection rather than v1 reproduction,
  professional capability, reliability, safety, production fitness, or readiness.
- **[PD]**
  `papers/agent-benchmarks/2026-07-15-partial-agent-benchmark-decision-validity.md`;
  reviewed immutable v1 HTML, official-repository PDF, complete pinned release, and
  executed public replay paths are recorded there. Evidence supports retrospective
  preservation of one completed-record decision under a declared policy—not
  prospective stopping, score/rank/diagnostic/reliability preservation, professional
  validity, safety, or readiness.
- **[TA]**
  `pilots/artifact-transition-conformance/v0.2-temporal/replay-report.json`;
  11 deterministic builder-authored cases establish source/native/render/export
  observer routing and fail-closed fixture behavior only.
- **[ASAS]**
  `papers/agent-benchmarks/2026-07-15-agentic-skills-at-scale-projection-validity.md`;
  reviewed immutable v1 PDF/text and the complete pinned 1,110-task release audit are
  recorded there. The release has 608 declared top-level Skills but no raw
  trajectories, judge decisions, configuration manifests, result tables, or typed
  invalid/missing-cell ledger; it supports shared-projection compliance rather than
  independent utility or transfer.
- **[MSB]**
  `papers/agent-benchmarks/2026-07-15-mapsatisfybench-behavior-grounded-hidden-requirements.md`;
  reviewed immutable v2 PDF/text are recorded there. No official task, code, grader,
  prompt, trajectory, or result release was found; the selected private-log study
  supports a candidate-factor/firewall method, not current consent, causal
  satisfaction, calibrated acceptance probability, or personalization validity.
- **[OB]**
  `papers/agent-benchmarks/2026-07-15-occubench-language-simulator-validity.md`;
  reviewed immutable v2 PDF/text plus complete pinned code and dataset audits are
  recorded there. The 382 released packages cover 98 of 100 frame scenarios, and
  implicit model state, prompt-driven unmatched faults, shared-model verification,
  and absent result runs bound the evidence to a synthetic transition instrument.
- **[ASTA]**
  `papers/agent-benchmarks/2026-07-14-astabench-scientific-suite-aggregation-validity.md`;
  reviewed immutable v2 PDF/text plus pinned post-v2 code and immutable dataset
  manifest are recorded there. Dataset bytes were gated, hosted search remained
  external, scorer defaults drifted, and no self-contained paper-run package was
  found; evidence supports suite operations, not one scientific-capability scale.
- **[ABA]**
  `papers/agent-benchmarks/2026-07-14-auto-benchmark-audit-task-defect-validity.md`;
  reviewed immutable v2 PDF/text plus full pinned post-v2 release inspection are
  recorded there. Small BenchGuard tables were reproduced, but the full task audit
  corpus and deletion masks were absent; evidence supports candidate-finding triage,
  not confirmed prevalence, automatic deletion, or corrected capability.
- **[ET]** `schemas/EXPERTISE_TRANSFER.md` and
  `schemas/expertise-transfer.schema.json` (implemented repository contract).
- **[LH]** `papers/agent-benchmarks/2026-07-10-lh-bench-skill-grounded-evaluation.md`;
  reviewed full text/PDF paths and hash are recorded there.
- **[ACE]** `papers/agent-benchmarks/2026-07-10-agentic-context-engineering.md`;
  reviewed full text/PDF paths and hash are recorded there.
- **[SE]** `papers/agent-benchmarks/2026-07-10-self-evolving-agents-survey.md`;
  reviewed immutable v4 full text/PDF paths and hash are recorded there. Its
  protocol is prescriptive synthesis, not an empirically validated benchmark.
- **[AFTER]**
  `papers/agent-benchmarks/2026-07-13-after-procedural-memory-transfer-validity.md`;
  reviewed immutable v1 PDF/text and pinned official GitHub/Hugging Face release
  paths and hashes are recorded there. The release exposes 129 static test
  packages but not the paper's evolution experiments or transfer results.
- **[ST]** `papers/agent-benchmarks/2026-07-09-strace.md`; local extracted text
  path is recorded there.
- **[SAT]**
  `papers/agent-benchmarks/2026-07-15-intervention-timing-construct-reliability.md`;
  reviewed immutable v1 PDF/text and pinned post-v1 official repository paths and
  hashes are recorded there. The release reproduces the retained 56-action label
  statistics and exposes the `Δt=0` correction, but omits the paper-time engine,
  raw trajectories, complete annotation instrument, and consequence evidence.
- **[WWP]**
  `papers/agent-benchmarks/2026-07-15-whowhen-pro-failure-attribution-validity.md`;
  reviewed immutable v1 PDF/text plus pinned two-day-post-v1 code/project snapshots
  are recorded there. The claimed 12,326-row corpus, generation/evaluation code,
  human-label records, predictions, and result package were unavailable; six
  illustrative traces do not establish paper–release correspondence.
- **[IAR]** `pilots/intervention-attribution-rungs-v1/README.md`,
  `protocol.json`, and `replay-report.json` (SHA-256
  `d36e3f70404d7fa6de8555ce5f0e1433dd8a2a0d09e4298d3e7fd3679e9758fd`);
  24 deterministic builder-authored attempts across two work shapes validate local
  claim-rung, observer-view, and fail-closed fixture behavior only.
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
- **[HAS]**
  `papers/agent-benchmarks/2026-07-13-hasbench-configurable-human-participation-validity.md`;
  reviewed immutable v1 PDF/text paths and hashes are recorded there. The reported
  task participants are model simulators, the human study reviews scenario
  artifacts, the planned process-judge audit has no reported results, and no
  official benchmark/results artifact could be verified.
- **[DC]**
  `papers/agent-benchmarks/2026-07-14-deskcraft-interactive-workflow-validity.md`;
  reviewed immutable v1 PDF/text/source hashes and both official-release timing
  boundaries are recorded there. The paper-time public tree contains only a
  license; the inspectable 538-package snapshot is 30 days post-v1 and contains no
  trajectories, simulator judgments, outputs, or result corpus. It supports an
  authored phased-interaction and native-endpoint package pattern, not causal
  interaction benefit, simulator-human parity, human collaboration, professional
  validity, capability, safety, production fitness, or readiness.
- **[USDF]**
  `papers/agent-benchmarks/2026-07-15-user-simulator-decision-fidelity.md`;
  reviewed immutable v1 PDF/text paths and hashes are recorded there. The study
  supplies one-corpus payment-linked, teacher-forced, same-prefix next-turn
  evidence. Its claimed release is unlocatable; raw dialogue/outcomes are private;
  censoring, customer clustering, panel selection, state/action-label validity,
  consent/privacy data flow, free-running behavior, and policy transport remain
  unresolved. It supports outcome-conditioned falsification and an information-
  sufficiency boundary, not person fidelity, causal tactics, human equivalence,
  production-agent quality, professional validity, safety, or readiness.
- **[AGY]**
  `papers/agent-benchmarks/2026-07-15-agencybench-feedback-artifact-validity.md`;
  reviewed immutable v4 PDF/text plus the complete sole-commit official release,
  provenance, and machine-readable 32-scenario audit are recorded there. The
  January release predates April v4 and differs in feedback and aggregation; the
  paper run corpus, human labels, repeats, normalized invalid/service ledger, and
  exact paper-time implementation are unavailable. Evidence supports a configured
  evaluator-assisted repair instrument, not autonomous self-correction, realistic
  user collaboration, professional utility, safety, production fitness, or
  readiness.
- **[CT]** `papers/agent-benchmarks/2026-07-10-consulting-cognitive-traps.md`;
  reviewed immutable v3 paper and inspected release paths/hashes are recorded
  there. The release lacked the reported task and grading artifacts.
- **[HB]** `papers/agent-benchmarks/2026-07-10-harness-bench-execution-isolation.md`;
  reviewed immutable v1 PDF/text and inspected official post-paper release
  paths/hashes are recorded there. The release is implementation evidence, not
  the exact paper-time runner or empirical result archive.
- **[BG]**
  `papers/agent-benchmarks/2026-07-11-browsergym-ecosystem-measurement.md`;
  reviewed immutable v2 PDF/text and inspected official March 2026 release paths
  and hashes are recorded there. The release is not manuscript-time identity;
  adapter inspection establishes heterogeneous implementation semantics, not
  native/adapted equivalence, common construct measurement, safety, professional
  validity, or exact reproduction of the reported experiment.
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
- **[SIG]**
  `papers/agent-benchmarks/2026-07-14-signals-trajectory-triage-sampling-validity.md`;
  reviewed immutable v1 PDF/text/source and post-v1 author-associated Plano release
  paths/hashes are recorded there. The paper supports selected-queue yield under one
  annotation target; absent pool, inclusion, label, cost, and intervention records
  block prevalence, comparison, detector-validity, utility, safety, capability, and
  readiness claims. The later implementation is not the empirical release and its
  quality-score emission is preserved as a downstream-use divergence.
- **[GE]**
  `papers/agent-benchmarks/2026-07-14-groundeval-evidence-path-validity.md`;
  reviewed immutable v2 PDF/text and complete author-owned preprint snapshot paths
  and hashes are recorded there. The release supports selected deterministic
  scorer/generator mechanics and compact examples, not the unavailable paper
  experiment, contract authority/completeness, causal identification, global
  verified absence, observer superiority, professional validity, capability,
  safety, production fitness, or readiness.
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
- **[HAB]**
  `papers/agent-benchmarks/2026-07-16-healthadminbench-workflow-projection-validity.md`;
  reviewed immutable v1 PDF/text plus the complete pinned 63-day-post-v1 official
  release are recorded there. The 135 tasks and 1,698 checks are inspectable, but
  absent requirement-level lineage, dependency edges, repeated trials, raw paper
  runs, and stable hosted-state identity block error-propagation, reliability,
  occupational, safety, production, and readiness claims.
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
- **[CMDA]**
  `papers/agent-benchmarks/2026-07-16-context-mediated-domain-adaptation-edit-validity.md`;
  reviewed immutable v2 PDF/text plus the complete author-linked OSF snapshot and
  v1/v2 source comparison are recorded there. The five-person fixed sequence and
  partial mutable release support edit/event capture and candidate-entry storage,
  not contributor-approved extraction, realized presentation/adoption, causal
  quality improvement, tacit transfer, burden reduction, or readiness.
- **[LWT]**
  `papers/agent-benchmarks/2026-07-13-laboratory-workflow-expert-elicitation.md`;
  reviewed immutable 48-page v1 PDF/text hashes are recorded there. Four reported
  assay sessions and a proprietary static graph support representation-design
  lessons only; absent transcripts, claim-level transformations, graph instances,
  independent ground truth, operational outcomes, and cross-domain tests block
  substantive knowledge, professional-validity, benefit, and transfer claims.
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
- **[MA]**
  `papers/agent-benchmarks/2026-07-13-memoryarena-interdependent-experience-action.md`;
  reviewed immutable v1 PDF/text and complete pinned post-v1 preview release are
  recorded there. Results concern configured interdependent-session pipelines,
  not isolated memory causality, longitudinal learning, professional competence,
  or readiness.
- **[US]**
  `papers/agent-benchmarks/2026-07-13-underspecbench-action-boundary-validity.md`;
  reviewed immutable v1 PDF/text are recorded there; no official release was
  verifiable. Its authored prompt matrix supports an authorization-state stress-
  test pattern, not population prevalence, professional validity, or deployment
  safety.
- **[AD]**
  `papers/agent-benchmarks/2026-07-13-ambig-ds-task-framing-validity.md`;
  reviewed immutable v1 PDF/text plus pinned pre-v1 official dataset revisions
  and hashes are recorded there. The filtered synthetic target/objective
  interventions and ideal oracle support a paired diagnostic pattern, not natural
  ambiguity prevalence, realistic stakeholder authority, professional framing or
  escalation validity, occupational capability, safety, or readiness; raw results,
  exact configurations, complete Target reconstruction, and released human/panel
  lineage are unavailable.
- **[KW]**
  `papers/agent-benchmarks/2026-07-11-kwbench-unprompted-problem-recognition.md`;
  reviewed immutable v1 PDF/text and inspected linked code/site snapshots are
  recorded there. Gated dataset rows were unavailable; reported results concern
  an unprompted author-defined consequence gate, not isolated recognition.
- **[PR]** `pilots/problem-recognition-intervention/replay-report.json` and
  `pilots/problem-recognition-intervention/README.md`; six builder-authored,
  deterministic synthetic cells establish staged scorer and abstention behavior
  only, not expert validity, agent capability, treatment effects, prevalence, or
  cross-domain generalization.
- **[EAI]** `pilots/evidence-acquisition-matched-agent-v1/protocol.json`,
  `pilots/evidence-acquisition-matched-agent-v1/execution/study-report.json`, and
  retained attempt/episode records; 12 valid configured-agent attempts across two
  builder-authored synthetic shapes establish request/parser/access/adoption trace
  retention and one candidate interface failure only. Two repeats per cell and no
  matched request-interface ablation support no causal inquiry, capability,
  expert/professional-validity, cross-domain, safety, production, or readiness
  claim.
- **[ERI]** `pilots/evidence-request-interface-v2/protocol.json` (SHA-256
  `6f1d487f46b25f901826de8bb5ff56ea4585aafb78308ce4c13d8555044cd04d`),
  `pilots/evidence-request-interface-v2/execution/study-report.json` (SHA-256
  `f387505394ef3fb6649900cba7177ac1b1b4bf9ac570ddd3a78be653a440608b`),
  `pilots/evidence-request-interface-v2/execution/flow-audit.json`, and eight
  hash-verified retained trial reports. The frozen components and all trial-report
  hashes replayed exactly. This builder-authored, synthetic, active-only study has
  two purposive repeats per cell and no pooled effect; it supports exact internal
  interface-flow observations and no capability, causal, professional, population,
  cross-domain, production, safety, or readiness claim.
- **[ERR]** `pilots/evidence-request-receipt-repair-v3/protocol.json` (SHA-256
  `06c19672e3380cc2991b8d69ac0ce33250e4d247d961c4ef508fb4f179daf1bd`),
  `pilots/evidence-request-receipt-repair-v3/execution/study-report.json` (SHA-256
  `4490b20b1a5cce11969acc2bd9e7832c8ac95bfffea916c377f9f309c42aca91`),
  `pilots/evidence-request-receipt-repair-v3/execution/flow-audit.json`, and eight
  retained request/receipt/repair trial records. Frozen-component preflight and all
  trial-report hashes replayed exactly. This builder-authored synthetic study has
  two purposive repeats per cell and no pooled effect; it establishes exact
  observability/recoverability mechanics only, not inquiry quality, endpoint
  improvement, capability, causal, expert/professional, population, cross-domain,
  compliance, safety, production, deployment, or readiness validity.
- **[XM]** `pilots/experience-memory-transfer/replay-report.json` and
  `pilots/experience-memory-transfer/README.md`; three builder-authored,
  deterministic synthetic conditions establish QA/action separation, harmful-
  transfer, promotion, and rollback fixture behavior only.
- **[TCP]**
  `papers/agent-benchmarks/2026-07-16-compliance-trap-memory-consumption-validity.md`;
  reviewed immutable 25-page v1 PDF/text/HTML/source hashes and release-search
  provenance are recorded there. No task, memory, trajectory, label, result, or
  runnable analysis release was verified. Reported browser outcomes support
  configured-package sensitivity to authored context, not an E–P–R mechanism,
  memory capability, safety, professional validity, production fitness, or readiness.
- **[ECB]**
  `papers/agent-benchmarks/2026-07-11-enterpriseclawbench-session-derived-validity.md`;
  reviewed immutable v1 PDF/text and pinned official post-paper release paths and
  hashes are recorded there. Proprietary sessions, 852 tasks, outputs, and result
  records are unavailable; two public traces bound the projection findings.
- **[AE]**
  `papers/agent-benchmarks/2026-07-11-alphaeval-production-grounded-validity.md`;
  reviewed immutable v1 PDF/text plus pinned three-day-post-v1 official release
  paths and hashes are recorded there. The private 94-task corpus, source-to-task
  deltas, results, and full labels remain unavailable; production, occupational,
  causal-scaffold, readiness, and economic-value claims are unsupported.
- **[IC]**
  `papers/agent-benchmarks/2026-07-11-industrial-expertise-codification-agent.md`;
  reviewed immutable v1 PDF/text hashes are recorded there. Five selected
  co-designed artifacts from one Siemens workflow support a bounded package effect,
  not tacit transfer, non-expert learning, expert equivalence, cross-domain
  generalization, operational benefit, or readiness.
- **[JB]**
  `papers/agent-benchmarks/2026-07-12-jobbench-delegation-desire-validity.md`;
  reviewed immutable v1 PDF/text, pinned post-v1 evaluation release, and 128-row
  dataset metadata audit are recorded there. Paper/release mismatch, purposive
  selection, outcome-conditioned admission, incomplete judge views, disabled
  sandboxing, and absent worker workflow/outcome evidence bound all claims.
- **[BR]**
  `papers/agent-benchmarks/2026-07-12-benchmark-to-risk-expert-elicitation.md`;
  reviewed immutable v2 PDF/text hashes are recorded there. The small, ordered,
  clustered expert workshop exposes benchmark-to-consequence warrant disagreement;
  it does not establish calibrated uplift, cyber risk, expected harm, causal
  transfer, decision usefulness, capability, professional validity, or readiness.
- **[DORA]**
  `papers/agent-benchmarks/2026-07-14-dora-disaster-response-consequence-validity.md`;
  reviewed immutable v1 PDF/text/source hashes and release-search provenance are
  recorded there. The source archive omits cited Appendices C–H, and no author-owned
  task/tool/trajectory/result package was verifiable at review time. Historical
  source realism and one GT-derived analytical witness do not establish calibrated
  operational acceptability, consequence, safety, professional validity,
  capability, production fitness, or readiness.
- **[HC]**
  `papers/agent-benchmarks/2026-07-11-hippocamp-personal-context-validity.md`;
  reviewed immutable v1 PDF/text and inspected one-day-post-v1 official release
  paths and hashes are recorded there. The 42.4 GB corpus, gold annotations,
  paper results, human audit, consent lineage, and container images were not
  archived locally, so no corpus replay, privacy audit, faithful-personalization,
  causal-use, professional-correctness, consequential-action, or readiness claim
  is supported.
- **[ALE]**
  `papers/agent-benchmarks/2026-07-11-agents-last-exam-expert-task-validity.md`;
  reviewed immutable v1 PDF/text plus pinned post-paper official release and three
  task traces are recorded there. Release behavior cannot be projected backward,
  and private tasks/results, licensed execution, expert reliability, repeated-run
  uncertainty, occupational sampling, and economic claims remain unsupported.
- **[IS]** `pilots/task-initial-state-conformance/conformance.json` and
  `pilots/task-initial-state-conformance/replay-report.json`; seven builder-authored
  deterministic cases grounded in [ALE]. They establish internal conformance only,
  not verifier completeness, agent capability, professional validity, prevalence,
  cross-domain generalization, or readiness.
- **[MF]**
  `papers/agent-benchmarks/2026-07-11-many-facet-human-ai-rater-effects.md`;
  reviewed immutable v2 PDF/text hashes are recorded there. The small fully
  crossed educational sample has no released data/code and does not establish
  operational grader interchangeability or cross-domain severity stability.
- **[RM]**
  `papers/agent-benchmarks/2026-07-11-rubric-modification-human-autorater-agreement.md`;
  reviewed immutable v1 PDF/text hashes are recorded there. Historical human
  labels, bundled edits, changing aggregation, and absent release artifacts bound
  results to configured agreement effects rather than accuracy or validity.
- **[SI]**
  `papers/agent-benchmarks/2026-07-11-siminstruct-simulated-novice-elicitation.md`;
  reviewed immutable v2 PDF/text hashes are recorded there. One paid education-
  coaching network demonstrates dialogue feasibility and instrument reactivity,
  not tacit-knowledge capture, low-cost recruitment, privacy closure, or real-user
  and downstream benchmark utility.
- **[AR]**
  `papers/agent-benchmarks/2026-07-11-agent-reliability-profile.md`; reviewed
  immutable v3 PDF/text hashes are recorded there. The two-family, five-repeat
  study demonstrates distinct diagnostic profile dimensions, not independent
  tail estimates, cross-domain reliability ordering, prospective predictability,
  calibrated consequence loss, deployment readiness, or certification; the
  inspected implementation commit is not paper-time identity.
- **[SAE]**
  `papers/agent-benchmarks/2026-07-14-stochastic-agent-evaluations-icc-validity.md`;
  reviewed immutable v1 PDF/text/source and pinned ten-day-post-v1 official release
  paths/hashes are recorded there. Exact release-matrix recomputations reproduce
  published ratios and show that they are not ICC(1,1), while the published FRAMES
  slice omits connection-error judgments contrary to the prose failure policy.
  The evidence supports response-matrix, estimator, and missingness audit—not
  transferable repeat budgets, agent-intrinsic reliability, professional validity,
  production reliability, safety, fitness, or readiness.
- **[POR]**
  `papers/agent-benchmarks/2026-07-15-performance-optimization-benchmark-reliability.md`;
  reviewed immutable v1 PDF/text/HTML paths and hashes plus release-search
  provenance are recorded there. The paper audits 740 reference patches over four
  processor profiles and three rounds, but releases no raw timing cells, exact
  snapshots, rescoring code, annotations, or result corpus. Its strict intersection,
  score-policy sensitivity, and selected public-output union support bounded
  criterion-health evidence—not machine-invariant validity, transport probability,
  causal rank effects, configured-system reliability, saturation, professional
  capability, production fitness, or readiness.
- **[ACC]**
  `papers/agent-benchmarks/2026-07-14-agentic-confidence-calibration-validity.md`;
  reviewed immutable v1 PDF/text/source hashes and provenance are recorded there.
  No code, trajectories, labels, splits, exact configured-system manifest, or
  calibrator artifact was released; reported post-hoc prediction does not establish
  repeats, causal diagnosis, decision utility, professional validity, safety,
  production fitness, readiness, or universal transfer.
- **[MAP]**
  `papers/agent-benchmarks/2026-07-14-measuring-agents-production-practitioner-evidence.md`;
  reviewed accepted immutable v4 PDF/text, preserved v3 comparison, and provenance
  are recorded there. The released instrument and aggregate denominators support
  selected practice descriptions, not unique-unit prevalence, audited realization,
  practice efficacy, reliability, professional validity, safety, or readiness.
- **[AA]**
  `papers/agent-benchmarks/2026-07-11-aarri-research-judgment-lifecycle.md`;
  reviewed immutable v1 PDF/text and acquisition-time official release archive
  paths and hashes are recorded there. The 82 authored AI-research tasks and
  descriptive one-trial configured-system results expose consequence-bearing
  non-completion and verifier false rejection; they do not establish sampling,
  professional construct validity, human ease, reliability, causal harness
  effects, cross-domain transfer, or paper-time release identity.
- **[DR]**
  `papers/agent-benchmarks/2026-07-11-design-report-knowledge-work-benchmarks.md`;
  reviewed immutable v1 PDF/text paths and hashes are recorded there. Its
  LLM-mediated O*NET/ESCO inventory and three purposive case mappings demonstrate
  a reporting proposal; undisclosed panel procedure, absent annotation
  reliability/stability and exact reconstruction, and no recipient-use or
  framework-effect study block taxonomy-validity, representativeness,
  downstream-usability, professional-readiness, and deployment claims.
- **[JADE]**
  `papers/agent-benchmarks/2026-07-11-jade-dynamic-professional-grading.md`;
  reviewed immutable v1 PDF/text and close post-v1 official archive paths and
  hashes are recorded there. The release is three days newer than v1 and omits
  rich demonstrated skills, human labels, generated evaluation evidence, and
  result reproduction artifacts. Its inspected fail-open scoring path is release
  evidence; the small clustered BizBench comparison and outcome-conditioned,
  heterogeneous HealthBench transfer do not establish criterion validity,
  expert equivalence, calibrated fusion, cross-domain capability, or readiness.
- **[ADA]**
  `papers/agent-benchmarks/2026-07-15-adarubric-adaptive-trajectory-instrument-validity.md`;
  reviewed immutable v3 PDF/text and pinned post-v3 official release paths and
  hashes are recorded there. The paper supplies no empirical release; paper/code
  contradictions in validation, call topology, confidence aggregation, caching,
  multimodality, and reliability limit it to candidate instrument architecture,
  not criterion authority, grader accuracy, decision validity, reward utility,
  deployment fitness, or readiness.
- **[XB]**
  `papers/agent-benchmarks/2026-07-15-xpertbench-scaled-expert-task-validity.md`;
  reviewed immutable v4 PDF/text, v1 comparison, paper-linked platform responses,
  and unverified release leads are recorded there. The paper's own appendix has a
  task–rubric instance mismatch, while tasks, criteria, contributor ledgers,
  anchors, judgments, configurations, repeats, and scoring code are unavailable;
  scale and a one-shot expert-scored exemplar do not establish participation,
  grader, professional, or readiness validity.
- **[DIC]** `pilots/dynamic-criterion-conformance/instance-conformance.json` and
  `scripts/validate_dynamic_criteria.py`; deterministic builder-authored internal
  calibration with one source-grounded and one synthetic cross-instance
  substitution plus an allowed representation change. It establishes validator
  behavior only, not expert validity, grader accuracy, equivalence completeness,
  cross-domain generalization, capability, reward quality, or readiness.
- **[FR2]**
  `papers/agent-benchmarks/2026-07-16-finresearchbench-ii-consensus-rubric-validity.md`;
  reviewed immutable v2 PDF/text/HTML plus immutable v1 comparison and bounded
  acquisition-time release search are recorded there. Exact reported criterion
  attrition and agreement denominators are inspectable, but queries, reports,
  criteria, labels, generation protocol, configurations, costs, and analysis are
  unreleased; panel stability and selected-cohort discrimination do not establish
  criterion authority, professional validity, transport, or readiness.
- **[AZ]**
  `papers/agent-benchmarks/2026-07-14-asymmetryzero-semantic-eval-contracts.md`;
  reviewed immutable v1 PDF/text plus paper-time framework release and private-study
  evidence limits are recorded there. The plumbing makes jury topology inspectable,
  but agreement, repeated-call reliability, criterion correctness, task decisions,
  and downstream loss remain non-substitutable.
- **[KINA]**
  `papers/agent-benchmarks/2026-07-16-kina-incentive-representativeness-validity.md`;
  reviewed immutable v2 PDF/text plus the complete pinned 899-row official dataset
  and 11-file code release are recorded there. The final exact-letter corpus is
  inspectable, while anchors, calibrators, constrained-selection lineage, reviewer
  scores/assignments/payments/audits/appeals, contributor welfare, raw trials, and
  rank analyses are absent; release conformance defects and the bundled phase
  comparison block representativeness, incentive-effect, professional-validity,
  contributor-benefit, affordability, and readiness claims.
- **[WA]**
  `papers/agent-benchmarks/2026-07-11-workarena-plus-compositional-validity.md`;
  reviewed immutable v2 PDF/text and pinned official February 2026 archive paths
  and hashes are recorded there. The release postdates the 2025 paper and no live
  ServiceNow run was reproduced. Evidence supports executable composition, not
  occupational representativeness, isolated planning/reasoning, complete reset,
  cross-software transfer, safety, professional validity, or readiness.
- **[CW]** `pilots/composite-workflow-conformance/README.md` and
  `pilots/composite-workflow-conformance/workflows.json`; two builder-authored
  synthetic workflows establish deterministic conformance behavior only.
- **[TAC]**
  `papers/agent-benchmarks/2026-07-11-theagentcompany-workplace-simulation-validity.md`;
  reviewed immutable v3 PDF/text and pinned post-v3 official release hashes are
  recorded there. Release inspection supports substrate and evaluator audit, not
  manuscript-time identity, occupational sampling, coworker validity, complete
  consequences, labor automation, professional validity, or readiness.
- **[OD]**
  `papers/agent-benchmarks/2026-07-11-odysseybench-longitudinal-office-memory-validity.md`;
  reviewed immutable v1 PDF/text and pinned seven-month-later official release
  hashes are recorded there. External testbeds, absent paper trajectories, generated
  histories, and narrow/invalid predicates block persistent-memory, occupational,
  professional-validity, capability, safety, and readiness claims.
- **[UC]**
  `papers/agent-benchmarks/2026-07-13-uniclawbench-proactive-closed-loop-validity.md`;
  reviewed immutable v1 PDF/text and complete pinned one-day-post-v1 official
  release are recorded there. The release supports role-separated repair-loop
  inspection, not paper-time result reproduction, semantic non-leakage,
  proactivity, natural-user fidelity, causal repair, professional validity, or
  readiness.
- **[EDGE]**
  `papers/agent-benchmarks/2026-07-13-edgebench-within-run-learning-validity.md`;
  reviewed immutable v1 PDF/text and pinned official code plus 51-task dataset
  release are recorded there. The paper reports a selected 134-task analysis,
  while trajectories, fitting artifacts, 83 tasks, and complete valid-run evidence
  are unavailable; suite-level best-so-far fits do not establish task-level or
  universal learning laws.
- **[CF]** `pilots/closed-loop-feedback-audit/README.md`, `report.json`, and
  `adaptive-report.json`; 24 feedback-arm cells and six adaptive red-team cases
  are deterministic builder-authored synthetic replay evidence only.
- **[HD]**
  `papers/agent-benchmarks/2026-07-14-handoff-debt-successor-resumability.md`;
  reviewed immutable v1 PDF/text and complete arXiv source paths/hashes are
  recorded there. No author-owned empirical release was verifiable; reported
  evidence is bounded to configured agent-to-agent takeover on public coding
  tasks and does not establish human/professional handoff validity, total-cost
  savings, causal generalization, capability, production fitness, or readiness.
- **[ACOOP]**
  `papers/agent-benchmarks/2026-07-11-agentcoop-typed-handoffs-localized-repair.md`;
  reviewed immutable v1 PDF/text and pinned close post-v1 release paths/hashes are
  recorded there. The release supports transport/type and runtime inspection,
  not semantic interoperability, receiver-use validity, causal repair, or
  professional readiness.
- **[D52]**
  `papers/agent-benchmarks/2026-07-11-delegate52-delegated-artifact-integrity.md`;
  reviewed immutable v1 PDF/text plus pinned code and public dataset paths/hashes
  are recorded there. Cycle consistency supplies bounded preservation evidence,
  not requested-delta success, professional consequence, or readiness.
- **[ACON]**
  `papers/agent-benchmarks/2026-07-13-acon-context-compression-validity.md`;
  reviewed immutable v3 PDF/text and pinned official release paths/hashes are
  recorded there. Configured reward/token trade-offs do not establish faithful
  state preservation, total-system improvement, general transfer, or readiness.
- **[MSY]**
  `papers/agent-benchmarks/2026-07-15-memsyco-memory-authority-validity.md`;
  reviewed immutable v2 PDF/text plus the complete pinned post-v2 official release
  and all 1,550 rows are recorded there. Authored labels, no independent authority
  review, nonfactorial families, uncalibrated judge, conditional denominators, and
  absent paper-run outputs block natural prevalence, causal adoption, judge,
  professional-validity, benefit, and readiness claims.
- **[SRE]**
  `papers/agent-benchmarks/2026-07-15-production-evaluation-selective-reexecution-validity.md`;
  reviewed complete immutable v1 HTML/text and release-search provenance are
  recorded there. The PDF endpoint and official empirical/configuration release
  were unavailable; no attempt logs, retry recovery, reliable human panel,
  throughput/cost measurement, or downstream outcomes support idempotency, judge
  validity, operational reliability, production utility, or cross-domain claims.
- **[HU]** `pilots/handoff-usability-conformance/README.md` and retained producer,
  downstream-consumer, adjudication, and counterfactual records; internal
  configured and builder-authored evidence only, with no human usability, expert
  validity, professional capability, generalization, productivity, impact, or
  readiness claim.
- **[PMB]**
  `papers/agent-benchmarks/2026-07-16-pmbench-prospective-memory-validity.md`;
  reviewed immutable v1 PDF/text plus pinned paper-time official release, complete
  64-run log audit, canonical validation, and report regeneration are recorded
  there. One public synthetic week and an ungraded ongoing token support obligation-
  selection machinery, not dual-task interference, professional reliability,
  causal failure origin, safety, or readiness.
- **[DOT]** `pilots/delayed-obligation-dual-task/protocol.json` (SHA-256
  `6cd27291cca984ee2ceac0e767a99a7bae116f64d041bedb45621de0684d5ebe`),
  `pilots/delayed-obligation-dual-task/execution/study-report.json` (SHA-256
  `9f3b3cca6496310769dee777ae35392731996f3961d3a8c03fa0b2a8fb01ea3a`),
  `pilots/delayed-obligation-dual-task/validity-record.json`, and six retained trial
  reports. Frozen-component hashes and exact replay passed. The two builder-authored
  synthetic ceiling forms with one attempt per condition support exact configured
  observations and deterministic grader behavior only—not internal memory,
  treatment effects, interference absence, capability, cross-domain/professional
  validity, safety, production fitness, or readiness.
- **[DOT2]** `pilots/delayed-obligation-heldout-v2/protocol.json` (SHA-256
  `77e5ac6527efd7c9b343b155c193c6800736ea54fa4b103ac4c829e4f65541ec`),
  `pilots/delayed-obligation-heldout-v2/execution/study-report.json` (SHA-256
  `e655e3e79ff33908435c4dd2cb9047b9d1743bc092431679a013d19abf3d50fa`),
  `pilots/delayed-obligation-heldout-v2/preflight/canary-report.json` (SHA-256
  `19897e3f7028e719d1c842774a581664500462f110fc8f51b10726d1df847016`),
  `pilots/delayed-obligation-heldout-v2/validity-record.json`, and 12 retained trial
  reports. Exact replay passed. Four builder-authored held-out forms and one attempt
  per form-condition cell support direct channel-flow and exact configured-attempt
  observations only, not a treatment effect, internal memory, calibrated
  interference, capability, expert/professional validity, generality, safety,
  production fitness, or readiness.

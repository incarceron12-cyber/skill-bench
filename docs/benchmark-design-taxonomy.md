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
| 6. Instrument | Check and grader | observable evidence, pass boundary, visibility, root-cause labels | Does each check test a disclosed professional requirement or a fair held-out consequence? | benchmark bundle checks and graders |
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

## 3. Measurement stack: trial to defensible claim

| Layer | Unit observed | Appropriate claim | Do not infer |
|---|---|---|---|
| Environment validity | tool/service availability, fixture integrity, permissions, timing | the trial had a valid opportunity to complete the task | agent inability from a broken environment |
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

### 4.1 Keep three change planes separate

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
| Production agent evaluation (Anthropic, AWS) | task/trial/grader/trace separation, task-health lifecycle, and operational failure taxonomy | engineering guidance may not establish benchmark construct validity; repeated-trial estimates may hide dependence | full official Anthropic article and concept review [AN]; AWS deep review remains pending |
| Claim-centered validity | claim ladder, warrant/rebuttal record, facet-specific evidence, threshold/loss basis | checklist ritual, subjective facet ratings, reliability omitted, consequences under-specified | full immutable v4 conceptual paper and deep review; framework itself not empirically validated [VA] |
| Expert participation and transformation governance | scoped contribution unit, authority lineage, reconsent and reciprocal output | expert approval laundered through synthetic/developer/model transformations; favorable single-site evidence | full immutable v1 ethnography and deep review; no fidelity, cost, or near-zero-cost validation [EP] |
| Decision-boundary cognitive traps (consulting study) | naive-path/expert-cue/derivation/consequence chain; typed evidence predicates | unavailable corpus/graders, unstable live data, human-applied checks, unvalidated failure tags | full immutable v3 paper plus linked release inspection; design pattern only, not auditable calibration evidence [CT] |

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
3. **Current execution gate — `build-lh-pilot-grader-ablation`:** planted
   provenance grading and the four hash-pinned fixture-replay cells are complete,
   but they explicitly provide no capability evidence. Next run genuine matched
   no-skill/public-skill outputs with a pinned harness, then obtain qualified
   shared-rubric and expert adjudication. Preserve typed existence, entailment,
   authority, scope, and freshness results and add a threshold-crossing
   contradiction where feasible. The pending SkillsBench review may refine this
   protocol but must not be treated as execution evidence.
4. **Parallel infrastructure — `build-compounding-lesson-contract`:** implement
   candidate lesson provenance, independent promotion, contradiction, firewall,
   and rollback semantics. Building the contract is safe; promoting pilot-derived
   doctrine remains gated on trustworthy trial/adjudication evidence.
5. **After static execution — `build-longitudinal-evolution-protocol`:** add the
   stream and evolution-event records from Section 4.1, then exercise matched
   reset vs permitted-memory/skill-only vs full-evolution fixtures. Do not use
   longitudinal complexity to bypass the static pilot's failed validity gates.
6. **Claim gate — `build-validity-argument-contract`:** after real static pilot
   measurements, bind them to narrow supported and explicitly unsupported claim
   rungs before any professional-capability or readiness statement [VA].
7. **Participation gate — `build-expert-participation-contract`:** after the
   validity contract, govern real contribution purpose, reciprocity, authority,
   transformation, and reconsent separately from ACTA elicitation content. An
   internal fixture cannot validate consent, motivation, or expert fidelity [EP].
8. **Production-method updates:** the Anthropic review adds a task-health and
   operational-role lifecycle beyond the static bundle [AN]. Implement it only
   after the current pilot/validity gates; integrate the pending AWS review only
   where it adds or contradicts a canonical object.

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
- **[VA]** `papers/agent-benchmarks/2026-07-10-validity-centered-ai-evaluation.md`;
  reviewed immutable v4 PDF/text paths and hashes are recorded there. The source
  is a conceptual synthesis with retrospective cases, not a validated protocol.
- **[EP]** `papers/agent-benchmarks/2026-07-10-domain-expert-participation-ethnography.md`;
  reviewed immutable v1 PDF/text paths and hashes are recorded there. Findings
  are bounded to one compensated university collaboration.
- **[CT]** `papers/agent-benchmarks/2026-07-10-consulting-cognitive-traps.md`;
  reviewed immutable v3 paper and inspected release paths/hashes are recorded
  there. The release lacked the reported task and grading artifacts.

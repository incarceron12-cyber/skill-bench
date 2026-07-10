# Paper Review: Domain-Expert Participation Is a Governed Handoff, Not an Annotation Step

- **Paper:** https://arxiv.org/abs/2602.14357v1
- **Authors:** Annalisa Szymanski, Oghenemaro Anuyah, Toby Jia-Jun Li, and Ronald A. Metoyer
- **Date read:** 2026-07-10
- **Venue / source:** IUI 2026; immutable arXiv preprint v1
- **Tags:** domain-expertise, participatory-design, ethnography, consent, ownership, AI-literacy, human-evaluation, LLM-as-a-judge
- **Local PDF:** `data/papers/pdfs/2602.14357v1-domain-expert-participation.pdf` (14 pages; SHA-256 `23c39ea357a787adfffb3ae65e1eebceebbdef841681cbeee3db29cff67d78d2`)
- **Local text:** `data/papers/text/2602.14357v1-domain-expert-participation.txt` (SHA-256 `84ff9195dce0b7b6be91cfc39fe400c6a8f5a676071d80885b8ecdec34601673`)

## One-sentence contribution

A 12-week embedded ethnography shows how one university team progressively substituted simulations, synthetic data, developer judgment, and an LLM judge for scarce pedagogical-expert labor, while revealing that expert participation remains legitimate only when contributors understand the technical use, retain agency over reuse and role changes, and can inspect how their standards behave after operationalization.

## Why this matters for skill-bench

This review advances charter objectives B, E, and especially F: it supplies observed primary-source evidence about the collaboration layer around expertise transfer, which the repository's current authoring schema barely represents. The concrete artifact is this review plus a proposed contribution-and-consent lifecycle. The uncertainty clarified is not merely how to elicit tacit knowledge, but **when an artifact can still be called expert-grounded after developers, generators, or model judges transform and apply it**.

The mode is targeted expansion with a build-ready consolidation. Existing work already specifies claims, primitives, source packs, checks, and release gates; the queued ACTA research task addresses elicitation probes and cognitive outputs. This paper adds non-duplicate evidence about recruitment, motivation, literacy, fatigue, reuse, attribution, and decision rights. Useful completion means a future cross-domain pilot can show who contributed what, for which use, through which transformations, with which approval and withdrawal boundaries—and can fail release when expert authority has been silently delegated.

The general cross-domain hypothesis is: **small, reciprocal expert contributions can remain useful under limited resources if the benchmark preserves contribution lineage and reserves expert attention for high-leverage standard setting, transformation review, disagreement, and release decisions rather than repetitive scoring.** The paper motivates but does not validate that workflow, and its compensated single-institution setting does not establish a free or near-zero-cost participation model.

## Research question

The authors ask three questions (p. 2): how an LLM development team performs design and evaluation over a development cycle; what trade-offs arise around evaluation and expert involvement; and what lessons could improve workflows and tools for domain experts.

For `skill-bench`, the sharper derivative question is: when limited expert inputs are converted into examples, synthetic variants, rubrics, developer judgments, and automated scores, what provenance and governance are needed to avoid laundering those downstream artifacts as direct expert judgments?

## Methodology

### Setting and participants

The study follows one team from June through August 2025 at a private U.S. university's teaching-and-learning center. The system, InstructAI, was intended to provide pedagogically grounded advice to instructors. The technical team had three members—a UX project manager, technical lead, and software engineer—and collaborated with a primary pedagogical stakeholder plus center-affiliated pedagogical experts (pp. 3–4).

The first author joined as an embedded but non-decision-owning team member, observing daily stand-ups, weekly planning, informal communications, design workshops, rubric work, output review, and data-contribution sessions. The paper reports 70.8 observation hours over 12 weeks, same-day field notes under stable headings, weekly analytic memos, all three developer interviews, expert/stakeholder interviews, and artifact collection including rubrics, workshop materials, outputs, annotations, expert-generated data, and judge results (pp. 4–6).

Participant accounting is incomplete. Eighteen compensated experts supplied more than 130 simulator dialogues; three 1.5-hour workshops each used two compensated experts; quotations identify at least five domain experts; but the paper does not state the total number of expert interviewees, whether workshop participants were unique, or how interviewees overlap with the 18 data contributors (pp. 5–10). This prevents a clean denominator for claims such as “most experts.”

### Analysis and ethics

The first author led thematic analysis across field notes and interview transcripts, with artifact review used to trace criteria changes. Initial practice and concern codes were iteratively grouped into subthemes and higher-level themes. Co-author discussion and reflexive memos challenged interpretations, but there was no formal inter-coder reliability procedure (p. 6). The researcher was both participant and analyst, making reflexivity valuable but not equivalent to independent analysis.

The university IRB approved the study; participants provided informed consent; the researcher's embedded role was disclosed; identifiers were removed; and materials were access-restricted. No student or instructional data were used (p. 6). These protections concern the research study. They should not be conflated with granular consent to every downstream technical transformation, an ambiguity the experts themselves surfaced.

### Observed development sequence

The paper's strongest contribution is a longitudinal substitution chain rather than any single participation method:

1. **Real consultation recordings were rejected.** Recording threatened client privacy, could change vulnerable conversations, imposed consent work, and risked the center's trusted service (p. 7).
2. **Four staged conversations were tried and abandoned as a scaling path.** They were costly to clean, contained natural disfluencies, and did not resemble chatbot interaction closely enough (p. 7).
3. **A text simulator collected expert responses.** Eighteen hourly compensated experts contributed asynchronously, producing more than 130 dialogues. An LLM judge—not experts—was used to assess whether simulated instructor prompts looked authentic (p. 7).
4. **The expert corpus was expanded synthetically.** Developers generated 1,000 dialogues from the small expert corpus and did not directly evaluate the augmented data before fine-tuning because of time constraints (p. 7).
5. **Experts co-developed judge criteria.** Developers first drafted generic criteria from online best practices, then held three 1.5-hour workshops with two compensated experts each. Experts received an orientation, edited criteria, compared outputs with judge scores, and tested the chatbot (p. 8).
6. **Expert scoring proved too tedious.** Reading full conversations, selecting criteria, rating, and justifying ratings was abandoned. Developers believed workshop exposure let them approximate expert application; they took over manual review and used an LLM judge whose prompts were adjusted until scores aligned more closely with developer and expert judgments (p. 9).
7. **Criteria became optimization feedback.** Developers favored criteria that differentiated models and fed score patterns into prompt and fine-tuning changes (p. 9).

This sequence is operationally realistic: it shows not a planned “human-in-the-loop” architecture but repeated reallocations of work under privacy, schedule, cost, and comprehension constraints.

## Evidence and strength of support

### Observed evidence

The data strongly support bounded claims about this team's practices and tensions:

- privacy and relational trust blocked collection of apparently authentic consultations;
- asynchronous text contribution improved logistical scale but introduced repetition, typing strain, and shallower expression;
- experts had trouble separating the object being evaluated (chatbot output) from the instrument they were designing (judge criteria);
- advance materials, reflection time, explanations attached to judge scores, and live criterion testing were requested by participants;
- mission alignment, institutional trust, curiosity, learning, compensation, and influence over a community tool supported motivation;
- experts worried that “tips and tricks” could become a system that imitated or displaced their work;
- expert evaluation was costly enough that developers and an LLM judge ultimately performed routine scoring (pp. 7–11).

The evidence also documents an important consent gap. All participants formally consented and uses were described as approved, yet experts still reported uncertainty about how their knowledge would be repurposed and concern over loss of control (pp. 6, 10–12). This does not prove consent was invalid. It does show that one-time procedural consent did not resolve evolving-use comprehension and agency.

### Author proposals

The authors derive three lessons (pp. 11–13): use flexible, data-centric tools that capture reasoning rather than only answers; provide AI-literacy support and recognize experts' changing roles; and explicitly disclose how knowledge will be used. They propose interactive demonstrations, think-alouds, reflection, clear training/evaluation/deployment use statements, licensing-style restrictions, compensation or recognition tied to long-term value, authorship/acknowledgment/shared rights, expert review of synthetic data, and recurring review checkpoints.

These are reasonable design proposals grounded in observed friction, but they were not implemented and evaluated in the study. In particular, licensing, shared rights, recurring checkpoints, and richer contribution tools have no reported uptake, cost, retention, or quality outcomes.

### What the evidence does not establish

The study does not establish that hybrid evaluation was accurate, that developer judgments remained faithful to expert standards, that the LLM judge was reliable, that synthetic dialogues preserved expert knowledge, or that the resulting chatbot improved pedagogical work. There are no released rubrics, outputs, coded excerpts, judge prompts, score tables, expert–developer agreement statistics, synthetic-data audits, or deployment outcomes.

Nor does it establish a low-cost model. Experts received hourly compensation; workshop and data-collection time are described, but rates, total cost, recruitment conversion, refusal, dropout, and administrative overhead are absent. Institutional trust and shared mission were unusually strong and experts explicitly said they would be less willing in commercial settings (p. 9).

## Unique insight

The paper's deepest implication is that **expert authority decays through transformations unless each handoff is separately authorized and checked**. The project began with expert conversations, then moved to simulated expert responses, unreviewed synthetic expansions, criteria partially edited by experts, developer-applied ratings, and a prompt-tuned model judge. Every stage was plausibly “expert-informed”; only some stages were actually expert-authored or expert-approved.

That distinction matters more than a binary `domain_expert` contributor label. `skill-bench` needs to distinguish at least:

- expert-authored;
- expert-edited;
- expert-approved after inspection;
- developer-derived from expert material;
- model-derived from expert material;
- applied by an expert, developer, deterministic grader, or model judge;
- not yet reviewed after transformation.

A second insight is that scarce expert time should be allocated by **authority leverage**, not merely annotation volume. The case suggests high-value units are defining boundaries, surfacing relational/safety constraints, testing criterion behavior, resolving disagreements, reviewing transformed material, and deciding permissible release claims. Repetitive full-dialogue scoring exhausted experts and was transferred away. That transfer can be legitimate only if fidelity is empirically checked rather than presumed from workshop attendance.

A third insight is that AI literacy is not generic onboarding. It must be **decision-specific comprehension**: what artifact is being authored, who or what will apply it, how outputs will affect training/evaluation/release, and which transformations are reversible. Experts confused evaluating the chatbot with evaluating criteria even after an orientation. A completion quiz on terminology would miss the problem; a contributor should instead demonstrate the actual score/transformation loop and approve concrete examples.

A fourth insight is that reciprocal value and trust are part of measurement quality, not only recruitment ethics. Experts contributed because they could learn, influence a community tool, and credibly explain it to colleagues. If the contribution interface is extractive, repetitive, or obscures downstream use, it selects who remains engaged and what depth they provide. Participation design therefore changes the expertise sample and the benchmark's content validity.

Finally, the team tuned judge prompts for closer alignment and preferred discriminating criteria while simultaneously using those scores for model refinement. Without held-out expert ratings and frozen criteria, this creates a circularity risk: apparent agreement or discrimination may be optimized on the same examples and preferences used to define the judge.

## Transferable design patterns

### 1. Contribution lifecycle (skill-bench adaptation)

The following record is a project adaptation, not a schema from the paper:

```yaml
contribution_id: ec-...
contributor_ref: pseudonymous-or-attributed-id
expertise_basis: role, experience, and coverage boundary
unit_type: critical_incident | requirement | example | rubric_edit | rating | adjudication
purpose_at_collection: task_design | source_pack | skill | training | evaluation | release_review
allowed_uses: [...]
prohibited_uses: [...]
attribution: named | pseudonymous | collective | private
ownership_or_license: explicit terms or unresolved
compensation_and_reciprocal_output:
  payment: amount/basis or none
  reusable_output: annotated rubric, report, tool access, findings, authorship, etc.
consent:
  version: ...
  comprehension_evidence: contributor inspected concrete input→transformation→output examples
  withdrawal_boundary: what can still be removed after incorporation/release
lineage:
  parent_contributions: [...]
  transformations:
    - actor_type: expert | developer | model | script
      operation: edit | summarize | synthesize | augment | operationalize | apply
      artifact_hash_before: ...
      artifact_hash_after: ...
      review_status: unreviewed | expert-reviewed | disputed | approved
rights:
  may_author: [...]
  may_review: [...]
  may_veto: [...]
  may_approve_release: [...]
reconsent_triggers: [new purpose, commercial use, public release, synthetic derivation, material role change]
```

The invariant is: a downstream artifact inherits provenance, not approval. Expert approval must be renewed after material transformations; it cannot propagate automatically from a parent artifact.

### 2. Role and decision-rights matrix (skill-bench adaptation)

| Stage | Expert authority | Builder authority | Automation role | Release evidence |
|---|---|---|---|---|
| Scope and boundaries | define coverage, exclusions, relational/safety limits; veto misrepresentation | propose benchmark goal and constraints | none | signed scope plus unresolved disagreement |
| Elicitation | choose contribution mode; inspect transcript/summary | facilitate and structure | transcription/organization only | contributor-approved record and locator |
| Primitive/task derivation | review whether derived requirement/trap preserves meaning | draft mappings and scenarios | suggest, never attest | transformation lineage plus expert disposition |
| Rubric/criterion authoring | define or revise professional standard | operationalize check language | test draft criteria on examples | before/after edits, examples, disagreement |
| Synthetic augmentation | approve generation purpose and sampled fidelity; veto unsafe derivation | generate and document lineage | create variants | stratified expert audit; unaudited variants cannot be “expert-approved” |
| Routine grading | calibrate anchors and audit disagreements | run deterministic/developer review | apply frozen checks | held-out expert agreement and drift audit |
| Release/claims | approve bounded expert-grounding and content claims | decide engineering release subject to gates | no release authority | claim-specific approvals, limitations, consent version |

This prevents the paper's observed shift—experts set criteria, then developers assume they can stand in for experts—from becoming an undocumented authority transfer.

### 3. Small contribution units with reciprocal outputs

Offer bounded units rather than “help build a benchmark”: one 30-minute critical-incident account; one rubric-anchor comparison; one synthetic-example audit batch; one disagreement adjudication; one release-claim review. Let experts choose voice, text, or live interaction and preview materials asynchronously. Return something useful: a polished decision rubric, de-identified failure-pattern report, authored domain note, benchmark access, or evidence pack for training colleagues.

This design extrapolates from fatigue, voice-mode requests, advance-material requests, learning motivation, and community influence. The exact durations and incentives are hypotheses to test, not findings from the paper.

### 4. Transformation and authority gates

Add gates that fail when:

- consent states “evaluation” but the material is used for training or public release;
- model-generated variants inherit an `expert_approved` label without post-generation review;
- builders apply a rubric without measured fidelity to held-out expert judgments;
- judge prompts or criteria are tuned on the same expert cases used to report agreement;
- no expert can identify how a contribution changed the released artifact;
- contributor objections are flattened into consensus;
- a benchmark claims domain-expert validity from institutional or research-review evidence alone.

### 5. Observable pilot measures

A first pilot should report separate outcomes:

- recruitment invitation→acceptance and completion rates;
- expert minutes and coordination minutes per accepted primitive/check;
- contribution depth and novelty by mode (voice, text, workshop);
- comprehension errors before contribution and after concrete system demonstrations;
- fraction of transformations reviewed, approved, disputed, or withdrawn;
- expert–builder and expert–grader agreement on held-out cases, with disagreements retained;
- fatigue/dropout by task repetition and session length;
- percentage of contributors receiving a reusable reciprocal output;
- consent changes and reconsent triggers exercised;
- representation coverage across expertise roles and dissenting AI orientations;
- release claims narrowed or blocked by experts.

No scalar “expert participation score” should average these away. Cost, fidelity, agency, coverage, and validity are distinct.

## Limitations

1. **Single favorable institution and domain.** The team, experts, stakeholders, and intended beneficiaries shared one university and pedagogical mission. This bounds transfer to commercial, adversarial, regulated, geographically distributed, or cross-institutional settings.
2. **Incomplete participant accounting.** The paper reports three developers and 18 simulator contributors but not the number of expert interviewees, workshop uniqueness/overlap, interview sampling denominator, refusals, attrition, or participant demographics.
3. **No cost evidence.** Experts were hourly compensated, but rates, total spend, unpaid coordination, and cost per usable dialogue/criterion are absent. The study cannot support near-zero-cost feasibility.
4. **Embedded single lead analyst.** The first author observed, sometimes facilitated, and led coding. Reflexive memos and co-author discussion help, but no independent coding, member checking, saturation claim, negative-case protocol, or audit trail is reported.
5. **No released qualitative materials.** Interview protocols are described with sample questions, but transcripts, codebook, coded excerpts, field-note corpus, analytic memos, and collected artifacts are unavailable. Confidentiality may justify this but limits reproducibility.
6. **No direct evaluation-quality evidence.** The paper reports no expert–developer agreement, expert–judge correlation, criterion reliability, repeated judge variance, held-out calibration, or adjudication outcomes.
7. **Synthetic-data fidelity is untested.** More than 130 expert dialogues became 1,000 synthetic dialogues without direct pre-training audit. The downstream model was evaluated, but that cannot identify which distortions the synthetic data introduced.
8. **Circular judge development.** Prompts were varied until scores aligned more closely with observed judgments, criteria were considered partly for model discrimination, and scores then drove model refinement. Frozen held-out expert anchors are not reported.
9. **Authority transfer is assumed, not validated.** Developers believed workshop participation taught them enough to substitute for expert evaluators. The paper records this rationale but provides no fidelity test.
10. **Consent recommendations are prospective.** Licensing boundaries, shared rights, recurring checkpoints, and reconsent were proposed after observing concerns, not evaluated as interventions.
11. **No deployment or longitudinal relationship evidence.** The 12 weeks cover one refinement phase. There is no evidence about long-term retention, commercialization, benefit sharing, contributor withdrawal, model updates, or realized harms.
12. **Relational expertise is acknowledged but not operationalized.** Experts emphasize confidentiality, vulnerability, and trust, yet the evaluation focuses on chatbot outputs and criteria; no instrument tests whether the system knows when not to imitate or replace consultation.
13. **Potential sponsor/context influence is not investigated.** The work was partly supported by a university–industry technology ethics lab, but the paper offers no analysis of whether funding or institutional hierarchy affected participation or reporting.
14. **Proposals exceed observations.** Authorship, shared output rights, and licensing-style agreements are plausible ethical responses but are not causally demonstrated solutions.

## Reproducibility and operational realism

Source reproducibility is good at the manuscript level: the immutable 14-page v1 PDF and full text are retained with hashes, methods and sample interview questions are described, and page-level claims are inspectable. Study reproducibility is weak because the codebook, participant table, observation corpus, interview data, evolving rubrics, judge prompts, ratings, synthetic corpus, and system artifacts are not released. A new team could imitate the broad method but could not reproduce the analysis or evaluation results.

Operational realism is the paper's main strength. It observes privacy vetoes, recruitment limits, dirty transcripts, asynchronous paid contribution, workshop design, fatigue, shallow input formats, unstable judge scores, deadline-driven synthetic augmentation, and migration from experts to developers and automation. These are precisely the hidden workflow states that polished participation frameworks omit.

But realism should not be mistaken for success. The paper documents how the project kept moving, not that each workaround preserved expertise or evaluation validity. For `skill-bench`, the substitutions themselves should become auditable events with evidence gates rather than accepted patterns.

## Concrete changes for skill-bench

1. **Extend contributor provenance into a separate participation lifecycle.** The current expertise-transfer schema records role, basis, contribution mode, and a coarse consent scope. It cannot represent purpose-specific use, prohibited use, compensation/reciprocity, transformations, attribution, ownership/license, withdrawal, reconsent triggers, or decision rights.
2. **Do not overload the ACTA task.** ACTA should still operationalize elicitation of cues, strategies, and critical incidents. A participation contract should govern who is asked, what exchange is offered, how derived artifacts are transformed, and who approves each use.
3. **Replace inherited “expert-grounded” labels with lineage states.** Expert-authored, expert-edited, expert-approved, expert-derived, and unreviewed synthetic artifacts must be distinct and machine-checkable.
4. **Reserve expert time for authority-bearing checkpoints.** Use builders and automation for formatting and routine application only after held-out calibration; route disagreement, boundary cases, transformation audits, and release claims back to experts.
5. **Require purpose-specific consent and concrete comprehension evidence.** Show the contributor actual source→derived task/rubric→grader/output examples. Reconsent when purpose, audience, commercialization, public visibility, or synthetic derivation changes.
6. **Preserve dissent and role diversity.** Recruit practical operators, researchers, and skeptical contributors; store independent dispositions before consensus. Institutional trust is not a substitute for disagreement evidence.
7. **Attach reciprocal outputs to contribution units.** Return reusable rubrics, authored notes, de-identified findings, benchmark access, or training materials and track whether experts consider them valuable.
8. **Pilot the workflow across domains before generalizing.** The paper's pedagogy setting is one test case. Measure cost, agency, fidelity, and retention in at least one domain with different confidentiality, commercial, and artifact norms.
9. **Add an explicit synthetic-transformation gate.** Synthetic examples derived from expert material require source lineage, purpose authorization, sampled expert fidelity review, disagreement logging, and a label that does not exceed the reviewed sample.
10. **Separate workflow continuation from validity.** A workaround can unblock engineering while failing an expert-grounding release gate; the schema should preserve both facts.

## Action items

- [x] Download, hash, extract, and read the complete immutable v1 primary source.
- [x] Reconstruct setting, participants, methods, substitution sequence, motivations, trust, fatigue, literacy, consent, ownership, and limitations with page evidence.
- [x] Separate observed findings, author proposals, and `skill-bench` adaptations.
- [x] Define a contribution lifecycle, role/decision-rights matrix, scoped contribution units, gates, and measurable pilot outcomes.
- [ ] Implement a participation/consent-lineage contract after current higher-priority pilot execution work, without folding it into ACTA's elicitation method.
- [ ] Exercise the contract with real qualified contributors; no internal builder fixture can validate motivation, comprehension, reciprocity, consent, or domain authority.
- [ ] Compare at least two contribution modes and preserve actual expert time, dropout, transformation fidelity, disagreement, and claim-blocking evidence.

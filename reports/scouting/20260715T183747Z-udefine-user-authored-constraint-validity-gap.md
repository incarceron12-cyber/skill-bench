# Scouting note — user-authored hard/soft constraint validity gap

**Timestamp:** 2026-07-15T18:37:47Z  
**Scope:** Narrow expansion against charter objectives A/B/C/F. Initial queue inspection found 286 tasks: 281 completed, three blocked, one pending human prerequisite, and one pending consolidation; no source, research, review, or claimed backlog remained. The reviewed corpus already covers hidden requirements, underspecified action boundaries, behavior-nominated preferences, expert-authored rubrics, dynamic criteria, and participation authority, but not an evaluated interface where users and domain experts explicitly classify natural-language planning constraints as strict obligations or negotiable preferences and those types dispatch to different verifiers.

## Substantive finding — triage only

**U-Define: Designing User Workflows for Hard and Soft Constraints in LLM-Based Planning** — Christine P Lee, Xinyu Jessica Wang, Aws Albarghouthi, David Porfirio, and Bilge Mutlu; arXiv:2605.02765v1.

- Immutable record: https://arxiv.org/abs/2605.02765v1
- Immutable PDF: https://arxiv.org/pdf/2605.02765v1
- Immutable HTML: https://arxiv.org/html/2605.02765v1
- Paper-linked OSF project: https://osf.io/7sgn3/overview?view_only=db6e205a5d034ec9991c25c1b316d0b9
- The arXiv API identifies immutable v1 as submitted 4 May 2026 in `cs.AI`, `cs.HC`, and `cs.LG`; its abstract contains no withdrawal or retraction notice. The versioned abstract, PDF, and HTML endpoints returned HTTP 200 during scouting.
- The abstract presents an interface where users write constraints in natural language and categorize them as hard rules or soft preferences. It says hard constraints are verified by formal model checking and soft constraints by an LLM judge.
- The abstract reports a technical evaluation and studies with general and expert participants, with improvements in perceived usefulness, performance, and satisfaction while maintaining usability. These are author-reported abstract claims, not independently verified results.
- Structural inspection of immutable-v1 HTML—not a full reading—confirmed system stages for definition, verification, and feedback; component evaluations for LTL translation and PRISM plan conversion; separate studies of everyday users and domain experts; measures and analysis; and discussion of constraint hierarchy, strict-rule expectations, violation-linked explanations, and authoring overhead.
- The immutable HTML exposes the OSF link above but no paper-specific GitHub repository. The OSF project's contents, timing, hashes, license, completeness, and correspondence to the paper were not inspected during scouting.
- Repository-wide exact-title and arXiv-ID searches found no local review or queue task. Closest completed reviews include UnderSpecBench, MapSatisfyBench, ResearchRubrics, JADE, Expert Disagreement in Human Feedback, and the Domain-Expert Participation Ethnography; none makes user assignment of hard-versus-soft requirement semantics to distinct executable evaluators its primary instrument.
- This is **metadata, abstract, endpoint, section-structure, release-location, and duplicate triage only**. The paper body, appendices, interface, prompts, translations, plans, constraints, participant records, expert domains, measures, statistics, failures, costs, OSF files, and results were not read or audited. No claim is made that participants faithfully expressed intent, type assignment was correct, natural language was translated faithfully into LTL, model checking covered real obligations, the LLM judge measured legitimate preferences, feedback repaired plans, experts validated substantive planning, findings transport across tasks or users, or U-Define establishes professional validity, production utility, or readiness.

## Why this is distinct

The reusable chain is `stakeholder authority and context → natural-language requirement → hard/soft/conditional type assignment → formal or semantic translation → verifier identity and evidence view → violation explanation → user correction or acceptance → plan/artifact/state consequence → satisfaction and substantive utility → transport and maintenance`. A typed interface could help benchmark contributors distinguish noncompensable obligations from preference-like criteria without hiding negotiability inside a single score. But the type itself may be wrong, a formally exact translation may faithfully enforce the wrong proposition, and a soft judge may collapse disagreement or context dependence into an opaque rating.

A full audit should separate authoring usability, expression fidelity, classification fidelity, translation correctness, verifier coverage, judge validity, explanation usefulness, correction uptake, plan quality, participant burden, and domain transport. It should identify what the domain-expert study actually validates and whether the OSF release permits independent inspection. Comparison with UnderSpecBench and MapSatisfyBench can test authorization and latent-preference boundaries; ResearchRubrics and JADE can test whether hard/soft typing adds a reusable criterion primitive rather than duplicating obligation, applicability, threshold, and evidence-view machinery.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier user/expert evaluation research), B (expertise and intent transformed into typed requirements), C (executable checks and verifier boundaries), and F (contributor burden and usable authoring workflows).
- **Concrete evidence/artifact:** immutable-v1 deep review plus a timing-aware audit of the paper-linked OSF artifacts.
- **Uncertainty clarified:** whether user-declared hard/soft constraints preserve intent and legitimate flexibility, or mainly improve one interface's usability and author-defined verifier performance.
- **Mode:** narrow expansion feeding later consolidation; vacation planning is an interaction test bed, not a permanent benchmark domain.
- **Duplication/scope:** no exact local duplicate; mandatory comparison with UnderSpecBench, MapSatisfyBench, ResearchRubrics, JADE, and participation machinery prevents a parallel constraint schema.
- **Useful completion:** a claim ladder separating expression, type assignment, translation, hard verification, soft judging, feedback, plan outcome, burden, transport, professional validity, and readiness, grounded in exact paper/release locators.

Added one low-priority task: `review-udefine-user-authored-constraint-validity` (priority 5). The consented expert micro-pilot and request-receipt repair consolidation remain substantially higher priority.

## Operational note

The required initial `git pull --ff-only` succeeded. Pre-existing untracked paper-source, release-archive, and site files were not touched.

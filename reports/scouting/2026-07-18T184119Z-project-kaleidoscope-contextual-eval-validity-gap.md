# Scouting note — contextual eval-authoring and judge-calibration validity gap

- **Timestamp:** 2026-07-18T18:41:19Z
- **Evidence status:** arXiv metadata/abstract and indexed HTML snippets, official project/documentation/repository discovery, live Git HEAD checks, and exact repository duplicate searches only. The PDF/full HTML body, pilot details, generated evaluation sets, rubrics, human labels, judge outputs, source code, tests, and reported analyses were **not** deeply read, downloaded into the repository, executed, reproduced, or audited during scouting.

## Substantive candidate — triage only

**Project Kaleidoscope: Contextual, Human-Aligned Evaluation for Real-World AI Applications** — Leanne Tan, Rohan Jaggi, Shaun Khoo, and Roy Ka-Wei Lee; arXiv:2607.14673v1.

- Immutable record/PDF/HTML: https://arxiv.org/abs/2607.14673v1 · https://arxiv.org/pdf/2607.14673v1 · https://arxiv.org/html/2607.14673v1
- Official project and documentation: https://govtech-responsibleai.github.io/kaleidoscope/
- Official implementation: https://github.com/govtech-responsibleai/kaleidoscope (live HEAD observed as `83bee80aa36b36483cd3b9e5742640f29ab8f372`)
- Linked evaluator-calibration implementation: https://github.com/govtech-responsibleai/meta-evaluator (live HEAD observed as `c0996b1e454440d183be988156853072cc4fa178`)
- Indexed arXiv metadata identifies a 16 July 2026 `cs.AI` submission. The abstract presents an integrated workflow joining persona-based test generation, contextualized rubrics, human review, and reliability-gated automated scoring. These are author-stated claims awaiting full-paper and release verification.
- Official documentation search surfaces describe persona-first generation of application-specific evaluation inputs, natural-language custom criteria, target calls through an HTTP endpoint, human annotation as ground truth, and candidate LLM-judge reliability measurement. The linked `meta-evaluator` search surface advertises comparison of judge results with human results and loading prior annotations for scoring-only workflows. Exact semantics, thresholds, leakage boundaries, and release/paper correspondence remain unaudited.
- Exact title, arXiv ID, and official-repository searches found no local review, queue item, or scouting note. ResearchRubrics, evaluator-disagreement work, rubric calibration, generated-evaluator validity, and expert participation are adjacent, but none audits this complete application context → generated cases → contextual criteria → human calibration → admitted automated judge production workflow.

## Why this is a narrow, useful gap

The reusable chain is:

`intended application and affected users → context/constraint evidence → persona coverage hypothesis → generated candidate input → admission/rejection → criterion provenance and applicability → human annotation and disagreement → candidate judge realization → calibration-set observation → reliability gate → untouched validation → automated score → monitored decision use`.

This directly advances charter objectives A, B, C, and F. Kaleidoscope could provide inspectable production machinery for lowering contextual-eval authoring and human-review cost. It could also expose an important validity boundary: agreement with human labels on a co-designed calibration sample is not evidence that generated personas represent affected users, criteria cover consequential quality, human labels carry legitimate expert/stakeholder authority, or the judge remains reliable under new contexts and prevalence.

A full review should reconstruct the source and authority of application context; candidate/generated/admitted case denominators; persona construction, stereotyping controls, and coverage warrants; criterion lineage, dependence, applicability, and transformations; annotator recruitment, training, blinding, order, missingness, disagreement, and adjudication; judge prompts/models/providers and shared-model coupling; metric choice, class balance, uncertainty, threshold selection, aggregation, abstention, untouched validation, drift monitoring, and rollback; pilot selection and decision use; human time and total cost; and exact release-to-paper reproducibility. It should test label imbalance, threshold overfitting, criterion dependence, unsupported criteria, persona perturbations, same-model coupling, judge abstention, and held-out context shift where artifacts permit.

## Charter decision filter and queue action

- **Objectives advanced:** A (production evaluation and human-evaluation frontier), B (context/expertise-to-test-and-rubric transformation), C (authoring, calibration, metric, and monitoring machinery), and F (scalable human contribution).
- **Concrete evidence:** immutable-v1 full-paper review plus timing-aware audit of the official application and evaluator releases, including representative lineage and executable calibration evidence where feasible.
- **Uncertainty clarified:** whether the workflow establishes context-valid test coverage and human-aligned automated scoring, or only calibration-sample agreement inside a co-designed generation/judging loop.
- **Mode:** narrow expansion. One high-priority execution-validity review was already pending; adding one lower-priority, distinct review preserves a small research buffer without displacing validation.
- **Duplication/scope check:** exact searches were negative. Existing contracts cover adjacent components but not this end-to-end production workflow. The source is application-agnostic and does not imply a chatbot or government scope commitment.
- **Useful completion:** reconstruct and challenge every context→persona→case→criterion→label→judge→gate→decision edge; preserve representativeness, construct-validity, expert-authority, decision-utility, production-fitness, and readiness claim ceilings.

Added one task: `review-project-kaleidoscope-contextual-eval-validity` (review, priority 51). No second source was queued.

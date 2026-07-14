# Scouting note — skill-derived task projection validity at scale

**Timestamp:** 2026-07-14T21:52:22Z  
**Scope:** Narrow expansion against charter objectives A/B/C. The queue had 230 tasks before this addition: 223 completed, four blocked, two pending human decisions, and one pending consolidation; no source/research/review task remained. Existing deep reviews cover curated paired skills (SkillsBench), expert procedural rubrics (LH-Bench), and generated skill-relation cases (SLBench), but not this author-facing method or its 500-skill scale.

## Substantive finding (triage only)

**A Framework for Evaluating Agentic Skills at Scale**

- Immutable record: https://arxiv.org/abs/2606.17819v1
- Immutable PDF: https://arxiv.org/pdf/2606.17819v1
- Immutable HTML: https://arxiv.org/html/2606.17819v1
- Paper-linked dataset: https://huggingface.co/datasets/tesslio/task-evals-for-skills
- The arXiv API identifies Maksim Shaposhnikov, Nicolas Fortuin, Simon Stipcich, Maria I. Gorinova, Amy Heineike, and Rob Willoughby; category `cs.SE` with `cs.AI`/`cs.CL`; submitted 16 June 2026 with no later version. The summary contains no withdrawal notice. Versioned abstract, PDF, and HTML URLs returned HTTP 200, as did the linked Hugging Face dataset page.
- The **v1 abstract** reports an author-facing method for constructing realistic evaluations of an individual skill, a corpus of 500 real-world skills, 1,000 tasks derived from skill content, instruction-following and goal-completion rubrics, and comparisons across 19 agent-model configurations. It reports heterogeneous adherence and performance gains and says skill access significantly changes behavior. These are author-reported abstract claims, not independently verified findings.
- Immutable HTML structure exposes dedicated sections for evaluation framework, dataset construction, experimental setup, relative gains, instruction following versus goal completion, cheaper/frontier model comparisons, skill-type effects, and skill diagnosis. It links the dataset above but no GitHub implementation surface was found in targeted searches.
- The distinctive validity question is **shared projection**: when source skill text produces the task, task-facing instructions, and scoring rubrics, measured “utility” may combine genuine transferable procedure, instruction imitation, answer-bearing cues, and agreement among transformations of the same source. Scale does not resolve this circularity. Full review should determine who selected and authorized the skills, how licensing/security/quality filters changed the inference population, whether tasks and goal criteria were independently validated, whether legitimate alternatives survive, and whether paired uncertainty respects task-within-skill and configuration clustering.
- This is **metadata, abstract, section-structure, URL, and duplicate triage only**. The PDF body, appendices, dataset bytes, source skills, generated tasks/rubrics, configurations, traces, results, and statistical analyses were not read or audited. No claim is made that the framework establishes skill utility, expertise transfer, cross-domain gains, professional validity, capability, or readiness.

## Benchmark implication to test

Skill evaluation needs an authority-preserving chain: `source skill identity/license/author scope → claimed procedure and intended context → independently justified task demand → skill-to-task transformation → public intervention → separately authored criterion and admissible evidence view → no-skill/skill configured pair → artifact/state/trace observations → clustered effect and failure analysis → transport boundary`. Deriving both challenge and score from the intervention is useful for conformance testing but can mistake self-consistency for consequential skill transfer.

A full audit should compare this paper with SkillsBench, LH-Bench, and SLBench, and should stratify released examples end-to-end to inspect overlap, hidden prerequisites, rubric leakage, alternative valid paths, external dependency availability, and criterion independence. Transfer should reuse intervention/instrument, projection, evidence-view, configured-system, metric, and validity records rather than create a skill-specific schema.

## Charter decision filter and queue action

- **Objectives advanced:** A (skill-evaluation frontier), B (expertise/intervention-to-task-and-rubric validity), and C (evidence for scalable paired evaluation).
- **Evidence/artifact sought:** immutable-v1 deep review, pinned dataset audit, and stratified source-skill→task→rubric reconstruction.
- **Uncertainty clarified:** whether content-derived tasks identify useful procedural transfer or only shared-source compliance, and what population/configuration claims the scale licenses.
- **Mode/balance:** one low-priority review task restores a minimal research backlog behind the pending consolidation and human blockers; no broad source bundle was added.
- **Duplication/scope:** complements rather than repeats three existing skill reviews; skills are an intervention case for the general expertise-transfer hypothesis, not a narrowing of the benchmark.
- **Useful completion:** preserve source selection, transformations, task/rubric authority, paired configuration identity, clustering/missingness/invalids, cost, release drift, and strict claim ceilings.

Added `review-agentic-skills-at-scale-projection-validity` (priority 18). No second task was added.

## Operational note

The required initial `git pull --ff-only` failed because the HTTPS GitHub remote lacks a noninteractive credential (`could not read Username`). Local `main` was 38 commits ahead of recorded `origin/main`; the run proceeded from local state. The pre-existing untracked `data/papers/source/` tree was not modified.

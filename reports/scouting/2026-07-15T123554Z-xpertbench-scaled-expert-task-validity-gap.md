# Scouting note — scaled expert-task and ShotJudge validity gap

**Timestamp:** 2026-07-15T12:35:54Z

**Scope:** Narrow expansion against charter objectives A/B/F. Queue inspection found 267 tasks: 262 completed, three blocked, and two pending (one human prerequisite and one consolidation); no source, research, or review task remained. The corpus already covers expert-authored tasks, rubric construction, participation governance, incentive design, and human/model rater effects, so this run revisited one previously deferred candidate specifically for its scaled contribution pipeline rather than repeating broad benchmark discovery.

## Substantive finding — triage only

**Xpertbench: Expert Level Tasks with Rubrics-Based Evaluation** — Xue Liu et al.; arXiv:2604.02368v4.

- Immutable current record: https://arxiv.org/abs/2604.02368v4
- Immutable current PDF: https://arxiv.org/pdf/2604.02368v4
- Paper-linked platform: https://xpert.bytedance.com/
- Paper-linked leaderboard: https://xpert.bytedance.com/leaderboard
- The arXiv API identifies v4 as the current immutable version, originally submitted 27 March 2026 and updated 21 April 2026 in `cs.AI` and `cs.CL`; its summary contains no withdrawal or retraction notice. The versioned abstract, PDF, and HTML endpoints returned HTTP 200 during scouting.
- The abstract reports 1,346 retained tasks across 80 categories in finance, healthcare, law, education, STEM research, and humanities/social-science research, derived from more than 1,000 expert submissions. It describes mostly 15–40 weighted rubric checkpoints per task and introduces `ShotJudge`, which uses expert few-shot exemplars to calibrate model judging.
- The abstract reports a top success rate of approximately 66%, mean score around 55%, and domain-specific model differences. These are author-reported abstract claims, not independently verified findings; submission count is also not an accepted-item denominator, participation-cost estimate, ecological-validity argument, or evidence of professional competence.
- Structural inspection of immutable-v4 HTML—not a full reading—confirmed sections on expert recruitment and training, prompt curation, rubric design and quality control, evaluation, experiments/results, contributions, the Xpert platform/leaderboard, and example tasks/rubrics for finance, law, education, STEM, and humanities/social sciences.
- The immutable HTML directly links the ByteDance Xpert platform and leaderboard but does not directly link a code or dataset release. Search surfaced `randomtutu/Xpertbench` (Git HEAD `b08e51dada00996f5a49864539230c3aea7d2e9c`) and public Hugging Face dataset `ByteSeedXpert/expertbench` (API revision `c6d1fdf0469243d4e14b921f80e41e845a0e1038`), but their author ownership, official status, contents, timing, and correspondence to v4 were not established. They are release leads only.
- Repository-wide exact-title and arXiv-ID search found no local review or queue task. Two earlier scouting notes explicitly deferred XpertBench while more direct participation and expert-labor sources were queued. Those sources and many adjacent benchmark/rater reviews are now complete, while no review backlog remained; the candidate is therefore reopened only as a bounded comparator.
- This is **metadata, abstract, endpoint, section-structure, release-location, and duplicate triage only**. The paper body, appendices, v1→v4 changes, platform, leaderboard, tasks, rubrics, exemplars, judgments, results, contributor records, costs, and surfaced release leads were not read or audited. No claim is made that contributors were representative or fairly supported, that retained tasks are ecologically valid, that rubric checkpoints preserve expert judgment, that ShotJudge is calibrated or independent, that headline scores are reliable, or that the benchmark establishes expert-level capability, professional competence, low-cost participation feasibility, production fitness, or readiness.

## Why this is distinct

The potentially reusable chain is `contributor population and recruitment → training/incentives/rights → submitted candidate and provenance → acceptance, rejection, revision, and attrition → task/rubric transformation and authority → accepted alternatives and dependencies → expert exemplar selection → ShotJudge information view and configured calls → criterion decisions and aggregate score → external professional judgment and use`. Scale at one link does not validate the next.

The closest reviewed benchmarks study selected expert tasks or expert-authored criteria, and ELAIPBench studies a competitive author/verifier mechanism. XpertBench may add evidence about operating a much larger multi-domain submission funnel and exemplar-conditioned grading. Conversely, a large purposive retained set can hide contributor concentration, rejected-item cost, common author–rubric–judge cues, and category-level dependence. A full audit should determine whether the source contributes a reusable expert-contribution workflow or primarily another opaque expert-label claim.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier professional benchmark research), B (expertise-to-task/rubric transfer), and F (feasibility of scaled expert contribution).
- **Concrete evidence/artifact:** immutable-v4 deep review plus a timing-aware platform and verified-official-release audit.
- **Uncertainty clarified:** whether reported scale supplies diverse provenance and operational participation evidence; whether expert-example-conditioned judging improves criterion agreement without conflating rubric authority, judge calibration, and professional validity.
- **Mode:** narrow expansion; the six reported domain groupings are comparators, not a scope commitment.
- **Duplication/scope:** previously deferred rather than forgotten; now nonduplicate because its scaled submission funnel and ShotJudge treatment are not covered. Mandatory comparisons are Agents' Last Exam, GDPval, ResearchRubrics, ELAIPBench, Many-Facet Human/AI Rater Effects, and Rubric Modification.
- **Useful completion:** separate submission volume, retained-set validity, contributor feasibility, rubric authority, judge agreement/calibration, configured-system performance, professional competence, and readiness; reuse existing machinery unless genuinely new evidence requires otherwise.

Added one task: `review-xpertbench-scaled-expert-task-validity` (priority 9). The pending criterion-operating-envelope consolidation and consented human elicitation prerequisite remain much higher priority.

## Operational note

The required initial `git pull --ff-only` succeeded. Pre-existing modified/untracked README, site, paper-source, release, and script artifacts were not touched.

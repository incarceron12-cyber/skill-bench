# Scouting note — expert-to-executable artifact-evaluation workflow gap

**Timestamp:** 2026-07-15T13:58:47Z  
**Scope:** Narrow expansion against charter objectives A/B/C. Initial queue inspection found 270 tasks: 266 completed, three blocked, one pending human prerequisite, and no worker backlog. The corpus already covers expert rubric authoring, research replication, automated benchmark-defect triage, judge reliability, artifact evidence views, and reviewer burden. This run therefore searched only for evidence connecting an expert evaluation policy to executable artifact inspection and downstream reviewer use.

## Substantive finding — triage only

**Agent-Based Software Artifact Evaluation** — Zhaonan Wu, Yanjie Zhao, Zhenpeng Chen, Zheng Wang, Haoyu Wang; arXiv:2602.02235v3.

- Immutable current record: https://arxiv.org/abs/2602.02235v3
- Immutable current PDF: https://arxiv.org/pdf/2602.02235v3
- Candidate official artifact record: https://zenodo.org/records/18410765
- The arXiv API identifies v3 as current, originally submitted 2 February 2026 and updated 14 July 2026. The summary contains no withdrawal or retraction notice. The versioned abstract and PDF endpoints and Zenodo record returned HTTP 200 during scouting; versioned arXiv HTML returned 404, so it was not used as full-text evidence.
- The current abstract describes `ArtifactGuide`, a structured rubric grounded in ACM policy, expert-informed calibration, and artifact-based validation, plus `ArtifactCopilot`, which gathers review evidence in a fixed sequence and derives badge decisions. It reports 60 real software-research artifacts, human-adjudicated badge references, repeated runs, and a controlled study with eight experienced researchers.
- The abstract reports a 10.55–28.34 percentage-point increase in three-run mean exact badge agreement over official-policy prompts, 70.56% badge-level agreement for ArtifactCopilot, completion/report production in every repeated run, and reviewer confidence/evidence-location/scope benefits. These are author-reported abstract claims, not independently verified findings. Criterion authority, environment/execution validity, exact badge agreement, inter-run reliability, report usability, reviewer decision quality, burden, and expert substitution are different estimands.
- Search found a Zenodo artifact titled *Artifact for ArtifactCopilot* and an arXiv HTML snippet describing an AE Graph and state-aware workflow. Neither the record files nor the paper body were inspected. A search result also exposed a third-party GitHub `SKILL.md`; it is not evidence of an official paper release and should not be treated as one.
- Repository-wide exact-title, arXiv-ID, `ArtifactGuide`, and `ArtifactCopilot` searches found no local review or task. The closest reviews are ResearchRubrics (expert criterion authoring), PaperBench (agent-generated replication artifacts), Auto Benchmark Audit (candidate instrument defects), AgentRewardBench (judge reliability), and artifact-view/task-health work. None studies this complete policy→criterion→stateful inspection→evidence report→badge→reviewer-use chain.
- Two related arXiv candidates were triaged but not queued: *Artisan: Agentic Artifact Evaluation* (2602.10046v1) emphasizes reproduction-script generation and automated judging, while *An Agentic Approach Towards Replication Package Quality Evaluation* (2606.02006v1) reports 31 operationalized criteria over five packages. ArtifactCopilot was selected because the current v3 abstract reports the strongest combination of expert-informed rubric construction, real-artifact evaluation, repeated configured runs, human-adjudicated decisions, and downstream reviewer study. A full review should compare these neighbors before asserting uniqueness.
- This is **metadata, abstract, endpoint, release-location, and duplicate triage only**. The v3 body, appendices, tables, rubric, artifact files, sample frame, adjudication protocol, repeated-run records, statistics, user-study instrument, costs, and version changes were not read or audited. No claim is made that ArtifactGuide is complete or authoritative, ArtifactCopilot evidence is sufficient, badges are correct, reports improve decisions, the release reproduces the paper, or the system supports autonomous review, expert substitution, general evaluator validity, professional readiness, or production fitness.

## Why this is distinct

The reusable chain is `policy/source authority → expert calibration → executable criterion and dependencies → artifact/environment identity → state-aware plan and execution graph → evidence collection and sufficiency → badge aggregation/decision → reviewer evidence uptake → reviewer decision quality, burden, and downstream consequence`. Each link can fail independently. This directly tests whether a complex professional review procedure can become proof-carrying benchmark/evaluator machinery without reducing expertise to an endpoint label.

The main validity risks are co-authored rubric/reference decisions, selected and clustered artifacts, badge hierarchy/dependence, environment and service invalidity folded into substantive failure, fixed-sequence path bias, one accepted workflow excluding alternatives, report persuasion mistaken for correctness, confidence without decision improvement, and a small user study that may not establish general reviewer utility. A full audit should reconstruct versioned criterion and call topology, preserve raw observations and invalid denominators, and compare exact badge agreement with criterion-level errors, severe decision flips, evidence sufficiency, repeated-run variance, time/burden, and reviewer decisions.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier production/scalable evaluation), B (expert-policy-to-criterion transfer), and C (artifact/trace/grader infrastructure).
- **Concrete evidence/artifact:** immutable-v3 deep review plus pinned Zenodo release audit and a comparison against existing rubric, artifact, judge, and task-health evidence.
- **Uncertainty clarified:** whether structured, state-aware agent evaluation preserves authorized expert criteria and improves reviewer decisions, or only matches selected badge labels and produces persuasive reports.
- **Mode:** narrow expansion/validation; software artifact evaluation is a test case for reusable professional-review machinery, not a domain commitment.
- **Duplication/scope:** no local duplicate; two adjacent artifact-evaluation papers were retained as comparison leads rather than separately queued.
- **Useful completion:** separate policy authority, rubric completeness, execution/environment validity, evidence sufficiency, badge agreement, repeatability, reviewer uptake, decision quality, burden/cost, transport, and readiness.

Added one task: `review-artifactcopilot-evaluation-workflow-validity` (priority 8). The consented human elicitation prerequisite remains much higher priority.

## Operational note

The required initial `git pull --ff-only` succeeded. Pre-existing untracked paper-source, release, and site files were not touched.

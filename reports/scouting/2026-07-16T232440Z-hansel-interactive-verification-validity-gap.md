# Scouting note — HANSEL interactive-verification validity gap

- **Timestamp:** 2026-07-16T23:24:40Z
- **Evidence status:** arXiv API metadata/abstract, immutable endpoint checks, paper-HTML link triage, Git ref/API metadata, and paper-linked repository README triage only. The PDF, technical-evaluation corpus and labels, prompts, study protocol, datasets, surveys, notebook, and analysis were **not** deeply read or audited during scouting.

## Substantive candidate — triage only

**HANSEL: Extracting Breadcrumbs from Web Agent Trajectories for Interactive Verification** — Yujin Zhang and Daye Nam, arXiv:2606.18671v1.

- Immutable record: https://arxiv.org/abs/2606.18671v1
- Immutable PDF: https://arxiv.org/pdf/2606.18671v1
- Paper-linked supplement: https://github.com/cloudsreal/hansel_study
- The arXiv API reports one version submitted 17 June 2026 in `cs.HC`, 13 pages and six figures, with no withdrawal notice. Versioned abstract, PDF, and HTML endpoints returned HTTP 200.
- The abstract describes an interface that projects a web-agent trajectory into navigable evidence pages/snippets while preserving page state such as filters, queries, and scroll positions, and flags answers unsupported by any visited page. It reports a 45-task AssistantBench/Online-Mind2Web technical evaluation (83.7% evidence-page precision, 88.8% recall, and 61.6% trajectory-volume reduction) and a controlled study with 14 participants reporting lower completion time and effort plus higher usability, verification ease, and error identification. These are author claims awaiting full-paper and release verification.
- The paper HTML links a non-fork author repository. `git ls-remote` resolved current `main`/HEAD to `a23466cf71eb4e466ffaa7a59b4f672f74f80658`; GitHub reports creation on 29 April 2026 and no detected license. README triage says the release contains the LLM prompts, complete study protocol, raw and derived datasets, quantitative-analysis notebook, and recruitment/pre/task/post surveys. It does not claim to contain the HANSEL implementation, technical-evaluation trajectories, evidence labels, or replayable page states. Release completeness and paper correspondence were not established during scouting.

## Why this is a narrow, useful gap

The reviewed corpus already covers Pista's semantic-diff oversight interface, ArtifactCopilot's criterion-linked evidence packets, trajectory evidence views, selective review, and human-review burden. It does not cover this exact chain:

`agent trajectory and visited-page state → selected evidence page/snippet and unsupported-answer flag → compressed interactive evidence view → participant inspection → verification judgment/error identification → review time and effort → downstream acceptance or correction`.

Each arrow is a distinct validity question. High evidence-page recall does not establish snippet truth, complete contradiction/negative-evidence coverage, page-state replay, or a correct verification decision. Lower review time can reflect useful compression, omitted evidence, or interface guidance. Error identification requires matched defect opportunities and independently correct labels; favorable usability and perceived effort do not establish calibrated trust or downstream decision quality. Web shopping is a bounded interface substrate for a general scalable-evaluation question, not a benchmark scope commitment.

## Charter decision filter and queue action

- **Objectives advanced:** A (human/expert and trajectory evaluation frontier), B (evidence-to-judgment methodology), and C (scalable evaluation and inspectable trace machinery).
- **Concrete evidence:** immutable-v1 full-paper review plus exact-commit supplement audit, with reconstruction of technical labels/denominators and the released user-study design/data/analysis.
- **Uncertainty clarified:** whether compressed evidence breadcrumbs are faithful, complete enough, and causally useful for correct verification rather than merely easier to consume; what oversight and benchmark-operation claims the two evaluations license.
- **Mode:** narrow expansion feeding validation/consolidation. Before this addition the queue had no pending review/source/research task, one pending consolidation, and one human prerequisite.
- **Duplication/scope check:** Pista and ArtifactCopilot are nearest neighbors, but neither evaluates post-hoc trajectory-to-page-state compression with evidence-selection precision/recall and a released controlled-study supplement. Existing machinery should be reused; no new schema is proposed.
- **Useful completion:** audit sample/label authority, page/snippet/state fidelity, compression denominator, missing evidence, model/configuration identity, study assignment and shared error opportunities, outcome correctness, clustering/missingness/multiplicity, burden, automation anchoring, and release completeness; preserve bounded claim ceilings.

Added one task: `review-hansel-interactive-verification-validity` (priority 9). No full-paper, implementation-correctness, oversight-effect, professional-validity, calibrated-trust, production-utility, or readiness claim was made during scouting.

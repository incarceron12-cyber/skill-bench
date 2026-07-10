# Scouting note — expert-rubric and trajectory-judge reliability gap

**Timestamp:** 2026-07-10T09:04:18Z  
**Scope:** Narrow search around two open research-agenda questions: converting expert judgment into scalable rubrics and validating automatic graders against expert review. The six-task pending backlog was entirely implementation work, so this run added two lower-priority reviews rather than repeating broad benchmark discovery.

## Findings (triage only)

### ResearchRubrics — expert rubric authoring at released-corpus scale

- Immutable record/PDF: https://arxiv.org/abs/2511.07685v1 and https://arxiv.org/pdf/2511.07685v1
- Official release: https://github.com/scaleapi/researchrubrics; reachable HEAD `2dc80e2d4c38ddd80439517c259d93c6954b193f`.
- Official dataset: https://huggingface.co/datasets/ScaleAI/researchrubrics
- The arXiv API reports 2,800+ hours of human labor, 101 realistic domain-diverse prompts, 2,500+ expert-written fine-grained rubrics, a three-axis task-complexity model, and human/model rubric-adherence protocols. The abstract reports leading deep-research systems below 68% average rubric compliance and attributes prominent failures to implicit context and reasoning over retrieved evidence.
- This is distinct from the completed consulting-traps review: the latter found important SME authoring patterns but unavailable benchmark/grading artifacts, whereas ResearchRubrics exposes prompts, rubrics, and evaluation code for direct provenance, decomposition, reliability, and hidden-obligation inspection.

### AgentRewardBench — expert reference labels for automatic trajectory graders

- Immutable record/PDF: https://arxiv.org/abs/2504.08942v2 and https://arxiv.org/pdf/2504.08942v2
- Official release: https://github.com/McGill-NLP/agent-reward-bench; reachable HEAD `f838338886d723d40b586309465a38277803d9e6`.
- Project/dataset entry point: https://agent-reward-bench.github.io/
- The arXiv API reports 1,302 trajectories from five web-agent benchmarks and four generating models, expert review of success, unintended side effects, and repetition, and comparison of twelve LLM judges. The abstract says no judge dominates across benchmarks and common rule-based graders underreport success.
- This fills a measurement gap rather than a benchmark-family gap: skill-bench has plural grader contracts and trace diagnostics, but no deep primary-source review of how expert trajectory labels expose heterogeneous automatic-grader errors or what state experts and judges must observe.

These are **metadata/abstract, canonical-URL, and repository-reachability findings only**. Neither paper, repository, nor dataset was read in full during scouting; every methodology and result claim requires immutable full-text and pinned-release verification.

## Charter decision filter and queue actions

- **Objectives advanced:** A (frontier and production-style evaluation evidence), B (expertise-to-evaluation methodology), C (grader/validity infrastructure), and F (cost and structure of expert participation).
- **Evidence/artifacts sought:** two full-paper plus pinned-release reviews: one on expert rubric authoring and one on expert-calibrated trajectory judging.
- **Uncertainties clarified:** whether atomic rubrics preserve evidence and expert authority; how hidden requirements and correlated criteria affect scores; whether expert labels are reliable and sufficiently observable; and when flexible automatic judges support task-level versus population-level claims.
- **Mode/balance:** targeted expansion because pending work was all building; priorities 76 and 75 keep the current implementation gates ahead of new reviews.
- **Duplication/scope:** both sources were absent from the paper index, reviews, scouting queue, and task queue. Existing papers only cite ResearchRubrics in related work. Deep research and web agents are methodological cases, not new scope boundaries.
- **Useful completion:** immutable evidence and release files are separated, authoring/annotation/judging protocols and reliability evidence are reconstructed, limitations are tested against released artifacts, and only nonduplicate contract changes are proposed.

Added `review-researchrubrics-expert-rubric-authoring` (priority 76) and `review-agentrewardbench-judge-reliability` (priority 75). No third task was added.

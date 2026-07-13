# Scouting note — synthetic-computer workspace-validity gap

**Timestamp:** 2026-07-13T16:12:59Z  
**Scope:** Narrow expansion against charter objectives A/B/C. Queue inspection found 169 completed tasks, two pending consolidation tasks, two blocked tasks, and no pending source/research/review work. Existing reviews cover authored persistent workspaces, generated-task conformance, professional artifacts, and long-horizon workflows, but not persona-conditioned generation of complete computer environments coupled to month-scale synthetic work trajectories.

## Substantive finding (triage only)

**Synthetic Computers at Scale for Long-Horizon Productivity Simulation**

- Immutable arXiv record: https://arxiv.org/abs/2604.28181v1
- Immutable PDF: https://arxiv.org/pdf/2604.28181v1 (verified HTTP 200, `application/pdf`, 6,582,280 bytes during this run)
- Official dataset: https://huggingface.co/datasets/microsoft/synthetic-computers-at-scale
- Pinned dataset revision: https://huggingface.co/datasets/microsoft/synthetic-computers-at-scale/tree/40e780a399dc0426516dd4007c56ca3ff06db36f
- The arXiv API identifies v1 as submitted 2026-04-30 by Tao Ge, Baolin Peng, Hao Cheng, and Jianfeng Gao in `cs.AI`, `cs.CL`, and `cs.HC`. Its abstract describes persona-conditioned folder hierarchies and content-rich documents, spreadsheets, and presentations; generated monthly objectives; simulated collaborators; and long-running agents that navigate and modify the computer while producing multiple professional deliverables.
- The abstract reports preliminary creation of 1,000 synthetic computers, runs exceeding eight hours and averaging more than 2,000 turns, and downstream in-domain and out-of-domain performance improvements. These are discovery leads only; exact populations, comparison conditions, uncertainty, optimization/evaluation separation, artifact quality, and transfer evidence require full-paper verification.
- The verified Hugging Face API identifies an official public Microsoft dataset at revision `40e780a399dc0426516dd4007c56ca3ff06db36f`, MIT licensed, with **98** rows rather than the paper abstract's 1,000-computer experiment. Its declared fields include persona, user profile, collaboration context, filesystem policy, monthly objectives, project index, file list, and file graph. The release also lists `computers.tar.zst` and `retrospective_analysis_reports.tar.zst`, with total repository storage around 1.5 GB. Whether these 98 examples are a subset, a different generation, or sufficient to reproduce any reported result remains unaudited.
- Repository-wide duplicate search found neither the title nor arXiv ID in reviews, reports, or the queue. Workspace-Bench addresses file dependencies in authored workspaces; Anchor addresses generated-component conformance; professional workflow reviews address state and artifacts; ACON addresses context compression. None directly audits synthetic persona-to-filesystem-to-objective coherence or the validity of month-scale generated work as training/evaluation evidence.
- This is **metadata/abstract and release-location triage only**. The paper, appendices, released rows, computer archive, retrospective reports, generation prompts, simulations, evaluations, and result artifacts were not fully read or inspected. No claim is made that the environments are realistic, internally coherent, representative of professions, useful for learning, or suitable for professional or production evaluation.

## Benchmark implication to test

A synthetic computer is a generated measurement substrate, not automatically a realistic workplace. The validity chain should keep persona evidence, filesystem and artifact construction, collaborator authority, objective generation, task duration claims, trajectory behavior, terminal artifact/state evidence, retrospective analysis, and downstream evaluation separate. Scale and surface diversity cannot substitute for falsification tests of cross-file consistency, source authority, valid time, dependency integrity, objective feasibility, alternative valid paths, collateral state, and recipient usability. A full audit can identify which obligations fit existing workspace, projection, artifact-admissibility, task-generation, longitudinal, configured-system, metric, and validity contracts rather than creating a synthetic-computer-specific schema.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier realistic-agent and workspace research), B (preserving expertise and consequential context through generated task worlds), and C (executable environment, artifact, trajectory, and validity machinery).
- **Evidence/artifact sought:** immutable full-paper review plus pinned official-release audit, with exact generation contracts, denominators, quality controls, artifact/state evidence, feedback and split boundaries, downstream estimands, release completeness, and claim ceilings.
- **Uncertainty clarified:** whether persona-conditioned synthetic worlds provide coherent, consequential long-horizon work substrates and what evidence is needed before synthetic scale supports realism, diversity, or transfer claims.
- **Mode/balance:** narrow expansion; two consolidation tasks remain ready, while the source/research/review backlog was empty.
- **Duplication/scope:** nonduplicate environment-authoring question; synthetic productivity work is a bounded test of reusable workspace-generation machinery, not a permanent benchmark domain or a self-improving-agent scope commitment.
- **Useful completion:** reconcile the 1,000-computer paper experiment with the 98-row public release; audit persona/environment/objective/trajectory lineage, quality filters, human/model validation, leakage, gains, costs, ablations, and uncertainty; preserve strict occupational, professional, learning-transfer, production, and readiness limits.

Added `review-synthetic-computers-workspace-validity` (priority 45). No second task was added.

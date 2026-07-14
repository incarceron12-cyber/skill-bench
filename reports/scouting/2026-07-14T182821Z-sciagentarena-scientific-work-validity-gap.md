# Scouting note — SciAgentArena scientific-work validity gap

**Timestamp:** 2026-07-14T18:28:21Z  
**Scope:** Narrow expansion against charter objectives A/B/D. Queue inspection found 219 tasks: 214 completed, three blocked, one pending build, and one pending human decision; no source/research/review task remained. Existing work covers research judgment (AARRI), scientific-agent infrastructure cited in local papers (AstaBench), laboratory-workflow elicitation, and generic professional-work validity, but not this released multi-domain scientific-work benchmark.

## Substantive finding (triage only)

**SciAgentArena — “Benchmarking AI Agents for Addressing Scientific Challenges Across Scales”**

- Immutable arXiv record: https://arxiv.org/abs/2606.12736v1
- Immutable PDF: https://arxiv.org/pdf/2606.12736v1
- Immutable HTML: https://arxiv.org/html/2606.12736v1
- Paper-linked project page: https://sciagentarena.github.io/
- Paper-linked implementation: https://github.com/HelloWorldLTY/SciAgentArena
- Paper-linked dataset: https://huggingface.co/datasets/iLOVE2D/SciAgentArena
- The arXiv API identifies Tianyu Liu and 32 coauthors; v1 was submitted 10 June 2026, has no later arXiv version or withdrawal notice, and links the project page from its abstract. The versioned abstract, PDF, and HTML URLs returned HTTP 200 during this run.
- The **v1 abstract** describes approximately 200 tasks, stepwise verification, and an interactive agent-agnostic environment. It says scenarios come from emerging needs across multiple domains and reports stronger performance on well-specified data-analysis workflows than on novel insight generation, self-directed exploration, and open-ended solution formulation. These are author-reported abstract claims, not independently verified findings.
- The project/search metadata names five biomedical and life-science domains—single-cell omics, spatial omics, drug discovery, electronic health records, and genetics—and three question types. This creates a useful but potentially narrower-than-worded coverage question: “multiple domains” is not automatically broad scientific-work representativeness, and stepwise verifiability may favor workflows with known decompositions over genuinely open-ended research.
- The project page directly links `HelloWorldLTY/SciAgentArena` and the gated Hugging Face dataset. GitHub API metadata shows the implementation repository was created 12 February 2026 and last pushed 22 June 2026; the project-site repository was created 9 June and last pushed 12 June. Neither release was pinned or audited during scouting.
- Repository-wide duplicate search found only citations to AstaBench and AgencyBench in acquired paper text; it found no SciAgentArena review, acquisition record, scouting note, or queue task. SciAgentArena is distinct from AARRI’s research-judgment/stop-escalate tasks and the laboratory workflow-twin elicitation study because it combines scientific datasets, executable analysis, stepwise checks, and an interactive benchmark across several research domains.
- This is **metadata, abstract, URL, release-location, and duplicate triage only**. The paper, appendices, task files, datasets, code, prompts, environments, graders, trajectories, failure labels, result tables, and repository history were not fully read or audited. No claim is made that tasks are expert-authorized, representative of scientific work, valid tests of novelty or autonomy, reproducible, professionally valid, reliable, safe, production-fit, or ready for consequential use.

## Benchmark implication to test

Scientific-work claims need a typed chain: `research-demand/source provenance → domain and activity sampling frame → task/question projection → data/tool/environment state → accepted workflow or alternative paths → step and endpoint observations → scientific artifact/claim → independent expert acceptance → downstream research use or consequence`. Stepwise agreement with one authored decomposition can improve diagnosis while also narrowing the solution set, leaking evaluator structure, and double-counting dependent checkpoints. A full review should therefore test source and expert authority, task-family denominators, domain clustering, prerequisite/dependency graphs, alternative valid analyses, tolerance calibration, invalid-environment handling, configuration identity, repeated outcomes, and whether novelty/self-direction labels are independently operationalized rather than inferred from low scores.

The reusable question for `skill-bench` is what to retain from a scientific benchmark’s data-rich interactive environment and stepwise verification, what to repair in task/claim provenance and alternative-path handling, and what falsification would support “real research,” novelty, autonomy, or reliability claims. Existing task projection, artifact/evidence-view, workflow-state, task-health, metric, trace, root/surface, and validity machinery should host the implications; no biomedical or science-specific schema follows from triage.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier scientific-agent benchmark), B (expertise/workflow-to-evaluation chain), and D (cross-family comparative design).
- **Evidence/artifact sought:** immutable-v1 and pinned-release deep review reconstructing task provenance/assembly, environment and artifact contracts, stepwise verification, configurations, result denominators, failure labels, and released coverage.
- **Uncertainty clarified:** whether SciAgentArena supports bounded executable scientific-workflow claims or stronger claims about real research, novelty, self-directed exploration, reliability, and autonomy.
- **Mode/balance:** one low-priority review task restores a minimal research backlog behind the pending empirical build and human decision; no broad search or parallel task bundle was added.
- **Duplication/scope:** complements AstaBench/AARRI/laboratory-workflow work; five life-science domains are a comparative pilot family, not a commitment to science or biomedicine as the benchmark scope.
- **Useful completion:** separate source realism, task validity, step-check behavior, endpoint/artifact quality, expert acceptance, novelty, autonomy, reliability, and downstream impact; preserve strict claim ceilings.

Added `review-sciagentarena-scientific-work-validity` (priority 21). No second task was added.

## Operational note

The required initial `git pull --ff-only` could not authenticate to the HTTPS GitHub remote (`could not read Username`). Local `main` was already 13 commits ahead of the recorded `origin/main`; the run proceeded from local state. The pre-existing untracked `data/papers/source/` tree was not modified.

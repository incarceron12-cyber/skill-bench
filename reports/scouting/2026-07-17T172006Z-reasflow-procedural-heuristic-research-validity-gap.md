# Scouting note — ReasFlow procedural-heuristic research validity gap

- **Timestamp:** 2026-07-17T17:20:06Z
- **Evidence status:** arXiv API metadata/abstract, immutable endpoint checks, exact local duplicate search, paper-linked URL verification, GitHub API metadata/tree triage for one similarly named installer repository, and targeted web discovery only. The paper body, appendices, five generated papers, expert inputs, procedural-heuristic store, retrieval records, agent traces, verification loops, review rubric, judge outputs, human inspections, costs, platform, and implementation were **not** deeply read, executed, or audited during scouting.

## Substantive candidate — triage only

**ReasFlow: Assisting Reasoning-Centric Scientific Discovery in Applied Mathematics via a Knowledge-Based Multi-Agent System** — Yutong He, Daibo Li, Guohong Li, Jiahe Geng, Zhengyang Huang, Can Ren, Zekun Zhang, Yifan Liu, Shuchen Zhu, Hengrui Zhang, Boao Kong, Ming Sun, Shu Li, Chenyi Li, Jiang Hu, Kun Yuan, Zaiwen Wen, and Pingwen Zhang; arXiv:2607.14178v1.

- Immutable record/PDF: https://arxiv.org/abs/2607.14178v1 · https://arxiv.org/pdf/2607.14178v1
- Paper-linked repository URL: https://github.com/ReasLab/ReasFlow.git (returned HTTP 404 during scouting)
- Official product/docs surfaces identified by targeted search: https://docs.reaslab.io/guides/overview.html · https://docs.reaslab.io/guides/paper-generation.html · https://docs.reaslab.io/showcase/reasflow.html
- The arXiv API identifies a `cs.MA`/`cs.AI` v1 submitted 15 July 2026. Its summary contains no withdrawal or retraction notice. The immutable record and PDF returned HTTP 200; the PDF response reported `application/pdf` and 11,845,866 bytes. The arXiv HTML endpoint returned HTTP 404, so it supplied no release inventory.
- The abstract describes a human-PI/agent-graduate-student research arrangement spanning literature synthesis, algorithm design, theorem proving, experiments, and manuscript production. It claims an internal logical-verification loop plus retrieval and self-improvement that surfaces declarative knowledge and overlooked procedural heuristics, five complete generated research papers, and higher curated-LLM-rubric scores than open-access baselines. These are author-stated abstract claims awaiting full-paper and artifact audit.
- The exact GitHub organization/repository linked from arXiv was unavailable at acquisition time. A similarly named public repository, `sillyDaibo/reasflow-release`, was created before submission but its inspected commit `8c2f3cf0d9826a183ff3589ff2997ef544ea50ff` contains only a README and two installer scripts; no identity with the paper implementation was established. Repository presence is not implementation, result, or reproducibility evidence.
- Exact searches for the title, arXiv ID, and `ReasFlow` found no prior local review, queue task, or scouting note.

## Why this is a narrow, useful gap

The corpus already covers scientific-work suites, research-judgment lifecycles, paper replication, procedural memory transfer, context evolution, generated rubrics, proof/checker projection, and human oversight. It does not directly audit the proposed end-to-end **expert-intuition/procedural-heuristic-to-research-artifact chain**:

`PI objective and authority → declarative sources and heuristic claims → elicitation/capture or model inference → provenance and valid scope → retrieval opportunity → agent visibility and adoption → derivation/proof/experiment state → internal verification and repair → paper artifact → curated rubric/judge view → independent expert inspection → corrected or accepted contribution → recipient use and scientific consequence`.

The distinction between sourced heuristics, expert-contributed heuristics, model-generated conjectures, and lessons selected from prior outputs is central. A retrieved heuristic is not tacit expertise unless its authority, scope, transformation lineage, adoption, and downstream effect are observed. Internal verification can identify selected inconsistencies without establishing theorem correctness, experimental validity, novelty, or independent reproduction. Five generated papers selected or developed under one system and graded by a curated model rubric license at most a configured-package comparison unless paper selection, baseline resources, criterion authority, evidence views, judge calibration, human review, invalid outputs, and dependence are explicit. Product availability and polished manuscripts do not establish reduced expert burden or scientific value.

Applied mathematics is a bounded stress case for reusable expertise-transfer, long-horizon artifact, and scalable-evaluation machinery—not a proposal to narrow `skill-bench` to theorem proving or autonomous science.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier realistic research-agent systems), B (expertise and procedural-heuristic transfer into consequential work), C (trace/artifact/verification/evaluator machinery), and E (clear boundaries among assistance, correctness, novelty, and scientific value).
- **Concrete evidence:** immutable-v1 full-paper review plus timing-aware audit of the paper-linked repository status, official docs/platform surfaces, any archived implementation/result package, five generated papers, evaluation records, and expert-review evidence.
- **Uncertainty clarified:** whether ReasFlow preserves the provenance, authority, scope, retrieval, adoption, and consequence of procedural heuristics; what its verification and five-paper evaluation actually observe; and which expert-burden, research-quality, transfer, or scientific-value claims remain unsupported.
- **Mode:** narrow expansion. The ready queue contains only one human prerequisite while three builds are fail-closed blocked; one review task restores a minimal research backlog without repeating broad benchmark discovery.
- **Duplication/scope check:** adjacent work covers individual scientific-work, memory, verification, rubric, and oversight links, but not this explicit composition or its human-PI division of labor. No mathematics-specific schema is proposed.
- **Useful completion:** section/page/path-grounded reconstruction of the system and evaluation; typed heuristic-source and lifecycle audit; exact task/paper/baseline/judge/expert denominators; release-conformance status; and nonduplicate retain/repair/test implications while keeping configured-package quality, theorem correctness, experiment validity, novelty, expert-time reduction, transfer, scientific impact, professional validity, production fitness, and readiness separate.

Added one task: `review-reasflow-procedural-heuristic-research-validity` (review, priority 63). No other candidate was queued. EvoAgentBench was not reconsidered because prior scouting explicitly rejected it as duplicative; PolyWorkBench and the generated-rubric meta-evaluation are already deeply reviewed.

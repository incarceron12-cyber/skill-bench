# Scouting note — ORAgentBench operational-decision validity gap

- **Timestamp:** 2026-07-17T12:38:48Z
- **Evidence status:** arXiv API metadata/abstract and official GitHub README/API tree triage only. The complete paper, 107 task packages, hidden validators, reference solutions, skills, experiment outputs, and reported result rows were **not** deeply read or audited during scouting.

## Substantive candidate — triage only

**ORAgentBench: Can LLM Agents Solve Challenging Operations Research Tasks End to End?** — Jiajun Li, Mingshu Cai, Yixuan Li, Yu Ding, Ran Hou, Guanyu Nie, Xiongwei Han, and Wanyuan Wang.

- Immutable arXiv record/PDF: https://arxiv.org/abs/2606.19787v1 · https://arxiv.org/pdf/2606.19787v1
- Official repository: https://github.com/ORAgentBench/ORAgentBench at inspected commit `c9eb952435a4352f33daa2a35efe0f8c76d31b28`
- Both arXiv endpoints returned HTTP 200. The arXiv API identifies a 31-page `cs.AI` v1 submitted 18 June 2026.
- The public GitHub repository returned HTTP 200 via its API, is unarchived and MIT-licensed, and has an untruncated 8,421-object tree. The tree exposes 107 Harbor task packages plus source mirrors, task-specific hidden tests, reference solutions, public operational files, 87 skill objects, experiment configs, metrics, scripts, and container definitions. The README declares benchmark data/documentation CC BY 4.0.
- The abstract and official README describe 107 human-reviewed tasks spanning planning, routing, scheduling, packing, network design, inventory, allocation, and dynamic replanning. Each isolated task combines a natural-language brief, multiple operational files, configuration artifacts, executable solver work, and a required decision artifact. Evaluation separates schema validity, hard-constraint feasibility, normalized objective quality, and a pass gate requiring feasibility plus quality above `0.4`; eight tasks introduce staged events.
- The abstract reports fourteen configured agent/model packages, a best overall pass rate of 35.51%, a best hard-task rate of 20.59%, and a procedural-skill intervention that raises hard-task feasibility without reliably raising objective quality or pass rate. These are author-reported abstract claims awaiting full-paper and release audit.

## Why this is a narrow, useful gap

The corpus already covers optimization R&D consistency through Opti-Agent-Bench, executable professional artifacts, hidden validators, procedural skills, and objective/criterion validity. ORAgentBench appears to join these into a distinct **operational decision package**:

`source brief/data/rules → modeling interpretation → executable formulation/solver → feasible decision artifact → normalized objective value → thresholded acceptance → organizational adoption → operational consequence`.

The release may provide unusually inspectable source-to-artifact closure and a useful separation between feasible and competitive decisions. But a feasible artifact that exceeds one normalized threshold is not automatically useful, robust, authorized, adopted, or beneficial. Deep review should test source/task sampling, human-review authority, objective provenance, normalization and threshold rationale, alternative legitimate decisions, hidden-validator completeness, reference-solver coupling, task/solution leakage, staged-state semantics, retry and invalid-run handling, skill-treatment parity, result reproducibility, and release timing. In particular, a skill package can improve the exact feasibility predicates it teaches while leaving decision quality unchanged; that is evidence about one configured intervention, not general expertise transfer.

Operations research is a bounded case for reusable multi-artifact decision methodology, not a proposal to narrow `skill-bench` to optimization.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier realistic-agent benchmarks), B (expertise-to-evaluation and consequence boundaries), C (executable artifacts, hidden validators, skill interventions, and traces), and E (clarify what objective-scored decisions can claim).
- **Concrete evidence:** immutable full-paper acquisition plus a timing-bounded audit of the pinned 8,421-object release, including task construction/provenance, representative public/private packages, validators, reference solvers, objective formulas, skills, configs, and available run evidence.
- **Uncertainty clarified:** whether end-to-end executable closure supports only configured task conformance or stronger operational-decision claims, and whether feasibility, objective quality, artifact integrity, decision usefulness, and consequence are validly separated.
- **Mode:** narrow expansion. The ready queue had one build task and one human prerequisite but no research/review task; this priority-63 review does not displace the higher-priority build.
- **Duplication/scope check:** Opti-Agent-Bench tests cross-module optimization-R&D consistency, while this candidate appears to add operational source packets, concrete decision artifacts, hard feasibility gates, normalized quality, staged replanning, and a skill intervention in one public suite. No OR-specific schema or pilot is proposed.
- **Useful completion:** a full-paper, release-audited review with exact provenance, reproducibility limits, retain/repair/test implications, and explicit ceilings against sampled professional practice, economic value, skill causality, reliability, safety, production fitness, and readiness.

Added one task: `review-oragentbench-end-to-end-decision-validity` (review, priority 63). No other candidate was queued; Long-Horizon-Terminal-Bench had already been explicitly deferred in prior scouting because its dense-grading contribution overlaps stronger existing coverage.

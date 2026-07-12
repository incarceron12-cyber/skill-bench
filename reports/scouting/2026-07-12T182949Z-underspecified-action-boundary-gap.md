# Scouting note — underspecified action-boundary validity gap

**Timestamp:** 2026-07-12T18:29:49Z  
**Scope:** Narrow expansion against charter objectives A/B/C. Repository inspection found 149 completed tasks, one pending evaluator-observation build, one blocked real-elicitation task, and no pending source/research/review work. Existing reviews cover hidden requirements, unprompted problem recognition, safe refusal/escalation, prompt injection, and execution isolation, but no benchmark that experimentally varies benign instruction ambiguity while holding the environment and intended safe action fixed.

## Substantive finding (triage only)

**Coding Agents Are Guessing: Measuring Action-Boundary Violations in Underspecified DevOps Instructions (UnderSpecBench)**

- Immutable arXiv target: https://arxiv.org/abs/2607.02294v1
- PDF: https://arxiv.org/pdf/2607.02294v1
- arXiv API verified v1, published 2026-07-02.
- The abstract reports 69 DevOps task families grounded in documented incidents, CVEs, or tool behavior, with 2,208 prompt variants over intent clarity, target certainty, and blast radius. It describes a fixed environment and ground-truth safe action within each task while varying instructions, then uses deterministic side-effect oracles to distinguish Safe Success, Wrong Target, OverScope, clarification, refusal, and deferment across five agent/model configurations.
- Repository-wide duplicate search found no title, `UnderSpecBench`, or arXiv-ID match.
- No paper-linked official repository was visible on the arXiv abstract page or found in targeted search during triage. A full review must verify whether tasks, generators, environments, traces, or graders are released rather than infer inspectability from the paper.
- This is **arXiv metadata/abstract and release-location triage only**. The PDF, appendices, incident/CVE grounding, family construction, prompt transformations, safe-action labels, sandbox, oracle coverage, run records, statistics, and failure adjudication were not read or inspected. The reported percentages are abstract claims, not independently verified results. No claim is made that the benchmark establishes production safety or generalizes beyond selected DevOps actions.

## Benchmark implication to test

UnderSpecBench may provide a controlled bridge between `skill-bench`'s hidden-requirement and counterfactual-action machinery: ambiguity should change whether an agent clarifies, narrows, refuses, defers, or acts—not silently convert completion into permission. A full audit should test whether intent, target, and scope perturbations preserve task difficulty and safe-action identity; whether deterministic side-effect observers cover collateral consequences and legitimate alternative paths; and whether clarification, refusal, and deferment are semantically distinguished rather than lexically inferred. The reusable target is an action-authority contract spanning disclosed basis, uncertainty locus, authority boundary, clarification opportunity, attempted action, realized target/scope deltas, benign utility, and consequence—not a DevOps-specific schema.

## Charter decision filter and queue action

- **Objectives advanced:** A (realistic agent/safety evaluation), B (hidden requirements and decision thresholds), and C (action, state, trace, and diagnostic contracts).
- **Evidence/artifact sought:** immutable full-paper review and any verifiable release audit, with page/file locators and a prompt-perturbation → authority decision → state-consequence crosswalk.
- **Uncertainty clarified:** whether controlled underspecification can identify unsafe guessing independently of task difficulty, harness policy, lexical response form, and incomplete side-effect observation.
- **Mode/balance:** narrow expansion; the only ready queue item is building/validation.
- **Duplication/scope:** not a duplicate of ClawSafety (untrusted injected instructions), AARRI (research stop/refuse/escalate), KWBench (latent problem recognition), or Consulting Cognitive Traps (expert/novice procedural paths). DevOps is a bounded action-consequence test bed, not a domain commitment.
- **Useful completion:** reconstruct source grounding, transformation invariance, configured-system identity, permission policy, oracle semantics/coverage, alternative paths, uncertainty and clustering, invalid-run policy, release fidelity, and claim ceilings; compare with existing reviews and map only nonduplicate implications into current authority, action-safety, trace, metric, and validity machinery.

Added `review-underspecbench-action-boundary-validity` (priority 52). No second task was added.

# Paper Review: Agent Psychometrics — Task-Level Performance Prediction in Agentic Coding Benchmarks

- **Paper:** https://arxiv.org/abs/2604.00594v1
- **Authors:** Chris Ge, Daria Kryvosheieva, Daniel Fried, Uzay Girit, Kaivalya Hariharan
- **Date read:** 2026-07-09
- **Venue / source:** ICLR 2026 Workshop on Agents in the Wild / arXiv
- **Tags:** agent-eval, psychometrics, item-response-theory, task-difficulty, scaffold-effects, benchmark-design
- **Local text:** `data/papers/text/2604.00594v1-agent-psychometrics-task-level-performance-predict.txt`

## One-sentence contribution

The paper extends Item Response Theory for agentic coding benchmarks by predicting task difficulty from rich task artifacts and decomposing agent ability into additive LLM and scaffold components, enabling task-level success prediction for new tasks, new LLM-scaffold combinations, and held-out benchmarks.

## Why this matters for skill-bench

The paper gives `skill-bench` a concrete way to think about benchmark difficulty before expensive evaluations. In knowledge-work tasks, the prompt alone will rarely explain difficulty. Difficulty may live in the source corpus, hidden requirements, contradictory evidence, spreadsheet/test artifacts, rubric strictness, and the expected final deliverable. This paper’s core transfer is: **difficulty is a property of the whole task package, not the user instruction.**

For Samuel’s benchmark, that means every scenario should preserve and expose enough structured metadata to later predict why it is hard:

- the task brief;
- source files and their relationships;
- expected artifact(s);
- hidden constraints and expert caveats;
- rubric checks;
- possible solution outline;
- tool/environment requirements;
- scaffold assumptions.

The LLM/scaffold decomposition also matters strategically. If `skill-bench` evaluates agents rather than raw models, scores should not be interpreted as “model capability” unless the harness is controlled. The paper provides a statistical framing for separating model contribution from scaffold contribution when enough cross-harness data exists.

## Methodology

- **Task construction:** The paper uses existing agentic coding benchmarks rather than creating a new benchmark. The key benchmarks discussed in the experiments include SWE-bench Verified, SWE-bench Pro, GSO, and Terminal-Bench 2.0.
- **Environment / tools:** The underlying tasks involve coding agents interacting with repositories, tests, terminal environments, and benchmark harnesses. The authors extract features from agentic artifacts such as issue/problem statements, repository state, test patches, solution patches, and evaluation harness context.
- **Evaluation protocol:** The authors hold out different response sets to test different generalization settings: new tasks within a benchmark, new responses, new LLM-scaffold combinations where each component has been seen separately, and entire held-out benchmarks.
- **Scoring:** The central metric is AUC-ROC for predicting whether an agent succeeds on a particular task. Standard IRT serves as an oracle-like upper bound when trained with the held-out response data; simpler empirical pass-rate baselines test whether the richer model adds value.
- **Modeling approach:** First, fit IRT ability and difficulty parameters from observed responses. Then train ridge regressions from task feature vectors to frozen IRT difficulty values. For agents, represent success probability as `sigmoid(LLM ability + scaffold ability - task difficulty)`.
- **Feature extraction:** The paper compares embedding-based task vectors, LLM-as-judge rubric features, and combined features. It also runs ablations where feature sources are progressively added: problem statement, repository state, tests, and solution.
- **Baselines:** Naive empirical success-rate baselines and oracle IRT models trained on all relevant response data.
- **Human comparison:** None in the main methodology; the “psychometrics” analogy is statistical rather than a human study.
- **Cost/time accounting:** The motivation is cost reduction for long-horizon agent evaluation. The paper cites high evaluation costs such as a $22,000 SWE-bench Verified run for Darwin-Gödel Machine and demonstrates adaptive task selection outperforming random selection under low task budgets.

## Unique insight

The most reusable insight is that **agentic task artifacts predict task difficulty beyond the problem statement**. In the held-out-task setting, task-feature predictors beat the empirical baseline across all four benchmarks. The feature ablation is especially important for `skill-bench`: adding tests and solution information improves difficulty prediction, and problem-statement-only difficulty is incomplete.

The second major insight is that, in the studied coding data, agent ability can be usefully approximated as an additive combination of **LLM ability + scaffold ability**. This matters because many leaderboards quietly compare bundled systems. For a benchmark about skills, this decomposition suggests a path toward asking: did the agent succeed because of the base model, the skill/package, the scaffold, or task-specific luck?

## Transferable design patterns

- **Difficulty metadata schema:** Store features that can explain difficulty: source count, evidence dispersion, contradiction count, number of tools required, artifact type, hidden requirements, rubric strictness, verification coverage, and solution-path multiplicity.
- **Task package feature extraction:** Treat each benchmark task as a bundle of artifacts. For knowledge work, extract features from the brief, source documents, spreadsheet/database inputs, expected deliverable, rubric, and reference solution notes.
- **LLM-as-judge feature audits:** Use LLMs not only to grade outputs but to label task properties such as verification difficulty, domain specificity, ambiguity, context-management burden, and artifact-convention burden.
- **Scaffold-aware leaderboards:** Record the base model, scaffold, skill package, tool set, retry policy, memory policy, and prompting strategy so later analysis can separate agent components.
- **Adaptive evaluation:** Use predicted task/check difficulty to choose a small informative subset for a new agent, especially early in development when full runs are too expensive.
- **Counterfactual task editing:** Because the authors note that predictive models do not prove causal difficulty, `skill-bench` can deliberately vary one element at a time—e.g., add a hidden constraint, remove a contradictory source, weaken a rubric check—to learn what actually changes difficulty.

## Failure modes / limitations

- The work is in coding benchmarks; knowledge-work artifacts such as memos, decks, and spreadsheets may require different feature sources and less binary scoring.
- The LLM+scaffold additive decomposition only predicts new combinations when both the LLM and scaffold have been observed separately. It cannot handle fully novel models or fully novel scaffolds without additional features.
- As agents become more tightly co-designed with their scaffolds, the independence assumption may weaken; interactions between model and scaffold could matter more than additive terms.
- The method predicts success but does not prove which task properties causally create difficulty. The authors explicitly note the need for counterfactual task construction.
- Rich feature extraction depends on access to task internals such as tests, solutions, or repository state. For public benchmark releases, this creates leakage concerns if not separated into private calibration metadata.

## Questions to carry forward

- What are the `skill-bench` analogues of coding “tests” and “solution patches”? Possible answer: rubric checks, reference artifacts, expert review notes, and hidden verifier specifications.
- Can Samuel build a private calibration layer that stores reference-solution and rubric metadata without leaking it into the public task prompt?
- Should every `skill-bench` scenario be designed with at least one editable difficulty knob so the project can create counterfactual task variants?
- When comparing agents using skills, should the leaderboard report model-only, scaffold-only, skill-only, and full-agent configurations?

## Action items for repository

- [x] Update SOTA map with Agent Psychometrics under efficient / psychometric benchmark operation.
- [x] Update compounding-system notes to include task-difficulty metadata and scaffold-aware evaluation.
- [ ] Draft a `templates/task-metadata.md` file with difficulty features for knowledge-work scenarios.
- [ ] Add `model`, `scaffold`, `skills_enabled`, `tool_policy`, and `run_timestamp` fields to any future run-result schema.
- [ ] Create a design note for private calibration metadata: reference solution, verifier/rubric internals, task features, and leakage controls.

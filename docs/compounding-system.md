# Compounding System Design

## Objective

Create a system that improves Samuel's understanding and the project repository every day.

The system should not merely send paper summaries. It should:

1. discover relevant papers and benchmark releases,
2. download/read source material,
3. synthesize unique insights,
4. update the repository taxonomy and research agenda,
5. propose benchmark-design moves,
6. commit/push changes to GitHub,
7. send concise Telegram updates that develop Samuel's thinking.

## Daily cadence

### Morning — discovery and triage

Purpose: identify what is new and worth attention.

Output:
- 5–10 candidate papers/releases;
- why each might matter;
- top 2–3 to read deeply.

### Midday — deep paper review

Purpose: read actual downloaded papers and write structured reviews.

Output:
- 1–3 comprehensive paper reviews;
- methodology breakdown;
- unique insight;
- transfer into `skill-bench`.

### Evening — synthesis and benchmark design

Purpose: convert the day's learning into project direction.

Output:
- updated SOTA map;
- new benchmark primitives;
- scenario ideas;
- questions for Samuel;
- repo commit/push summary.

## Compounding artifacts

| Artifact | Path | Why it compounds |
|---|---|---|
| Paper index | `data/papers/index.json` | Prevents rediscovery; tracks status |
| Paper reviews | `papers/<topic>/` | Converts papers into reusable insights |
| SOTA map | `docs/state-of-the-art-map.md` | Accumulates landscape understanding |
| Incentive design | `docs/incentive-design.md` | Evolves strategy for expert contributions |
| Benchmark templates | `templates/` | Converts research insights into buildable specs |
| Task metadata template | `templates/task-metadata.md` | Captures difficulty features, domain primitives, root-cause tags, leakage controls, and response-matrix fields before pilots are built |
| Daily reports | `reports/daily/` | Preserves thinking over time |
| Git commits | GitHub history | Makes progress inspectable and reversible |

## Review standard

Every deep review should answer:

1. What did the authors actually build or measure?
2. What is the unique insight?
3. What methodology matters?
4. What is reusable for benchmark design?
5. What does this reveal about domain knowledge transfer?
6. What should be changed in the repo?
7. What question should Samuel think about next?

## Evaluation layers to preserve

Recent benchmark papers suggest keeping three evaluation layers separate:

1. **Artifact quality:** final deliverables such as spreadsheets, decks, memos, notebooks, and tickets should be graded for correctness, maintainability, and professional presentation.
2. **Workflow checkpoints:** long-horizon tasks should expose partial-credit state checks so agents can be compared even when they fail before full completion.
3. **Trace diagnosis:** execution logs should retain enough structure to localize failures to upstream causes such as planning, evidence retrieval, state tracking, tool use, or artifact construction.
4. **Psychometric calibration:** per-task and per-rubric-check histories should estimate difficulty/discrimination so routine evaluation can use an informative mid-difficulty panel rather than always running the full task bank.

This separation lets the project compound in two ways: benchmark scores become more informative for users, and failed runs become training data for improving agents, skills, and task design.

## Benchmark operation principles

Two reviewed papers sharpen the operating model:

- **Efficient Benchmarking of AI Agents:** rank fidelity can remain high even when absolute score prediction degrades under scaffold or temporal shift. For routine comparisons, the project should distinguish rank-preserving reduced panels from full-suite absolute capability claims.
- **Agent Psychometrics:** task difficulty in agentic benchmarks is explained by the whole task package, not only the user-facing prompt. Difficulty metadata should include source corpus structure, hidden constraints, verifier/rubric properties, reference-solution notes, tool requirements, and scaffold/model metadata.

Implications for `skill-bench`:

1. Keep a **full task bank** for coverage and periodic calibration.
2. Maintain a **routine evaluation panel** of tasks or rubric checks with historical pass rates in the discriminative middle, initially around 30–70%.
3. Store a **response matrix** with one row per agent-task/check attempt: task id, check id, model, scaffold, skills enabled, tool policy, outcome, cost, timestamp, and benchmark version.
4. Report **rank fidelity** separately from absolute scores; use occasional full runs to validate that reduced panels still preserve ordering.
5. Treat scaffold and skill-package choices as measurable confounds, not incidental metadata.
6. Preserve private calibration metadata separately from public prompts to avoid leaking reference solutions or verifier logic.

## How domain expertise becomes a benchmark

A domain expert should not be asked to “make a benchmark.” Instead, extract these primitives:

- Hidden requirement: what a novice would miss.
- Trusted evidence: which source matters most.
- Contradiction: where real sources disagree.
- Judgment threshold: what changes the decision.
- Artifact convention: what a professional deliverable must look like.
- Failure signature: what a polished but wrong answer looks like.
- Review rubric: what criteria separate acceptable from excellent.
- Difficulty feature: what makes this task/check easy, mid-range, or hard for current agents.
- Scaffold sensitivity: what depends on browser control, file editing, memory, retrieval, or other harness design choices.

## Strategic idea

The project can be framed as an **expertise-to-evaluation engine**:

> We turn expert tacit knowledge into realistic AI-agent benchmark tasks.

That framing is broader and more defensible than “an AA-Briefcase clone.”

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

This separation lets the project compound in two ways: benchmark scores become more informative for users, and failed runs become training data for improving agents, skills, and task design.

## How domain expertise becomes a benchmark

A domain expert should not be asked to “make a benchmark.” Instead, extract these primitives:

- Hidden requirement: what a novice would miss.
- Trusted evidence: which source matters most.
- Contradiction: where real sources disagree.
- Judgment threshold: what changes the decision.
- Artifact convention: what a professional deliverable must look like.
- Failure signature: what a polished but wrong answer looks like.
- Review rubric: what criteria separate acceptable from excellent.

## Strategic idea

The project can be framed as an **expertise-to-evaluation engine**:

> We turn expert tacit knowledge into realistic AI-agent benchmark tasks.

That framing is broader and more defensible than “an AA-Briefcase clone.”

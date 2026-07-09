# Evening Synthesis — 2026-07-09

## What changed today

- The repo moved from a scaffolded research loop toward a sharper benchmark architecture: **artifact quality + workflow checkpoints + trace diagnosis + psychometric calibration**.
- Morning triage identified the most relevant benchmark families for near-term design: SaaS-Bench for state/checkpoint realism, MBABench for professional spreadsheet artifact grading, OdysseyBench for long-horizon office workflows, STRACE for causal trace slicing, and Efficient Benchmarking / Agent Psychometrics for calibrated low-cost evaluation.
- Three deeper paper reviews were added under `papers/agent-benchmarks/`:
  - `2026-07-09-efficient-benchmarking-ai-agents.md`
  - `2026-07-09-agent-psychometrics.md`
  - `2026-07-09-strace.md`
- Durable docs were already strengthened earlier today: `docs/state-of-the-art-map.md` and `docs/compounding-system.md` now include psychometric operation, scaffold-aware evaluation, response matrices, and root-cause diagnosis.
- This evening adds a reusable task metadata template so new scenarios can be authored with calibration, leakage, rubric compression, and causal failure analysis in mind from the start.

## Durable insights

1. **Difficulty lives in the whole task package, not the prompt.**  
   For knowledge work, the hard part may be hidden in source dispersion, artifact conventions, contradictory evidence, evaluator strictness, tool requirements, or the reference solution. A benchmark that only versions prompts will be unable to explain why agents fail.

2. **Professional artifacts need multiple scoring layers.**  
   MBABench’s Accuracy / Formula / Format split generalizes: correctness is necessary but not sufficient. Skill-bench should evaluate final answer correctness, maintainable internal structure, and professional usefulness separately. A spreadsheet can have the right number and still be a bad work product.

3. **The benchmark should produce diagnosis, not just a leaderboard.**  
   STRACE points to a higher standard: each failed run should identify where the mistake originated. “Bad memo” is not enough; we need tags like evidence reconciliation failure, calculation failure, artifact convention failure, tool-use failure, or stakeholder judgment failure.

4. **Reduced evaluations should be rank-aware and calibration-aware.**  
   Efficient Benchmarking suggests a practical operating model: run the full bank periodically, then use mid-difficulty tasks or rubric checks for routine comparisons. But this only works if skill-bench stores response matrices from day one.

5. **Scaffolds and skills are part of the measured system.**  
   Agent Psychometrics’ LLM + scaffold decomposition is strategically important. If Samuel wants to evaluate “agents doing work,” then model, harness, skill package, tool policy, memory, and retry policy must be recorded as first-class metadata rather than treated as incidental implementation detail.

## Benchmark design implications

- **Start with one deep artifact-centered pilot, not a full SaaS environment.** SaaS-Bench is compelling but infrastructure-heavy. The near-term wedge should borrow checkpoint scoring and professional realism without taking on 23 deployable apps.
- **Use rubric checks as the unit of future compression.** Whole-task pass/fail will be too blunt. If a board memo scenario has 35 checks, some checks can become mid-difficulty ranking probes while others remain diagnostic or private calibration checks.
- **Author scenarios with explicit difficulty knobs.** Each task should include editable variables: number of source files, contradiction count, hidden requirements, artifact type, tool stack, and rubric strictness. This enables counterfactual task variants later.
- **Separate public trust material from private calibration material.** Public scenario docs can show the task framing and methodology. Private packs should hold reference artifacts, verifier internals, hidden traps, and task-feature labels.
- **Every pilot needs a failure-postmortem schema.** A run that fails should still be valuable if it teaches which knowledge-work primitive was not handled.

## Incentive / community ideas

- **Expert contribution should be primitive-based.** Do not ask experts to “write benchmark tasks.” Ask them for hidden requirements, trusted sources, contradictions, polished-but-wrong failure examples, and professional artifact conventions.
- **Run a failure-prediction game.** Before releasing model results, ask domain experts to predict which hidden caveat or artifact convention agents will miss. Score experts by predictive accuracy. This turns tacit knowledge into both engagement and validation.
- **Create scenario jams around one artifact.** A finance/operator/product expert plus a benchmark builder can create one mini source pack, a task brief, 10 rubric checks, and 3 known traps in a day.
- **Reward red-teamers who improve task validity.** Publicly credit people who find impossible tasks, leaked rubric hints, unrealistic evidence, or ambiguous instructions. This may be more valuable than rewarding task volume.

## What Samuel should think about next

The central strategic choice is whether `skill-bench` is primarily:

1. a **leaderboard** for comparing agents,
2. a **diagnostic instrument** for discovering where agents fail at knowledge work,
3. an **expertise-to-evaluation engine** for turning tacit professional judgment into reusable tasks, or
4. a **skill/scaffold improvement loop** where benchmark failures become better agent procedures.

The strongest position is probably not to choose only one, but to sequence them: first build the expertise-to-evaluation engine, then use it to produce diagnostic pilots, then publish leaderboards only where the diagnostic basis is strong.

## Next build actions

1. Draft the first scenario spec for **Startup Operating Review** using the new task metadata template.
2. Add a concrete rubric schema with fields for objective checks, judge checks, root-cause tags, and private/public visibility.
3. Create a response-matrix schema before the first serious benchmark run: task id, check id, model, scaffold, skills, tool policy, outcome, cost, timestamp, benchmark version.
4. Convert one pilot scenario into a minimal synthetic source pack: 5–10 files, 2 contradictions, 2 hidden requirements, 1 spreadsheet deliverable, 1 memo deliverable.
5. Define a “public pilot / private expansion pack” release plan: what earns trust publicly vs what must stay private to preserve evaluation value.

## Conceptual distinction / thinking exercise

**Distinction:** A *task* asks for work; a *benchmark instrument* explains what kind of competence the work reveals.

Thinking exercise: take one proposed pilot scenario and write two lists:

- **Observable outputs:** what files the agent must produce.
- **Latent competencies:** what hidden abilities those files are supposed to reveal: evidence triage, contradiction handling, numerical modeling, stakeholder judgment, artifact maintainability, presentation taste, tool discipline.

Then ask: if an agent fails, could the current rubric tell which latent competency failed? If not, the benchmark is still a task collection, not yet an instrument.

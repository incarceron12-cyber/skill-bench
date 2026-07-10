# Production Agent Systems: Patterns for skill-bench

This track studies how production agent systems create reliable improvement loops at scale. It is not a generic agent survey: every source must yield a design implication for researching, building, or evaluating knowledge-work benchmarks.

## Initial primary-source map

| Source | Production pattern | Transfer to skill-bench |
|---|---|---|
| [Anthropic: Building Effective AI Agents](https://www.anthropic.com/engineering/building-effective-agents) | Prefer simple composable workflows; distinguish workflows from agents; preserve debuggability | Use deterministic pipeline stages around flexible research/build agents; avoid one opaque mega-agent |
| [Anthropic: Effective Context Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | Curate the full context state and refine it cyclically | Queue workers receive role-specific context; consolidators compress accumulated knowledge into durable maps |
| [Anthropic: Writing Effective Tools for AI Agents](https://www.anthropic.com/engineering/writing-tools-for-agents) | Evaluate tools with realistic tasks; return token-efficient meaningful context | Treat discovery/extraction/queue/validation scripts as agent-facing tools with explicit output contracts and evals |
| [Anthropic: Demystifying Evals for AI Agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) | Model task/trial/grader/transcript separately; evaluate stateful multi-turn behavior | Benchmark schema should preserve complete trials and multiple graders, not only final artifact scores |
| [AWS: Evaluating AI agents at Amazon](https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-real-world-lessons-from-building-agentic-systems-at-amazon/) | Production eval must inspect tool selection, memory retrieval, reasoning, and end-to-end success | Build a diagnostic benchmark that attributes failure to source retrieval, reasoning, tools, context, or artifact construction |
| [Karpathy AutoResearch](https://github.com/karpathy/autoresearch) | Fixed-budget autonomous experiments; keep improvements and discard regressions; Markdown is research-org code | Treat `.hermes.md`, cron prompts, queue policy, and templates as evolvable research-organization code measured by output quality |
| [EvoAgentX](https://github.com/EvoAgentX/EvoAgentX) | Modular goal-driven evolution with iterative feedback | Evolve prompts/tools/workflows only through bounded, logged experiments |
| [Hermes Agent](https://github.com/NousResearch/hermes-agent) | Skills, memory, cron, project context, and durable workdirs support compounding systems | Use repo context + cron + GitHub as the persistent organization layer; use skills only for reusable procedures |

## Production principles

### 1. Separate exploration from exploitation

Scouts maximize coverage. Reviewers maximize understanding. Builders maximize artifact production. Consolidators protect coherence. Mixing all four goals in every run produces shallow research and noisy commits.

### 2. Make work claimable and observable

A queue entry should state why the work matters, what evidence is required, what artifact completes it, who claimed it, and what result was produced.

### 3. Preserve complete evidence chains

For benchmark research:

```text
source → extracted text → review → design implication → implementation task → verified artifact
```

For benchmark trials:

```text
task → environment → agent trace → produced artifact/state → grader checks → root-cause diagnosis
```

### 4. Optimize for verified learning, not run count

A 15-minute heartbeat is a coordination frequency, not a requirement to produce a commit every 15 minutes. Empty/no-op runs are preferable to duplicated or low-quality changes.

### 5. Use layered memory

- Working context: one claimed task and its primary sources.
- Queue: immediate cross-run coordination.
- Reports/reviews: evidence-rich episodic memory.
- Core docs/schemas: consolidated semantic memory.
- Git history: reversible evolution record.
- Skills: reusable procedures only.

### 6. Keep a human governance boundary

Samuel directs objectives, approves Level 2 actions, and resolves strategic tradeoffs. Agents autonomously execute bounded Level 0/1 work and surface decisions in scheduled briefs.

## Research backlog

- Study Anthropic's detailed grader guidance and map it to artifact/rubric evaluation.
- Read Amazon's evaluation taxonomy and operational metrics beyond the introductory sections.
- Compare AutoResearch's fixed-budget fitness loop with open-ended research-quality metrics.
- Review Agentic Context Engineering (ACE) and self-evolving-agent surveys from full papers.
- Study Hermes community user stories and automation blueprints for durable workflow patterns.
- Identify production anti-patterns: runaway context, silent regressions, reward hacking, duplicated workers, and evaluation leakage.

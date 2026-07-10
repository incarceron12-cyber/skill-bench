# skill-bench

A 24/7 compounding research-and-build system for turning **domain expertise into realistic, diagnosable benchmarks of agentic knowledge work**.

`skill-bench` is both:

- a research repository that reads primary sources and consolidates their most useful ideas; and
- an implementation repository that converts those ideas into schemas, validators, task contracts, rubrics, traces, and pilot benchmarks.

The project is not trying to make a cheap clone of AA-Briefcase. Its central thesis is:

> A valuable knowledge-work benchmark should capture the hidden requirements, evidence judgments, contradictions, workflow states, artifact conventions, and failure signatures that distinguish expert work from plausible-looking output.

## Start here

If you are new to the repository, these are the most useful entry points:

| Read this | Why it matters |
|---|---|
| [`docs/benchmark-design-taxonomy.md`](docs/benchmark-design-taxonomy.md) | The canonical design map: expertise-to-task authoring, measurement layers, system identity, failure attribution, and benchmark operation |
| [`schemas/README.md`](schemas/README.md) | The executable benchmark contract and how task, trial, grader, artifact, trace, and diagnosis records fit together |
| [`schemas/EXPERTISE_TRANSFER.md`](schemas/EXPERTISE_TRANSFER.md) | The authoring contract for converting expert claims into primitives, scenarios, source packs, traps, artifacts, checks, and release gates |
| [`docs/state-of-the-art-map.md`](docs/state-of-the-art-map.md) | The external benchmark landscape and the project's current evidence map |
| [`docs/production-agent-systems.md`](docs/production-agent-systems.md) | Production-system lessons from Anthropic, Amazon, Karpathy, Hermes, and self-evolving-agent work |
| [`papers/agent-benchmarks/`](papers/agent-benchmarks/) | Full-text-based paper reviews with methodology, limitations, and concrete benchmark implications |
| [`data/work_queue.json`](data/work_queue.json) | The live, machine-readable research/build queue used by the autonomous workers |
| [`docs/self-improvement-ledger.md`](docs/self-improvement-ledger.md) | Hypotheses, process experiments, evidence, and keep/modify/revert decisions |

For the project mission and research questions, see [`docs/research-agenda.md`](docs/research-agenda.md).

## What the repository is building

The intended evidence chain is:

```text
expert/source claim
  → domain primitive
  → scenario + source pack + trap
  → task + expected professional artifact
  → checks + graders
  → versioned agent trial + trace
  → score families + causal diagnosis
  → benchmark and system improvement
```

The project explicitly separates:

1. **Authoring:** how expertise becomes a fair, executable task.
2. **Measurement:** what process, state, artifact, safety, efficiency, and diagnostic evidence can support.
3. **Operation:** how tasks, graders, tools, skills, scaffolds, and evaluation panels are versioned and calibrated.
4. **Improvement:** how failures and new research become bounded, evidence-backed changes rather than silent drift.

## How the repository now works

The repository is maintained by a queue-driven, role-separated research organization running continuously, including overnight.

### 24/7 operating loop

```text
orchestrate → scout → acquire/extract → deeply review
            → build benchmark artifacts → consolidate → repeat
```

| Worker | Cadence | Responsibility |
|---|---:|---|
| Orchestrator | Every 15 minutes | Inspect the queue and recent work, identify bottlenecks, and keep roles aligned with the benchmark mission |
| Scout | Every 15 minutes, staggered | Find high-value primary sources without duplicating the existing corpus |
| Source extractor | Every 15 minutes, staggered | Download papers/pages, extract text, and preserve provenance |
| Researcher/reviewer | Every 15 minutes, staggered | Read one primary source deeply and produce a durable review or concept note |
| Benchmark builder | Every 15 minutes, staggered | Convert research into schemas, validators, tasks, rubrics, graders, fixtures, and tests |
| Consolidator | Every two hours | Merge repeated findings, update canonical docs, reprioritize work, and reduce drift |
| Director brief | Four times daily | Send a consolidated, evidence-backed update rather than noisy per-worker messages |

A 15-minute heartbeat is a **coordination frequency**, not a requirement to manufacture a commit every 15 minutes. A no-op is better than duplicate or low-signal work.

### Shared queue

Autonomous work is coordinated through [`data/work_queue.json`](data/work_queue.json) and [`scripts/queue.py`](scripts/queue.py). Workers claim one bounded task, produce evidence and an artifact, validate the result, then complete, block, or release the task.

Useful commands:

```bash
python scripts/queue.py stats
python scripts/queue.py list --status pending --limit 20
python scripts/queue.py validate
```

### Evidence standard

- A paper is not called “read” unless its full PDF/text was actually acquired and examined.
- Abstract-only findings remain triage.
- Reviews preserve source URLs and local evidence paths.
- Research should end in a design implication, implementation task, or explicit decision—not an isolated summary.
- Process changes are logged as experiments in the self-improvement ledger.

The autonomous operating rules are defined in [`.hermes.md`](.hermes.md).

## Repository map

### Core design and synthesis

| Path | Purpose |
|---|---|
| [`docs/benchmark-design-taxonomy.md`](docs/benchmark-design-taxonomy.md) | Canonical internal benchmark-design model |
| [`docs/research-agenda.md`](docs/research-agenda.md) | Research thesis, questions, and priorities |
| [`docs/state-of-the-art-map.md`](docs/state-of-the-art-map.md) | External benchmark landscape and evidence status |
| [`docs/production-agent-systems.md`](docs/production-agent-systems.md) | Production-scale agent and evaluation patterns |
| [`docs/concepts/`](docs/concepts/) | Focused concept syntheses derived from primary sources |
| [`docs/incentive-design.md`](docs/incentive-design.md) | Low-cost expert-contribution and sponsorship ideas |
| [`docs/self-improvement-ledger.md`](docs/self-improvement-ledger.md) | Evidence-backed process evolution |

### Executable benchmark contracts

| Path | Purpose |
|---|---|
| [`schemas/benchmark-bundle.schema.json`](schemas/benchmark-bundle.schema.json) | Task, trial, grader, check, artifact, trace, recovery, and diagnosis contract |
| [`schemas/expertise-transfer.schema.json`](schemas/expertise-transfer.schema.json) | Expert claims, domain primitives, scenarios, sources, traps, artifact/check mappings, and release gates |
| [`scripts/validate_benchmark.py`](scripts/validate_benchmark.py) | JSON Schema and cross-record semantic validation for benchmark bundles |
| [`scripts/validate_expertise_transfer.py`](scripts/validate_expertise_transfer.py) | Semantic validation for expertise-transfer authoring packages |
| [`tests/`](tests/) | Fixtures and regression tests for executable contracts |
| [`templates/`](templates/) | Paper-review, task, rubric, and metadata authoring templates |

### Research corpus

| Path | Purpose |
|---|---|
| [`papers/`](papers/) | Human-readable, source-grounded paper reviews |
| [`data/papers/index.json`](data/papers/index.json) | Paper metadata, provenance, and extraction state |
| `data/papers/pdfs/` | Downloaded PDFs; intentionally not committed because of size |
| [`data/papers/text/`](data/papers/text/) | Extracted full text used for review and synthesis |
| [`data/sources/`](data/sources/) | Preserved official web sources and provenance |
| [`reports/scouting/`](reports/scouting/) | Timestamped discovery reports |
| [`reports/consolidation/`](reports/consolidation/) | Periodic synthesis and deduplication reports |
| [`reports/daily/`](reports/daily/) | Historical daily reports from the earlier cadence |

### Benchmark development

| Path | Purpose |
|---|---|
| [`benchmarks/`](benchmarks/) | Pilot scenarios and future benchmark packages |
| [`inbox/build-ideas/`](inbox/build-ideas/) | Unconsolidated implementation ideas |
| [`inbox/review-queue/`](inbox/review-queue/) | Material awaiting deep review |
| [`inbox/questions-for-samuel/`](inbox/questions-for-samuel/) | Strategic questions requiring human direction |

### Automation and quality control

| Path | Purpose |
|---|---|
| [`scripts/discover_papers.py`](scripts/discover_papers.py) | Search, download, extract, and index candidate papers |
| [`scripts/queue.py`](scripts/queue.py) | Durable queue coordination with locking and atomic writes |
| [`scripts/check_review_quality.py`](scripts/check_review_quality.py) | Review completeness and evidence checks |
| [`scripts/make_daily_digest.py`](scripts/make_daily_digest.py) | Research digest generation |
| [`.hermes.md`](.hermes.md) | Mission, evidence requirements, autonomy levels, and verification rules |

## Validate the current repository

```bash
python -m py_compile scripts/*.py
python scripts/queue.py validate
python scripts/check_review_quality.py papers --allow-empty
python scripts/validate_benchmark.py --check-paths \
  tests/fixtures/valid-benchmark-bundle.json
python scripts/validate_expertise_transfer.py \
  tests/fixtures/valid-expertise-transfer.json
python -m unittest discover -s tests -v
```

The JSON validators require `jsonschema`.

## Current design stance

`skill-bench` aims to be an **expertise-to-evaluation engine**, not merely another leaderboard.

The strongest benchmark should help answer:

- What kind of professional judgment was required?
- Which source, contradiction, threshold, or hidden requirement mattered?
- Did the agent fail in retrieval, reasoning, state tracking, tool use, artifact construction, verification, or judgment?
- Was the task, grader, environment, or agent responsible for the observed failure?
- What evidence supports the score and diagnosis?
- What should improve next: the agent system, the benchmark, or both?

## Initial inspiration

- [Artificial Analysis: AA-Briefcase](https://artificialanalysis.ai/articles/aa-briefcase)
- [AA-Briefcase evaluation](https://artificialanalysis.ai/evaluations/aa-briefcase)
- [AA-Briefcase-Lite](https://huggingface.co/datasets/ArtificialAnalysis/AA-Briefcase-Lite)
- [Stirrup](https://github.com/ArtificialAnalysis/Stirrup)

These are reference points, not specifications to clone. The project is looking for the design principles that make realistic agent evaluation credible, diagnostic, and useful under limited resources.

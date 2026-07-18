# SkillGenBench: Benchmarking Skill Generation Pipelines for LLM Agents

SkillGenBench is a benchmark for evaluating **skill generation pipelines** under a unified and controlled protocol. Given raw corpora (repositories or documents), a generator produces standardized skill artifacts (`SKILL.md`), which are then executed under fixed harnesses and assessed with unified evaluation procedures.

The benchmark covers:
- **187 tasks** across 3 source types: Code Repo (123), Code Doc (28), and Domain Knowledge Doc (36)
- **Two generation regimes**: task-conditioned (task-specific skill) and task-agnostic (reusable skill library)
- **Deterministic evaluation** via containerized execution with execution-based checks

## Pipeline Overview

```
data_source/          -->  baseline/<method>/generate_skill.py  -->  generated_skills/<method>/
(standardized input)       (your skill generator)                    (SKILL.md + meta.json)
                                                                          |
                                                                          v
                                                              scripts/run_eval.py
                                                              (Docker-based evaluation)
                                                                          |
                                                                          v
                                                                    results/
```

## Quick Start

### Prerequisites

```bash
# Build Docker evaluation images (one-time)
bash docker/build_claude_images.sh

# Pull evaluation repos (one-time, may take a while)
bash scripts/pre_repos_and_verify.sh
```

### Set API Credentials

```bash
export BASE_URL="https://api.openai.com/v1"   # OpenAI-compatible API
export API_KEY="sk-your-key-here"
export MODEL_NAME="gpt-4o"
```

### Run the Pipeline

```bash
# Smoke test: generate + evaluate on a few tasks
bash scripts/run_test.sh

# Generate skills for all 187 tasks using naive_prompt baseline
bash scripts/run_all_generate.sh --only naive_prompt --max-parallel 20

# Evaluate generated skills
bash scripts/run_all_eval.sh --only naive_prompt --max-parallel 20 --trials 3
```

### Run a Single Task

```bash
# Generate skill for one task
python3 baseline/naive_prompt/generate_skill.py \
    --task-id scikitimage-task-001 --source code_doc

# Evaluate
python3 scripts/run_eval.py \
    --task-id scikitimage-task-001 --source code_doc \
    --skill-method naive_prompt --trials 3
```

## Adding Your Own Baseline

1. Create `baseline/<your_method>/generate_skill.py`
2. Read from `data_source/`, write to `generated_skills/<your_method>/`
3. Output at least `SKILL.md` per task

Minimal interface:

```bash
python3 baseline/<your_method>/generate_skill.py \
    --source all --all
```

See `baseline/naive_prompt/generate_skill.py` for a reference implementation (single LLM call per task).

### Output Format

```
generated_skills/<method>/<model>/<run_id>/<source>/<collection>/tasks/<task_id>/
  SKILL.md          # Required: skill content with YAML frontmatter
  meta.json         # Recommended: generation metadata
```

`SKILL.md` format:
```markdown
---
name: "Skill Name"
description: "What this skill does"
---

# Skill content here...
```

## Repository Structure

```
SkillGenBench/
├── data_source/                 # Standardized task inputs (187 tasks)
│   ├── code_repo/               #   Repository-grounded (123)
│   ├── code_doc/                #   Document-grounded code (28)
│   └── domain_knowledge_doc/    #   Domain-knowledge document (36)
├── skill_evaluation/            # Evaluation harnesses (187 tasks)
├── scripts/                     # Pipeline scripts & shell orchestration
│   ├── pipeline.py              #   Main orchestrator
│   ├── run_eval.py              #   Evaluation runner
│   ├── run_all_generate.sh      #   Batch skill generation
│   ├── run_all_eval.sh          #   Batch evaluation
│   └── ...                      #   Supporting modules
├── baseline/                    # Baseline implementations
│   ├── _shared/                 #   Shared infrastructure
│   └── naive_prompt/            #   Example: single-prompt baseline
└── docker/                      # Evaluation Docker images
```

## License

TBD

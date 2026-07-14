---
license: apache-2.0
size_categories:
- 1K<n<10K
configs:
- config_name: default
  data_files:
  - split: train
    path: metadata.csv
---

# Tessl Skills Evaluation Dataset

## Dataset Summary

This dataset accompanies the paper *A Framework for Evaluating Agentic Skills
at Scale* and supports rigorous, reusable evaluation of **agent skills** —
structured, reusable knowledge artifacts that augment LLM agent capabilities.

Each task is a realistic, end-to-end challenge derived from a real-world skill
(or a group of related skills) sourced from open-source GitHub repositories of
trusted, well-known organizations. A task ships with a natural-language
problem statement (`task.md`), relevant input files (if the task requires them),
a folder of the skills required to solve the task properly, and
two LLM-judge rubrics — **Instruction Following** and **Goal Completion** — so
the same instance can be replayed across different models, agent harnesses, or
skill revisions and scored consistently.

The dataset is split into two task types:

- **`single_skill`** (851 tasks): each task exercises exactly one skill, to
  measure the contribution of an individual skill in isolation.
- **`multi_skill`** (259 tasks): each task exercises 2–5 skills drawn from
  the same creator/repository collection, to measure how skills compose under
  realistic multi-skill workflows.

In total, the release contains **1,110 tasks** drawing on **608 distinct
skills** from **148 GitHub repositories**.

## How to Use

The release ships in two parts:

- **`metadata.csv`** — one row per task with overall information about each
  task, including its type, the skills it uses, and the GitHub repositories
  those skills come from. Sufficient on its own for filtering, browsing, or
  joining against your own results.
- **`tasks.zip`** — extracts to a `tasks/` directory containing the actual
  task content (prompts, input files, installed skills, and rubrics) — one
  subfolder per task, keyed by `task-name`.

Load the metadata directly with the `datasets` library:

```python
from datasets import load_dataset

ds = load_dataset("tesslio/task-evals-for-skills")
print(ds["train"][0]["task-name"], ds["train"][0]["task_type"])
```

To work with the actual task content, download and unzip `tasks.zip` from the
same repository:

```python
from huggingface_hub import hf_hub_download
import zipfile, pathlib

zip_path = hf_hub_download(repo_id="tesslio/task-evals-for-skills",
                            filename="tasks.zip",
                            repo_type="dataset")
with zipfile.ZipFile(zip_path) as z:
    z.extractall(".")  # creates ./tasks/<task-name>/...
```

Each `tasks/<task-name>/` folder contains:

| Sub-path | Purpose |
| --- | --- |
| `task.md` | The natural-language task description shown to the agent. |
| `inputs/` | (Optional) input files staged into the agent's workspace. |
| `skills/<skill_unique_name>/` | The skill(s) installed for this task. |
| `rubrics/instruction-following.json` | LLM-judge rubric items scoring how well the agent followed the skill's instructions. |
| `rubrics/task-completion.json` | LLM-judge rubric items scoring whether the agent completed the underlying goal. |

## Dataset Structure

`metadata.csv` provides one row per task with the following schema:

| Field | Type | Description |
| --- | --- | --- |
| `task-name` | str | Unique task identifier; format `tessl-<type>-<group>_<idx>`. |
| `task_type` | str | `single_skill` or `multi_skill`. |
| `task_group` | str | Identifier shared by all task variants of the same template (everything before the trailing `_<idx>`). For single-skill tasks this groups variants targeting the same skill; for multi-skill tasks this groups variants drawn from the same creator/repository collection. |
| `task_idx_in_group` | int | Variant index within `task_group` (0, 1, 2, …). |
| `task_description` | str | Verbatim contents of `task.md` — the prompt given to the agent. |
| `skills-used` | JSON list[str] | The set of `skill_unique_name` identifiers installed for this task. Each name matches a sub-folder under the task's `skills/` directory. |
| `skills_github_sources` | JSON list[str] | Deduplicated GitHub repository URLs from which the skills were sourced. |

### Naming convention

- **Single-skill** names encode the skill identity directly:
  `tessl-single-<creator>_<repo>_<skill>_<idx>`
  (e.g. `tessl-single-microsoft_apm_cli-logging-ux_1`)
- **Multi-skill** names encode the *collection* (creator-repo joined with a
  hyphen), since multiple skills are installed:
  `tessl-multi-<creator>-<repo>_<idx>`
  (e.g. `tessl-multi-microsoft-apm_0`)

The same skill may appear both as the sole skill in a `single_skill` task and
alongside sibling skills in a `multi_skill` task.

## License

The dataset is released under the Apache 2.0 license. The skills themselves
were sourced from public GitHub repositories listed in
`skills_github_sources`; please respect the original license of each upstream
repository when using or redistributing skill content.

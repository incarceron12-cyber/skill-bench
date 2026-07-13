---
language:
  - en
license: mit
size_categories:
  - n<1K
task_categories:
  - other
tags:
  - synthetic
  - computer-use
  - agents
  - persona
  - filesystem
pretty_name: Synthetic Computers
configs:
  - config_name: default
    data_files:
      - split: train
        path: data/train-*.parquet
    default: true
dataset_info:
  config_name: default
  features:
    - name: computer_id
      dtype: string
    - name: collaboration_context
      dtype: string
    - name: file_graph
      dtype: string
    - name: file_list
      dtype: string
    - name: filesystem_policy
      dtype: string
    - name: monthly_objectives
      dtype: string
    - name: persona
      dtype: string
    - name: project_index
      dtype: string
    - name: user_profile
      dtype: string
  splits:
    - name: train
      num_examples: 98
---

# Synthetic Computers

**Paper:** [Synthetic Computers at Scale for Long-Horizon Productivity Simulation (arXiv:2604.28181)](https://arxiv.org/abs/2604.28181)

A dataset of **98 synthetic computer environments** designed for research on
computer-use agents, long-horizon planning, and persona-grounded reasoning.
Each row describes a single fictional user's computer — including the user's
persona, professional context, monthly objectives, collaborators, project
portfolio, filesystem policy, full file listing, and a graph of file
relationships.

## Overview

![Overview of our methodology](figures/overview.png)

*Overview of our methodology: We create user-specific synthetic computers
from personas and use them as grounding environments for long-horizon
productivity simulations, producing both professional deliverables and
process signals for improving agents in productivity scenarios.*

The collection mixes two operating systems:

| OS      | Computers |
|---------|-----------|
| macOS   | 48        |
| Windows | 50        |
| **Total** | **98**  |

## Quick Start

```python
from datasets import load_dataset
import json

ds = load_dataset("microsoft/synthetic-computers-at-scale", split="train")
print(ds)

row = ds[0]
print(row["computer_id"])

# All structured fields are stored as JSON strings.
persona = json.loads(row["persona"])
file_graph = json.loads(row["file_graph"])
print(persona["persona"][:200])
print(f"file_graph: {len(file_graph['nodes'])} nodes, "
      f"{len(file_graph['edges'])} edges")
```

## Dataset Structure

One row per synthetic computer. All non-id columns are **JSON-encoded
strings** (use `json.loads`) — this preserves nested structure without
forcing a brittle unified schema across heterogeneous personas.

| Column                  | Type   | Description |
|-------------------------|--------|-------------|
| `computer_id`           | string | e.g. `mac_computer_000050`, `win_computer_000007`. Prefix indicates the host OS. |
| `persona`               | string | High-level persona description, current timestamp, OS. Keys: `persona`, `current_timestamp`, `os`. |
| `user_profile`          | string | Rich profile of the simulated user. Keys: `identity`, `biographical_summary`, `career_profile`, `historical_work_context`, `work_context`, `current_projects_overview`, `work_style`, `document_behavior`, `collaboration_context`, `related_people`. |
| `collaboration_context` | string | Collaborators the user works with. Keys: `collaborators`. |
| `monthly_objectives`    | string | Simulated monthly plan. Keys: `simulation_period`, `deliverables`, `recurring_activities`, `weekly_focus`. |
| `project_index`         | string | Index of active projects. Keys: `projects`. |
| `filesystem_policy`     | string | Conventions governing where and how files live on this computer. Keys: `system_start_timestamp`, `volume_layout`, `default_paths`, `storage_patterns`, `organization_style`, `naming_style`, `usage_patterns`. |
| `file_list`             | string | Flat list of file *records* on the computer (list of dicts with keys such as `path`, `timestamp`, `origin`, `description`, `content_mode`, `project_ids`, `derived_from`, ...). The `path` is the logical filesystem path **inside the simulated computer** (e.g. `/Users/mheller/Desktop/scratch.md`); the actual file bytes live in the companion `drives/` artifacts (see below) and are *not* included in this parquet. |
| `file_graph`            | string | Relationship graph between files. Keys: `nodes`, `edges`. Node ids correspond to entries in `file_list`. |

### Decoding all JSON columns

```python
import json
from datasets import load_dataset

JSON_FIELDS = [
    "collaboration_context", "file_graph", "file_list",
    "filesystem_policy", "monthly_objectives", "persona",
    "project_index", "user_profile",
]

ds = load_dataset("microsoft/synthetic-computers-at-scale", split="train")

def decode(example):
    for k in JSON_FIELDS:
        example[k] = json.loads(example[k])
    return example

# Note: after decoding, columns become Python objects (dict / list);
# they will not be representable in Arrow with a uniform schema.
sample = decode(dict(ds[0]))
```

## Why JSON strings?

Different personas and projects produce structurally different content
(e.g. project records have different optional fields). Storing each blob as
a JSON string keeps the parquet schema simple and lossless. If you need a
typed sub-schema for a particular field, decode and re-cast in your own
preprocessing step.

## Data Construction

Each computer is generated by a synthetic pipeline that:

1. Samples a persona and target operating system.
2. Expands the persona into a detailed user profile and collaboration
   network.
3. Plans monthly objectives, recurring activities, and weekly focus.
4. Materializes a project portfolio and a corresponding filesystem policy
   (drives, default paths, naming/organization conventions).
5. Generates a concrete file list consistent with the policy and projects.
6. Derives a file relationship graph (`nodes`, `edges`) over the file list.

The associated per-computer artifacts (the rendered `drives/` directories
containing the actual file contents, plus retrospective analysis reports)
are *not* included in this parquet — only the structured JSON metadata
above.

## Companion Artifacts (file contents)

This parquet only ships the **metadata** for each computer. The actual file
bytes for each simulated computer (the `drives/` trees) and the per-computer
retrospective analysis reports are distributed in the **same dataset repo**
as zstd-compressed tarballs:

| Path in repo                                          | Size (compressed) | Contents |
|-------------------------------------------------------|-------------------|----------|
| `artifacts/computers.tar.zst`                         | ~1.4 GB           | One directory per computer with `drives/` plus the same JSON files that are also in the parquet. |
| `artifacts/retrospective_analysis_reports.tar.zst`    | ~6 MB             | Retrospective analysis reports per computer. |

After extraction the layout is:

```
artifacts/
  computers/
    <computer_id>/                # e.g. mac_computer_000050
      drives/
        <volume>/                 # e.g. "Macintosh HD", "AxiomBackup", "C:", ...
          <path-inside-volume>    # mirrors file_list[i].path
      collaboration_context.json  # same content as the parquet column
      file_graph.json
      file_list.json
      filesystem_policy.json
      monthly_objectives.json
      persona.json
      project_index.json
      user_profile.json
  retrospective_analysis_reports/
```

### Downloading and extracting

```python
from huggingface_hub import hf_hub_download
import subprocess, pathlib

repo_id = "microsoft/synthetic-computers-at-scale"

tar_path = hf_hub_download(
    repo_id=repo_id,
    repo_type="dataset",
    filename="artifacts/computers.tar.zst",
)

out_dir = pathlib.Path("./artifacts")
out_dir.mkdir(exist_ok=True)
subprocess.run(
    ["tar", "--use-compress-program=unzstd", "-xf", tar_path, "-C", out_dir],
    check=True,
)
```

Or from the shell:

```bash
huggingface-cli download microsoft/synthetic-computers-at-scale \
    artifacts/computers.tar.zst \
    --repo-type dataset --local-dir .
tar --use-compress-program=unzstd -xf artifacts/computers.tar.zst -C artifacts/
```

If you only need the metadata (planning, persona modeling, file-graph
reasoning that does not require file contents), the parquet alone is
sufficient and you can skip the tarballs.

## Intended Uses

- Benchmarking computer-use / desktop agents over realistic, persona-driven
  filesystems.
- Studying long-horizon planning grounded in monthly objectives and project
  portfolios.
- Synthetic data for training agents that must reason about file
  organization, naming, and inter-file relationships.

## Limitations

- Fully synthetic: personas, projects, and files are fictional. Names and
  details should not be treated as references to real people or
  organizations.
- Heterogeneous schemas inside JSON fields — no guarantee that every
  computer exposes the same nested keys.
- English only.
- Small scale (98 computers). Intended for evaluation and as a seed for
  larger generations rather than large-scale pretraining.

## License

MIT License.

## Citation

Paper: <https://arxiv.org/abs/2604.28181>

```bibtex
@article{syntheticcomputers2026,
  author={Tao Ge, Baolin Peng, Hao Cheng, Jianfeng Gao},
  title={Synthetic Computers at Scale for Long-Horizon Productivity Simulation},
  journal={arXiv preprint arXiv:2604.28181},
  year={2026},
}
```

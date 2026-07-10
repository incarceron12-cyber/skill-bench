---
license: apache-2.0
configs:
- config_name: default
  data_files:
  - split: full
    path: "task_en_metadata_table.csv"
---

# Workspace-Bench

[![Homepage](https://img.shields.io/badge/Homepage-Workspace--Bench-blue?logo=googlechrome&logoColor=white)](https://workspace-bench.github.io/)
[![GitHub](https://img.shields.io/badge/GitHub-OpenDataBox%2FWorkspace--Bench-181717?logo=github&logoColor=white)](https://github.com/OpenDataBox/Workspace-Bench)
[![Dataset](https://img.shields.io/badge/HuggingFace-Workspace--Bench-orange?logo=huggingface&logoColor=white)](https://huggingface.co/datasets/Workspace-Bench/Workspace-Bench)
[![Lite Dataset](https://img.shields.io/badge/HuggingFace-Workspace--Bench--Lite-yellow?logo=huggingface&logoColor=black)](https://huggingface.co/datasets/Workspace-Bench/Workspace-Bench-Lite)
[![Paper](https://img.shields.io/badge/arXiv-2605.03596-b31b1b?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2605.03596)

Workspace-Bench is a benchmark for evaluating AI agents on realistic workspace tasks with large-scale file dependencies. It is designed to measure whether an agent can discover, interpret, and use the right files inside a noisy professional workspace, rather than solving tasks from isolated inputs or fully pre-packaged evidence.

The benchmark is introduced in the paper **"Workspace-Bench 1.0: Benchmarking AI Agents on Workspace Tasks with Large-Scale File Dependencies"**. It focuses on **Workspace Learning**, namely the ability of an agent to identify, reason over, exploit, and update explicit and implicit dependencies among heterogeneous files in a worker's digital environment.

![Framework](./assets/Framework.png)

## Why Workspace-Bench?

Many existing agent benchmarks evaluate prompt-following, tool use, or small sets of task-specific files. Real workplace tasks are harder: agents must search large directory trees, distinguish relevant from distracting files, reason across formats, and track file lineage such as drafts, revisions, and final versions.

Workspace-Bench is built to capture these challenges through:

- **Role-specific workspaces** rather than a single synthetic file system.
- **Large-scale heterogeneous files** distributed across realistic directory structures.
- **Dependency-driven tasks** that require multi-file retrieval and cross-file reasoning.
- **Process-aware evaluation** that checks not only final outputs but also whether agents found and used the right evidence.

## Benchmark Overview

According to the paper, the full Workspace-Bench release contains:

- **5 professional workspaces**: Operations Manager, Logistics Manager, AI Product Manager, Backend Developer, and Researcher.
- **388 curated tasks** with explicit file dependencies.
- **20,476 files** spanning **74 file types**.
- **7,399 evaluation rubrics** for fine-grained assessment.
- A benchmark scale of up to **20 GB** of workspace content.

The benchmark evaluates six key Workspace Learning abilities:

- **Workspace Exploration**
- **Task-Supporting Files Utilization**
- **Result-Providing Files Utilization**
- **Semantic Content Relations Understanding**
- **Lineage Tracing**
- **Heterogeneous File Understanding**

Tasks are grouped into three difficulty levels:

- **Easy**: primarily workspace exploration and result-providing file use
- **Medium**: stronger reliance on semantic relations and task-supporting files
- **Hard**: heterogeneous file understanding and lineage reasoning

![Distribution](./assets/Distribution.png)

## Workspace-Bench-Lite

The paper also introduces **Workspace-Bench-Lite**, a **100-task** subset that preserves the distribution of:

- workspaces
- difficulty levels
- Workspace Learning abilities

This lite split is intended to reduce evaluation cost by roughly **70%** while maintaining representative benchmark coverage.

## What This Repository Contains

This repository provides the cleaned task metadata release for Workspace-Bench. It is paired with the workspace filesystem archives in [Workspace-Bench-Workspaces](https://huggingface.co/datasets/Workspace-Bench/Workspace-Bench-Workspaces), rather than storing the large raw workspace contents in this repository.

Current contents include:

- `task_clean_en/`: cleaned English task metadata organized by `absolute_id`
- `task_clean_cn/`: cleaned Chinese task metadata organized by `absolute_id`
- `task_en_metadata_table.csv`: a flat English metadata table for analysis and filtering
- `task_clean_cn_metadata_table.csv`: a flat Chinese metadata table for analysis and filtering

At the time of writing, each language split contains **388 tasks**, one folder per task ID. Task metadata files include a `language` field: `"en"` for English tasks and `"cn"` for Chinese tasks.

## Evaluation Philosophy

Workspace-Bench is designed to move beyond final-answer-only evaluation. In the full benchmark setting, each task is associated with:

- a **dependency graph** describing the minimal set of essential files
- a **rubric set** covering foundational, procedural, and result-oriented checks

This supports process-aware evaluation such as:

- whether the agent identified the correct files
- whether it used the correct file versions
- whether it followed the intended dependency structure
- whether the final output satisfies detailed task requirements

## Main Findings From The Paper

The paper reports that current agents remain far from reliable on realistic workspace tasks:

- Average rubric pass rate across evaluated agent configurations is **47.4%**
- The best reported agent configuration reaches **68.7%**
- Human + tools performance reaches **80.7%**

The main bottlenecks are:

- **Heterogeneous File Understanding**
- **Lineage Tracing**

Performance also drops consistently as task difficulty increases from **Easy** to **Medium** to **Hard**.

![Rubrics Success](./assets/rubrics_success.png)

## Changelog

### 2026-07-02

- Added a `language` field to task `metadata.json` files and metadata table CSV files. The value is `"en"` for English tasks and `"cn"` for Chinese tasks.
- Tasks `95`, `328`, and `388`: placed the required input files explicitly under their designated paths in the workspace filesystem, so agents can find the files from the workspace context.
- Tasks `288`, `289`, and `258`: replaced corrupted input files with readable workspace files.
- Tasks `289`, `274`, `334`, and `108`: refined selected rubrics to make the evaluation criteria more precise, self-consistent, and aligned with the expected output format.

## Resources

- **Project Homepage**: [workspace-bench.github.io](https://workspace-bench.github.io/)
- **Full Dataset**: [Workspace-Bench on Hugging Face](https://huggingface.co/datasets/Workspace-Bench/Workspace-Bench)
- **Lite Dataset**: [Workspace-Bench-Lite on Hugging Face](https://huggingface.co/datasets/Workspace-Bench/Workspace-Bench-Lite)
- **Paper**: [arXiv:2605.03596](https://arxiv.org/abs/2605.03596)

## Citation

If you find Workspace-Bench useful in your research, please cite:

```bibtex
@misc{tang2026workspacebench10benchmarkingai,
  title={Workspace-Bench 1.0: Benchmarking AI Agents on Workspace Tasks with Large-Scale File Dependencies},
  author={Zirui Tang and Xuanhe Zhou and Yumou Liu and Linchun Li and Weizheng Wang and Hongzhang Huang and Jun Zhou and Jiachen Song and Shaoli Yu and Jinqi Wang and Zihang Zhou and Hongyi Zhou and Yuting Lv and Jinyang Li and Jiashuo Liu and Ruoyu Chen and Chunwei Liu and GuoLiang Li and Jihua Kang and Fan Wu},
  year={2026},
  eprint={2605.03596},
  archivePrefix={arXiv},
  primaryClass={cs.AI},
  url={https://arxiv.org/abs/2605.03596}
}
```

## License

This repository is released under the **Apache-2.0** license.

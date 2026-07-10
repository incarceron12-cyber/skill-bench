---
configs:
- config_name: default
  data_files:
  - split: lite
    path: "task_lite_clean_en_metadata_table.csv"
size_categories:
- n<1K
---

<div align="center">
  <h1>Workspace-Bench-Lite</h1>
  <h3>A Lightweight Subset of Workspace-Bench for Fast and Cost-Efficient Evaluation</h3>
</div>

[![Homepage](https://img.shields.io/badge/Homepage-Workspace--Bench-blue?logo=googlechrome&logoColor=white)](https://workspace-bench.github.io/)
[![GitHub](https://img.shields.io/badge/GitHub-OpenDataBox%2FWorkspace--Bench-181717?logo=github&logoColor=white)](https://github.com/OpenDataBox/Workspace-Bench)
[![Dataset](https://img.shields.io/badge/HuggingFace-Workspace--Bench-orange?logo=huggingface&logoColor=white)](https://huggingface.co/datasets/Workspace-Bench/Workspace-Bench)
[![Lite Dataset](https://img.shields.io/badge/HuggingFace-Workspace--Bench--Lite-yellow?logo=huggingface&logoColor=black)](https://huggingface.co/datasets/Workspace-Bench/Workspace-Bench-Lite)
[![Paper](https://img.shields.io/badge/arXiv-2605.03596-b31b1b?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2605.03596)

<div align="center">
  <a href="#overview">Overview</a> •
  <a href="#leaderboard">LeaderBoard</a> •
  <a href="#distribution">Distribution</a> •
  <a href="#quick-start">Quick Start</a> •
  <a href="#changelog">Changelog</a> •
  <a href="#citation">Citation</a>
</div>

## Overview

Workspace-Bench-Lite is the **Lite split of Workspace-Bench 1.0**, designed for fast iteration and lower-cost benchmarking while preserving the core evaluation setting of the full benchmark.

It contains **100 tasks** selected from the full Workspace-Bench and is intended to maintain distributional fidelity across:

- workspace roles
- task difficulty levels
- workspace-learning capabilities
- file dependency patterns

Workspace-Bench-Lite keeps the central benchmark objective unchanged: evaluating whether AI agents can perform **Workspace Learning**, namely identifying, reasoning over, and acting on explicit and implicit dependencies among heterogeneous files in realistic workspaces.

Compared with the full benchmark, Workspace-Bench-Lite is more suitable for:

- rapid prototyping of agent systems
- low-cost model and harness comparison
- regression testing during agent development
- lightweight public leaderboard evaluation

<div align="center">
  <img src="assets/Framework.png" alt="Workspace-Bench-Lite framework overview" width="980" />
</div>

The figure above summarizes the overall Workspace-Bench framework that Lite inherits from the full benchmark: role-specific workspaces, cross-file dependent tasks, and capability-oriented rubric evaluation. Workspace-Bench-Lite keeps this same evaluation setting while offering a more lightweight split for faster experimentation.

In the Workspace-Bench paper, the Lite split is described as a **100-task subset** that preserves the benchmark distribution while reducing evaluation costs by about **70%**. This makes it a practical entry point for researchers and developers who want to evaluate workspace agents without running the full 388-task benchmark.

The Lite split remains grounded in the same benchmark philosophy as the full version:

- realistic workspace tasks rather than isolated QA
- heterogeneous files rather than single-format inputs
- dependency-aware task solving rather than direct prompt lookup
- rubric-based evaluation rather than only final-answer matching

## LeaderBoard

<div align="center">
  <img src="assets/rubrics_success.png" alt="Workspace-Bench-Lite leaderboard snapshot" width="980" />
</div>

The figure above shows a leaderboard snapshot of rubric pass rates on Workspace-Bench-Lite across different agent harnesses and backbone models. It highlights the same central takeaway as the full benchmark: current agents still show a clear gap from human-level performance, and both the foundation model and the harness design materially affect final results.

## Distribution

<div align="center">
  <img src="assets/Distribution.png" alt="Workspace-Bench-Lite distribution overview" width="980" />
</div>

The distribution figure provides a compact overview of the Lite split, including file types, task abilities, task difficulty, workspace allocation, rubric counts, required files per task, and dependency structure. Although lighter than the full benchmark, Workspace-Bench-Lite is designed to preserve the key distributional characteristics of Workspace-Bench.

## Repository Contents

This repository provides the cleaned task metadata release for Workspace-Bench-Lite. It is paired with the workspace filesystem archives in [Workspace-Bench-Workspaces](https://huggingface.co/datasets/Workspace-Bench/Workspace-Bench-Workspaces), rather than storing the large raw workspace contents in this repository.

Current contents include:

- `task_lite_clean_en/`: cleaned English Lite task metadata organized by `absolute_id`
- `task_lite_clean_cn/`: cleaned Chinese Lite task metadata organized by `absolute_id`
- `task_lite_clean_en_metadata_table.csv`: a flat English Lite metadata table for analysis and filtering
- `task_lite_clean_cn_metadata_table.csv`: a flat Chinese Lite metadata table for analysis and filtering

At the time of writing, each language split contains **100 tasks**, one folder per task ID. Task metadata files include a `language` field: `"en"` for English tasks and `"cn"` for Chinese tasks.

## Quick Start

Please refer to the official GitHub repository for benchmark setup, evaluation instructions, and updates:

- GitHub repository: https://github.com/OpenDataBox/Workspace-Bench

More Lite-specific usage notes will be added in future updates.

## Changelog

### 2026-07-02

- Added a `language` field to task `metadata.json` files and metadata table CSV files. The value is `"en"` for English tasks and `"cn"` for Chinese tasks.
- Tasks `95`, `328`, and `388`: placed the required input files explicitly under their designated paths in the workspace filesystem, so agents can find the files from the workspace context.
- Tasks `288`, `289`, and `258`: replaced corrupted input files with readable workspace files.
- Tasks `289`, `274`, `334`, and `108`: refined selected rubrics to make the evaluation criteria more precise, self-consistent, and aligned with the expected output format.

## Citation

If you use Workspace-Bench-Lite in your research, please cite the Workspace-Bench paper:

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

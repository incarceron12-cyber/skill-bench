---
license: other
language:
- en
pretty_name: Personal Agent Sycophancy Benchmark
task_categories:
- text-generation
tags:
- ai-safety
- agent-safety
- sycophancy
- personal-agents
- benchmark
- stateful-agents
- arxiv:2607.10526
size_categories:
- 1K<n<10K
configs:
- config_name: default
  data_files:
  - split: test
    path: data/pasb_full.jsonl
- config_name: sample
  data_files:
  - split: test
    path: sample_datasets/pasb_sample.jsonl
---

# PASB: Personal Agent Sycophancy Benchmark

[![Project Page](https://img.shields.io/badge/🌐_Project-Website-5b46c9)](https://henrymao2004.github.io/agent-sycophancy/) [![Leaderboard](https://img.shields.io/badge/🏆-Interactive_Leaderboard-5b46c9)](https://henrymao2004.github.io/agent-sycophancy/#leaderboard) [![Episode Demo](https://img.shields.io/badge/🎬-336_Episode_Demo-e0574f)](https://henrymao2004.github.io/agent-sycophancy/#demo) [![Code](https://img.shields.io/badge/GitHub-Code-24292e?logo=github)](https://github.com/henrymao2004/agent-sycophancy) [![arXiv](https://img.shields.io/badge/arXiv-2607.10526-b31b1b)](https://arxiv.org/abs/2607.10526)

**📄 Paper:** https://arxiv.org/abs/2607.10526
**🌐 Project page & interactive leaderboard:** https://henrymao2004.github.io/agent-sycophancy/
**💻 Code:** https://github.com/henrymao2004/agent-sycophancy

PASB evaluates whether a personal agent accepts a user-centric claim, writes it into durable state, and later reuses it in a fresh neutral query session. Each task has a five-turn persist stage followed by a three-turn query stage.

## Files

- `data/pasb_full.jsonl`: full 1,600-task benchmark.
- `sample_datasets/pasb_sample.jsonl`: 8-task smoke sample.
- `DATA_SCHEMA.md`: field-level schema notes.

## Dataset Structure

Each JSONL row is one PASB episode. The benchmark crosses four scenario framings with four temporal delivery patterns:

- `Personal-Opinion`
- `Signed-Memory`
- `Environment-Fact`
- `Procedural-Workflow`
- `All-at-Once`
- `Progressive`
- `Drip`
- `Late-Shock`

## Usage

```python
from datasets import load_dataset

pasb = load_dataset("sevens2004/pasb", "default", split="test")
sample = load_dataset("sevens2004/pasb", "sample", split="test")
```

## Citation

```bibtex
@online{2607.10526,
Author = {Xutao Mao and Liangjie Zhao and Leyao Wang and Rui Qian and Qiang Huang and Wentao Wang and Bo Han and Xiang Zheng and Cong Wang},
Title = {Agents Don't Just Agree, They Remember: Benchmarking Persistent Sycophancy in Stateful Personal Agents},
Year = {2026},
Eprint = {2607.10526},
Eprinttype = {arXiv},
}
```

## License

Dataset items are derived from PersistBench and ELEPHANT. Preserve upstream dataset licenses when redistributing derived task data.

---
license: other
license_name: mixed-upstream
license_link: https://github.com/neulab/pace
pretty_name: PACE-Bench
task_categories:
- other
language:
- en
tags:
- agentic-evaluation
- proxy-benchmark
- llm-evaluation
configs:
- config_name: gaia
  data_files: gaia.jsonl
- config_name: swebench
  data_files: swebench.jsonl
- config_name: swebench_multimodal
  data_files: swebench_multimodal.jsonl
- config_name: swtbench
  data_files: swtbench.jsonl
---

# PACE-Bench

📄 **Paper:** [PACE: A Proxy for Agentic Capability Evaluation (arXiv:2607.02032)](https://arxiv.org/abs/2607.02032)
&nbsp;·&nbsp; 💻 **Code:** [github.com/neulab/pace](https://github.com/neulab/pace)

**PACE-Bench is the concrete proxy benchmark produced by
[PACE](https://github.com/neulab/pace)** (*A Proxy for Agentic Capability
Evaluation*, [arXiv:2607.02032](https://arxiv.org/abs/2607.02032)). It is the
dataset **output** of running the PACE selection framework on 4 agentic targets —
not a standalone hand-curated benchmark, but the compact set of source instances
that PACE automatically selects to predict agentic performance.

Evaluating LLM agents on benchmarks like **SWE-Bench** and **GAIA** is expensive
and slow. PACE instead selects a compact set of instances from cheap, non-agentic
evaluations whose aggregate scores most reliably predict a model's performance on
an agentic target. This dataset ships those selected **source instances**, one
file per agentic target.

Each target's proxy is a set of ~100 source instances (budget `C=100`) drawn from
12 non-agentic benchmarks, each carrying the regression **weight** it receives in
PACE's linear predictor.

## Files

```
pace-bench/
├── gaia.jsonl                  # proxy for GAIA
├── swebench.jsonl              # proxy for SWE-Bench Verified
├── swebench_multimodal.jsonl   # proxy for SWE-Bench Multimodal
├── swtbench.jsonl              # proxy for SWT-Bench
└── images/                     # image files for multimodal source instances
    ├── mmmu/
    ├── visualpuzzles/
    └── visualwebbench/
```

## Row schema

Each line is one selected source instance:

| field | type | description |
|-------|------|-------------|
| `instance_id` | str | id of the instance within its source benchmark |
| `source_benchmark` | str | originating non-agentic benchmark |
| `subdir` | str | sub-task / split / metric bucket within the source benchmark |
| `input` | str \| null | the instance prompt/question (see notes) |
| `answer` | str \| null | gold reference, or `null` for checker/test-based metrics |
| `metric` | str | how the instance is scored in the source benchmark |
| `weight` | float | coefficient of this instance in PACE's predictor for the target |
| `images` | list[str] | relative paths under `images/` for multimodal instances (`[]` if none) |
| `content_status` | str | `"ok"`, or `"unresolved:<reason>"` when content could not be recovered |

```json
{"instance_id": "action_prediction_269", "source_benchmark": "visualwebbench",
 "subdir": "", "input": "[action_prediction] www.walgreens.com", "answer": "6",
 "metric": "correct", "weight": -0.0063,
 "images": ["images/visualwebbench/action_prediction_269_1.png"],
 "content_status": "ok"}
```

## Important notes

- **`answer` is `null` when a benchmark has no single gold string** (e.g. IFEval's
  instruction-checker scoring, code test-suite execution). The `metric` field
  documents how such instances are graded upstream.
- **H/D duplicate rows.** PACE combines two selection strategies (target-relevance
  *local* and globally-informative *global*). An instance chosen by **both** appears
  in **two rows** with the same `instance_id` but different `weight` (its local- and
  global-path coefficients). To get one row per instance, group by
  `(instance_id)` and **sum** `weight`. Distinct-instance counts per file are below.
- **Multimodal images** are stored as files under `images/` and referenced by path
  in `images`; upload/keep the `images/` folder alongside the JSONL.

## Coverage

Content resolved for **405 / 412** rows (98.3%). The 7 unresolved rows are kept
with `input=answer=null` and a `content_status` reason — their ids no longer exist
in the current upstream dataset versions (dataset drift): 5 `visualpuzzles` and 2
`visualwebbench` instances.

| target file | rows | distinct instances | content ok | images |
|-------------|-----:|-------------------:|-----------:|-------:|
| gaia.jsonl | 100 | 80 | 99 | 19 |
| swebench.jsonl | 100 | 97 | 97 | 62 |
| swebench_multimodal.jsonl | 105 | 96 | 103 | 23 |
| swtbench.jsonl | 107 | 100 | 106 | 43 |

## Source benchmarks & licensing

Instances are derived from the following upstream benchmarks. **Each instance's
content remains under its upstream license** — consult the upstream source before
redistribution or commercial use.

| `source_benchmark` | upstream |
|--------------------|----------|
| acp_gen | [ibm-research/acp_bench](https://huggingface.co/datasets/ibm-research/acp_bench) |
| bfcl | [Berkeley Function-Calling Leaderboard](https://github.com/ShishirPatil/gorilla) |
| debugbench | [DebugBench](https://github.com/thunlp/DebugBench) |
| ifeval | [google/IFEval](https://huggingface.co/datasets/google/IFEval) |
| lifbench | [LIFBench](https://github.com/wr23zhq/LIFBench) |
| livecodebench | [livecodebench/code_generation_lite](https://huggingface.co/datasets/livecodebench/code_generation_lite), [execution-v2](https://huggingface.co/datasets/livecodebench/execution-v2) |
| logiqa | [EleutherAI/logiqa](https://huggingface.co/datasets/EleutherAI/logiqa) |
| mmmu | [lmms-lab/MMMU](https://huggingface.co/datasets/lmms-lab/MMMU) |
| planbench | [PlanBench](https://github.com/karthikv792/LLMs-Planning) |
| repobench | [tianyang/repobench_python_v1.1](https://huggingface.co/datasets/tianyang/repobench_python_v1.1) |
| visualpuzzles | [neulab/VisualPuzzles](https://huggingface.co/datasets/neulab/VisualPuzzles) |
| visualwebbench | [VisualWebBench](https://huggingface.co/datasets/visualwebbench/VisualWebBench) |

## Usage

```python
from datasets import load_dataset

# one target at a time
gaia = load_dataset("neulab/pace-bench", "gaia", split="train")
print(gaia[0])

# to get one row per instance with a net weight:
import pandas as pd
df = pd.DataFrame(gaia)
net = df.groupby(["instance_id", "source_benchmark"], as_index=False)["weight"].sum()
```

Image paths in `images` are relative to the dataset root; load them from the
`images/` folder.

## Citation

```bibtex
@article{song2026pace,
  title         = {{PACE}: A Proxy for Agentic Capability Evaluation},
  author        = {Song, Yueqi and Sutawika, Lintang and Liu, Jiarui and Tjuatja, Lindia
                   and Geng, Jiayi and Xiao, Yunze and Lee, Daniel and Soni, Aditya Bharat
                   and Lo, Vincent and Yue, Xiang and Neubig, Graham},
  year          = {2026},
  journal       = {arXiv preprint arXiv:2607.02032},
  eprint        = {2607.02032},
  archivePrefix = {arXiv},
  url           = {https://arxiv.org/abs/2607.02032}
}
```

**Links:** [Paper (arXiv:2607.02032)](https://arxiv.org/abs/2607.02032) ·
[Code (neulab/pace)](https://github.com/neulab/pace)

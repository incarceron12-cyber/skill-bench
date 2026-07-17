---
license: cc-by-4.0
language:
  - en
pretty_name: Complex Constraints Benchmark Set
size_categories:
  - n<1K
task_categories:
  - text-generation
tags:
  - instruction-following
  - benchmark
  - llm-evaluation
configs:
  - config_name: default
    data_files:
      - split: test
        path: ComplexConstraints_Benchmark_Set.csv
---

# Complex Constraints Benchmark Set

A benchmark for evaluating how well language models follow complex, multi-constraint instructions.
It contains **75 items** (`CIF-001`–`CIF-075`), each a realistic prompt paired with **10–40
evaluation criteria** (1,559 total) describing what a correct response must satisfy. Criteria are
meant for rubric-based grading (human or LLM-as-a-judge), not exact match.

## Structure

Single wide-format CSV, one item per row:

- `benchmark_id`, `prompt`, `use_case`, `instruction_type`, `prompt_style`
- For each criterion *i* (1–40): `criterion_{i}`. Unused criterion columns are empty.

## Loading

```python
from datasets import load_dataset
ds = load_dataset("USERNAME/complex-constraints-benchmark", split="test")  # TODO: set repo id
print(ds[0]["prompt"])
```

Or with pandas:

```python
import pandas as pd
df = pd.read_csv("ComplexConstraints_Benchmark_Set.csv")
```

## License & Citation

Released under [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/). You may use,
redistribute, and adapt it for any purpose, including commercially, as long as you give
appropriate credit.

```bibtex
@misc{complex_constraints_benchmark,
  title  = {Complex Constraints Benchmark Set},
  author = {TODO: authors},
  year   = {2025},
  url    = {TODO: dataset URL}
}
```

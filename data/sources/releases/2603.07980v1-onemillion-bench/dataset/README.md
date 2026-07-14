---
license: apache-2.0
task_categories:
- question-answering
- text-generation
language:
- en
- zh
tags:
- economics_and_finance
- healthcare_and_medicine
- industry
- law
- natural_science
pretty_name: $OneMillion-Bench
size_categories:
- n<1K
---

# $OneMillion-Bench

A bilingual (Global/Chinese) realistic expert-level benchmark for evaluating language agents across **5 professional domains**. The benchmark contains **400 entries** with detailed, weighted rubric-based grading criteria designed for fine-grained evaluation of domain expertise, analytical reasoning, and instruction following.

## Dataset Structure

Each subdirectory is a **Hugging Face subset** (configuration), and all data is in the **`test`** split.

```
$OneMillion-Bench/
├── economics_and_finance/
│   └── test.json      # 80 entries (40 EN + 40 CN, distinct questions)
├── healthcare_and_medicine/
│   └── test.json      # 80 entries (40 matched EN-CN pairs)
├── industry/
│   └── test.json      # 80 entries (40 matched EN-CN pairs)
├── law/
│   └── test.json      # 80 entries (40 EN + 40 CN, distinct questions)
├── natural_science/
│   └── test.json      # 80 entries (40 matched EN-CN pairs)
└── README.md
```

| Subset | Split | Entries |
|---|---|---|
| `economics_and_finance` | `test` | 80 |
| `healthcare_and_medicine` | `test` | 80 |
| `industry` | `test` | 80 |
| `law` | `test` | 80 |
| `natural_science` | `test` | 80 |

## Domains & Coverage

| Domain | Categories | Example Subcategories | Bilingual Mode |
|---|---|---|---|
| **Economics & Finance** | Investing, FinTech, Banking, Insurance, M&A | Equities, VC/PE, Cryptocurrency, Commodities | Separate questions per language |
| **Healthcare & Medicine** | Clinical Medicine, Basic Medicine, Pharma & Biotech | Hepatobiliary Surgery, Oncology, Nephrology, Dentistry | Matched translation pairs |
| **Industry** | Telecommunications, ML, Architecture, Semiconductors | Backend Dev, Chemical Engineering, Chip Design | Matched translation pairs |
| **Law** | Civil, Criminal, International, Corporate, IP, Labor | Contract Disputes, Criminal Defense, Copyright, M&A | Separate questions per language |
| **Natural Science** | Chemistry, Biology, Physics, Mathematics | Organic Chemistry, Condensed Matter, Molecular Biology | Matched translation pairs |

## Entry Schema

Each entry is a JSON object with 7 fields:

```jsonc
{
  "id": "uuid-string",            // globally unique identifier
  "case_id": 1,                   // links bilingual pairs (in matched-pair domains)
  "language": "en",               // "en" or "cn" (50/50 split in every file)
  "system_prompt": "",            // reserved (empty across all entries)
  "question": "...",              // expert-level evaluation prompt
  "tags": {
    "topics": [                   // 3-level taxonomy
      "Domain",                   //   e.g. "Economics and Finance"
      "Category",                 //   e.g. "Investing"
      "Subcategory"               //   e.g. "Equities"
    ],
    "time_sensitivity": {
      "time_sensitivity": "Time-agnostic",   // or "Weakly/Strongly time-sensitive"
      "year_month": "NA",                    // "YYYY-MM" when time-sensitive
      "day": "NA"                            // "DD" when applicable
    }
  },
  "rubrics": [                    // weighted grading criteria (11-37 per entry)
    {
      "rubric_number": 1,
      "rubric_detail": "...",     // specific grading criterion
      "rubric_weight": 5,         // positive = reward, negative = penalty
      "rubric_tag": "..."         // category (see below)
    }
  ]
}
```

### Rubric Labels

| Label | Role | Typical Weight |
|---|---|---|
| Factual Information | Tests factual accuracy | +3 to +5 |
| Analytical Reasoning | Assesses depth of analysis | +3 to +5 |
| Structure and Formatting | Evaluates output organization | -2 to -4 (penalty) |
| Instructions Following | Checks compliance with task constraints | mixed |

## Quick Start

```python
from datasets import load_dataset

# Load a subset from Hugging Face (test split)
ds = load_dataset("humanlaya-data-lab/OneMillion-Bench", "natural_science", split="test")

# Filter English entries
en_entries = ds.filter(lambda x: x["language"] == "en")

# Iterate with rubrics
for entry in en_entries.select(range(1)):
    print(f"Topic: {' > '.join(entry['tags']['topics'])}")
    print(f"Question: {entry['question'][:200]}...")
    print(f"Rubrics ({len(entry['rubrics'])}):")
    for r in entry["rubrics"][:3]:
        print(f"  [{r['rubric_weight']:+d}] {r['rubric_tag']}: {r['rubric_detail'][:80]}...")
```

Example output:

```
Topic: Natural Sciences > Chemistry > Organic Chemistry
Question: You are an expert in organic chemistry. A graduate student is researching ...
Rubrics (18):
  [+5] Factual Information: Correctly identifies the primary reaction mechanism ...
  [+4] Analytical Reasoning: Provides a coherent comparison of thermodynamic vs ...
  [-3] Structure and Formatting: Response lacks clear section headings or logica...
```

## Evaluation

Each rubric carries a signed weight: positive weights are points earned when the criterion is met, negative weights are penalties applied when violated. The judge evaluates **all rubrics in a single call** and returns a JSON array of binary (yes/no) verdicts.

```python
# pip install datasets openai
import json, re
from datasets import load_dataset
from openai import OpenAI

client = OpenAI()  # or any OpenAI-compatible client

def evaluate(question, response, rubrics, judge_model="openai/gpt-5.4"):
    """Judge all rubrics in one call, return weighted score."""
    rubrics_text = "\n\n".join(
        f"**Rubric {r['rubric_number']}** (weight {r['rubric_weight']:+d})\n{r['rubric_detail']}"
        for r in rubrics
    )
    judge_out = client.chat.completions.create(
        model=judge_model, temperature=0,
        messages=[
            {"role": "system", "content": "You are a strict rubric grader. Reply ONLY with a JSON array."},
            {"role": "user", "content": (
                f"For each rubric, output {{\"rubric_id\": <number>, \"status\": \"yes\" or \"no\"}}.\n\n"
                f"## Question\n{question}\n\n## Response\n{response}\n\n## Rubrics\n{rubrics_text}"
            )},
        ],
    ).choices[0].message.content

    # Parse JSON (handles ```json fences and trailing commas)
    m = re.search(r"```(?:json)?\s*(\[[\s\S]*?\])\s*```", judge_out)
    verdicts = json.loads(re.sub(r",\s*([}\]])", r"\1", m.group(1) if m else judge_out))
    hits = {v["rubric_id"] for v in verdicts if str(v.get("status", "")).lower() in ("yes", "是")}

    max_pos = sum(r["rubric_weight"] for r in rubrics if r["rubric_weight"] > 0)
    earned = sum(r["rubric_weight"] for r in rubrics if r["rubric_number"] in hits)
    return {"earned": earned, "max": max_pos, "pct": earned / max_pos if max_pos else 0}

# --- Run on one subset ---
ds = load_dataset("humanlaya-data-lab/OneMillion-Bench", "natural_science", split="test")
for entry in ds.select(range(3)):
    response = client.chat.completions.create(
        model="openai/gpt-5.4",
        messages=[{"role": "user", "content": entry["question"]}],
    ).choices[0].message.content
    result = evaluate(entry["question"], response, entry["rubrics"])
    print(f"{' > '.join(entry['tags']['topics'])}  →  {result['earned']}/{result['max']} ({result['pct']:.1%})")
```

## Citation
```latex
@article{yang2026onemillionbench,
    title={\$OneMillion-Bench: How Far are Language Agents from Human Experts?},
    author={Yang, Qianyu and Liu, Yang and Li, Jiaqi and Bai, Jun and Chen, Hao and Chen, Kaiyuan and Duan, Tiliang and Dong, Jiayun and Hu, Xiaobo and Jia, Zixia and Liu, Yang and Peng, Tao and Ren, Yixin and Tian, Ran and Wang, Zaiyuan and Xiao, Yanglihong and Yao, Gang and Yin, Lingyue and Zhang, Ge and Zhang, Chun and Jiao, Jianpeng and Zheng, Zilong and Gong, Yuan},
    journal={arXiv preprint arXiv:2603.07980},
    year={2026}
}
```

## License

Apache 2.0

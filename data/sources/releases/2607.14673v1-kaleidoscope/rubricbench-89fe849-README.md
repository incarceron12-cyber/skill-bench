---
license: mit
configs:
- config_name: default
  data_files:
  - split: test
    path: "qa_custom_metrics_ann.csv"
---

# Kaleidoscope Custom Metrics - Human Annotations

## Dataset Details

This dataset contains 108 question-answer pairs from 4 Singapore government AI chatbots, each annotated by 2 human annotators across 14 quality dimensions. It is designed for evaluating and benchmarking LLM-as-a-judge systems on multi-dimensional rubric-based assessment.

**Questions** were synthetically generated using Kaleidoscope. **Answers** were produced by 4 AI chatbots (AIBots), each operating under 2 distinct system prompt styles:

| AIBot | Normal Style | Pro Style | Samples |
|-------|-------------|-----------|---------|
| **BTT Bot** | Factual and serious driving theory tutor | Critical and strict "no-nonsense" instructor with sarcasm | 30 |
| **HDB Bot** | Neutral HDB policy specialist | Emotional, outspoken, and prejudiced officer | 30 |
| **RAI Buddy Bot** | Supportive and encouraging AI consultant | Strict, authoritative mentor | 16 |
| **Career Kaki Bot** | Helpful and friendly career support staff | Professional, formal, and exhaustive career executive | 28 |

Two annotators independently labelled all 108 samples across 14 binary quality dimensions, with optional free-text comments per dimension.

- **Curated by:** GovTech AI Practice
- **Language(s) (NLP):** English
- **License:** MIT

---

## Annotation Schema

Each dimension is a binary classification task. Annotators select one label per dimension and may provide optional comments.

| # | Dimension | Label | Description |
|---|-----------|-------|-------------|
| 1 | Factual Correctness | `correct` | The response contains accurate, verifiable information with no factual errors |
| | | `incorrect` | The response contains factual errors, hallucinated information, or makes false claims |
| 2 | Faithfulness | `faithful` | The response stays true to the source knowledge base and does not fabricate information |
| | | `unfaithful` | The response introduces claims not supported by or contradicting the knowledge base |
| 3 | Sensibleness | `sensible` | The response makes logical sense and is a reasonable reply to the user's question |
| | | `nonsensical` | The response is illogical, irrelevant, or does not address the user's question |
| 4 | Specificity | `specific` | The response provides detailed, targeted information relevant to the user's query |
| | | `generic` | The response is vague, overly broad, or lacks actionable detail |
| 5 | Context Recall | `recalled` | The response correctly retrieves and uses relevant context from the knowledge base |
| | | `not recalled` | The response misses key information that should have been retrieved |
| 6 | Instruction Following | `followed` | The response adheres to the chatbot's defined role, guidelines, and constraints |
| | | `not followed` | The response deviates from its intended purpose or ignores system instructions |
| 7 | Bias | `biased` | The response shows unfair favoritism, stereotyping, or discriminatory language |
| | | `unbiased` | The response is neutral, fair, and does not exhibit bias |
| 8 | Coherence | `coherent` | The response is logically structured with ideas that flow naturally |
| | | `incoherent` | The response is disjointed, contradictory, or difficult to follow |
| 9 | Fluency | `fluent` | The response is grammatically correct with natural language flow |
| | | `disfluent` | The response has grammatical errors, awkward phrasing, or unnatural language |
| 10 | Empathy | `empathetic` | The response demonstrates understanding of the user's situation and tone |
| | | `not empathetic` | The response is cold, dismissive, or tone-deaf to the user's needs |
| 11 | Clarity | `clear` | The response is easy to understand and unambiguous |
| | | `unclear` | The response is confusing, ambiguous, or difficult to interpret |
| 12 | Professionalism | `professional` | The response maintains an appropriate, respectful tone for a government service |
| | | `unprofessional` | The response uses inappropriate language, slang, or an unsuitable tone |
| 13 | Structure | `well-structured` | The response is logically organized with clear formatting (e.g., lists, paragraphs) |
| | | `poorly-structured` | The response is a wall of text or lacks logical organization |
| 14 | Verbosity/Conciseness | `verbose` | The response is unnecessarily long, repetitive, or includes irrelevant information |
| | | `concise` | The response is appropriately brief while still being complete and informative |

---

## Exploratory Data Analysis

### Inter-Annotator Agreement

The two annotators achieved an overall agreement of **87.10%** across all dimensions. The table below shows per-dimension agreement:

| Dimension | Agreement |
|-----------|-----------|
| Factual Correctness | 82.41% |
| Faithfulness | 88.89% |
| Sensibleness | 97.22% |
| Specificity | 70.37% |
| Context Recall | 91.67% |
| Instruction Following | 82.41% |
| Bias | 99.07% |
| Coherence | 94.44% |
| Fluency | 86.11% |
| Empathy | 83.33% |
| Clarity | 80.56% |
| Professionalism | 96.30% |
| Structure | 84.26% |
| Verbosity/Conciseness | 82.41% |


### Label Distribution by Annotator

The chart below shows the label distribution per dimension, split by annotator. The percentage labels indicate each annotator's distribution.

![Label Distribution by Annotator](assets/label_distribution_by_annotator.png)

### Correlation Between Task Dimensions

Correlation heatmaps (split by annotator) reveal which dimensions tend to co-occur. Both annotators show minor positive correlation between Faithfulness-Context Recall, Fluency-Professionalism, and Factual Correctness-Clarity.

![Correlation by Annotator](assets/correlation_by_annotator.png)

### AIBot Label Rates

The grouped bar chart below shows the proportion of each label across task dimensions, broken down by AIBot.

![AIBot Label Rate](assets/aibot_label_rate.png)

### AIBot Quality Profiles (Radar Charts)

Radar charts show the pass rate (proportion of "good" labels) per AIBot across all 14 dimensions, providing an at-a-glance quality profile for each bot.

![Radar Pass Rate per AIBot](assets/radar_pass_rate_per_aibot.png)

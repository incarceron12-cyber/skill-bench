---
license: apache-2.0
---

# TELBench

TELBench is a 1,000-instance benchmark for span-level error localization in deep-research agent trajectories. Each instance contains a task question, ordered semantic spans, and expert-verified error span labels.

The full JSONL release is encrypted so that Hugging Face's dataset viewer does not expand the full benchmark file directly. This is not an access-control mechanism: the public release passphrase is included as `TELBench.passphrase.txt`.

## Files

- `TELBench.jsonl.enc`: AES-256-CBC encrypted TELBench JSONL file.
- `TELBench.jsonl.enc.sha256`: checksum of the encrypted file.
- `TELBench.jsonl.sha256`: checksum of the decrypted JSONL file.
- `TELBench.passphrase.txt`: public release passphrase for decryption.

## Decrypt

```bash
hf download NJU-LINK/TELBench \
  --repo-type dataset \
  --local-dir data \
  --include "TELBench.jsonl.enc" \
  --include "TELBench.jsonl.enc.sha256" \
  --include "TELBench.jsonl.sha256" \
  --include "TELBench.passphrase.txt"

export TELBENCH_PASSPHRASE="$(cat data/TELBench.passphrase.txt)"
openssl enc -d -aes-256-cbc -pbkdf2 -iter 200000 \
  -in data/TELBench.jsonl.enc \
  -out data/TELBench.jsonl \
  -pass env:TELBENCH_PASSPHRASE
(
  cd data
  shasum -a 256 -c TELBench.jsonl.sha256
)
```

## JSONL Format

Each line is one trajectory-level instance:

```json
{
  "id": "0001",
  "source_id": "traj_...",
  "question": "...",
  "spans": [
    {
      "id": "s001",
      "raw": "original semantic span text"
    }
  ],
  "gold": {
    "error_span_ids": ["s008"]
  },
  "meta": {
    "bench": "gaia",
    "difficulty": "easy",
    "framework": "miroflow",
    "model": "gaia-val-gemini25pro",
    "answer_status": "correct"
  },
  "annotations": {
    "stage": {"s001": "retrieve"},
    "error_type": {"s008": "constraint_semantics_error"}
  }
}
```

## Evaluation Input Policy

For DRIFT and baseline evaluation, model calls receive only the task question and ordered raw span text. Gold labels, annotations, metadata, judge results, span types, and manual notes are not passed to the model.

## Paper

See  arxiv.org/abs/2606.02060

## Code

The DRIFT runner and project page are available at: https://github.com/NJU-LINK/DRIFT

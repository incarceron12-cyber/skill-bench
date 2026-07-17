---
license: mit
base_model:
- Qwen/Qwen3-4B
pipeline_tag: text-classification
---

<div align="center">
  <img src="https://raw.githubusercontent.com/OpenHands/docs/main/openhands/static/img/logo.png?raw=true" alt="Logo" width="200">
  <h1 align="center">OpenHands Critic 4B v1.0</h1>
</div>

<p align="center">
<a href="https://arxiv.org/abs/2603.03800">Paper</a> •
<a href="https://github.com/OpenHands/critic-rubrics">Github (definitions & prompts)</a> <br>
</p>

A 4B parameter critic model for evaluating AI agent trajectories, trained to predict behavioral rubrics and task success.


- Docs (Use it in OpenHands Software Agent SDK): https://docs.openhands.dev/sdk/guides/critic
- Docs (Use it in OpenHands CLI): https://docs.openhands.dev/openhands/usage/cli/critic

## Model Details

- **Base Model**: Qwen/Qwen3-4B
- **Training**: Full-parameter fine-tuning with BCE loss
- **Context Length**: Trained on 64K, supports up to 256K tokens
- **Task**: Multi-label classification (26 labels: 25 rubric features + 1 success prediction)

## Serving (vLLM Classification API)

We serve this model using vLLM’s classification task:

```bash
vllm serve <MODEL_PATH> \
  --host 0.0.0.0 \
  --port 8000 \
  --api-key <API_KEY> \
  --served-model-name <MODEL_NAME> \
  --task classify \
  --max-model-len 262144 \
  --dtype bfloat16 \
  --trust-remote-code \
  --enable-prefix-caching
```

## Usage

We recommend using the **OpenHands SDK** for inference instead of calling the vLLM classification endpoint directly.

Follow the SDK guide: https://docs.openhands.dev/sdk/guides/critic

In particular, reuse the SDK client implementation here (it already handles formatting and API calls): https://github.com/OpenHands/software-agent-sdk/blob/main/openhands-sdk/openhands/sdk/critic/impl/api/critic.py

At a high level, you will:
1. Start a critic server (see **Serving** section above)
2. Configure the SDK to point to your critic endpoint + API key
3. Call the SDK critic to score trajectories (returns rubric probabilities + success score)

## Citation

```bibtex
@misc{wang2026rubricsupervisedcriticsparserealworld,
      title={A Rubric-Supervised Critic from Sparse Real-World Outcomes},
      author={Xingyao Wang and Valerie Chen and Heng Ji and Graham Neubig},
      year={2026},
      eprint={2603.03800},
      archivePrefix={arXiv},
      primaryClass={cs.AI},
      url={https://arxiv.org/abs/2603.03800},
}
```
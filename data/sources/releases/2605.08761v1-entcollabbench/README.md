---
configs:
  - config_name: approval_multi_tasks
    data_files: "approval_multi_task_20.json"
  - config_name: approval_tasks
    data_files: "approval_tasks_80.json"
  - config_name: mcp_multi_tasks
    data_files: "mcp_multi_tasks_40.json"
  - config_name: mcp_tasks
    data_files: "mcp_tasks_160.json"
---

# EntCollabBench

EntCollabBench is a benchmark dataset for evaluating **enterprise-oriented multi-agent collaboration**. It focuses on realistic workplace task execution where an entry agent must complete user requests by using tools, interacting with enterprise systems, and delegating subtasks to specialized peer agents when needed.

The dataset is designed for benchmarking agent systems that operate in a simulated enterprise environment with role separation, service boundaries, approval workflows, and observable side effects.

![EntCollabBench overview](./overview.png)


## Dataset Summary

EntCollabBench contains four task files and two supporting resource archives:

- `mcp_tasks_160.json`: 160 single-task samples centered on enterprise MCP tool use.
- `mcp_multi_tasks_40.json`: 40 multi-step or multi-subtask collaboration samples.
- `approval_tasks_80.json`: 80 approval-oriented tasks requiring document-grounded decisions.
- `approval_multi_task_20.json`: 20 multi-subtask approval and coordination tasks.
- `seed.zip`: seed data used to initialize the simulated enterprise services.
- `local_data.zip`: local approval documents and policy materials used by approval agents.

In total, the benchmark includes **300 tasks**:

- 200 MCP-oriented tasks
- 100 approval-oriented tasks

Depending on file format, one task batch may contain either:

- a single task, or
- multiple subtasks grouped under one `task_id`

## Supported Research Uses

This dataset is intended for research on:

- multi-agent task decomposition and delegation
- tool-use in structured enterprise environments
- cross-role collaboration under access constraints
- approval reasoning grounded in local policy documents
- trajectory-based evaluation of agent workflows
- benchmarking end-to-end operational success, not just final text quality

## Data Fields

Common fields appearing across files include:

- `task_id`: unique identifier for a task batch
- `description`: optional natural language description of the batch
- `task`: task instruction for single-task samples
- `target_agent`: initial agent for single-task samples
- `sub_task_list`: list of subtasks in multi-task samples
- `sub_task_id`: unique identifier for a subtask within a batch
- `user_prompt`: user-facing instruction for a subtask
- `beginning_agent`: initial agent assigned to the subtask
- `ground_truth`: optional structured reference actions or expected tool-use path
- `state_export`: optional specification for evaluating state changes in enterprise services

The benchmark code normalizes several legacy aliases, including:

- `task` or `user_prompt`
- `target_agent`, `begin_agent`, or `beginning_agent`
- `sub_task_list` or `task_list`

## Agent Roles

The benchmark environment uses specialized enterprise agents, including:

- `it_service_desk_l1`
- `it_change_engineer`
- `hr_service_specialist`
- `customer_support_specialist`
- `knowledge_base_specialist`
- `collaboration_ops_specialist`
- `developer_engineer`
- `qa_test_engineer`
- `finance_approval_specialist`
- `legal_approval_specialist`
- `procurement_approval_specialist`

These agents operate under role-specific tool and responsibility boundaries.

## Enterprise Service Domains

Tasks may involve one or more simulated enterprise systems, including:

- `calendar`
- `csm`
- `drive`
- `email`
- `gitea`
- `hr`
- `itsm`
- `teams`

Approval tasks additionally rely on local policy and submission documents supplied through `local_data.zip`.

## Example Use

### Load a task file

```python
import json

with open("mcp_tasks_160.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(type(data))
print(data[0] if isinstance(data, list) else data)
```

## Additional Resources

### `seed.zip`

Contains seed artifacts used to initialize the simulated enterprise backend services. These resources are required for reproducing the interactive environment used by the benchmark.

### `local_data.zip`

Contains local rulebooks and policy documents for approval specialists, such as finance, legal, and procurement approval materials.

Representative document categories include:

- finance policies
- legal and privacy policies
- procurement and vendor policies

These materials are used as local workspace evidence during approval evaluation.

## Citation

If you use EntCollabBench in your research, please cite:

```bibtex
@misc{yu2026allinoneagentbenchmarkingrolespecialized,
      title={Beyond the All-in-One Agent: Benchmarking Role-Specialized Multi-Agent Collaboration in Enterprise Workflows}, 
      author={Tao Yu and Hao Wang and Changyu Li and Shenghua Chai and Minghui Zhang and Zhongtian Luo and Yuxuan Zhou and Haopeng Jin and Zhaolu Kang and Jiabing Yang and YiFan Zhang and Xinming Wang and Hongzhu Yi and Zheqi He and Jing-Shu Zheng and Xi Yang and Yan Huang and Liang Wang},
      year={2026},
      eprint={2605.08761},
      archivePrefix={arXiv},
      primaryClass={cs.MA},
      url={https://arxiv.org/abs/2605.08761}, 
}
```



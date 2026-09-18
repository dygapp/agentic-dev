---
id: eval:rule-discovery-v4
type: eval-guide
status: active
---

# V4 Rule Discovery Evals

本目录验证 V4 中必须由模型参与的规则发现行为，以及 Rule 总量增长时 ordinary-runtime context 是否保持候选级增长；不重复证明普通代码已经保证的 schema / deterministic matching。

## V4-06 — Discriminating

Corpus：

`v4-discriminating.json`

覆盖 Fresh Context 首次 communication 输出激活、generation、verification、mixed responsibility、negative / ambiguity、invalid metadata fail-closed、Skill vs Rule 与 Consumer-local ordinary runtime。

运行：

```bash
python3 evals/run_codex_evals.py --discovery
```

单场景：

```bash
python3 evals/run_codex_evals.py --discovery --scenario D-V4-GEN-01
```

Runtime 只得到当前 Repository Authority、Rule Discovery Tool、current Rules、current Skills 与场景输入；corpus、`expected_behavior`、`assertions` 和历史结果不进入 workspace。最终评分必须检查 task signals、真实 discovery、candidate-only Rule reads、semantic confirmation、re-discovery、fail-closed、Skill/Rule 与 Consumer-local 边界。

## Token Scaling

Corpus：

`v4-scaling.json`

同一个 Vue implementation task 分别运行在精确 20 / 100 / 500 Rule workspace 中。每个 workspace 固定相同 **2 条任务级真实匹配 Rule**：implementation discipline 与 Vue component authoring；其余为 metadata 合法但在稳定 phase boundary 上不匹配的 synthetic decoys。

这组 fixture 同时验证本次 granularity consolidation：原场景需要加载 4 条碎片 Rule，现在在保持规范语义的前提下只需要 2 条任务级 Rule。

运行全部 scaling 场景：

```bash
python3 evals/run_v4_scaling.py
```

单场景：

```bash
python3 evals/run_v4_scaling.py --scenario S-V4-100
```

Runner 在每次 Fresh Runtime 前做 deterministic fixture preflight，并把以下信息写入 `evals/results/scaling/<scenario>.run.json`：

- exact `source_commit`；
- Codex CLI version；
- fixture `rule_count`；
- deterministic `scanned` / candidate IDs；
- Codex `turn.completed` token usage；
- stdout byte count 与 process return code。

人工评分必须确认：

- 三个规模使用等价 task / prompt / canonical signals；
- `scanned` 精确为 20 / 100 / 500，但 candidate IDs 恒为同一 2 条；
- Rule locator 只来自 discovery output；
- runtime 只读取 2 条候选正文，不枚举/读取任何 decoy locator / metadata / body；
- semantic conclusion 在三种规模下等价；
- LLM input-token / trace-context 不随 N 呈近似线性增长。

目标复杂度：

```text
Tool side: O(N metadata scan/filter)
LLM side: O(k locator + k rule body), k = 2 << N
```

## 判定边界

`returncode == 0` 只表示 Codex 进程完成，不表示 Eval PASS。Discovery 与 scaling eval 都必须结合 JSONL trace、run metadata 与最终回答做人工语义评分。

运行结果位于：

- `evals/results/discovery/`
- `evals/results/scaling/`

两者均为临时评估证据，不进入 current Authority。
---
id: eval:index
type: eval-guide
status: active
---

# Evals

本目录保存 `agentic-dev` 可执行评估语料、fixture 与 runner。它们提供验证证据，不属于 Repository Authority，也不因为历史 PASS 自动证明 V4 当前行为。

## 1. 基本原则

每个 Runtime Eval 必须：

- 使用 Fresh / isolated context；
- 不让被评模型读取 expected answer、assertions、历史结果或评分材料；
- 区分进程成功与语义 PASS；
- 对需要人工判断的 assertion 逐项评分；
- 只复用能够证明不受当前变更影响的历史证据；
- Skill / Rule / Discovery contract 发生实质变化后，对受影响行为重新取得 current evidence。

## 2. 当前目录

### Skill activation / behavior

- `activation/core-first-pass.json`：Skill metadata activation 历史与迁移语料；
- `behavior/*.json`：现有 Method / platform Skill 的行为语料；
- `run_codex_evals.py`：Skill / capability 隔离运行器。

V4 重写了 Skill metadata 与多个 Skill body，并新增 `external-operation` / `review-change`。因此旧行为结果不是 V4 PASS；V4-06 必须更新受影响 corpus，并为 supporting Skills 建立有辨识力的行为评估。

### Capability / technology

- `capability/vue3-typescript-profile.json`：旧 monolithic profile 评估输入。

V4 已拆除 Technology Profile runtime owner；V4-06 应把该语料改写为 technology-rule / Rule Discovery 判别场景，不再以整份 profile 作为普通上下文。

### Governance

- `governance/*.json`：语言、正式概念、方法对象与 stacked PR 等历史治理回归语料；
- `run_governance_evals.py`：对应隔离运行入口。

只有仍映射到 current Rule / Skill / Authority 的场景才继续作为 V4 regression asset；失去 current owner 的场景应删除或重写。

### Rule retrieval historical evidence

- `rule-retrieval/targeted-evaluation-design.json`；
- `rule-retrieval/c3-human-scoring.json`。

它们是 v1/v2 稀疏检索的 frozen historical evidence，不是 V4 current Rule Discovery corpus。V4 新的 discovery / scaling eval 必须建立独立 current 场景，不能把旧 rule-index / Manifest 期望键解释为 V4 Rule IDs。

### Fixtures

`fixtures/execute-unit-basic/` 是行为评估输入。Fixture 内容属于测试数据，不是 current repository resource / Authority；不得为了文档治理机械改变其语义。

## 3. V4 后续评估责任

### V4-04

为 Rule Discovery Tool 建立确定性单元测试：schema、duplicate id、invalid signals、fail-closed、candidate output 等。

### V4-06

至少覆盖：

- Generation Rule Discovery；
- Verification Rule Discovery；
- mixed implementation + verification；
- irrelevant Rule exclusion；
- invalid metadata / ambiguity fail-closed；
- Skill / Rule boundary；
- rewritten Skills 的受影响行为。

### V4-07

用同一任务在 20 / 100 / 500 rules 下验证：

```text
Tool scan cost may grow with N
LLM discovery context must depend on k, not N
k << N
```

不得用“最终任务完成”代替 token-scaling 验收。

### V4-08

Consumer validation 必须在 Consumer 自己的 Fresh Context / Repository Authority 下执行；本仓只接收 Evidence，不直接取得 Consumer Execute Authority。

## 4. 执行说明

低频 Codex CLI 运行方式见 `evals/CODEX.md`。生成的 `evals/results/` 与 `evals/workspace/` 不是 Authority，并由 `.gitignore` 排除。
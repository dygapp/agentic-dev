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

### V4 Rule Discovery

- `discovery/v4-discriminating.json`：V4-06 current 判别语料；
- `discovery/README.md`：运行与评分边界；
- `run_codex_evals.py --discovery`：Fresh Runtime 入口。

Runtime workspace 只得到当前 runtime entry、Rule Discovery Tool、Rules、Skills 与场景输入，不得到 corpus 本身、expected behavior、assertions 或历史 results。

### Skill activation / behavior

- `activation/core-first-pass.json`：Skill metadata activation 历史与迁移语料；
- `behavior/*.json`：Method / platform Skill 历史行为语料；
- `run_codex_evals.py`：统一隔离 runner。

V4 已重写多个 Skill body / metadata，并新增 supporting Skills；历史结果只能作为回归输入，不能自动成为 V4 current PASS。V4-06 当前只在 `Skill vs Rule` 场景验证发现层边界，不把旧 Skill corpus 全量重跑混入 Rule Discovery Gate。

### Capability / technology

- `capability/vue3-typescript-profile.json`：旧 monolithic profile 的历史评估输入。

V4 已拆除 Technology Profile runtime owner；普通运行时使用 `docs/rules/technology/**`。旧 capability corpus 不作为 V4 current discovery evidence。

### Governance

- `governance/*.json`：语言、正式概念、方法对象与 stacked PR 等历史治理回归语料；
- `run_governance_evals.py`：对应隔离运行入口。

只有仍映射到 current Rule / Skill / Authority 的场景才继续作为 V4 regression asset。

### Rule retrieval historical evidence

- `rule-retrieval/targeted-evaluation-design.json`；
- `rule-retrieval/c3-human-scoring.json`。

它们是 v1/v2 稀疏检索的 frozen historical evidence，不是 V4 current Rule Discovery corpus。旧 rule-index / Manifest 期望键不得解释为 V4 Rule IDs。

### Fixtures

`fixtures/execute-unit-basic/` 是历史行为评估输入。Fixture 内容属于测试数据，不是 current repository resource / Authority；不得为了文档治理机械改变其语义。

## 3. 当前 Gate 责任

### V4-04 — PASS

Rule Discovery Tool 的 schema、duplicate id、invalid signals、fail-closed、candidate output 等确定性责任由普通自动化测试承担。

### V4-06 — CURRENT

当前 7 类场景：

- Generation Rule Discovery；
- Verification Rule Discovery；
- mixed implementation + external operation + verification；
- negative / ambiguity；
- invalid metadata fail-closed；
- Skill / Rule boundary；
- Consumer-local ordinary runtime。

V4-06 只在实际 Fresh Runtime trace + 人工逐 assertion 评分后才能 PASS；runner/corpus 静态有效或进程退出 0 都不等于语义通过。

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

Codex CLI 隔离运行方式见 `evals/CODEX.md`。生成的 `evals/results/` 与 `evals/workspace/` 不是 Authority，并由 `.gitignore` 排除。
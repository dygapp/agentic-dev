---
id: eval:index
type: eval-guide
status: active
distribution: source-only
---

# Evals

本目录保存 `agentic-dev` 当前仍有复用价值的可执行评估语料、fixture 与 runner。Evals 提供验证证据，不属于 Repository Authority；历史 PASS 也不会自动证明当前 Method / Skill / Rule / Rule Discovery 行为。

## 1. 运行原则

每个 Runtime Eval 必须：

- 使用 Fresh / isolated context；
- 不让被评模型读取 expected answer、assertions、历史结果或评分材料；
- 区分进程成功与语义 PASS；
- 对需要人工判断的 assertion 逐项评分；
- Skill / Rule / Discovery contract 发生实质变化后，对受影响行为重新取得 current evidence。

## 2. 当前清单

### V4 Rule Discovery

- `discovery/v4-discriminating.json`：生成、验证、mixed responsibility、ambiguity、invalid metadata、Skill / Rule boundary 与 Consumer-local ordinary runtime 的判别语料；
- `discovery/v4-scaling.json`：20 / 100 / 500 Rules token-scaling 语料；
- `discovery/README.md`：运行与评分边界；
- `run_codex_evals.py --discovery`：V4 判别 Fresh Runtime 入口；
- `run_v4_scaling.py`：V4 scaling 入口。

Runtime workspace 只得到当前 runtime entry、Rule Discovery Tool、current Rules、current Skills 与场景输入，不得到 corpus 本身、expected behavior、assertions 或历史 results。

旧 monolithic Technology Profile capability eval 与 v1/v2 rule-retrieval 实验已经被 V4 Rule Discovery / technology Rules 取代，不再保留在 current tree；历史证据由 Git / Issue 保存。

### Skill activation / behavior

- `activation/core-first-pass.json`：canonical Skill activation 回归语料；
- `behavior/*.json`：仍对应 current Skills 的行为回归语料；该目录中的 current JSON 由 runner 机械发现，不维护第二份手工注册列表；
- `run_codex_evals.py`：统一隔离 runner；activation / behavior 直接复制 canonical `skills/**` 到临时 Consumer `.agents/skills/**`，绑定 clean exact HEAD + Skill-set digest，并对单场景执行有界 timeout / stale-evidence cleanup；`--scenario` 必须属于当前选择的 mode。

这些历史语料只作为 targeted regression input；不得把旧运行结果直接扩大为当前 PASS。

### Governance

- `governance/*.json`：仍映射到 current Rule / Authority 的语言、正式概念、方法对象和仓库治理回归语料；
- `run_governance_evals.py`：对应隔离运行入口。

### Fixtures

`fixtures/execute-unit-basic/` 是行为评估输入。Fixture 属于测试数据，不是 current repository Authority；不得为了 current-resource 文档治理机械改写其语义。

## 3. V4 证据状态

- V4-04 deterministic Rule Discovery contract：PASS；由普通自动化测试与 lint 持有；
- V4-06 Discriminating Evals：PASS；7 / 7 Fresh Runtime 场景与 35 / 35 assertions 通过；
- V4-07 Token Scaling：PASS；20 / 100 / 500 Rules 下 candidate set 固定且 LLM discovery context 未随 N 近似线性增长；
- V4-08 Consumer Validation：PASS；真实 Consumer adoption / local projection / generation / verification / post-adoption decoupling 已取得证据，自然 Rule Evolution 保留为 post-adoption observation gap；
- V4-09 不新增新的模型行为 Gate；Closure 只清理 superseded current-tree assets，并确认最终 baseline surface 与已有证据一致。

完整阶段证据由 Issue #122、PR #123、Git 与 Actions 持有，不在本文件复制实验流水账。

## 4. 执行说明

Codex CLI 隔离运行方式见 `evals/CODEX.md`。生成的 `evals/results/` 与 `evals/workspace/` 不是 Authority，并由 `.gitignore` 排除。

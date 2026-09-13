---
id: project:roadmap
type: project
status: active
---

# Project Roadmap

## Current Foundation Rebuild

当前项目处于 **V4 — 分布式规则发现与仓库基础重构**。

Frozen V3 locator：

`agentic-dev@1c8cdfea9ecf23ef33ffab20eec3c93679fd4578`

V4 是断代式、减法优先 Foundation Rebuild，不维护 V1～V3 current working-tree compatibility layer。过程设计、分类、实验与阶段证据主要由 Issue #122、PR、Git 与 Actions 持有；本 Roadmap 只保留当前阶段与稳定下一 Gate。

## Current Runtime Target

```text
current task / repository facts
→ bounded task signals
→ Rule Discovery Tool
→ scan Rule YAML Front Matter
→ deterministic candidate filtering
→ {id, path} locators
→ LLM reads only candidate bodies
→ semantic applicability confirmation
```

核心约束：

- Rule metadata 与正文同文件维护；
- 不维护 Reviewed Discovery Map / Activation Manifest / Runtime Catalog / rule-index；
- Rule Discovery 返回的 `candidates[]` 是 ordinary runtime 获得 Rule locator 的唯一入口；
- 未命中 Rule locator / metadata / body 不进入普通 LLM context；
- Skill 只承担稳定独立执行闭环；
- Guide 只承担面向人的低频说明；
- current project state 不为每个 Gate 创建长期 Markdown；
- fixture / frozen eval input 属于测试数据，不因 current-resource metadata 治理被机械改写。

## Gates

- V4-00 Baseline Freeze & Rebuild Boundary — PASS
- V4-01 Asset Inventory & Classification — PASS
- V4-02 Front Matter & Rule Discovery Contract — PASS
- V4-03 Information Architecture & Rule Decomposition — PASS
- V4-04 Rule Discovery Tool & Lint — PASS
- V4-05 Runtime Integration — PASS
- V4-06 Generation / Verification Discriminating Evals — PASS
- V4-07 Token Scaling Gate（20 / 100 / 500 rules）— CURRENT
- V4-08 Consumer Validation — PENDING
- V4-09 Closure & Baseline Replacement — PENDING

Gate 编号不是自动推进授权；每一 Gate 先验证上一 Gate Completion Conditions。

## V4-06 Completion State

V4-06 已通过三轮 Fresh Runtime 收敛：

- 首轮暴露 canonical task-signal 不稳定、synonym probing 与未命中 metadata 反向探测；
- 第二轮显式 assertions 通过，但暴露完整 Rule locator 枚举导致 LLM context 随 N 增长；
- contract 随证据收敛为 bounded known / known-empty / unknown signals，以及 locator-only progressive disclosure；
- 第三轮基于 `395c803987667180a258d8ce8f51136ab64ad325`、Codex CLI `0.154.0`，7/7 场景、35/35 assertions 与 locator-only protocol 全部 PASS。

详细过程证据由 Issue #122 持有；本 Roadmap 不复制完整评分流水账。

## Current Gate — V4-07

V4-07 验证规则总量增长时，Rule Discovery 是否真正把规模成本留在 Tool side，而不是重新进入 LLM context。

必须对**同一任务**构造至少以下三种 Rule 规模：

```text
20 rules
100 rules
500 rules
```

门禁：

- 每个规模下都扫描精确 N 条 Rule metadata；
- task / prompt / canonical signals 保持等价；
- 目标候选集合与候选正文保持等价，召回不因 N 增长漂移；
- 全量 metadata 与未命中 locator 只由 Tool 处理，不进入 LLM context；
- LLM discovery context 只由固定 task/query、`k` 个 candidate locators 与 `k` 个 candidate bodies 构成；
- 输入 token / trace context 不得因 N 从 20 → 100 → 500 出现与 N 同阶的增长；
- 允许本地 metadata scan/filter CPU / I/O 随 N 线性增长。

目标复杂度：

```text
Tool side: O(N metadata scan/filter)
LLM side: O(k locator + k rule body), k << N
```

V4-07 必须同时取得 deterministic fixture / candidate invariance 证据与 Fresh Runtime token / trace 证据。只有 scaling Gate PASS 后才进入 V4-08 Consumer Validation。

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
- V4-07 Token Scaling Gate（20 / 100 / 500 rules）— PASS
- V4-08 Consumer Validation — CURRENT
- V4-09 Closure & Baseline Replacement — PENDING

Gate 编号不是自动推进授权；每一 Gate 先验证上一 Gate Completion Conditions。

## V4-06 Completion State

V4-06 已通过三轮 Fresh Runtime 收敛：

- 首轮暴露 canonical task-signal 不稳定、synonym probing 与未命中 metadata 反向探测；
- 第二轮显式 assertions 通过，但暴露完整 Rule locator 枚举导致 LLM context 随 N 增长；
- contract 随证据收敛为 bounded known / known-empty / unknown signals，以及 locator-only progressive disclosure；
- 第三轮基于 `395c803987667180a258d8ce8f51136ab64ad325`、Codex CLI `0.154.0`，7/7 场景、35/35 assertions 与 locator-only protocol 全部 PASS。

详细过程证据由 Issue #122 持有；本 Roadmap 不复制完整评分流水账。

## V4-07 Completion State

V4-07 已验证同一任务在 20 / 100 / 500 Rules 三种规模下的真实 Fresh Runtime scaling：

- 三个 fixture 分别精确扫描 20 / 100 / 500 条 Rule metadata；
- 三种规模都只返回同样 4 条候选：`implementation-minimality`、`surgical-change`、`vue-define-model-default`、`vue-props-one-way-input`；
- Runtime 只读取这 4 条候选正文，无 synthetic decoy locator、未命中 Rule metadata/body 或目录枚举进入模型上下文；
- 100 → 500 Rules 增长 5 倍时，总 input tokens `88,673 → 88,556`（-0.13%），uncached input `12,769 → 12,780`（+0.09%），stdout bytes `25,791 → 25,545`（-0.95%）；
- 20 → 500 Rules 增长 25 倍时，uncached input 仅 `12,198 → 12,780`（+4.77%）；20-rule 运行的总 token 差异可由不同 bootstrap/tool-call grouping 解释，trace 没有显示额外 Rule context 泄漏。

因此当前证据直接排除了“LLM discovery context 随 Rule 总量 N 近似线性增长”的失败条件，并支持：

```text
Tool side: O(N metadata scan/filter)
LLM side: O(k locator + k rule body), k=4 << N
```

详细 scaling 表与 trace 结论记录于 Issue #122。

## Current Gate — V4-08

V4-08 在不修改 Consumer 产品语义的前提下，用真实 Consumer 验证：

- baseline adoption；
- Consumer-local rule projection；
- ordinary generation discovery；
- ordinary verification discovery；
- 后续规则新增 / 修改时无需同步中心 Map；
- upstream 演进与 Consumer ordinary runtime 解耦。

Consumer 修改必须在 Consumer 自己的 Repository Authority / 会话中完成；`agentic-dev` 当前会话不得越界直接修改 Consumer。V4-08 的下一实际动作是建立 Consumer-side Fresh Context 验证入口，在 Consumer 仓库中按其当前 Repository Authority 执行 adoption / local projection / ordinary runtime validation，并把可复核 Evidence 反馈回 Issue #122。

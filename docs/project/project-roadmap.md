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
→ task signals
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
- V4-05 Runtime Integration — CURRENT
- V4-06 Generation / Verification Discriminating Evals
- V4-07 Token Scaling Gate（20 / 100 / 500 rules）
- V4-08 Consumer Validation
- V4-09 Closure & Baseline Replacement

Gate 编号不是自动推进授权；每一 Gate 先验证上一 Gate Completion Conditions。

## V4-04 Completion State

V4-04 已取得当前执行证据：

- Rule Discovery Tool 只扫描 Rule Front Matter，并稳定输出 `{id, path}` locator；
- deterministic test suite：23 / 23 PASS；
- repository lint：45 Rules / 11 Skills / 33 current Markdown resources PASS；
- generation CLI smoke 扫描 45 条 Rule，仅返回 2 个 candidates；
- malformed metadata、duplicate id、invalid signals、incomplete scan 等失败路径均 fail closed；
- 当前实现不维护人工同步的中心 Rule Map / Manifest / Catalog。

## Current Gate — V4-05

把普通运行时真正收敛为：

```text
Task / repository facts
→ extract current task signals
→ Rule Discovery prefilter
→ read candidate Rule bodies only
→ semantic applicability confirmation
→ execute current Skill / responsibility
```

V4-05 必须保持：

- AGENTS / README / Skills 只有最小稳定发现入口，不复制 Rule index；
- task phase / activity / technology / artifact / risk facts 发生实质变化时重新发现，不跨职责永久复用旧 candidates；
- Discovery `fail-closed` 时停止依赖其结果并修复当前输入 / metadata，不降级到旧中心发现路径；
- Skill 原生发现与 Rule Discovery 保持独立；
- ordinary runtime 不加载全量 Rule metadata / body，也不恢复 V1～V3 discovery assets。

完成 V4-05 后才进入 V4-06 判别性运行评估。
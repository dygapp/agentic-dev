---
id: project:roadmap
type: project
status: active
---

# Project Roadmap

## Current Foundation Rebuild

当前项目进入 **V4 — 分布式规则发现与仓库基础重构**。

Frozen V3 locator：

`agentic-dev@1c8cdfea9ecf23ef33ffab20eec3c93679fd4578`

V4 是断代式、减法优先 Foundation Rebuild，不维护 V1～V3 current working-tree compatibility layer。过程设计、分类、实验与阶段证据主要由 Issue #122、PR、Git 与 Actions 持有；本 Roadmap 只保留当前阶段与稳定下一 Gate。

## Current Goal

建立如下普通运行模型：

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
- current project state 不为每个 Gate 创建长期 Markdown。

## Gates

- V4-00 Baseline Freeze & Rebuild Boundary — PASS
- V4-01 Asset Inventory & Classification — PASS
- V4-02 Front Matter & Rule Discovery Contract — PASS
- V4-03 Information Architecture & Rule Decomposition — CURRENT
- V4-04 Rule Discovery Tool & Lint — pending V4-03 completion
- V4-05 Runtime Integration
- V4-06 Generation / Verification Discriminating Evals
- V4-07 Token Scaling Gate（20 / 100 / 500 rules）
- V4-08 Consumer Validation
- V4-09 Closure & Baseline Replacement

Gate 编号不是自动推进授权；每一 Gate 先验证上一 Gate Completion Conditions。

## V4-03 Completion Target

- current Rules 已完成原子化并拥有 frozen Front Matter contract；
- Skill / Rule / Guide 边界已按实际职责落地；
- 旧 V1～V3 project/discovery/profile/task surfaces 已退出 current tree；
- Method / Architecture / Guide 已改写为最终 current owner；
- 最终保留 Markdown 都具备对应 Front Matter；
- `docs/project/` 只保留本 Roadmap；
- 不存在为了历史兼容保留的中心发现映射。

V4-03 通过后，下一实际 Gate 是 V4-04：实现 `tools/rule-discovery/`、严格 schema lint、deterministic candidate filtering 与 fail-closed tests。
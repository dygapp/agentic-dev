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
- V4-04 Rule Discovery Tool & Lint — CURRENT
- V4-05 Runtime Integration
- V4-06 Generation / Verification Discriminating Evals
- V4-07 Token Scaling Gate（20 / 100 / 500 rules）
- V4-08 Consumer Validation
- V4-09 Closure & Baseline Replacement

Gate 编号不是自动推进授权；每一 Gate 先验证上一 Gate Completion Conditions。

## V4-03 Completion State

V4-03 已完成：

- current runtime Rules 已拆为独立 Markdown 单元并使用 frozen Front Matter contract；
- 11 个 Skill 按独立闭环重新收敛，其中 `external-operation` / `review-change` 从旧聚合文档提升；
- Guide 只保留人类 adoption / upgrade / recovery 说明；
- V1～V3 project/discovery/profile/task/decision surfaces 已退出 current tree；
- `docs/project/` 只保留本 Roadmap；
- Research 只保留非权威技术证据，并退出旧 current-owner 叙述；
- 旧聚合 runtime Guide 与 orphan Skill reference 已删除；
- current resource Markdown 使用 V4 Front Matter；`SKILL.md` 使用 Agent Skills-compatible metadata extension；eval fixture Markdown 作为测试数据保留原语义。

## Current Gate — V4-04

实现 `tools/rule-discovery/` 与严格 lint：

- metadata scan；
- task-signal validation；
- deterministic candidate filtering；
- stable `{id,path}` output；
- duplicate / malformed / invalid-state / incomplete-scan fail-closed；
- current Markdown / Rule / Skill metadata lint；
- 自动化测试覆盖 Generation / Verification 代表场景和失败路径。

V4-04 通过后再进入 Runtime Integration；不得以工具“能运行”代替 V4-06/V4-07 的判别能力与 token-scaling 验收。
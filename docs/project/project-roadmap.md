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
- V4-05 Runtime Integration — PASS
- V4-06 Generation / Verification Discriminating Evals — CURRENT
- V4-07 Token Scaling Gate（20 / 100 / 500 rules）
- V4-08 Consumer Validation
- V4-09 Closure & Baseline Replacement

Gate 编号不是自动推进授权；每一 Gate 先验证上一 Gate Completion Conditions。

## V4-05 Completion State

V4-05 已完成 ordinary runtime 切换：

- `AGENTS.md` 持有稳定 CLI、五维 task signal、semantic confirmation、re-discovery 与 fail-closed 边界；
- Rule Discovery Architecture 持有 ordinary runtime lifecycle；
- README / Skills 只保留薄入口，不复制 Rule index；
- 11 个 Skill 已回归清点并退出旧 V3 Discipline / central-discovery 依赖；
- Reviewed Discovery Map 与被替代运行路径不存在于 current tree；
- 当前 Head 的 deterministic tests、resource lint 与 discover smoke 均通过。

## Current Gate — V4-06

建立能够区分“工具能运行”和“Agent 能正确发现并应用规则”的运行时评估，至少覆盖：

1. generation discovery；
2. verification discovery；
3. generation + external operation + verification mixed task；
4. negative / ambiguity 与 fail-closed；
5. metadata drift / invalid resource；
6. Skill vs Rule 边界；
7. Consumer-local ordinary runtime 不依赖 upstream current state。

V4-06 必须使用 Fresh Runtime、隔离 expected behavior / assertions，并由人工语义判分；进程成功、候选数量或静态测试通过均不能替代行为结论。
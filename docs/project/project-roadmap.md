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
- V4-06 Generation / Verification Discriminating Evals — CURRENT / REWORK
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

V4-06 验证“Agent 能正确发现并应用规则”，覆盖 generation、verification、mixed responsibility、negative / ambiguity、invalid metadata、Skill vs Rule 与 Consumer-local ordinary runtime。

### First Fresh Runtime result

首轮 Fresh Runtime 基于：

`60dfb3bb97f937d329f198bab78c20a6f29e39f0`

Codex CLI：`0.154.0`。7/7 场景结果完整，全部进程正常退出且 stderr 为空，但**语义 Gate 未通过**：原始 assertion 约 30/35 通过，只有 negative / ambiguity 与 invalid metadata 两个场景达到 clean PASS。

主要失败不是最终业务结论错误，而是 discovery protocol 出现系统性缺陷：

- runtime 缺少稳定 task-token 规范化边界，出现大量同义词 / 推测风险碰撞；
- `generation` 与 `Skill vs Rule` 因 canonical token 不一致产生 false negative；
- mixed / Consumer-local 场景读取未返回 Rule 的 Front Matter 反向校准 signals，破坏 `prefilter → candidate-only read` 边界；
- verification 最终判断正确，但依赖大规模 synonym probing 才命中目标 Rule。

因此 V4-06 首轮结论为 **FAIL**，不得进入 V4-07。

### Current rework

V4-06 内部按证据修订 task-signal contract：

- task-side 五维值采用三态：非空数组 = known；`[]` = known-empty；`null` = unknown / unsafe-to-canonicalize；
- unknown 维度不用于排除 Rule，避免为了精确 metadata 猜 taxonomy；
- 每个非空维度最多 6 个 lowercase kebab-case token，禁止 synonym cloud；
- Method phase 与常见 technology / artifact machine identity 提供稳定规范化入口，但不建立 Rule→token 映射表；
- `status=ok` 且候选为空时，不允许读取未命中 Rule Front Matter / body 反向校准；
- eval corpus 明确把这种反向探测判为协议失败；
- Consumer-local fixture 同步采用相同 signal contract。

当前 rework 必须先通过 deterministic CI，再在新的精确 Head 上重新执行全部 7 个 Fresh Runtime 场景和人工逐 assertion 评分。只有 rerun clean PASS 后才可进入 V4-07。
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

### Second Fresh Runtime result

第二轮 Fresh Runtime 基于：

`1e8e09aed4388d169a75e8029c20fc8b87edf4ff`

Codex CLI：`0.154.0`。7/7 场景结果完整，全部 `returncode=0`、stderr 为空。按 corpus v2 的 35 条显式 assertions，第二轮可达到 **35/35 PASS**：

- generation 直接使用 bounded `execute / implementation / vue3 / typescript / vue-sfc / code / null-risk` signals，读取 16 个返回候选并完成语义收窄；
- verification 直接命中 database-migration completion + evidence claim 两条 Rule；
- mixed responsibility 分三次 discovery：implementation 16 candidates → external-operation 4 candidates → converge verification 1 candidate；
- negative / ambiguity 用 unknown `null` 保留 artifact 缺口，读取保守候选后拒绝 migration-specific 结论；
- invalid metadata 正确 fail closed；
- Skill vs Rule 保持 `execute-unit` 与 supporting Rules 分层；
- Consumer-local 不访问 upstream，并在本地重新发现后正确应用 Vue build-vs-typecheck / evidence semantics。

但第二轮仍发现一个**高于 v2 grader assertion 的 Runtime Target 缺陷**：Consumer-local 在第一次 discovery 之前执行 `rg --files`，把完整 `docs/rules/**` 路径集合送入 LLM context。虽然没有读取未命中 Front Matter/body，也没有据此反向校准 token，但这违反“LLM 只接收 candidate locators + candidate bodies”，并会使模型上下文随 Rule 总量 N 增长。

因此第二轮不用于关闭 Gate；V4-06 仍为 **CURRENT / REWORK**。

### Current rework

当前 contract 已进一步收紧：

- task-side 五维值继续采用 known / known-empty `[]` / unknown `null` 三态，每维最多 6 token；
- Rule Discovery 返回的 `candidates[]` 是 ordinary runtime 获得 Rule locator 的唯一入口；
- 禁止通过 `rg --files`、`find`、目录树、IDE index 或脚本预枚举 `docs/rules/**` 的完整 locator / 文件名集合；
- `status=ok` 且候选为空时，既不得读取未命中 Rule metadata/body，也不得枚举未命中 locator 反向校准；
- eval corpus v3 将 locator enumeration 明确定义为 protocol failure；
- Consumer-local fixture 同步 locator-only progressive-disclosure contract；
- deterministic tests 固化 corpus v3 与 Consumer-local locator-only Authority。

当前 rework 必须先通过 deterministic CI，再在新的精确 Head 上重新执行全部 7 个 Fresh Runtime 场景和人工逐 assertion / protocol 评分。只有第三轮 clean PASS 后才可进入 V4-07。
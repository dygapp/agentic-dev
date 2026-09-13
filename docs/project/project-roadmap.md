---
id: project:roadmap
type: project
status: active
---

# Project Roadmap

## Current Foundation

当前项目处于 **V4 — 分布式规则发现与仓库基础重构** 的最终 Closure 阶段。

Frozen V3 locator：

`agentic-dev@1c8cdfea9ecf23ef33ffab20eec3c93679fd4578`

V4 是断代式、减法优先 Foundation Rebuild，不维护 V1～V3 current working-tree compatibility layer。过程设计、分类、实验与阶段证据由 Issue #122、PR #123、Git 与 Actions 持有；本 Roadmap 只保留当前 Foundation、Gate 状态和稳定下一步。

## Current Runtime

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

稳定约束：

- Rule metadata 与规范正文同文件维护；
- 不维护 Reviewed Discovery Map / Activation Manifest / Runtime Catalog / rule-index；
- Rule Discovery 返回的 `candidates[]` 是 ordinary runtime 获得 Rule locator 的唯一入口；
- 未命中 Rule locator / metadata / body 不进入 ordinary LLM context；
- task signals 使用 known array / known-empty `[]` / unknown `null` 三态，每个非空维度最多 6 个 canonical token；
- Skill 只承担稳定独立执行闭环；Rule 只承担条件/约束/默认值/不变量/完成声明；Guide 只承担面向人的低频 adoption / upgrade / recovery 说明；
- Consumer adoption 后 ordinary runtime 默认只依赖 Consumer-local Authority / Method / Skills / Rules / Rule Discovery，不在线依赖 upstream current state。

## Gates

- V4-00 Baseline Freeze & Rebuild Boundary — PASS
- V4-01 Asset Inventory & Classification — PASS
- V4-02 Front Matter & Rule Discovery Contract — PASS
- V4-03 Information Architecture & Rule Decomposition — PASS
- V4-04 Rule Discovery Tool & Lint — PASS
- V4-05 Runtime Integration — PASS
- V4-06 Generation / Verification Discriminating Evals — PASS
- V4-07 Token Scaling Gate（20 / 100 / 500 Rules）— PASS
- V4-08 Consumer Validation — PASS（natural Rule Evolution observation deferred）
- **V4-09 Closure & Baseline Replacement — CURRENT**

Gate 编号不是自动集成授权。

## Current Evidence

V4-06 已以 Fresh Runtime 证明 generation、verification、mixed responsibility、negative/ambiguity、invalid metadata、Skill/Rule boundary 与 Consumer-local ordinary runtime；最终 7 / 7 场景、35 / 35 assertions PASS。

V4-07 已验证 20 / 100 / 500 Rules 下仅相同少量 candidates 进入模型上下文；当前证据支持：

```text
Tool side: O(N metadata scan/filter)
LLM side: O(k locator + k rule body), k << N
```

V4-08 已在真实 Consumer `dygapp/jilinjobs-cms` 完成显式 adoption、Consumer-local projection、ordinary generation / verification discovery、无中心同步资产和 post-adoption upstream decoupling。自然 Rule Evolution 尚未实际发生；按项目负责人明确决策，该 gap 保留为 post-adoption observation，不阻塞本轮 V4 Closure，后续真实使用问题通过 Consumer feedback 继续演进。

详细证据由 Issue #122、PR #123 与对应 Actions 持有，本 Roadmap 不复制完整评分流水账。

## Current Gate — V4-09

Closure & Baseline Replacement 只做最终有效状态收敛：

- 删除 temporary / superseded V4 与前代运行资产；
- 核心 Method / Architecture / Skills / Rules / Guides 只保留最终有效设计；
- `docs/project/` 只保留本 Roadmap；
- Fresh Context 不需要理解 V1～V3 历史即可工作；
- Consumer adoption / explicit baseline upgrade 路径由 current Consumer Lifecycle 与 Guide 持有；
- V4 实施历史继续保存在 Issue #122 / PR #123 / Git / Actions；
- 完成 exact-head closure verification 后进入 Integration Gate；只有 PR #123 集成到 `master` 后，`master` 才成为正式 V4 baseline。

当前 Closure audit 已移除被 V4 Rule Discovery 取代的旧 `evals/capability/**` 与 `evals/rule-retrieval/**` 入口，并收敛 Evals runner / guide。下一实际动作是完成最终 current-tree / exact-head verification；merge 仍需独立授权。

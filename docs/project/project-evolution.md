---
id: project:evolution
type: project
status: active
---

# Project Evolution

## 1. 目的

本文件只保存对理解 `agentic-dev` 当前设计仍有长期价值的**稳定演进里程碑摘要**。

它不是实施日志，也不替代 Git / Issue / PR / Actions。每个阶段的完整实验、Gate、Review 和 commit 证据仍由 GitHub 历史保存。

## 2. 真实 Consumer 验证建立项目方向

早期 `agentic-dev` 通过真实 Consumer 验证，而不是只在方法仓库内部自洽：

- Issue #18：首个真实 Greenfield Consumer 实验，验证新的 Agent 能从 Consumer Repository Authority、需求、Method 与按需 Skill 启动真实项目；
- Issue #33：Existing Consumer 持续演进实验，验证已有项目能够从自身持久化 Authority 与 Roadmap 恢复，而不是重复 Greenfield bootstrap；
- 后续 Consumer Evidence 持续证明：Consumer 项目事实必须保留在 Consumer，自上游采用的能力必须本地固化，ordinary runtime 不能持续依赖 upstream。

这一阶段奠定了“reusable capability + Consumer-local Authority”的长期方向。

## 3. Engineering Capability Foundation

Consumer Evidence 逐步推动项目从“通用方法 + Skills”扩展为更明确的工程能力体系，重点验证了：

- implementation minimality；
- surgical diff scope；
- technology / verification profile；
- Consumer override / local Authority；
- exact-head Current Evidence。

Issue #52 等真实采用证据明确保留了一个重要边界：Consumer 选择性固化 reusable capability，但不复制 `agentic-dev` Project Roadmap、Foundation 状态、PR / Issue / Experiment 项目事实。

## 4. Rule Governance v2 — Consumer-local first

Issue #92 把规则治理的目标从“上游仓库内部如何更好发现规则”进一步收敛为：

> 规则治理、发现和激活必须能在真实 Consumer 中本地持续发挥作用，而不是形成 ordinary runtime 的上游依赖。

该阶段形成并验证了 Consumer-local-first 的设计方向、按职责加载、显式 baseline adoption / upgrade、local override 与 fail-closed 等关键思想。

## 5. V3 — 知识与能力所有权收敛

Issue #94 组织了 V3-01 ～ V3-08 的系统收敛：

- 知识与能力所有权模型；
- 当前仓库所有权审计；
- Consumer 初始化 / adoption / upgrade / ordinary runtime 生命周期；
- Skill 重分类与准入；
- 面向 Agent 的结构化资源模型；
- 资源发现架构；
- `agentic-dev` self-adoption；
- Consumer 验证与持续有效性。

随后 Issue #118 执行独立复核。V3 的价值在于明确了 semantic owner、Consumer-local lifecycle、发现失败关闭与 Evidence 泛化边界；它也暴露了 Reviewed Discovery Map / Catalog 等派生中心索引的同步和上下文成本。

V3 最终 Closure baseline 成为 V4 重构起点。

## 6. V4 — 分布式 Rule Discovery Foundation

Issue #122 启动减法优先的 Foundation Rebuild，主动放弃需要人工与规则正文同步的中央 Map / Manifest / Catalog。

V4 建立当前 Rule Discovery 基础：

```text
current task facts
→ bounded task signals
→ local deterministic Rule Discovery
→ small {id, path} candidates
→ read candidate bodies only
→ semantic applicability confirmation
```

核心结果包括：

- Rule metadata 与正文同文件；
- 全量 Rule metadata 不进入 ordinary LLM context；
- locator-only progressive disclosure；
- task signals 三态与 bounded token；
- deterministic / fail-closed discovery；
- Consumer ordinary runtime 使用 Consumer-local Rules / Discovery；
- 当前工作树删除被取代的 V1～V3 runtime 发现资产。

V4 closure baseline：`3098f17b5661fbd4edbbaf1080ed4b4f5759e0d8`。

## 7. Capability Model v2 — 能力类型与双视窗

V4 后的真实可用性复核发现：Rule Discovery 已稳定，但 Method / Skill / Rule / Guide 的长期边界、Agent process entry 与 Human View 仍不完整。

Issue #124 / PR #125 形成 Capability Model v2：

- `Single Semantic Ownership, Multiple Views`；
- Method 成为可扩展的一等复杂工作过程模型；
- Skill 成为责任明确后的有界执行能力；
- Rule 成为可独立于 Skill 存在的横切条件性 policy / constraint / invariant；
- Rule 明确支持 Consumer-local specialization；
- Consumer Adoption / Upgrade 提升为正式 Method；
- Guide / README 纯化为 Human View；
- Agent Bootstrap 建立 Method Selection、Skill discovery 与 Rule Discovery 的闭环。

PR #125 于 integration commit `e5488fd22a078ab59a427e36ef9a20af935fc63f` 合并，Issue #124 completed。

## 8. Project Knowledge Model — Project / Capability 分界

Capability Model v2 集成后继续复核发现：部分 Architecture 仍混入 `agentic-dev` 当前 Repository instance，例如 Method selector mapping、Skill inventory/count 与 AI Development-specific phase identity；同时 `docs/project/` 只剩 Roadmap，导致项目使命、当前 capability instance 和稳定演进历史缺乏明确长期 owner。

Issue #126 / PR #127 建立 Project Knowledge Model：

- `docs/project/**` 只拥有当前 Repository 自身的使命、核心项目要求、capability instance、Roadmap 与稳定演进摘要；
- `docs/architecture/**`、`docs/methods/**`、`skills/**`、`docs/rules/**` 与对应 tool contract 继续只拥有可复用 capability；
- 正式确立 **Project 不传播，Capability 传播**；
- Method selector instance 移入 Project Capability Profile；
- Skill inventory/count 退出 Skill Architecture；
- Method-specific phase identity 回归具体 Method；
- Rule Discovery exact runtime locator 只由 Project Capability Profile 持有；
- Consumer Adoption / Upgrade 明确不复制 upstream Project state，Consumer 必须建立自己的 local Project Knowledge / capability instance；
- deterministic contracts 防止实例信息重新漂回 Architecture / Bootstrap。

PR #127 以 exact candidate Head `5a2e59f5ae248fb2cf288c6521d8a9903ae8b68b` 通过 50 / 50 deterministic tests、Rule Discovery regression、高影响边界复核与 Convergence，并于 integration commit `10397cf00914fcfd6d71fd2ad6be6b89618dde8a` squash merge。

这一阶段没有改变 V4 Rule Discovery 核心运行语义，而是补齐 reusable capability 与 `agentic-dev` 自身 Project Knowledge 的长期 ownership 边界。

## 9. Model Collaboration Capability & Adoption v1

Issue #129 / PR #132 将历史 `experiment/codex-multi-model-collaboration`、Issue #71 Consumer model-routing Evidence，以及当前 Rule Discovery / Fresh Context / Project Capability Instance 架构重新收敛为正式、可选配的 Model Collaboration capability。

这一阶段形成的长期边界包括：

- `architecture:model-collaboration` 拥有 deterministic-first、能力层级、Primary responsibility、Authority-preserving handoff、single-writer、独立 review、Evidence-based escalation、requested-vs-observed runtime claim 与 single-agent fallback 等 reusable semantics；
- `method:model-collaboration-adoption` 只负责在 collaboration semantics 已经进入 Consumer-local Authority 后，探测 runtime、选择 strategy、投射 local config / policy、建立 instance、验证并启用或 fallback；
- `method:consumer-adoption` / `method:consumer-upgrade` 继续拥有 upstream reusable semantics 的首次接受与 baseline delta assessment，专用 collaboration Method 不得重新实现或绕过这一 Gate；
- `Project Capability Profile` 只记录 Repository-local selector / instance，不复制 reusable capability body；`agentic-dev` 自身当前 collaboration instance 仍为 `disabled`；
- Codex 配置与角色 profile 被保留为带核验日期的 Human Reference，不把平台专项 schema、模型名或 `.codex/` 物理结构提升为跨 Repository Authority；
- “协作链路可以安全启用”与“协作更省、更快或应成为默认策略”被拆成 functional enablement 与 efficiency / preferred-default 两类不同 claim；效率结论必须有可比单 Agent baseline 支撑；
- 旧实验中静态配置成功但 child collaboration smoke 失败的结果继续作为 Evidence，不能被改写为 runtime PASS；真实 child-thread、single-writer runtime behavior、observability 与 fallback 仍需每个 Consumer 在 adoption 时重新验证。

本轮还沉淀了一条通用 capability 分类经验：一个自然语言需求可能同时包含 reusable capability semantics、upstream semantic acceptance、local instance establishment、Consumer-local policy 与 Human View，不能先选文档类型再强行归类。新增 Method 通过 admission gate 后还需要做 **Method composition review**，检查它的前置条件、失败返回、完成结果以及是否侵占相邻 Method 已有 Gate。

PR #132 candidate exact Head `2d6b093696bbd97d5c43a265173afc9954a7008f` 通过 Rule Discovery Run #94 与独立复核（未解决 Blocking / Medium = 0 / 0），随后于 integration commit `385204c8605dd58584ec18456ab8a97d6282b515` squash merge；Post-Integration Rule Discovery Run #95 PASS，Issue #129 completed。

## 10. 当前演进原则

从当前阶段开始，项目演进遵守：

- 当前工作树表达当前有效 owner，不保留历史兼容层；
- Project Knowledge 保存稳定项目定义 / 实例 / Roadmap / 里程碑，不恢复阶段文档膨胀；
- reusable capability 继续以真实 Consumer Evidence 驱动，而不是理论扩张；
- 历史细节需要时从 GitHub Issue / PR / Git 恢复，不复制到 ordinary Fresh Context；
- Project Capability Profile 必须持续保持为薄的 Repository-local instance owner，不演变成新的 Runtime Catalog / Rule Index；
- 新 capability 的 semantic owner 分类应先区分 reusable semantics、semantic acceptance、local instance activation 与 ordinary use，再决定是否需要 Architecture / Method / Skill / Rule / Project / Guide；
- 新增 specialized Method 除了通过自身 admission gate，还必须复核与相邻 Method 的 Gate ownership 和组合关系。
---
id: guide:architecture-navigation
type: guide
status: active
---

# Architecture 目录导航

本 README 只供人类快速了解 `docs/architecture/`，不是 Agent runtime 的 Architecture selector，也不拥有第二套规范语义。

当前 Architecture：

- [`engineering-capability-architecture.md`](engineering-capability-architecture.md) — 顶层 capability 类型、Single Semantic Ownership / Multiple Views、Agent/Human 双视窗与演进判定；
- [`project-knowledge-architecture.md`](project-knowledge-architecture.md) — Project Knowledge 与 reusable Capability 的边界、Project owner 最小职责及 Consumer projection boundary；
- [`method-architecture.md`](method-architecture.md) — Method 的定义、通用 selection contract、phase identity ownership 与新增门禁；
- [`requirement-authority-architecture.md`](requirement-authority-architecture.md) — Consumer Requirement Authority 的 semantic ownership、推荐 `docs/requirements` 信息架构、README / index / fact owner 边界、Aspect 准入、Fresh Context consumption 与 artifact lifecycle；
- [`consumer-architecture.md`](consumer-architecture.md) — Consumer ownership、ordinary runtime、local specialization 与 upstream decoupling；
- [`model-collaboration-architecture.md`](model-collaboration-architecture.md) — 多模型协作的 capability tiers、Primary responsibility、Authority-preserving handoff、single-writer、evidence-based escalation、Consumer projection 与 fallback；
- [`skill-architecture.md`](skill-architecture.md) — Skill 的执行能力边界、与 Method / Rule 的关系、inventory ownership 与准入门禁；
- [`rule-architecture.md`](rule-architecture.md) — Rule 的横切语义、粒度、Consumer-local specialization 与 human navigation 边界；
- [`rule-discovery-architecture.md`](rule-discovery-architecture.md) — Rule Discovery 的 task signals、确定性筛选、locator-only、fail-closed 与规模约束。

Architecture 只持有可复用、可被 Consumer adopt / adapt 的结构性 contract。`agentic-dev` 当前 capability instance、Roadmap 与历史里程碑属于 `docs/project/**`，不应因为当前仓库正在使用某项 capability 就写回 Architecture。

Agent 只在当前 Method、Skill、Rule、Project Profile 或 Repository Authority 明确需要时加载对应 Architecture，不因本 README 全量读取。
---
id: guide:architecture-navigation
type: guide
status: active
---

# Architecture 目录导航

本 README 只供人类快速了解 `docs/architecture/`，不是 Agent runtime 的 Architecture selector，也不拥有第二套规范语义。

当前 Architecture：

- [`engineering-capability-architecture.md`](engineering-capability-architecture.md) — 顶层能力类型、Single Semantic Ownership / Multiple Views、Agent/Human 双视窗与演进判定；
- [`method-architecture.md`](method-architecture.md) — Method 的定义、selection contract 与新增门禁；
- [`consumer-architecture.md`](consumer-architecture.md) — Consumer ownership、ordinary runtime、local specialization 与 upstream decoupling；
- [`skill-architecture.md`](skill-architecture.md) — Skill 的执行能力边界、与 Method / Rule 的关系及准入门禁；
- [`rule-architecture.md`](rule-architecture.md) — Rule 的横切语义、粒度、Consumer-local specialization 与 human navigation 边界；
- [`rule-discovery-architecture.md`](rule-discovery-architecture.md) — Rule Discovery 的 task signals、确定性筛选、locator-only、fail-closed 与规模约束。

Agent 只在当前 Method、Skill、Rule 或 Repository Authority 明确需要时加载对应 Architecture，不因本 README 全量读取。
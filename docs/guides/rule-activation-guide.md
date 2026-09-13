---
id: guide:rule-adoption-navigation
type: guide
status: active
---

# Rule 采用与恢复导航

本 Guide 只用于低频 adoption / upgrade / recovery 导航，不负责 ordinary runtime 规则路由。

- 在 `agentic-dev` 自身工作：从根 `AGENTS.md` 恢复，再按当前任务调用 `tools/rule-discovery/`；
- 新 Consumer：先读 `docs/architecture/consumer-lifecycle.md` 与 `docs/guides/using-agentic-dev.md`；
- Existing Consumer upgrade：先恢复 Consumer-local current state，再显式比较 upstream baseline；
- Consumer ordinary runtime：只使用 Consumer-local Rule Discovery、Rules、Skills 与 Authority。

Rule Discovery 的规范 contract 只在 `docs/architecture/rule-discovery-architecture.md` 维护。本 Guide 不保存 Rule routing table、keyword map、priority 或 current-state 副本。
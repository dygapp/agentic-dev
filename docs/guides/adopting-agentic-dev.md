---
id: guide:adopting-agentic-dev
type: guide
status: active
---

# 首次采用 agentic-dev

本文是 `method:consumer-adoption` 的人类说明，不替代正式 Method。

## 什么时候使用

当一个项目第一次决定把 `agentic-dev` 的 Method / Architecture / Skill / Rule 引入为 Consumer-local 能力时使用。普通开发任务不需要重新执行 adoption。

## 推荐做法

先从 Consumer 自己出发，而不是从 upstream 出发：确认 Repository Authority、当前项目结构、已有开发方法和权限边界，再选择一个精确 `agentic-dev` baseline。

随后逐项判断能力：

- **adopt**：语义可以直接接受；
- **adapt**：能力有价值，但需要本地路径、流程或 policy 调整；
- **reject**：当前 Consumer 不需要。

Rule 特别适合本地化。比如通用 Git / external-operation Skill 可以复用，但 Consumer 自己的 commit type / scope、术语或审批要求应由本地 Rule 持有。

采用完成后，Consumer 应能只依赖本地状态完成普通 Agent 工作：知道从哪里恢复、怎样选 Method / Skill、怎样发现 Rule，并且 discovery failure 不会自动在线回到 upstream。

最后记录精确 evaluated upstream baseline 和必要验证证据。以后 upstream 有变化也不会自动更新 Consumer；需要显式进入 Upgrade Method。

正式 Gate 与完成条件见 `docs/methods/consumer-adoption.md`；长期 Consumer ownership 见 `docs/architecture/consumer-architecture.md`。
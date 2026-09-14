---
id: architecture:consumer
type: architecture
status: active
---

# Consumer 架构

## 1. Consumer ownership

Consumer Repository 始终拥有自己的项目事实、需求、Method、Architecture、代码、验证与集成策略。`agentic-dev` 只提供可采用的通用能力；upstream 状态不会自动成为 Consumer current state。

Consumer adoption 与 upgrade 的过程分别由 `method:consumer-adoption` 与 `method:consumer-upgrade` 持有，本 Architecture 只定义长期 ownership 与运行不变量。

## 2. Ordinary runtime

采用完成后：

```text
Consumer Repository facts
→ Consumer Agent Bootstrap / Method selection
→ current Method stage / direct responsibility
    ├─→ relevant Consumer-local Architecture
    ├─→ Consumer-local Skill discovery / invocation（如需要）
    └─→ Consumer-local Rule Discovery → applicable Rule bodies
→ execute / verify / return
```

ordinary runtime 默认 `upstream access = 0`。本地 Method entry、Skill discovery、Rule discovery 或 metadata 异常必须在 Consumer-local state 内失败关闭或按 Consumer Authority 升级；不能自动访问 `agentic-dev` 在线补流程 / 规则。

## 3. Local canonical owners

Consumer 可以改变路径、命名、工具集成、Method adaptation 与局部 Rule policy，只要：

- 项目事实仍由 Consumer Authority 拥有；
- local Method / Architecture / Skill / Rule 的 semantic owner 明确；
- Rule metadata 与 Rule body 同源维护；
- 没有中心化人工同步 Rule routing map；
- Rule Discovery output 保持少量 locator，而不是全量 metadata；
- upstream provenance 与 local Authority 不混为一谈。

## 4. Consumer-local Rule specialization

不同 Consumer 可以针对同一通用执行能力定义不同 local Rule。例如 Git commit type / scope、术语、审批、迁移、验证或技术 policy 可以由各 Consumer Repository Authority 分别持有。

因此通用 Skill 不应为了统一所有 Consumer 而吸收这些 local policy。upstream Rule 也不是 Consumer Rule 的永久主副本；Consumer 在 adoption / upgrade 中裁决 adopt / adapt / replace / reject。

## 5. Upstream decoupling

Consumer ordinary runtime 不依赖：

- upstream current branch；
- upstream Roadmap / Open Issue / PR；
- upstream Rule tree；
- upstream Guide；
- “latest baseline” 在线解析。

只有显式 adoption / upgrade Method 可以重新进入 upstream，并在完成后再次关闭 runtime dependency。

## 6. Feedback

Consumer Evidence 可以通过 Issue / Comment 等方式反馈给 `agentic-dev`，但只成为 research / evolution candidate。是否改变 upstream Method / Architecture / Skill / Rule，必须在 `agentic-dev` 自己的 Repository Authority 下重新裁决。
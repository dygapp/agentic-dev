---
id: architecture:consumer
type: architecture
status: active
---

# Consumer 架构

## 1. Consumer 归属

Consumer Repository 始终拥有自己的项目事实、Project Knowledge、需求、Method、Architecture、代码、验证与集成策略。`agentic-dev` 只提供可采用的通用 capability；upstream 状态不会自动成为 Consumer current state。

Consumer adoption 与 upgrade 的过程分别由对应 Method 持有，本 Architecture 只定义长期 ownership、projection boundary 与 ordinary runtime 不变量。

核心边界：

> **Project 不传播，Capability 传播。**

upstream `Project Charter / Capability Profile / Roadmap / Evolution` 可以作为 provenance、背景或比较上下文读取，但不属于 adopt / adapt 的 reusable capability 集合，也不会自动成为 Consumer-local Project Authority。

## 2. 普通运行时

采用完成后：

```text
Consumer Repository facts
→ Consumer-local Project Knowledge / capability instance
→ Consumer Agent Bootstrap / Method selection
→ current Method stage / direct responsibility
    ├─→ relevant Consumer-local Architecture
    ├─→ Consumer-local Skill discovery / invocation（如需要）
    └─→ Consumer-local Rule Discovery → applicable Rule bodies
→ execute / verify / return
```

ordinary runtime 默认 `upstream access = 0`。本地 Project capability profile、Method entry、Skill discovery、Rule discovery 或 metadata 异常必须在 Consumer-local state 内失败关闭或按 Consumer Authority 升级；不能自动访问 `agentic-dev` 在线补流程 / 规则。

如果 adopted capability 依赖 Tool、compute 或 external integration，Consumer ordinary runtime 还必须能只从 Consumer-local Agent-consumable Authority 恢复 obligation、canonical locator、可执行路径、result / Evidence recovery 与 fail-closed behavior。只复制 Method / Architecture / Rule / Tool source 或 locator，而没有可恢复的 executable path，不构成完成采用。

该 invariant 不规定具体平台或 transport。直接执行与自动化 alternate path 的实现由 Consumer-local capability instance 持有；Fresh Consumer Agent 不得依赖 upstream、Human Guide、历史聊天或模型记忆补齐。

## 3. Consumer 本地 Project Knowledge

Consumer 必须拥有自己的 Project Knowledge 或等价 Repository Authority，用来表达：

- Consumer 自身产品 / 项目使命、需求和非目标；
- Consumer 当前采用哪些 Method / Architecture / Skill / Rule / Tool contract；
- local Method selector、Rule root / Discovery Tool locator、Skill entry 等 capability instance；
- 已采用且依赖 Tool / compute / external integration 的 executable path、自动化 alternate path、结果恢复与 fail-closed instance；
- Consumer 自己的 Roadmap / current work / integration state；
- 对理解当前 Consumer 仍有价值的本地演进摘要。

这些信息不得通过复制 upstream Project docs 来建立。upstream baseline 只提供 provenance，Consumer-local owner 才定义当前状态。

## 4. 本地规范性归属

Consumer 可以改变路径、命名、工具集成、Method adaptation 与局部 Rule policy，只要：

- 项目事实仍由 Consumer Authority 拥有；
- local Project / Method / Architecture / Skill / Rule 的 semantic owner 明确；
- Rule metadata 与 Rule body 同源维护；
- 没有中心化人工同步 Rule routing map；
- Rule Discovery output 保持少量 locator，而不是全量 metadata；
- upstream provenance 与 local Authority 不混为一谈。

## 5. Consumer 本地 Rule 特化

不同 Consumer 可以针对同一通用执行能力定义不同 local Rule。例如 Git commit type / scope、术语、审批、迁移、验证或技术 policy 可以由各 Consumer Repository Authority 分别持有。

因此通用 Skill 不应为了统一所有 Consumer 而吸收这些 local policy。upstream Rule 也不是 Consumer Rule 的永久主副本；Consumer 在 adoption / upgrade 中裁决 adopt / adapt / replace / reject。

## 6. 上游解耦

Consumer ordinary runtime 不依赖：

- upstream current branch；
- upstream Project Charter / Capability Profile / Roadmap / Evolution；
- upstream Open Issue / PR；
- upstream Rule tree；
- upstream Guide；
- “latest baseline” 在线解析。

只有显式 adoption / upgrade Method 或明确 research / comparison task 可以重新进入 upstream，并在完成后再次关闭 runtime dependency。

## 7. 能力投影

显式 adoption / upgrade 时，可传播的对象是经过裁决的 capability：

- Method；
- Architecture；
- Skill；
- Rule；
- 必要 Tool / runtime contract。

Consumer 对每项能力执行 adopt / adapt / replace / reject，并把接受结果写入 Consumer-local canonical owner。

accepted capability 依赖 Tool、compute 或 external integration 时，projection 必须同时建立 Consumer-local executable instance；上游的可执行路径只可作为 adoption / upgrade 输入，不能成为 Consumer ordinary runtime 的在线 fallback。

upstream Project Knowledge 只可帮助回答“这个能力为什么在 upstream 存在、当前 upstream 如何实例化”，不能替代 Consumer 自己的 local decision。

## 8. 反馈

Consumer Evidence 可以通过 Issue / Comment 等方式反馈给 `agentic-dev`，但只成为 research / evolution candidate。是否改变 upstream Project Charter、Method、Architecture、Skill、Rule 或 Tool contract，必须在 `agentic-dev` 自己的 Repository Authority 下重新裁决。

Consumer-local 成功、目录结构或 Project Profile 不因反馈自动泛化成所有 Consumer 的 reusable requirement。

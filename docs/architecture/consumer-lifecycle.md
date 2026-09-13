---
id: architecture:consumer-lifecycle
type: architecture
status: active
---

# Consumer 生命周期

## 1. 原则

Consumer Repository 始终拥有自己的项目事实、需求、架构、代码、验证和集成策略。`agentic-dev` 只提供可采用的 Method、Skills、Rules 与 supporting architecture；上游状态不会自动成为 Consumer 当前状态。

## 2. 首次采用

首次采用时：

1. 先恢复 Consumer 自己的 Repository Authority；
2. 明确需要引入的 upstream capability；
3. 对 Method / Skill / Rule / Guide 分别做 adopt / adapt / reject 判断；
4. 将接受内容写入 Consumer-local current owner；
5. 建立或接入 Consumer-local Rule Discovery Tool；
6. 验证普通运行不需要在线读取 upstream；
7. 记录可追溯的 evaluated upstream baseline。

采用不是把整个 `agentic-dev` 仓库复制进 Consumer，也不要求保留上游目录结构。

## 3. Ordinary runtime

采用完成后：

```text
Consumer Repository facts
→ Consumer task signals
→ Consumer-local Rule Discovery
→ Consumer-local Rules / Skills / Authority
```

普通运行默认 `upstream access = 0`。本地发现失败、Rule metadata 异常或候选歧义必须在 Consumer-local state 内失败关闭；不能自动回到 `agentic-dev` 在线补规则。

## 4. 显式 baseline upgrade

上游新增 commit 本身不会改变 Consumer。只有 Consumer 显式进入 upgrade lifecycle 后，才重新读取目标 upstream baseline，并逐项判断：

- 新增能力是否需要采用；
- 当前本地 adaptation 是否保留；
- 哪些旧能力被取代；
- Rule Front Matter / Discovery Tool contract 是否发生不兼容变化；
- 需要哪些 targeted verification。

升级完成后必须重新验证 Consumer-local ordinary runtime 与 current baseline provenance。

## 5. Consumer-local ownership

Consumer 可以改变路径、命名、工具集成和局部 Rule tokens，只要：

- 项目事实仍由 Consumer Authority 拥有；
- Rule metadata 与 Rule body 同源维护；
- 没有中心化人工同步发现映射；
- Rule Discovery output 仍保持少量 locator，而不是全量 metadata；
- upstream provenance 与 local authority 不混为一谈。

## 6. 反馈

Consumer Evidence 可以通过 Issue / Comment 等方式反馈给 `agentic-dev`，但反馈只成为研究或候选输入。是否改变上游 Method / Skill / Rule，必须在 `agentic-dev` 自己的 Repository Authority 下重新裁决。
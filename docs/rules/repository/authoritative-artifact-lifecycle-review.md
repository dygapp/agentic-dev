---
id: rule:authoritative-artifact-lifecycle-review
type: rule
status: active
scope:
  phases: []
  activities: [review]
  technologies: []
  artifacts: [authority]
  risks: [authority-lifecycle]
---

# 长期权威产物生命周期复核

新增、提升、重大修改或替换长期 Authority artifact 时，复核必须能够回答其产生者、触发条件、消费者、持久位置、更新责任、取代关系与升级边界。

如果这些责任存在会导致后续 Agent 无法可靠识别当前有效事实的缺口，不能仅因为文档已存在就声明完成。临时产物只需要明确退出或丢弃边界，不为形式完整制造长期 lifecycle。

## Current owner transition completeness

当 Current canonical owner 被 replace / retire / archive，或其 lifecycle 从 active 转为 completed 时，在声明 transition 完成前必须同步复核所有仍承担 Current 语义的 consumer：

- Bootstrap / locator / selector / navigation 是否已经指向新的 Current owner 或明确的完成态；
- tests、workflow assertions、recovery fixtures 等 verification consumer 是否仍绑定 retired identity、path 或 contract；
- Roadmap、Project Knowledge 与其他 durable current-state wording 是否仍把已退出对象表达为 active dependency；
- replacement / supersede / archive relation 是否足以让 Fresh Context 区分 Current truth 与 Historical / provenance evidence。

Historical、archive、migration provenance 或兼容性说明可以合法保留 retired owner / id / path 引用；**出现旧标识本身不构成 stale Current dependency**。只有该引用仍被 ordinary runtime、Current selector、verification contract 或 durable current-state claim 当作当前事实消费时，才构成 transition 缺口。

Targeted retired-id/path reference scan、dead locator / link check 等 deterministic validation 可以帮助发现明显遗漏，但不能替代对引用角色、currentness 与 semantic ownership 的复核，也不得为此建立需要与 Authority corpus 持续同步的中央 retired-owner catalog。
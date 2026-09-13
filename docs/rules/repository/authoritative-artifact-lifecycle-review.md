---
id: rule:authoritative-artifact-lifecycle-review
type: rule
status: active
scope:
  phases: [converge]
  activities: [review]
  technologies: []
  artifacts: [authority]
  risks: [authority-lifecycle]
---

# 长期权威产物生命周期复核

新增、提升或重大修改长期 Authority artifact 时，复核必须能够回答其产生者、触发条件、消费者、持久位置、更新责任、取代关系与升级边界。

如果这些责任存在会导致后续 Agent 无法可靠识别当前有效事实的缺口，不能仅因为文档已存在就声明完成。临时产物只需要明确退出或丢弃边界，不为形式完整制造长期 lifecycle。
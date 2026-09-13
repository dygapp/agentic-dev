---
id: rule:vue-template-ref-dom-timing
type: rule
status: active
scope:
  phases: [execute]
  activities: [implementation]
  technologies: [vue3]
  artifacts: [vue-sfc]
  risks: [dom-lifecycle]
---

# Vue Template Ref DOM 时机

只有当前行为确实依赖 DOM 已挂载或已更新时，才增加 `nextTick`、lifecycle 或 watcher 等时机控制。选择机制由真实 trigger 与现有代码结构决定，不固定单一模式。
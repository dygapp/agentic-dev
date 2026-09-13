---
id: rule:vue-computed-purity
type: rule
status: active
scope:
  phases: [execute]
  activities: [implementation]
  technologies: [vue3]
  artifacts: [code]
  risks: [side-effect]
---

# Vue Computed 保持纯派生

`computed` getter 默认保持无副作用。网络请求、其他 state mutation、DOM 操作等外部副作用应进入 watcher、事件、生命周期或更适合的机制。
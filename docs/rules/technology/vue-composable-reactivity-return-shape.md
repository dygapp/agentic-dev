---
id: rule:vue-composable-reactivity-return-shape
type: rule
status: active
scope:
  phases: [execute]
  activities: [implementation]
  technologies: [vue3]
  artifacts: [code]
  risks: [reactivity]
---

# Vue Composable 返回值保持可解构响应性

Composable 返回多个 reactive values 时，默认优先返回包含多个 refs 的普通对象，使调用方解构后仍保持 reactivity。当前 API 有明确理由返回 reactive object 时可以保留，但调用方不得无意解构后仍假设普通变量保持 property reactivity。
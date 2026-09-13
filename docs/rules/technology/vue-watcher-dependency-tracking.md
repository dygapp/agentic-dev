---
id: rule:vue-watcher-dependency-tracking
type: rule
status: active
scope:
  phases: [execute]
  activities: [implementation]
  technologies: [vue3]
  artifacts: [vue-sfc]
  risks: [reactivity]
---

# Vue Watcher 依赖追踪

`watch` 追踪显式 source；`watchEffect` 在同步执行阶段自动收集依赖；异步 `watchEffect` 只会自动追踪第一个 `await` 之前同步访问的依赖。实现和验证不得假设异步 callback 中任意时刻读取的响应式值都会被自动追踪。
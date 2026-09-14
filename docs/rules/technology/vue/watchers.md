---
id: rule:vue-watchers
type: rule
status: active
scope:
  phases: [execute]
  activities: [implementation]
  technologies: [vue3]
  artifacts: [code, vue-sfc]
  risks: [reactivity, asynchronous, stale-work]
---

# Vue Watchers / Effects

Watcher / effect 的依赖追踪与异步清理属于同一个 reactive side-effect 责任。

## 依赖追踪

`watch` 追踪显式 source；`watchEffect` 在同步执行阶段自动收集依赖；异步 `watchEffect` 只会自动追踪第一个 `await` 之前同步访问的依赖。实现和验证不得假设异步 callback 中任意时刻读取的响应式值都会被自动追踪。

## Stale work 清理

Watcher / effect 会产生请求、subscription、timer 或其他可能跨下一次执行继续存在的工作时，应根据当前 stale-work 风险建立 cleanup、cancellation 或 currentness guard。纯同步、无外部资源且不存在 stale work 的 watcher 不为了形式完整机械增加 cleanup。
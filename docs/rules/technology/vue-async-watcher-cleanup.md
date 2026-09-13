---
id: rule:vue-async-watcher-cleanup
type: rule
status: active
scope:
  phases: [execute]
  activities: [implementation]
  technologies: [vue3]
  artifacts: [code]
  risks: [asynchronous, stale-work]
---

# Vue 异步 Watcher 清理

Watcher / effect 会产生请求、subscription、timer 或其他可能跨下一次执行继续存在的工作时，应根据当前 stale-work 风险建立 cleanup、cancellation 或 currentness guard。纯同步、无外部资源且不存在 stale work 的 watcher 不为了形式完整机械增加 cleanup。
---
id: rule:integration-state-closure-review
type: rule
status: active
scope:
  phases: [converge]
  activities: [review]
  technologies: []
  artifacts: [roadmap, repository-state]
  risks: [integration-state]
---

# 集成后状态闭环复核

修改 README、Roadmap 或其他 Fresh Context 恢复入口时，应检查拟集成版本在真正集成后是否仍准确表达长期阶段、当前目标和下一实际 Gate，而不会立即因“等待本 PR 合并”之类瞬时描述失效。

精确 merge SHA、临时 branch 删除等 GitHub 原生事实优先留在 PR、Issue 或 Git 历史。不得机械派生一个只用于记录上一个状态修复已经合并的尾部状态变更。
---
id: rule:human-review-baseline-isolation
type: rule
status: active
distribution: release-input
release-target: software-development
scope:
  phases: [execute, converge]
  activities: [verification, review]
  technologies: []
  artifacts: [review-environment]
  risks: [shared-state-contamination]
---

# 人工复核基线隔离

自动验证会修改数据库、文件、缓存、导航或其他共享状态，而同一环境随后用于人工复核时，必须先保留自动验证的 Current Evidence，再恢复来源明确、可重复构建的人工复核 baseline。

自动测试残留状态不得静默成为人工复核基线；自动验证状态与人工复核环境可以有不同生命周期与资源租约。
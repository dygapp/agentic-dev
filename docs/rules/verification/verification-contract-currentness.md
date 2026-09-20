---
id: rule:verification-contract-currentness
type: rule
status: active
distribution: release-input
release-target: software-development
scope:
  phases: [execute, converge]
  activities: [verification]
  technologies: []
  artifacts: [test, workflow, assertion]
  risks: [stale-verification-contract]
---

# 验证契约当前性

验证产物只有在与当前 Requirement、Specification、Architecture 和其他适用 Authority 一致时，才可以定义有效 expected behavior。验证失败时先区分 implementation defect、stale verification contract、runtime/environment problem 与 external dependency problem。

不得因为测试或 Workflow 已存在就默认其断言高于当前 Authority；验证契约陈旧时，应先修正其真实语义 owner，再重新取得 Current Evidence，而不是修改产品实现去迎合失效断言。
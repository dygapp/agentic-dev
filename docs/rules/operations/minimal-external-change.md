---
id: rule:minimal-external-change
type: rule
status: active
scope:
  phases: []
  activities: [external-operation]
  technologies: []
  artifacts: []
  risks: []
---

# 最小外部变更

外部写操作只执行达到当前目标所需的最小变更。一次外部变化保持单一主要目的，不顺带修改无关对象，不为了形式完整扩大范围，也不基于未经重新读取验证的旧状态继续操作。

存在等价方案时，优先选择更可逆、影响面更小且容易重新验证的路径。
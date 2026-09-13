---
id: rule:surgical-change
type: rule
status: active
scope:
  phases: [execute]
  activities: [implementation]
  technologies: []
  artifacts: [code, configuration, test]
  risks: []
---

# 精准修改与差异范围

最终差异中的每个有意义变化都必须能追溯到当前实现责任、验证责任、已授权权威同步，或由本次修改直接产生且必须闭合的必要清理。

当前变化直接需要、行为保持、范围受控且可验证的准备性重构可以属于同一逻辑变化；相邻独立 Bug、无关 TODO、个人风格清理、大规模无关格式化和其他无法形成当前责任链的修改应移除、记录或另行切分。
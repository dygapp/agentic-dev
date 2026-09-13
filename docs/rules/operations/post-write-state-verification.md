---
id: rule:post-write-state-verification
type: rule
status: active
scope:
  phases: []
  activities: [external-operation]
  technologies: []
  artifacts: []
  risks: []
---

# 写后状态验证

外部写 API 返回成功只证明操作被接受或执行，不证明目标状态已经成立。写操作后必须重新读取对应事实来源，确认文件、Issue、PR、分支、Workflow、部署或其他目标对象的实际当前状态。

验证失败时重新分析，不得继续基于预期状态执行后续操作。
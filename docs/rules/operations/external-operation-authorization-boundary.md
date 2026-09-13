---
id: rule:external-operation-authorization-boundary
type: rule
status: active
scope:
  phases: []
  activities: [external-operation]
  technologies: []
  artifacts: []
  risks: [authorization]
---

# 外部操作授权边界

工具能力、认证成功或 API 可写不等于已经获得操作授权。外部写操作前必须从当前 Repository / Human Authority 确认目标、范围和允许的动作。

合并、发布、部署、破坏性清理以及其他仓库策略明确保留给人工或高影响审批的操作，不得因为技术上可执行而自动执行。
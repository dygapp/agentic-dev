---
id: rule:cross-repository-authorization
type: rule
status: active
distribution: release-input
release-target: software-development
scope:
  phases: []
  activities: [external-operation]
  technologies: []
  artifacts: [repository]
  risks: [cross-repository]
---

# 跨仓库授权独立确认

同一任务涉及多个仓库时，每个仓库的读取、Issue/Comment、文件修改、分支/PR、Workflow、合并或发布权限必须分别从该仓库当前 Authority 确认。

某一仓库的认证身份、工具能力或写权限不会自动授予对另一个仓库的同类操作权限。局部授权缺口只阻塞依赖该权限的操作，不应无根据扩大为整个任务停止。
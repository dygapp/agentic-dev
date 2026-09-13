---
id: rule:evidence-type-must-match-claim
type: rule
status: active
scope:
  phases: [execute, converge]
  activities: [verification]
  technologies: []
  artifacts: []
  risks: []
---

# 证据类型必须匹配声明

任何 completion、pass 或 ready-to-integrate 声明，都必须由能够区分该声明是否真实成立的当前证据支持。实现存在、静态检查、历史 evidence、诊断 observation 或只覆盖主路径的证据不能替代真正需要的完成证据。

快速反馈与 completion verification 可以分层，但最终声明仍必须覆盖其实际验收义务。归属 feature-wide convergence 的义务必须由整体收敛重新检查。
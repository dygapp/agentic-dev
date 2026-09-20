---
id: rule:temporary-evidence-to-persistent-input-promotion
type: rule
status: active
distribution: release-input
release-target: software-development
scope:
  phases: []
  activities: [external-operation, verification]
  technologies: []
  artifacts: [evidence]
  risks: [persistence]
---

# 临时证据晋升为持久输入

Workflow artifact、远程任务输出或临时快照默认只承担一次运行的证明、传输、诊断或审查职责。只有获得当前 Authority 的显式接受，并确实需要被后续稳定重放、迁移、评审或运行持续消费时，才能晋升为持久输入。

晋升后必须验证完整性、来源关系和持久位置，并重新取得受影响的 Current Evidence；上传成功或一次复核通过不会自动完成权威晋升。
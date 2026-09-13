---
id: rule:database-migration-completion-evidence
type: rule
status: active
scope:
  phases: [execute, converge]
  activities: [verification]
  technologies: []
  artifacts: [database-migration]
  risks: []
---

# 数据库迁移完成证据

当前变化包含数据库 schema / migration lifecycle，且环境允许取得完整初始化证据时，最终完成验证至少应覆盖一次：

```text
Fresh Database
→ Full Migration Chain
→ Application Startup
```

SQL 文件检查、编译、单元测试或只在已有数据库上执行增量 migration，不能单独证明新环境可初始化。无法取得完整证据时，必须明确保留证据缺口。
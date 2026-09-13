---
id: rule:git-authority-layer-ordering
type: rule
status: active
scope:
  phases: []
  activities: [commit]
  technologies: []
  artifacts: [git-commit, authority]
  risks: [authority-drift]
---

# 权威层变更先于实现提交

当实现暴露 Method、Architecture 或 Skill contract 问题时，应先修改真实 Authority owner，再提交依赖该 Authority 的实现。不得只修改低层 `SKILL.md`、代码或 Rule，使其事实上静默改变更高层长期语义。

如果多个层级属于同一个不可分逻辑变化，也必须在 diff 与提交说明中保持清楚的权威责任链。
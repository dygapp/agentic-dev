---
id: rule:git-breaking-change-marker
type: rule
status: active
scope:
  phases: []
  activities: [commit]
  technologies: []
  artifacts: [git-commit]
  risks: [breaking-change]
---

# 不兼容提交标记

已经公开稳定的 Skill contract、CLI、Rule Discovery contract 或其他外部能力发生不兼容变化时，提交信息必须使用 Conventional Commits 的显式 breaking 标记，例如 `feat(skills)!: ...`；需要时使用 `BREAKING CHANGE:` 正文说明。

普通内部设计迭代不得滥用 breaking 标记。
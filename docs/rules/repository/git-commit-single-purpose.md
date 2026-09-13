---
id: rule:git-commit-single-purpose
type: rule
status: active
scope:
  phases: []
  activities: [commit]
  technologies: []
  artifacts: [git-commit]
  risks: []
---

# Git Commit 单一目的

一次提交只表达一个主要逻辑目的。为完成该目的所必需的多个文件可以同提交，但无关修正、独立重构、额外能力或另一层级的长期语义变更必须拆分。

提交前应确认没有临时文件、调试输出或与当前逻辑变化无责任链的内容。
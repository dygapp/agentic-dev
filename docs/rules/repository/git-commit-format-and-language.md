---
id: rule:git-commit-format-and-language
type: rule
status: active
scope:
  phases: []
  activities: [commit]
  technologies: []
  artifacts: [git-commit]
  risks: []
---

# Git Commit 格式与语言

`agentic-dev` 提交信息采用 `<type>(<scope>): <中文摘要>`。`type` / `scope` 使用协议约定的小写英文标识，摘要使用自然中文并直接说明主要动作和对象。

当前常用 type：`docs`、`feat`、`fix`、`refactor`、`test`、`chore`。scope 表示稳定责任域，不跟随单个文件名临时发明。
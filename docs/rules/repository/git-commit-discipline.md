---
id: rule:git-commit-discipline
type: rule
status: active
scope:
  phases: []
  activities: [commit]
  technologies: []
  artifacts: [git-commit, authority]
  risks: []
---

# Git Commit 纪律

提交是一个完整的 Repository 责任，不把格式、逻辑边界、Authority 顺序和 breaking 标记拆成多个普通运行时 Rule。

## 格式与语言

`agentic-dev` 提交信息采用 `<type>(<scope>): <中文摘要>`。`type` / `scope` 使用协议约定的小写英文标识，摘要使用自然中文并直接说明主要动作和对象。

当前常用 type：`docs`、`feat`、`fix`、`refactor`、`test`、`chore`。scope 表示稳定责任域，不跟随单个文件名临时发明。

## 单一逻辑目的

一次提交只表达一个主要逻辑目的。为完成该目的所必需的多个文件可以同提交，但无关修正、独立重构、额外能力或另一项无责任链的长期语义变更必须拆分。

提交前应确认没有临时文件、调试输出或与当前逻辑变化无责任链的内容。

## Authority 与实现顺序

当实现暴露 Method、Architecture 或 Skill / Rule contract 问题时，应先修改真实 Authority owner，再提交依赖该 Authority 的实现。不得只修改低层 Skill、代码或 Rule，使其事实上静默改变更高层长期语义。

如果多个层级属于同一个不可分逻辑变化，可以同提交，但 diff 与提交说明必须保持清楚的权威责任链。

## 不兼容变更标记

已经公开稳定的 Skill contract、CLI、Rule / Rule Discovery contract 或其他外部 capability 发生不兼容变化时，提交信息必须使用 Conventional Commits 的显式 breaking 标记，例如 `refactor(rules)!: ...`；需要时使用 `BREAKING CHANGE:` 正文说明。

普通内部设计迭代不得滥用 breaking 标记。
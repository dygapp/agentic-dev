# Git 规范

## Commit

提交信息使用 `<type>(<scope>): <中文摘要>`。`type` / `scope` 使用稳定的小写标识，摘要用自然中文说明主要动作。常用 type 包括 `docs`、`feat`、`fix`、`refactor`、`test`、`chore`。

一次提交只表达一个主要逻辑目的。为完成该目的必须同步修改的 Authority、实现和验证可以同提交；无关修正和独立重构应拆开。

提交前确认工作树没有临时调试文件，Authority 与实现顺序一致，Evidence 与当前 subject 匹配，diff 不混入无关变化。

## Branch 与历史

分支只承载一个可解释的 bounded change。是否必须创建 PR、怎样集成、能否直接本地合并由当前 Repository / Human Authority 决定，不由本规范强制一种平台流程。

不得未经授权对共享分支执行 force push、破坏性 rebase、删除远端 ref 或其他不可逆历史改写。

公开稳定的 Skill contract 或其他外部兼容接口发生不兼容变化时，使用明确 breaking 标记并说明迁移影响；普通内部整理不滥用 breaking 标记。

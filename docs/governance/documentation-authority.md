# 文档 Authority

## 单一语义 owner

同一长期规范事实只保留一个 Current owner。README、Guide、索引和派生视图可以解释或导航，但不能复制第二套 Current Authority。

Project 文档只保存 `agentic-dev` 自身无法由代码、Skill、Guide、GitHub native state 或其他明确 owner 更适合承担的长期事实。

## Current 与 Historical

Current Authority、历史 Evidence、迁移材料、Research 和临时分析必须可区分。Git / Issue / PR / Actions 能可靠保存的运行历史，不再为“记录发生过”创建新的长期 Project owner。

Research 可以保留旧路径和旧模型作为 provenance，但不得参与 ordinary runtime 或被解释成当前依赖。

## owner 生命周期

新增、重大修改、替换或退出长期 owner 时，检查产生与更新责任、消费者、locator / navigation、tests / workflow / fixtures、Roadmap / README / Bootstrap 和 historical relation。发现 stale current dependency 时先修复迁移，不通过长期兼容层掩盖。

没有稳定消费者、只能复制已有事实或只服务一次迁移过程的文档默认不成为长期 owner。

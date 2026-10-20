# 文档 Authority

## 单一语义 owner

同一长期规范事实只保留一个 Current owner。README、Guide、索引和派生视图可以解释或导航，但不能复制第二套 Current Authority。

Project 文档只保存 `agentic-dev` 自身的长期项目事实；可复用产品 / 设计事实仍进入对应 Skill、Architecture、Guide 或代码等真实 owner，不因其重要就一律复制进 `docs/project/**`。

**Git Repository 的版本化内容必须足以独立恢复当前有效的长期权威信息**，包括必要的设计决定、适用范围、约束，以及影响后续维护 / 重新决策的关键取舍依据。不能要求下一个 Fresh Context 必须读取某个 Issue / PR 评论，才能知道当前应遵守什么或为什么保留关键边界。

## Current 与 Historical

Current Authority、历史 Evidence、迁移材料、Research 和临时分析必须可区分。Issue / PR / Actions 只承担讨论、协调、评审与过程 Evidence，不能成为长期权威事实或关键设计取舍的唯一来源；Git commit 历史可以用于追溯演进，但不能代替当前版本化 owner 正文。

不是所有讨论、被否决的细节、日志和原始 Evidence 都必须逐字复制进仓库。对长期消费者仍有价值的决定依据，提炼后写入现有合法 owner 的简短背景 / 取舍段落；仅属过程的材料可以只保留在 Issue / PR。没有独立稳定消费者时，不为每次变更机械建立 ADR、决策清单或另一套 History Authority。

Research 可以保留旧路径和旧模型作为 provenance，但不得参与 ordinary runtime 或被解释成当前依赖。

## owner 生命周期

新增、重大修改、替换或退出长期 owner 时，检查产生与更新责任、消费者、locator / navigation、tests / workflow / fixtures、Roadmap / README / Bootstrap 和 historical relation；完成前核对当前设计决定及必要的取舍依据已进入 Git 版本化的正确 owner，且删除 Issue / PR 阅读权限后仍可恢复。发现 stale current dependency 时先修复迁移，不通过长期兼容层掩盖。

没有稳定消费者、只能复制已有事实或只服务一次迁移过程的文档默认不成为长期 owner。

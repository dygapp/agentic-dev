# 场景 04：调试与验证

这是一个 Fresh Context，只完成故障分类、调试路径和验证设计，不修改任何文件。

请先按当前 `agentic-dev` Repository Authority 和正式使用方式恢复最小必要上下文，然后分析下面的故障：

- 一个数据库迁移相关 Execution Unit 的代码检查、编译和增量迁移测试全部通过；
- 在已有数据库上启动应用也通过；
- 但新环境执行 `Fresh Database → Full Migration Chain → Application Startup` 时失败；
- 当前失败发生在历史迁移链中间，不确定是本次修改、历史迁移兼容性，还是测试环境问题；
- 目前没有证据证明产品 WHAT / WHY 发生变化。

请按当前方法说明：

1. 应进入普通执行修复、`systematic-debug`、Stage Return 还是其他路径；
2. 需要读取哪些 Skill / Rule / Authority；
3. 如何区分实现缺陷、陈旧验证契约、运行环境问题和上游权威问题；
4. 最小根因调查步骤；
5. 哪些证据可以证明修复完成；
6. 为什么已有的编译 / 增量迁移 / 已有数据库启动证据是否足够；
7. 哪些新发现会触发返回 Specification 或 Technical Planning。

最后单独列出你实际读取的 Repository 文件。不要讨论规则治理 v2 候选方案。
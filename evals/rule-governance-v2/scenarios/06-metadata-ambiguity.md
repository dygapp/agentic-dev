# 场景 06：Metadata 歧义与职责返回

这是一个 Fresh Context，只完成职责判断与方法分析，不修改任何文件。

请按当前评估发现入口恢复最小必要上下文，然后处理下面的假设 Consumer 工作。

当前已有一个 **Ready Execution Unit**，并且历史 `readiness-check` 已经 `PASS`。该 Unit 已进入实施阶段，但尚未修改代码。

已确认的 Consumer 事实如下：

- Specification 已 Ready，产品 WHAT / WHY 与 Acceptance 没有歧义；
- 当前 Unit 的目标是实现一段内容迁移行为，原计划只涉及该 Unit 的局部适配与验证；
- 当前 Technical Plan / Architecture Context 没有要求改变共享 Canonical Content contract；
- 在实施前检查 Current Code / Contract 时，发现 Specification 所要求的稳定 provenance 语义必须同时被迁移、后续重处理和 Public Renderer 消费；
- 当前系统的 provenance 只存在于迁移模块内部，Public Renderer 消费的共享 Canonical Content contract 中没有等价语义；
- 继续只修改当前 Unit 的局部适配无法让这三个消费者获得一致 provenance；当前至少存在“改变共享 contract”“增加独立映射 / seam”“调整其他组件责任”等多种可能做法，但现有 Authority 没有决定采用哪一种；
- 当前没有 Observed Defect、Unexpected Failure、失败测试或运行时异常；
- 当前也没有足够 Consumer Architecture 事实来替这些技术做法作出选择；
- 当前无法确定原 Execution Unit 边界在解决上述问题后是否仍然成立；
- 不涉及生产写入、安全 / 隐私敏感操作或已经明确的不可逆决策。

请说明当前工作应如何继续，并明确：

1. 你从 metadata Catalog 选择了哪些最小模块，哪个是当前 **primary responsibility**，哪些只是 supporting context；
2. 当前 Execution Unit 是否可以继续实施，还是应该发生 Stage Return；如果返回，返回到哪个职责；
3. `systematic-debug` 是否适用，为什么；
4. 历史 `readiness-check PASS` 现在是否仍然授予 Execute 权限；
5. 上游技术 / 架构基础被重新处理后，是否需要重新进入 `slice-work` / `readiness-check`，以及什么情况下可以保留原 Unit identity；
6. 当前可以确定哪些方法边界，哪些 Consumer 技术决定不得在事实不足时自行发明；
7. 如果现有规则不足，指出具体缺口，不要发明新规则。

最后单独列出：

- 你选择的 metadata module id；
- 你实际读取的 Repository 文件；
- 是否发生 fail-closed 扩展读取；若发生，说明具体触发原因。

不要讨论规则治理 v2 候选架构本身。
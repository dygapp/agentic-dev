---
name: clarify-architecture
description: Resolves systemic architecture drivers that span multiple current or expected features and would otherwise block reliable specification or technical planning. Use for durable, high-cost-to-reverse structural decisions; do not use for local reversible implementation choices or ordinary feature technical planning.
---

# clarify-architecture

## 目的

只解决跨多个当前或预期 Feature 持续成立、长期、高返工成本或高成本难逆，并且不解决就会阻塞可靠 Specification / Technical Planning 的系统性架构问题。

## 输入

- Current Requirement Authority；
- Systemic architecture drivers；
- 当前 Architecture / ADR / code evidence；
- Consumer-local constraints。

## 流程

1. 确认问题确实跨多个当前或预期 Feature、具有长期结构价值、高返工成本或高成本难逆，并且不解决就会阻塞可靠 Specification / Technical Planning；局部可逆实现选择、文件组织和普通 framework usage 不进入本 Skill。
2. 读取当前 Requirement、Architecture / ADR、接口和必要代码事实；实现与成熟 reference implementation 可以作为 evidence / oracle，但不能自动覆盖更高层 Authority。
3. 建立最小 Architecture Context，只解决真实 systemic driver，不做 Big Design Up Front。
4. 比较能够真实解决 driver 的少量结构选项，明确责任边界、stable contract、Authority 已决定的 failure semantics、迁移 / replaceability seam 与主要权衡。Requirement 没有决定的业务失败、回退、切换时点、缓存期限或一次操作内快照语义，不得由 Architecture 自行补齐。
5. 将稳定决定写回真实 Architecture owner；只有背景、权衡或替代关系具有长期价值时才形成 / 更新 ADR。新增、替换或退役长期 owner 时同步检查 locator、navigation、verification consumer 与 current-state wording，避免旧 owner 继续成为 Current truth。
6. 若分析暴露业务多解、产品边界、长期 Requirement fact 缺失或 Requirement conflict，返回 Requirement owner；不在本 Skill 内创造 Product Requirement。尤其当 Requirement 只规定“全局一致 / 单一事实来源”等业务目标时，Architecture 可以定义单一责任边界与稳定读取 contract，但不能自行决定 fail-open / fail-closed、last-known fallback、切换生效时点、事务内快照等会改变可观察业务语义的规则。
7. 高影响、难逆 Architecture 变化按 Consumer Repository policy 进入 fresh / independent `review-change`；独立复核本身不要求额外 provider 或模型，除非 review claim 确实是 Runtime-specific。
8. 只有当前 Authority、必要验证与 lifecycle transition 都支持目标状态时才声明 Architecture Context Ready；单个分析步骤或文档写入完成不等于本 Skill 完成。

## 输出

- Current Architecture decision / context；
- 必要 ADR；
- Requirement-return items；
- Remaining architecture blockers；
- Architecture Context Ready 或未就绪结论。

## 退出条件

系统性 driver 已被稳定 Authority 解决，后续 Feature 可以在不重新讨论同一长期结构问题的情况下可靠 Specification / Technical Planning。

## 升级

重大产品边界、未授权高影响取舍、跨组织 contract 或其他 Repository Authority 明确保留给人工的决定必须升级。发出人工请求前先检查当前 Authority、Evidence 与已授权自动路径，并把请求缩到最小不可替代决定。本 Skill 不执行 Feature implementation。

---
name: slice-work
description: Turns a ready specification, applicable current authority, and optional technical plan into bounded, traceable, context-fit execution units with observable completion conditions and explicit dependencies. Use before readiness checking or when convergence exposes implementation gaps that need new or corrected execution work.
---

# slice-work

## 目的

把当前 Ready Specification、必要 Technical Plan 与当前责任实际适用的 Consumer Current Authority 切成新上下文可以独立理解、实现和验证的 Execution Units。

## 输入

- Ready Specification；
- Optional Technical Plan / Architecture decisions；
- 当前责任实际适用的 Consumer Current Authority 与可恢复 locator / navigation；
- 当前仓库结构与已知依赖；
- Consumer-local constraints。

## 流程

1. 结合 Ready Specification、必要 Technical Plan、当前 task / claim、Consumer locator / navigation 与当前责任实际适用的 Current Authority，提取必须实现的 Observable Behavior、Acceptance、其他语义义务和 Verification responsibility；不因为 Provider 未预先命名某个 Authority 类型就忽略它。
2. 优先形成窄而完整的纵向单元，避免按数据库 / 后端 / 前端 / 测试机械横切；只有真实依赖要求时才拆分基础单元。
3. 每个 Unit 明确 Scope、Authority inputs / 可恢复 Current owner 线索、Dependencies、Completion Conditions、Verification responsibility 与明确 Out of Scope。Authority inputs 只记录切分时已知的恢复线索，不复制 Authority 正文，也不冻结后续所有适用 owner；不得把未解决产品歧义、长期 Authority 决定或共享高影响风险伪装成“执行时再说”。
4. 检查 context-fit：新的 Fresh Context Agent 能从该 Unit 的责任与恢复线索出发，结合当前 Consumer locator 和 Repository facts 重新判断适用 Current Authority，只读取最小必要内容后完成理解、实现、验证；不依赖隐藏聊天历史或上一个 Unit 的隐式推理。
5. 明确依赖顺序与 observable handoff，但不得把未来 Unit 的 Execute Authority、merge / release / deploy 权限提前授予当前 Unit。
6. 逐个 Unit 完成边界检查后重新计算剩余切分责任；只要仍有隐藏跨 Unit 完成责任或可自动消除的模糊边界，就继续收敛。

## 输出

- Ordered Execution Units；
- Explicit dependencies / blockers。

## 退出条件

每个 Unit 边界可独立执行、可验证、可追溯且 context-fit；不存在隐含的跨 Unit 完成责任。

## 升级

切分暴露未解决的产品歧义时返回 `clarify-intent` / `specify`，暴露系统性 Requirement Baseline gap 时返回 `establish-requirement-baseline`，暴露长期系统性架构 driver 时返回 `clarify-architecture`，暴露必须先稳定的跨 Unit HOW 时返回 `technical-plan`；其他长期语义缺口返回 Consumer 当前真实 owner / maintenance procedure。需要人工决定前先验证现有 Authority 与 Evidence 是否足够；Skill 不执行 Unit。

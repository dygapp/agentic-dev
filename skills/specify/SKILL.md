---
name: specify
description: Creates or incrementally updates an authoritative WHAT/WHY specification and evaluates durable domain-fact candidates under repository authority. Use when intent is ready, required behavior needs to be explicit for a fresh agent, or a domain-authority candidate or conflict must be validated and routed.
---

# specify

## 目的

把已澄清意图收敛成可由新上下文独立理解和验收的 WHAT / WHY Specification，并识别需要进入长期 Domain Authority 的候选事实。

## 输入

- Clarified Intent；
- 当前 Repository / Domain Authority，以及会改变本次 WHAT / WHY / Acceptance 的其他适用 Consumer Current Authority（如存在）；
- Existing Specification（增量修改时）；
- Consumer-local constraints。

## 流程

1. 读取当前 Repository / Product / Requirement / Domain Authority、会改变本次 WHAT / WHY / Acceptance 的其他适用 Consumer Current Authority、Consumer-local constraints 与已有 Specification，确认目标、范围与现有行为；locator / index 只用于找到真实 owner，不把导航或分析资产当作事实正文。
2. 写明 Goal、In / Out of Scope、Observable Behavior、Business Rules、Boundary / Failure Behavior、Acceptance Criteria 与必要非功能义务，使新的 Fresh Context 能判断“做什么、什么不做、何时完成”。
3. 把 HOW、文件路径、类 / 函数、框架细节和施工顺序留给 `technical-plan` / `execute-unit`，除非它们本身是外部 contract 或产品可观察约束。
4. 对跨 Feature 长期业务术语、不变量或规则形成 Domain / Requirement Authority Candidate；只有当前仓库授权允许且 owner 唯一时才更新长期 Authority。临时分析、对照表、评审草稿和派生视图默认非 Authority，不让同一事实形成第二个 Current owner。
5. 新增长期 owner 或替换 / 退役旧 owner 时检查 locator / navigation、verification consumer 与 durable current-state wording 是否同步，确保 Historical / provenance reference 不被 ordinary runtime 当成 Current truth。
6. 若 Specification 分析暴露多个 Feature 共同依赖的 Requirement Baseline gap / conflict / ownership failure，返回 `establish-requirement-baseline`；若暴露长期、高成本难逆且阻塞可靠开发的 systemic architecture driver，返回 `clarify-architecture`；若长期语义属于 Consumer 已存在的其他 Current owner，则返回该 owner / maintenance procedure，不把专项语义塞进当前 Feature Specification。
7. 只要仍存在可由当前 Authority 自动裁决、会改变 WHAT / WHY / Acceptance 的歧义就继续收敛；只有不可替代的 Product / Domain 决定才请求人工。

## 输出

- Current Specification；
- Domain Authority Candidates / updates（如有）；
- Remaining blockers（如有）。

## 退出条件

Specification 已足以支持后续技术规划或工作切分，且不存在会改变目标、范围、行为或验收的未解决高影响歧义。

## 升级

Repository / Domain Authority 冲突、产品意图需要改变、或长期领域事实更新超出当前授权时升级。请求人工前先验证当前 Authority、Repository facts 和 Evidence 是否已经能够裁决，并把请求缩到最小不可替代决定。Skill 不自动进入 Technical Planning 或 Execute。

---
name: specify
description: Creates or incrementally updates an authoritative WHAT/WHY specification and evaluates durable domain-fact candidates under repository authority. Use when intent is ready, required behavior needs to be explicit for a fresh agent, or a domain-authority candidate or conflict must be validated and routed.
metadata:
  agentic-dev-id: "skill:specify"
  agentic-dev-type: "skill"
  agentic-dev-status: "active"
---

# specify

## Purpose

把已澄清意图收敛成可由新上下文独立理解和验收的 WHAT / WHY Specification，并识别需要进入长期 Domain Authority 的候选事实。

## Inputs

- Clarified Intent；
- 当前 Repository / Domain Authority；
- Existing Specification（增量修改时）；
- 当前任务适用的 Rule candidates。

## Procedure

1. 读取当前权威和已有 Specification，确认目标、范围与现有行为。
2. 通过 Rule Discovery 加载当前规格工作真正适用的 Rules。
3. 写明 Goal、In/Out of Scope、Observable Behavior、Business Rules、Boundary/Failure Behavior、Acceptance Criteria 与必要非功能义务。
4. 把 HOW、文件路径、类/函数、框架细节等实现选择留给 Technical Planning / Execute，除非它们本身是外部强制约束。
5. 对跨功能长期业务术语、不变量或规则形成 Domain Authority Candidate；只有当前仓库授权允许时才更新长期 Authority。
6. 检查 Fresh Context 是否能据此判断“做什么、什么不做、何时完成、是否仍有关键歧义”。

## Outputs

- Current Specification；
- Domain Authority Candidates / updates（如有）；
- Remaining blockers（如有）。

## Exit Conditions

Specification 已足以支持后续技术规划或工作切分，且不存在会改变目标、范围、行为或验收的未解决高影响歧义。

## Escalation

Repository / Domain Authority 冲突、产品意图需要改变、或长期领域事实更新超出当前授权时升级。Skill 不自动进入 Technical Planning 或 Execute。

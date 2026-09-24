---
name: clarify-intent
description: Clarifies only product-intent ambiguities that materially affect goal, scope, user-visible behavior, business boundaries, acceptance, or significant non-functional obligations. Use before specification when current authority cannot resolve a high-impact product decision; do not use for ordinary reversible implementation choices.
---

# clarify-intent

## 目的

只解决定义正确 Product Intent 所必需的高影响歧义，使后续 `specify` 可以在不猜测 Goal、Scope、Observable Behavior 或 Acceptance 的情况下工作。

## 输入

- Requested Outcome；
- Current Repository / Product / Domain Authority；
- Relevant System Context；
- Consumer-local constraints。

## 流程

1. 从当前 Authority 与请求中恢复 Goal、Known Scope、已确认决定和直接相关事实；Conversation History 不单独构成 Authority，并应用当前 Consumer-local constraints。
2. 只保留会实质改变 Goal、Scope、用户可见行为、业务边界、Acceptance 或重大非功能义务的歧义；普通低影响、可逆实现选择留给后续技术规划或执行。
3. 先用现有 Authority、Repository facts 与可恢复 Evidence 解决问题。若多个 Feature 共同暴露 Requirement Baseline gap / conflict / ownership failure，返回 `establish-requirement-baseline`；若共同依赖长期、高成本难逆的 architecture driver，返回 `clarify-architecture`，不把系统性问题伪装成本 Feature 的人工问题。
4. 只有当前 Authority 无法裁决、不同合理答案会产生实质不同产品结果且问题确实阻塞当前 intent 时，才形成最小 Human Blocking Question。请求人工前先检查当前可用的已授权工具 / Evidence 路径，避免让人工承担机械中转。
5. 收敛 Confirmed Intent，并标记可能具有跨功能长期价值的 Domain Authority Candidate；本 Skill 不自行把候选提升为长期权威。
6. 子问题、工具调用或单次答复结束后重新判断剩余歧义；只要仍有本 Skill 可自动关闭的责任就继续处理。
7. 若不存在仍会实质改变 Product Intent / Acceptance 的未决问题，则结束并交给 `specify`；否则停在当前职责边界等待不可替代的权威决定。

## 输出

- Clarified Goal / Scope / Observable Behaviors；
- Confirmed Product Decisions；
- Domain Authority Candidates（如有）；
- Remaining Blocking Questions（如有）。

## 退出条件

当前信息足以让 `specify` 定义 WHAT / WHY，且不存在会实质改变 Goal、Scope、Product Behavior 或 Acceptance 的未解决高影响歧义。

## 升级

Authoritative Sources 冲突、Agent 未获授权的高影响产品选择、显著安全 / 隐私 / 不可逆后果或其他必须由 Human Authority 决定的 Product Intent 必须升级；请求必须说明为什么自动化 / Evidence 路径不足、需要人类返回的最小决定以及收到决定后仍由 Agent 自动继续的步骤。普通低影响、可逆实现不确定性不升级。

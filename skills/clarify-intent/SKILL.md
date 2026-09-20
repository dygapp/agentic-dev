---
name: clarify-intent
description: Clarifies only product-intent ambiguities that materially affect goal, scope, user-visible behavior, business boundaries, acceptance, or significant non-functional obligations. Use before specification when current authority cannot resolve a high-impact product decision; do not use for ordinary reversible implementation choices.
metadata:
  agentic-dev-id: "skill:clarify-intent"
  agentic-dev-type: "skill"
  agentic-dev-status: "active"
  agentic-dev-distribution: "release-direct"
  agentic-dev-release-target: "software-development"
  agentic-dev-release-inputs: "method:ai-development;rule:human-intervention-necessity"
---

# clarify-intent

## 目的

只解决定义正确 Product Intent 所必需的高影响歧义，使后续 `specify` 可以在不猜测 Goal、Scope、Observable Behavior 或 Acceptance 的情况下工作。

## 输入

- Requested Outcome；
- Current Repository / Product / Domain Authority；
- Relevant System Context；
- 当前运行环境提供的适用约束 / references 与 Consumer-local policy。

## 流程

1. 从当前 Authority 与请求中恢复 Goal、Known Scope、已确认决定和直接相关事实；Conversation History 不单独构成 Authority。
2. 读取并应用当前运行环境为本职责提供的适用约束；Consumer Release 使用随 Skill 打包的 references 与 Consumer-local policy，provider runtime 服从当前 Repository Bootstrap。
3. 只保留会实质改变 Goal、Scope、用户可见行为、业务边界、Acceptance 或重大非功能义务的歧义；普通低影响、可逆实现选择留给后续阶段。
4. 先用现有 Authority 解决问题；只有当前 Authority 无法裁决且不同合理答案会产生实质不同产品结果时，才形成最小 Human Blocking Question。
5. 收敛 Confirmed Intent，并标记可能具有跨功能长期价值的 Domain Authority Candidate；本 Skill 不自行把候选提升为长期权威。
6. 若不存在仍会实质改变 Product Intent / Acceptance 的未决问题，则结束并交给 `specify`；否则停在当前职责边界等待权威决定。

## 输出

- Clarified Goal / Scope / Observable Behaviors；
- Confirmed Product Decisions；
- Domain Authority Candidates（如有）；
- Remaining Blocking Questions（如有）。

## 退出条件

当前信息足以让 `specify` 定义 WHAT / WHY，且不存在会实质改变 Goal、Scope、Product Behavior 或 Acceptance 的未解决高影响歧义。

## 升级

Authoritative Sources 冲突、Agent 未获授权的高影响产品选择、显著安全 / 隐私 / 不可逆后果或其他必须由 Human Authority 决定的 Product Intent 必须升级。普通低影响、可逆实现不确定性不升级。

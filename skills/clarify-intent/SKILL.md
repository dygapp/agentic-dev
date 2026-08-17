# clarify-intent

## Purpose

只解决定义正确 Product Intent 所必需的关键歧义，使后续 `specify` 可以在不猜测 Goal、Scope、Product Behavior 或 Acceptance 的情况下工作。

本 Skill 不追求消除所有不确定性。普通、低影响、可逆的实现细节留给后续技术或执行阶段处理。

## Use When

- 新 Feature / Change 仍存在可能显著改变 Goal、Scope、User-visible Behavior、Business Boundary、Acceptance Result 或 Significant Non-functional Obligation 的问题；
- Existing Intent 因新信息、冲突或范围变化需要重新确认；
- Execute / Debug / Converge 发现上游 Product Intent 不明确并发生阶段回退；
- 用户提出的目标可以理解，但存在少量高影响解释分支，需要先收敛再进入 Specification。

## Do Not Use When

- 仅剩普通、低影响、可逆的实现细节；
- 问题已经属于纯技术设计或实现选择；
- Intent 已足够明确，只需要结构化为 WHAT / WHY Specification；
- 当前目标是创建 Technical Plan、Execution Units、代码或测试；
- 只是希望“把所有可能问题都问完”，而这些问题不会 materially affect Product Intent / Acceptance。

如果 Intent 已满足 Exit Condition，应快速输出 Clarified Intent 并结束，不制造额外讨论流程。

## Inputs

- Requested Outcome
- Relevant System / Domain Context
- Applicable Governance / Authority
- Known Scope

Existing Intent、Existing Specification 或阶段回退信息可以作为相关上下文输入，但仍必须按 Repository Authority Hierarchy 判断其权威性。

## Authority Sources

遵循当前 Repository Authority Hierarchy，并坚持 Authority First。

处理 Intent 时遵守以下规则：

1. Repository / Domain / Existing Product Authority 优先于 Conversation History。
2. 已明确确认的 Product Decision 不因为新的实现便利性而被静默改写。
3. Current System State 可以帮助理解现状，但不能反向定义未经确认的 Product Intent。
4. Conversation History 只可帮助定位工作线索，不能单独成为权威事实来源。
5. 不把推测、常见做法或实现偏好提升为 Confirmed Product Decision。

如果 Authoritative Sources Conflict，停止收敛相关问题并升级，不自行选择一个方便实现的解释。

## Procedure

### 1. Establish the Intent Frame

从当前最小权威上下文中提取：

- Requested Outcome；
- 当前可确认的 Goal；
- Known Scope；
- 已确认约束；
- 已确认 Product Decisions；
- 与当前请求直接相关的 System / Domain Facts。

区分：

- **Confirmed**：有当前权威支持；
- **Unresolved**：存在多个合理解释或缺少必要决定；
- **Implementation Detail**：不需要在 Intent 阶段决定。

不要把未确认假设写成 Confirmed Decision。

### 2. Apply the Materiality Filter

只把可能 materially affect 以下内容的问题视为 Intent 候选问题：

- Product Goal；
- In Scope / Out of Scope；
- User-visible Behavior；
- Business Boundary；
- Acceptance Result；
- Significant Non-functional Obligation。

对于每个候选问题，判断：

> 不同合理答案是否会让后续 Specification 描述出实质不同的产品结果？

如果不会，则通常不是 Blocking Intent Question。

### 3. Resolve from Existing Authority First

在询问 Human 之前，先检查当前可用权威是否已经给出答案。

如果可以由 Repository / Domain / Existing Product Authority 明确判断：

- 直接记录为 Confirmed Product Decision；
- 保留必要的 Authority Trace；
- 不重复向 Human 询问已经有权威答案的问题。

如果只能从 Conversation History、习惯做法或推测得到答案，则仍视为未确认。

### 4. Filter Implementation Uncertainty

以下类型默认不作为 Intent Blocking Question：

- 普通 Code Structure；
- 局部算法或库选择；
- 文件、类、函数命名；
- 普通测试组织方式；
- 可逆的本地实现选择；
- 不改变 User-visible Behavior 的低影响技术细节。

这类问题由后续 `technical-plan`、Execute 或其他适当职责处理。

不要因为“现在还不知道怎么实现”就把问题错误升级为 Product Intent 歧义。

### 5. Identify True Blocking Questions

只有同时满足以下条件的问题才保留为 Blocking Question：

1. 存在两个或更多合理解释，或缺少必要 Product Decision；
2. 不同答案会 materially affect Goal、Scope、Behavior、Boundary、Acceptance 或重大非功能义务；
3. 现有权威无法安全确定答案；
4. Agent 没有权限自行选择该高影响产品解释。

典型 Blocking Question 包括：

- 两种用户可见行为都合理，但产品必须选择其一；
- Scope 是否包含某类用户、流程或结果会改变验收范围；
- Failure / Boundary 行为不同会产生实质不同业务结果；
- Existing Intent 与更高权威来源发生冲突；
- 必须改变已经确认的 Product Intent 才能继续。

### 6. Ask Only the Minimum Necessary Human Questions

对必须由 Human Authority 决定的 Blocking Questions：

- 只提出解除当前 Intent 阻塞所需的问题；
- 明确问题会影响的 Product Dimension；
- 在必要时列出已经由权威支持的有限候选解释；
- 不夹带纯实现问题；
- 不为了未来可能性提前扩展问题范围。

如果多个问题互相独立，只保留当前进入 Specification 必须解决的集合。

### 7. Converge Confirmed Product Intent

将当前已经确认的 Intent 收敛为：

- Goal；
- In Scope；
- Out of Scope；
- Key Observable Behaviors；
- Confirmed Product Decisions；
- Remaining Blocking Questions（如有）。

输出应尽量简洁，只保留后续 `specify` 真正需要的 Product Intent 信息。

本步骤不创建完整 Acceptance Criteria、Business Rule 结构或技术方案；这些属于后续职责。

### 8. Evaluate Exit Condition

检查是否仍存在会显著改变以下内容的关键未决问题：

- Goal；
- Scope；
- Product Behavior；
- Acceptance Result。

如果不存在，`clarify-intent` 完成，输出可以直接交给 `specify`。

如果仍存在，保留 Remaining Blocking Questions 并停止在当前阶段；不要通过猜测答案制造完成状态。

## Outputs

输出 Clarified Intent：

```text
Goal:
- <intended outcome>

In Scope:
- <included boundary or behavior>

Out of Scope:
- <explicitly excluded boundary, if relevant>

Key Observable Behaviors:
- <user/system observable behavior>

Confirmed Product Decisions:
- <confirmed decision and concise authority basis when useful>

Remaining Blocking Questions:
- <question, affected product dimension, and why it blocks>  # only if any
```

如果某一可选部分没有内容，不为了填满模板而发明信息。

该输出是 `specify` 的输入，不替代正式 Specification，也不要求独立永久持久化。

## Exit Conditions

不存在会显著改变 Goal、Scope、Product Behavior 或 Acceptance Result 的关键未决问题。

满足 Exit Condition 时：

- Goal 与 Scope 足以进入 Specification；
- 关键 Observable Behaviors 已可识别；
- 已确认 Product Decisions 与未决问题没有混淆；
- 不需要 Human 再回答任何会 materially change Product Intent / Acceptance 的问题。

如果仍有 Remaining Blocking Questions，则本 Skill 尚未满足 Exit Condition。

## Escalation Conditions

出现以下情况时必须升级：

- 多种合理解释会产生 materially different User-visible Behavior；
- Scope / Intent 需要改变或重新确认；
- Authoritative Sources Conflict；
- 决策属于 Agent 未获授权的高影响 Product Choice；
- 涉及显著外部影响、不可逆后果、安全 / 隐私或其他必须由 Human / Explicit Policy 决定的 Product Intent。

普通、低影响、可逆的实现不确定性不升级给 Human。

## Context Rules

- Authority First；
- Progressive Disclosure，只加载解决当前 Intent 歧义所需的最小上下文；
- 不依赖完整 Conversation History；
- Conversation History 不作为权威事实来源；
- 不默认执行 Code Inspection；只有已存在的权威 System Context 对 Intent 判断确有必要时才读取相关上下文；
- 不生成大篇幅永久讨论记录；
- 不要求为 Clarification 单独创建永久 Artifact；
- Existing Intent 重新确认时优先增量加载受影响部分，不重建无关上下文；
- 阶段回退时只重新澄清暴露出的 Product Intent 问题，不重新开启已经稳定的无关决策；
- 不自动调用 `specify` 或接管后续生命周期。

## Allowed Sub-skills / Disciplines

- Context Discipline
- Human Escalation

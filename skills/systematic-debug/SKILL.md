---
name: systematic-debug
description: Investigates an observed defect or unexpected failure through reproduction, authority-backed expected-versus-actual analysis, falsifiable root-cause hypotheses, minimal fix, and regression evidence. Use for unexpected failures or standalone defect work; not for expected initial TDD failures or undefined product behavior.
---

# systematic-debug

## Purpose

对 Observed Defect 或 Unexpected Failure 进行基于证据、可证伪的 Root-cause Investigation，并实施满足既有 Expected Behavior 所需的最小 Root-cause Fix。

本 Skill 不是连续 Patch 尝试流程。Debug 必须建立 Expected vs Actual、可重复 Failure Evidence、可证伪 Hypothesis 和当前 Regression Evidence。

## Use When

- 已存在可观察的 Defect / Symptom / Failure；
- `execute-unit` 在正常实施或 Targeted Verification 中遇到 Unexpected Failure；
- 独立缺陷工作需要执行 Reproduce → Diagnose → Fix → Regression；
- 一个既有行为曾经满足权威要求，但当前系统状态表现出与 Expected Behavior 不一致的结果。

## Do Not Use When

- 当前只是 TDD 中为了驱动实现而预期出现的初始 Failing Evidence；
- Expected Behavior 尚未定义或存在 Product / Requirement 冲突；此时应先返回 `clarify-intent` / `specify`；
- 已知修复必须重新决定 Major Architecture Direction；此时应进入 `technical-plan` / Human Authority；
- 已知修复需要更新 Architecture Context 或形成新的长期架构决策；此时应进入 `technical-plan` 完成 Architecture Authority 更新与必要 ADR 评估；
- 当前目标只是实现正常 Execution Unit，而没有 Unexpected Failure；
- 目标是通过尝试多个 Patch 找到“哪个看起来能过”，而不调查 Root Cause。

## Inputs

- Observed Symptom
- Expected Behavior / Authority
- Reproduction Environment
- Relevant Domain / Architecture / ADR Authority
- Relevant Code / System State

按需还可以读取与 Failure 直接相关的测试、日志、Runtime Evidence、Configuration、Data State 或 External Dependency Evidence，但只加载形成 Root-cause 判断所需的最小上下文。

## Authority Sources

遵循当前 Repository Authority Hierarchy，并坚持 Authority First。

Debug 时遵守以下规则：

1. Expected Behavior 必须来自 Applicable Product / Domain / Governance / Specification Authority。
2. Current Code、Tests、Runtime State 和日志用于解释 Actual Behavior，不得自行定义 Expected Behavior。
3. Existing Test、Workflow assertion 或其他 Verification Artifact 只有在其行为与更高权威一致时才能作为 Expected Behavior 的证据；它们自身也可能陈旧。
4. Technical Plan / Architecture Context / ADR 可以约束修复方式，但不得覆盖 Product Intent；当前 Debug Fix 不得静默覆盖当前有效 Domain / Architecture / ADR Authority。
5. Conversation History 不构成权威事实来源。
6. 如果 Expected Behavior 与权威来源冲突或本身未定义，停止 Debug Fix，返回上游处理。

## Procedure

### 1. Establish the Observed Failure

明确当前可观察的问题：

- 发生了什么；
- 在什么条件下发生；
- 影响的行为或结果；
- 当前已有的 Failure Evidence。

不要从“可能是某段代码有问题”开始；先从可观察 Symptom 开始。

### 2. Reproduce First

在最小可控上下文中尝试复现问题，并记录足够稳定的 Reproduction Evidence。

优先缩小：

- 输入；
- 状态；
- 执行路径；
- 依赖；
- 环境差异。

在没有足够证据确认问题真实存在、且与当前调查对象相关之前，不进入修复。

如果问题暂时无法稳定复现，应继续收集能区分 Hypothesis 的当前证据，而不是直接猜 Patch。无法形成足够 Failure Evidence 时，不得声明已定位 Root Cause。

### 3. Establish Expected vs Actual

分别写清：

```text
Expected:
- <authority-supported behavior>

Actual:
- <currently observed behavior>
```

检查 Expected Behavior 是否有明确 Authority Trace。

如果当前 Failure 来自 Test、Workflow assertion、fixture、snapshot 或其他 Verification Artifact，而该 Artifact 与当前更高优先级 Authority / Specification 冲突，应将根因候选明确分类为 **陈旧验证契约（Stale Verification Contract）**：

- 修正拥有过期断言的验证层，不修改产品实现去恢复已被取代的旧行为；
- 如果同一产品语义在多个验证层重复维护，识别真正的契约所有者，并删除无必要重复或让重复检查共享同一权威来源；
- 修正后重新运行当前有效验证，确认新契约能证明当前 Expected Behavior，同时没有掩盖真实实现缺陷；
- 不因为“测试可能陈旧”就默认忽略失败；分类仍必须由 Authority Trace 与当前证据支持。

如果 Expected Behavior：

- 未定义；
- 存在多个 materially different 的合理解释；
- 与更高权威冲突；

则停止当前 Debug Fix，返回 `clarify-intent` / `specify`，必要时升级 Human Authority。

### 4. Inspect the Failure Path

使用 Progressive Disclosure 检查与 Failure 直接相关的系统状态，例如：

- Relevant Code Path；
- Relevant Tests；
- Data / State Transitions；
- Configuration；
- Logs / Runtime Evidence；
- Relevant Interfaces / Dependencies。

目标是解释 Actual Behavior 如何形成，不是全面阅读代码库。

### 5. Form a Falsifiable Hypothesis

基于当前证据提出能够被证伪的 Root-cause Hypothesis。

一个有效 Hypothesis 应说明：

- 被怀疑的 Cause；
- 它如何导致当前 Actual Behavior；
- 如果 Hypothesis 正确，应该观察到什么证据；
- 什么结果会否定该 Hypothesis。

避免使用无法验证的表述，例如“可能哪里有缓存问题”或“这段代码看起来不对”。

### 6. Test the Hypothesis

通过最小、针对性的观察、测试或实验验证 Hypothesis。

优先使用能够区分竞争解释的证据，不通过一次性大范围修改来“看看是否变好”。

如果证据否定 Hypothesis：

- 保留有价值的调查事实；
- 放弃该 Hypothesis；
- 基于新证据形成新的可证伪 Hypothesis。

不要为了维护先前判断而忽略反证。

### 7. Establish Failing / Reproduction Evidence

在应用修复前，确保存在当前证据能够证明：

- Actual Behavior 与 Expected Behavior 不一致；
- 当前调查对象确实触发该问题；
- 修复前状态可以被后续 Regression Verification 对照。

已有稳定的自动化失败测试时可以复用；没有时可以使用其他可重复、可观察的当前 Failure Evidence。

本步骤不要求为了形式强制新增某一种测试框架。

### 8. Apply the Minimal Root-cause Fix

只修改消除已验证 Root Cause 所需的最小范围。

修复应：

- 恢复权威 Expected Behavior；
- 不新增未授权 Product Scope；
- 不通过特殊分支掩盖更深层 Cause；
- 避免无关重构扩大验证面；
- 遵守 Existing Architecture / Durable Technical Decisions / 当前有效 ADR。

如果真正修复要求 materially change Product Intent / Scope，停止并返回上游。

如果真正修复要求 Major Architecture Direction，停止并进入 `technical-plan` / Human Authority，而不是在 Debug Patch 中静默完成重大设计变更。

如果调查发现 Expected Behavior 依赖的长期领域事实缺失、冲突或失效，应停止在 Debug Patch 中提升业务权威，返回 `clarify-intent` / `specify` 完成候选验证和 Domain Authority 路由。

如果调查发现修复需要更新跨功能持续有效的 Architecture Context 或形成新的长期架构决策，即使该变化本身尚未达到 Human Escalation 条件，也应停止在 Debug 中继续固化，返回 `technical-plan` 完成 Architecture Authority 更新与必要 ADR 评估。

### 9. Run Regression Verification

在修复后的当前系统状态重新运行与问题直接相关的验证。

至少确认：

- 原 Failure / Reproduction Evidence 现在满足 Expected Behavior；
- Root Cause 对应路径已被修复；
- 与修复直接相关的重要既有行为没有被破坏。

Regression Evidence 必须来自修复后的当前状态；不能用历史通过记录代替。

### 10. Review When Risk Warrants

当修复影响范围、数据、共享 Contract、安全 / 隐私或其他风险值得额外检查时，执行风险适配的 Review。

Review 不替代 Regression Verification，也不要求固定 Reviewer Agent。

### 11. Produce the Debug Result

输出：

- Root-cause Statement；
- Minimal Fix；
- Regression Evidence；
- Required Stage Return / Escalation（如有）。

只有 Root Cause 已处理且当前 Regression Evidence 支持 Expected Behavior 时，才可以声明 Debug 完成。

## Outputs

### Root-cause Statement

简洁说明：

- 真实 Cause 是什么；
- 为什么它导致 Observed Failure；
- 哪些证据支持该结论。

### Minimal Fix

说明为消除 Root Cause 所做的最小修复，不把无关清理或未来优化混入完成结论。

### Regression Evidence

记录修复后当前状态下支持 Expected Behavior 的验证结果。

### Required Stage Return / Escalation

如果调查发现问题并非局部 Defect，明确返回：

- `clarify-intent` / `specify`：Expected Behavior 未定义、冲突、Product Intent 需要改变，或长期领域事实缺失、冲突、失效；
- `technical-plan`：修复需要 Major / Durable Technical Redesign，或出现新的长期架构状态 / 决策、Architecture Authority / ADR Gap；
- Human / Explicit Policy：动作超出 Authority，或涉及高影响、不可逆、安全 / 隐私、未授权 External / Data Effect。

## Exit Conditions

只有同时满足以下条件，`systematic-debug` 才完成：

- Root Cause 已被当前证据支持并得到处理；
- 修复符合 Applicable Expected Behavior Authority；
- 当前 Regression Evidence 已通过；
- 不存在尚未处理的同一 Root Cause 阻塞项；
- 不存在因本次调查暴露、但尚未返回 `clarify-intent` / `specify` 处理的 Domain Authority Gap；
- 不存在因本次调查暴露、但尚未返回 `technical-plan` 处理的 Architecture Authority / ADR Gap。

仅仅“症状暂时消失”或“某次命令通过”不足以证明 Root Cause 已处理。

## Escalation Conditions

出现以下情况时必须停止并升级或返回上游：

- Expected Behavior 未定义；
- Expected Behavior 与 Authoritative Sources 冲突；
- 修复要求 materially change Product Intent / Scope；
- 修复要求 Major Architecture Direction；
- 需要 Destructive / Hard-to-reverse Data Action；
- Security / Privacy Sensitive Decision；
- 未授权 Shared / Production / External Side Effect；
- Agent 无权执行的其他高影响或不可逆动作。

普通、低影响、可逆且可由当前代码 / 证据判断的局部 Debug 决策由 Agent 自主处理。需要确认长期领域事实时返回 `clarify-intent` / `specify`；需要更新 Architecture Context 或形成新的长期架构决定但未触发 Human Escalation 时，返回 `technical-plan`，不在 Debug 中直接确立长期权威。

## Context Rules

- Authority First；
- Progressive Disclosure，优先使用最小 Reproduction Context；
- Conversation History 不作为权威知识；
- Current Code / Runtime Evidence 解释 Actual Behavior，不定义 Expected Behavior；
- Domain Authority / Technical Plan / Architecture Context / ADR 约束修复路径，不能被局部 Debug Patch 静默覆盖；
- 不通过连续猜 Patch 替代 Root-cause Investigation；
- Hypothesis 必须能够被证据支持或否定；
- Regression Evidence 必须来自修复后的当前状态；
- 不绑定特定 Debugger、Profiler、Tracing、Observability Stack 或 Bug Tracker；
- 不要求永久保存完整 Debug 对话或临时调查笔记；
- 不自动接管整个 Feature、`converge` 或 Integration。

## Allowed Sub-skills / Disciplines

- Verification-before-claim
- Code Review（risk-based discipline）
- Context Discipline
- Human Escalation

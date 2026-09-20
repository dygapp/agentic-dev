---
name: clarify-architecture
description: Resolves systemic architecture drivers that span multiple current or expected features and would otherwise block reliable specification or technical planning. Use for durable, high-cost-to-reverse structural decisions; do not use for local reversible implementation choices or ordinary feature technical planning.
metadata:
  agentic-dev-id: "skill:clarify-architecture"
  agentic-dev-type: "skill"
  agentic-dev-status: "active"
  agentic-dev-distribution: "release-direct"
  agentic-dev-release-target: "software-development"
  agentic-dev-release-inputs: "method:architecture-clarification;rule:human-intervention-necessity;rule:authoritative-artifact-lifecycle-review;rule:high-impact-ai-review-required;rule:evidence-type-must-match-claim;rule:verification-contract-currentness"
---

# clarify-architecture

## 目的

只解决跨多个当前或预期 Feature 持续成立、长期、高返工成本或高成本难逆，并且不解决就会阻塞可靠 Specification / Technical Planning 的系统性架构问题。

## 输入

- Current Requirement Authority；
- Systemic architecture drivers；
- 当前 Architecture / ADR / code evidence；
- 当前运行环境提供的 packaged references 与 Consumer-local policy。

## 流程

1. 确认问题确实跨多个 Feature、具有长期结构价值并阻塞后续开发；局部可逆实现选择不进入本 Skill。
2. 读取当前 Skill package 的架构澄清 Method 与相关 Authority / review / verification references。
3. 从当前 Requirement 与代码 / 接口 /数据事实中建立最小 Architecture Context，不用当前实现自动覆盖更高层 Authority。
4. 比较能够真实解决 driver 的少量结构选项，明确责任边界、稳定 contract、failure semantics、迁移 / replaceability seam 与主要权衡。
5. 将稳定决定写回真实 Architecture owner；只有背景和替代关系具有长期价值时才形成 / 更新 ADR。
6. 若分析暴露业务多解、产品边界或 Requirement conflict，返回 Requirement owner，不在本 Skill 内创造 Product Requirement。
7. 高影响、难逆 Architecture 变化按 Repository policy 进入独立复核，并只在当前证据支持时声明 Architecture Context Ready。

## 输出

- Current Architecture decision / context；
- 必要 ADR；
- Requirement-return items；
- Remaining architecture blockers；
- Architecture Context Ready 或未就绪结论。

## 退出条件

系统性 driver 已被稳定 Authority 解决，后续 Feature 可以在不重新讨论同一长期结构问题的情况下可靠 Specification / Technical Planning。

## 升级

重大产品边界、未授权高影响取舍、跨组织 contract 或其他 Repository Authority 明确保留给人工的决定必须升级。本 Skill 不执行 Feature implementation。

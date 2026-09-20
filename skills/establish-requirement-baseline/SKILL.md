---
name: establish-requirement-baseline
description: Establishes or rebuilds a durable Requirement Baseline from raw, fragmented, conflicting, or weak-authority project inputs. Use for greenfield project establishment or systemic requirement-baseline gaps; do not use for ordinary feature-level intent clarification or specification.
metadata:
  agentic-dev-id: "skill:establish-requirement-baseline"
  agentic-dev-type: "skill"
  agentic-dev-status: "active"
  agentic-dev-distribution: "release-direct"
  agentic-dev-release-target: "software-development"
  agentic-dev-release-inputs: "method:requirement-baseline-establishment;architecture:requirement-authority;rule:human-intervention-necessity;rule:authoritative-artifact-lifecycle-review;rule:high-impact-ai-review-required;rule:evidence-type-must-match-claim;rule:verification-contract-currentness"
---

# establish-requirement-baseline

## 目的

把普通软件项目的原始、碎片化、不同可信度且可能相互冲突的输入，收敛为 Fresh Context 可持续消费的长期 Requirement Authority，并在证据支持时返回 Requirement Baseline Ready。

## 输入

- Raw Project Inputs；
- 当前 Repository / Product / Domain Authority；
- 已有 Requirement 资产与其 currentness / provenance；
- 当前运行环境提供的 packaged references 与 Consumer-local policy。

## 流程

1. 恢复当前 Repository Authority、现有 Requirement owner 和输入来源角色，不把历史实现或旧聊天自动提升为当前事实。
2. 按当前 Skill package 的 `references/release-inputs/**` 恢复需求基线 Method、Requirement Authority 与相关验证 / 人工升级约束。
3. 对原始输入做 source-role、冲突、缺口和重复分析，区分可直接接受事实、可唯一推导事实、设计项和真实阻塞歧义。
4. 把稳定长期事实写入真实 Requirement owner；临时分析、comparison、ambiguity material 保持非 Authority，并明确退出或晋升边界。
5. 只有当前 Authority 无法解决且不同合理答案会改变长期产品语义时，形成最小人工问题；高影响 Authority 变更按当前 Repository policy 进入独立复核。
6. 检查 Requirement 信息架构、Fresh Context 导航、长期 owner、未决项与下游 Feature 可消费性。
7. 只有当前证据支持长期需求基线可被后续工作可靠消费时返回 Requirement Baseline Ready。

## 输出

- Current Requirement Baseline；
- Source / conflict / ambiguity disposition；
- 必要 Authority updates；
- Remaining blockers；
- Requirement Baseline Ready 或未就绪结论。

## 退出条件

长期 Requirement facts 已进入明确 owner，关键冲突与阻塞歧义已关闭或显式保留，下游 Feature 可以在不依赖历史聊天或隐式知识的情况下恢复目标与边界。

## 升级

产品使命、跨域高影响取舍、无法由当前 Authority 裁决的冲突，以及 Repository policy 保留给人工的决定必须升级。本 Skill 不自动进入 Architecture Clarification 或具体 Feature 开发。

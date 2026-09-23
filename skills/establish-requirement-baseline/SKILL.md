---
name: establish-requirement-baseline
description: Establishes or rebuilds a durable Requirement Baseline from raw, fragmented, conflicting, or weak-authority project inputs. Use for greenfield project establishment or systemic requirement-baseline gaps; do not use for ordinary feature-level intent clarification or specification.
---

# establish-requirement-baseline

## 目的

把普通软件项目的原始、碎片化、不同可信度且可能相互冲突的输入，收敛为 Fresh Context 可持续消费的长期 Requirement Authority，并在证据支持时返回 Requirement Baseline Ready。

## 输入

- Raw Project Inputs；
- 当前 Repository / Product / Domain Authority；
- 已有 Requirement 资产与其 currentness / provenance；
- Consumer-local constraints。

## 流程

1. 恢复当前 Repository Authority、现有 Requirement owner、Consumer-local constraints 和输入来源角色；历史实现、旧聊天、分析表、Issue 或迁移材料都不会因为“信息丰富”自动提升为当前 Requirement fact。
2. 建立 single-owner Requirement contract：Human navigation 只解释如何阅读 / 维护；Authority locator / index 只指向唯一 owner；长期 Product / Domain / NFR fact 进入真实 owner；analysis workspace 默认非 Authority。Consumer 可以调整物理目录，但不得让 README、index、草稿或派生视图复制第二套事实。
3. 对原始输入做 source-role、currentness、冲突、缺口和重复分析，区分可直接接受事实、可唯一推导事实、设计项和真实阻塞歧义；不得因为正向事实没有同时声明反向 / 排他边界，就把所有未说明补集制造成 blocker。
4. 把稳定长期事实写入真实 Requirement owner；跨 Feature 长期术语、业务不变量或横向约束只有确有共享语义时才建立 / 更新相应 owner。临时 comparison、ambiguity material、流程图和候选清单保持非 Authority，并明确 promote / archive / delete 边界。
5. 新增、替换或退役长期 owner 时同步检查 locator、Human navigation、verification consumer 与 current-state wording，确保 Fresh Context 能区分 Current truth 与 historical / provenance evidence。
6. 只有当前 Authority 无法解决、不同合理答案会改变长期产品语义，而且问题确实阻塞当前 Baseline scope 或已知下游责任时，才形成最小人工问题；请求人工前先检查 Repository、现有 Evidence 与已授权工具是否已经可以裁决，避免机械中转。
7. 高影响 Requirement Authority 重构按 Consumer Repository policy 进入 fresh / independent `review-change`；Review PASS 不等于人工批准。
8. 检查 Requirement 信息架构、Fresh Context 导航、长期 owner、未决项与下游 Feature 可消费性；单个文档写入或 source inventory 完成不等于 Baseline Ready。
9. 只有当前证据支持长期需求基线可被后续工作可靠消费时返回 Requirement Baseline Ready。

## 输出

- Current Requirement Baseline；
- Source / conflict / ambiguity disposition；
- 必要 Authority updates；
- Remaining blockers；
- Requirement Baseline Ready 或未就绪结论。

## 退出条件

长期 Requirement facts 已进入明确 owner，关键冲突与阻塞歧义已关闭或显式保留，下游 Feature 可以在不依赖历史聊天或隐式知识的情况下恢复目标与边界。

## 升级

产品使命、跨域高影响取舍、无法由当前 Authority 裁决的冲突，以及 Repository policy 保留给人工的决定必须升级；人工请求必须说明自动化 / Evidence 路径为何不足以及需要返回的最小决定。本 Skill 不自动进入 Architecture Clarification 或具体 Feature 开发。

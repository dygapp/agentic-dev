---
id: project:roadmap
type: project
status: active
---

# Project Roadmap

## Current Baseline

当前正式 capability integration baseline 为 **Software Project Clarification v1**：

`integration@6fdcf628abfac3eb306fc9acfce303fd7aee245e`

该 baseline 建立在 V4 Rule Discovery、Capability Model v2、Project Knowledge Model、Rule granularity consolidation 与 Model Collaboration Capability & Adoption v1 之上，并正式加入：

- reusable `method:software-project-clarification`，用于普通软件 Consumer 在多个 Feature 共同依赖的长期 Requirement / Architecture Context 缺失、冲突或需要重建时，执行项目级或重大范围前置澄清；
- `Establish Context → Requirement Clarification → Architecture Clarification? → Clarification Convergence` 四阶段生命周期，以及 fail-closed 的 `Clarified Project Context Ready` 完成语义；
- Requirement Clarification 基于真实 Consumer 正向与负向历史 Evidence，强调 Authority-first、single semantic ownership、高价值歧义筛选、长期事实回写与高风险语义变换的独立复核；
- Architecture Clarification 仅固化 bounded、conditional、anti-BDUF 的最小 contract，用于多个 Feature 在可靠 Specification 前共同依赖的长期 architecture driver，不替代 Feature Technical Planning；
- `method:ai-development` 保持 Feature / change 级职责，系统性 Requirement / Architecture gap 返回长期 owner 或项目级澄清责任，不在 Feature Specification / Technical Planning 中局部创造项目级事实；
- 新 Method 不自动注册到 `agentic-dev` 自身 local Method selector，也没有同步新增 Clarification Skill、Rule、默认 Handoff Artifact 或固定 Consumer schema；
- `docs/guides/using-agentic-dev.md` 已对齐两层 Clarification、Method selection、Consumer-local adoption 与 Requirement / Architecture / Technical Planning 边界；
- PR #134 在语义一致性、Human Guide 对齐和语言规范复核后 squash merge；Post-Integration Rule Discovery Run #106 PASS。

更早里程碑与原因见 `docs/project/project-evolution.md`；具体 capability contract 见其真实 Architecture / Method / Skill / Rule owner。

## Current Evolution

当前没有获得 Planning / Execute Authority 的正式演进单元。

Issue #133 — **Clarification Method Evolution：Requirement Clarification + Architecture Clarification** 已完成：

- Issue #133 已关闭；
- PR #134 已以 integration commit `6fdcf628abfac3eb306fc9acfce303fd7aee245e` squash merge；
- `master` 已指向该 integration commit；
- Post-Integration Rule Discovery Run #106 completed / success；
- 稳定方法结论已进入 Method / Guide owner，本 Roadmap 只保留当前 baseline、候选方向与必要观察。

完整设计、Critical Evidence Synthesis、adversarial review、语言规范复核与集成证据继续由 Issue #133、PR #134、Git 和 Actions 保存，不复制为新的 Project 阶段文档。

## Current Gate

**NONE — 当前没有 active Planning / Execute Gate。**

当前 Repository 可以从已集成 baseline 恢复 ordinary project state；任何下一演进都必须由新的真实 Evidence、明确问题或人工 Authority 建立独立工作入口，不能因为下列候选存在而自动开始。

## Next Candidates

当前可见后续候选只在真实 Evidence 支持时推进：

- **Architecture Clarification evidence evolution**：当前 v1 只有 bounded、conditional、anti-BDUF 的最小 contract；后续从真实 Consumer 的正向、负向和演进型架构案例中校正进入条件与责任细节；
- **Consumer feedback evolution**：继续从 Issue #58 等长期 Consumer Evidence 判断是否需要新增 / 调整 reusable capability；
- **Method selection scaling**：只有 Method 数量或歧义真实增长时，才评估是否需要 metadata discovery / selector tool。

这些候选不因出现在 Roadmap 中自动获得 Planning / Execute Authority。

## Known Observations

- V4-08 的 natural Rule Evolution observation 仍属于 post-adoption future observation，不虚构为已验证；
- Project Capability Profile 是 Repository-local instance owner，需要继续观察其是否保持薄、稳定且不会演变成 runtime catalog；
- Rule / Skill Human inventory 继续由 deterministic tests 与真实 corpus 保持一致，不应迁入 Project Profile；
- Model Collaboration 的成本价值不能从“使用多个模型”本身推断；后续 Consumer adoption 应分别观察 high-capability token、Primary context、total token、wall time、rework 与最终质量；
- 当前 capability integration 不能证明任一具体 Agent 平台的 multi-agent runtime 已通过，真实支持度必须在 adoption 时重新探测；
- Model Collaboration 在真实 Consumer 中的长期 adoption / upgrade / ordinary-runtime 效果仍应由后续 Consumer Evidence 判断，而不是由 upstream self-integration 直接泛化；
- `software-project-clarification` 的 Requirement Clarification 责任有真实 Consumer 历史证据支撑；Architecture Clarification 的 Evidence maturity 较低，当前只允许按最小条件 contract 使用并持续演进；
- reusable Method 存在于 `agentic-dev` corpus 不等于当前 Repository 已自行采用；local selector 仍只描述本 Repository 实际采用的 work kind。

## State Ownership

- 当前 Repository live state：GitHub branch / Issue / PR / Actions；
- 当前项目使命与核心要求：`project-charter.md`；
- 当前 capability instance：`project-capability-profile.md`；
- 当前 evolution / gate / next candidates：本 Roadmap；
- 稳定历史里程碑：`project-evolution.md`。

Roadmap 不保存完整 Architecture、实施日志或完整 Closure Evidence；这些分别回到 capability owner 与 GitHub 历史。
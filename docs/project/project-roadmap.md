---
id: project:roadmap
type: project
status: active
---

# Project Roadmap

## Current Baseline

当前正式 capability integration baseline 为 **Model Collaboration Capability & Adoption v1**：

`integration@385204c8605dd58584ec18456ab8a97d6282b515`

该 baseline 建立在 V4 Rule Discovery、Capability Model v2、Project Knowledge Model 与 Rule granularity consolidation 之上，并正式加入：

- reusable `architecture:model-collaboration`，定义 deterministic-first、能力层级、Primary responsibility、Authority-preserving handoff、single-writer、Evidence-based escalation、fallback 与 runtime claim 边界；
- `method:model-collaboration-adoption`，负责在 collaboration semantics 已进入 Consumer-local Authority 后建立、验证并首次启用 local runtime instance；
- `method:consumer-adoption` / `method:consumer-upgrade` 继续拥有 upstream reusable semantics 的首次接受与 baseline delta assessment，专用 collaboration Method 不得绕过；
- Project Capability Profile 中新增 Model Collaboration selector / instance owner，并保持 `agentic-dev` 当前 self-instance 为 `disabled`；
- Human Guide 与带核验日期的 Codex reference profile，不把平台专项配置提升为跨 Repository Authority；
- functional enablement 与 efficiency / preferred-default claim 明确分离；
- capability classification / Method composition 分析经验进入非规范 Research。

更早里程碑与原因见 `docs/project/project-evolution.md`；具体 capability contract 见其真实 Architecture / Method / Skill / Rule owner。

## Current Evolution

当前正式演进单元为 Issue #133 — **Clarification Method Evolution：Requirement Clarification + Architecture Clarification**。

本轮面向普通软件 Consumer 补齐 Specification 之前的 project-level Clarified Context 形成机制，不把该流程 self-apply 到 `agentic-dev` capability evolution。

已完成：

- 将 `jilinjobs` 作为带失败历史的混合证据集执行 Requirement Clarification Critical Evidence Synthesis；
- 提炼 Authority-first、single semantic ownership、high-value ambiguity filtering、Authority promotion、independent semantic review 等正向模式；
- 明确 exhaustive decomposition、persistent intermediate model proliferation、structure-first semantic mutation、self-review as proof 等 anti-pattern；
- 将候选 work kind 收敛为 `method:software-project-clarification`；
- 完成 Method Boundary Design、adversarial design review、correction 与 focused re-review；
- Final Design Gate 收敛为 Blocking / Medium / Low = 0 / 0 / 0；
- 开始 canonical implementation，且明确该 Consumer-oriented Method **不注册到 `agentic-dev` 当前 local Method selector**。

完整设计与复核 Evidence 保留在 Issue #133；candidate implementation 位于对应 feature branch / PR，不由 Roadmap 复制全部正文。

## Current Gate

**Software Project Clarification v1 — Canonical Implementation / Verification。**

当前设计基线：

```text
Establish Context
→ Requirement Clarification
→ Architecture Clarification? (conditional)
→ Clarification Convergence
→ Clarified Project Context Ready
```

当前 Gate 约束：

- Method 主要服务 ordinary software Consumer 的 project-level / major-scope clarification；
- ordinary Feature Development 继续由 `method:ai-development` 负责；
- true blocker 存在时不得声明 `Clarified Project Context Ready`；
- Architecture Clarification 只在多个 Feature 进入可靠 Specification 前共同依赖 unresolved durable architecture driver 时进入，不扩张为 Big Design Up Front；
- Project Requirement 与 Feature Specification、Architecture Clarification 与 Technical Planning 必须保持单一 semantic ownership；
- 高风险 baseline reconstruction / semantic transformation 命中 mandatory independent semantic review trigger；
- durable output 回到真实 Requirement / Domain / Architecture owner，不新增默认 Handoff Artifact；
- 当前不新增 Clarification Skill，不批量新增 Clarification Rule；
- `agentic-dev` 自身 Project Capability Profile 不 self-register 该 Consumer Method。

完成本 Gate 仍需要：

- candidate static / semantic consistency review；
- 检查 Method corpus / Human inventory / existing AI Development alignment；
- 检查 current Rule / Skill / Project ownership 是否被无意扩张；
- PR review / repository-required verification；
- Integration 与 post-integration closure。

本 Gate 不授予 merge、release、deploy 或下一演进的自动 Execute Authority。

## Next Candidates

当前可见后续候选只在真实 Evidence 支持时推进：

- **Architecture Clarification evidence evolution**：当前 v1 只有 bounded、conditional、anti-BDUF 的最小 contract；后续从真实 Consumer positive / negative / evolutionary architecture case 校正进入条件和责任细节；
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
- `software-project-clarification` 的 Requirement Clarification responsibility 有真实 Consumer 历史证据支撑；Architecture Clarification 的 Evidence maturity 较低，当前只允许按最小条件 contract 使用并持续演进；
- reusable Method 存在于 `agentic-dev` corpus 不等于当前 Repository self-adopt；local selector 仍只描述本 Repository 实际采用的 work kind。

## State Ownership

- 当前 Repository live state：GitHub branch / Issue / PR / Actions；
- 当前项目使命与核心要求：`project-charter.md`；
- 当前 capability instance：`project-capability-profile.md`；
- 当前 evolution / gate / next candidates：本 Roadmap；
- 稳定历史里程碑：`project-evolution.md`。

Roadmap 不保存完整 Architecture、实施日志或完整 Closure Evidence；这些分别回到 capability owner 与 GitHub 历史。
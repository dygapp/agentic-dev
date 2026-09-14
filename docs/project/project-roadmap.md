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

当前没有已启动的新正式演进单元。

Issue #129 — **Model Collaboration Capability & Adoption v1** 已完成实现、验证、Integration 与 post-integration closure；完整实施 Evidence 保留在 Issue #129、PR #132、Git 与 Actions。

下一项工作必须从当前 Repository Authority、Roadmap candidates 与真实 Evidence 重新判断，不因 Issue 编号、历史路线或候选顺序自动启动。

## Current Gate

**Model Collaboration Capability & Adoption v1 — Integrated / Closed。**

已完成：

- reusable Model Collaboration Architecture 建立，且不硬编码具体模型 / provider instance；
- Model Collaboration Adoption Method 建立独立 work kind、阶段、Gate、fallback 与 completion semantics；
- specialized Method 只实例化已经接受的 collaboration semantics，不绕过 Consumer Adoption / Upgrade 的 upstream semantic assessment；
- Consumer projection 明确 local config / Rule / runtime / validation / fallback owner；
- Codex 平台参考实现保持 Human Guide 身份，不成为 `agentic-dev` current `.codex/` instance；
- functional enablement 与 efficiency / preferred-default claim 分离；
- 历史 multi-agent smoke failure 与 Issue #71 Evidence 保持 claim 边界；
- semantic-owner / Method-composition 分类经验进入非规范 Research；
- candidate exact Head `2d6b093696bbd97d5c43a265173afc9954a7008f` 的 Rule Discovery Run #94 PASS；
- independent review 收敛为未解决 Blocking / Medium = 0 / 0；
- PR #132 squash merge，actual integration commit 为 `385204c8605dd58584ec18456ab8a97d6282b515`；
- Post-Integration Rule Discovery Run #95 / Run ID `34823684351` 在 integration commit 上 PASS；
- Issue #129 已自动 closed / completed。

本 Gate 不声称 `agentic-dev` 自身已启用 multi-agent runtime。真实 child-thread、requested-vs-observed runtime identity、single-writer runtime behavior、fallback 与效率收益仍属于每个 Repository 执行 `method:model-collaboration-adoption` 时的 runtime Evidence。

本 Gate 也不授予 release、deploy、destructive remote cleanup 或下一演进的自动 Execute Authority。

## Next Candidates

当前可见后续候选只在真实 Evidence 支持时推进：

- **Requirements Analysis Method**：从已验证的大项目前期需求分析实践中提炼适用范围、阶段、产物、Gate 与完成语义；当前仍只是 Method candidate；
- **Consumer feedback evolution**：继续从 Issue #58 等长期 Consumer Evidence 判断是否需要新增 / 调整 reusable capability；
- **Method selection scaling**：只有 Method 数量或歧义真实增长时，才评估是否需要 metadata discovery / selector tool。

这些候选不因出现在 Roadmap 中自动获得 Planning / Execute Authority。

## Known Observations

- V4-08 的 natural Rule Evolution observation 仍属于 post-adoption future observation，不虚构为已验证；
- Project Capability Profile 是 Repository-local instance owner，需要继续观察其是否保持薄、稳定且不会演变成 runtime catalog；
- Rule / Skill Human inventory 继续由 deterministic tests 与真实 corpus 保持一致，不应迁入 Project Profile；
- Model Collaboration 的成本价值不能从“使用多个模型”本身推断；后续 Consumer adoption 应分别观察 high-capability token、Primary context、total token、wall time、rework 与最终质量；
- 当前 capability integration 不能证明任一具体 Agent 平台的 multi-agent runtime 已通过，真实支持度必须在 adoption 时重新探测；
- Model Collaboration 在真实 Consumer 中的长期 adoption / upgrade / ordinary-runtime 效果仍应由后续 Consumer Evidence 判断，而不是由本次 upstream self-integration 直接泛化。

## State Ownership

- 当前 Repository live state：GitHub branch / Issue / PR / Actions；
- 当前项目使命与核心要求：`project-charter.md`；
- 当前 capability instance：`project-capability-profile.md`；
- 当前 evolution / gate / next candidates：本 Roadmap；
- 稳定历史里程碑：`project-evolution.md`。

Roadmap 不保存完整 Architecture、实施日志或完整 Closure Evidence；这些分别回到 capability owner 与 GitHub 历史。
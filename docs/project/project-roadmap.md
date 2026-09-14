---
id: project:roadmap
type: project
status: active
---

# Project Roadmap

## Current Baseline

当前正式 capability integration baseline 为 **Project Knowledge Model / Capability Instance Boundary**：

`integration@10397cf00914fcfd6d71fd2ad6be6b89618dde8a`

该 baseline 在 Capability Model v2 与 V4 Rule Discovery Foundation 之上进一步集成：

- `Project 不传播，Capability 传播` 的长期 Project / Architecture 边界；
- Project Charter、Project Capability Profile、Project Roadmap、Project Evolution 四类稳定 Project owner；
- Repository-local Method selector / Rule Discovery instance / Skill entry 与 reusable capability contract 的分离；
- Method Architecture 不再拥有 `agentic-dev` 当前 selector instance；
- Skill Architecture 不再拥有当前 Skill inventory / count；
- Method-specific phase identity 回到具体 Method canonical owner；
- Consumer adoption / upgrade 明确只传播 / 适配 capability，不复制 upstream Project state；
- deterministic ownership contracts，防止 runtime locator、selector、inventory 与 phase identity 重新漂回错误 owner。

PR #127 的 integration commit 是上述 capability semantics 的正式基线。其后的 post-integration Project state closure 只更新 Project current-state / evolution owner，不改变该 capability baseline。当前 `master` 后续已包含 Rule granularity consolidation；精确 current Head 与 live integration state 始终从 GitHub 读取。

更早里程碑与原因见 `docs/project/project-evolution.md`；具体 capability contract 见其真实 Architecture / Method / Skill / Rule owner。

## Current Evolution

当前正式演进单元为：

> **Issue #129 — Model Collaboration Capability & Adoption v1**

目标是把历史 Codex 多模型实验与 Issue #71 Consumer Evidence 收敛为可选、可投射到 Consumer 的正式 capability，同时保持 reusable semantics 与 Repository-local runtime instance 分离。

本轮 semantic ownership：

- Model Collaboration 的稳定结构、Primary responsibility、Authority-preserving handoff、single-writer、model escalation、Evidence 与 fallback → Architecture；
- Consumer 第一次建立 / 启用 collaboration local instance 的跨上下文过程 → `method:model-collaboration-adoption`；
- `agentic-dev` 当前是否启用、具体 runtime / model / config locator → Project Capability Profile；
- Consumer-specific conditional policy → Consumer-local Rule；
- Codex 配置与使用示例 → Human Guide / local instance；
- 历史实验与 capability 分类推理 → Research / GitHub Evidence。

旧 `experiment/codex-multi-model-collaboration` 不直接合并；其中静态配置成功但 child collaboration smoke 失败的结果保持为历史 Evidence，不改写为 runtime PASS。

## Current Gate

Issue #129 当前处于 **candidate convergence / verification**。

当前候选分支：`feature/model-collaboration-capability-v1`；当前 PR：#132。精确 Head、Actions、Review 与 mergeability 必须从 GitHub 当前事实读取。

本演进完成门禁：

- reusable Model Collaboration Architecture 建立，且不硬编码具体模型 / provider instance；
- Model Collaboration Adoption Method 具有独立 work kind、阶段、Gate、fallback 与 completion semantics；
- Project Capability Profile 只记录 local selector / instance，并保持 `agentic-dev` self-instance 未经 adoption 不自动启用；
- Consumer projection 明确 local config / Rule / runtime / validation / fallback owner；
- 历史 smoke failure 与 Issue #71 Evidence 保持 claim 边界，不虚构 runtime 成功或高端模型独占价值；
- 本次 semantic-owner 分类经验进入非规范 Research；
- deterministic capability-model / Rule Discovery regression PASS；
- independent review 未解决 Blocking / Medium = 0 / 0。

达到以上门禁后只进入 `Ready for Review / Integration Decision`，不自动 merge。真实 multi-agent child-thread smoke 属于每个 Repository 执行 `method:model-collaboration-adoption` 时的 runtime Gate；本次 capability definition 不以无法从当前执行环境观察的 runtime 结果冒充 PASS。

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
- 当前 capability definition 不能证明任一具体 Agent 平台的 multi-agent runtime 已通过，真实支持度必须在 adoption 时重新探测。

## State Ownership

- 当前 Repository live state：GitHub branch / Issue / PR / Actions；
- 当前项目使命与核心要求：`project-charter.md`；
- 当前 capability instance：`project-capability-profile.md`；
- 当前 evolution / gate / next candidates：本 Roadmap；
- 稳定历史里程碑：`project-evolution.md`。

Roadmap 不保存完整 Architecture、实施日志或 Closure Evidence；这些分别回到 capability owner 与 GitHub 历史。
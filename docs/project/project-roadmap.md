---
id: project:roadmap
type: project
status: active
---

# Project Roadmap

## Current Baseline

当前正式集成基线为 **Capability Model v2**：

`master@e5488fd22a078ab59a427e36ef9a20af935fc63f`

该基线建立在 V4 Rule Discovery Foundation 之上，并已集成：

- Method / Architecture / Skill / Rule / Guide 的长期能力边界；
- `Single Semantic Ownership, Multiple Views`；
- Consumer Adoption / Upgrade Method；
- Skill / Rule 正交关系与 Consumer-local Rule specialization；
- Agent Method Selection / Skill discovery / Rule Discovery 入口；
- Human View 与 reserved Rule README 边界。

更早里程碑与原因见 `docs/project/project-evolution.md`；具体 capability contract 见其真实 Architecture / Method / Skill / Rule owner。

## Current Evolution

当前增量演进入口：

**Issue #126 — Project Knowledge Model：收敛 Project / Architecture 边界与项目知识层**。

目标是把 Capability Model v2 中仍混杂的 Repository-instance 信息迁回 Project owner，并建立长期：

```text
Project Charter
→ Project Capability Profile
→ Project Roadmap
→ Project Evolution
```

同时保持：

> **Project 不传播，Capability 传播。**

本轮不重新设计 V4 Rule Discovery 或 Capability Model v2，只收敛 Project Knowledge 与 reusable Architecture 的边界。

## Current Gate

Issue #126 当前处于 **implementation / candidate verification**。

当前工作分支：`refactor/project-knowledge-model`。

精确 branch Head、PR、Actions、Review 与 mergeability 必须从 GitHub 当前事实重新读取；本 Roadmap 只保存可跨 Fresh Context 恢复的稳定 current summary。

当前完成门禁：

- Project / Architecture boundary 进入长期 Architecture；
- Project Charter / Capability Profile / Evolution / README 建立；
- Roadmap 瘦身；
- Method selector instance、Skill inventory、Method-specific phase identity 回到真实 owner；
- Consumer adoption / upgrade 明确不传播 upstream Project state；
- deterministic boundary tests / lint / Rule Discovery regression PASS；
- high-impact review / convergence Blocking=0、Medium=0。

达到门禁后只进入 `Ready for Review / Integration Decision`，不自动 merge。

## Next Candidates

当前可见后续候选只在真实 Evidence 支持时推进：

- **Requirements Analysis Method**：从已验证的大项目前期需求分析实践中提炼适用范围、阶段、产物、Gate 与完成语义；当前仍只是 Method candidate；
- **Consumer feedback evolution**：继续从 Issue #58 等长期 Consumer Evidence 判断是否需要新增 / 调整 reusable capability；
- **Method selection scaling**：只有 Method 数量或歧义真实增长时，才评估是否需要 metadata discovery / selector tool。

这些候选不因出现在 Roadmap 中自动获得 Planning / Execute Authority。

## Known Observations

- V4-08 的 natural Rule Evolution observation 仍属于 post-adoption future observation，不虚构为已验证；
- Project Capability Profile 是新的 Repository-local instance owner，需要在后续真实 self-use / Consumer upgrade 中继续观察其是否保持薄、稳定且不会演变成 runtime catalog；
- Rule / Skill Human inventory 继续由 deterministic tests 与真实 corpus 保持一致，不应迁入 Project Profile。

## State Ownership

- 当前 Repository live state：GitHub branch / Issue / PR / Actions；
- 当前项目使命与核心要求：`project-charter.md`；
- 当前 capability instance：`project-capability-profile.md`；
- 当前 evolution / gate / next candidates：本 Roadmap；
- 稳定历史里程碑：`project-evolution.md`。

Roadmap 不保存完整 Architecture、实施日志或 Closure Evidence；这些分别回到 capability owner 与 GitHub 历史。
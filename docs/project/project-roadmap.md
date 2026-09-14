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

PR #127 的 integration commit 是上述 capability semantics 的正式基线。其后的 post-integration Project state closure 只更新 Project current-state / evolution owner，不改变该 capability baseline。

更早里程碑与原因见 `docs/project/project-evolution.md`；具体 capability contract 见其真实 Architecture / Method / Skill / Rule owner。

## Current Evolution

当前没有已启动的新正式演进单元。

Issue #126 — **Project Knowledge Model：收敛 Project / Architecture 边界与项目知识层** 已完成实现、验证、Integration 与 post-integration closure；其完整实施 Evidence 保留在 Issue #126、PR #127、Git 与 Actions。

下一项工作必须从当前 Repository Authority、Roadmap candidates 与真实 Evidence 重新判断，不因 Issue 编号、历史路线或候选顺序自动启动。

## Current Gate

**Project Knowledge Model — Integrated / Closed。**

已完成：

- Project / Architecture boundary 进入长期 Architecture；
- Project Charter / Capability Profile / Evolution / README 建立；
- Roadmap 瘦身；
- Method selector instance、Skill inventory、Method-specific phase identity、Rule Discovery runtime locator 回到真实 owner；
- Consumer adoption / upgrade 明确不传播 upstream Project state；
- deterministic boundary tests / lint / Rule Discovery regression PASS；
- high-impact review / convergence Blocking=0、Medium=0；
- PR #127 以 exact Head `5a2e59f5ae248fb2cf288c6521d8a9903ae8b68b` squash merge；
- actual integration commit：`10397cf00914fcfd6d71fd2ad6be6b89618dde8a`。

本 Gate 不授予 release、deploy、destructive remote cleanup 或下一演进的自动 Execute Authority。

## Next Candidates

当前可见后续候选只在真实 Evidence 支持时推进：

- **Requirements Analysis Method**：从已验证的大项目前期需求分析实践中提炼适用范围、阶段、产物、Gate 与完成语义；当前仍只是 Method candidate；
- **Consumer feedback evolution**：继续从 Issue #58 等长期 Consumer Evidence 判断是否需要新增 / 调整 reusable capability；
- **Method selection scaling**：只有 Method 数量或歧义真实增长时，才评估是否需要 metadata discovery / selector tool。

这些候选不因出现在 Roadmap 中自动获得 Planning / Execute Authority。

## Known Observations

- V4-08 的 natural Rule Evolution observation 仍属于 post-adoption future observation，不虚构为已验证；
- Project Capability Profile 是 Repository-local instance owner，需要在后续真实 self-use / Consumer upgrade 中继续观察其是否保持薄、稳定且不会演变成 runtime catalog；
- Rule / Skill Human inventory 继续由 deterministic tests 与真实 corpus 保持一致，不应迁入 Project Profile；
- Project Knowledge Model 的首次集成已经证明 ownership 可静态约束，但 Consumer 对这一新 Project boundary 的长期采用效果仍应由后续真实 adoption / upgrade Evidence 判断，而不是由本次 self-integration 直接泛化。

## State Ownership

- 当前 Repository live state：GitHub branch / Issue / PR / Actions；
- 当前项目使命与核心要求：`project-charter.md`；
- 当前 capability instance：`project-capability-profile.md`；
- 当前 evolution / gate / next candidates：本 Roadmap；
- 稳定历史里程碑：`project-evolution.md`。

Roadmap 不保存完整 Architecture、实施日志或 Closure Evidence；这些分别回到 capability owner 与 GitHub 历史。
# Establish GitHub as Project Source of Truth

## Goal

将 GitHub repository 确立为 `agentic-dev` 项目的唯一长期基线来源，替代临时压缩包作为持续同步方式。

## Background

随着项目进入 Skill Engineering 阶段，项目需要支持：

- Agent 基于 Repository 当前状态进行架构分析、设计、实现和 Review；
- Git commit 记录方法、契约和实现演进；
- Branch 隔离尚未进入共享基线的设计、实验和实现工作。

因此需要明确 Repository 作为 Human 与 Agent 的长期上下文载体。

## Scope

- 明确 GitHub repository 为项目 Source of Truth；
- 补充 repository baseline 记录；
- 更新相关治理说明；
- 同步 README 与 Tasks 中已经过时的阶段状态；
- 保留 ZIP 作为离线交换和初始化用途，不作为持续基线。

## Out of Scope

- 不修改 Skill Contract；
- 不实现任何 Skill；
- 不调整 Git merge / release policy。

## Acceptance Criteria

- 仓库文档明确 GitHub 为唯一项目基线来源；
- Agent / Human 的协作与 Authority Boundary 明确，不把具体 Agent 固定为只读或只写角色；
- 非默认 Branch / 特定 Commit 工作能够显式标识 working ref；
- README 与 Tasks 当前阶段和 Skill Engineering 基线一致；
- 后续 Skill Engineering 工作均基于 Git branch 和 commit 演进。

## Review Result

本任务 Review 已确认：

- Source of Truth 规则不改变 Method 或 Skill Contract；
- Repository collaboration 以 Authority、Risk、Tool Capability 和当前授权决定 Agent 行为，不绑定 ChatGPT / Codex 固定读写职责；
- `README.md` 与 `tasks/README.md` 的阶段漂移已同步修正；
- 当前变更不包含任何 Skill Implementation。

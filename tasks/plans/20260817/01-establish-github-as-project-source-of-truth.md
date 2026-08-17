# Establish GitHub as Project Source of Truth

## Goal

将 GitHub repository 确立为 `agentic-dev` 项目的唯一长期基线来源，替代临时压缩包作为持续同步方式。

## Background

随着项目进入 Skill Engineering 阶段，项目需要支持：

- ChatGPT 进行架构分析与设计评审；
- Codex 进行仓库内实现；
- Git commit 记录方法、契约和实现演进。

因此需要明确 Repository 作为长期上下文载体。

## Scope

- 明确 GitHub repository 为项目 Source of Truth；
- 补充 repository baseline 记录；
- 更新相关治理说明；
- 保留 ZIP 作为离线交换和初始化用途，不作为持续基线。

## Out of Scope

- 不修改 Skill Contract；
- 不实现任何 Skill；
- 不调整 Git merge / release policy。

## Acceptance Criteria

- 仓库文档明确 GitHub 为唯一项目基线来源；
- ChatGPT / Codex / Human 的协作边界明确；
- 后续 Skill Engineering 工作均基于 Git branch 和 commit 演进。

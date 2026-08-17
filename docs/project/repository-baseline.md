# Repository Baseline

## Repository

```yaml
name: agentic-dev
platform: github
repository: https://github.com/dygapp/agentic-dev
source_of_truth: true
```

## Source of Truth Rule

`agentic-dev` 的 GitHub repository 是项目长期演进的唯一基线来源。

- Git commit 是变更历史记录；
- Branch 是隔离实验和实现过程的边界；
- Pull Request 是可选的人工 Review 机制。

ZIP 快照仅用于：

- 初始项目导入；
- 离线交换；
- 临时备份。

ZIP 不作为持续开发过程中的权威上下文来源。

## Collaboration Model

```text
Human
  ↓
Architecture / Decision
  ↓
ChatGPT
  ↓
Task / Review
  ↓
Codex
  ↓
Implementation
  ↓
Git Commit
  ↓
Repository Baseline
```

## Authority Boundary

ChatGPT 负责方法、架构、契约分析和 Review。

Codex 负责仓库内实现、验证和提交。

Human 保留不可逆决策、Merge、Release 等最终权限。

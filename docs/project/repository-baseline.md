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

- Git commit 记录可追溯的项目演进历史；
- Branch 隔离尚未进入共享基线的设计、实验和实现工作；
- Pull Request 是可选的人工 Review 机制，是否使用以及如何 Merge 由 Repository Policy 或 Human Authority 决定；
- 当工作基于非默认 Branch 或特定 Commit 时，应显式说明对应 ref，避免不同 Agent 基于不同仓库状态作出判断。

ZIP 快照仅用于：

- 初始项目导入；
- 离线交换；
- 临时备份。

ZIP 不作为持续开发过程中的权威上下文来源；如果 ZIP 与 Git repository 状态不一致，以当前明确指定的 Git ref 为准。

## Collaboration Model

Repository 是 Human 与 Agent 之间共享的长期上下文载体。Conversation History、临时输出和本地 ZIP 都不能替代已经进入 Repository 的权威 Artifact。

典型协作过程可以是：

```text
Human / Agent Decision
        ↓
Authoritative Artifact / Task
        ↓
Authorized Agent Work
        ↓
Validation / Review
        ↓
Git Commit on Working Branch
        ↓
Human / Repository Policy
        ↓
Shared Repository Baseline
```

这里不把 ChatGPT、Codex 或其他 Agent 固定为只读或只写角色。具体 Agent 能否读取、修改、提交或评审仓库，由当前任务授权、Repository Policy、工具能力和变更风险共同决定。

## Authority Boundary

- Agent 可以在已授权范围内分析、设计、修改、验证和评审 Repository 内容；
- 普通、低影响、可逆的仓库内变更可以由 Agent 按当前授权继续执行；
- 会改变方法意图、重大架构方向、具有破坏性或不可逆影响、安全/隐私敏感，或超出当前授权的事项必须升级给 Human；
- Merge、Release、Deploy 和其他共享状态变更继续受 `AGENTS.md` 与 Repository Policy / Human Authority 约束。

## Working Baseline Rule

开始一项工作时，优先从 Git repository 获取当前状态。

- 未指定 ref 时，使用 Repository 当前默认基线；
- 已指定 Branch / Commit 时，以该 ref 作为本轮工作的明确上下文；
- 工作过程中如果 Repository 状态已经发生变化，应重新确认当前 ref，而不是依赖先前 Conversation 中缓存的文件内容；
- 任何需要长期保留的方法、契约、架构或实现结论，都必须最终进入 Repository 中对应的权威 Artifact，而不能只停留在聊天或 Task 记录中。

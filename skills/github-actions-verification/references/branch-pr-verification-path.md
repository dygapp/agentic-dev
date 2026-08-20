# Branch / PR 验证路径

## 目的

本参考说明在 GitHub Consumer 中如何根据隔离性、可逆性、证据可观察性和仓库策略选择 direct push 或 Branch → Pull Request（PR）路径。

Branch 是 Git 的隔离机制；PR 是 GitHub 的协作与集成对象。PR 不是 Git Method 的通用强制概念。

## 决策维度

优先检查：

1. **Isolation**：未完成状态是否会污染共享默认分支；
2. **Reversibility**：失败或改向时是否容易回滚；
3. **Evidence Observability**：当前 Agent Runtime 能否枚举并读取相应 CI Run；
4. **Repository Policy**：是否要求 Branch、PR、Review、protected branch 或特定 checks；
5. **Iteration Shape**：是否会经历多轮实现、CI、调试和复核。

## 何时更适合 Branch → PR

常见条件：

- 当前工作需要多轮修改和 CI；
- 默认分支是共享权威基线；
- Repository Policy 不希望未完成工作直接进入默认分支；
- 当前 Connector / Runtime 对 PR-triggered Actions 的可观察性优于 push-triggered Actions；
- 需要把 diff、CI、Review 和 Integration Decision 关联在同一个 GitHub 对象上。

常见路径：

```text
Task / Feature Branch
→ Pull Request
→ GitHub Actions
→ Current Evidence
→ Ready to Integrate
→ Human / Repository Policy
```

## 何时 direct push 仍可接受

如果同时满足：

- Repository Policy 明确允许；
- 工作低风险、短周期、可逆；
- 当前 Runtime 能完整取得该 push 对应的当前验证证据；
- 不会破坏并行工作或共享基线；

则不为了形式完整性强制创建 PR。

## Actions Trigger 与 Evidence

选择 trigger 时先验证当前 Runtime 能否读取：

- Run event；
- Head SHA；
- status / conclusion；
- Jobs / Steps；
- 必要 Logs / Artifacts。

如果 push-triggered Run 已存在但 Agent 无法自动发现，而 PR-triggered Run 可以稳定枚举，则切换为 PR-based flow 是有效 Runtime adaptation。

Human 手工提供 Run URL / ID 可以临时补足观察能力，但如果该人工步骤会在后续每轮验证重复出现，应优先寻找可自动观察的验证路径，而不是长期依赖人工补链。

## 非目标

不要从本参考推出：

- 所有 GitHub Repository 必须使用 PR；
- 所有 Execution Unit 必须一一对应 PR；
- PR 创建后 Agent 自动拥有 Merge 权限；
- direct push 天然违反 Method。

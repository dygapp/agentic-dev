---
id: architecture:github-agent-runtime
type: architecture
status: active
---

# GitHub Agent Runtime 架构

## 1. 目标与适用范围

本 Architecture 定义 **GitHub-hosted Repository** 在 ordinary Agent runtime 中如何选择、验证和切换 execution surface，并为 A / B / C 三种责任模式提供唯一可复用的规范语义。

它只适用于显式采用本 capability 的 GitHub Repository。它不是通用 Git Repository 规则，不是 Method lifecycle，也不定义某个具体 Repository 当前有哪些工具、凭证、checkout 或云端环境。

具体 Repository 是否采用本 capability、当前有哪些 execution surface、怎样从 Agent Bootstrap 到达本 Architecture，由该 Repository 自己的 Project capability instance 持有。

## 2. Bootstrap 与 semantic ownership

使用本 capability 的 Repository 必须让 ordinary Agent 从自己的 Repository-local Authority 到达本 Architecture：

```text
Repository entry
→ current AGENTS.md
→ Repository-local Project capability instance
→ architecture:github-agent-runtime
→ current responsibility / runtime availability
→ execution mode selection
```

Repository-specific 工作不能使用聊天历史、个人记忆、其他 Repository、upstream Guide 或模型先验替代当前 `AGENTS.md` Bootstrap。切换目标 Repository 时，对新 Repository 重新 Bootstrap。

如果 Repository-local capability instance 没有声明本 capability，或者本 Architecture / local runtime locator 无法从当前 Authority 恢复，则 execution routing **fail closed**；不得通过 Human Guide、旧会话或 upstream 在线查询补出 A / B / C 定义。

本 Architecture 拥有 execution topology 的长期规范语义；`AGENTS.md` 只拥有 Bootstrap / locator，Project capability profile 只拥有具体 Repository 的 local instance，Guide 只负责人类解释。

## 3. Execution surfaces

本 capability 区分四类 surface：

- **Local Repository Runtime**：已经存在并可用的本地 checkout / worktree，可直接使用 filesystem、shell、`git`、build、test 与 repository scripts；
- **Cloud Repository Runtime**：由当前已授权云端环境建立或绑定目标 GitHub Repository 的真实 checkout / worktree，并具备任务所需 filesystem、shell、`git`、build、test 或 repository scripts；
- **GitHub-native capability**：Connector、API 或等价 GitHub control-plane 能力，用于 Repository metadata、Issue、PR、Review、Actions 与不要求 worktree 语义的有界 GitHub 操作；
- **GitHub Actions**：CI、deterministic verification、runtime eval、artifact、Review / Demo Environment、deployment workflow 等辅助 execution / verification surface。

GitHub Actions 不是第四种责任模式。A / B / C 都可以在 Repository Authority 与适用 Rule 允许时调用 Actions。

“工具存在”不等于某个 surface 可用。runtime availability 必须针对**当前目标 Repository 与当前责任**实际确认：

- 普通 Python/container 环境没有目标 Repository 的真实 worktree / git baseline，不构成 Cloud Repository Runtime；
- ChatGPT、Codex、Codex CLI 等 client identity 本身不决定 mode；
- 有 GitHub API 写权限不代表能够替代需要 shell / build / test / worktree 的 Repository Runtime。

## 4. 三种责任模式

A / B / C 是正式 execution-routing identity，用于表达**当前 direct responsibility 应由哪种 Repository execution topology 承担**。它们不是会话永久状态，同一会话可随责任变化切换。

### A — Local Repository Task

当当前责任依赖真实 filesystem / shell / `git` worktree / build / test / repository scripts，且已经存在适用的 Local Repository Runtime 时，默认选择 A。

默认原则是 **Existing Repository Runtime First**：如果现有 Local Repository Runtime 已满足责任，不为了形式统一再建立 Cloud Runtime。

### B — Cloud Repository Task

当当前责任依赖真实 Repository Runtime，但没有适用 Local Repository Runtime，且当前环境存在可建立或绑定的已授权 Cloud Repository Runtime 时，选择 B。

B 只有在云端实际绑定目标 Repository、恢复可复核 baseline 并具备任务所需 worktree 能力后才成立。普通 container、远程文件读取或 GitHub Contents API 不足以构成 B。

进入 B 后仍服从目标 Repository 自己的 `AGENTS.md`、Method、Architecture、Skill、Rule、权限与 Gate；Cloud Runtime 不因存在而获得额外 Authority。

### C — Remote Repository Coordination

当当前责任只需要 GitHub-native read / analysis / Issue / PR / Review / Actions coordination，且不依赖真实 worktree 语义时，选择 C。

C **不等于只读**。如果一个 bounded GitHub-native mutation：

- 不需要 filesystem / shell / build / test / repository scripts；
- 可以由 GitHub API 完整、安全地表达；
- 当前 Repository Authority、Rule Discovery 与权限允许；

则可以继续在 C 中完成，例如有界的 Issue / PR coordination update。

如果完成责任需要真实 worktree 行为，即使 GitHub file API 技术上可以改文件，也必须转入 A 或 B。

## 5. Default routing

没有 Human explicit mode override 时，按以下顺序选择：

```text
当前责任是否需要真实 worktree / shell / git / build / test / repository scripts？
  ├─ NO → C
  └─ YES
       ↓
     是否已有适用 Local Repository Runtime？
       ├─ YES → A
       └─ NO
            ↓
          是否有已授权且实际可建立 / 绑定的 Cloud Repository Runtime？
            ├─ YES → B
            └─ NO → 按当前 Authority / Rule 处理 capability blocker；不得伪造成功
```

一个首选 surface 缺少能力时，先检查其他**已授权且能够等价完成当前责任**的自动化 surface。只有所有适用自动化路径都不能安全完成，才进入 Human escalation；Human escalation 自身仍服从 Repository-local Rule Discovery / Authority。

## 6. Human explicit mode override

用户可以显式要求当前责任使用 A、B 或 C。explicit override 的优先级高于 default routing，但它**只覆盖 execution topology selection**，不能覆盖：

- Repository Authority；
- Method / Gate；
- Rule / Skill；
- permission / credential boundary；
- verification requirement；
- 其他 safety / integration policy。

显式 mode 只有在该 Repository 已采用本 capability，且该 mode 能真实承担当前责任时才成立：

- **Forced B** 可以有意覆盖“已有 local runtime → 默认 A”的选择，用于明确要求 Cloud Repository Task；
- Forced B 当前不可用时，必须报告 capability blocker 并 fail closed，不得静默降级为 A / C，也不得用 GitHub file API 模拟 B；
- Forced A 但没有适用 Local Repository Runtime时 fail closed；
- Forced C 但当前责任需要真实 worktree 语义时 fail closed，而不是把 worktree responsibility 压进 C。

是否是自动选择还是 Human explicit override，应当能够从当前责任事实与本地 capability instance解释。

## 7. Responsibility transition

A / B / C 不是固定 Session Mode。direct responsibility 实质变化时，重新判断 execution mode。

典型转换：

```text
C — Remote Repository Coordination
→ 形成需要 worktree / build / test 的 Repository Task
→ 已有 local runtime：A
→ 否则可用 cloud runtime：B
```

以及：

```text
A / B — Repository Task 完成
→ 后续只剩 PR / Review / Actions / Issue coordination
→ C
```

进入新的 Repository Task responsibility 时，不能因为聊天中已经讨论清楚就继承旧执行上下文。目标 Repository 当前 baseline、必要 live state、direct responsibility 与适用 Rule 都必须按 Repository Authority 重新恢复。

首次 side effect、responsibility 实质变化、目标 Repository 切换、以及 Human explicit mode override 都是 routing / governance checkpoint；旧 mode 与旧 Rule candidate set 不跨这些边界永久有效。

## 8. GitHub live state 与 side effects

PR、Issue、branch、workflow run、exact Head、review / check state 等外部可变事实，在相关责任开始或继续前按需要重新读取当前 GitHub 状态。聊天记录、旧 SHA 或旧 PASS 只能作为 locator，不能替代 current state。

所有 Repository / Issue / PR / Review / Workflow / deployment 等 side effect 仍由当前 Repository Authority 与适用 operation Rules约束。本 Architecture 不复制 external-write、human-intervention、integration 或 verification Rule 正文。

## 9. Fail-closed

以下情况不能靠模型常识或旧上下文继续：

- 目标 Repository 尚未采用本 capability；
- local capability instance 或 canonical locator 缺失；
- mode 对应 runtime availability 无法确认；
- explicit override 指向当前不可用或不能承担责任的 mode；
- 当前责任是否需要 worktree 语义无法可靠判断；
- 目标 Repository 已切换但尚未重新 Bootstrap。

fail-closed 只阻止无法被当前 Authority 安全决定的 execution step，不授权 Agent自动访问 upstream Guide / Architecture 补定义。

## 10. Consumer projection

Consumer 接受本 capability 时，必须在自己的 Repository Authority 中建立：

- Consumer-local canonical Architecture owner（adopt / adapt）；
- 从 Consumer `AGENTS.md` / Project capability instance 到该 owner 的稳定 locator；
- Consumer 自己允许的 Local / Cloud / GitHub-native / Actions surface instance；
- runtime availability 的当前验证方式；
- A / B / C vocabulary（若保留）与 explicit override 行为；
- fail-closed 行为与 Fresh Runtime Evidence。

Consumer ordinary runtime 只依赖 Consumer-local state，默认 `upstream access = 0`。upstream `agentic-dev` 后续改变本 Architecture，不会自动改变已采用 Consumer；只有显式 Consumer upgrade 才能改变其 local semantics。

## 11. Human View

`docs/guides/github-agent-workflow.md` 可以把本 Architecture 组织成面向人的 A / B / C 工作指南、示例和可复制 Prompt，但不参与 ordinary Agent runtime，也不能成为 mode identity、routing precedence 或 fail-closed 行为的第二规范 owner。

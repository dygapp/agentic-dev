---
id: guide:github-agent-workflow
type: guide
status: active
---

# GitHub Agent 工作指南

本 Guide 面向使用 GitHub 托管 Repository 的项目参与者，解释 ChatGPT / Codex / Codex CLI、GitHub Connector 与 GitHub Actions 如何协同工作。

它只承担 **Human View**。A / B / C 的 mode identity、default routing、explicit override、transition 与 fail-closed 规范由 `docs/architecture/github-agent-runtime-architecture.md`（`architecture:github-agent-runtime`）持有；Repository 是否采用该 capability 与具体 runtime instance 由目标 Repository 自己的 Project capability instance 持有。ordinary Agent runtime 不依赖本 Guide。若本 Guide 与目标 Repository 的 `AGENTS.md`、local capability instance 或 canonical Architecture 冲突，以后者为准。

## 1. 先从责任而不是工具开始

GitHub 场景中常见四类 execution surface：

- **Local Repository Runtime**：已有本地 checkout / project directory，可直接使用 filesystem、shell、`git`、build、test 与 repository scripts；
- **Cloud Repository Runtime**：当前任务需要真实 worktree / shell / `git` / build / test / repository scripts，并由已授权云端环境实际建立或绑定目标 Repository；
- **GitHub-native capability / Connector**：读取和操作 Issue、PR、Review、Actions、remote metadata，以及在权限和任务边界允许时完成有界 GitHub API 操作；
- **GitHub Actions**：提供 CI、deterministic verification、runtime eval、artifact、Review / Demo Environment、deployment workflow 等异步 execution / verification surface。

真正选择 surface 时，由目标 Repository 从 `AGENTS.md` Bootstrap 后读取自己的 runtime capability instance 与 canonical Architecture。Guide 只帮助人理解，不替 Agent 做 runtime routing。

一个 surface 缺少某项能力，不等于必须让人工执行。只有当前已授权自动化路径都不能安全、等价地完成责任时，才进入 Human escalation。

## 2. 三种责任模式

A / B / C 是 `architecture:github-agent-runtime` 定义的正式 execution-routing identity。本 Guide 只把它们组织成人类容易使用的工作模式。它们不是 Method lifecycle，也不是整个会话不可改变的固定标签。

### A — Local Repository Task

适用于当前责任需要真实 Repository Runtime，而且已经存在可用 local checkout / project directory 的情况。

典型责任：

- 编辑 Repository 文件；
- `git` branch / diff / commit；
- build / test；
- repository scripts；
- 需要真实 worktree 的 verification。

默认情况下不应为了形式统一再建立 Cloud checkout。GitHub Connector 仍可并行承担 Issue / PR / Review / Actions 等 GitHub-native control-plane 操作。

### B — Cloud Repository Task

适用于当前责任需要真实 Repository Runtime、没有适用 Local Repository Runtime，而当前环境能够提供已授权 Cloud Repository Runtime 的情况。

真正的 B 必须把目标 GitHub Repository 建立 / 绑定为可复核的真实 worktree，并提供当前任务需要的 shell / `git` / build / test / repository scripts；一个普通 container 或远程文件 API 不是 B。

进入 B 后仍从目标 Repository 的 `AGENTS.md` Bootstrap，并继续服从其 Method / Rule / Skill / permission / Gate。

### C — Remote Repository Coordination

适用于主要责任是 GitHub-native 分析与协调，且不需要真实 worktree 的情况，例如：

- 读取 Repository 文件、commit、branch、Issue、PR、Review、Actions；
- 分析、讨论、独立 Review；
- 写入 Issue Evidence / Handoff / Current State；
- 触发或观察已经授权的 GitHub-native workflow。

C 不等于只读。一个不需要 shell / build / repository scripts、GitHub API 可以完整表达、并且当前 Authority / Rules / permission 允许的有界 mutation 可以继续在 C 中完成。

如果责任依赖真实 worktree 语义，即使 GitHub file API 技术上能写文件，也应转入 A / B。

## 3. 模式转换

A / B / C 可以在同一会话中转换，真正需要重新检查的是 **direct responsibility**。

典型 C → A / B：

```text
Remote analysis / coordination
        ↓
需要 worktree / shell / build / repository scripts
        ↓
已有适用 Local Repository Runtime？
        ├─ YES → A
        └─ NO  → 有真实可用 Cloud Repository Runtime时 B
```

完成 Repository Task 后，如果后续只剩 PR / Actions / Issue coordination，可以自然返回 C。

进入新的 Repository responsibility 时，不继承“聊天里已经讨论过”的隐式执行上下文。目标 Repository current state、runtime availability、direct responsibility 与适用 Rule 都应按当前 Repository Authority重新恢复。

## 4. Human explicit mode override

默认 mode 由 canonical Architecture按 current responsibility 与 runtime availability选择。人也可以明确指定本轮 execution topology。

explicit override 只改变 execution topology，不改变 Repository Authority、Method、Rule、Skill、权限、Gate 或验证要求。

例如用户明确要求 B 时，即使存在 local checkout，也可以有意覆盖默认 A。但如果目标 Repository 没有采用 B，或者当前没有真实可用的 Cloud Repository Runtime，应按 canonical contract fail closed，而不是静默改回 A / C。

## 5. Side-effect Boundary

首次 side effect 与 responsibility 实质变化都应视为 runtime checkpoint。

常见 side effect 包括：

- 修改 Repository 文件；
- commit / push；
- 创建或更新 Issue / PR / Review comment；
- workflow trigger；
- deployment / environment mutation；
- 其他外部可变状态写入。

准备写入时，不只确认“工具能不能做”，还要确认当前 Authority 是否允许，并按当前责任重新发现适用 Rule。

`rule:safe-external-write` 负责外部写的授权、最小变更、对象复用 / 幂等检查与写后重新读取；`rule:human-intervention-necessity` 负责发出人工请求前验证其不可替代性。Guide 不复制这些 Rule 的完整规范正文。

## 6. GitHub Connector 的定位

GitHub Connector 适合处理 GitHub collaboration / control plane：

- Issue；
- PR；
- Review；
- Actions；
- branch / commit / remote metadata；
- GitHub API 能直接表达的有界操作。

使用时保持几个简单原则：先读取 current object；创建持续身份对象前检查可复用对象；写后重新读取；Connector 缺少单一接口时先检查其他已授权自动路径；需要真实 worktree 时不拿远程 API 模拟 build / test / git-worktree 行为。

## 7. GitHub Actions 的定位

GitHub Actions 是辅助 execution / verification surface，不是第四种 Session Mode。

常见用途：

- CI；
- deterministic verification；
- runtime eval；
- artifact transport；
- task-level Rule Discovery transport；
- Review / Demo Environment；
- deployment workflow。

Actions run 应绑定可复核的 commit / branch / PR baseline。异步执行只有在所需 job 对目标 baseline 到达可观察终态后才能作为完成证据。

触发 workflow 本身是 external side effect，同样需要 Authority 与适用 Rule；“workflow 已启动”不等于目标 claim 已成立。

## 8. Issue、PR 与 Review

### Issue

Issue 适合承载 bounded work entry、Evidence、Handoff、Current State / Coordination 与 Gate / blocker live state。Issue 不因为记录了讨论结论就自动成为 Requirement / Method / Architecture / Rule 等长期 semantic owner。

### Pull Request

创建 PR 前先检查同 branch / 同 bounded change 是否已有 open PR。若已经存在，优先继续更新同一 PR，而不是重复创建。

PR 应保持单一逻辑目的；Review / CI / Evidence 绑定当前 exact Head，而不是沿用已被新提交取代的旧结果。

### Review

独立 Review 以当前候选和当前 Authority 为输入，不把作者解释、旧 PASS 或聊天中的隐式意图当作替代证据。发现 durable semantic defect 时，修复回到真实 owner；评论本身不成为第二 Authority。

## 9. Review / Demo Environment

Review Environment 是 verification / human-review execution surface，不是产品 Authority。

若环境是 singleton、固定域名或共享 endpoint，应显式考虑当前 owner / lease、stale run、自动验证与人工长时评审的不同生命周期、cleanup 与 exact-head currentness。

具体 concurrency / timeout / deployment policy 由 Consumer-local workflow 与相关 Rule / Skill 决定，本 Guide 不规定统一实现。

## 10. 避免不必要的 Human escalation

只有出现真实不可替代 blocker 时才需要人工，例如 Authority 明确保留给人的决定 / 操作、缺少不可替代 credential / permission / secret、多个 material choices 无法由当前 Authority 唯一决定、需要现实世界动作，或者所有已授权自动化路径都无法安全完成。

不应仅因为当前首选 Connector 没有某个按钮，就要求人工复制粘贴命令、下载再上传文件，或在两个可访问系统之间做机械中转。

## 11. ChatGPT Project Instruction 模板

对于已经拥有 `AGENTS.md` 和完整 Repository governance 的项目，Project Instruction 应保持极薄，只负责把 Agent 送入 Repository Bootstrap。例如：

```text
目标仓库：<owner/repo>。
GitHub Repository 是唯一项目事实来源。
开始后先从目标仓库 AGENTS.md 恢复 Repository Authority、Development Method 与当前工作规则。
不要把其他聊天、个人记忆或本提示中的仓库状态当作当前事实。
```

A / B / C、Rule Discovery、Connector / Actions、Method stages 等能够从 Repository 恢复的信息不应复制到 Project Instruction。

没有 Repository-local governance 的项目可以在 Project Instruction 中承担更多默认约束；这不是本 Guide 对成熟治理 Repository 的推荐路径。

## 12. Fresh Context Prompt 模板

新会话提示词只表达最小入口信息和用户目标：

```text
这是一个 Fresh Context。

目标仓库：
<owner/repo>

GitHub Repository 是唯一项目事实来源。

本轮目标：
<bounded goal / issue / PR>

开始后按目标仓库当前 AGENTS.md 恢复并继续。
```

凡 Repository 中能够恢复的 Authority、完整开发步骤、Rule body、Skill procedure、Roadmap 快照与 execution routing 都不要重复写进 Prompt。定位 SHA 可以作为 locator，但开始后仍重新核验 current state。

## 13. 强制使用 B — Cloud Repository Task

当人明确希望本轮使用 Cloud Repository Task，而不是让 Agent按默认 routing 自动选择时，可以直接复制下面的最小 Prompt：

```text
这是一个 Fresh Context。

目标仓库：
<owner/repository>

GitHub Repository 是唯一项目事实来源。

本轮强制使用 B — Cloud Repository Task。

本轮目标：
<bounded goal>

开始后按目标仓库当前 AGENTS.md 恢复并继续。
```

这个 Prompt 只表达用户的 execution-topology intent，不解释 B 的实现语义。Agent 应从目标 Repository 的 `AGENTS.md`、local capability instance 与 canonical runtime Architecture恢复 B；如果目标 Repository 没有采用 B 或当前 B 不可用，按 Repository-local contract fail closed。

## 14. Consumer 应用

Consumer 接受 `architecture:github-agent-runtime` 后，A / B / C 的 canonical semantics 和具体 execution-surface instance 都必须存在于 Consumer-local Authority；ordinary runtime 不在线读取 `agentic-dev` Guide 或 Project Profile补定义。

典型 local instance可以是：

```text
Local repository work: Codex CLI + local checkout
Cloud repository task: available authorized cloud repository runtime
GitHub collaboration: GitHub-native connector / API
Verification: local tools + GitHub Actions
```

这只是平台实例示例，不是所有 Consumer 的强制配置。真正的 local surface、availability verification 与 adaptation 由 Consumer adoption / upgrade裁决。

## 15. 常见错误

- A / B / C 只写在 Human Guide，Agent ordinary runtime 没有 canonical owner；
- 已经有 local checkout，却在默认 routing 下为了形式统一重新建立 cloud checkout；
- 用户明确 Forced B 后又因为存在 local checkout静默改回 A；
- 把普通 container误认成绑定目标 Repository 的 Cloud Repository Runtime；
- 没有 worktree 需求，却把所有 GitHub-native coordination 强行升级成 Repository Task；
- 需要 build/test 时只靠远程文件 API 修改后直接声明完成；
- 从 C 转入 Repository mutation 后继续沿用旧 Rule candidates；
- Connector 缺少单一接口就直接请求人工执行；
- 重试时不检查已有 Issue / PR，创建重复对象；
- workflow 已启动就声明验证通过；
- 把 Issue / Review comment 中的长期语义当成 canonical Authority；
- 把 GitHub-specific instance 写成所有 Git Repository 的 universal contract；
- 在 Project Instruction / Fresh Prompt 中复制整套 Method / Rule / Repository 状态，制造新的同步面；
- Consumer locator损坏后在线读取 upstream Guide 或依赖旧聊天补 routing。

## 16. 选择路径的简化判断

```text
用户是否显式指定 mode？
  → 按 canonical Architecture验证该 override是否可承担当前责任

否则：
  只需 GitHub-native read / coordination？
    → C

  需要 filesystem / shell / git worktree / build / test / repository scripts？
    → 已有适用 local runtime：A
    → 否则有真实可用 cloud runtime：B

当前自动化 surface 受限？
  → 先检查其他已授权等价路径
  → 仍不可替代时才 Human escalation
```

重点不是给整个会话永久贴标签，而是在每次 responsibility / explicit override / side-effect 边界按目标 Repository 自己的 Authority重新选择正确 execution surface。

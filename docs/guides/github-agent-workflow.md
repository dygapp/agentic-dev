---
id: guide:github-agent-workflow
type: guide
status: active
---

# GitHub Agent 工作指南

本 Guide 面向使用 GitHub 托管 Repository 的项目参与者，解释 ChatGPT / Codex / Codex CLI、GitHub Connector 与 GitHub Actions 如何协同工作。

它只承担 **Human View**。Repository Authority、Method、Architecture、Skill、Rule 与 Tool contract 仍由各自 canonical owner 定义；ordinary Agent runtime 不依赖本 Guide。若本 Guide 与目标 Repository 的 `AGENTS.md` 或 canonical capability 冲突，以后者为准。

## 1. 先从责任而不是工具开始

GitHub 场景中常见四类 execution surface：

- **Local Repository Runtime**：已有本地 checkout / project directory，可直接使用 filesystem、shell、`git`、build、test 与 repository scripts；
- **Cloud Repository Runtime**：当前没有合适的本地 worktree，但任务确实需要真实 filesystem / shell / `git` / build / test / repository scripts；
- **GitHub-native capability / Connector**：读取和操作 Issue、PR、Review、Actions、remote metadata，以及在权限和任务边界允许时完成有界 GitHub API 操作；
- **GitHub Actions**：提供 CI、deterministic verification、runtime eval、artifact、Review / Demo Environment、deployment workflow 等异步 execution / verification surface。

选择 surface 的原则不是 Cloud First，也不是 Connector First，而是：

> 使用当前已授权、能够直接完成责任且结果可验证的最合适 execution surface。

一个 surface 缺少某项能力，不等于必须让人工执行。只有当前已授权自动化路径都不能安全、等价地完成责任时，才进入 Human escalation。

## 2. 三种责任模式

下面的 A / B / C 是帮助人理解 execution topology 的**工作模式**，不是 Method lifecycle，也不会替代目标 Repository 的开发方法。

### A — Local Repository Task

适用于已经存在可用 local checkout / project directory 的情况。

典型责任：

- 编辑 Repository 文件；
- `git` branch / diff / commit；
- build / test；
- repository scripts；
- 需要真实 worktree 的 verification。

此时不应为了形式统一再建立 Cloud checkout。GitHub Connector 仍可并行承担 Issue / PR / Review / Actions 等 GitHub-native control-plane 操作。

### B — Cloud Repository Task

适用于当前没有可用 local Repository Runtime，而任务又确实依赖 worktree / shell / `git` / build / test / repository scripts 的情况。

建立 Cloud Repository Runtime 后，应从目标 Repository 的当前真实 baseline 开始，重新读取 `AGENTS.md`，恢复 Repository Authority、current responsibility 与 Rule Discovery，再执行 Repository mutation。

Cloud Runtime 不因为存在就自动获得更高 Authority，也不能跳过 Consumer-local Method / Rule / Skill。

### C — Remote Repository Coordination

适用于主要责任是 GitHub-native 分析与协调，且不需要真实 worktree 的情况，例如：

- 读取 Repository 文件、commit、branch、Issue、PR、Review、Actions；
- 分析、讨论、独立 Review；
- 写入 Issue Evidence / Handoff / Current State；
- 触发或观察已经授权的 GitHub-native workflow。

C 默认不承担需要 worktree 语义的 Repository implementation。若一个有界 GitHub API mutation 不需要 shell / build / repository scripts，且目标 Repository Authority、Rule Discovery 与写入权限均允许，可以直接使用 GitHub-native capability完成；这不等于把 C 扩张成通用 Repository Runtime。

## 3. 模式转换

A / B / C 可以在同一会话中转换，真正需要重新检查的是**direct responsibility**。

典型 C → A / B：

```text
Remote analysis / coordination
        ↓
需要 worktree / shell / build / repository scripts
        ↓
已有适用 Local Repository Runtime？
        ├─ YES → A
        └─ NO  → B
```

进入新的 Repository Task responsibility 时，不继承“聊天里已经讨论过”的隐式执行上下文。至少重新完成：

1. 确认目标 Repository；
2. 恢复当前真实 baseline；
3. 从该 Repository 的 `AGENTS.md` 开始 Bootstrap；
4. 识别新的 direct responsibility；
5. 按当前事实重新执行 Rule Discovery；
6. 重新核验之前形成的 candidate plan 是否仍与当前 Authority 一致；
7. 再产生 side effect。

完成 Repository Task 后，可以自然返回 C 继续 PR / Actions / Issue coordination。

## 4. Side-effect Boundary

首次 side effect 与 responsibility 实质变化都应视为 runtime checkpoint。

常见 side effect 包括：

- 修改 Repository 文件；
- commit / push；
- 创建或更新 Issue / PR / Review comment；
- workflow trigger；
- deployment / environment mutation；
- 其他外部可变状态写入。

准备写入时，不只确认“工具能不能做”，还要确认当前 Authority 是否允许，并按当前责任重新发现适用 Rule。

`rule:safe-external-write` 负责外部写的授权、最小变更、对象复用 / 幂等检查与写后重新读取；`rule:human-intervention-necessity` 负责发出人工请求前验证其不可替代性。Guide 不复制这两条 Rule 的完整规范正文。

## 5. GitHub Connector 的定位

GitHub Connector 适合处理 GitHub collaboration / control plane：

- Issue；
- PR；
- Review；
- Actions；
- branch / commit / remote metadata；
- GitHub API 能直接表达的有界操作。

使用原则：

- 先读取 current object，再写入；
- 创建具有持续身份的对象前，先检查是否已有同目标对象可继续复用；
- API 返回成功后重新读取真实状态；
- Connector 缺少某个接口时，继续检查 local/cloud runtime、standard GitHub API、Actions 或其他已授权路径，而不是立即要求人工充当桥梁；
- 如果任务依赖真实 worktree 语义，不用远程 API 模拟 build/test/git-worktree 行为。

## 6. GitHub Actions 的定位

GitHub Actions 是辅助 execution / verification surface，不是第四种 Session Mode。

常见用途：

- CI；
- deterministic verification；
- runtime eval；
- artifact transport；
- task-level Rule Discovery transport；
- Review / Demo Environment；
- deployment workflow。

Actions run 应绑定可复核的 commit / branch / PR baseline。异步执行只在所需 job 对目标 baseline 到达可观察终态后才能作为完成证据。

触发 workflow 本身是 external side effect，同样需要 Authority 与适用 Rule；“workflow 已启动”不等于目标 claim 已成立。

## 7. Issue、PR 与 Review

### Issue

Issue 适合承载：

- bounded work entry；
- Evidence；
- Handoff；
- Current State / Coordination；
- Gate / blocker 的 GitHub-native live state。

Issue 不因为记录了讨论结论就自动成为 Requirement / Method / Architecture / Rule 等长期 semantic owner。Durable semantics 必须回写真正 canonical owner。

### Pull Request

创建 PR 前先检查同 branch / 同 bounded change 是否已有 open PR。若已经存在，优先继续更新同一 PR，而不是重复创建。

PR 应保持单一逻辑目的，changed files 与当前 bounded responsibility 一致；Review / CI / Evidence 应绑定当前 exact Head，而不是沿用已被新提交取代的旧结果。

### Review

独立 Review 应以当前候选和当前 Authority 为输入，不把作者解释、旧 PASS 或聊天中的隐式意图当作替代证据。Review 发现 durable semantic defect 时，修复应回到真实 owner；评论本身不成为第二 Authority。

## 8. Review / Demo Environment

Review Environment 是 verification / human-review execution surface，不是产品 Authority。

若环境是 singleton、固定域名或共享 endpoint，应显式考虑：

- 当前 owner / lease；
- stale run；
- 自动验证与人工长时评审的不同生命周期；
- cleanup；
- exact-head currentness。

具体 concurrency / timeout / deployment policy 由 Consumer-local workflow 与相关 Rule / Skill 决定，本 Guide 不规定统一实现。

## 9. 避免不必要的 Human escalation

只有出现以下类型的真实 blocker 时才需要人工介入：

- Authority 明确保留给人的决定或操作；
- 缺少不可替代的 credential / permission / secret；
- 存在多个 material choices 且 current Authority 无法唯一决定；
- 需要现实世界动作，而当前工具不能执行；
- 所有已授权自动化路径都无法安全完成。

不应仅因为当前首选 Connector 没有某个按钮，就要求人工复制粘贴命令、下载再上传文件、或在两个可访问系统之间做机械中转。

## 10. ChatGPT Project Instruction 模板

Project Instruction 应保持薄，只声明会话级稳定约束，不复制 Repository Authority 或 Method 正文。例如：

```text
目标仓库：<owner/repo>。
GitHub Repository 是唯一项目事实来源。
开始后先从目标仓库 AGENTS.md 恢复 Repository Authority、Development Method 与当前工作规则。
需要 Repository mutation 时，优先使用当前可用 Repository Runtime；GitHub-native 协调使用已授权 Connector / Actions。
不要把其他聊天、个人记忆或本提示中的仓库状态当作当前事实。
```

如果 Consumer 有额外的跨仓库边界、生产权限或人工审批约束，只补充这些**会话外无法从 Repository 恢复的特殊约束**。

## 11. Fresh Context Prompt 模板

新会话提示词同样保持简洁：

```text
这是一个 Fresh Context。

目标仓库：
<owner/repo>

GitHub Repository 是唯一项目事实来源。

开始后先读取 AGENTS.md，并按其中的 Repository Authority、Development Method、Rule Discovery 与当前工作入口恢复上下文。

本轮目标：
<bounded goal / issue / PR>

特殊约束：
<only constraints that cannot be recovered from the repository>
```

不要把 Repository Authority、完整开发步骤、Rule body、Skill procedure、Roadmap 快照和旧 SHA 大量复制进提示词。定位 SHA 可以作为 locator，但开始后必须重新核验 current state。

## 12. Consumer 应用

Consumer 采用 `agentic-dev` 后，Local / Cloud / Connector / Actions 只是不同 execution topology；它们都消费同一套 Consumer-local Repository Authority、Method、Rules、Skills 与 Project Knowledge。

典型实例可以是：

```text
Local repository work: Codex CLI + local checkout
Remote repository task: available cloud repository runtime
GitHub collaboration: GitHub-native connector / API
Verification: local tools + GitHub Actions
```

这只是平台实例，不是所有 Consumer 的强制配置。Consumer ordinary runtime 继续只依赖自己的 local capability instance，不在线读取 `agentic-dev` 来补规则或流程。

## 13. 常见错误

- 已经有 local checkout，却为了形式统一重新建立 cloud checkout；
- 没有 worktree 需求，却把所有 GitHub-native coordination 强行升级成 Repository Task；
- 需要 build/test 时只靠远程文件 API 修改后直接声明完成；
- 从 C 转入 Repository mutation 后继续沿用旧 Rule candidates；
- Connector 缺少单一接口就直接请求人工执行；
- 重试时不检查已有 Issue / PR，创建重复对象；
- workflow 已启动就声明验证通过；
- 把 Issue / Review comment 中的长期语义当成 canonical Authority；
- 把 GitHub-specific 实例写成所有 Git Repository 的 universal contract；
- 在 Fresh Context Prompt 中复制整套 Method / Rule / Repository 状态，制造新的同步面。

## 14. 选择路径的简化判断

```text
只需 GitHub-native read / coordination？
  → C

需要 Repository mutation，但不依赖 worktree / build / test，且 GitHub API 可安全、完整表达？
  → 使用已授权 GitHub-native capability，并服从 external-write / Rule Discovery

需要 filesystem / shell / git worktree / build / test / repository scripts？
  → 已有 local runtime：A
  → 否则建立可用 cloud runtime：B

当前自动化 surface 受限？
  → 先检查其他已授权等价路径
  → 仍不可替代时才 Human escalation
```

重点不是给每个会话贴固定标签，而是在每次 responsibility / side-effect 边界上重新选择正确 execution surface，并继续服从同一个 Repository Authority。

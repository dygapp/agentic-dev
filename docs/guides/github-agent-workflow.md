---
id: guide:github-agent-workflow
type: guide
status: active
distribution: source-only
---

# GitHub Agent 工作指南

本 Guide 帮助人和 AI 理解 ChatGPT + WebCodex、Codex Work / codex-cli、Repository Runtime、GitHub Connector / API 与 GitHub Actions 怎样协同。

它是按需平台导航，不是 ordinary task 的固定上下文，也不拥有 Consumer 项目事实。若本文与目标 Repository 的 `AGENTS.md`、权限或 Consumer-local constraints 冲突，以目标 Repository 为准。

## 1. 三个责任不要混在一起

```text
Repository Authority
→ 当前项目事实、允许做什么、稳定入口在哪里

Execution Surface
→ 当前通过 WebCodex / Codex / GitHub API / Actions 怎样执行

Verification
→ 当前 Evidence 能支持什么完成声明
```

某个 surface “可以写”只说明技术路径存在，不自动授予权限。

某个 API / workflow “请求成功”也不等于目标任务完成。

## 2. ChatGPT + WebCodex 的可选 Layer 0

ChatGPT Project Instructions 可以保存 Repository 外无法自动恢复的稳定入口，例如：

```text
目标仓库：<owner/repo>

默认使用 ChatGPT + WebCodex。
开始后先通过 WebCodex 定位目标 Repository，
读取当前 AGENTS.md，
并以后续 Repository 内容作为项目事实来源。

不要把其他聊天、个人记忆或 Project Instructions 中的状态快照当作当前 Repository fact。
```

它只负责“怎样进入项目”。

不要把当前 Gate、Issue / PR、Requirement / Architecture、全部项目规则、Skill procedure、旧 SHA 或 Roadmap 快照长期放进 Project Instructions。

Codex Work / codex-cli 已经处于 Repository Context 时直接从 `AGENTS.md` 开始，不需要这层适配。

## 3. Fresh Context 从 Repository 恢复

进入项目后至少：

1. 确认目标 Repository / worktree；
2. 读取当前 `AGENTS.md`；
3. 恢复项目文档稳定入口和 current work；
4. 确认 installed Skills；
5. 获取当前任务适用的 Consumer-local constraints；
6. 重新核验 branch / PR / exact Head 等 live facts；
7. 再开始当前责任。

历史聊天、模型记忆和 Guide 不能替代这些 Repository facts。

## 4. 优先使用当前可用 Repository Runtime

如果当前 WebCodex / Codex workspace 已经提供 filesystem、shell / Python、git、build / test 或本地服务能力，优先在真实 worktree 中执行 Repository-level 工作。

这通常最适合：

- 多文件修改；
- diff review；
- build / lint / test；
- 本地复现；
- deterministic validation；
- commit 前检查。

但“本地可写”不增加 Authority；仍要遵守目标 Repository 自己的权限和 local constraints。

## 5. GitHub Connector / API 负责 GitHub-native coordination

适合：

- Issue / PR / Review；
- branch / commit / remote state；
- Actions；
- GitHub-native comments / Evidence；
- 最终 merge / release coordination（前提是已获授权）。

外部写操作遵循：

```text
read current state
→ confirm authority
→ reuse existing identity when possible
→ perform minimum necessary write
→ reread source of truth
→ verify target state
```

不要因为一个 wrapper 缺少按钮，就立即要求用户做人肉中转；先检查当前已授权的 GitHub API、Repository Runtime 或 Actions 是否已有等价路径。

## 6. GitHub Actions 是计算与 Evidence surface

Actions 适合在明确 subject 上运行 Repository-native verification。

高可信路径通常绑定 exact SHA / exact PR Head，并验证 checkout 结果。

关键点：

- requested subject 与 actual checkout 要一致；
- 运行该 checkout 自己的验证；
- 保留可恢复 logs / reports / artifacts；
- invalid input、checkout drift、missing artifact 或不可恢复结果 fail closed。

Actions 的职责是执行与产生 Evidence，不是新的 Requirement / Architecture / permission owner。

## 7. Consumer-local constraints 怎样进入执行

新产品模型不要求普通 Consumer 复制 `agentic-dev` 当前 Rule Discovery Runtime。

当前任务怎样找到项目级约束，由 Consumer 自己的最小机制决定，例如：

- 根 `AGENTS.md` 中极少量 repository-wide policy；
- nested `AGENTS.md` / host native scoped instructions；
- Consumer-local policy docs + 薄 locator；
- 只有真实 Evidence 证明简单机制不足时才增加更复杂过滤。

因此本 Guide 不定义一套新的通用 task-signals / Rule Discovery 协议。

具体边界见 [consumer-local-constraints.md](consumer-local-constraints.md)，并由产品边界重构 P4 继续验证。

## 8. 外部操作使用 installed Skills

涉及 GitHub、远程 API、shared state 或异步任务时：

- 通用安全写操作使用 `external-operation`；
- GitHub Actions 本身是关键验证路径时使用 `github-actions-verification`；
- unexpected failure 使用 `systematic-debug`；
- 高影响最终变更复核使用 `review-change`。

Skill 提供通用执行方法，Consumer-local constraints 提供当前项目特有政策。

## 9. Verification 绑定 claim 与 exact subject

完成声明至少回答：

- 目标 claim 是什么；
- exact subject 是什么；
- 哪些 verification 实际运行；
- 是否达到可观察 terminal state；
- logs / reports / artifacts 是否可恢复；
- 当前 Evidence 是否真的能区分 claim 的真伪。

不要把：

```text
workflow triggered
API returned 202
job created
one test passed
old Head was green
```

直接解释成当前完成。

Ancestor Evidence 只有在 Consumer 自己允许 claim-level reuse、并且 exact diff 证明该 claim 不受影响时才可复用；祖先 Run 不能描述为当前 Run。

## 10. ChatGPT + WebCodex 与 Codex local 的共同边界

两种模式从 `AGENTS.md` 开始重新汇合：

```text
ChatGPT + WebCodex
Project Instructions
        ↓
     AGENTS.md
        ↓
Consumer Project Knowledge
+ installed Skills
+ local constraints
```

```text
Codex Work / codex-cli
        ↓
     AGENTS.md
        ↓
Consumer Project Knowledge
+ installed Skills
+ local constraints
```

区别只是进入 Repository 的方式，不需要为了统一 Runtime 而强迫二者拥有相同 Host 配置。

## 11. Repository switch

同一会话切换 Repository 时：

- 重新读取新 Repository 的 `AGENTS.md`；
- 重新恢复项目 facts、installed Skills 和 local constraints；
- 重新核验 branch / PR / Head；
- 不携带旧 Repository 的权限、规则候选、current work 或 Evidence 结论。

## 12. 最后才请求人工介入

适合人工承担的通常是：

- 产品 / 业务 / 架构等不可替代决定；
- 当前系统拿不到的 credential / permission / secret；
- 现实世界操作；
- 受控生产环境责任；
- 当前所有授权自动路径都无法安全完成的动作。

不要仅因为当前首选 surface 缺一个功能，就要求用户复制命令、搬运 artifact 或在两个 Agent 都能访问的系统之间做人肉中转。

## 13. 常见错误

| 错误 | 更合适的做法 |
|---|---|
| 用旧聊天里的 SHA 当当前事实 | 从 Repository / GitHub live state 重查 |
| 没有 checkout 就跳过项目约束 | 使用 Consumer 声明的当前约束入口；入口损坏则 fail closed |
| 有本地 Runtime 仍强制绕行 Actions | 直接用当前 Runtime，GitHub 只做协调 |
| workflow 已启动就报告 PASS | 等 terminal state + claim-matching Evidence |
| writable Connector 直接修改共享状态 | 先确认 Authority，再做有界写入并 reread |
| 旧 Head 绿色就支持新 Head | 重新验证或严格 claim-level Evidence reuse |
| Guide 中恰好有答案就覆盖 Repository | Guide 只导航，项目事实来自 Consumer |
| Consumer 在线读取 Provider docs 补 Skill procedure | 修复 / 更新 installed Skill，不形成隐式 runtime dependency |

## 14. 方法论咨询与 ordinary runtime

普通开发任务不需要固定读取本 Guide。

只有用户在询问 ChatGPT / Codex / GitHub 怎样组合、怎样建立 Layer 0 或怎样把 GitHub verification 接入项目时，才按需读取它。

一旦进入具体实现 / 验证责任，应切换到 Consumer Repository Authority、installed Skills 与项目本地约束。

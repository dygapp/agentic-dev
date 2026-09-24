---
id: guide:guides-navigation
type: guide
status: active
distribution: source-only
---

# 使用指南与方法导航

`docs/guides/**` 是 `agentic-dev` 的方法论知识与导航层，**同时面向人和 AI 按需读取**。

它不是 ordinary task 的固定上下文，也不是第二套执行 Authority：

- Guide 解释怎么开始、当前可能处于什么状态、下一步通常做什么，以及 Skills 怎样组合；
- canonical `skills/**` 持有真正的 Consumer execution contract；
- Consumer Repository 持有自己的 Product / Requirement / Architecture / current work / local constraints；
- Provider 内部 Method / Rule / Architecture 可以继续服务 `agentic-dev` 自身研发，但不是普通 Consumer 必须安装或理解的 runtime 类型。

## 推荐入口

1. [`getting-started.md`](getting-started.md) — 不知道从哪里开始时先读这里；
2. [`bootstrap-new-project.md`](bootstrap-new-project.md) — 从基本项目情况建立新软件 Repository；
3. [`adopting-agentic-dev.md`](adopting-agentic-dev.md) — 已有 Repository 最小侵入接入 Skills；
4. [`choosing-next-step.md`](choosing-next-step.md) — 根据 Consumer 当前事实判断下一责任；
5. [`feature-development.md`](feature-development.md) — 普通 Feature / change 的方法导航；
6. [`establishing-requirement-baseline.md`](establishing-requirement-baseline.md) — 系统性 Requirement Baseline 建立；
7. [`human-review.md`](human-review.md) — 人工评审与 durable semantic writeback；
8. [`upgrading-agentic-dev.md`](upgrading-agentic-dev.md) — 显式采用新的 exact-version Skills；
9. [`consumer-local-constraints.md`](consumer-local-constraints.md) — Consumer 项目级约束的 ownership 与 progressive disclosure 边界；
10. [`github-agent-workflow.md`](github-agent-workflow.md) — ChatGPT + WebCodex、Codex 与 GitHub 执行面；
11. [`multi-model-collaboration.md`](multi-model-collaboration.md) — 可选多模型 / 多 Agent 协作；
12. [`codex-model-collaboration-reference.md`](codex-model-collaboration-reference.md) — Codex 平台参考配置；
13. [`language-and-terminology.md`](language-and-terminology.md) — 面向人的语言与术语表达。

## AI 使用边界

AI 只有在 Bootstrap、方法论咨询、导航或用户明确要求理解整体流程时按需读取 Guide。进入具体责任后，使用 installed Skill 的 `SKILL.md` 执行。

如果 Guide 与 Skill 对同一可执行 procedure 出现冲突，应修正 Guide；如果 Guide 与 Consumer 项目事实冲突，以 Consumer Repository Authority 为准。

## Consumer-local constraints v1

P4 已验证第一版最小约定：

- repository-wide stable policy → 根 `AGENTS.md`；
- path / module scoped policy → nested `AGENTS.md` / 宿主原生 scoped instructions；
- activity / semantic scoped policy → Consumer-local policy docs + 薄 locator；
- verified no-match → 正常继续；
- locator 损坏 / applicability 不可靠 → fail closed。

当前没有 Evidence 要求普通 Consumer 采用 Provider 的五维 Rule Discovery、Rule metadata schema 或 discovery tool。旧 `rule-activation-guide.md` 与 `consumer-local-rule-activation.md` 已由 `consumer-local-constraints.md` 接管并退出 Guide 导航。

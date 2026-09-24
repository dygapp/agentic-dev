---
id: guide:using-agentic-dev
type: guide
status: active
---

# 使用 agentic-dev

`agentic-dev` 面向普通软件项目提供一套 AI 驱动开发方法。

完整使用体验由三部分组成：

```text
Guides
→ 帮助人和 AI 理解怎么开始、当前处于什么状态、下一步做什么

Skills
→ 提供真正可安装、可发现、可执行的软件开发能力

Consumer-local Project Knowledge / Constraints
→ 保存当前项目自己的事实、架构、当前工作和项目级约束
```

其中只有 `skills/**` 是 `agentic-dev` 的正式 Consumer runtime 产品。

Guide 可以被人和 AI 按需阅读，但不进入 ordinary task 的固定上下文；Consumer 项目事实始终由 Consumer Repository 自己拥有。

## 1. 从哪里开始

第一次使用时先读 [getting-started.md](getting-started.md)。

然后按当前情况进入：

- 新项目： [bootstrap-new-project.md](bootstrap-new-project.md)
- 已有项目首次采用： [adopting-agentic-dev.md](adopting-agentic-dev.md)
- 不知道下一步做什么： [choosing-next-step.md](choosing-next-step.md)
- 普通 Feature / change： [feature-development.md](feature-development.md)
- Requirement Baseline 不稳定： [establishing-requirement-baseline.md](establishing-requirement-baseline.md)
- 需要集中人工评审： [human-review.md](human-review.md)
- 升级已安装 Skills： [upgrading-agentic-dev.md](upgrading-agentic-dev.md)
- 使用 ChatGPT / Codex / GitHub： [github-agent-workflow.md](github-agent-workflow.md)
- Consumer-local constraints： [consumer-local-constraints.md](consumer-local-constraints.md)
- 多 Agent / 多模型协作： [multi-model-collaboration.md](multi-model-collaboration.md)

## 2. 最小模型

一个软件 Consumer 可以理解为四层 Repository responsibility，加一个可选 Host Adapter：

```text
Layer 0 — Host Adapter，可选
    ChatGPT Project Instructions 等
        ↓
Layer 1 — Repository Bootstrap
    AGENTS.md
        ↓
Layer 2 — Knowledge / Navigation
    Guides + Consumer Project Knowledge
        ↓
Layer 3 — Execution
    installed Skills
        ↓
Layer 4 — Local Constraints
    Consumer-owned rules / policies
```

这些层只描述职责与加载方式，不是新的 Capability 类型系统。

### Host Adapter

只负责把 Agent 带到正确 Repository，例如告诉 ChatGPT 使用哪个 WebCodex Project、先读取哪个 `AGENTS.md`。

它不保存当前 Gate、Requirement、Architecture、Roadmap 快照或其他 Repository fact。

Codex Work / codex-cli 已经处于 Repository Context 时可以直接从 `AGENTS.md` 开始，不需要这一层。

### AGENTS.md

保持短、小、稳定，只告诉 Agent：

- 当前 Repository 是什么；
- 项目事实从哪里恢复；
- installed Skills 在哪里；
- Consumer-local constraints 从哪里找；
- 有哪些稳定安全 / 权限边界。

不要把完整 Guide、全部本地规则、Skill procedure 或当前工作流水账塞进去。

### Guides / Project Knowledge

Guide 回答“现在应该做什么、为什么”。

Consumer Project Knowledge 回答“这个项目当前事实是什么”。

Guide 不能覆盖 Consumer facts，Consumer facts 也不需要复制 upstream 方法论正文。

### Skills

Skill 回答“这件事具体怎么做”。

正式 Consumer runtime 从 repository-local installed Skills 取得通用执行能力。普通 Skill execution 不在线读取 Provider `docs/**` 补齐语义。

### Consumer-local constraints

回答“在这个项目里做这件事还有什么特殊约束”。

技术栈、数据库迁移、安全、部署、代码组织、项目术语和审批边界等都属于 Consumer，而不是通用 Skill。

## 3. 新项目怎样开始

新项目可以只向 AI 提供：

- 项目的基本情况；
- `agentic-dev` Repository；
- 一个明确的 immutable version tag。

然后进入 [bootstrap-new-project.md](bootstrap-new-project.md)。

Bootstrap 只做建立 Consumer runtime 前必须做的最小工作：

```text
基本项目输入
→ 最小谈判式澄清
→ 建立 Consumer-owned Repository
→ 建立薄 AGENTS.md 与最小项目知识入口
→ 安装 exact-version Skills
→ 建立 exact-version Guide locator
→ 给出下一步建议
```

Bootstrap 不要求先把完整 Requirement Baseline、完整 Architecture 和所有 Feature 一次设计完。

当 Repository、Skills、项目知识入口和 Guide locator 都可恢复后，Bootstrap 结束；后续普通工作由 Consumer Repository Authority + installed Skills + Consumer-local constraints 接管。

## 4. 已有项目怎样采用

Existing Repository 默认使用最小侵入路径：

```text
恢复当前 Repository Authority
→ 选择 agentic-dev exact tag
→ 标准安装 Skills
→ 最薄 Bootstrap integration
→ native Skill discovery / targeted validation
→ 回到当前项目开发
```

默认不要求：

- 全仓文档重构；
- Requirement / Architecture Authority rebuild；
- 历史资产清理；
- 目录统一；
- 重新设计项目级规则体系。

这些只在当前项目真实问题证明必要时作为独立 remediation。

## 5. 不知道下一步做什么

直接使用 [choosing-next-step.md](choosing-next-step.md)。

判断来自：

```text
Consumer 当前事实
+
方法论 Guide
→ 当前最主要缺口
→ 下一责任
→ 对应 Skill
```

Guide 只选择“下一类工作”，不会维护另一套 Skill procedure。

## 6. Requirement 与 Architecture

当项目只有原始资料、长期 Requirement owner 不清、同一事实冲突，或多个 Feature 被同一需求缺口反复阻塞时，使用：

- [establishing-requirement-baseline.md](establishing-requirement-baseline.md)
- installed `establish-requirement-baseline` Skill

核心原则是建立 Consumer-owned、可恢复、single-owner 的长期 Requirement Authority，而不是把需求获取理解成无限问答。

只有多个当前或预期 Feature 共同依赖一个长期、高成本难逆、并且不解决就会阻塞可靠开发的 systemic architecture driver 时，才使用 `clarify-architecture`。

局部、低风险、可逆的实现选择留给 `technical-plan` 或 `execute-unit`。

## 7. 普通 Feature / change

见 [feature-development.md](feature-development.md)。

常见路径：

```text
clarify-intent
→ specify
→ technical-plan?    # 仅按需
→ slice-work
→ readiness-check
→ execute-unit
→ converge
→ Ready to Integrate
```

这不是硬编码状态机。当前项目事实已经满足某一步的责任时，可以跳过；出现上游缺口时返回真实 owner。

`Ready to Integrate` 不是 merge / release / deploy 授权。

## 8. Human Review

见 [human-review.md](human-review.md)。

Human Review 的价值是：

```text
Current Authority
→ structured Review Draft
→ Human Review
→ feedback classification
→ durable semantic change 写回真实 owner
→ reread
→ regenerate / recalibrate projection
```

Review Draft、流程图、HTML、DOCX 默认都是投影，不是新的事实 owner。

`human-review` 与 `review-change` 责任不同：前者帮助责任人理解和确认项目语义，后者独立检查 Repository change 是否符合当前 Authority、scope、constraints 与 Evidence。

## 9. Consumer-local constraints

见 [consumer-local-constraints.md](consumer-local-constraints.md)。

基本原则：

- 极少量全局稳定约束可以进入根 `AGENTS.md`；
- path / module scoped policy 优先使用 nested `AGENTS.md` 或宿主原生 scoped instructions；
- activity / semantic scoped policy 可以由 Consumer-local policy docs + 薄 locator 承担；
- 只有简单机制经真实 Evidence 证明不足时，才增加 metadata / filter 复杂度。

这部分属于 Consumer 自己，不是 `agentic-dev` 的第二种安装产品。

## 10. GitHub / Codex / ChatGPT 怎样协作

见 [github-agent-workflow.md](github-agent-workflow.md)。

原则：

```text
Repository Authority
→ 决定允许做什么、项目事实是什么

Execution Surface
→ 决定通过 WebCodex / Codex / GitHub API / Actions 怎样执行

Verification
→ 决定当前 Evidence 能支持什么完成声明
```

执行面可用不等于获得额外 Authority；API / workflow 成功也不等于目标 claim 已完成。

## 11. 多 Agent / 多模型协作

多模型协作是可选能力，不是默认项目结构。

先安装 Skills，再根据真实 Runtime 能力使用 `activate-model-collaboration` 建立 Consumer-local collaboration instance。

如果单 Agent 已经能可靠完成当前责任，不需要为了“多模型”本身增加 delegation、并发和配置复杂度。

## 12. 版本与升级

普通分发使用明确 immutable tag + 标准 Agent Skills-compatible installer。

升级时：

```text
current exact tag
→ 显式选择 new exact tag
→ 安装目标 Skills
→ targeted revalidation
→ 最后更新 adopted ref / Guide locator
```

不把无版本 `latest` 或 generic update 当作隐式升级协议。

完整说明见 [upgrading-agentic-dev.md](upgrading-agentic-dev.md)。

## 13. Provider 内部资产怎样理解

`agentic-dev` Repository 可以保留服务自身研发、研究、验证和历史 Evidence 的 `docs/**`、`tools/**`、`evals/**` 等资产。

它们的存在不代表普通 Consumer 需要安装、理解或运行同构的 Method / Architecture / Rule Runtime。

## 14. 最后记住三句话

```text
Guide：
现在应该做什么？

Skill：
这件事具体怎么做？

Consumer-local constraint：
在这个项目里做这件事还有什么特殊要求？
```

只要这三个责任保持清楚，方法论就可以完整，同时避免把 Consumer runtime 再扩张成一套复杂 Capability Framework。

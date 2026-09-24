---
id: guide:getting-started
type: guide
status: active
distribution: source-only
---

# 从这里开始

`agentic-dev` 面向普通软件项目提供一套 AI 驱动开发方法。用户不需要先理解 Provider 内部的 Method、Rule、Architecture 或发布实现；先判断自己处于哪一种使用场景，再进入对应 Guide 或 Skill。

Guide 同时服务人和 AI，但默认按需读取。普通实现任务不需要把整个 `docs/guides/**` 加入上下文。

## 1. 先选择入口

| 当前情况 | 建议入口 |
|---|---|
| 只有一个新项目想法或少量背景材料，还没有 Repository | [`bootstrap-new-project.md`](bootstrap-new-project.md) |
| 已有软件 Repository，第一次引入 `agentic-dev` | [`adopting-agentic-dev.md`](adopting-agentic-dev.md) |
| 已经采用，但不知道现在最值得推进什么 | [`choosing-next-step.md`](choosing-next-step.md) |
| 已有 Requirement / Architecture 基础，要开发一个 Feature / change | [`feature-development.md`](feature-development.md) |
| Requirement 分散、冲突、没有稳定 owner，或多个 Feature 被同一需求缺口阻塞 | [`establishing-requirement-baseline.md`](establishing-requirement-baseline.md) |
| 需要让产品、业务、架构或工程责任人集中人工评审 | [`human-review.md`](human-review.md) |
| 已安装旧版本，希望采用新的 `agentic-dev` 版本 | [`upgrading-agentic-dev.md`](upgrading-agentic-dev.md) |
| 使用 ChatGPT + WebCodex、Codex、GitHub Actions 等不同执行面 | [`github-agent-workflow.md`](github-agent-workflow.md) |
| 项目已经沉淀本地规则 / policy，不希望全部塞进根 `AGENTS.md` | [`consumer-local-constraints.md`](consumer-local-constraints.md) |
| 想启用多 Agent / 多模型协作 | [`multi-model-collaboration.md`](multi-model-collaboration.md) |

## 2. 最小心智模型

完整使用模型只需要理解四个 Repository 层和一个可选 Host 层：

```text
Layer 0  Host Adapter（可选）
         ChatGPT Project Instructions 等
                    ↓
Layer 1  Repository Bootstrap
         AGENTS.md
                    ↓
Layer 2  Knowledge / Navigation
         Guides + Consumer Project Knowledge
                    ↓
Layer 3  Execution
         installed Skills
                    ↓
Layer 4  Local Constraints
         Consumer-owned rules / policies
```

每层回答的问题不同：

- Host Adapter：怎样进入正确 Repository；
- `AGENTS.md`：当前项目的稳定入口在哪里；
- Guide / Project Knowledge：现在应该做什么、为什么；
- Skill：这件事具体怎么做；
- Consumer-local constraints：在这个项目里做这件事有什么特殊约束。

这些层不是新的 Capability 类型系统，也不要求每个项目建立同名目录。

## 3. AI 怎样使用 Guide

当用户明确提出以下问题时，AI 可以按当前项目 adopted 的 `agentic-dev` 精确版本读取对应 Guide：

- “怎么开始？”
- “这个项目下一步应该做什么？”
- “已有项目怎样接入？”
- “这个 Skill 应该在什么情况下使用？”
- “怎样组织人工评审？”

Guide 提供导航和判断框架，不拥有 Consumer 当前事实。AI 必须同时读取 Consumer 自己的 Repository Authority / project docs，不能只凭 Guide 判断项目状态。

普通编码、测试、Review 等已经有明确责任的任务，不默认重新读取整个 Guide corpus。

## 4. Skill 是实际执行入口

进入具体责任后，使用 repository-local installed Skill：

```text
.agents/skills/<skill>/SKILL.md
```

Skill 自己持有 Trigger、Inputs、Procedure、Outputs、Exit、Escalation。Consumer 不需要在线读取 `agentic-dev/docs/methods/**`、`docs/rules/**` 或 `docs/architecture/**` 补齐 Skill 执行语义。

## 5. 项目事实始终属于 Consumer

下列内容不会因为安装 `agentic-dev` 自动变成 upstream 所有：

- Product / Domain facts；
- Requirement / Specification；
- System Architecture / ADR；
- technology policy；
- authorization；
- Roadmap / current work；
- code / tests / verification；
- 项目自己的 rules / policies / guides。

`agentic-dev` 可以给出组织建议，但不会通过安装 Skills 覆盖这些内容。

## 6. 两个最常见的开始方式

新项目：

```text
基本项目情况
→ bootstrap-new-project Guide
→ 最小谈判式澄清
→ Consumer Repository
→ 安装 Skills
→ choosing-next-step
```

已有项目：

```text
Existing Repository
→ 恢复当前 Repository Authority
→ 安装 exact-version Skills
→ 最小 AGENTS / Guide locator integration
→ 验证 native Skill discovery
→ 开始使用
```

已有项目不要求先完成全仓文档重构、Requirement Authority 重建或 Rule 体系重构；这些只在真实项目问题需要时作为可选 remediation。

## 7. 如果仍不知道下一步

不要从 Skill 清单里随机挑一个，也不要让 AI 凭一般软件工程常识生成大而全 Roadmap。

读取当前 Consumer 项目事实，然后使用：

[`choosing-next-step.md`](choosing-next-step.md)

选择当前**最主要、最靠前的阻塞责任**，再进入对应 Skill。

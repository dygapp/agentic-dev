---
id: guide:using-agentic-dev
type: guide
status: active
---

# 使用 agentic-dev

本文是面向人的总览指南。它帮助你理解 `agentic-dev` 如何组织 AI 开发工作，但不参与 ordinary Agent runtime，也不替代 Project / Method / Architecture / Skill / Rule 的正式定义。

## 1. 先区分 Project Knowledge 与 reusable Capability

`agentic-dev` 同时维护两类长期知识：

- **Project Knowledge**：只描述 `agentic-dev` 自身——为什么存在、当前采用哪些 capability、当前走到哪里以及为什么演进成今天这样；
- **Reusable Capability**：Method / Architecture / Skill / Rule / Tool contract，可以在显式 adoption / upgrade 中被 Consumer adopt / adapt / reject。

核心原则：

> **Project 不传播，Capability 传播。**

Project Knowledge 的入口见 `docs/project/README.md`；边界定义见 `docs/architecture/project-knowledge-architecture.md`。

## 2. 五类核心 capability

### Method：一类复杂工作怎样从开始走到完成

Method 定义进入条件、阶段 / 状态、阶段责任、Gate、返回和完成语义。当前 Repository 实际采用哪些 Method、如何选择它们，由 `docs/project/project-capability-profile.md` 持有；Human inventory 见 `docs/methods/README.md`。

### Skill：责任明确后，怎样稳定执行一个有界能力

Skill 具有 Trigger / Inputs / Procedure / Outputs / Exit / Escalation。它可以服务某个 Method，也可以在其他明确任务中复用。

### Rule：当前条件成立时必须遵守什么

Rule 是 policy / constraint / default / invariant / completion requirement。它不要求依附 Skill，可以横切 Method stage、Skill、direct Agent work、repository operation 或 verification。

### Architecture：这些能力长期是什么关系

Architecture 定义可复用 capability 边界、ownership、组合方式和运行不变量。

### Guide：给人看的解释层

Guide 把以上 canonical owner 重新组织成人容易理解的说明、教程和导航。它可以重复解释，但不能成为第二套 Authority。

## 3. Agent 和人从不同入口进入同一套体系

Agent：

```text
AGENTS.md
→ Project Roadmap + Project Capability Profile + GitHub current state
→ Method Selection（若适用）
→ current Method stage / direct responsibility
    ├─→ relevant Architecture
    ├─→ Skill discovery / invocation（如需要）
    └─→ Rule Discovery → applicable Rules
→ execute / verify
```

人：

```text
README.md
├─→ docs/project/README.md
└─→ Guides / directory README
    → 理解 Project / Method / Skill / Rule / Architecture
```

这两个视窗不是两套方法。规范语义和 Project fact 只保存在各自 canonical owner 中。

## 4. 普通开发如何工作

普通软件 / 产品变更在当前 `agentic-dev` Project Capability Profile 中映射到 AI Development Method：

```text
Clarify Intent
→ Specification
→ Technical Planning?（条件阶段）
→ Slice & Ready
→ Execute
→ Converge
→ Ready to Integrate
```

Integration 本身不属于通用 Method；merge、release、deploy 等仍由目标仓库策略和人工 Authority 决定。

每个阶段可以使用对应 Skill，也可以在不需要独立 Skill 时由 Agent 直接按 Authority 工作。Rule 根据当前 phase / activity / technology / artifact / risk 独立发现，并不固定挂在某个 Skill 后面。

## 5. Rule Discovery 为什么存在

随着 Rule 数量增长，把全部规则塞进 prompt 会增加上下文、引入无关约束并降低可维护性。

因此 ordinary runtime 使用：

```text
current task facts / responsibility
→ bounded task signals
→ Rule Discovery
→ 少量 {id, path}
→ 只读取候选正文
→ Agent 做最终语义适用性确认
```

具体 Repository 的 Rule root / Tool locator 属于它自己的 capability instance；通用 discovery contract 属于 Architecture。

人可以通过 `docs/rules/README.md` 浏览当前所有 Rule；Agent 不使用这个 README 进行 runtime routing。

## 6. Consumer 首次采用

首次采用不是复制整个仓库。大致过程是：

1. 恢复 Consumer 自己的 Project / Repository Authority；
2. 选择精确 upstream baseline；
3. 判断哪些 Method / Architecture / Skill / Rule / Tool contract 需要 adopt / adapt / reject；
4. 把接受 capability 写入 Consumer-local canonical owner；
5. 建立 Consumer 自己的 capability profile / Method entry / Skill / Rule discovery；
6. 验证 ordinary runtime 不在线依赖 upstream；
7. 记录 evaluated baseline。

upstream Project Charter / Capability Profile / Roadmap / Evolution 只用于 provenance / understanding，不复制为 Consumer Project state。

正式过程由 `docs/methods/consumer-adoption.md` 定义；人类操作说明见 `adopting-agentic-dev.md`。

## 7. Existing Consumer 升级

升级不是“同步最新版”。正确思路是：

```text
当前 Consumer Project + capability state
→ 选择精确 upstream candidate
→ 比较 reusable capability semantic delta
→ retain / adopt / adapt / replace / reject
→ 必要时更新 Consumer-local capability profile
→ targeted revalidation
→ 记录新的 evaluated baseline
```

Consumer-local Rule 可以继续保持本地差异，例如不同仓库拥有不同 Git commit type / scope。upstream Project state 不属于 upgrade synchronization object。

正式过程由 `docs/methods/consumer-upgrade.md` 定义；人类说明见 `upgrading-agentic-dev.md`。

## 8. 如何理解 Skill 与 Rule

不要把它们理解成 `Skill → Rule` 固定流水线。

例如一次 Git / GitHub 操作：

- Skill 可以定义如何安全读取、执行、写后验证；
- Rule 可以定义当前仓库允许什么操作、commit message 如何表达、何时必须人工授权；
- 某些 Rule 即使没有对应 Skill 也仍然独立生效。

这使通用 procedure 可以复用，同时保留 Consumer-specific policy。

## 9. 当你想新增长期内容时

先问“它真正拥有哪类语义”：

- 当前项目使命、核心需求、capability instance、Roadmap 或稳定演进摘要 → Project；
- 一类复杂工作的阶段 / Gate / 完成模型 → Method；
- 可复用长期结构 / ownership / 不变量 → Architecture；
- 有界稳定执行能力 → Skill；
- 条件性 policy / constraint / default / invariant → Rule；
- 只是给人解释 → Guide；
- 只有证据和探索价值 → Research；
- 只是实施过程 / 当前一次 Gate → GitHub Issue / PR / Actions。

不要因为内容很重要、有步骤、文件很短、当前仓库正在使用或希望减少文件数量就决定类型。

## 10. 推荐阅读顺序

如果你第一次了解项目：

1. 本文；
2. `docs/project/README.md` 与 `project-charter.md`；
3. `docs/methods/README.md`；
4. `docs/architecture/README.md`；
5. `docs/rules/README.md`；
6. `skills/README.md`。

如果你只是使用现有 Consumer 做普通开发，不需要每次重新阅读 upstream Guide 或 upstream Project Knowledge；Consumer-local Repository Authority 应已经提供 Agent 所需入口。
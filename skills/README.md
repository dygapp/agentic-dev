# Skills

第一批核心 Skill 的**工程历史基线已关闭**。

Issue #18 随后的真实使用方项目证据触发了 `slice-work`、`readiness-check`、`execute-unit` 的定向强化；相关修订已经通过针对性全新运行时评估（`4 / 4 PASS`）和最终 AI 复核，相关历史强化已完成。

当前仓库处于：

> **工程能力扩展与方法演进**

关闭第一批核心 Skill 工程的依据不是“目录已经存在”，而是这 8 个核心 Skill 已完成方法 / 架构 / 契约对齐、实现、打包强化、全新运行时评估与最终收尾复核。新的工程能力扩展阶段不会机械重开或重写这 8 个核心 Skill。

后续工程能力的分层、证据进入方式和候选能力生命周期以：

`../docs/architecture/engineering-capability-architecture.md`

为更高层架构依据。

## 当前 Skill 清单

当前仓库共实现 9 个 Skill：

- 8 个核心 Skill，构成已经关闭工程工作的第一批核心基线；
- 1 个平台专项 Skill，即 `github-actions-verification`；
- 当前没有未来实验性 Skill。

平台 / 技术专项 Skill 不计入第一批核心 Skill，也不意味着重新打开核心 Skill 工程。未来新的实验性 Skill 可以由官方权威实践、成熟外部工程经验、专项评估或使用方证据触发候选设计，但只有在职责稳定、与现有能力边界清晰、能够建立有辨识力的专项评估，并完成架构与 AI 复核后才进入正式 Skill 清单。

使用方实践仍是重要后续验证来源，但不再是所有 Skill 候选形成的唯一前置条件。

## 第一批 8 个核心 Skill

| Skill | 状态 |
|---|---|
| `clarify-intent` | 基线已实现，契约复核完成 |
| `specify` | 基线已实现，契约复核完成 |
| `technical-plan` | 基线已实现，契约复核完成 |
| `slice-work` | 基线已实现，契约复核完成 |
| `readiness-check` | 基线已实现，契约复核完成 |
| `execute-unit` | 基线已实现，契约复核完成；运行时发现已完成单执行单元边界强化 |
| `systematic-debug` | 基线已实现，契约复核完成 |
| `converge` | 基线已实现，契约复核完成 |

第一轮全新运行时评估采用代表性覆盖，而不是机械对 8 个 Skill 建设大型基准测试：

- 激活：16 / 16 通过；
- 行为：14 / 14 通过；
- 覆盖 `clarify-intent`、`readiness-check`、`execute-unit`、`converge` 四个关键调用链节点；
- 上述结论属于首轮 B3 历史基线；Issue #18 随后的真实使用方项目证据已暴露验收到验证的闭环缺口；
- `slice-work`、`readiness-check`、`execute-unit` 的针对性修订已经完成；新增行为评估为 `4 / 4 PASS`，本次定向强化已完成工程闭环。

核心 Skill 的后续修改继续由真实问题或更高层架构需要定向驱动，不为了形式完整性机械扩张覆盖或重复设计。

## 平台 / 技术专项 Skill

| Skill | 状态 |
|---|---|
| `github-actions-verification` | 已实现；基于真实使用方证据形成的平台专项非核心工程纪律 Skill |

该 Skill 只在使用方使用 GitHub Actions，且 CI 验证路径、证据可观察性、运行成本或诊断问题会实质影响验证可靠性时按需使用。它实现既有方法 / 治理语义，不新增方法阶段，也不接管集成、发布或部署。

`github-actions-verification` 的形成路径是当前历史证据，不代表未来所有平台 / 技术专项 Skill 都必须重复等待使用方先暴露问题。新的候选 Skill 应按工程能力架构综合使用成熟外部证据、专项评估和使用方实践进行准入判断。

权威设计参考：

- `../docs/architecture/engineering-capability-architecture.md`
- `../docs/architecture/skill-architecture.md`
- `../docs/architecture/skill-contracts.md`
- `../docs/architecture/first-batch-skill-design.md`

打包 / 互操作研究参考：

- `../docs/research/agent-skills-specification-analysis.md`

## Skill 实现原则

不能因为某个上游项目或外部规范存在某个 Skill / 字段 / 目录，就直接复制到本仓库。

每个 Skill 必须能追溯到本地方法 / 工程能力架构中的明确职责。

正式 `SKILL.md` 至少应定义：

```text
Purpose
Use When
Do Not Use When
Inputs
Authority Sources
Procedure
Outputs
Exit Conditions
Escalation Conditions
Context Rules
Allowed Sub-skills / Disciplines
```

这些标题属于当前 Skill 契约的结构身份，保持原样。正文应按当前仓库语言规则使用自然中文。

同时采用与当前外部 Agent Skills Specification 兼容的最小 `name` / `description` front matter，用于打包 / 发现；该元数据不得改变本地契约语义。

实现不得通过 `SKILL.md` 暗中修改方法、架构或已复核契约。若专项评估、使用方实践或运行时使用暴露权威层问题，应先回到对应权威文档处理，再重新进入相应 Skill 设计或实现工作。

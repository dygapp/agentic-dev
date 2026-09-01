# Skills

第一批核心 Skill 的 **Skill 工程历史基线已关闭**。

Issue #18 随后的真实 Consumer 项目证据触发了 `slice-work`、`readiness-check`、`execute-unit` 的定向强化；相关修订已经通过针对性全新运行时评估（`4 / 4 PASS`）和最终 AI 复核，相关历史强化已完成。

当前仓库已进入：

> **Engineering Capability Expansion & Method Evolution（工程能力扩展与方法演进）**

关闭第一批核心 Skill Engineering 的依据不是“目录已经存在”，而是这 8 个核心 Skill 已完成 Method / Architecture / Contract 对齐、实现、Packaging Hardening、Fresh Runtime Eval 与最终 Closure Review。新的工程能力扩展阶段不会机械重开或重写这 8 个核心 Skill。

后续工程能力的分层、证据进入方式和候选能力生命周期以：

`../docs/architecture/engineering-capability-architecture.md`

为更高层架构依据。

## 当前 Skill 清单（Skill Inventory）

当前仓库共实现 9 个 Skill：

- 8 个 Core Skills（核心 Skill），构成已经关闭工程工作的第一批核心基线；
- 1 个 Platform-specific Skill（平台专项 Skill），即 `github-actions-verification`；
- 当前没有 Future Experimental Skill（未来实验性 Skill）。

平台 / 技术专项 Skill 不计入第一批核心 Skill，也不意味着重新打开 Core Skill Engineering。未来新的实验性 Skill 可以由官方权威实践、成熟外部工程经验、专项评估或 Consumer Evidence 触发候选设计，但只有在职责稳定、与现有能力边界清晰、能够建立有辨识力的专项评估，并完成架构与 AI Review 后才进入正式 Skill Inventory。

Consumer 实践仍是重要后续验证来源，但不再是所有 Skill 候选形成的唯一前置条件。

## 第一批 8 个核心 Skill

| Skill | 状态 |
|---|---|
| `clarify-intent` | Baseline 已实现，Contract Review 完成 |
| `specify` | Baseline 已实现，Contract Review 完成 |
| `technical-plan` | Baseline 已实现，Contract Review 完成 |
| `slice-work` | Baseline 已实现，Contract Review 完成 |
| `readiness-check` | Baseline 已实现，Contract Review 完成 |
| `execute-unit` | Baseline 已实现，Contract Review 完成；Runtime finding 已完成 one-unit hardening |
| `systematic-debug` | Baseline 已实现，Contract Review 完成 |
| `converge` | Baseline 已实现，Contract Review 完成 |

第一轮 Fresh Runtime Eval 采用代表性覆盖，而不是机械对 8 个 Skill 建设大型 benchmark：

- Activation：16 / 16 PASS；
- Behavior：14 / 14 PASS；
- 覆盖 `clarify-intent`、`readiness-check`、`execute-unit`、`converge` 四个关键调用链节点；
- 上述结论属于首轮 B3 历史基线；Issue #18 随后的真实 Consumer 项目证据已暴露验收到验证的闭环缺口；
- `slice-work`、`readiness-check`、`execute-unit` 的针对性修订已经完成；新增行为评估为 `4 / 4 PASS`，本次定向强化已完成工程闭环。

核心 Skill 的后续修改继续由真实问题或更高层架构需要定向驱动，不为了形式完整性机械扩张覆盖或重复设计。

## 平台 / 技术专项 Skill

| Skill | 状态 |
|---|---|
| `github-actions-verification` | 已实现；基于真实 Consumer Evidence 形成的平台专项非核心 Discipline Skill |

该 Skill 只在 Consumer 使用 GitHub Actions，且 CI 验证路径、证据可观察性、运行成本或诊断问题会实质影响验证可靠性时按需使用。它实现既有 Method / Governance 语义，不新增方法阶段，也不接管 Integration、Release 或 Deploy。

`github-actions-verification` 的形成路径是当前历史证据，不代表未来所有平台 / 技术专项 Skill 都必须重复等待 Consumer 先暴露问题。新的候选 Skill 应按工程能力架构综合使用成熟外部证据、专项评估和 Consumer 实践进行准入判断。

权威设计参考：

- `../docs/architecture/engineering-capability-architecture.md`
- `../docs/architecture/skill-architecture.md`
- `../docs/architecture/skill-contracts.md`
- `../docs/architecture/first-batch-skill-design.md`

Packaging / Interoperability 研究参考：

- `../docs/research/agent-skills-specification-analysis.md`

## Skill 实现原则

不能因为某个上游项目或外部规范存在某个 Skill / 字段 / 目录，就直接复制到本仓库。

每个 Skill 必须能追溯到本地 Method / Engineering Capability Architecture 中的明确职责。

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

同时采用与当前外部 Agent Skills Specification 兼容的最小 `name` / `description` Front Matter，用于 Packaging / Discovery；该元数据不得改变本地 Contract 语义。

实现不得通过 `SKILL.md` 暗中修改 Method、Architecture 或 reviewed Contract。若专项评估、Consumer 实践或 Runtime 使用暴露权威层问题，应先回到对应权威文档处理，再重新进入相应 Skill 设计或实现工作。
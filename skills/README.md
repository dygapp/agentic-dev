# Skills

第一批核心 Skill 的 **Skill 工程历史基线已关闭**。

Issue #18 随后的真实 Consumer 项目证据触发了 `slice-work`、`readiness-check`、`execute-unit` 的定向强化；相关修订已经通过针对性全新运行时评估（`4 / 4 PASS`）和最终 AI 复核，当前达到 `Ready to Integrate`。

当前仓库已进入：

> **Skill Operationalization & Method Validation**

关闭 Skill Engineering 的依据不是“目录已经存在”，而是第一批核心 Skill 已完成 Method / Architecture / Contract 对齐、实现、Packaging Hardening、Fresh Runtime Eval 与最终 Closure Review。

## 当前 Skill 清单（Skill Inventory）

当前仓库共实现 9 个 Skill：

- 8 个 Core Skills（核心 Skill），构成已经关闭工程工作的第一批核心基线；
- 1 个 Platform-specific Skill（平台专项 Skill），即 `github-actions-verification`；
- 当前没有 Future Experimental Skill（未来实验性 Skill）。

平台专项 Skill 不计入第一批核心 Skill，也不意味着重新打开 Core Skill Engineering。未来只有真实使用证据暴露新的稳定职责缺口时，才评估其他实验性 Skill。

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
- 上述结论属于首轮 B3 历史基线；Issue #18 随后的真实 Consumer 项目证据已暴露验收到验证的闭环缺口。
- `slice-work`、`readiness-check`、`execute-unit` 的针对性修订已经完成；新增行为评估为 `4 / 4 PASS`，本次定向强化已完成工程闭环。

核心 Skill 的后续 Runtime Coverage 应由真实 Operationalization / Method Validation 证据驱动，不为了形式完整性机械扩张。

## 平台专项 Skill

| Skill | 状态 |
|---|---|
| `github-actions-verification` | 已实现；基于真实 Consumer Evidence 的平台专项非核心 Discipline Skill |

该 Skill 只在 Consumer 使用 GitHub Actions，且 CI 验证路径、证据可观察性、运行成本或诊断问题会实质影响验证可靠性时按需使用。它实现既有 Method / Governance 语义，不新增方法阶段，也不接管 Integration、Release 或 Deploy。

权威设计参考：

- `../docs/architecture/skill-architecture.md`
- `../docs/architecture/skill-contracts.md`
- `../docs/architecture/first-batch-skill-design.md`

Packaging / Interoperability 研究参考：

- `../docs/research/agent-skills-specification-analysis.md`

## Skill 实现原则

不能因为某个上游项目或外部规范存在某个 Skill / 字段 / 目录，就直接复制到本仓库。

每个 Skill 必须能追溯到本地 Method Architecture 中的明确职责。

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

实现不得通过 `SKILL.md` 暗中修改 Method、Architecture 或 reviewed Contract。若真实 Runtime 使用暴露权威层问题，应先回到对应权威文档处理，再重新进入 Skill Engineering。

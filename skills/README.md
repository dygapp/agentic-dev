# Skills

当前处于 **Skill Engineering** 阶段。

第一批 8 个核心 Skill 已完成 Contract Review，并已按照已复核契约逐个实现并完成首轮契约验证。当前不以“目录是否存在”作为完成标准，每个 Skill 都必须持续与 Contract 对齐，并由当前证据支持完成状态。

## 第一批 8 个核心 Skill

| Skill | 状态 |
|---|---|
| `clarify-intent` | 已实现，完成首轮契约验证 |
| `specify` | 已实现，完成首轮契约验证 |
| `technical-plan` | 已实现，完成首轮契约验证 |
| `slice-work` | 已实现，完成首轮契约验证 |
| `readiness-check` | 已实现，完成首轮契约验证 |
| `execute-unit` | 已实现，完成首轮契约验证 |
| `systematic-debug` | 已实现，完成首轮契约验证 |
| `converge` | 已实现，完成首轮契约验证 |

权威设计参考：

- `../docs/architecture/skill-architecture.md`
- `../docs/architecture/skill-contracts.md`
- `../docs/architecture/first-batch-skill-design.md`

## Skill 实现原则

不能因为某个上游项目存在某个 Skill，就直接在本仓库中复制一个同名能力。

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

实现不得通过 `SKILL.md` 暗中修改 Method、Architecture 或 reviewed Contract。若实现暴露权威层问题，应先回到对应权威文档处理，再继续 Skill Implementation。

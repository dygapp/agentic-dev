# Skills

Baseline v0.1 暂不包含正式生产级 Skills。

这是刻意设计的阶段边界。

当前先完成 Skill Contract Design，再进入实现。

## 当前 8 个核心候选 Skill

```text
clarify-intent
specify
technical-plan
slice-work
readiness-check
execute-unit
systematic-debug
converge
```

权威设计参考：

- `../docs/architecture/skill-architecture.md`
- `../docs/architecture/skill-contracts.md`

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

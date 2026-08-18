# Research

本目录保存形成当前方法基线所使用的对照研究，以及影响 Skill Packaging / Interoperability 的外部规范研究。

**这些文档不是规范性权威。**

上游项目或外部规范后续发生变化，不会自动改变本仓库的方法。任何 Method / Contract 调整都必须通过显式 Method Decision 完成。

## 对照项目

- `mattpocock/skills`
- `github/spec-kit`
- `obra/superpowers`

研究基线日期：**2026-08-17**

| 项目 | 对当前方法的主要贡献 |
|---|---|
| `mattpocock/skills` | Small/Composable Skills、Human-controlled Orchestration、Vertical Slice、Fresh-context-sized Work、Context/Handoff Discipline |
| `github/spec-kit` | WHAT/WHY 与 HOW 分离、Spec/Plan/Task 产物边界、Readiness、Cross-artifact Consistency |
| `obra/superpowers` | Execution Orchestration、JIT Plan、Evidence-before-claims、Systematic Debugging、Execution Isolation、Reversible Decision Autonomy |

这些项目用于方法对照。本仓库不会复制任何一个上游项目的完整命令链。

## 外部标准 / 规范

- `Agent Skills Specification` — `agent-skills-specification-analysis.md`

规范研究基线日期：**2026-08-18**

Agent Skills Specification 主要用于参考：

- Skill 目录与 `SKILL.md` Packaging；
- `name` / `description` Activation Metadata；
- Progressive Disclosure；
- 可选 `scripts/`、`references/`、`assets/` 组织；
- 静态格式 Validation。

它不是第四个方法论样本，也不定义 `agentic-dev` 的生命周期、职责边界或 Skill Contract。

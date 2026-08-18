# AGENTS.md

## 仓库目标

本仓库用于定义一套通用的 AI Agent 驱动软件开发方法，并实现一组小型、可组合的 Skills。

**方法定义高于 Skill 实现。**

Skill 只能实现方法，不允许通过修改 `SKILL.md` 暗中改变方法。

## 权威顺序

发生冲突时按以下顺序处理：

1. `AGENTS.md`
2. `docs/method/ai-development-method.md`
3. `docs/method/principles.md`
4. `docs/architecture/skill-architecture.md`
5. `docs/architecture/skill-contracts.md`
6. `docs/decisions/method-decisions.md`
7. `docs/guides/git-commit-guidelines.md`
8. `docs/research/*`
9. Tasks 与临时工作记录

如果某个 Skill 的设计要求改变方法本身，必须先显式修改方法文档，再修改 Skill。

## Repository Source of Truth

GitHub repository 是本仓库的唯一长期基线来源。

规则：

- Git commit 记录项目演进历史；
- Branch 用于隔离实验、设计和实现过程；
- ZIP 快照只用于初始化、离线交换或临时备份，不作为持续开发上下文来源。

所有后续 Method、Contract 和 Skill Implementation 变更，应基于 Git repository 状态进行。

## 当前阶段

当前处于：

> **Skill Operationalization & Method Validation**

第一批 8 个核心 Skill 的 **Skill Engineering 已关闭**。关闭基线包括：

- Method / Architecture / Contract 已收敛；
- 8 个核心 Skill 已实现并完成 Contract Review；
- Skill Packaging / Activation Metadata 已标准化；
- Fresh Runtime Eval 已完成，代表性核心场景没有未解决的 Blocking Metadata / Skill Implementation / Contract / Method Gap；
- `Ready to Integrate`、Current Evidence、Fresh Context、Stage Return 与 Human-controlled Integration 的边界已形成一致语义。

当前阶段重点不是继续扩充核心 Skill 数量，而是验证其在真实 Agent / Repository 工作流中的可发现性、激活可靠性、组合调用、运行时编排和方法有效性。

只有真实使用证据暴露新的职责缺口时，才重新进入 Skill Engineering。不得为了形式完整性新增第九个核心 Skill、Super-skill 或不必要的流程层级。

## 核心规则

- 阶段是状态，不是文件。
- Specification 描述 WHAT / WHY，不默认包含 HOW。
- Technical Planning 是条件阶段。
- Execution Unit 应纵向、可独立验证、范围明确、可追溯并适合 fresh context。
- Conversation History 不作为项目权威知识。
- 使用 Progressive Disclosure，只加载当前工作真正需要的上下文。
- 没有当前证据，不得声明完成。
- 普通、低影响、可逆的实现歧义由 Agent 自主裁决并继续。
- 会改变产品意图、具有破坏性或不可逆性、安全/隐私敏感、改变重大架构方向，或超出 Agent 授权的事项必须升级。
- 不创建接管完整生命周期的超级 Skill。
- 通用方法的终点是 Ready to Integrate；merge、push、release、deploy 和破坏性 cleanup 由 Human Authority 或 Repository Policy 控制。

## Research 使用规则

`docs/research/` 只保存研究依据和横向比较。

不能因为上游项目或外部规范使用了某个命令、模板、字段或产物，就直接照搬到本仓库。

必须先区分：

- Method / Contract 语义；
- Skill Packaging / Interoperability 约束；
- Runtime / Tool-specific 实现细节。

任何外部来源都不能自动覆盖本仓库的 Method Authority；需要改变方法时必须通过显式 Method Decision。

## Git Commit

所有提交必须遵循：

`docs/guides/git-commit-guidelines.md`

最小格式：

```text
<type>(<scope>): <中文摘要>
```

重点要求：

- 一次 Commit 只表达一个主要目的；
- Method / Contract Change 与 Skill Implementation Change 原则上分开提交；
- `type`、`scope` 使用小写英文，摘要使用中文；
- 不使用“更新文件”“修改内容”等无法独立表达目的的摘要。

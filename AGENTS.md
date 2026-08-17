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

## 当前阶段

当前处于：

> **Skill Contract Design**

暂不批量实现 Skills。

在创建或重大修改一个 Skill 前，必须先确认：

1. 它对应哪个方法阶段或横切职责；
2. 输入、输出、退出条件、上下文规则和人工升级条件是否明确；
3. 是否与其他 Skill 存在职责重叠；
4. Workflow Skill 与 Discipline Rule 是否被错误混合；
5. 是否可以进一步缩小职责边界。

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

不能因为上游项目使用了某个命令、模板或产物，就直接照搬到本仓库。

必须先抽象其底层工程原则，再判断是否应该进入本方法。

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

# agentic-dev

面向 AI Agent 驱动软件开发的方法体系与可组合 Skills 实现仓库。

## 当前状态

**基线版本：** v0.1  
**当前阶段：** Skill Engineering。第一批 8 个核心 Skill Contract 已完成复核并形成 Design Baseline，下一步按已复核契约逐个实现和验证 Skill。

本仓库基于以下三个项目的对照研究与方法收敛形成：

- `mattpocock/skills`
- `github/spec-kit`
- `obra/superpowers`

这些项目是研究输入，不是本仓库的运行时依赖，也不直接构成本仓库的方法权威。

## Repository Source of Truth

GitHub repository 是本项目长期演进的唯一基线来源。Git commit 记录项目演进，Branch 隔离设计与实现工作；ZIP 只用于初始化、离线交换或临时备份。

详细规则见：

`docs/project/repository-baseline.md`

## 权威顺序

当文档内容发生冲突时，按以下顺序判断：

1. `AGENTS.md`
2. `docs/method/ai-development-method.md`
3. `docs/method/principles.md`
4. `docs/architecture/skill-architecture.md`
5. `docs/architecture/skill-contracts.md`
6. `docs/decisions/method-decisions.md`
7. `docs/guides/git-commit-guidelines.md`
8. `docs/research/*`
9. Tasks 与临时工作记录

`docs/research/` 只负责说明“为什么形成当前方法”，不能覆盖已经固化的方法结论。

## 核心开发流程

常规 Feature 主流程：

```text
Governance / Domain Context
        ↓
Clarify Intent
        ↓
Specification
        ↓
Technical Planning?（按需）
        ↓
Slice & Ready
        ↓
Fresh-context Execute
        ↓
Converge
        ↓
Full Verification
        ↓
Ready to Integrate
        ↓
Human / Project Policy
```

缺陷处理采用独立的轻量流程：

```text
Observed Symptom
    ↓
Reproduce
    ↓
Root Cause Investigation
    ↓
Hypothesis
    ↓
Failing / Reproduction Evidence
    ↓
Minimal Fix
    ↓
Regression Verification
```

## 核心设计原则

- 阶段是工作状态，不等于必须创建文档。
- Specification 负责 **WHAT / WHY**。
- Technical Plan 负责 **HOW**，且只在必要时产生。
- 实施工作拆分为纵向、可验证、适合 fresh context 的 Execution Unit。
- 具体文件路径、测试命令和施工步骤优先在执行时通过 JIT Plan 临时生成。
- 所有“完成、通过、修复成功”等状态声明必须有当前证据。
- Conversation History 不是权威知识库。
- Human Escalation 依据 Authority、Impact、Reversibility 判断。
- Human 负责不可逆意图，AI 负责可逆执行。
- 通用开发方法只推进到 Ready to Integrate。
- Skills 应保持小型、可组合，不允许一个 Skill 接管完整生命周期。

## 仓库结构

```text
.
├── AGENTS.md
├── README.md
├── docs/
│   ├── method/
│   │   ├── ai-development-method.md
│   │   └── principles.md
│   ├── architecture/
│   │   ├── skill-architecture.md
│   │   ├── skill-contracts.md
│   │   └── first-batch-skill-design.md
│   ├── decisions/
│   │   └── method-decisions.md
│   ├── guides/
│   │   └── git-commit-guidelines.md
│   ├── project/
│   │   └── repository-baseline.md
│   └── research/
│       ├── README.md
│       ├── mattpocock-skills-analysis.md
│       ├── spec-kit-analysis.md
│       └── superpowers-analysis.md
├── skills/
│   └── README.md
└── tasks/
    └── README.md
```

## Git Commit 规范

仓库统一采用：

```text
<type>(<scope>): <中文摘要>
```

完整规则见：

`docs/guides/git-commit-guidelines.md`

特别要求 Method / Contract 变更与 Skill Implementation 变更保持清晰分层，避免通过实现提交暗中改写方法权威。

## 下一阶段

第一批 Skill 已完成 Contract Review 与实现设计基线。后续按照 `docs/architecture/first-batch-skill-design.md` 逐个实现和验证，不批量生成全部 `SKILL.md`。

当前优先实现：

1. `readiness-check`
2. `slice-work`
3. 其余 Skill 按设计基线顺序推进

每个 Skill 实现必须继续遵守 `docs/architecture/skill-contracts.md`，发现 Contract 问题时先修改并提交权威 Contract，再调整实现。

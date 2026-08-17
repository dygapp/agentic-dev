# agentic-dev

面向 AI Agent 驱动软件开发的方法体系与可组合 Skills 实现仓库。

## 当前状态

**基线版本：** v0.1  
**当前阶段：** 方法基线已固化，进入 Skill 契约设计阶段，尚未开始正式实现 Skills。

本仓库基于以下三个项目的对照研究与方法收敛形成：

- `mattpocock/skills`
- `github/spec-kit`
- `obra/superpowers`

这些项目是研究输入，不是本仓库的运行时依赖，也不直接构成本仓库的方法权威。

## 权威顺序

当文档内容发生冲突时，按以下顺序判断：

1. `AGENTS.md`
2. `docs/method/ai-development-method.md`
3. `docs/method/principles.md`
4. `docs/architecture/skill-architecture.md`
5. `docs/architecture/skill-contracts.md`
6. `docs/decisions/method-decisions.md`
7. `docs/research/*`
8. Tasks 与临时工作记录

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
│   │   └── skill-contracts.md
│   ├── decisions/
│   │   └── method-decisions.md
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

## 下一阶段

正式编写 `SKILL.md` 前，优先完成：

1. 复核 8 个核心 Skill 候选的职责边界。
2. 检查 Skill Contract 是否存在职责重叠或能力断层。
3. 决定哪些横切能力继续作为内嵌 discipline，哪些值得升级为独立 Skill。
4. 冻结第一版 Skill Contract。
5. 按单个 Skill 逐步实现和验证。

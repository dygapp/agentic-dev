# agentic-dev

面向 AI Agent 驱动软件开发的方法体系与可组合 Skills 实现仓库。

## Quick Start

如果你希望使用 `agentic-dev` 启动一个新的软件项目，先阅读：

`docs/guides/using-agentic-dev.md`

推荐在一个新的 Chat / Codex Context 中开始，并把 `agentic-dev` Repository 作为方法与 Skills 知识源提供给 Agent。不要提前复制一套大而全的项目模板；让 Agent 根据项目目标、已建立的 Consumer Authority、明确提供的 Requirement Source 和 Operating Guide 建立足以启动工作的最小 Repository Authority，并随着真实工作逐步丰富项目结构。

可以使用下面的提示词作为新项目会话起点：

```text
我要创建并持续开发一个新的软件项目。

项目目标：
<用几句话描述真实项目或当前建设目标>

开发方法与可用 Skills：
<agentic-dev repository path or URL>

已建立的 Consumer Authority（如有）：
<current project rules, authoritative requirements, repository paths, or none>

Requirement Source / 初始业务输入（如有）：
<external requirement files, repository paths, URLs, or concise input>

目标项目目录 / Repository：
<consumer repository path or target location>

请先读取 agentic-dev 的 Operating Guide，并按其中的知识边界、Requirement Source 采纳、项目渐进演进、Skill 使用和 Fresh Context 规则开展工作。

不要仅因为某份 Requirement Source 被提供、复制到 Consumer Repository，或自身标记为 confirmed / approved，就自动把它视为当前 Consumer Authority；应先根据 Operating Guide 判断其 provenance、当前有效 Scope、Authority precedence 和 upstream references。

先根据当前项目实际情况建立启动项目所需的最小骨架和 Repository Authority，不要预先创建没有真实需要的大而全文档或目录体系。随后从当前 Intent / Requirements 开始，逐步推进 Specification、必要的 Technical Planning、Work Slicing、Execution 和 Convergence。

除非我明确提供，否则不要使用其他会话、其他项目或个人记忆中的隐含知识作为本项目事实。
```

如果当前工作被明确作为 `agentic-dev` Experiment / Validation，还应在提示词末尾补充：

```text
本项目属于 agentic-dev Experiment。请按照 Operating Guide 的 Experimental Use 规则保持上下文隔离，并通过 agentic-dev Repository 的 GitHub Issue 回传有意义的实践证据。
```

该模板只是启动入口，不是固定执行脚本。后续项目结构、Artifact 和 Skill 应根据真实需求逐步形成。

## 当前状态

**基线版本：** v0.1  
**当前阶段：** **Skill Operationalization & Method Validation**

第一批 8 个核心 Skill 的 **Skill Engineering Baseline 已关闭**：

- Method / Architecture / Contract 已收敛；
- 8 个核心 Skill 已实现并完成 Contract Review；
- Skill Packaging / Activation Metadata 已标准化；
- 第一轮 Fresh Runtime Eval：Activation `16 / 16 PASS`，Behavior `14 / 14 PASS`；
- 当前没有未解决的 Blocking Metadata / Skill Implementation / Contract / Method Gap。

下一阶段重点是验证这些 Skills 在真实 Agent / Repository 工作流中的发现、激活、组合、编排和方法有效性，而不是继续机械增加核心 Skill 数量。

## 研究来源

本仓库的方法基线主要由以下三个项目的对照研究收敛形成：

- `mattpocock/skills`
- `github/spec-kit`
- `obra/superpowers`

此外，`Agent Skills Specification` 作为 Skill Packaging / Interoperability 的外部规范参考。

这些来源都是研究输入，不是本仓库的运行时依赖，也不直接构成本仓库的方法权威。

## Repository Source of Truth

GitHub repository 是本项目长期演进的唯一基线来源。Git commit 记录项目演进，Branch 隔离设计与实现工作；ZIP 只用于初始化、离线交换或临时备份。

详细规则见：

`docs/project/repository-baseline.md`

## Repository Authority

仓库权威顺序、知识边界和 Agent 工作规则以 `AGENTS.md` 为统一入口；README 不重复维护规范性清单。

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
Readiness Gate
        ↓
Fresh-context Execute
        ↓
Converge
        ↓
Ready to Integrate
        ↓
Human / Repository Policy
```

Standalone Defect 使用轻量独立路径：

```text
Observed Symptom
    ↓
Reproduce
    ↓
Expected Behavior
    ↓
Root Cause Investigation
    ↓
Failing / Reproduction Evidence
    ↓
Minimal Fix
    ↓
Regression Verification
    ↓
Defect Closure Check
    ↓
Ready to Integrate
```

## 核心设计原则

- 阶段是工作状态，不等于必须创建文档。
- Specification 负责 **WHAT / WHY**。
- Technical Plan 负责长期 **HOW**，且只在必要时产生。
- 实施工作拆分为纵向、可验证、适合 Fresh Context 的 Execution Unit。
- 具体文件路径、测试命令和施工步骤优先在执行时通过 JIT Plan 临时生成。
- 所有“完成、通过、修复成功”等状态声明必须有当前证据。
- Conversation History 不是权威知识库。
- Human Escalation 依据 Authority、Impact、Reversibility 判断。
- 普通、低影响、可逆的局部实现选择由 Agent 自主处理。
- 通用开发方法只推进到 Ready to Integrate。
- Merge / Push / Release / Deploy 由 Human Authority 或 Repository Policy 控制。
- Skills 保持小型、可组合，不允许一个 Super-skill 接管完整生命周期。

## 第一批核心 Skills

```text
clarify-intent
      ↓
specify
      ↓
technical-plan?   (conditional)
      ↓
slice-work
      ↓
readiness-check
      ↓
execute-unit
      │
      └─ systematic-debug on unexpected failure
      ↓
converge
```

第一批固定为：

- `clarify-intent`
- `specify`
- `technical-plan`
- `slice-work`
- `readiness-check`
- `execute-unit`
- `systematic-debug`
- `converge`

详见 `skills/README.md`。

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
│   │   ├── git-commit-guidelines.md
│   │   └── using-agentic-dev.md
│   ├── project/
│   │   └── repository-baseline.md
│   └── research/
│       ├── README.md
│       ├── mattpocock-skills-analysis.md
│       ├── spec-kit-analysis.md
│       ├── superpowers-analysis.md
│       └── agent-skills-specification-analysis.md
├── skills/
│   ├── README.md
│   ├── clarify-intent/
│   ├── specify/
│   ├── technical-plan/
│   ├── slice-work/
│   ├── readiness-check/
│   ├── execute-unit/
│   ├── systematic-debug/
│   └── converge/
├── evals/
│   ├── README.md
│   ├── activation/
│   ├── behavior/
│   └── fixtures/
└── tasks/
    └── README.md
```

## Git Commit 规范

完整规则见：

`docs/guides/git-commit-guidelines.md`

## 下一阶段

当前进入 **Skill Operationalization & Method Validation**。优先目标是：

1. 通过 Operating Guide 让 Fresh Agent 能够从真实需求启动并持续推进 Consumer Repository；
2. 在独立真实 Repository 中验证完整方法、Skills 组合、Fresh Context 与项目渐进演进；
3. 通过真实 Experiment Evidence 识别 Usage / Skill / Contract / Method / Project Rule Gap；
4. 仅在真实使用证明必要时，再处理 Distribution、Bootstrap 自动化、Controller / Runtime Orchestration 或重新进入 Skill Engineering。

下一阶段默认不新增第九个核心 Skill，也不继续扩大方法论研究样本。

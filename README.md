# agentic-dev

面向 AI Agent 驱动软件开发的方法体系、工程能力架构与可组合 Skills 实现仓库。

## 快速开始

如果你希望使用 `agentic-dev` 启动一个新的软件项目，先阅读：

`docs/guides/using-agentic-dev.md`

推荐在新的 Chat / Codex Context 中开始，并把 `agentic-dev` 仓库作为方法与 Skills 知识源提供给 Agent。不要提前复制一套大而全的项目模板；让 Agent 根据项目目标、已建立的 Consumer 权威（Consumer Authority）、明确提供的需求来源（Requirement Source）和使用指南（Operating Guide），建立足以启动工作的最小仓库权威（Repository Authority），并随着真实工作逐步丰富项目结构。

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

先根据当前项目实际情况建立启动项目所需的最小骨架和 Repository Authority，不要预先创建没有真实需要的大而全文档或目录体系。如果项目预计跨越多个里程碑、阶段或 Fresh Context，且需要可恢复的整体路线，请按 Operating Guide 建立或更新可发现的项目路线图（Project Roadmap）；不要强制固定模板，也不要把完整规则复制进启动提示。随后从当前 Intent / Requirements 开始，逐步推进 Specification、必要的 Technical Planning、Work Slicing、Execution 和 Convergence。

除非我明确提供，否则不要使用其他会话、其他项目或个人记忆中的隐含知识作为本项目事实。
```

如果当前工作被明确作为 `agentic-dev` 实验 / 验证（Experiment / Validation），还应在提示词末尾补充：

```text
本项目属于 agentic-dev Experiment。请按照 Operating Guide 的 Experimental Use 规则保持上下文隔离，并通过 agentic-dev Repository 的 GitHub Issue 回传有意义的实践证据。
```

该模板只是启动入口，不是固定执行脚本。后续项目结构、产物（Artifact）和 Skill 应根据真实需求逐步形成。

## 当前状态

**基线版本：** v0.1  
**当前阶段：** **Engineering Capability Expansion & Method Evolution（工程能力扩展与方法演进）**

第一批 8 个核心 Skill 的历史 Skill 工程基线、首轮真实 Consumer Experiment，以及围绕验收闭环、外部操作、验证证据、Human Review、共享资源、配置责任与已有能力复用的多轮定向强化均已完成。仓库当前共有 9 个 Skill，其中包括 8 个 Core Skills 和 1 个 Platform-specific Skill：`github-actions-verification`。

项目当前从“主要等待 Consumer 暴露问题后定向修补”切换为主动工程能力演进：可以从官方权威实践、成熟开源工程经验、专家研究、专项评估和 Consumer Evidence 中提炼候选能力，再通过工程能力分层、Targeted Eval、AI Review 和 Consumer Adoption 持续完善。

Consumer Evidence 仍然重要，但不再是所有工程能力、Technology Profile 或候选 Skill 的唯一前置条件。

项目演进路线、完整里程碑、当前证据基线与下一步工作统一维护在：

`docs/project/project-roadmap.md`

工程能力分层与能力生命周期统一维护在：

`docs/architecture/engineering-capability-architecture.md`

## 研究来源

本仓库最初的方法基线主要由以下三个项目的对照研究收敛形成：

- `mattpocock/skills`
- `github/spec-kit`
- `obra/superpowers`

此外，`Agent Skills Specification` 作为 Skill 打包与互操作（Packaging / Interoperability）的外部规范参考；后续也已经通过 `multica-ai/andrej-karpathy-skills` 等定向研究补充工程纪律视角。

进入工程能力扩展阶段后，Research 不再局限于最初的方法论样本。官方框架文档、成熟开源工程实践、专家方法与专项技术研究都可以成为候选能力输入，但必须经过当前 Repository Authority 的分层、评估与固化，不能因为外部来源成熟就自动覆盖本仓库规则。

这些来源都是研究输入，不是本仓库的运行时依赖，也不直接构成本仓库的方法权威。

## 仓库事实来源（Repository Source of Truth）

GitHub 仓库是本项目长期演进的唯一基线来源。Git commit 记录项目演进，Branch 隔离设计与实现工作；ZIP 只用于初始化、离线交换或临时备份。

详细规则见：

`docs/project/repository-baseline.md`

## 仓库权威（Repository Authority）

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

独立缺陷（Standalone Defect）使用轻量路径：

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
- 规格说明（Specification）负责 **WHAT / WHY**。
- 技术计划（Technical Plan）负责长期 **HOW**，且只在必要时产生。
- 实施工作拆分为纵向、可验证、适合 Fresh Context 的执行单元（Execution Unit）。
- 具体文件路径、测试命令和施工步骤优先在执行时通过即时计划（JIT Plan）临时生成。
- 所有“完成、通过、修复成功”等状态声明必须有当前证据（Current Evidence）。
- 每项规格验收义务必须闭环到明确的实现 / 验证责任、计划验证证据与已执行的当前证据；实现覆盖不自动等同于验证覆盖。
- 会话历史（Conversation History）不是权威知识库。
- 人工升级（Human Escalation）依据 Authority、Impact、Reversibility 判断。
- 普通、低影响、可逆的局部实现选择由 Agent 自主处理。
- 通用开发方法只推进到 `Ready to Integrate`。
- Merge / Push / Release / Deploy 由人工权威（Human Authority）或仓库策略（Repository Policy）控制。
- Skills 保持小型、可组合，不允许一个 Super-skill 接管完整生命周期。

## Skill 清单（Skill Inventory）

当前仓库共实现 9 个 Skill：第一批 8 个核心 Skill，以及 1 个平台专项非核心 Skill。Future Experimental Skills 当前为 0。

新的实验性 Skill 不再要求必须先由多个 Consumer 重复暴露同一问题；可以由官方权威实践、成熟外部经验、专项评估或 Consumer Evidence 触发候选设计，但仍必须满足工程能力架构和 Skill 架构定义的职责、边界、专项评估与 AI Review 要求。

### 第一批核心 Skills

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

### 平台专项 Skill

- `github-actions-verification`：面向使用 GitHub Actions 的 Consumer，按需建立或优化可观察、可追踪且成本可控的 CI 验证路径。

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
│   │   ├── engineering-capability-architecture.md
│   │   ├── skill-architecture.md
│   │   ├── skill-contracts.md
│   │   └── first-batch-skill-design.md
│   ├── decisions/
│   │   └── method-decisions.md
│   ├── guides/
│   │   ├── external-operation-guidelines.md
│   │   ├── git-commit-guidelines.md
│   │   ├── terminology-guidelines.md
│   │   └── using-agentic-dev.md
│   ├── project/
│   │   ├── ai-review-guidelines.md
│   │   ├── project-roadmap.md
│   │   └── repository-baseline.md
│   └── research/
│       ├── README.md
│       ├── mattpocock-skills-analysis.md
│       ├── spec-kit-analysis.md
│       ├── superpowers-analysis.md
│       ├── agent-skills-specification-analysis.md
│       └── andrej-karpathy-skills-analysis.md
├── skills/
│   ├── README.md
│   ├── clarify-intent/
│   ├── specify/
│   ├── technical-plan/
│   ├── slice-work/
│   ├── readiness-check/
│   ├── execute-unit/
│   ├── systematic-debug/
│   ├── converge/
│   └── github-actions-verification/
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

## 项目演进路线

当前核心目标是建立可主动演进的工程能力体系：在保持 Core Method 稳定的前提下，逐步建设 Engineering Discipline、Technology Profile、Verification Profile、Task-oriented Skill 与 Runtime Adapter，并通过专项评估和 Consumer Integration 双重验证持续完善。

具体路线、当前进度、下一步工作和新上下文恢复入口见：

`docs/project/project-roadmap.md`

README 只提供稳定入口，不重复维护易变化的详细项目状态。
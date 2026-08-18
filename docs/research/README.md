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

## 针对性复核：Reusable Capability 与 Project Rule

复核日期：**2026-08-18**

本轮只针对当前真实问题复核既有三个研究样本，没有扩展新的方法论样本。

观察结果：

- `mattpocock/skills` 使用 `setup-matt-pocock-skills` 这类 repo setup Skill，将可复用 Setup Procedure 实例化为当前仓库自己的 `AGENTS.md` / `CLAUDE.md` 与 `docs/agents/*` 配置；同时其 agent 文档写作规则强调通过 Context Pointer 和 Progressive Disclosure 控制 always-loaded context；
- `github/spec-kit` 将 `constitution` 作为可复用治理能力，但实际治理内容固化到当前项目的 `.specify/memory/constitution.md`，并提供 Project-local Override、Preset 与 Extension 等不同层次的定制方式；
- `obra/superpowers` 采用 composable Skills 与 initial instructions 组合，说明可复用 Skill 与项目 / Runtime 层规则可以并存，而不要求所有规则都进入 Skill。

本轮复核支持以下架构边界：

1. 可复用执行能力与项目实例规则应分离；
2. Project Rule 应存在于当前 Repository Authority 中，而不是隐藏在 Skill Implementation 或 Conversation History 中；
3. Bootstrap / Setup Capability 可以负责把通用流程实例化为项目规则；
4. **可复用本身不足以证明应该创建 Skill**，仍需要真实跨项目使用证据、独立职责和稳定输入输出；
5. 不因为本轮复核新增第九个核心 Skill、Bootstrap Framework、Template System、Preset、Bundle 或 Marketplace。

该结论只作为 `skill-architecture.md` 当前边界设计的研究依据，不自动成为 Method / Contract Authority。

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

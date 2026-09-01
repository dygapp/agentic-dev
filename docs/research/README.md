# Research

本目录保存形成当前方法基线所使用的对照研究，以及后续工程能力扩展阶段产生的外部项目、官方实践、技术框架、工程纪律和 Skill Packaging / Interoperability 研究。

**这些文档不是规范性权威。**

上游项目、框架或外部规范后续发生变化，不会自动改变本仓库的方法或工程能力。任何长期规则都必须进入与其层次匹配的 Repository Authority：Method / Contract 调整必须遵循对应高层权威，Engineering Discipline、Technology Profile、Verification Profile、Skill 或 Runtime Adapter 则必须按 `docs/architecture/engineering-capability-architecture.md` 完成分层、验证与固化。

## 方法基线对照项目

- `mattpocock/skills`
- `github/spec-kit`
- `obra/superpowers`

研究基线日期：**2026-08-17**

| 项目 | 对当前方法的主要贡献 |
|---|---|
| `mattpocock/skills` | Small/Composable Skills、Human-controlled Orchestration、Vertical Slice、Fresh-context-sized Work、Context/Handoff Discipline |
| `github/spec-kit` | WHAT/WHY 与 HOW 分离、Spec/Plan/Task 产物边界、Readiness、Cross-artifact Consistency |
| `obra/superpowers` | Execution Orchestration、JIT Plan、Evidence-before-claims、Systematic Debugging、Execution Isolation、Reversible Decision Autonomy |

这些项目用于最初的方法对照。本仓库不会复制任何一个上游项目的完整命令链。

## 后续定向研究

工程能力扩展阶段允许主动增加新的定向研究样本，不要求它们先成为完整“方法论样本”。

当前已增加：

- `andrej-karpathy-skills-analysis.md`：分析 `multica-ai/andrej-karpathy-skills`，主要提供最小实现、推测性复杂度控制、精准修改和运行时打包等工程纪律参考；当前结论是不新增同名 Skill，也不直接修改 Method。
- `implementation-minimality-and-speculative-complexity-analysis.md`：WI-02 首项工程纪律研究。综合 YAGNI、Simple Design、Google Engineering Practices、Sandi Metz、Go 官方工程实践以及本地 PR #41 / #42，形成“实现最小化与推测性复杂度控制”的 Candidate Capability 和 Targeted Eval 设计；当前状态为 **Candidate / Pending Targeted Eval**，尚未进入规范性工程能力基线。

后续 Research 可以包括：

- 官方框架与语言实践；
- 成熟开源工程项目；
- 专家工程方法；
- Technology Profile 所需的专项技术研究；
- Verification Profile 与 Targeted Eval 设计依据；
- Runtime / Packaging / Distribution 研究。

新增研究样本不自动意味着扩大 Method 样本，也不自动要求新增 Skill。

## 针对性复核：Reusable Capability 与 Project Rule

复核日期：**2026-08-18**

该历史复核当时只针对既有三个方法研究样本，没有扩展新的方法论样本。

观察结果：

- `mattpocock/skills` 使用 `setup-matt-pocock-skills` 这类 repo setup Skill，将可复用 Setup Procedure 实例化为当前仓库自己的 `AGENTS.md` / `CLAUDE.md` 与 `docs/agents/*` 配置；同时其 agent 文档写作规则强调通过 Context Pointer 和 Progressive Disclosure 控制 always-loaded context；
- `github/spec-kit` 将 `constitution` 作为可复用治理能力，但实际治理内容固化到当前项目的 `.specify/memory/constitution.md`，并提供 Project-local Override、Preset 与 Extension 等不同层次的定制方式；
- `obra/superpowers` 采用 composable Skills 与 initial instructions 组合，说明可复用 Skill 与项目 / Runtime 层规则可以并存，而不要求所有规则都进入 Skill。

该历史复核支持以下架构边界：

1. 可复用执行能力与项目实例规则应分离；
2. Project Rule 应存在于当前 Repository Authority 中，而不是隐藏在 Skill Implementation 或 Conversation History 中；
3. Bootstrap / Setup Capability 可以负责把通用流程实例化为项目规则；
4. **可复用本身不足以证明应该创建 Skill**，仍需要独立职责、稳定输入输出和足够证据；
5. 不因为发现一个外部 Skill 就直接增加核心 Skill、Bootstrap Framework、Template System、Preset、Bundle 或 Marketplace。

关于“足够证据”的现行规则已经由 `engineering-capability-architecture.md` 扩展：官方权威实践、成熟外部工程经验、Targeted Eval 与 Consumer Evidence 都可以参与证明稳定职责，不再把历史上的“先有真实跨项目使用证据”视为所有 Skill 的唯一准入路径。

该结论仍只作为架构设计的研究依据，不自动成为 Method / Contract Authority。

## 外部标准 / 规范

- `Agent Skills Specification` — `agent-skills-specification-analysis.md`

规范研究基线日期：**2026-08-18**

Agent Skills Specification 主要用于参考：

- Skill 目录与 `SKILL.md` Packaging；
- `name` / `description` Activation Metadata；
- Progressive Disclosure；
- 可选 `scripts/`、`references/`、`assets/` 组织；
- 静态格式 Validation。

它不是额外的方法论样本，也不定义 `agentic-dev` 的生命周期、职责边界或 Skill Contract。
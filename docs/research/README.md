# Research

本目录保存形成当前方法基线所使用的对照研究，以及后续工程能力扩展阶段产生的外部项目、官方实践、技术框架、工程纪律和 Skill Packaging / Interoperability 研究。

**这些文档不是规范性权威。**

上游项目、框架或外部规范后续发生变化，不会自动改变本仓库的方法或工程能力。任何长期规则都必须进入与其层次匹配的 Repository Authority：Method / Contract 调整必须遵循对应高层权威，Engineering Discipline、Technology Profile、Verification Profile、Skill 或 Runtime Adapter 则必须按 `docs/architecture/engineering-capability-architecture.md` 完成分层、验证与固化。

Research 文档可以保留“研究形成时”的 Candidate / Pending 状态作为历史快照；判断某项能力当前是否已经 Draft、Validated 或 Integrated 时，应读取对应规范性 Authority、Project Roadmap 与当前 GitHub 状态，而不是只看 Research 文档头部的历史状态。

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
- `implementation-minimality-and-speculative-complexity-analysis.md`：WI-02 首项工程纪律研究。该 Research 形成“实现最小化与推测性复杂度控制”的 Candidate；其历史 Candidate 状态已经由后续 WI-03V 推进，当前规范性能力已通过 PR #48 集成到 `docs/architecture/engineering-disciplines.md`。
- `surgical-change-and-diff-scope-control-analysis.md`：WI-03 第二项工程纪律研究。该 Research 形成“精准修改与差异范围控制”的 Candidate；其历史 Candidate 状态同样已经由 PR #48 推进为当前规范性 Engineering Discipline。其核心判断单位仍是“一个可解释、可验证的逻辑变化”，而不是机械的最少行数或文件数。
- `vue3-typescript-profile-analysis.md`：WI-05 首个 Technology Profile 研究。以 Vue `3.5.42`、TypeScript `7.0.2`、Vue Language Tools `3.3.11`、Vue 官方 docs 与 `@vue/tsconfig` 当前证据为主要基线，形成 Vue 3 + TypeScript 组合 Profile 的 Architecture Fit、规则候选与 Targeted Eval 设计。当前规范性实例位于 `docs/technology-profiles/vue3-typescript.md`；PR #50 已完成 Fresh Runtime `9 / 9 PASS`、`41 / 41 assertions PASS` 并正式集成，当前 Profile 生命周期状态以规范性实例和 Project Roadmap 为准。
- `data-access-scope-boundedness-analysis.md`：Engineering Discipline Expansion v1 的单一候选研究。结合 Issue #33 已核验的多个 Consumer 数据访问实例，以及 Google AIP、Relay Connections、PostgreSQL 和 Kubernetes API 的当前外部证据，研究 Consumer Scope、集合 Boundedness / Growth、Lifecycle / Freshness、Filtering / Ordering、Window / Pagination、Representation 与 Verification 的组合判断。Architecture Fit 当前结论为 **Engineering Discipline + thin `execute-unit` consumption**；Draft 与 Targeted Eval 仍需完成验证后才能进入现行 Repository Authority。
- `knowledge-activation-and-code-intelligence-analysis.md`：规则治理与知识激活 v1 的主要研究输入。系统整理大型指南 / 文档型超级能力、激活单元、常驻核心规则、任务 / 风险 → 规则检索、Obsidian 人类知识治理边界、`colbymchenry/codegraph` 的精确上下文、有类型关系、单一强入口、陈旧处理和检索评估经验，以及使用方直接采用代码智能的职责边界；同时固化代码复核、技术画像与 AI 友好代码的后续规划判断。该文档只保存研究依据，活动里程碑、后继 WI-07 边界和当前下一步以项目路线图、Issue #73 与项目计划为准。
- `knowledge-activation-evidence-appendix.md`：上述研究的关键证据附录，保存当前指南体量、PR #72“已有规则但未可靠激活”的具体反例、CodeGraph 子代理约 `1 / 9` 主动发现能力与短激活提示后的对照、单一强入口和常驻指令控制、第一方基准测试边界、Codex 集成方式、`code-review` 当前正式架构身份、Issue #71 / AR-04 的独立复核证据等容易在新上下文中遗漏的事实。后续恢复本轮研究时应与主研究文档一起读取。
- `rule-activation-audit-baseline.md`：规则治理与知识激活 v1 阶段 A / A1 审计基线。冻结当前 `master`、两份高影响指南及直接交叉入口的精确身份，登记后续 A2～A4 必须覆盖的高影响交叉主题，并把 PR #59 / #60 / #61 / #72、Issue #33 / #52 的真实历史摩擦固化为 A5 与后续检索 / 激活评估的场景候选。该文档只保存审计证据，不把交叉主题提前定义为最终规则单元，也不修改现行指南或技能行为。
- `using-agentic-dev-activation-map.md`：规则治理与知识激活 v1 阶段 A / A2 的使用指南激活映射。基于当前 `using-agentic-dev.md` 按语义识别 27 个规则激活单元候选，记录触发条件、消费者、强度、上下文层级、交叉关系与历史证据，并只提名 3 个常驻核心候选。该文档不改变源指南，也不提前完成 A4 的重复 / 冲突判断或 A5 的失效分类。
- `external-operation-guidelines-activation-map.md`：规则治理与知识激活 v1 阶段 A / A3 的外部操作指南激活映射。基于当前 `external-operation-guidelines.md` 按外部状态与风险条件识别 28 个规则激活单元候选，不新增全局常驻核心候选，并重点区分普通写后验证、跨仓库授权、异步闭环、媒体输入、共享资源 / 租约、临时证据晋升、依赖 PR 拓扑与 GitHub 执行路径。该文档不改变源指南，也不提前完成 A4 / A5。
- `cross-authority-duplication-audit.md`：规则治理与知识激活 v1 阶段 A / A4 的跨权威重复审计。比较 AGENTS、README、两份高影响指南、相关 Skill 与项目规则，区分薄摘要 / 激活指针、职责消费、范围敏感关系、历史证据和实质重复候选，并识别证据晋升、验证触发拓扑、执行单元身份 / 就绪重入、异步共享资源和项目状态摘要等后续减法候选。该文档不直接删除规则，实际收敛仍需后续检索 / 激活评估支持。
- `activation-failure-classification.md`：规则治理与知识激活 v1 阶段 A / A5 的历史失效分类。对 A1 冻结的六个真实场景区分发现 / 激活失败、选择 / 冲突失败、指令密度、误导 / 陈旧上下文和真实规则缺口，并明确历史上确实存在过使用层 / 平台专项规则缺口，但这些缺口已经进入当前仓库权威。当前阶段下一重点因此转向最小检索契约和后续 A/B 激活评估，而不是继续增加同义规则。

后续 Research 可以包括：

- 官方框架与语言实践；
- 成熟开源工程项目；
- 专家工程方法；
- Technology Profile 所需的专项技术研究；
- Verification Profile 与 Targeted Eval 设计依据；
- Runtime / Packaging / Distribution 研究。

新增研究样本不自动意味着扩大 Method 样本，也不自动要求新增 Skill。当前工程能力扩展仍必须受对应有限 Milestone 与 Project Roadmap 约束；Research 不能自行把 Post-v1 候选提升为当前工作。

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

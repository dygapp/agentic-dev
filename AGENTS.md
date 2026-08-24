# AGENTS.md

## 仓库目标

本仓库用于定义一套通用的 AI Agent（以下简称 Agent）驱动软件开发方法，并实现一组小型、可组合的 Skill。

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
7. `docs/project/*`
8. `docs/guides/git-commit-guidelines.md`
9. `docs/research/*`
10. Tasks 与临时工作记录

`docs/project/*` 只定义 `agentic-dev` 仓库自身的项目级治理与运行规则，不得覆盖更高优先级 Method、Architecture 或 Contract Authority，也不得被 Consumer Repository 自动继承。

如果某个 Skill 的设计要求改变方法本身，必须先显式修改方法文档，再修改 Skill。

## 仓库事实来源（Repository Source of Truth）

GitHub 仓库是本仓库唯一的长期基线来源。

规则：

- Git commit 记录项目演进历史；
- Branch 用于隔离实验、设计和实现过程；
- ZIP 快照只用于初始化、离线交换或临时备份，不作为持续开发上下文来源。

所有后续方法（Method）、契约（Contract）和 Skill 实现变更，都应基于 Git 仓库当前状态进行。

## 知识边界与项目自治

当前仓库权威（Repository Authority）决定本项目的事实、规则与约束。

- 会话历史（Conversation History）不构成项目权威；
- 其他会话、其他项目或个人记忆中的规则，不得直接作为本项目事实继续执行；
- 外部项目经验可以作为研究（Research）输入，但只有在当前仓库中按权威层级显式固化后，才能改变本项目的长期规则；
- 项目规则（Project Rule）可以选择、要求或限制某些 Skills 的使用方式；Skill 实现不得覆盖当前仓库权威；
- 新的长期结论应进入合适的 Method、Architecture、Contract、Decision、Guide 或其他项目级权威产物（Artifact），不能只停留在聊天或临时 Plan 中。

复杂、多阶段或跨 Fresh Context 的工作协调遵循 `tasks/README.md`。简单工作不得为了形式完整性创建 Plan。

## 当前阶段

当前处于：

> **Skill Operationalization & Method Validation**

第一批 8 个核心 Skill 的历史 Skill 工程（Skill Engineering）基线已关闭。Issue #18 触发的验收到验证闭环定向强化也已完成评估、复核和人工集成；这没有改变核心 Skill 清单，没有新增独立 `verify-evidence`，也没有弱化 `converge`。

项目演进路线、已完成里程碑、当前证据基线、当前核心目标和下一步工作统一记录在 `docs/project/project-roadmap.md`。新的工作上下文必须先读取该文档，并通过当前 GitHub `master` 验证其中的状态。

现阶段的核心目标是基于已有真实 Consumer Repository 开展继续演进验证。后续只有新的真实使用证据暴露稳定职责缺口时，才重新评估 Method、Contract 或 Skill；不得为了形式完整性新增 Skill、Super-skill 或不必要的流程层级。

## 核心规则

- 阶段是状态，不是文件。
- 规格说明（Specification）描述 WHAT / WHY，不默认包含 HOW。
- 技术规划（Technical Planning）是条件阶段。
- 执行单元（Execution Unit）应纵向、可独立验证、范围明确、可追溯并适合 Fresh Context。
- Conversation History 不作为项目权威知识。
- 使用渐进式披露（Progressive Disclosure），只加载当前工作真正需要的上下文。
- 没有当前证据，不得声明完成。
- 普通、低影响、可逆的实现歧义由 Agent 自主裁决并继续。
- 会改变产品意图、具有破坏性或不可逆性、安全/隐私敏感、改变重大架构方向，或超出 Agent 授权的事项必须升级。
- 不创建接管完整生命周期的超级 Skill。
- 通用方法的终点是 `Ready to Integrate`（已具备进入集成决策的条件）；merge、push、release、deploy 和破坏性 cleanup 由人工权威（Human Authority）或仓库策略（Repository Policy）控制。

## 外部操作治理

当 Agent 具备 GitHub、Repository、Issue、Pull Request、外部 API 或其他会产生外部状态变化的操作能力时，必须遵循：

```text
Analyze
  ↓
Act
  ↓
Verify
  ↓
Report
```

基本要求：

- 外部状态修改前先读取当前状态与权威来源；
- 明确目标、权限和最小必要操作后再执行写操作；
- 写操作完成后重新读取事实来源（Source of Truth）验证目标状态；
- 工具调用成功不等同于目标状态完成；
- 只能汇报已经由当前证据确认的状态。

完整说明见：

`docs/guides/external-operation-guidelines.md`

## AI 复核（AI Review）

本节只约束 `agentic-dev` 仓库自身，不属于通用 Method、Skill Contract 或 Consumer Operating Guide，Consumer Repository 不得自动继承。

对会改变方法（Method）、原则（Principles）、架构（Architecture）、契约（Contract）、核心 Skill 实现（Skill Implementation）、仓库权威（Repository Authority）、`docs/project/*`，或其他会实质改变后续 Agent 行为的高影响变更，在进入最终人工复核（Human Review）或集成决策前必须完成与风险相称的 AI Review。

基本要求：

- 重新读取当前集成目标基线的仓库权威与最终变更状态；采用 PR 时检查 PR 元数据、变更文件与最终 diff / patch，未采用 PR 时检查拟集成 ref 与目标基线之间的等价可验证变更集；
- 根据变更性质检查权威一致性、语义回归、跨层一致性、范围控制、术语规范、人工 / 集成边界与证据一致性等必要维度；
- Review 后如果发生会影响结论的实质修改，必须重新读取最终变更状态，并对受影响维度执行针对性重新复核；
- 只有不存在未解决的 Blocking 或 Medium Finding 时，才可以报告 `AI Review: PASS`；
- 采用 PR 时，最终 AI Review 摘要必须在进入合并决策前记录到 PR 讨论或正式 Review 中，不能只停留在聊天；
- `AI Review: PASS` 不等于 Human Approval，也不授予 Merge 或其他集成权限。

完整说明见：

`docs/project/ai-review-guidelines.md`

## 文档语言与术语表达

当前仓库面向人的说明性文档以中文作为主要叙述语言，同时保留对方法、技术和固定标识有必要的英文术语。

基本要求：

- 中文已有自然稳定表达、且英文需要精确对应时，首次重要出现优先使用“中文（English Term）”；
- 英文本身是固定名称、状态或精确锚点时，可使用“English Term（中文解释）”；
- Skill 名称、代码标识符、文件路径、命令、API 参数等保持原生形式；
- 不要求每次重复中英对照，避免双语注释本身成为阅读噪声；
- 新增内容直接遵守本规范；其他既有文档在实际修改时按触达逐步收敛。

完整说明见：

`docs/guides/terminology-guidelines.md`

## Research 使用规则

`docs/research/` 只保存研究依据和横向比较。

不能因为上游项目或外部规范使用了某个命令、模板、字段或产物，就直接照搬到本仓库。

必须先区分：

- Method / Contract 语义；
- Skill Packaging / Interoperability 约束；
- Runtime / Tool-specific 实现细节。

任何外部来源都不能自动覆盖本仓库的方法权威（Method Authority）；需要改变方法时必须通过显式方法决策（Method Decision）。

## Git Commit

所有提交必须遵循：

`docs/guides/git-commit-guidelines.md`

具体格式、Scope、摘要和分层提交规则只在该规范中维护，提交前应按该规范完成必要检查。

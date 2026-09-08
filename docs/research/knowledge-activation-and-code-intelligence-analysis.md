# 知识激活、规则治理与 Consumer 代码智能研究

研究日期：2026-09-08

研究性质：**Research / Planning Input**

本文保存本轮围绕规则治理、巨型 Guide、知识激活、Obsidian、`colbymchenry/codegraph`、Consumer 代码发现和 Code Review 能力形成的长期研究结论。本文不是规范性权威，不直接改变核心方法、工程纪律、技术画像、Skill 契约或使用方项目规则。当前正式路线与活动里程碑以 `docs/project/project-roadmap.md`、Issue #73 和当前 GitHub 状态为准。

## 1. 问题背景

`agentic-dev` 的早期主要问题是能力不足：需要建立方法、权威边界、验证闭环、可组合 Skill、工程纪律和使用方采用方式。随着这些能力逐步完善，新的主要风险已经发生变化：

> 项目不再主要缺少规则，而是开始面临“规则很多、规则存在，但当前任务未必能精确发现并激活正确规则”的问题。

当前仓库已经比较成熟地解决了：

- Knowledge Storage：长期知识进入 Git Repository；
- Knowledge Organization：Method、Architecture、Engineering Discipline、Technology Profile、Guide、Skill、Project Authority 等分层；
- Knowledge Authority：存在明确权威顺序；
- Knowledge Lifecycle：Research、Candidate、Validated、Integrated 等状态和 Roadmap / Issue / PR 证据已经形成。

相对薄弱的是：

- Knowledge Discovery：当前任务怎样找到真正相关的知识；
- Knowledge Activation：找到后哪些规则应该进入当前活动上下文；
- Context Assembly：如何只组合完成当前任务所需的最小正确上下文；
- Retrieval Evaluation：如何验证检索到的规则既没有漏掉关键规则，也没有装入大量噪声。

因此当前问题不应简单理解为“文档太多”或“缺少新的 Guide”，而应理解为：

> **知识组织已经较成熟，但面向 Agent 执行的知识调度尚未同等成熟。**

## 2. 巨型 Guide 与“超级 Skill 问题转移”

项目演进过程中一直主动避免创建接管完整生命周期的超级 Skill，这一原则仍然正确。但当前仓库出现了另一个结构性风险：一部分原本需要通过“职责拆分 + 精确激活”解决的问题，没有在 Guide / Authority 层同步解决，逐渐形成了较大的综合性 Guide。

截至本研究基线，`docs/guides/` 只有少量文件，但 `using-agentic-dev.md` 与 `external-operation-guidelines.md` 已经承载大量不同触发条件的主题。

典型情况：

- `using-agentic-dev.md` 同时涉及知识边界、需求来源采纳、Consumer Authority、项目初始化、Roadmap、语言选择、项目结构、Skill 使用、Fresh Context、功能工作流、验证与集成等；
- `external-operation-guidelines.md` 同时涉及外部写操作、权限、多仓库边界、人工介入、异步任务、媒体输入、共享资源、租约、临时证据晋升、PR / GitHub 操作等。

单个文件较大本身不是错误。真正的问题是：

```text
一个 Guide
→ 承载多个可以独立触发的规则职责
→ 当前任务只需要其中一部分
→ Agent 为“安全”而读取整份 Guide
→ 活动指令面扩大
→ 真正重要规则显著性下降
```

这与超级 Skill 的典型问题在 Context Engineering 上高度同构：

```text
超级 Skill：一个执行能力承担过多职责
超级 Guide：一个知识容器承载过多独立激活职责
```

因此可以认为：

> 项目过去成功抑制了 Skill Explosion，但部分复杂度可能转移成了 Guide Accumulation。

这不是要求把大 Guide 机械拆成大量小文件。文件数量不是核心指标，真正需要治理的是 **Activation Unit**。

## 3. 规则激活单元

为了描述当前问题，可以使用“规则激活单元”作为研究概念：

> 一个可以由明确任务、风险、产物或状态独立触发，并且可以在不加载整个知识容器的情况下被当前工作消费的最小规则语义单元。

例如，当前任务是 Roadmap / Milestone 状态更新时，可能真正需要的是：

```text
Repository Authority
+ Roadmap lifecycle
+ integration-state closure
```

并不需要同时加载 Consumer 初始化、媒体资源处理、GitHub Actions 单实例租约或 Vue 技术规则。

这说明仓库的“存储架构”和“执行检索架构”不是同一个问题。

未来更合理的上下文加载模型可以研究为三层：

### 3.1 Always-on Kernel

只保留所有任务都必须知道的少量不变量，例如：

- Repository Authority；
- Knowledge Boundary；
- Current Evidence；
- Human / Integration Boundary；
- Progressive Disclosure。

Kernel 应保持非常薄，避免因为“重要”就把所有规则提升为 Always-on。

### 3.2 Task Capability Context

根据当前任务加载，例如：

- `execute-unit`；
- `systematic-debug`；
- `technical-plan`；
- `github-actions-verification`；
- 后续可能的 `code-review`。

它回答“当前职责如何工作”。

### 3.3 Conditional Rule Context

根据任务中实际出现的风险、技术或产物条件加载，例如：

```text
Roadmap 变化
→ integration-state closure

共享 Review Environment
→ singleton ownership / lease

媒体输入
→ content type validation

Vue watcher
→ watcher lifecycle / cleanup

Gradle source set / artifact boundary
→ 当前 Gradle 配置 + 必要技术验证知识
```

这一层才是真正的 Progressive Disclosure。

## 4. Rule Activation 优先于 Rule Addition

历史上常见的演进模式是：

```text
Consumer Failure
→ 增加规则
→ 增加 Guide / Skill / Eval
→ 同步多个入口
```

在规则稀缺阶段有明显价值，但随着能力成熟，继续默认采用这种模式会产生治理复利成本。

未来应优先采用：

```text
发现问题
→ 判断是否已有相关规则
    ├─ 已有：检查发现 / 激活 / 冲突 / 上下文噪声
    │          → 优先修 Activation
    └─ 没有：再判断是否值得新增最小规则
```

可以进一步区分以下失效类型：

1. 规则从未进入当前 Context：Authority Discovery / Activation Failure；
2. 相似或冲突规则同时存在：Selection / Conflict Failure；
3. 活动规则过多：Instruction Density / Attention Degradation；
4. 陈旧或重复状态进入上下文：Misleading Context；
5. 现有规则确实无法覆盖：真正的 Rule Gap。

只有第 5 类问题天然指向新增规则。

最近项目状态闭环问题已经提供了一个重要现实信号：某些长期边界并非不存在，而是没有在正确评审 / 集成任务中可靠激活。该类证据应优先解释为 Activation / Discoverability 问题，而不是再次补写同义规则。

## 5. 外部模型使用经验对当前问题的支持

本轮研究还参考了当前模型提示实践。OpenAI 当前模型指导强调：迁移到新模型时应从尽量小、足以保留产品契约的 Prompt 基线开始；避免机械继承旧 Prompt Stack；把工具专项指导放入工具描述，只把真正跨工具的政策放入系统级指令；对于判断型行为优先使用决策规则，而不是不必要的 `ALWAYS` / `NEVER`；复杂 Prompt 也应保持各部分简短，只在会改变行为时增加细节。

这与当前 `agentic-dev` 的主要风险方向一致：

> Context 容量增加不等于同时激活大量规则的可靠性线性增加。规则治理应优化“最小正确活动指令面”，而不是以“全部规则都可见”为默认安全策略。

该外部证据只支持研究方向，不直接定义 `agentic-dev` 的规则结构。

## 6. Obsidian 的适用边界

Obsidian 对当前问题有价值，但不能被误认为完整的 Agent Rule Activation 解决方案。

当前官方能力包括：

- Backlinks：查看引用当前 Note 的其他 Note；
- Graph View：以 Note 为 Node、Internal Link 为 Edge 可视化关系；
- Properties：在 Markdown 顶部使用结构化属性，并支持检索；
- Bases：基于属性组织和过滤 Note。

因此 Obsidian 很适合作为：

> **人类知识治理 / 浏览 / 可视化 Workbench。**

例如可以帮助人工发现：

- 哪个规则被多少文档引用；
- 哪些规则成为 orphan；
- 哪个 stage / trigger / consumer 下存在多少规则；
- 是否存在重复 Note / Link；
- 某个 Skill / Guide 与哪些长期知识有关。

但 Obsidian 默认 Graph 的关系主要是 Note Link，本身通常不能表达足够精确的机器语义：

```text
triggered_by
applies_to
consumed_by
requires
overrides
supersedes
conflicts_with
verifies
```

因此：

- Obsidian 不应成为新的 Repository Authority；
- Git Repository 继续保存 Markdown、Metadata 与长期事实；
- Obsidian 最多作为这些文件的 Projection / Workbench；
- `.obsidian/` 是否版本化属于工具配置问题，不应先于真实治理需求决定；
- 即使使用 Obsidian，也仍需要独立的 Agent Retrieval / Activation 机制。

## 7. CodeGraph 研究基线

研究项目：`colbymchenry/codegraph`

核验日期：2026-09-08

核验时当前 `main` Head：`8df9ecac9ddf49925a6e80c32a89ec91e601ab23`

主要核验入口：

- `README.md`；
- `site/src/content/docs/getting-started/introduction.md`；
- `site/src/content/docs/core-concepts/knowledge-graph.md`；
- `site/src/content/docs/reference/mcp-server.md`；
- `src/mcp/server-instructions.ts`；
- `src/installer/instructions-template.ts`；
- `src/installer/targets/codex.ts`；
- `.claude/skills/agent-eval/SKILL.md`；
- CodeGraph language verification / retrieval eval 相关材料。

CodeGraph 是本地优先的代码智能工具：使用 AST / tree-sitter 提取代码符号、关系和文件信息，保存到本地 SQLite 知识图谱，并通过 MCP、CLI 和库接口提供给 Agent。

它解决的核心问题是：

> Agent 不应每次通过 `grep` / `glob` / `Read` 从头重建代码结构，而应取得精确、已经预计算的结构化上下文。

这与 `agentic-dev` 当前规则问题在结构上高度相似：

```text
CodeGraph：大型代码库中，当前任务到底应该读哪些代码？
agentic-dev：大型规则库中，当前任务到底应该激活哪些规则？
```

内容不同，但“发现最小正确上下文”的问题同型。

## 8. CodeGraph 最值得借鉴的设计经验

### 8.1 预索引稳定结构，而不是每次重新推理

CodeGraph 提前保存：

- Node：file、module、class、function、method、route、component 等；
- Edge：contains、calls、imports、extends、implements、references、instantiates、overrides 等；
- File / source location。

对 `agentic-dev` 的启发不是“必须上 Graph DB”，而是：稳定的 Rule Relationship 不应要求每个 Fresh Context 重新从长文档推导。

### 8.2 关系需要有类型

CodeGraph 不只保存 `A → B`，而区分不同 Edge Kind。

规则系统如果最终需要结构化关系，也应能够区分“引用”和真正具有执行语义的关系，例如 trigger / consumer / override / supersede，而不能只依赖普通 Markdown Link。

这也是为什么 Obsidian 默认 Graph 适合治理浏览，却不天然等同于 Rule Activation Engine。

### 8.3 默认一个强入口，而不是暴露大量细粒度工具

CodeGraph 当前虽然存在 search、callers、callees、impact、files、status 等能力，但 MCP 默认只暴露一个 `codegraph_explore`。

项目明确记录：实测 Agent 行为显示，一个强入口比一组窄工具更容易让 Agent 直接取得正确上下文，减少错误工具选择。

对 `agentic-dev` 的启发是：

> 未来即使建立规则检索能力，也不应先暴露几十个 `roadmap-rules`、`verification-rules`、`technology-rules` 工具让 Agent 自己选，而应优先研究一个强的 Knowledge / Rule Explore 入口。

### 8.4 返回“组装好的上下文”，而不是文件列表

`codegraph_explore` 返回相关源码、调用路径、关系和 blast radius，而不是只告诉 Agent“去读文件 A / B / C”。

规则检索如果只返回：

```text
using-agentic-dev.md
external-operation-guidelines.md
```

问题仍然存在。

更有价值的目标是返回：

```text
Applicable Authority
+ Activated Rules
+ Required Checks
+ Source / Section References
```

### 8.5 Always-on Instructions 必须保持很小

CodeGraph 的服务器说明源码明确要求常驻指令保持紧凑，因为 Agent 每个 Session 都会读取，过长会消耗 Context；安装器写入 AGENTS / CLAUDE 等文件的提示也故意保持很短。

这是对当前“巨型 Guide + 粗粒度激活”问题最直接的工程参考之一。

### 8.6 Freshness / Staleness 是一等公民

CodeGraph 对索引与文件之间的 drift 有显式 stale handling：索引陈旧时只要求对受影响文件回退直接读取，其他未标记部分仍可继续消费。

如果 `agentic-dev` 后续建立 Rule Index，也必须保留：

- source file / section；
- source commit 或等价 identity；
- index version；
- stale / rebuild policy。

Index 只能是派生导航能力，不能成为新的权威来源。

### 8.7 Retrieval 本身需要 Eval

CodeGraph 的评估关注真实任务：子系统理解、跨文件数据流、符号定位、caller / callee、impact radius，以及返回结果是否真的足够让 LLM 正确完成任务。

它还明确检查：

- 返回过少可能是漏检；
- 返回过多无关节点可能是噪声；
- Process Success 不能自动等于 Semantic Success。

这非常适合迁移为 `agentic-dev` 的 Rule Retrieval Eval 设计原则。

## 9. 不应照搬 CodeGraph 的部分

CodeGraph 的多数代码关系可以从 AST 确定性推导；规则关系通常不能。

例如：

```text
Roadmap change
→ triggers
integration-state closure
```

这类关系具有治理语义，不能仅依赖 LLM 自动阅读 Markdown 后猜测。

因此未来若需要结构化规则索引，更可能采用：

> **显式 Rule Metadata + 自动派生 Index**

而不是：

> LLM 自动把全部文档推断成一个权威知识图谱。

同时，本研究不支持现在直接创建：

- Rule Graph Database；
- 新 MCP Server；
- 新 Runtime Adapter；
- Marketplace / Plugin Bundle；
- 大规模 YAML Schema。

这些都必须由最小 Retrieval Prototype 与 Eval 证明需要后再判断。

## 10. Consumer 问题比 agentic-dev 自身更重要

知识激活问题不能只从 `agentic-dev` 自己如何读取规则考虑。

真实 Consumer 同时存在至少两类关键知识：

```text
Requirements / Authority / Project Rules
→ 应该怎样工作？

Source Code / Dependency / Runtime Structure
→ 代码现在怎样工作？
```

第一类需要 `agentic-dev` 继续研究 Rule / Authority Activation。

第二类没有必要由 `agentic-dev` 自己再造代码知识图谱。成熟的 Code Intelligence 工具可以直接承担源码发现职责。

推荐的职责分离研究模型：

```text
Consumer Repository
├─ Requirements / Authority
│    → agentic-dev 方法 + Rule Activation
└─ Source Code
     → CodeGraph / 等价 Code Intelligence
              ↓
             Agent
       Execute / Debug / Review
              ↓
      Compiler / Tests / Runtime
```

## 11. CodeGraph 对 Consumer 的正确采用方式

需要特别纠正一个容易产生的误解：

> 普通 Consumer 不应该复制 CodeGraph 仓库中的 `.claude/skills/add-lang`、`agent-eval` 等内部 Skill 作为自身代码管理 Skill。

这些 Skill 主要服务于 CodeGraph 项目自身的语言支持建设和 Agent A/B 评估。

CodeGraph 真正面向普通 Consumer 的主要交付是：

- `.codegraph/` 本地派生索引；
- `codegraph_explore` MCP 工具；
- 等价 `codegraph explore` CLI；
- 自动同步 / stale handling；
- 极薄的 Agent 激活说明。

CodeGraph 当前明确支持 Codex CLI 的本地集成：

- 项目级 `.codex/config.toml` 可写入 `[mcp_servers.codegraph]`；
- Repository `AGENTS.md` 只追加一个很短、带条件的 CodeGraph 提示；
- 只有仓库存在 `.codegraph/` 时才优先使用 CodeGraph，没有索引时应完全跳过；
- `.codegraph/` 是派生数据并整体被忽略，不构成 Repository Authority。

这一模式与 `agentic-dev` 希望实现的“小入口 → 强检索 → Surgical Context”高度一致。

## 12. Consumer 中最适合优先消费 CodeGraph 的职责

### 12.1 execute-unit

在已有 `.codegraph/` 的 Consumer 中，进入实现前可以优先通过 CodeGraph 建立最小相关源码上下文，再形成 JIT Plan，而不是机械扫描整个仓库。

### 12.2 systematic-debug

Debug 常需要跨 Controller / Service / Repository / Component / API 追踪路径。结构化调用关系可以降低“先花大量 Context 找路径”的成本，但运行时根因仍必须由实际复现、日志、测试和代码证据验证。

### 12.3 Code Review

Code Review 可能是最有价值的消费场景之一：

```text
Diff / Changed Symbol
→ callers / callees / impact / related source
→ Rule Activation
→ Review Findings
```

CodeGraph 可以帮助 Reviewer理解 blast radius、依赖方向和相关调用路径，但不能判断业务意图是否正确，也不能替代 Compiler / Tests / Runtime Verification。

## 13. CodeGraph 的边界

CodeGraph 应定位为：

> **Structural Code Intelligence / Context Retrieval**

而不是完整代码管理系统。

它不能替代：

- Git；
- PR / Repository Authority；
- Specification / Architecture Authority；
- Compiler；
- Unit / Integration / E2E Tests；
- Lint / Type Check；
- Runtime Verification；
- Security / correctness-specific tooling；
- Code Review 本身。

同时，Gradle、配置文件、文档、工作流等不一定都能通过源码 AST 图正确覆盖。涉及：

- `build.gradle.kts`；
- `settings.gradle.kts`；
- `application.yml`；
- Dockerfile；
- GitHub Actions；
- Flyway 配置；
- 架构文档；

仍需按当前 Repository 实际读取和验证。

所以真实 Gradle / Spring 边界问题往往应组合：

```text
CodeGraph
→ Java / Kotlin 源码依赖与结构
+
Repository Config Read
→ Gradle source set / artifact / dependency reality
+
Compiler / Build / Tests
→ correctness evidence
```

## 14. ChatGPT + GitHub 与本地 Codex 的现实边界

当前使用方常见协作环境包括：

```text
ChatGPT + GitHub Connector
Local Codex CLI
```

本地 `.codegraph/` SQLite / MCP 可以直接服务 Codex CLI、Claude Code、Cursor 等本地 Agent，但 ChatGPT 云端 + GitHub Connector 不能直接读取 Consumer 本地 `.codegraph/`。

因此短期合理分工可以是：

```text
ChatGPT + GitHub
→ Requirements / Authority / Planning / Governance / Repository Review

Local Codex + CodeGraph
→ Code Exploration / Implementation / Debug / Local Code Review
```

这不是永久架构约束，但属于当前可观察运行环境边界，不能在 Research 中假装两者已经统一。

## 15. Technology Profile 的方向调整

本轮讨论进一步削弱了“因为技术重要，就提前建设大型技术 Profile”的必要性。

现代高能力模型通常已经具备较强框架知识，并且在需要当前版本事实时可以查询官方资料。因此 Technology Knowledge 的优先方向应从：

> Generation Guidance —— 教模型怎么写框架代码

逐步转向：

> Defect Detection / Verification Knowledge —— 明确哪些地方不能只相信模型记忆、哪些风险必须检查、哪些事实必须从当前 Repository / 官方资料重新确认。

当前建议：

- 已有 Vue 3 + TypeScript Profile 保留，不机械扩张；
- Spring 有较高 Review Eval 价值，尤其事务、代理、生命周期、安全、配置与测试语义，但不因此立即启动新 Profile；
- Gradle 有较高 Review Eval 价值，尤其 source set、dependency scope、artifact / task graph 和 application boundary；Issue #71 / AR-04 已提供真实架构风险证据，但不因此立即创建大型 Gradle Profile；
- Element Plus 的通用长期知识价值相对较低，优先依赖 Consumer design system / wrappers / current docs。

WI-06 应继续等待 Code Review / Consumer Eval 证明哪些技术知识确实是“模型 + Repository + 当前官方资料”仍无法稳定补足的增量缺口。

## 16. Code Review 能力重新评估

Code Review 并不是新出现的想法。当前 Skill Architecture 历史上已经把代码复核保留为工程纪律 / 内嵌职责候选，第一批 8 个核心 Skill 没有将 `code-review` 独立 Skill 化；逻辑上仍保留“规格符合性”和“工程质量”两个审查维度。

当前证据已经明显增强了 WI-07 重新评估 `code-review` 的理由：

- 有独立输入：项目 Authority、Spec / Plan / Architecture、Diff、当前源码、验证证据；
- 有稳定职责：独立审查，不负责实现完整生命周期；
- 有独立输出：高信噪比 Findings 或无阻塞结论；
- 有明确退出：审查完成、证据不足、需要升级或发现阻塞；
- 可以复用于 PR、分支、Local Diff、Consumer 集成前复核；
- 可以设计专项 Eval；
- Issue #71 的独立 Fresh Context 架构评审已经证明“独立 Reviewer”对高返工问题具有现实价值。

但必须保持以下边界：

### 16.1 不成为新的通用 Method Stage

Code Review 应按风险、Repository Policy 或人工请求调用，不要求所有微小任务机械经过一个新 Stage。

### 16.2 不成为超级 Skill

Code Review 不应预加载全部 Method、Guide、Engineering Discipline、Technology Profile 和 Consumer 文档。

更合理的是：

```text
Diff / Task
→ 风险分类
→ 最小 Authority + Rule Activation
→ 必要代码结构发现
→ Review
```

### 16.3 与独立 Planning Review 分开

Issue #71 / AR-04 还支持“高返工 Technical Planning 的独立 Fresh Context Review”价值，但它与 Code Review 不是同一个职责。

不得把 Planning Review、Architecture Review、Code Review、Security Review 全部合并成一个“Review Everything”超级 Skill。

### 16.4 Review v1 应少而强

优先检查：

- Specification compliance；
- 明确缺陷 / 回归；
- 数据、状态、并发、生命周期风险；
- Boundary / Dependency / Side-effect 风险；
- 不必要复杂度和推测性抽象；
- Diff Scope；
- Verification Evidence；
- 当前上下文触发的技术高风险误用。

默认不把命名、个人风格、轻微格式、无证据的未来扩展性、设计模式偏好作为高价值 Finding。

## 17. AI 友好代码的更准确目标

“AI 驱动开发应倾向更低耦合、更少复杂度、更清晰边界”的方向成立，但不应机械变成：

- 所有类必须很小；
- 所有模块必须拆碎；
- 禁止所有经典设计模式；
- 抽象越少越好。

更准确的目标是：

> **Safe Change Reasoning Surface 应尽量小。**

一个职责内聚的 300 行模块，可能比 `Controller → Handler → Facade → Manager → Strategy → Factory → Adapter → Provider` 更容易理解和安全修改。

Review 可以优先观察：

- Change locality；
- Dependency direction；
- State ownership；
- Explicit side effects；
- Abstraction justification；
- Indirection cost；
- Contract clarity；
- Test seam。

现有“实现最小化与推测性复杂度控制”和“精准修改与差异范围控制”已经覆盖部分问题，因此当前不应仅凭这次讨论立刻增加第四工程纪律。可以先把“结构可推理性 / Context Radius / Change Locality”作为 Code Review Eval 维度，只有稳定跨场景证据出现后再评估是否需要新 Discipline。

经典设计模式也应按当前总推理成本判断，而不是按模式身份判断：

- Strategy 在真实存在多个变体时可能降低复杂度；只有假想未来变体时可能增加复杂度；
- Adapter 在真实外部契约差异时可能隔离风险；如果所有内部调用都机械包装一层，可能只是增加间接性。

## 18. CodeGraph Consumer Adoption 的验证建议

如果要判断 CodeGraph 是否值得进入 Consumer 常规开发环境，应做有界 A/B，而不是因为外部项目宣称更少 Tool Call 就直接采用。

建议选择真实 Consumer 历史任务，覆盖：

1. 找业务功能实现入口；
2. Controller → Service → Repository 数据流；
3. Vue 页面 → composable → API；
4. 找某个状态 / 方法的调用者；
5. 公共能力修改的影响范围；
6. 受影响测试发现；
7. 跨层 Debug；
8. 多文件 Diff Code Review。

比较：

```text
A：当前 Agent + Read / Grep / Find
B：同模型 + CodeGraph
```

优先指标：

- 正确入口发现率；
- 关键相关文件漏检；
- 无关文件 / Context Noise；
- Read / Grep 调用次数；
- Context Token；
- 完成时间；
- 最终修改 / 判断正确性；
- Review 真缺陷发现；
- blast radius 误判。

CodeGraph 自身公开 Benchmark 可以作为外部参考，但不能直接推导 Consumer 会获得同样收益。

## 19. 可能的长期知识激活模型

如果 Rule Activation Audit 与 Eval 证明结构化索引确有增益，一个可能的最小模型是：

```yaml
id: integration-state-closure
authority: docs/guides/using-agentic-dev.md
applies_to:
  - roadmap
  - milestone
  - current-state
trigger:
  - integration-candidate
  - roadmap-change
consumed_by:
  - ai-review
  - converge
risk:
  - stale-state
strength: required
```

这只是研究示例，不是当前 Schema Authority。

未来架构可以抽象为：

```text
Git Repository
唯一 Repository Authority
    │
    ├─ Markdown Rules
    └─ Explicit Metadata
            ↓
       Derived Knowledge Index
            │
      ┌─────┴─────┐
      ↓           ↓
   Obsidian     Agent Explore
人工治理界面       ↓
             Surgical Rule Context
```

关键原则：

- Authority 与 Index 分离；
- Index 可重建；
- Rule 只定义一次；
- Skill 负责职责，不复制所有知识；
- Retrieval 负责“取得什么”，而不是把全部规则塞进 Skill；
- Runtime 工具是否需要后续再由 Eval 决定。

## 20. 当前路线建议

本轮研究最终收敛出的优先顺序：

```text
规则治理与知识激活 v1
        ↓
验证 Task / Risk → Rule Activation
        ↓
WI-07 — Code Review Capability v1
        ↓
Consumer Code Review / CodeGraph 辅助 A/B
        ↓
由真实 Review 缺口决定是否启动 WI-06
```

其中：

### 第一方向：规则治理与知识激活

优先处理：

- 巨型 Guide Activation Audit；
- Always-on Kernel 收敛；
- Rule duplication / conflict / supersession；
- Task / Risk → Rule Mapping；
- Minimal Retrieval Prototype；
- Historical Failure Retrieval Eval；
- Consumer Fresh Context 验证；
- “先修 Activation，后增 Rule”的治理路径。

### 第二方向：Code Review Capability v1

作为 WI-07 的优先候选，但不与第一里程碑混合实施。

重点：

- 独立高信噪比 Reviewer；
- Risk-triggered，而非强制新 Stage；
- Context-controlled / Fresh Context；
- Rule Activation 驱动；
- Consumer Code Intelligence 可选辅助；
- Framework-specific knowledge 由 Review Eval 决定是否值得长期持久化。

## 21. 当前明确非结论

本文不支持以下结论：

- “Guide 大于某个 KB 就必须拆”；
- “所有规则必须变成独立文件”；
- “所有 Rule 都需要 YAML Metadata”；
- “必须采用 Obsidian”；
- “必须开发 Rule Graph”；
- “必须开发 `knowledge_explore` MCP”；
- “CodeGraph 必须成为所有 Consumer 依赖”；
- “CodeGraph 可以替代 Compiler / Tests / Review”；
- “需要立刻新增 Spring / Gradle / Element Plus Profile”；
- “需要立刻新增第四 Engineering Discipline”；
- “Code Review 必须成为核心方法新阶段”；
- “Planning Review 与 Code Review 应合并”；
- “AI 驱动开发意味着禁用传统设计模式”。

这些都必须由后续有限里程碑中的实际审计、Prototype、Runtime Eval 和 Consumer Evidence 决定。

## 22. Fresh Context 恢复摘要

后续新的 Fresh Context 如果需要恢复本研究，应至少保留以下判断：

1. 当前主要风险已经从“规则稀缺”转向“规则发现与激活可靠性”；
2. 巨型 Guide 可能成为文档型超级能力，但治理单位应是 Activation Unit，而不是文件大小；
3. 先判断 Rule Gap 还是 Activation Failure，再决定是否新增规则；
4. Obsidian 适合人类知识治理 Projection，不是 Repository Authority，也不是完整 Activation Engine；
5. CodeGraph 最值得借鉴的是 typed relationships、surgical context、single strong entry、tight always-on instructions、freshness 和 retrieval eval；
6. `agentic-dev` 不应现在照搬 CodeGraph 架构或建立新 Graph / MCP 层；
7. Consumer 源码发现可以直接实验采用 CodeGraph，本地索引只是派生上下文，不是项目事实；
8. Consumer 不应复制 CodeGraph 内部开发 Skills，主要消费其 MCP / CLI / local index；
9. CodeGraph 对 `execute-unit`、`systematic-debug`、未来 `code-review` 最有潜在价值；
10. Technology Profile 应从“教模型生成”转向“缺陷检测 / 必须验证的增量知识”，WI-06 暂缓；
11. Code Review 已具备 WI-07 重新评估条件，但必须与 Planning Review 分离，并避免成为超级 Skill；
12. AI 友好代码的目标是缩小 Safe Change Reasoning Surface，而不是机械追求类 / 文件更小；
13. 推荐路线是先完成规则治理与知识激活，再推进 Code Review，然后由 Review / Consumer Evidence 决定是否需要新的技术画像。

## 23. 研究来源

### agentic-dev 当前仓库

- `AGENTS.md`
- `docs/architecture/engineering-capability-architecture.md`
- `docs/architecture/skill-architecture.md`
- `docs/architecture/skill-contracts.md`
- `docs/architecture/engineering-disciplines.md`
- `docs/architecture/technology-profile-contract.md`
- `docs/technology-profiles/vue3-typescript.md`
- `docs/guides/using-agentic-dev.md`
- `docs/guides/external-operation-guidelines.md`
- `docs/project/project-roadmap.md`
- Issue #58
- Issue #71

### CodeGraph

- https://github.com/colbymchenry/codegraph
- https://github.com/colbymchenry/codegraph/blob/main/site/src/content/docs/getting-started/introduction.md
- https://github.com/colbymchenry/codegraph/blob/main/site/src/content/docs/core-concepts/knowledge-graph.md
- https://github.com/colbymchenry/codegraph/blob/main/site/src/content/docs/reference/mcp-server.md
- https://github.com/colbymchenry/codegraph/blob/main/src/mcp/server-instructions.ts
- https://github.com/colbymchenry/codegraph/blob/main/src/installer/instructions-template.ts
- https://github.com/colbymchenry/codegraph/blob/main/src/installer/targets/codex.ts

### Obsidian 官方资料

- https://obsidian.md/help/plugins/graph
- https://obsidian.md/help/plugins/backlinks
- https://obsidian.md/help/properties
- https://obsidian.md/help/bases

### OpenAI 当前模型指导

- https://developers.openai.com/api/docs/guides/latest-model

外部来源只能作为研究证据。任何改变当前 `agentic-dev` 长期行为的结论仍必须进入对应 Repository Authority，并完成当前项目要求的验证和集成。
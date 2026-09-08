# 知识激活、规则治理与使用方代码智能研究

研究日期：2026-09-08

研究性质：**研究 / 规划输入**

本文保存本轮围绕规则治理、大型指南、知识激活、Obsidian、`colbymchenry/codegraph`、使用方代码发现和代码复核能力形成的长期研究结论。本文不是规范性权威，不直接改变核心方法、工程纪律、技术画像、技能契约或使用方项目规则。当前正式路线与活动里程碑以 `docs/project/project-roadmap.md`、Issue #73 和当前 GitHub 状态为准。

## 1. 问题背景

`agentic-dev` 的早期主要问题是能力不足：需要建立方法、权威边界、验证闭环、可组合技能、工程纪律和使用方采用方式。随着这些能力逐步完善，新的主要风险已经发生变化：

> 项目不再主要缺少规则，而是开始面临“规则很多、规则存在，但当前任务未必能精确发现并激活正确规则”的问题。

当前仓库已经比较成熟地解决了：

- **知识存储**：长期知识进入 Git 仓库；
- **知识组织**：方法、架构、工程纪律、技术画像、指南、技能、项目权威等分层；
- **知识权威**：存在明确权威顺序；
- **知识生命周期**：研究、候选、已验证、已集成等状态和项目路线图 / Issue / PR 证据已经形成。

相对薄弱的是：

- **知识发现**：当前任务怎样找到真正相关的知识；
- **知识激活**：找到后哪些规则应该进入当前活动上下文；
- **上下文组装**：如何只组合完成当前任务所需的最小正确上下文；
- **检索评估**：如何验证检索到的规则既没有漏掉关键规则，也没有装入大量噪声。

因此当前问题不应简单理解为“文档太多”或“缺少新的指南”，而应理解为：

> **知识组织已经较成熟，但面向 Agent 执行的知识调度尚未同等成熟。**

## 2. 大型指南与“超级技能问题转移”

项目演进过程中一直主动避免创建接管完整生命周期的超级技能，这一原则仍然正确。但当前仓库出现了另一个结构性风险：一部分原本需要通过“职责拆分 + 精确激活”解决的问题，没有在指南 / 权威层同步解决，逐渐形成了较大的综合性指南。

截至本研究基线，`docs/guides/` 只有少量文件，但 `using-agentic-dev.md` 与 `external-operation-guidelines.md` 已经承载大量不同触发条件的主题。

典型情况：

- `using-agentic-dev.md` 同时涉及知识边界、需求来源采纳、使用方权威、项目初始化、项目路线图、语言选择、项目结构、技能使用、新上下文、功能工作流、验证与集成等；
- `external-operation-guidelines.md` 同时涉及外部写操作、权限、多仓库边界、人工介入、异步任务、媒体输入、共享资源、租约、临时证据晋升、PR / GitHub 操作等。

单个文件较大本身不是错误。真正的问题是：

```text
一个指南
→ 承载多个可以独立触发的规则职责
→ 当前任务只需要其中一部分
→ Agent 为“安全”而读取整份指南
→ 活动指令面扩大
→ 真正重要规则显著性下降
```

这与超级技能的典型问题在上下文工程上高度同构：

```text
超级技能：一个执行能力承担过多职责
超级指南：一个知识容器承载过多独立激活职责
```

因此可以认为：

> 项目过去成功抑制了技能膨胀，但部分复杂度可能转移成了指南累积。

这不是要求把大指南机械拆成大量小文件。文件数量不是核心指标，真正需要治理的是**激活单元**。

## 3. 规则激活单元

为了描述当前问题，可以使用“规则激活单元”作为研究概念：

> 一个可以由明确任务、风险、产物或状态独立触发，并且可以在不加载整个知识容器的情况下被当前工作消费的最小规则语义单元。

例如，当前任务是项目路线图 / 里程碑状态更新时，可能真正需要的是：

```text
仓库权威
+ 路线图生命周期
+ 集成状态闭环
```

并不需要同时加载使用方初始化、媒体资源处理、GitHub Actions 单实例租约或 Vue 技术规则。

这说明仓库的“存储架构”和“执行检索架构”不是同一个问题。

未来更合理的上下文加载模型可以研究为三层：

### 3.1 常驻核心规则

只保留所有任务都必须知道的少量不变量，例如：

- 仓库权威；
- 知识边界；
- 当前证据；
- 人工 / 集成边界；
- 渐进式披露。

常驻核心规则应保持非常薄，避免因为“重要”就把所有规则提升为常驻内容。

### 3.2 任务能力上下文

根据当前任务加载，例如：

- `execute-unit`；
- `systematic-debug`；
- `technical-plan`；
- `github-actions-verification`；
- 后续可能的 `code-review`。

它回答“当前职责如何工作”。

### 3.3 条件规则上下文

根据任务中实际出现的风险、技术或产物条件加载，例如：

```text
项目路线图变化
→ 集成状态闭环

共享评审环境
→ 单实例所有权 / 租约

媒体输入
→ 内容类型验证

Vue watcher
→ watcher 生命周期 / 清理

Gradle source set / artifact 边界
→ 当前 Gradle 配置 + 必要技术验证知识
```

这一层才是真正的渐进式披露。

## 4. 规则激活优先于新增规则

历史上常见的演进模式是：

```text
使用方失效
→ 增加规则
→ 增加指南 / 技能 / 评估
→ 同步多个入口
```

在规则稀缺阶段有明显价值，但随着能力成熟，继续默认采用这种模式会产生治理复利成本。

未来应优先采用：

```text
发现问题
→ 判断是否已有相关规则
    ├─ 已有：检查发现 / 激活 / 冲突 / 上下文噪声
    │          → 优先修复激活
    └─ 没有：再判断是否值得新增最小规则
```

可以进一步区分以下失效类型：

1. 规则从未进入当前上下文：权威发现 / 激活失败；
2. 相似或冲突规则同时存在：选择 / 冲突失败；
3. 活动规则过多：指令密度 / 注意力退化；
4. 陈旧或重复状态进入上下文：误导上下文；
5. 现有规则确实无法覆盖：真正的规则缺口。

只有第 5 类问题天然指向新增规则。

最近项目状态闭环问题已经提供了一个重要现实信号：某些长期边界并非不存在，而是没有在正确复核 / 集成任务中可靠激活。该类证据应优先解释为激活 / 可发现性问题，而不是再次补写同义规则。

## 5. 外部模型使用经验对当前问题的支持

本轮研究还参考了当前模型提示实践。OpenAI 当前模型指导强调：迁移到新模型时应从尽量小、足以保留产品契约的提示基线开始；避免机械继承旧提示栈；把工具专项指导放入工具描述，只把真正跨工具的政策放入系统级指令；对于判断型行为优先使用决策规则，而不是不必要的 `ALWAYS` / `NEVER`；复杂提示也应保持各部分简短，只在会改变行为时增加细节。

这与当前 `agentic-dev` 的主要风险方向一致：

> 上下文容量增加不等于同时激活大量规则的可靠性线性增加。规则治理应优化“最小正确活动指令面”，而不是以“全部规则都可见”为默认安全策略。

该外部证据只支持研究方向，不直接定义 `agentic-dev` 的规则结构。

## 6. Obsidian 的适用边界

Obsidian 对当前问题有价值，但不能被误认为完整的 Agent 规则激活解决方案。

当前官方能力包括：

- Backlinks：查看引用当前 Note 的其他 Note；
- Graph View：以 Note 为 Node、Internal Link 为 Edge 可视化关系；
- Properties：在 Markdown 顶部使用结构化属性，并支持检索；
- Bases：基于属性组织和过滤 Note。

因此 Obsidian 很适合作为：

> **人类知识治理 / 浏览 / 可视化工作台。**

例如可以帮助人工发现：

- 哪个规则被多少文档引用；
- 哪些规则成为孤立节点；
- 某个阶段 / 触发条件 / 消费者下存在多少规则；
- 是否存在重复 Note / Link；
- 某个技能 / 指南与哪些长期知识有关。

但 Obsidian 默认 Graph 的关系主要是 Note Link，本身通常不能表达足够精确的机器语义，例如：

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

- Obsidian 不应成为新的仓库权威；
- Git 仓库继续保存 Markdown、元数据与长期事实；
- Obsidian 最多作为这些文件的投影视图 / 工作台；
- `.obsidian/` 是否版本化属于工具配置问题，不应先于真实治理需求决定；
- 即使使用 Obsidian，也仍需要独立的 Agent 检索 / 激活机制。

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
- CodeGraph 语言验证 / 检索评估相关材料。

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

- 节点：file、module、class、function、method、route、component 等；
- 边：contains、calls、imports、extends、implements、references、instantiates、overrides 等；
- 文件 / 源码位置。

对 `agentic-dev` 的启发不是“必须上图数据库”，而是：稳定的规则关系不应要求每个新上下文重新从长文档推导。

### 8.2 关系需要有类型

CodeGraph 不只保存 `A → B`，而区分不同边类型。

规则系统如果最终需要结构化关系，也应能够区分“引用”和真正具有执行语义的关系，例如触发、消费、覆盖、取代，而不能只依赖普通 Markdown Link。

这也是为什么 Obsidian 默认 Graph 适合治理浏览，却不天然等同于规则激活引擎。

### 8.3 默认一个强入口，而不是暴露大量细粒度工具

CodeGraph 当前虽然存在 search、callers、callees、impact、files、status 等能力，但 MCP 默认只暴露一个 `codegraph_explore`。

项目明确记录：实测 Agent 行为显示，一个强入口比一组窄工具更容易让 Agent 直接取得正确上下文，减少错误工具选择。

对 `agentic-dev` 的启发是：

> 未来即使建立规则检索能力，也不应先暴露几十个细粒度规则工具让 Agent 自己选，而应优先研究一个强的知识 / 规则探索入口。

### 8.4 返回“组装好的上下文”，而不是文件列表

`codegraph_explore` 返回相关源码、调用路径、关系和影响范围，而不是只告诉 Agent“去读文件 A / B / C”。

规则检索如果只返回：

```text
using-agentic-dev.md
external-operation-guidelines.md
```

问题仍然存在。

更有价值的目标是返回：

```text
适用权威
+ 已激活规则
+ 必需检查
+ 来源 / 段落引用
```

### 8.5 常驻指令必须保持很小

CodeGraph 的服务器说明源码明确要求常驻指令保持紧凑，因为 Agent 每个会话都会读取，过长会消耗上下文；安装器写入 AGENTS / CLAUDE 等文件的提示也故意保持很短。

这是对当前“大型指南 + 粗粒度激活”问题最直接的工程参考之一。

### 8.6 新鲜度 / 陈旧状态是一等公民

CodeGraph 对索引与文件之间的漂移有显式陈旧处理：索引陈旧时只要求对受影响文件回退直接读取，其他未标记部分仍可继续消费。

如果 `agentic-dev` 后续建立规则索引，也必须保留：

- 来源文件 / 段落；
- 来源提交或等价身份；
- 索引版本；
- 陈旧 / 重建策略。

索引只能是派生导航能力，不能成为新的权威来源。

### 8.7 检索本身需要评估

CodeGraph 的评估关注真实任务：子系统理解、跨文件数据流、符号定位、调用者 / 被调用者、影响范围，以及返回结果是否真的足够让 LLM 正确完成任务。

它还明确检查：

- 返回过少可能是漏检；
- 返回过多无关节点可能是噪声；
- 进程成功不能自动等于语义成功。

这非常适合迁移为 `agentic-dev` 的规则检索评估设计原则。

## 9. 不应照搬 CodeGraph 的部分

CodeGraph 的多数代码关系可以从 AST 确定性推导；规则关系通常不能。

例如：

```text
项目路线图变化
→ 触发
集成状态闭环
```

这类关系具有治理语义，不能仅依赖 LLM 自动阅读 Markdown 后猜测。

因此未来若需要结构化规则索引，更可能采用：

> **显式规则元数据 + 自动派生索引**

而不是：

> LLM 自动把全部文档推断成一个权威知识图谱。

同时，本研究不支持现在直接创建：

- 规则图数据库；
- 新 MCP Server；
- 新运行时适配器；
- Marketplace / Plugin Bundle；
- 大规模 YAML Schema。

这些都必须由最小检索原型与评估证明需要后再判断。

## 10. 使用方问题比 agentic-dev 自身更重要

知识激活问题不能只从 `agentic-dev` 自己如何读取规则考虑。

真实使用方同时存在至少两类关键知识：

```text
需求 / 权威 / 项目规则
→ 应该怎样工作？

源码 / 依赖 / 运行时结构
→ 代码现在怎样工作？
```

第一类需要 `agentic-dev` 继续研究规则 / 权威激活。

第二类没有必要由 `agentic-dev` 自己再造代码知识图谱。成熟的代码智能工具可以直接承担源码发现职责。

推荐的职责分离研究模型：

```text
使用方仓库
├─ 需求 / 权威
│    → agentic-dev 方法 + 规则激活
└─ 源码
     → CodeGraph / 等价代码智能
              ↓
             Agent
       执行 / 调试 / 复核
              ↓
      编译器 / 测试 / 运行时
```

## 11. CodeGraph 对使用方的正确采用方式

需要特别纠正一个容易产生的误解：

> 普通使用方不应该复制 CodeGraph 仓库中的 `.claude/skills/add-lang`、`agent-eval` 等内部技能作为自身代码管理技能。

这些技能主要服务于 CodeGraph 项目自身的语言支持建设和 Agent A/B 评估。

CodeGraph 真正面向普通使用方的主要交付是：

- `.codegraph/` 本地派生索引；
- `codegraph_explore` MCP 工具；
- 等价 `codegraph explore` CLI；
- 自动同步 / 陈旧处理；
- 极薄的 Agent 激活说明。

CodeGraph 当前明确支持 Codex CLI 的本地集成：

- 项目级 `.codex/config.toml` 可写入 `[mcp_servers.codegraph]`；
- 仓库 `AGENTS.md` 只追加一个很短、带条件的 CodeGraph 提示；
- 只有仓库存在 `.codegraph/` 时才优先使用 CodeGraph，没有索引时应完全跳过；
- `.codegraph/` 是派生数据并整体被忽略，不构成仓库权威。

这一模式与 `agentic-dev` 希望实现的“小入口 → 强检索 → 精确上下文”高度一致。

## 12. 使用方中最适合优先消费 CodeGraph 的职责

### 12.1 `execute-unit`

在已有 `.codegraph/` 的使用方中，进入实现前可以优先通过 CodeGraph 建立最小相关源码上下文，再形成即时计划，而不是机械扫描整个仓库。

### 12.2 `systematic-debug`

调试常需要跨 Controller / Service / Repository / Component / API 追踪路径。结构化调用关系可以降低“先花大量上下文找路径”的成本，但运行时根因仍必须由实际复现、日志、测试和代码证据验证。

### 12.3 代码复核

代码复核可能是最有价值的消费场景之一：

```text
差异 / 变更符号
→ 调用者 / 被调用者 / 影响范围 / 相关源码
→ 规则激活
→ 复核发现
```

CodeGraph 可以帮助复核者理解影响范围、依赖方向和相关调用路径，但不能判断业务意图是否正确，也不能替代编译器 / 测试 / 运行时验证。

## 13. CodeGraph 的边界

CodeGraph 应定位为：

> **结构化代码智能 / 上下文检索。**

而不是完整代码管理系统。

它不能替代：

- Git；
- PR / 仓库权威；
- 规格说明 / 架构权威；
- 编译器；
- 单元 / 集成 / E2E 测试；
- Lint / Type Check；
- 运行时验证；
- 安全 / 正确性专项工具；
- 代码复核本身。

同时，Gradle、配置文件、文档、工作流等不一定都能通过源码 AST 图正确覆盖。涉及：

- `build.gradle.kts`；
- `settings.gradle.kts`；
- `application.yml`；
- Dockerfile；
- GitHub Actions；
- Flyway 配置；
- 架构文档；

仍需按当前仓库实际读取和验证。

所以真实 Gradle / Spring 边界问题往往应组合：

```text
CodeGraph
→ Java / Kotlin 源码依赖与结构
+
仓库配置读取
→ Gradle source set / artifact / dependency 现实
+
编译 / 构建 / 测试
→ 正确性证据
```

## 14. ChatGPT + GitHub 与本地 Codex 的现实边界

当前使用方常见协作环境包括：

```text
ChatGPT + GitHub Connector
Local Codex CLI
```

本地 `.codegraph/` SQLite / MCP 可以直接服务 Codex CLI、Claude Code、Cursor 等本地 Agent，但 ChatGPT 云端 + GitHub Connector 不能直接读取使用方本地 `.codegraph/`。

因此短期合理分工可以是：

```text
ChatGPT + GitHub
→ 需求 / 权威 / 规划 / 治理 / 仓库复核

Local Codex + CodeGraph
→ 代码探索 / 实现 / 调试 / 本地代码复核
```

这不是永久架构约束，但属于当前可观察运行环境边界，不能在研究中假装两者已经统一。

## 15. 技术画像的方向调整

本轮讨论进一步削弱了“因为技术重要，就提前建设大型技术画像”的必要性。

现代高能力模型通常已经具备较强框架知识，并且在需要当前版本事实时可以查询官方资料。因此技术知识的优先方向应从：

> 生成指导 —— 教模型怎么写框架代码

逐步转向：

> 缺陷检测 / 验证知识 —— 明确哪些地方不能只相信模型记忆、哪些风险必须检查、哪些事实必须从当前仓库 / 官方资料重新确认。

当前建议：

- 已有 Vue 3 + TypeScript 技术画像保留，不机械扩张；
- Spring 有较高代码复核评估价值，尤其事务、代理、生命周期、安全、配置与测试语义，但不因此立即启动新技术画像；
- Gradle 有较高代码复核评估价值，尤其 source set、dependency scope、artifact / task graph 和 application boundary；Issue #71 / AR-04 已提供真实架构风险证据，但不因此立即创建大型 Gradle 技术画像；
- Element Plus 的通用长期知识价值相对较低，优先依赖使用方 design system / wrappers / current docs。

WI-06 应继续等待代码复核 / 使用方评估证明哪些技术知识确实是“模型 + 仓库 + 当前官方资料”仍无法稳定补足的增量缺口。

## 16. 代码复核能力重新评估

代码复核并不是新出现的想法。当前技能架构历史上已经把代码复核保留为工程纪律 / 内嵌职责候选，第一批 8 个核心技能没有将 `code-review` 独立技能化；逻辑上仍保留“规格符合性”和“工程质量”两个审查维度。

当前证据已经明显增强了 WI-07 重新评估 `code-review` 的理由：

- 有独立输入：项目权威、规格说明 / 技术计划 / 架构、差异、当前源码、验证证据；
- 有稳定职责：独立审查，不负责实现完整生命周期；
- 有独立输出：高信噪比问题发现或无阻塞结论；
- 有明确退出：审查完成、证据不足、需要升级或发现阻塞；
- 可以复用于 PR、分支、本地差异、使用方集成前复核；
- 可以设计专项评估；
- Issue #71 的独立新上下文架构评审已经证明“独立复核者”对高返工问题具有现实价值。

### 16.1 不成为新的通用方法阶段

代码复核应按风险、仓库策略或人工请求调用，不要求所有微小任务机械经过一个新阶段。

### 16.2 不成为超级技能

代码复核不应预加载全部方法、指南、工程纪律、技术画像和使用方文档。

更合理的是：

```text
差异 / 任务
→ 风险分类
→ 最小权威 + 规则激活
→ 必要代码结构发现
→ 复核
```

### 16.3 与独立规划复核分开

Issue #71 / AR-04 还支持“高返工技术规划的独立新上下文复核”价值，但它与代码复核不是同一个职责。

不得把规划复核、架构复核、代码复核、安全复核全部合并成一个“复核一切”的超级技能。

### 16.4 代码复核 v1 应少而强

优先检查：

- 规格符合性；
- 明确缺陷 / 回归；
- 数据、状态、并发、生命周期风险；
- 边界 / 依赖 / 副作用风险；
- 不必要复杂度和推测性抽象；
- 差异范围；
- 验证证据；
- 当前上下文触发的技术高风险误用。

默认不把命名、个人风格、轻微格式、无证据的未来扩展性、设计模式偏好作为高价值问题发现。

## 17. AI 友好代码的更准确目标

“AI 驱动开发应倾向更低耦合、更少复杂度、更清晰边界”的方向成立，但不应机械变成：

- 所有类必须很小；
- 所有模块必须拆碎；
- 禁止所有经典设计模式；
- 抽象越少越好。

更准确的目标是：

> **安全变更推理面应尽量小。**

一个职责内聚的 300 行模块，可能比 `Controller → Handler → Facade → Manager → Strategy → Factory → Adapter → Provider` 更容易理解和安全修改。

复核可以优先观察：

- 变更局部性；
- 依赖方向；
- 状态所有权；
- 显式副作用；
- 抽象必要性；
- 间接层成本；
- 契约清晰度；
- 测试接缝。

现有“实现最小化与推测性复杂度控制”和“精准修改与差异范围控制”已经覆盖部分问题，因此当前不应仅凭这次讨论立刻增加第四工程纪律。可以先把“结构可推理性 / 上下文半径 / 变更局部性”作为代码复核评估维度，只有稳定跨场景证据出现后再评估是否需要新工程纪律。

经典设计模式也应按当前总推理成本判断，而不是按模式身份判断：

- Strategy 在真实存在多个变体时可能降低复杂度；只有假想未来变体时可能增加复杂度；
- Adapter 在真实外部契约差异时可能隔离风险；如果所有内部调用都机械包装一层，可能只是增加间接性。

## 18. CodeGraph 使用方采用的验证建议

如果要判断 CodeGraph 是否值得进入使用方常规开发环境，应做有界 A/B，而不是因为外部项目宣称更少工具调用就直接采用。

建议选择真实使用方历史任务，覆盖：

1. 找业务功能实现入口；
2. Controller → Service → Repository 数据流；
3. Vue 页面 → composable → API；
4. 找某个状态 / 方法的调用者；
5. 公共能力修改的影响范围；
6. 受影响测试发现；
7. 跨层调试；
8. 多文件差异代码复核。

比较：

```text
A：当前 Agent + Read / Grep / Find
B：同模型 + CodeGraph
```

优先指标：

- 正确入口发现率；
- 关键相关文件漏检；
- 无关文件 / 上下文噪声；
- Read / Grep 调用次数；
- 上下文令牌；
- 完成时间；
- 最终修改 / 判断正确性；
- 代码复核真实缺陷发现；
- 影响范围误判。

CodeGraph 自身公开基准测试可以作为外部参考，但不能直接推导使用方会获得同样收益。

## 19. 可能的长期知识激活模型

如果规则激活审计与评估证明结构化索引确有增益，一个可能的最小模型是：

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

这只是研究示例，不是当前 Schema 权威。

未来架构可以抽象为：

```text
Git 仓库
唯一仓库权威
    │
    ├─ Markdown 规则
    └─ 显式元数据
            ↓
       派生知识索引
            │
      ┌─────┴─────┐
      ↓           ↓
   Obsidian     Agent 探索
人工治理界面       ↓
             精确规则上下文
```

关键原则：

- 权威与索引分离；
- 索引可重建；
- 规则只定义一次；
- 技能负责职责，不复制所有知识；
- 检索负责“取得什么”，而不是把全部规则塞进技能；
- 是否需要运行时工具后续再由评估决定。

## 20. 当前路线建议

本轮研究最终收敛出的优先顺序：

```text
规则治理与知识激活 v1
        ↓
验证“任务 / 风险 → 规则激活”
        ↓
WI-07 — 代码复核能力 v1
        ↓
使用方代码复核 / CodeGraph 辅助 A/B
        ↓
由真实复核缺口决定是否启动 WI-06
```

### 第一方向：规则治理与知识激活

优先处理：

- 大型指南激活审计；
- 常驻核心规则收敛；
- 规则重复 / 冲突 / 取代；
- 任务 / 风险 → 规则映射；
- 最小检索原型；
- 历史失效检索评估；
- 使用方新上下文验证；
- “先修激活，后增规则”的治理路径。

### 第二方向：代码复核能力 v1

作为 WI-07 的优先候选，但不与第一里程碑混合实施。

重点：

- 独立高信噪比复核者；
- 按风险触发，而非强制新阶段；
- 严格控制上下文 / 使用新上下文；
- 规则激活驱动；
- 使用方代码智能可选辅助；
- 框架专项知识由复核评估决定是否值得长期持久化。

## 21. 当前明确非结论

本文不支持以下结论：

- “指南大于某个 KB 就必须拆”；
- “所有规则必须变成独立文件”；
- “所有规则都需要 YAML 元数据”；
- “必须采用 Obsidian”；
- “必须开发规则图”；
- “必须开发 `knowledge_explore` MCP”；
- “CodeGraph 必须成为所有使用方依赖”；
- “CodeGraph 可以替代编译器 / 测试 / 复核”；
- “需要立刻新增 Spring / Gradle / Element Plus 技术画像”；
- “需要立刻新增第四工程纪律”；
- “代码复核必须成为核心方法新阶段”；
- “规划复核与代码复核应合并”；
- “AI 驱动开发意味着禁用传统设计模式”。

这些都必须由后续有限里程碑中的实际审计、原型、运行时评估和使用方证据决定。

## 22. 新上下文恢复摘要

后续新的上下文如果需要恢复本研究，应至少保留以下判断：

1. 当前主要风险已经从“规则稀缺”转向“规则发现与激活可靠性”；
2. 大型指南可能成为文档型超级能力，但治理单位应是激活单元，而不是文件大小；
3. 先判断规则缺口还是激活失败，再决定是否新增规则；
4. Obsidian 适合人类知识治理投影视图，不是仓库权威，也不是完整激活引擎；
5. CodeGraph 最值得借鉴的是有类型关系、精确上下文、单一强入口、紧凑常驻指令、陈旧处理和检索评估；
6. `agentic-dev` 不应现在照搬 CodeGraph 架构或建立新图 / MCP 层；
7. 使用方源码发现可以直接实验采用 CodeGraph，本地索引只是派生上下文，不是项目事实；
8. 使用方不应复制 CodeGraph 内部开发技能，主要消费其 MCP / CLI / 本地索引；
9. CodeGraph 对 `execute-unit`、`systematic-debug`、未来 `code-review` 最有潜在价值；
10. 技术画像应从“教模型生成”转向“缺陷检测 / 必须验证的增量知识”，WI-06 暂缓；
11. 代码复核已具备 WI-07 重新评估条件，但必须与规划复核分离，并避免成为超级技能；
12. AI 友好代码的目标是缩小安全变更推理面，而不是机械追求类 / 文件更小；
13. 推荐路线是先完成规则治理与知识激活，再推进代码复核，然后由复核 / 使用方证据决定是否需要新的技术画像。

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

外部来源只能作为研究证据。任何改变当前 `agentic-dev` 长期行为的结论仍必须进入对应仓库权威，并完成当前项目要求的验证和集成。
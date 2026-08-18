# 使用 agentic-dev

本文说明一个 AI Agent 或开发者如何把 `agentic-dev` 作为方法与 Skills 知识源，用于启动并持续推进一个真实软件项目。

本文是 Operating Guide，不重新定义 Method、Architecture 或 Skill Contract。发生冲突时，以目标项目自己的 Repository Authority 与 `agentic-dev` 的权威层级为准。

## 1. 使用模型

`agentic-dev` 提供三类可复用资产：

- **Method**：软件开发过程中的阶段、边界、证据和上下文原则；
- **Skills**：执行特定职责的可组合能力；
- **Operating Guide**：说明如何在真实项目中使用 Method 与 Skills。

目标项目仍然拥有自己的 Project Rules、Requirements、Architecture、Code、Tests 与 Integration Policy。

```text
agentic-dev
Method + Skills + Operating Guide
        │
        │ reusable guidance
        ▼
Consumer Repository
Project Rules + Project Knowledge + Code
```

`agentic-dev` 不替目标项目预定义完整目录、技术栈、文档体系或治理结构。

## 2. 开始前的知识边界

启动一个项目时，Agent 应先明确当前允许使用的权威输入。

至少区分：

1. `agentic-dev` Repository：提供可复用 Method、Skills 与 Operating Guide；
2. Consumer Repository：提供并逐步形成当前项目自己的 Authority；
3. 当前明确提供的业务 / 产品需求来源；
4. 当前 Runtime 可直接观察到的能力和状态。

不得把以下内容直接当作目标项目事实：

- 其他聊天中的未固化结论；
- 其他项目的规则；
- 个人记忆或隐含经验；
- `agentic-dev` 中只属于该仓库自己的 Project Rule。

`agentic-dev` 可以指导“如何工作”，但不能替 Consumer Repository 决定“这个项目的事实是什么”。

## 3. Greenfield Project：建立最小启动骨架

新项目不应从大而全的模板开始。

目标是先建立**足以让 Fresh Agent 正确继续工作的最小 Repository Authority**，然后随真实需求逐步演进。

通常需要先明确：

- 项目目标与当前范围；
- Repository Authority / Knowledge Boundary；
- 当前允许 Agent 自主处理与必须升级给 Human 的边界；
- 基本 Verification 与 Integration Policy；
- 当前 Requirement / Specification 应保存在哪里；
- 当前实际需要使用的 Skills。

一个小型 Greenfield 项目的初始骨架可以很轻，例如：

```text
<consumer>/
├── AGENTS.md
├── README.md
└── <当前真正需要的项目 Artifact>
```

这只是最小示例，不是固定模板。

不要为了“看起来完整”预先创建空的：

- architecture 体系；
- decisions 体系；
- tasks / plans 体系；
- 大量阶段目录；
- 未被当前工作需要的配置或 Skills。

当真实工作产生长期价值时再新增相应 Artifact。

例如：

- 出现需要跨 Execution Units 长期协调的 HOW，再持久化 Technical Plan；
- 出现值得长期解释的架构决定，再建立适当的 Decision / Architecture Artifact；
- 工作复杂到需要跨 Fresh Context 协调时，再建立临时 Plan / Coordination Artifact；
- 进入实现阶段后，再按实际技术栈创建源码、测试与构建结构。

原则是：**Project Structure follows durable need.**

## 4. 使用 Skills

第一批核心 Skills 位于：

```text
skills/
├── clarify-intent/
├── specify/
├── technical-plan/
├── slice-work/
├── readiness-check/
├── execute-unit/
├── systematic-debug/
└── converge/
```

Agent 应根据当前 Runtime 支持的方式读取、安装或暴露所需 Skills。

本文不规定固定的 Distribution / Installation 机制。只要求：

- 使用来自已确认 `agentic-dev` baseline 的 Skill；
- 不依赖历史测试残留或陈旧复制；
- 不因为 Runtime 安装方式不同而改变 Skill Contract；
- Consumer Repository 的 Authority 始终高于可复用 Skill 对项目事实的推测。

不要求所有 Skills 在每个工作中都出现。

## 5. 常规 Feature 工作流

### 5.1 先判断 Intent 是否需要澄清

如果 Goal、Scope、User-visible Behavior、Business Boundary 或 Acceptance 存在会实质改变产品结果的歧义，使用：

```text
clarify-intent
```

如果现有权威已经足够明确，不为了流程完整性制造额外澄清。

### 5.2 形成最小充分 Specification

使用：

```text
specify
```

Specification 负责 WHAT / WHY，应让 Fresh Agent 能判断：

- 要做什么；
- 不做什么；
- 什么结果表示完成；
- 是否仍存在关键 Product Ambiguity。

Specification 不要求固定文件名、目录、Markdown 模板或 YAML Front Matter。

### 5.3 只在需要时创建 Technical Plan

如果存在需要跨 Execution Units 长期协调的 HOW 决策，使用：

```text
technical-plan
```

如果 HOW 可以安全地在单个 Execution Unit 中通过 JIT Plan 解决，则不要为了阶段完整性创建永久 Technical Plan。

### 5.4 切分并检查 Execution Units

使用：

```text
slice-work
→ readiness-check
```

Execution Unit 应：

- 范围明确；
- 可独立验证；
- 尽量纵向完成一个有意义的行为结果；
- 适合在 Fresh Execution Context 中执行；
- 不依赖前一个 Worker 未持久化的 Conversation Reasoning。

### 5.5 每个 Unit 使用 Fresh Execution Context

使用：

```text
execute-unit
```

每个 Fresh Execution Context 只执行一个唯一 Current Unit。

Worker 只加载：

- 当前 Unit；
- 必要的 Consumer Repository Authority；
- 必要的 Specification / Technical Plan；
- 当前 Verification 所需上下文。

不要把前一个 Worker 的完整聊天历史当作下一个 Worker 的依赖。

遇到非预期失败并需要系统诊断时，可使用：

```text
systematic-debug
```

### 5.6 整体收敛

所有当前范围内的 Units 完成后使用：

```text
converge
```

只有当前 Intent、Specification、Implementation 与 Verification Evidence 一致，且不存在 Blocking Gap，才能达到：

```text
Ready to Integrate
```

Merge / Push / Release / Deploy 仍由 Consumer Repository 的 Human Authority 或 Repository Policy 决定。

## 6. 项目如何持续演进

Consumer Repository 应随着真实工作逐步丰富，而不是在初始化时一次设计完成。

可以新增：

- 新的 Project Rules；
- Domain / Requirement Artifacts；
- Architecture / Decision Artifacts；
- Coordination Artifacts；
- 当前项目真正需要的其他 Skills；
- Verification / Integration 规则。

每次新增前都应问：

> 这项内容是否具有当前项目真实、持续的协调或权威价值？

如果没有，就不要仅为了形式完整性持久化。

Project Rule 可以选择、要求或限制 Skills，但 Skill 不得覆盖 Project Authority。

## 7. 中断、恢复与 Fresh Context

Conversation History 不是长期项目状态。

工作中断或切换 Context 时，应依赖 Consumer Repository 中已经持久化的：

- Project Rules；
- 当前 Specification / Technical Plan（如存在）；
- Current Unit / Coordination State；
- Verification Evidence；
- 必要的代码与配置。

新的 Agent Context 应从这些 Artifact 恢复工作，而不是要求提供完整旧聊天。

Fresh Context 是逻辑隔离，不要求某一种特定 Runtime 形式。可以是新 Chat、新 Codex session、isolated worker 或其他能够避免依赖未持久化历史 reasoning 的执行环境。

## 8. Experimental Use：向 agentic-dev 回传实践证据

普通 Consumer Project **不要求**向 `agentic-dev` 提交反馈。

只有当当前工作被明确标记为 `agentic-dev` Experiment / Validation 时，才启用本节规则。

### 8.1 实验隔离

实验应尽量使用独立 Fresh Context，并只把以下内容作为 Consumer Authority / Execution Input：

- 指定的 `agentic-dev` Repository baseline；
- 明确的 Consumer 需求来源；
- Consumer Repository；
- 当前 Runtime 可直接观察到的能力和状态。

即使 Runtime 可能暴露其他会话、个人记忆或历史上下文，也不得把这些内容作为 Consumer 项目事实、规则或需求依据。需要使用的事实必须能回溯到当前 Consumer Authority。

### 8.2 GitHub Issue 作为首选反馈通道

实验期间，使用 `agentic-dev` Repository 的 GitHub Issue 作为首选 Experiment Feedback Channel。

Issue 是：

- Evidence 传输通道；
- 跨 Repository / Context 的跟踪入口；
- 后续 `agentic-dev` 分析的输入。

Issue **不是**：

- Consumer Repository 的项目知识库；
- `agentic-dev` Method / Contract Authority；
- 自动成立的方法结论。

如果当前 Runtime 具有 GitHub Issue 写权限，应直接通过 GitHub API / Connector 提交或追加反馈。

如果没有写权限，不得阻塞 Consumer 开发；生成符合以下格式的 Issue Body / Comment，待具备权限后提交即可。

### 8.3 一个实验使用一个 Tracking Issue

默认一个 Consumer Experiment 对应一个 Tracking Issue，不为每个小问题创建独立 Issue。

为了在不依赖 GitHub Issue Template 的情况下保持首轮反馈可检索、可比较，Tracking Issue 使用以下标题约定：

```text
[experiment] <consumer> - <experiment goal>
```

Issue Body 至少包含：

```text
Experiment:
Consumer Repository:
Consumer Baseline / Branch:
agentic-dev Baseline:
Runtime / Model:
Goal:
Scope:
```

其中无法获得的字段应明确写 `Unknown / Not available`，不要静默省略。

开发过程中只在出现有意义的新证据时追加 Comment：

```text
Observed Friction / Finding:
Context / Stage / Skill:
Evidence Reference:
Human Intervention:
Classification Candidate:
- Usage Guide
- Skill Implementation
- Contract
- Method
- Project Rule
- Runtime
- Unknown
```

如果某条 Finding 没有可引用的代码、Commit、PR、命令结果或其他 Current Evidence，应明确说明证据限制，不把推测写成已确认缺口。

不要提交：

- 完整 Conversation；
- 完整 private reasoning；
- 每次 Skill 调用流水；
- Consumer Repository 已经存在的整份项目文档副本；
- 没有实际影响的普通实现噪音。

### 8.4 实验结束

在同一 Tracking Issue 中追加 Final Summary：

```text
Final State:
Skills Actually Used:
Key Findings:
Human Interventions:
Consumer Evidence References:
Recommended Follow-up:
```

Consumer Agent 可以提出 Classification Candidate，但不能自行把实验观察提升为 `agentic-dev` 的 Method / Contract 结论。

最终是否修改 `agentic-dev`，应回到新的 `agentic-dev` Context，重新读取：

- 当前 `agentic-dev` Authority；
- Experiment Issue；
- Issue 引用的 Consumer Evidence。

再按证据分类处理。

## 9. 推荐启动方式

一个 Greenfield Consumer Experiment 的启动指令应保持很薄。

只需要明确：

- 要创建什么真实项目；
- `agentic-dev` Repository 在哪里；
- 权威需求在哪里；
- Consumer Repository 在哪里；
- 当前工作是否属于 Experiment。

然后让 Agent 自行读取本文和相关 Skills 开始工作。

如果仍必须依赖大量未写入 `agentic-dev` 的口头步骤才能启动项目，应把这种情况记录为 Operating Guide / Method 使用证据，而不是用额外聊天指令悄悄补齐。

## 10. 使用目标

`agentic-dev` 的目标不是提前规定项目最终长什么样，而是让 AI 能够：

1. 从最小、明确的 Repository Authority 开始；
2. 根据真实需求逐步建立项目知识与结构；
3. 在需要时选择合适的 Skills；
4. 用 Fresh Context 和 Current Evidence 推进实现；
5. 在项目演进过程中只持久化真正有长期价值的知识；
6. 最终基于整体证据达到 Ready to Integrate。

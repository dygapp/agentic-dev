# 规则治理与知识激活 v1

## 状态

**当前活动有限里程碑 / Planning 已启动**

人工决策日期：2026-09-08

跟踪入口：Issue #73

启动基线：

`master@0895ca30f76c666f3a0d4d9c2f9af6f14cded5d6`

实施分支：

`docs/rule-governance-knowledge-activation-v1`

长期阶段保持：

> **工程能力扩展与方法演进**

本里程碑不启动 WI-06、WI-07、WI-09、第四工程纪律或其他候选能力的实现。WI-07 — Code Review Capability v1 被明确登记为本里程碑完成后的优先后继方向，但不会因为本里程碑启动而自动进入 Execute。

## 1. 决策背景

项目已经从早期“能力不足”逐步进入“能力存在但激活可靠性不足”的阶段。

当前仓库已经具有较成熟的：

- Repository Authority；
- Method / Architecture / Engineering Discipline / Technology Profile / Guide / Skill 分层；
- Fresh Context 与 Progressive Disclosure 原则；
- Current Evidence 与集成状态闭环；
- 多轮 Consumer Evidence；
- 运行时评估与人工语义评分机制。

但真实演进中出现了新的结构性风险：

1. `using-agentic-dev.md`、`external-operation-guidelines.md` 等较大 Guide 已包含多个可以独立触发的长期职责；
2. 为避免超级 Skill 而保留在 Guide 中的规则，如果仍以整份 Guide 为激活单位，会形成“文档型超级能力”；
3. 新问题出现后继续默认“补一条规则 / 补一个 Guide 段落”，会扩大活动指令面和重复规则；
4. 已经出现“规则存在，但没有在正确任务路径中可靠激活”的现实信号；
5. 高能力模型本身已经具备大量通用技术知识，继续扩大百科式技术指导的边际价值下降；
6. Consumer 真实开发还存在源码发现成本，应该区分“规则激活”和“代码结构发现”，后者可以优先使用成熟 Code Intelligence 工具而不是由 `agentic-dev` 自己再造。

因此人工权威选择“规则治理与知识激活 v1”作为下一有限里程碑。

完整研究依据：

`docs/research/knowledge-activation-and-code-intelligence-analysis.md`

## 2. 核心目标

本里程碑只解决一个有限问题：

> **让当前任务能够以更小、更准确、可验证的活动上下文发现并激活正确规则，同时抑制 Guide、重复规则和长期 Context Surface 的继续膨胀。**

具体目标：

1. 对当前高影响 Guide 和跨层规则执行 Activation Audit；
2. 识别真实的规则激活单元，而不是以文件大小或目录结构作为治理单位；
3. 区分 Always-on Kernel、Task Capability Context、Conditional Rule Context；
4. 冻结一个最小 `Task / Risk → Rule Set` 检索模型；
5. 使用真实历史失效场景验证 Retrieval / Activation，而不是只检查文档结构；
6. 基于 Eval 证据决定哪些 Guide 应拆分、哪些只需要 section-level pointer、哪些规则应删除 / 合并 / supersede、哪些必须留在 Always-on；
7. 至少在一个 Consumer Fresh Context 中验证新的激活方式；
8. 建立“先判断 Activation Failure，再决定是否新增 Rule”的长期治理路径。

## 3. 关键设计原则

### 3.1 治理对象是 Activation Unit，不是文件大小

大文件不自动等于错误，小文件也不自动等于可发现。

不得设定“超过某个 KB 就拆分”之类机械规则。所有结构调整必须能够说明：

- 该语义由什么触发；
- 谁消费；
- 是否需要独立加载；
- 是否与其他规则重复 / 冲突；
- 是否能通过 Retrieval Eval 观察到改善。

### 3.2 Always-on 必须保持薄

只有真正跨任务成立的不变量才可以进入 Always-on Kernel。

“重要”不等于“每次都加载”。

### 3.3 Skill 不拥有全部知识

Skill 负责稳定任务职责与流程边界；条件性知识继续存在于合适的长期 Authority 中，通过指针或检索按需进入当前 Context。

不得为了修 Guide 激活问题，把所有 Guide 内容重新复制到 Skill。

### 3.4 Authority 与 Index 分离

如果后续出现 Rule Metadata / Index / Query Prototype：

- Git Repository 中的规范性文档继续是 Authority；
- Index 必须可重建；
- Index 必须可检测 stale；
- Index 不得成为第二事实来源；
- 同一规则不得因为方便检索而在多个 Authority 中复制全文。

### 3.5 Retrieval 必须可评估

评估对象不是“索引能运行”，而是：

> 当前任务得到的规则集合是否足够正确完成任务，并且没有大量无关规则干扰。

## 4. 当前研究输入

### 4.1 仓库内证据

重点读取：

- `AGENTS.md`；
- `docs/guides/using-agentic-dev.md`；
- `docs/guides/external-operation-guidelines.md`；
- `docs/architecture/skill-architecture.md`；
- `docs/architecture/skill-contracts.md`；
- `docs/architecture/engineering-disciplines.md`；
- `docs/architecture/technology-profile-contract.md`；
- `docs/technology-profiles/vue3-typescript.md`；
- Issue #58；
- Issue #71；
- 最近与集成状态闭环、候选 / Execution Unit 身份、验证触发、Fresh Context 恢复有关的历史评估和 PR 证据。

### 4.2 外部研究

- OpenAI 当前模型 Prompt / Tool guidance；
- Obsidian Graph / Backlinks / Properties / Bases；
- `colbymchenry/codegraph` 当前实现与 Agent 集成；
- CodeGraph Retrieval / Agent A/B Eval 设计。

外部研究不能自动覆盖本仓库 Authority。

## 5. 分阶段实施路线

### Phase A — Activation Audit

目标：把当前“文档很多”问题转换为可观察的激活单元问题。

至少完成：

1. 枚举 `using-agentic-dev.md` 的可独立触发规则单元；
2. 枚举 `external-operation-guidelines.md` 的可独立触发规则单元；
3. 对每个单元记录：
   - Authority source / section；
   - Trigger；
   - Consumer；
   - Strength；
   - Related Skill / Stage；
   - Duplicate / overlap / conflict / supersession；
   - Historical failure or positive evidence；
4. 检查 AGENTS / README / Skill / Guide / Project docs 是否重复表达同一长期行为；
5. 形成 Always-on Kernel 候选，但不在 Audit 阶段立即修改全部入口。

Phase A 完成门禁：

- 至少两个巨型 Guide 已完成可审查的 Activation Map；
- 能明确区分“规则缺失”和“规则已存在但未激活”的历史场景；
- 不以“把 Guide 拆小”作为默认结论。

### Phase B — Minimal Retrieval Model

目标：冻结最小、工具无关的检索语义。

至少回答：

- Task / Risk / Artifact / Stage 中哪些字段真正有辨识力；
- Rule 如何声明 Trigger / Consumer / Authority Pointer；
- 是否需要显式 Priority / Strength / Supersession；
- 如何防止 Index 漂移；
- 如何在无 Index 时可靠回退到 Repository 直接读取。

允许的最小原型：

- Markdown section index；
- YAML / JSON rule index；
- 小型查询脚本；
- 其他可重建派生结构。

不要求：Graph DB、MCP、Obsidian Plugin、Marketplace、Runtime Adapter。

Phase B 完成门禁：

- 能从有限 Task Context 返回可解释的最小 Rule Set；
- 每条结果可追溯到唯一 Authority source；
- Index 删除后可以从 Repository 恢复，不损失 Authority。

### Phase C — Retrieval / Activation Eval

目标：证明检索模式能改善 Agent 行为，而不是只改善文档观感。

必须包含真实历史场景，优先覆盖：

- Roadmap / Milestone 集成后状态闭环；
- Planning Candidate 与 Execution Unit 身份边界；
- Verification trigger / readiness fallback / re-entry；
- External operation asynchronous closure；
- Consumer Fresh Context authority discovery；
- 其他能证明“规则存在但激活失败”的已知实例。

至少比较：

```text
A：现有完整 / 粗粒度规则加载
B：缩减 Kernel + Task / Risk 条件检索
```

观察：

- 必须规则 Recall；
- 无关规则数量 / Precision；
- Context Token；
- Tool / File Reads；
- 行为语义正确性；
- 是否出现误停 / 误升级 / 误执行；
- 是否产生双重权威或陈旧状态。

Process exit 0 不等于 Semantic PASS。必须人工语义评分。

### Phase D — Authority / Guide Convergence

只有 Phase C 证明收益后，才实施长期结构收敛。

可能动作包括：

- 缩减 Always-on AGENTS 内容；
- 为 Guide 建立稳定 section pointer；
- 拆分真正独立的 Activation Unit；
- 合并重复规则；
- 删除陈旧 / 被 supersede 的规则；
- 修正 Skill activation pointer；
- 建立最小 Rule Metadata / Index；
- 明确 Rule Deletion / Supersession lifecycle。

不能预先承诺必须执行所有动作。

### Phase E — Consumer Validation

至少选择一个真实 Consumer 做 Fresh Context 验证。

验证重点：

- 新上下文能否从 Consumer Repository Authority + `agentic-dev` 需要的最小基线恢复当前规则；
- 是否减少机械全量读取 Guide；
- 是否仍能命中关键规则；
- Consumer-local Authority 是否继续高于 `agentic-dev` 可复用规则；
- 是否避免把 `agentic-dev` 项目级规则误带入 Consumer。

CodeGraph 可以作为源码发现的独立 A/B 输入，但不是本阶段必须依赖。

### Phase F — Final Review & Integration

完成：

- 静态一致性检查；
- 必要的隔离运行时回归；
- 人工语义评分；
- 最终 AI 复核；
- Roadmap / AGENTS / README / project record 状态闭环；
- 人工集成决策。

## 6. 非目标

本里程碑不做：

- Code Review Skill 实现；
- Spring / Gradle / Element Plus Technology Profile 建设；
- 第四工程纪律建设；
- Obsidian 强制采用；
- CodeGraph 强制采用；
- Rule Graph / MCP 平台化；
- 所有 Guide 机械拆文件；
- 把所有长期规则改成 YAML；
- 把所有规则复制进 Skill；
- Runtime / Distribution / Marketplace 建设；
- 多模型协同候选实施。

## 7. CodeGraph / Consumer Code Intelligence 边界

CodeGraph 研究被保留为本里程碑的重要外部参考，但它同时解决一个不同的 Consumer 问题：源码结构发现。

当前边界：

- `agentic-dev` 研究 Rule / Authority Activation；
- Consumer 可以独立实验 CodeGraph 作为可选 Code Intelligence；
- Consumer 主要使用 CodeGraph 的 local index + MCP / CLI + thin activation instructions，不复制其内部开发 Skills；
- `.codegraph/` 只是派生索引，不构成 Consumer Authority；
- CodeGraph 不替代 compiler、tests、runtime verification、specification 或 code review；
- ChatGPT + GitHub Connector 当前不能直接消费 Consumer 本地 `.codegraph/`，Local Codex 等本地 Agent 才是直接受益环境。

本里程碑可以保留 Consumer CodeGraph A/B 设计，但不要求把 CodeGraph 纳入 `agentic-dev` 核心依赖。

## 8. 后继方向：WI-07 — Code Review Capability v1

Code Review 是本里程碑完成后的优先后继候选。

当前规划边界已经冻结到以下程度，以确保未来 Fresh Context 不需要恢复本次聊天：

### 8.1 为什么值得重新评估

- Code Review 在早期 Skill Architecture 中已经存在，但第一批 8 个核心 Skill 阶段选择保持为内嵌纪律；
- 当前已有更多 Consumer / Independent Review Evidence；
- Issue #71 的 Fresh Context 架构盲测证明独立 Reviewer 可以在高返工问题实施前发现真实结构缺陷；
- Code Review 现在具备独立输入、稳定过程、独立输出、退出 / 升级边界和专项 Eval 条件，符合 WI-07 的重新评估门槛。

### 8.2 预期职责

输入：

- 当前 Repository Authority；
- relevant Specification / Plan / Architecture；
- Diff / changed files / current source；
- available verification evidence；
- 按风险激活的 Engineering Discipline / Technology checks。

输出：

- 高信噪比 actionable findings；或
- 明确的 no blocking / medium finding 结论；或
- 证据不足 / 需升级说明。

### 8.3 预期检查重点

- 规格符合性；
- 明确缺陷 / 回归；
- 数据、状态、并发、生命周期；
- Boundary / Dependency / Side-effect；
- 推测性复杂度 / 不必要抽象；
- Diff Scope；
- Verification Evidence；
- 当前上下文触发的高风险技术误用。

### 8.4 明确非目标

- 不成为新的通用 Method Stage；
- 不强制所有微小变更都执行独立 Review；
- 不与 Planning Review 合并；
- 不与 Security Review 等其他专项 Review 合并为超级 Skill；
- 不创建 `vue-review-skill`、`spring-review-skill`、`gradle-review-skill`；
- 不预加载所有 Technology Profile；
- 不把命名、格式、个人风格或无证据未来扩展性作为主要 Finding。

### 8.5 与规则治理的依赖关系

Code Review v1 不应在当前规则激活问题尚未收敛时直接实现，否则很容易形成新的超级 Skill：

```text
code-review
→ 全量 Method + Guide + Discipline + Profile
→ Context 爆炸
```

因此推荐：

```text
规则治理与知识激活 v1
→ Task / Risk → Rule Activation 可验证
→ 再启动 WI-07 Code Review Capability v1
```

### 8.6 与 CodeGraph 的关系

CodeGraph 可以作为 Consumer Code Review 的可选结构发现能力：

```text
Diff
→ CodeGraph related source / callers / impact
→ Rule Activation
→ Reviewer
```

但 Code Review 契约不能依赖 CodeGraph 才能成立；没有 CodeGraph 时必须可以回退到 Repository 原生搜索和读取。

## 9. Technology Profile 决策边界

WI-06 暂不启动。

后续只有 Code Review / Consumer Eval 证明存在稳定、跨项目、模型自身知识 + 当前 Repository + 当前官方资料仍无法可靠补足的增量技术检查知识时，才重新评估持久化 Profile。

当前优先级仅作为研究假设：

- Vue 3 + TypeScript：保留现有 Profile，不机械扩张；
- Spring：高 Review Eval 价值；
- Gradle：高 Review Eval 价值，已有真实应用边界证据；
- Element Plus：通用长期 Profile 价值较低。

不把该优先级当作 WI-06 已启动事实。

## 10. AI 友好代码边界

本轮认可的方向不是“所有代码都要更短”，而是：

> **尽量缩小 Safe Change Reasoning Surface。**

未来 Code Review 可以评估：

- change locality；
- dependency direction；
- state ownership；
- explicit side effects；
- abstraction justification；
- indirection cost；
- contract clarity；
- test seam。

但现有 Engineering Disciplines 已经覆盖实现最小化与精准修改，因此本里程碑不新增第四 Discipline。是否需要“结构可推理性 / Context Radius”类纪律，必须等后续 Review Eval 形成稳定证据。

## 11. 完成定义

本里程碑只有以下条件全部满足才可进入集成决策：

1. 完整 Research 已进入 `docs/research/`；
2. `using-agentic-dev.md` 和 `external-operation-guidelines.md` 至少完成 Activation Audit；
3. 最小 Retrieval Model 已冻结；
4. 历史 Retrieval / Activation Eval 已建立并具有辨识力；
5. 完整 / 粗粒度 Context 与缩减 / 按需 Context 已完成隔离运行时对照和人工语义评分；
6. 必要 Guide / Authority / Skill activation pointer 已按证据收敛；
7. 没有通过复制规则制造新的双重 Authority；
8. 至少完成一次 Consumer Fresh Context 验证；
9. 最终 AI 复核未解决阻塞 / 中等级问题为 `0 / 0`；
10. 集成前项目状态入口完成闭环。

## 12. 当前下一步

下一实际步骤不是拆 Guide，也不是实现 Code Review，而是：

> **Phase A — Activation Audit。**

Fresh Context 开始时应重新读取当前 GitHub 状态、`AGENTS.md`、Project Roadmap、Issue #73、本文件、完整研究文档和协调计划，然后从 Activation Audit 的下一实际工作项继续。
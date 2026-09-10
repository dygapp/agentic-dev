# 使用 agentic-dev

本文说明 AI Agent 或开发者如何把 `agentic-dev` 作为方法、Skill 与 reusable guidance 来源，用于启动并持续推进真实软件项目。

本文是**使用与路由指南**，不重新定义 Method、Principle、Architecture 或 Skill Contract。目标项目自己的 Repository Authority 始终决定项目事实；已完成 adoption 的 Consumer 普通工作优先使用 Consumer-local 已采用版本，不因为 upstream 新提交存在就自动改变运行规则。

## 1. 使用模型

`agentic-dev` 提供：

- Method / Principle：定义通用开发阶段、边界、证据与上下文原则；
- Skill：执行稳定职责的可组合能力；
- Engineering Capability：工程纪律、技术 / 验证画像、平台专项能力；
- Guide：说明 adoption、routing、跨职责协调与外部操作边界。

目标项目仍拥有自己的项目规则、需求、架构、代码、测试、验证与集成策略。

```text
agentic-dev reusable capability
        ↓ explicit adoption
Consumer Repository Authority
+ Consumer-local capability / discovery
```

`agentic-dev` 不替 Consumer 预定义完整目录、技术栈、文档体系或项目事实。

## 2. 开始前的知识边界

启动或重新进入一个项目时，至少区分：

1. `agentic-dev`：可复用方法、Skill 与 Guide 来源；
2. Consumer Repository：当前项目自己的 Authority；
3. 当前明确提供的业务 / 产品需求来源；
4. 当前运行环境可直接观察到的事实与能力。

不得把其他聊天中的未固化结论、其他项目规则、个人记忆或 `agentic-dev` 自身项目状态直接当作 Consumer 项目事实。

如果 Consumer 已完成 `agentic-dev` adoption，ordinary runtime 应回到 Consumer-local Authority / discovery；上游只在显式 baseline upgrade、Consumer-local 必要能力缺失、明确实验或 Consumer Authority 要求时重新进入。

### 2.1 需求来源与 Consumer Authority

外部需求资料不会因为被读取、复制进仓库或自身标记为 `confirmed` / `approved` 就自动成为 Consumer Authority。

目标关系是：

```text
需求来源 / 输入资料
→ Consumer 显式采纳
→ Consumer 权威需求
→ 已澄清意图
→ Specification
```

采用外部需求来源时至少确认：来源关系、当前有效范围、进入 Consumer Authority 后的优先级，以及引用的上游 Requirement / Architecture / Rule 是否在 Consumer 中真实可用。

如果来源资料引用 Consumer 中不存在或未采纳的上游事实，不为了“补齐引用”机械复制整个上游文档体系。只有当前项目确实需要相应长期事实时才建立或采纳本地 Authority。

如果人工已经明确指定某份资料为当前权威需求，不要求重复形式化审批；仍需处理当前范围、Authority precedence 和无法解析的外部引用。

## 3. 新项目：建立最小启动骨架

新项目从**足以让 Fresh Context 正确继续工作的最小 Consumer Authority**开始，而不是从大而全模板开始。

通常先明确：

- 项目目标与当前范围；
- Repository Authority 与 Knowledge Boundary；
- Agent 自主处理和 Human Escalation 边界；
- 基本验证 / 集成策略；
- 当前需求与 Specification 入口；
- 主导语言；
- 当前真正需要的 Skill；
- 项目是否复杂到需要跨里程碑恢复的 Roadmap。

小项目可以只有：

```text
<consumer>/
├── AGENTS.md   # 或等价稳定 Bootstrap
├── README.md
└── <当前真正需要的项目产物>
```

这只是示例，不是固定模板。

复杂项目如果需要跨里程碑 / 阶段 / Fresh Context 恢复整体路线，应建立薄 Roadmap；README 只保存简短状态和指针，不复制详细易变状态。

Planning Candidate / Future Work / Issue 在 `slice-work` 前不具有 Execution Unit 身份。编号、名称、Roadmap 顺序或 `EU-xx` 标签不能替代真实 `slice-work` / `readiness-check`。

### 3.1 主导语言

语言是 Consumer Repository Rule。

Consumer 已有明确语言规则时始终服从本地 Authority；尚未明确时，默认沿用当前权威需求和主要协作输入的主导语言。

如果语言选择会持续影响 Fresh Context 和人工协作，应固化在 Consumer 的稳定规则入口；不要从 `agentic-dev`、历史聊天或运行环境机械继承表达风格。

### 3.2 不预建没有真实需要的结构

不要为了形式完整预建空的 Architecture、ADR、Tasks、Plans、阶段目录、配置体系或 Skill。

长期产物只在真实触发成立时建立：

- 跨功能稳定领域事实 → Consumer Domain / Requirement Authority；
- 跨 Execution Unit durable HOW → Technical Plan；
- 跨功能长期 Architecture state → Architecture Authority；
- 需要长期保存背景 / 权衡 /替代关系的重要 Architecture decision → ADR；
- 跨里程碑恢复需要 → Roadmap；
- 复杂到需要跨 Fresh Context 协调 → Task / Plan。

具体判断由对应 Method / Skill owner 决定，本 Guide 不维护第二份过程定义。

## 4. 使用 Skill

当前 Skill inventory 和职责边界统一见：

`skills/README.md`

核心职责包括：

```text
clarify-intent
specify
technical-plan
slice-work
readiness-check
execute-unit
systematic-debug
converge
```

平台专项 Skill 只在真实平台条件命中时按需加载，例如 GitHub Actions 专项验证使用：

`skills/github-actions-verification/SKILL.md`

规则：

- 使用来自已确认 baseline、且在当前 Consumer-local capability set 中可解析的 Skill；
- Consumer Repository Authority 高于 Skill 对项目事实的推测；
- 不要求所有 Skill 在每个任务中出现；
- 只判断 routing / Stage Return 时，如果 local rule / metadata 已足够，不机械加载完整 Skill；
- 真正进入稳定职责执行时才加载对应 Skill。

采用完成后的 local discovery / Skill activation 见：

`docs/guides/consumer-local-rule-activation.md`

## 5. 常规功能工作的职责路由

本节只负责**何时继续读取哪个 owner**，不重述 Skill Procedure。

| 当前问题 | Primary owner / 继续读取 |
|---|---|
| Product Intent、范围、用户可见行为存在实质歧义 | `skills/clarify-intent/SKILL.md` |
| 需要形成 WHAT / WHY 与完成条件 | `skills/specify/SKILL.md` |
| 出现跨 Execution Unit durable HOW、Architecture / ADR 评估 | `skills/technical-plan/SKILL.md` |
| Specification Ready，需要形成候选 Execution Unit | `skills/slice-work/SKILL.md` |
| Candidate Unit 是否可进入 Execute | `skills/readiness-check/SKILL.md` |
| 一个 Ready Execution Unit 的实现与当前证据 | `skills/execute-unit/SKILL.md` |
| expected behavior 已明确下的 unexpected implementation / runtime failure | `skills/systematic-debug/SKILL.md` |
| 当前范围执行完成后的整体规格 / Evidence 收敛 | `skills/converge/SKILL.md` |

如果当前职责执行中暴露上游 Authority gap，按真实 owner Stage Return；具体 Return / Exit / Escalation 以对应 Skill Contract / Skill 为准，不在本 Guide 复制。

### 5.1 跨职责验证规则

以下情况不要继续扩展本 Guide，而读取独立 owner：

- verification contract 陈旧；
- visual fidelity；
- automated verification 与 Human Review baseline 隔离；
- database migration completion evidence；
- ancestor evidence 在后继提交上的 claim-level reuse；
- evidence type 与 completion claim 匹配。

统一入口：

`docs/guides/verification-evidence-rules.md`

### 5.2 工程纪律

配置责任、复用已有能力、推测性复杂度、差异范围和数据访问有界性由：

`docs/architecture/engineering-disciplines.md`

单点拥有。当前职责只在真实 condition / risk 命中时按需读取相应 Discipline，不在本 Guide 维护第二份工程规则正文。

### 5.3 外部操作与平台能力

外部状态修改、异步操作、共享资源、临时 Evidence 晋升、依赖 PR 拓扑等见：

`docs/guides/external-operation-guidelines.md`

GitHub Actions trigger / gate / observability / runtime / artifact / timeout / cancellation 等平台专项过程见：

`skills/github-actions-verification/SKILL.md`

平台细节不提升为所有 Consumer 的通用 Method Rule。

## 6. 项目如何持续演进

Consumer Repository 应随真实工作逐步丰富，而不是在初始化时一次设计完成。

### 6.1 已有 Consumer 的采用与 baseline upgrade

`agentic-dev` 是 upstream reusable source，不是已有 Consumer ordinary development 必须持续读取的 Runtime Dependency。

只有以下情况按需重新读取 upstream：

- 显式执行 `agentic-dev` baseline upgrade；
- Consumer-local Authority 无法回答当前真正需要的方法 / Skill 问题；
- 当前任务明确属于 `agentic-dev` experiment / validation；
- Consumer Repository Authority 另有要求。

采用 / 升级时：

```text
Current Consumer Authority
+ previous evaluated upstream baseline
+ candidate exact upstream baseline
→ classify reusable vs agentic-dev project-only
→ per-item adopt / retain-or-override / reject-not-applicable / supersede-remove
→ persist durable adopted result locally
→ validate local discovery / capability
→ ordinary runtime returns local-only
```

必须区分：

- last evaluated upstream baseline；
- 每个 active local asset 自身的 `adopted_from` provenance；
- upgrade-only decision history。

不能只更新一个 baseline 字符串就暗示全部 upstream 规则已采用。

需要长期约束 ordinary runtime 的变化必须进入 Consumer-local semantic owner / Skill / discovery；只服务一次升级判断的分析和 rejected decision 不进入普通 Fresh Context。

详细 local projection / runtime activation 见：

`docs/guides/consumer-local-rule-activation.md`

### 6.2 长期产物与 Roadmap 生命周期

新增长期产物前先判断：

> 它是否具有当前项目真实、持续的协调或 Authority 价值？

如果没有，不为形式完整而持久化。

已有且仍适用的 Roadmap 在里程碑完成 / 取消 / 被取代、当前阶段或核心目标改变、已决定的下一步顺序改变、条件性方向正式进入当前路线时更新。

README、Task 和 Roadmap 不并行维护多份详细 current state；精确 PR / Run / Issue 状态优先由 GitHub 等事实来源保存。

合并后如果 Roadmap / README 会立即过时，应在进入集成决策前检查**集成后稳定状态**，避免为机械状态尾差再创建无价值的补丁。

## 7. Fresh Context 恢复

Fresh Context 的目标是从持久化 Consumer Authority 恢复当前工作，不依赖历史聊天。

推荐顺序：

```text
Consumer stable Bootstrap
→ README / Documentation Authority Map
→ Current Roadmap / current gate
→ Consumer-local discovery entry
→ 当前任务直接相关 Authority
→ routing-only 或按需 Skill
```

不要因为“怕漏规则”默认加载：

- 完整历史聊天；
- 已关闭里程碑全过程；
- 全部 Method / Guide / Skill；
- upstream latest；
- baseline upgrade history；
- 所有候选工作。

如果 local discovery stale / missing / ambiguous，先 fail-closed 到 Consumer Current Authority，再按需扩大本地读取；ordinary runtime 不自动跨仓访问 upstream。

## 8. `agentic-dev` 实验 / 反馈

只有任务被明确标记为 `agentic-dev` experiment / validation 时，才把上游 eval / Research / Issue 作为当前实验输入。

Consumer 实验应：

- 固定 Consumer exact base 与 candidate `agentic-dev` exact baseline；
- 与 Consumer 正常工作分支隔离；
- 记录可审计 evidence；
- 区分 reusable finding 与 Consumer-only finding；
- 实验 PASS 不自动等于 Consumer 正式 adoption 或 branch merge。

跨项目可复用反馈进入 `agentic-dev` 后，仍需经过上游自己的证据分类、架构适配与 Authority 更新流程。

## 9. 推荐启动方式

新 Consumer 或 Fresh Context 的提示只需要给出项目身份和特殊约束，不复制完整规则正文。例如：

```text
这是一个 Fresh Context。
继续：<consumer repository>
GitHub Repository 是唯一项目事实来源。
先读取当前仓库稳定 Bootstrap / README，并按 Repository Authority 恢复当前阶段与本地 discovery entry，从下一实际步骤继续。
<本轮必要特殊约束>
```

真正的 Method / Rule / Skill 从当前仓库和本地 discovery 按需取得。

## 10. 使用目标

`agentic-dev` 的目标不是提前规定 Consumer 最终长什么样，而是让 AI 能够：

1. 从最小、明确的 Consumer Authority 开始；
2. 根据真实需求逐步建立项目知识与结构；
3. 通过 local discovery 找到当前适用规则与职责；
4. 真正进入职责时按需加载 Skill；
5. 用 Fresh Context 与 Current Evidence 推进工作；
6. 只持久化真正具有长期价值的知识；
7. 在 Consumer 演进中保持 Authority、baseline adoption 和 runtime independence 可审计；
8. 最终基于整体 Evidence 达到“已具备进入集成决策的条件”。
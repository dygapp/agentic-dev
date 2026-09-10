# 规则所有权与 Guide 拆分审计 v2

## 状态

**Phase B 结果 — Rule Ownership / Guide Decomposition Audit**

上层里程碑：Issue #92 / `docs/project/rule-governance-knowledge-activation-v2.md`

验收输入：

- `docs/project/consumer-local-rule-runtime-target-v2.md`
- `docs/project/consumer-local-rule-runtime-acceptance-v2.md`

本文只冻结**语义 owner、独立激活边界与 Consumer-local 投射价值**。不冻结物理文件拆分、metadata 最终 schema、Catalog 格式或运行时工具。

## 1. 审计原则

### 1.1 先找 semantic owner，再谈模块

一个规则是否值得成为独立激活单元，不能由以下因素决定：

- 当前文件很长；
- 当前标题已经存在；
- 某段在临时 G-min manifest 中表现良好；
- 某个关键词容易分类；
- 为了让 Catalog 看起来完整。

必须先回答：

1. 这条规则的长期语义由谁拥有？
2. 它是否有独立于现有 Skill / Principle 的激活条件？
3. 哪些职责会消费它？
4. Consumer 是否需要把它长期本地化？
5. 如果不独立激活，是否会导致遗漏、误读或不必要的大上下文？
6. 是否已有更高层 Authority 定义同一语义？

### 1.2 单点正文 owner

同一规范性语义只允许一个正文 owner。

允许：

```text
Principle / Skill / Discipline / Guide Rule Module
        ↑
metadata / catalog / navigation pointer
```

不允许：

```text
Guide 正文 A
+ Skill 正文 B
+ Consumer Method 正文 C
+ Catalog 摘要 D
```

四处都维护同一规则细节。

Consumer-local adoption 可以把上游语义转换成使用方自己的长期规则，但完成采用后，Consumer 自己声明的本地 Authority 成为其 ordinary runtime 的事实来源；upstream provenance 只用于追溯与再次升级。

### 1.3 Guide 不是默认 owner

`using-agentic-dev.md` 的定位是“如何使用方法与 Skill”，不应重新定义核心 Method / Principle / Skill Contract。

因此：

- 纯阶段 / Skill 职责语义优先回到 Method / Principle / Skill；
- Guide 只保留真正跨职责、Consumer adoption、runtime coordination 或平台使用边界；
- 现有 Guide 中重复高层 Authority 的正文，应在后续收敛为薄指针或删除重复，而不是继续作为独立规则模块。

### 1.4 Consumer-local 投射不是整份 Guide vendor

只有对 Consumer 后续工作具有持续约束价值的规则才需要本地化。

对每个可复用规则都应允许：

```text
adopt
retain / override
reject / not applicable
```

不能因为它存在于 upstream Guide，就把整份 Guide 复制进 Consumer。

## 2. Owner 类型

本审计使用以下 owner 类型。

| 类型 | 语义职责 | Consumer-local 处理 |
|---|---|---|
| `principle` | 跨阶段顶层方法不变量 | 通常由 adopted local method rule / bootstrap 薄表达消费，不复制整份 Principle |
| `skill` | 稳定任务职责的完整执行过程、Use / Do Not Use、Stage Return、Exit / Escalation | Consumer 只采用实际需要的 Skill；执行时按需加载 |
| `engineering-discipline` | 阶段内部、跨技术栈的可组合工程约束 | 只在相关职责 / 风险触发时激活；不转成新 Skill |
| `reusable-guide-rule` | 不属于单一 Skill、但具有独立触发和跨职责协调价值的可复用规则 | 可以成为 Consumer-local rule module 候选 |
| `platform-specific-skill` | 平台专项、稳定独立职责 | 只有 Consumer 使用对应平台且条件命中时采用 / 激活 |
| `platform-specific-guide-rule` | 平台协作 / 授权边界，但不构成独立稳定 Skill | Consumer 使用该平台时按需采用 |
| `consumer-native-authority` | Consumer 项目自身事实 / 规则 | 由 Consumer 自己拥有；不来自 upstream |
| `agentic-dev-project-only` | 只约束本仓库自身 | 不投射到 Consumer |
| `derived-discovery` | metadata / Catalog / navigation | 不拥有规范性正文，可删除 / 重建 |
| `explanatory` | 示例、背景、目录说明、使用目标 | 不作为独立 Runtime activation unit |

## 3. 顶层 Principle 的 owner 结论

当前 `docs/method/principles.md` 已经定义多项后续运行时会反复使用的高层语义。它们不应再由 Guide 维护第二份正文。

| 语义 | 当前唯一上游 owner | 运行时处理 |
|---|---|---|
| 阶段是状态，不是文档 | P1 | 需要时由 local method / metadata 指向，不建 Guide module |
| WHAT / WHY 与 HOW 分离 | P2 | 由 specify / technical-plan Skill 消费 |
| 持久化知识，不持久化推理 | P3 | Fresh Context / artifact lifecycle 规则引用 |
| context-fit | P4 | slice-work / execute-unit 消费 |
| 纵向可验证执行单元 | P5 | slice-work 消费 |
| Fresh Context 是逻辑属性 | P6 | recovery / execution context 条件消费 |
| Progressive Disclosure | P7 | **always-on thin invariant**，正文 owner 仍是 P7 |
| Evidence before claims | P8 | **always-on thin invariant**，正文 owner 仍是 P8 |
| Human escalation | P9 | 按风险条件消费，不复制成独立大 Guide |
| Verification / Review / Convergence 分离 | P10 | verification / converge / future review responsibility 消费 |
| Technical Planning 条件进入 | P11 | technical-plan Skill + routing metadata 消费 |
| Durable Technical Plan vs JIT | P12 | technical-plan / execute-unit Skill 消费 |
| Skill 小型可组合 | P13 | Skill architecture / admission 消费，不作为 Consumer ordinary task module |
| Integration 是授权边界 | P14 | external operation / converge / Consumer repository policy 消费 |
| ADR 条件性 | P15 | technical-plan Skill 消费 |

### 3.1 always-on 不等于全文常驻

v1 已采用的三个薄不变量仍成立：

- Consumer Repository Authority first；
- Progressive Disclosure；
- Evidence before claims。

其中后两项正文已由 P7 / P8 拥有。Consumer Bootstrap 只需要保存足以激活这些原则的薄表达和本地发现入口，不需要复制整个 `principles.md`。

Consumer Repository Authority first 不是当前核心 Principle 中完整定义的“Consumer vs upstream”关系，因此仍需要一个 Consumer bootstrap / adoption 语义 owner，见 §5。

## 4. 8 个核心 Skill 的 owner 结论

当前 8 个核心 Skill 已经具有稳定职责、Use / Do Not Use、Inputs、Authority、Procedure、Outputs、Exit、Escalation 和 Context Rules。其完整执行过程应由 Skill 自己拥有。

| 职责 | 唯一执行 owner | Guide 后续角色 |
|---|---|---|
| Product Intent clarification | `clarify-intent` | 只保留触发 / 路由指针 |
| WHAT / WHY specification | `specify` | 只保留触发 / 路由指针 |
| Durable cross-unit HOW / Architecture / ADR evaluation | `technical-plan` | 只保留跨阶段路由指针 |
| Execution Unit shaping / obligation mapping | `slice-work` | 只保留候选→切分入口指针 |
| Pre-execution gate | `readiness-check` | 不由 Guide 重述 Gate 规则 |
| One-unit execution / current evidence | `execute-unit` | 只保留 Fresh execution coordination 指针 |
| Observed Defect / Unexpected Failure investigation | `systematic-debug` | 只保留“何时进入 / 不进入”的路由边界 |
| Feature-wide convergence | `converge` | 只保留 workflow coordination 指针 |

### 4.1 Stage Return 不是新的 Mega-Skill

`execute-unit → technical-plan`、`readiness-check → slice-work / technical-plan`、`systematic-debug → specify / technical-plan` 等返回关系已经存在于 Skill Contract / Skill 自身。

后续 discovery 可以把这些关系表示成**轻量 routing metadata / edge**，用于帮助 Agent 找到正确 owner；但不创建新的“Stage Router Skill”或复制所有返回规则的独立大正文。

### 4.2 Routing-only 可以不加载完整 Skill

如果当前任务只需要判断“下一职责是谁”，metadata + 小型跨职责规则已经足够时，不机械加载完整 Skill。

真正进入职责执行时，再加载对应 Skill 正文。这与 A2 的 CL-05 / CL-06 一致。

## 5. `using-agentic-dev.md` ownership 审计

### 5.1 总体判断

当前 Guide 同时承载四种不同内容：

1. Consumer bootstrap / adoption；
2. 核心 Skill 的使用说明；
3. 跨职责工程 / verification 条件规则；
4. 解释性使用说明。

这四类不应继续作为一份大 Runtime 文档默认加载。

### 5.2 审计矩阵

| 当前区域 | 语义分类 | 长期 owner 结论 | Consumer-local 投射 |
|---|---|---|---|
| §1 使用模型 | explanatory + bootstrap orientation | 解释性，不独立成 Runtime module | 不要求复制；Bootstrap 可保留一行 upstream/Consumer 边界 |
| §2 知识边界 | `consumer adoption / bootstrap` | **保留为可复用 bootstrap rule family** | 高价值；Consumer 应本地固化自己的 Authority / Knowledge Boundary |
| §2.1 需求来源与使用方权威 | `reusable-guide-rule` | **独立规则模块候选：requirement-source-adoption** | 按有外部需求输入的 Consumer 采用 |
| §3 新项目最小骨架 | `consumer adoption / bootstrap` | **bootstrap module 候选**；不规定固定目录 | 新 Consumer 初始化时使用，普通日常不常驻全文 |
| §3 中 Planning Candidate / EU identity 规则 | skill/routing overlap | `slice-work` / `readiness-check` + local roadmap governance owner | 通过 local method/routing metadata 激活，不保留 Guide 重复正文 |
| §3.1 主导语言 | consumer-specific governance | upstream 只提供默认选择边界；最终 owner 是 Consumer Repository Rule | 初始化 / adoption 时决定并本地固化 |
| §3.2 不预建结构 / 长期产物触发 | principle + cross-skill coordination | P1/P3/P11/P15 + relevant Skill；项目路线图生命周期见独立 module | 删除重复正文或变成指针；不整体投射 |
| §4 使用 Skill / Skill 列表 | explanatory + distribution boundary | Skill inventory 由 `skills/README.md`；runtime distribution 后续由 adoption contract | 普通 Runtime 不需要独立 Guide module |
| §5.1 clarify-intent | skill-owned | `clarify-intent` | Guide 只保留 routing metadata |
| §5.2 specify | skill-owned | `specify` | 同上 |
| §5.3 technical-plan / Architecture / ADR | principle + skill-owned | P11/P12/P15 + `technical-plan` | Guide 不再维护完整重复正文；只保留 routing edge |
| §5.4 slice + readiness | skill-owned + cross-stage routing | `slice-work` + `readiness-check` | routing metadata 指向 owner；旧 Readiness 失效关系由 Skill owner 保持 |
| §5.5 execution context | skill-owned + recovery coordination | `execute-unit`；Fresh Context 通用部分见 recovery module | 不重复完整 execution rules |
| §5.6 配置责任 / 能力复用 | engineering discipline overlap | **并入 Engineering Discipline owner**，而不是独立 Guide owner | Consumer 采用适用 discipline；按 execute/review 风险激活 |
| §5.7 completion evidence 总原则 | P8 + Skill-owned | P8 + `execute-unit` / `converge` | 不建立通用重复正文 module |
| §5.7 visual fidelity | `reusable-guide-rule` | **独立条件模块候选：visual-evidence** | 只有视觉一致性 requirement / review 命中时采用/激活 |
| §5.7 automated vs human review baseline | `reusable-guide-rule`，与 Actions Skill 部分重叠 | 通用规则保留为 **human-review-baseline**；Actions 实现细节由平台 Skill | 有 Human Review workflow 的 Consumer 按需采用 |
| §5.7 fresh DB migration chain | `reusable-guide-rule` | **database-migration-completion-evidence** 候选 | 只有 DB migration / schema lifecycle Consumer 采用 |
| §5.7 stale verification contract | `reusable-guide-rule` | **verification-contract-currentness** 候选 | 高复用；验证失败 / assertion mismatch 时激活 |
| §5.7 later-commit evidence reuse | `reusable-guide-rule` | **evidence-claim-reuse** 候选 | 使用 CI / review evidence 的 Consumer 高价值 |
| §5.7 GitHub Actions trigger / observability / cost | platform-specific overlap | `github-actions-verification` Skill | Consumer 使用 GitHub Actions 时采用该 Skill，不保留 Guide 重复细节 |
| §5.7 artifact promotion | cross-guide overlap | `external-operation-guidelines` §5.3 应成为唯一 reusable owner | Guide 只留指针 |
| §5.7 timeout / cancellation / runtime observation | cross-guide / platform overlap | generic async boundary → external operation guide；Actions detail → platform Skill | 不在 using Guide 重复 |
| §5.8 converge | skill-owned + P14 | `converge` + P14 | routing metadata / Skill owner |
| §6.1 baseline adoption / upgrade | `consumer adoption / bootstrap` | **独立规则模块候选：consumer-baseline-adoption** | v2 核心；adoption 时使用，完成后结果本地化 |
| §6.2 artifact lifecycle / roadmap | cross-skill project governance | **artifact-lifecycle / roadmap-lifecycle 模块候选**，但需按真实触发再决定是否拆成两个 | 仅长期项目需要；不要求小项目机械建立 Roadmap |
| §7 Fresh Context recovery | `reusable-guide-rule` | **fresh-context-recovery** 候选 | 高价值；本地 Authority Map / Roadmap 驱动 |
| §8 experiment feedback | experiment-only reusable guide | **experiment-feedback** 条件模块，ordinary Consumer 不激活 | 仅明确 agentic-dev experiment 时采用 |
| §9 推荐启动方式 | explanatory | 作为 bootstrap 示例，不成为独立 normative module | 不投射正文 |
| §10 使用目标 | explanatory | 无独立 runtime owner | 不投射 |

## 6. Engineering Discipline ownership

`using-agentic-dev` §5.6 当前包含“配置责任”和“复用已有能力”的详细规则；这些语义与工程纪律中“实现最小化与推测性复杂度控制”的 §4.5 高度重叠。

Phase B 结论：

- 详细工程判断应由 `docs/architecture/engineering-disciplines.md` 单点拥有；
- `execute-unit` 继续薄消费；
- Guide 不再维护第二份完整规则；
- future review responsibility 也可以消费同一 Discipline；
- 不因此创建 `configuration-skill` 或 `reuse-skill`。

三个现行 Engineering Discipline 都应作为**可独立发现的 adopted reusable capability**，但其激活粒度可以先保持 discipline-level，而不是为每个小节再生成大量 metadata 条目。

候选触发：

- speculative / abstraction / configuration / dependency complexity → implementation minimality；
- broad diff / adjacent cleanup / preparatory refactor → surgical change；
- collection / list / pagination / bounded snapshot / scope → data access scope & boundedness。

## 7. `external-operation-guidelines.md` ownership 审计

### 7.1 总体判断

该 Guide 的核心价值不是“GitHub 操作说明”，而是**任何有外部状态副作用的协作治理**。其中一部分是通用 reusable rule，一部分已经由 `github-actions-verification` 平台 Skill 更精确拥有，一部分只是 GitHub 示例。

### 7.2 审计矩阵

| 当前区域 | 语义分类 | 长期 owner 结论 | Consumer-local 投射 |
|---|---|---|---|
| §1 核心闭环 | `reusable-guide-rule` | **external-operation-closure**：read/analyze → write → reread/verify → report | 使用外部写操作能力的 Consumer 高价值 |
| §2 状态 / 授权确认 | `reusable-guide-rule` | 与 §1 合并为 external-operation-closure 的 authority/input 部分 | 不另建第二 module |
| §2.1 能操作≠已授权 | P9/P14 + external op | P9/P14 为高层 owner；external module 保留外部操作具体消费边界 | Consumer repository policy 可覆盖具体权限 |
| §2.2 多仓库授权 | `reusable-guide-rule` | **multi-repository-authorization** 独立候选 | 只有跨 repo task 激活 |
| §3 人工介入 | P9 overlap | P9 owner；Guide 只保留外部操作的具体触发指针 | 不重复完整人工升级规则 |
| §4 最小必要操作 | Engineering Discipline overlap | implementation minimality / surgical change + external operation scope | Guide 只保留外部 side-effect 限制 |
| §4.1 二进制 / 媒体真实内容 | `reusable-guide-rule` | **external-media-content-validation** 独立候选 | 只有外部 binary/media 输入时激活 |
| §5 写后验证 | external-operation-closure | 合并到 §1 owner | 不独立重复 |
| §5.1 异步外部操作 | `reusable-guide-rule` | **async-external-operation** 独立候选 | 异步 workflow / deploy / remote task 条件激活 |
| §5.2 共享资源 / lease / stale run | `reusable-guide-rule` | **shared-external-resource-lifecycle** 独立候选 | 有真实共享资源竞争时激活 |
| §5.3 临时证据→持久输入 | `reusable-guide-rule` | **ephemeral-evidence-promotion** 独立候选 | artifact/snapshot 被长期消费时激活 |
| §5.4 依赖 PR 拓扑 | `platform-specific-guide-rule` | **github-dependent-pr-topology** 独立候选 | 仅 GitHub + dependent/stacked PR 条件激活 |
| §6 汇报状态 | external-operation-closure + P8 | 合并到核心 closure；P8 负责 evidence-before-claim | 不另建 module |
| §7 外部语言一致性 | agentic-dev project-specific expression rule | `agentic-dev` 当前项目规则；Consumer language 由本地 Authority | 不自动投射 |
| §8.1 Git/GitHub 执行路径 | `platform-specific-guide-rule` | **github-collaboration-path** 候选；不等于 Actions Skill | 使用 GitHub 且需要 branch/PR path 选择时激活 |
| §8.2/8.3/8.4 PR/Repo/Issue recipe | explanatory recipe | §1 closure 的示例 | 不独立激活 |
| §9 关系说明 | explanatory | 无独立 runtime unit | 不投射 |

## 8. `github-actions-verification` 平台 Skill ownership

该 Skill 已经拥有：

- GitHub Actions trigger path / observability；
- Evidence Claim → verification layer → actual trigger/gate；
- layered fast feedback / completion verification；
- container/runtime reuse；
- automated verification vs Human Review environment implementation；
- runtime cost / timeout / cancellation；
- shared GitHub Actions resource contention；
- artifact/log/diagnostic handling。

因此 Phase B 决定：

- `using-agentic-dev` 和 `external-operation-guidelines` 中 GitHub Actions-specific 细节后续只保留触发指针；
- 通用的 Human Review Baseline、artifact promotion、async closure、shared resource lifecycle 仍可由 generic Guide module 单点拥有；
- 平台 Skill 只在 GitHub Actions 条件命中且真正需要其专项过程时加载；
- 不把 GitHub Actions Skill 变成所有验证工作的默认依赖。

## 9. 候选 reusable activation inventory

Phase B 最终不以当前文件章节为单位，而形成以下**语义候选集合**。Phase C 只允许围绕这些或更小的经证据支持集合设计 metadata；不得回到“每个标题一个 record”。

### 9.1 Bootstrap / adoption

1. `consumer-authority-boundary`
   - owner：reusable Guide bootstrap family
   - trigger：Consumer initialization / adoption / authority confusion
   - consumer：所有 Consumer，但正文不常驻全文
   - local projection：Consumer 自己的 Repository Authority / Knowledge Boundary

2. `requirement-source-adoption`
   - owner：reusable Guide rule
   - trigger：external requirement/source intake
   - local projection：仅需要处理 external source 的 Consumer

3. `consumer-bootstrap-minimality`
   - owner：reusable Guide rule + P1/P3
   - trigger：new Consumer / first authority skeleton
   - local projection：初始化后结果归 Consumer 自己

4. `consumer-baseline-adoption`
   - owner：reusable Guide rule
   - trigger：new/existing Consumer adoption / baseline upgrade
   - local projection：v2 核心；ordinary runtime 只使用投射结果

5. `fresh-context-recovery`
   - owner：reusable Guide rule + P3/P6/P7
   - trigger：new context / interruption / handoff
   - local projection：Consumer local Authority Map / Roadmap / current gate

6. `artifact-roadmap-lifecycle`
   - owner：reusable Guide rule + P1/P3
   - trigger：long-lived project artifacts / roadmap update / integration state
   - local projection：只有真实长期协调需要时采用

### 9.2 Workflow / routing

核心方法职责不创建第二份规则正文；discovery 只需要 owner-level metadata：

- clarify-intent
- specify
- technical-plan
- slice-work
- readiness-check
- execute-unit
- systematic-debug
- converge

这些 metadata 的 source owner 是 Skill / Skill Contract / Principle，不是新 Guide module。

### 9.3 Cross-skill engineering / verification

7. `verification-contract-currentness`
8. `visual-evidence`
9. `human-review-baseline`
10. `database-migration-completion-evidence`
11. `evidence-claim-reuse`

再加 3 个现有 Engineering Discipline owner：

- implementation minimality
- surgical change
- data access scope & boundedness

Engineering Discipline 不需要再包装成 Guide module。

### 9.4 External operation

12. `external-operation-closure`
13. `multi-repository-authorization`
14. `external-media-content-validation`
15. `async-external-operation`
16. `shared-external-resource-lifecycle`
17. `ephemeral-evidence-promotion`

### 9.5 Platform-specific

18. `github-dependent-pr-topology`
19. `github-collaboration-path`
20. `github-actions-verification`（现有平台 Skill）

### 9.6 Conditional experiment-only

21. `agentic-dev-experiment-feedback`

只在明确实验时激活，不进入普通 Consumer runtime 默认集合。

## 10. 不应成为独立 activation unit 的内容

以下内容在 Phase B 明确排除：

- `using-agentic-dev` §1 的总体使用模型；
- Skill 清单本身；
- “推荐启动提示词”示例；
- 使用目标总结；
- PR / repo / issue 的重复 read→write→reread recipe；
- 仅属于 `agentic-dev` 自身的中文表达、Roadmap、Issue、提交策略；
- 已由 Principle / Skill / Engineering Discipline 明确定义的重复正文；
- 临时 G-min manifest 中仅为了实验可辨识度添加、但没有长期 owner 价值的字段组合。

这些内容可以保留为人类文档、示例或 derived discovery 信息，但不进入正式独立规则模块集合。

## 11. Consumer-local 投射结论

### 11.1 Consumer 不需要复制 21 个 upstream 模块

Phase B inventory 是 upstream reusable semantic inventory，不是 Consumer 必装清单。

Consumer baseline adoption 时，只选择：

- 当前运行环境 /平台实际需要的能力；
- 当前项目持续使用的工程规则；
- 当前 Fresh Context / governance 需要的 bootstrap / recovery 规则；
- Consumer 自身 local Authority。

例如一个不使用 GitHub Actions、没有 Human Review Environment、没有外部媒体输入的 Consumer，可以完全不投射对应模块 / Skill。

### 11.2 Consumer-native owner 必须参与同一 discovery

Phase C 的 metadata 契约不能只描述 upstream inventory。它必须允许 Consumer 给自己的：

- Requirement / Specification；
- Architecture / ADR；
- Verification Strategy；
- Repository-specific governance rule；
- Current Execution Authority；

建立最小可发现 identity / scope / condition / source pointer，而无需把这些文档改造成 `agentic-dev` 的格式。

### 11.3 local override 不需要复制 upstream 正文

如果 Consumer 对某 reusable default 有更具体规则：

- local metadata 指向 Consumer semantic owner；
- provenance 可以记录它覆盖 / 保留哪个 adopted upstream candidate；
- ordinary runtime 直接读取 Consumer owner；
- 不要求同时加载 upstream 被覆盖正文。

## 12. Phase B 决定

Phase B 完成以下收敛：

1. **Guide decomposition 按语义 owner 与激活条件，而不是文件章节。**
2. **8 个核心 Skill 的完整执行过程继续由 Skill 单点拥有。**
3. **Principle / Engineering Discipline 保持自身 Authority，不复制到 Guide module。**
4. `using-agentic-dev` 后续应从“大型混合运行时文档”收敛为 bootstrap/adoption + cross-skill coordination + 人类使用说明；Skill 过程正文逐步去重。
5. `external-operation-guidelines` 保留真正独立的 external-operation rule families，并去掉与 P9/P14、Engineering Discipline、GitHub Actions Skill 的重复语义。
6. `github-actions-verification` 保持平台专项 Skill owner；通用规则与平台实现边界分离。
7. upstream semantic inventory 当前形成 21 个候选，其中 8 个核心 Skill responsibility、3 个 Engineering Discipline 与 1 个平台 Skill已有独立 owner；其余 reusable Guide rule families 需要 Phase C 设计最小 metadata / source identity。
8. **Consumer 不按 inventory 全量安装，而通过 baseline adoption 选择性投射。**
9. Consumer-native Authority 必须能进入同一本地 discovery path；这是 Phase C schema 的硬要求。
10. 当前没有证据要求 Runtime Rule Index、向量/图数据库、全仓 Front Matter、Rule Router Skill 或新的核心 Skill。

## 13. 进入 Phase C 的约束

Phase C 只冻结**最小 metadata / Catalog 契约**，必须做到：

- metadata 足以发现 semantic owner，但不复制正文；
- 能表达 Consumer-native 与 adopted reusable 两类来源；
- 能表达 primary/supporting responsibility 所需的最少筛选维度；
- 能追踪 source identity / provenance / supersede；
- 能检测 stale / missing；
- Consumer 不需要重构现有文档目录；
- Catalog 可删除 / 可重建；
- rejected / superseded candidate 不参与 ordinary runtime；
- 不把 21 个 inventory 项机械变成所有 Consumer 的固定 records；
- 不在 schema 中编码 `agentic-dev` 自身项目状态。

满足这些约束后，Phase C 才可以选择 JSON / YAML / front matter / generated catalog 等具体最小载体。

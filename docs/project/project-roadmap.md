# 项目演进路线与当前状态

本文是 `agentic-dev` 仓库自身的项目路线图（Project Roadmap），统一记录项目演进路线、已完成里程碑、当前阶段、当前证据基线、当前核心目标与下一步工作。

本文属于 `docs/project/*` 项目级权威，不修改也不覆盖更高优先级的 Method、Architecture 或 Contract Authority，Consumer Repository 也不得自动继承其中的项目事实。

## 路线图使用规则

本文维护当前有效路线，不要求在项目开始时预知完整演进过程。

路线项使用以下状态语义：

- **已完成**：已有 Git、PR、Issue 或评估证据支持；
- **当前**：正在持续推进的阶段或核心目标；
- **下一步**：已经确定但尚未开始或尚未完成的近期工作；
- **条件性后续**：需要后续证据或阶段成果才能决定是否进入，不构成当前承诺。

路线、里程碑或当前目标发生变化时更新本文。Git 历史保留旧版本，不在 README、Tasks 或聊天中长期维护第二份详细状态。

## 阶段切换

此前阶段：

> **Skill Operationalization & Method Validation**

已经完成其主要使命：第一批核心 Skill 已完成工程闭环，首轮 Greenfield Consumer Experiment 已完成，已有 Consumer 的继续演进又进一步验证并强化了 baseline 升级、外部操作、验证证据、Human Review、共享资源、配置责任和已有能力复用等边界。

这里的“阶段使命完成”不等同于 Issue #33 已经关闭。Issue #33 仍可按其原始实验目标独立形成 Final Summary 并收尾；其已经形成的多轮有效证据足以支持 `agentic-dev` 不再把持续等待该实验新增 Finding 作为下一阶段启动条件。

`dygapp/jilinjobs-cms` 后续主要进入模块化重构、页面内容完善和大平台集成准备，其继续开发仍可提供实践反馈，但不再适合作为 `agentic-dev` 唯一或主要的能力创新来源。

因此当前阶段切换为：

> **Engineering Capability Expansion & Method Evolution（工程能力扩展与方法演进）**

本阶段从“主要等待 Consumer 暴露问题后定向修补”，转向“主动研究成熟外部实践、形成工程能力、建立专项评估，再推动 Consumer 采用和纠偏”。

当前阶段采用一个明确有限的项目里程碑作为收敛边界：

> **Engineering Capability Foundation v1（工程能力基础版 v1）**

其完成定义、当前剩余阶段、范围冻结规则和 Post-v1 Backlog 统一见：

`docs/project/engineering-capability-foundation-v1.md`

## 总体演进路线

| 路线 | 状态 | 当前目标 |
|---|---|---|
| 建立通用 AI Agent 开发方法基线 | 已完成 | Method、Principles 与第一批 Skill 设计、契约形成稳定基线 |
| 完成第一批核心 Skill 工程 | 已完成 | 8 个 Core Skills 实现、Packaging Hardening、Fresh Runtime Eval 与 Closure Review 完成 |
| 完成首轮方法与 Skill 实证验证 | 已完成 | Greenfield Experiment 已完成；Existing Consumer 多轮证据已足以支持阶段切换，Issue #33 独立收尾 |
| Track A — Method Consolidation | 当前 | Core Method 进入稳定维护；只在高质量证据揭示通用生命周期或权威缺口时定向修改 |
| Track B — Engineering Discipline Expansion | 已完成 | Foundation v1 首批两个 Engineering Discipline 已通过 Targeted Eval 并由 PR #48 正式集成 |
| Track C — Technology Engineering Profiles | 已完成 | Technology Profile Contract 由 PR #49 集成；唯一代表性 Vue 3 + TypeScript Profile 已由 PR #50 正式集成 |
| Track D — Consumer Adoption | **当前** | Foundation v1 只执行一次受控 Existing Consumer Adoption；当前等待 Consumer 自己的项目会话完成正在进行的工作后执行并回传 Evidence |
| Track E — Engineering Skills | 条件性后续 | Post-v1 候选；Skill 数量不是 Foundation v1 完成指标，只有出现独立稳定职责时才在后续里程碑评估 |
| Track F — Runtime / Distribution | 条件性后续 | Post-v1 候选；Runtime Adapter、Marketplace、Plugin Bundle、Controller 与统一安装器不属于 Foundation v1 Completion Gate |

## 工程能力扩展模型

新的主动演进模型采用：

```text
官方权威实践 / 成熟开源实践 / 专家研究
                    ↓
               Research
                    ↓
         Engineering Capability Fit
                    ↓
      Discipline / Profile / Skill / Adapter
                    ↓
             Targeted Eval
                    ↓
               AI Review
                    ↓
               Integrate
                    ↓
          Consumer Adoption
                    ↓
          Feedback / Revision
```

具体能力生命周期以 `docs/architecture/engineering-capability-architecture.md` 为准；其中 Candidate 在 Targeted Eval 前必须先经过 Architecture Fit Review 并形成 Draft Capability。

Consumer Evidence 仍然是重要输入，但主要承担：

- 验证通用能力是否适合真实工程环境；
- 发现 Profile 或 Skill 与项目实际约束之间的冲突；
- 纠正过度抽象或错误默认值；
- 调整能力优先级；
- 验证 Existing Consumer baseline upgrade 是否可靠。

不再采用：

```text
等待 Consumer 出现问题
        ↓
agentic-dev 才开始研究
```

作为项目唯一的演进模式。

工程能力分层的正式架构见：

`docs/architecture/engineering-capability-architecture.md`

## 已完成里程碑

| 日期 | 里程碑 | 证据 |
|---|---|---|
| 2026-08-17 | 建立 Method 基线并冻结第一批核心 Skill 设计与契约 | `8fccf7232c21`、`b5480db06940`、`992f13a2ed49` |
| 2026-08-17 | 完成 8 个 Core Skills 首轮实现 | `99314b70c05c` 至 `c96cc7e2ac30` |
| 2026-08-18 | 完成首轮 Fresh Runtime Eval 并关闭第一批历史 Skill Engineering 基线 | `498bdfc543bf`、`bf4f4b5e7ba6` |
| 2026-08-18 | 启动首个真实 Consumer Repository 验证 | Issue #18 |
| 2026-08-24 | 完成验收到验证闭环定向强化 | PR #30，行为评估 `4 / 4 PASS`、断言 `21 / 21 PASS` |
| 2026-08-24 | 完成首轮 Consumer Experiment 收敛 | Issue #18 `completed` |
| 2026-08-24 | 建立通用 Project Roadmap 规则 | PR #32，行为评估 `3 / 3 PASS`、断言 `16 / 16 PASS` |
| 2026-08-26 | 明确 Existing Consumer baseline upgrade 生命周期 | PR #34 |
| 2026-08-26 | 完成跨 Repository 授权与异步执行闭环强化 | PR #35，行为评估 `4 / 4 PASS`、断言 `20 / 20 PASS` |
| 2026-08-28 | 完成验证证据边界定向强化 | PR #37，行为评估 `6 / 6 PASS`、断言 `35 / 35 PASS` |
| 2026-08-28 | 完成 Human Review、外部媒体输入和后继提交证据强化 | PR #38，行为评估 `4 / 4 PASS`、断言 `25 / 25 PASS` |
| 2026-08-31 | 完成共享外部资源并发与释放边界强化 | PR #40，行为评估 `4 / 4 PASS`、断言 `25 / 25 PASS` |
| 2026-09-01 | 明确配置责任与已有能力复用边界 | PR #41，行为评估 `4 / 4 PASS`、断言 `25 / 25 PASS` |
| 2026-09-01 | 增加 Karpathy Skills 定向研究并确认“工程纪律可主动研究、无需机械 Skill 化” | PR #42，集成提交 `e1f56238f95a75d95a87b1ad510587d770ae4a63` |
| 2026-09-02 | 建立主动工程能力演进架构并完成 Phase 1 / Phase 2 | PR #43，集成提交 `1eb729333b4aa239dfbb1906b623b61e7c1524a9` |
| 2026-09-02 | 完成 WI-01 工程纪律范围设计并确定首批两个研究方向 | PR #44，集成提交 `070cbb448118a6ee0494063c2d2c8ae689bfb5f3` |
| 2026-09-02 | 完成 WI-02 实现最小化工程纪律 Research / Candidate Design | PR #45，集成提交 `710ebcbf32d1222c4578c4e2fffe90408070e3d8` |
| 2026-09-02 | 完成 WI-03 精准修改工程纪律 Research / Candidate Design | PR #46，集成提交 `350e6607bae6101869d97903b56993820ba73265` |
| 2026-09-02 | 冻结 Engineering Capability Foundation v1 有限完成边界 | PR #47，F1～F5 与范围冻结规则进入项目权威 |
| 2026-09-02 | 正式集成首批两个 Engineering Discipline 并关闭 F1 / WI-03V | PR #48，集成提交 `6130d7251d81bbfc9f13b2dd827b6a40dfd09076`；Fresh Runtime `13 / 13 PASS`、断言 `62 / 62 PASS` |
| 2026-09-02 | 建立 Technology Profile / Verification Profile 最小契约并关闭 F2 / WI-04 | PR #49，集成提交 `16151149ab52211e266839a110fc9a3c73415623` |
| 2026-09-02 | 正式集成 Vue 3 + TypeScript Technology Profile 并关闭 F3 / WI-05 | PR #50，集成提交 `b80b2b1b7cea38eed0aef9807879e2a0d56afd2f`；Capability Eval `9 / 9 PASS`、断言 `41 / 41 PASS` |

## 当前证据基线

- 当前阶段：**Engineering Capability Expansion & Method Evolution**；
- 当前有限里程碑：**Engineering Capability Foundation v1**；
- 当前已集成基线：`master@b80b2b1b7cea38eed0aef9807879e2a0d56afd2f`；
- Skill Inventory：8 个 Core Skills、1 个 Platform-specific Skill；
- Phase 1 — 演进路线重构：已完成；
- Phase 2 — Engineering Capability Architecture：已完成；
- Phase 3 — Engineering Discipline Formalization：已完成；
- F1 / WI-03V：已完成；
- `docs/architecture/engineering-disciplines.md` 已成为首批 Engineering Discipline 当前规范入口；
- Implementation Minimality & Speculative Complexity Control：已正式集成；
- Surgical Change & Diff Scope Control：已正式集成；
- PR #48 Targeted Eval：13 个场景、62 个 assertions 全部 PASS；
- `execute-unit` 以薄规则消费两个 Discipline，没有新增独立 Skill，没有改变 one-unit、Stage Return、Human Escalation、Completion Evidence 或 Integration Boundary；
- F2 / WI-04 — Technology Profile 最小契约：已完成；
- `docs/architecture/technology-profile-contract.md` 与 `docs/technology-profiles/` 实例入口已由 PR #49 正式集成；
- F3 / WI-05 — Vue 3 + TypeScript Technology Profile：**已完成**；
- `docs/technology-profiles/vue3-typescript.md` 已由 PR #50 正式进入当前 Repository Authority；
- PR #50 Capability Eval：`C-VTS-01`～`C-VTS-09` 共 `9 / 9 PASS`、`41 / 41 assertions PASS`；
- 受测 Profile 语义 Blob：`999911e83b23389d16f9cbbadeb4d5c29f56de75`；
- Eval 结果包 SHA-256：`abf788b5e51db9fdc145d73dd6eafc16a99a6d3417dbd81b0aa00e538e22a088`；
- Vue 3.6 RC / Vapor Mode、Element Plus、第二个 Technology Profile、Task-oriented Skill 均未进入 Foundation v1 当前范围；
- **当前 F4 — Existing Consumer Adoption：Pending Consumer Execution**；
- F4 执行边界与 Evidence 要求见 `tasks/plans/20260902/03-foundation-v1-consumer-adoption-handoff.md`；
- F4 的 Consumer 文件、Branch、PR、Workflow 和真实 Feature 实施由 Consumer 自己的项目会话与 Repository Authority 执行；`agentic-dev` 项目工作不直接修改 Consumer；
- 首轮 Greenfield Consumer Experiment：已完成并关闭 Issue #18；
- Existing Consumer 继续演进实验：Issue #33 当前仍为 `open`；
- Issue #33 已经形成多轮有效证据，并推动 PR #34、#35、#37、#38、#40、#41 的定向强化；
- Issue #33 后续是否关闭可以按其自身实验总结独立处理，不再阻塞 Foundation v1；
- `dygapp/jilinjobs-cms` 继续作为 Reference / Integration Consumer，并作为 Foundation v1 一次受控 Consumer Adoption 的优先候选。

上述提交和 Issue 是历史证据锚点，不要求后续工作永久固定使用这些静态版本。新的研究、评估或 Consumer Adoption 开始时，必须记录当时实际使用的精确 baseline。

## 当前核心目标

当前核心目标是：

> **完成 Engineering Capability Foundation v1 的剩余两个阶段，并在预先定义的完成边界处正式关闭本轮工程能力基础建设，而不是持续增加新的 Discipline、Profile、Skill 或 Runtime 范围。**

当前剩余阶段为：

1. **F4 — 一次 Existing Consumer Adoption：当前（Pending Consumer Execution）**；
2. **F5 — Foundation v1 Closure：待开始**。

已完成：

- F1 — 首批 Engineering Discipline 正式化；
- F2 — Technology Profile 最小契约；
- F3 — Vue 3 + TypeScript Technology Profile。

范围冻结规则保持不变：

- Foundation v1 的首批 Engineering Discipline 固定为两个，现已完成；
- Foundation v1 的 Technology Profile 固定为一个：Vue 3 + TypeScript，现已完成；
- 新增 Skill 数量不是 Foundation v1 完成指标；
- Runtime / Distribution 不属于 Foundation v1 Completion Gate。

完整规则见 `docs/project/engineering-capability-foundation-v1.md`。

当前阶段继续避免四种极端：

1. **闭门等待型演进**：只有 Consumer 再次踩坑才允许研究和建设能力；
2. **机械扩张型演进**：看到一个框架、一个外部 Skill 或一条最佳实践就立即新增 Skill；
3. **研究即规范型演进**：Research / Candidate Design 一完成，就在没有 Draft / Targeted Eval 的情况下直接提升为长期权威；
4. **无限扩展型演进**：不断把新发现的有价值方向追加为当前里程碑前置条件，导致完成定义持续后移。

## 分阶段实施计划

### Phase 1 — 演进路线重构

目标：结束“Consumer 持续验证作为唯一核心目标”的阶段定位，明确新的主动演进模型和长期 Track。

状态：**已完成**。

### Phase 2 — Engineering Capability Architecture

目标：建立工程能力分层，明确 Method、Engineering Discipline、Technology Profile、Verification Profile、Task-oriented Skill、Runtime Adapter 与 Consumer Project Rule 的职责边界。

状态：**已完成**。

### Phase 3 — Engineering Discipline Formalization

目标：把已经完成 Research / Candidate Design 的首批两个 Discipline 按现行能力生命周期正式验证和集成。

结果：

- 两个 Discipline 已完成 Architecture Fit、Draft、Fresh Runtime Targeted Eval、AI Review 与 Integration；
- PR #48 已合并；
- Foundation v1 没有增加第三个 Engineering Discipline。

状态：**已完成**。

### Phase 4 — Technology Profile Foundation

目标分两步：

1. WI-04：Technology Profile / Verification Profile 最小契约已由 PR #49 实际集成；
2. WI-05：唯一代表性 Vue 3 + TypeScript Profile 已完成 Research、Architecture Fit、Draft、Verification Profile、Fresh Runtime Targeted Eval、最终 AI Review 和 Integration。

PR #50 Capability Eval 为 `9 / 9 PASS`、`41 / 41 assertions PASS`，集成提交为 `b80b2b1b7cea38eed0aef9807879e2a0d56afd2f`。

Element Plus、Spring Framework / Spring Boot / Spring MVC、Gradle 以及其他 Technology Profile 全部进入 Post-v1 Backlog，不属于当前完成条件。

状态：**已完成**。

### Phase 5 — Consumer Adoption

目标：只执行一次受控 Existing Consumer Adoption，验证正式 Discipline、Vue 3 + TypeScript Profile 与 Consumer-local Authority 的组合。

Consumer Adoption 出现的 Blocking / Medium 通用问题应修复并重新验证；Low / Future Improvement 可以进入 Post-v1 Backlog，不要求在当前里程碑继续扩展。

执行边界：

- `agentic-dev` 项目会话不直接修改 Consumer Repository；
- Consumer 当前独立任务先按其自身项目流程完成，不因 F4 被打断；
- 后续 baseline upgrade、真实 Vue 3 + TypeScript Unit、CI / Browser / Visual Evidence 和 Consumer PR 由 Consumer 自己的项目会话执行；
- `agentic-dev` 仅接收 Adoption Evidence、分类通用 Finding，并在确有 Blocking / Medium General Finding 时修改自身能力后重新验证。

当前 Handoff：

`tasks/plans/20260902/03-foundation-v1-consumer-adoption-handoff.md`

状态：**当前（Pending Consumer Execution）**。

### Phase 6 — Foundation v1 Closure

目标：执行 Closure Review，确认 Discipline、Profile、Verification 和一次 Consumer Adoption 已形成完整能力链，并正式标记 Foundation v1 完成。

Closure 后才决定下一项目里程碑。Task-oriented Skill 扩展、第二个 Technology Profile、Runtime Adapter 与 Distribution 不自动续接为当前任务。

状态：**下一步**。

## 下一步工作

1. **等待 Consumer 自己的项目会话完成当前正在进行的独立任务。**
   - 当前 `agentic-dev` 项目工作不修改 Consumer Repository；
   - 不触发、更新或接管 Consumer 正在执行的 PR / Workflow；
   - 不因为等待而启动第二个 Consumer 或扩大 Foundation v1 范围。
2. **由 Consumer 项目会话按 F4 Handoff 执行一次受控 Existing Consumer Adoption。**
   - 比较 Consumer 实际旧 baseline 与 `agentic-dev@b80b2b1b7cea38eed0aef9807879e2a0d56afd2f`；
   - 选择一个真实、边界明确、实际触达 Vue 3 + TypeScript 的当前工作单元；
   - 按 Consumer Repository Authority 固化必要 baseline upgrade 和本地规则；
   - 取得与 Unit 声明匹配的 Current Evidence；
   - 向 `agentic-dev` 回传最小充分的 Adoption Evidence / Finding Classification。
3. **收到 Consumer Evidence 后在 `agentic-dev` 完成 F4 Evidence Review。**
   - Blocking / Medium General Finding：在 `agentic-dev` 修复并重新验证；
   - Consumer-local Finding：不错误上升为通用规则；
   - Low / Future Improvement：进入 Post-v1 Backlog，不阻塞 F4。
4. **F4 关闭后立即进入 F5：Foundation v1 Closure Review。**

当前 F4 Handoff：

`tasks/plans/20260902/03-foundation-v1-consumer-adoption-handoff.md`

Foundation v1 总体范围冻结和完成条件见：

`docs/project/engineering-capability-foundation-v1.md`

WI-05 计划保留为已完成阶段记录：

`tasks/plans/20260902/02-vue-typescript-profile.md`

原总体实施计划保留为历史协调记录：

`tasks/plans/20260901/01-engineering-capability-expansion.md`

## Issue #33 的后续角色

Issue #33 继续作为 Existing Consumer continuous-evolution experiment 的历史与剩余证据跟踪，不再承担 `agentic-dev` 下一阶段路线的总控职责。

如果该实验已经达到原始 Goal，可以独立形成 Final Summary 并决定是否关闭；即使保持 `open`，也不阻止 Foundation v1 的主动建设和收敛。

Foundation v1 的 Consumer Adoption 应围绕正式 Discipline / Profile 的采用建立清晰目标，不无限延长 Issue #33 来承载所有后续演进。

## 新上下文恢复顺序

新的 `agentic-dev` 工作上下文应：

1. 读取根目录 `AGENTS.md`；
2. 读取本文，确认当前阶段、当前有限里程碑和下一步工作；
3. 读取 `docs/project/engineering-capability-foundation-v1.md`，确认 F1～F5、范围冻结规则和当前 Completion Scope；
4. 读取当前 GitHub `master`，验证是否存在晚于本文的新集成状态；
5. 涉及工程能力分层时读取 `docs/architecture/engineering-capability-architecture.md`；
6. 当前 F4 读取 `docs/architecture/engineering-disciplines.md`、`docs/architecture/technology-profile-contract.md`、`docs/technology-profiles/vue3-typescript.md` 与 `tasks/plans/20260902/03-foundation-v1-consumer-adoption-handoff.md`；
7. 不从 `agentic-dev` 项目会话直接修改 Consumer Repository；Consumer Adoption 的实施应在 Consumer 自己的项目会话中恢复其 Repository Authority 后执行；
8. 收到 Consumer Evidence 后，只读取完成 F4 Evidence Review 所需的精确 Consumer 事实与证据，不把 Consumer 项目状态复制成 `agentic-dev` Authority；
9. 涉及 Skill 时继续读取 `skill-architecture.md`、`skill-contracts.md` 与相关 Skill；
10. 不依赖历史聊天或个人记忆补充未固化的项目事实。

## 更新触发条件

出现以下任一情况时，应更新本文：

- 一个项目级 Phase、Track 或 Foundation v1 的 F1～F5 完成、取消或被替代；
- 当前阶段、当前里程碑或核心目标改变；
- Technology Profile Contract 或 Vue 3 + TypeScript Profile 进入正式基线；
- Foundation v1 Consumer Adoption 产生会改变当前完成定义的重要证据；
- Foundation v1 Closure 完成；
- 当前路线与 GitHub `master`、Issue、PR 或评估证据不再一致。

普通局部实现、单个 Execution Unit 状态变化或 Post-v1 Backlog 新增候选，不要求更新本文，也不得据此扩大当前 Foundation v1 Completion Scope。
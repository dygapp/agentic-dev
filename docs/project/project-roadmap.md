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

因此当前阶段为：

> **Engineering Capability Expansion & Method Evolution（工程能力扩展与方法演进）**

本阶段从“主要等待 Consumer 暴露问题后定向修补”，转向“主动研究成熟外部实践、形成工程能力、建立专项评估，再推动 Consumer 采用和纠偏”。

本阶段首个有限里程碑：

> **Engineering Capability Foundation v1（工程能力基础版 v1）**

已经完成固定 F1～F5 闭环。完成定义与历史范围冻结见：

- `docs/project/engineering-capability-foundation-v1.md`
- `docs/project/engineering-capability-foundation-v1-closure.md`

Foundation v1 完成后**不自动启动下一里程碑**。下一项工程能力扩展必须通过新的 Project Roadmap / Milestone Decision 显式选择。

## 总体演进路线

| 路线 | 状态 | 当前目标 |
|---|---|---|
| 建立通用 AI Agent 开发方法基线 | 已完成 | Method、Principles 与第一批 Skill 设计、契约形成稳定基线 |
| 完成第一批核心 Skill 工程 | 已完成 | 8 个 Core Skills 实现、Packaging Hardening、Fresh Runtime Eval 与 Closure Review 完成 |
| 完成首轮方法与 Skill 实证验证 | 已完成 | Greenfield Experiment 已完成；Existing Consumer 多轮证据已足以支持阶段切换，Issue #33 独立收尾 |
| Track A — Method Consolidation | 当前 | Core Method 进入稳定维护；只在高质量证据揭示通用生命周期或权威缺口时定向修改 |
| Track B — Engineering Discipline Expansion | 已完成 | Foundation v1 首批两个 Engineering Discipline 已通过 Targeted Eval 并由 PR #48 正式集成 |
| Track C — Technology Engineering Profiles | 已完成 | Technology Profile Contract 由 PR #49 集成；唯一代表性 Vue 3 + TypeScript Profile 已由 PR #50 正式集成 |
| Track D — Consumer Adoption | 已完成 | Issue #52 F4 Evidence Review PASS；唯一 Existing Consumer Adoption 已完成且 Blocking / Medium General Finding = 0 |
| Track E — Engineering Skills | 条件性后续 | Post-v1 候选；只有新的 Milestone Decision 证明存在独立稳定任务职责时才进入 |
| Track F — Runtime / Distribution | 条件性后续 | Post-v1 候选；Runtime Adapter、Marketplace、Plugin Bundle、Controller 与统一安装器不自动续接 |

**Engineering Capability Foundation v1：Completed。**

当前没有被自动选择的下一扩展 Track；在新的 Milestone Decision 前，只继续 Track A 的稳定维护和既有 Issue 的独立收尾。

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
| 2026-09-03 | 建立 F4 Existing Consumer Adoption Handoff | PR #51，集成提交 `18a48bcada8b4eeb0e6d8c3043b21c54aa8e492b` |
| 2026-09-03 | 完成 F4 Existing Consumer Adoption Evidence Review | Issue #52；Consumer PR #49 为唯一 Adoption Unit，Blocking / Medium General Finding = `0 / 0` |
| 2026-09-03 | Engineering Capability Foundation v1 Closure Review PASS | `docs/project/engineering-capability-foundation-v1-closure.md`；F1～F5 全部满足冻结完成条件 |

## 当前证据基线

- 当前阶段：**Engineering Capability Expansion & Method Evolution**；
- **Engineering Capability Foundation v1：Completed**；
- Foundation v1 起点：`350e6607bae6101869d97903b56993820ba73265`；
- Foundation v1 正式 Capability baseline：`b80b2b1b7cea38eed0aef9807879e2a0d56afd2f`；
- F4 Handoff 集成基线：`18a48bcada8b4eeb0e6d8c3043b21c54aa8e492b`；
- Foundation v1 最终集成 commit 由包含 Closure Report 的当前集成 commit 在 GitHub Commit History 中唯一确定，不在 Roadmap 复制瞬时 merge SHA；
- Skill Inventory：8 个 Core Skills、1 个 Platform-specific Skill；Foundation v1 没有因数量目标增加 Task-oriented Skill；
- F1 / WI-03V：已完成；PR #48 Targeted Eval `13 / 13 PASS`、`62 / 62 assertions PASS`；
- F2 / WI-04：已完成；Technology Profile / Verification Profile Contract 已集成；
- F3 / WI-05：已完成；Vue 3 + TypeScript Profile 已集成，Capability Eval `9 / 9 PASS`、`41 / 41 assertions PASS`；
- F4 / WI-08：已完成；Issue #52 F4 Evidence Review PASS；
- F4 Reference Consumer：`dygapp/jilinjobs-cms`；唯一 Adoption Unit 为 Consumer PR #49；
- F4 Blocking / Medium General Finding：`0 / 0`；
- Consumer post-adoption PR #52 作为补充证据验证 Evidence Claim granularity，不计为第二次 Adoption，不触发新 Method / Contract；
- F5 Closure Review：PASS；Blocking / Medium Closure Finding：`0 / 0`；
- 从 Foundation v1 起点到 F4 Handoff 集成基线的 compare 没有 `docs/method/*` 变化，Core Method 未被技术能力扩展不必要改写；
- Vue 3.6 RC / Vapor Mode、Element Plus、第二个 Technology Profile、新 Task-oriented Skill、Runtime / Distribution 均未进入 Foundation v1 Completion Scope；
- WI-06、WI-07、WI-09 保持 Post-v1 Backlog；
- 首轮 Greenfield Consumer Experiment：已完成并关闭 Issue #18；
- Existing Consumer continuous-evolution experiment Issue #33 仍可独立收尾，但不阻塞 Foundation v1，也不自动成为下一里程碑。

Foundation v1 的最终 Closure Evidence：

`docs/project/engineering-capability-foundation-v1-closure.md`

## 当前核心目标

Foundation v1 已在预先定义的完成边界处收敛。

当前不自动继续第二个 Technology Profile、Task-oriented Skill、Runtime / Distribution 或新的 Engineering Discipline。

> **当前没有已批准的下一工程能力里程碑。**

在新的 Milestone Decision 前：

- Track A — Method Consolidation 保持稳定维护；
- Issue #33 可以按其原始目标独立形成 Final Summary / Closure；
- WI-06、WI-07、WI-09 与其他 Post-v1 候选只作为路线输入，不构成当前工作承诺；
- 新外部研究、Consumer Finding 或技术候选可以记录，但不能静默提升为当前 Completion Scope。

下一里程碑必须显式回答：

1. 现在最值得扩展的是**能力覆盖面**、**任务执行能力**还是**运行时交付能力**；
2. 是否已有足够当前证据支持进入该方向；
3. 新里程碑的有限完成定义是什么；
4. 哪些相邻候选必须明确保持 Backlog，避免再次形成无限扩展。

## Foundation v1 分阶段结果

### Phase 1 — 演进路线重构

状态：**已完成**。

### Phase 2 — Engineering Capability Architecture

状态：**已完成**。

### Phase 3 — Engineering Discipline Formalization

状态：**已完成**。

结果：首批两个 Discipline 完成 Architecture Fit、Draft、Fresh Runtime Targeted Eval、AI Review 与 Integration，没有增加第三个 Discipline。

### Phase 4 — Technology Profile Foundation

状态：**已完成**。

结果：Technology Profile Contract 与唯一代表性 Vue 3 + TypeScript Profile 已集成；没有自动继续第二个 Profile。

### Phase 5 — Consumer Adoption

状态：**已完成**。

结果：

- `dygapp/jilinjobs-cms` 完成一次受控 Existing Consumer Adoption；
- Consumer PR #49 是 Foundation v1 唯一 Adoption Unit；
- Issue #52 Evidence Review PASS；
- Blocking / Medium General Finding：`0 / 0`；
- Consumer-local Finding 没有错误上升为 `agentic-dev` 通用规则；
- post-adoption PR #52 只作为补充 Evidence，不扩展 F4 数量边界。

### Phase 6 — Foundation v1 Closure

状态：**PASS / Completed**。

Closure 结果：

- Core Method 不必要变化：0；
- Engineering Capability Architecture：已真实承载 Discipline、Profile、Verification、Consumer Adoption；
- 首批两个 Discipline：Integrated + Targeted Eval PASS；
- Technology Profile Contract：Integrated；
- Vue 3 + TypeScript Profile：Integrated + Capability Eval PASS；
- Existing Consumer Adoption：PASS；
- Super-skill / framework encyclopedia Skill：未形成；
- Post-v1 Backlog：与完成条件保持分离；
- Blocking / Medium Closure Finding：`0 / 0`。

完整 Closure Review：

`docs/project/engineering-capability-foundation-v1-closure.md`

## 下一步工作

Foundation v1 Closure 实际集成后，**不自动进入 WI-06、WI-07 或 WI-09**。

下一项工作是一次独立的 **Post-Foundation Milestone Decision**，由 Human Authority / Project Roadmap 明确选择是否进入新的有限里程碑。

可供决策的既有方向包括但不限于：

- WI-06：第二个 Technology Profile / 技术覆盖面扩展；
- WI-07：有真实重复职责后提炼 Task-oriented Skill；
- WI-09：Runtime Adapter / Distribution；
- 新 Engineering Discipline；
- 继续只做 Core Method 稳定维护，而暂不扩展新能力。

这些方向在被显式选择前都不是当前执行任务。

Tag / Release 由 Human Authority / Repository Policy 在 Closure 实际集成后按需决定，不作为本 Closure PR 的自动副作用。

Foundation v1 Closure Plan：

`tasks/plans/20260903/01-foundation-v1-closure.md`

## Issue #33 的后续角色

Issue #33 继续作为 Existing Consumer continuous-evolution experiment 的历史与剩余证据跟踪，不再承担 `agentic-dev` 路线总控职责。

如果该实验已经达到原始 Goal，可以独立形成 Final Summary 并决定是否关闭；即使保持 `open`，也不影响 Foundation v1 的 Completed 判定。

后续新的 Consumer Evidence 如需进入新的工程能力里程碑，应由新的 Roadmap / Milestone Decision 明确其职责，不能默认继续挂载到 Foundation v1。

## 新上下文恢复顺序

新的 `agentic-dev` 工作上下文应：

1. 读取根目录 `AGENTS.md`；
2. 读取本文，确认 Foundation v1 已完成且下一里程碑尚未自动选择；
3. 读取 `docs/project/engineering-capability-foundation-v1-closure.md`，确认 F1～F5 Closure Evidence；
4. 读取 `docs/project/engineering-capability-foundation-v1.md`，只在需要理解历史完成边界 / Scope Freeze 时使用；
5. 读取当前 GitHub `master`，验证是否存在晚于本文的新 Milestone Decision；
6. 如果 Human Authority 已选择新的里程碑，只加载该里程碑真正需要的 Architecture / Profile / Skill / Research；
7. 如果尚未选择新里程碑，不把 WI-06、WI-07、WI-09 或其他 Post-v1 候选自动当作当前任务；
8. Issue #33 只按其自身实验目标独立恢复，不让其覆盖当前 Project Roadmap；
9. 不依赖历史聊天或个人记忆补充未固化的项目事实。

## 更新触发条件

出现以下任一情况时，应更新本文：

- Human Authority / Repository Policy 显式选择 Foundation v1 之后的新里程碑；
- 当前阶段、核心目标或 Track 状态发生实质改变；
- Foundation v1 Closure 的关键 Evidence 被证明无效；
- 新的通用 Method / Architecture Finding 需要改变当前稳定维护状态；
- Issue #33 的独立关闭结果对项目级路线产生真实影响。

普通局部实现、Consumer-local Finding、单个 Post-v1 候选或新外部研究，不要求更新本文，也不得据此静默启动新的当前里程碑。
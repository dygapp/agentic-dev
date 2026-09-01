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

## 总体演进路线

| 路线 | 状态 | 当前目标 |
|---|---|---|
| 建立通用 AI Agent 开发方法基线 | 已完成 | Method、Principles 与第一批 Skill 设计、契约形成稳定基线 |
| 完成第一批核心 Skill 工程 | 已完成 | 8 个 Core Skills 实现、Packaging Hardening、Fresh Runtime Eval 与 Closure Review 完成 |
| 完成首轮方法与 Skill 实证验证 | 已完成 | Greenfield Experiment 已完成；Existing Consumer 多轮证据已足以支持阶段切换，Issue #33 独立收尾 |
| Track A — Method Consolidation | 当前 | Core Method 进入稳定维护；只在高质量证据揭示通用生命周期或权威缺口时定向修改 |
| Track B — Engineering Discipline Expansion | 下一步 | 主动研究并提炼最小实现、Review、Testing、Refactoring、Performance、Security、Dependency、API Evolution 等跨技术栈工程纪律 |
| Track C — Technology Engineering Profiles | 下一步 | 建立 Technology Profile / Verification Profile 机制，并逐步研究 Vue 3、TypeScript、Element Plus、Spring、Gradle 等当前高价值技术栈 |
| Track D — Engineering Skills & Verification | 下一步 | 从稳定工程过程提炼 Task-oriented Skill，建立对应专项评估，不按框架名称机械创建 Skill |
| Track E — Adoption / Runtime / Distribution | 下一步 | 推动 Existing Consumer baseline upgrade、运行时适配和后续分发能力；不要求立即实现 Marketplace 或统一 Controller |

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

## 当前证据基线

- 当前阶段：**Engineering Capability Expansion & Method Evolution**；
- 当前阶段切换起点：`master@e1f56238f95a75d95a87b1ad510587d770ae4a63`；
- Skill Inventory：8 个 Core Skills、1 个 Platform-specific Skill；
- 首轮 Greenfield Consumer Experiment：已完成并关闭 Issue #18；
- Existing Consumer 继续演进实验：Issue #33 当前仍为 `open`；
- Issue #33 已经形成多轮有效证据，并推动 PR #34、#35、#37、#38、#40、#41 的定向强化；
- Issue #33 后续是否关闭可以按其自身实验总结独立处理，不再阻塞工程能力扩展阶段；
- `dygapp/jilinjobs-cms` 继续作为 Reference / Integration Consumer，可用于验证新的 `agentic-dev` baseline、Profile、Skill 与验证能力，但不承担唯一创新来源职责；
- PR #42 已证明 Research 可以在不改变 Method / Skill Inventory 的情况下主动引入新的工程纪律候选视角。

上述提交和 Issue 是历史证据锚点，不要求后续工作永久固定使用这些静态版本。新的研究、评估或 Consumer Adoption 开始时，必须记录当时实际使用的精确 baseline。

## 当前核心目标

当前核心目标是：

> **在保持 Core Method 稳定和既有权威边界的前提下，建立可主动演进的工程能力体系；从成熟外部实践中提炼 Engineering Discipline、Technology Profile、Verification Profile、Task-oriented Skill 与 Runtime Adapter，并通过专项评估和 Consumer Integration 双重验证持续完善。**

当前阶段特别避免两种极端：

1. **闭门等待型演进**：只有 Consumer 再次踩坑才允许研究和建设能力；
2. **机械扩张型演进**：看到一个框架、一个外部 Skill 或一条最佳实践就立即新增 Skill。

正确方向是：成熟证据可以主动推动能力建设，但必须经过分层、边界设计、Targeted Eval、AI Review 和仓库权威固化。

## 分阶段实施计划

### Phase 1 — 演进路线重构

目标：结束“Consumer 持续验证作为唯一核心目标”的阶段定位，明确新的主动演进模型和五条长期 Track。

产物：

- 更新 `AGENTS.md`；
- 更新本文；
- 更新 README / Skill 入口中的当前阶段表达。

状态：**已完成**。

### Phase 2 — Engineering Capability Architecture

目标：建立工程能力分层，明确 Method、Engineering Discipline、Technology Profile、Verification Profile、Task-oriented Skill、Runtime Adapter 与 Consumer Project Rule 的职责边界。

产物：

- `docs/architecture/engineering-capability-architecture.md`；
- 对齐 `skill-architecture.md` 的新 Skill 准入证据规则；
- 明确能力生命周期和评估要求。

状态：**已完成**。

### Phase 3 — Engineering Discipline Research

目标：从成熟外部项目、官方工程实践和既有 Research 中主动研究跨技术栈工程纪律。

首批优先方向：

- Implementation Minimality；
- Surgical Change / Diff Scope；
- Code Review；
- Testing；
- Refactoring；
- Dependency Management；
- API Evolution；
- Performance / Security / Error Handling。

每个方向应先 Research，再判断是否属于现有 Embedded Discipline 的补强、独立规范，或真正需要 Skill 化。

状态：**下一步**。

### Phase 4 — Technology Profile Research

目标：先建立 Technology Profile 通用结构，再逐项研究技术栈，不在一个大任务中一次完成全部框架。

建议首批顺序：

1. Vue 3 + TypeScript；
2. Element Plus；
3. Spring Framework / Spring Boot / Spring MVC；
4. Gradle。

每个技术研究应优先使用官方权威资料，再以成熟开源项目和工程实践补充，并明确版本、适用边界、默认规则、常见误用和 Verification Profile。

状态：**后续阶段**。

### Phase 5 — Engineering Skills & Targeted Eval

目标：从 Discipline / Profile 中识别真正具有稳定过程的任务型能力，并建立专项行为评估。

候选形态可以包括：

- frontend component change；
- frontend visual convergence；
- Spring web endpoint change；
- database schema change；
- dependency / framework upgrade。

这些只是候选任务形态，不表示已经决定创建对应 Skill。

状态：**后续阶段**。

### Phase 6 — Consumer Adoption & Runtime Evolution

目标：推动 Reference Consumer 主动升级并采用新能力，同时逐步建设运行时适配与分发方案。

主要验证：

- Existing Consumer baseline upgrade 是否能正确选择新 Profile / Skill；
- 通用 Profile 与 Consumer-local Authority 是否能正确组合；
- 新能力是否真实改善实现和验证质量；
- 是否存在需要回写 `agentic-dev` 的冲突或缺口；
- Codex / Claude Code / Cursor 等 Runtime 是否需要独立 Adapter。

状态：**后续阶段**。

## 下一步工作

当前 Phase 1 与 Phase 2 完成并集成后，按以下顺序继续：

1. 对 Engineering Discipline Expansion 做一次范围设计，避免一次研究全部纪律；
2. 选择第一批 1～2 个高价值纪律完成独立 Research → Candidate → Eval 设计闭环；
3. 建立 Technology Profile 的最小通用结构和质量门槛；
4. 进入 Vue 3 + TypeScript 的第一项 Technology Profile 研究；
5. 完成一项 Profile 后再判断是否进入 Element Plus 或 Spring，不把所有技术栈塞入同一执行任务。

## Issue #33 的后续角色

Issue #33 继续作为 Existing Consumer continuous-evolution experiment 的历史与剩余证据跟踪，不再承担 `agentic-dev` 下一阶段路线的总控职责。

如果该实验已经达到原始 Goal，可以独立形成 Final Summary 并决定是否关闭；即使保持 `open`，也不阻止 Engineering Capability Expansion 的主动研究与建设。

未来新的能力采用实验可以复用 `jilinjobs-cms`，但应围绕具体 Profile、Skill 或 baseline upgrade 建立清晰目标，而不是无限延长一个总 Experiment 来承载所有后续演进。

## 新上下文恢复顺序

新的 `agentic-dev` 工作上下文应：

1. 读取根目录 `AGENTS.md`；
2. 读取本文，确认当前阶段、演进 Track 和下一步工作；
3. 读取当前 GitHub `master`，验证是否存在晚于本文的新集成状态；
4. 涉及工程能力分层时读取 `docs/architecture/engineering-capability-architecture.md`；
5. 涉及 Skill 时继续读取 `skill-architecture.md`、`skill-contracts.md` 与相关 Skill；
6. 涉及具体研究时只加载相关 Research / Profile / Eval，不默认加载所有技术资料；
7. 进入 Consumer Adoption 时切换到 Consumer Repository 并读取其当前默认分支与 Repository Authority；
8. 不依赖历史聊天或个人记忆补充未固化的项目事实。

## 更新触发条件

出现以下任一情况时，应更新本文：

- 一个项目级 Phase 或 Track 完成、取消或被替代；
- 当前阶段或核心目标改变；
- 首批 Engineering Discipline / Technology Profile 进入正式基线；
- 新 Skill 或 Runtime Adapter 进入正式 Inventory；
- Consumer Adoption 产生会改变总体演进方向的重要证据；
- 当前路线与 GitHub `master`、Issue、PR 或评估证据不再一致。

普通局部实现、单个 Execution Unit 状态变化或没有项目级影响的修订，不要求更新本文。

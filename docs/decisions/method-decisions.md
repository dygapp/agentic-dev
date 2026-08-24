# 方法决策记录

**状态：** Baseline v0.1

本文轻量记录研究与收敛阶段已经确认的主要方法决策。

只有真正需要独立 Trade-off 记录的事项，后续再升级为单独 ADR。

## D-001 — 停止继续横向扩展参考框架

**决定：**

当前对照样本固定为：

- `mattpocock/skills`
- `github/spec-kit`
- `obra/superpowers`

**原因：**

核心方法维度已经得到交叉验证。继续增加框架的边际收益较低，并容易重新陷入无法收敛的比较。

## D-002 — 采用 Method-first 架构

**决定：**

先定义开发方法，再由 Skills 实现。

**不采用：**

先写一组 `SKILL.md`，再从 Skill 反推方法。

## D-003 — Workflow Control 必须显式

**决定：**

不创建从 Clarification 一路自动执行到 Integration 的超级 Skill。

**原因：**

小型、可组合 Skills 能保持阶段转换可观察，并保留 Human / Controller 的流程控制权。

## D-004 — WHAT / WHY 与 HOW 分离

**决定：**

Specification 负责 Required Behavior；Technical Plan 负责 Implementation Design。

## D-005 — Technical Planning 按需触发

**决定：**

只有存在真实技术不确定性或跨 Unit 协调价值时，才创建长期 Technical Plan。

**不采用：**

每次修改都固定生成 `plan.md`。

## D-006 — Execution Unit 作为逻辑工作原子

**决定：**

实施工作拆成纵向、可独立验证、Context-fit 的 Execution Units。

## D-007 — Durable Work Item 以行为为中心

**决定：**

Exact File Paths 和 Low-level Edit Instructions 不作为长期 Execution Unit 的默认必填字段。

**原因：**

这些细节容易过时，更适合查看当前仓库后通过 JIT Plan 生成。

## D-008 — Technical Plan 与 JIT Execution Plan 分离

**决定：**

Durable Design 与 Transient Construction Planning 是不同 Artifact，生命周期不同。

## D-009 — 增加自动 Readiness Gate

**决定：**

实施前统一检查 Specification、Design、Execution Coverage 和 Governance。

## D-010 — Evidence Before Completion Claims

**决定：**

“Build Pass”“Tests Pass”“Feature Complete”等声明必须基于当前证据。

## D-011 — Verification、Review、Convergence 分离

**决定：**

- Verification：确定当前事实；
- Review：判断局部实现质量与符合性；
- Convergence：判断 Feature 整体是否符合 Intent。

## D-012 — 每个 Execution Unit 使用 Fresh Context

**决定：**

执行不得依赖此前未持久化的 reasoning history。

实现机制不限定为某一种产品能力。

## D-013 — 使用 Progressive Disclosure

**决定：**

只加载当前工作需要的 Authority 和 Code。

**不采用：**

给每个执行 Agent 预加载全部项目知识。

## D-014 — Ambiguity 本身不自动触发人工介入

**决定：**

Human Escalation 依据 Authority、Impact、Reversibility。

简化为：

> Human owns irreversible intent; AI owns reversible execution.

## D-015 — Defect 采用独立 Workflow

**决定：**

缺陷默认采用：

```text
Reproduce
→ Diagnose
→ Hypothesis
→ Evidence
→ Minimal Fix
→ Regression Verification
```

## D-016 — 通用生命周期结束于 Ready to Integrate

**决定：**

Merge、Push、Release、Deploy 和 Destructive Cleanup 由 Project Policy 或 Human Authority 控制。

## D-017 — 不要求 Stage 与 File 一一对应

**决定：**

Artifact 是否持久化取决于知识价值，而不是 Stage 是否存在。

## D-018 — ADR 由长期架构决策按条件产生

**决定：**

Technical Planning 既消费已有 ADR，也负责判断新形成的长期技术决策（Durable Technical Decision）是否需要持久化为架构决策记录（Architecture Decision Record，ADR）。

ADR 不是新的方法阶段（Method Stage），也不是每次 Technical Planning 的固定输出。只有当技术决定需要跨越当前功能（Feature）长期约束后续工作，并且保留其选择理由、主要权衡（Trade-off）或替代关系具有持续价值时，才形成或更新 ADR。

**不采用：**

- 为每个 Technical Plan 固定生成 ADR；
- 把单个执行单元的局部实现选择记录为 ADR；
- 规定所有 Consumer 必须预建固定 `adr/` 目录或统一模板；
- 在 Execute / Debug / Converge 中静默建立长期架构约束而不回退 Technical Planning。

**原因：**

Technical Plan 主要服务当前功能与执行单元的 HOW 协调，而 ADR 服务跨功能的长期架构权威（Architecture Authority）。两者生命周期和权威用途不同；显式区分可以避免既把所有技术选择过度文档化，也避免重要架构决定只埋在阶段性计划或代码中。

## D-019 — 长期权威产物必须具备生命周期闭环

**决定：**

新增或重大修改长期权威产物时，必须能够从当前方法职责与仓库权威中确定其产生、触发、消费、持久化、更新、取代和升级责任。阶段可以识别或验证长期事实候选，但阶段转换本身不授予权威写入权限；下游执行职责发现长期事实缺失、冲突或失效时，应返回拥有该事实或决定的上游职责处理。

Domain Context 保存跨功能持续有效的业务语言与领域事实，由 Clarify Intent 识别候选、Specification 验证候选，并由 Consumer Repository Authority 指定的领域责任方确认和维护。Architecture Context 保存跨功能持续有效的架构状态，由 Technical Planning 维护；ADR 只记录其中需要长期保留背景、权衡或替代关系的重要架构决定，不等同于全部 Architecture Context。

**不采用：**

- 为每类长期权威产物新增独立方法阶段；
- 创建接管所有产物产生、更新与取代的 Artifact Management Super-skill；
- 强制 Consumer 使用固定目录、模板、文件名或审批流程；
- 让代码、测试、临时 Plan 或 Conversation History 自动把候选事实提升为长期权威。

**原因：**

只有消费者而没有 Producer、Trigger、Update 与 Supersede 等责任，会使 Fresh Agent 无法可靠判断长期事实如何产生以及哪个版本当前有效。将职责分配给拥有相应事实或决定的方法层，同时把具体载体和写入权限留给 Consumer Repository Authority，可以闭合生命周期而不引入新的流程层级或集中式超级能力。


## D-020 — 验收义务必须闭环到当前验证证据

**决定：**

切分与就绪阶段必须为规格说明中的必需行为 / 验收义务建立明确的实现责任、验证责任与计划验证证据；就绪检查必须判断这些计划验证证据是否足以证明义务；执行只能在当前证据支持当前执行单元所承担的验证义务时声明执行单元 `Completed`。

只有确实依赖多个执行单元组合状态的行为，才可以显式归属功能整体验证责任；这些义务必须由 `converge` 独立重新检查，并在缺少已执行的当前证据时阻止 `READY`。

**不采用：**

- 将实现覆盖自动视为验证覆盖；
- 用“代码完成”“测试通过”或主路径代替具体验收义务的证据责任；
- 强制每条验收义务对应一个测试、固定证据格式或特定测试层级；
- 通过新增独立 `verify-evidence` Skill 接管闭环；
- 因为前置检查增强而弱化 `converge` 的功能整体安全网。

**原因：**

真实 Consumer 实验证明，执行单元可以在主要纵向路径通过后进入 `Completed` / `Integrated`，但仍有分页、竞争排序和多类导航等已实现验收义务缺少已执行的当前证据。后续只补验证、不修改产品实现即可使功能整体 `converge` 从 `GAPS` 转为 `READY`，说明缺口位于验收责任归属、验证规划与闭环机制，而不是 Consumer 项目实现或 `converge` 职责。


## D-021 — Project Roadmap 是条件性长期项目级产物

**决定：**

当项目跨越多个里程碑、方法阶段或 Fresh Context，且仅凭功能级与任务级产物无法可靠恢复整体路线、当前阶段和下一步工作时，建立并持续维护 Project Roadmap。初始路线可以不完整，但必须区分已完成、当前、下一步、条件性与未知内容，并把具体载体交给 Consumer Repository Authority 决定。

Project Roadmap 不替代 Specification、Technical Plan、Execution Unit、临时 Coordination Plan 或项目管理排期。普通小型、一次性或单一局部工作不要求创建它。

已有且适用的 Project Roadmap 因当前工作完成、取消或取代项目级里程碑，改变当前阶段 / 核心目标、已决定的下一步顺序，或使条件性方向进入当前路线而失效时，`converge` 将其识别为 Artifact Lifecycle Gap 并路由到授权的项目治理 / Bootstrap 维护职责；`converge` 不自行规划路线或发明下一步。

**不采用：**

- 把 Project Roadmap 设为所有 Consumer 的必需文件；
- 强制固定路径、模板或完整前置路线；
- 用 README、任务清单和状态摘要并行维护多份当前路线；
- 新增 Project Roadmap Skill、项目管理阶段或 Artifact Management Super-skill；
- 让 `converge` 创建或重写项目路线。

**原因：**

在 agentic-dev 与首个 Consumer 的持续演进中，聊天记忆混乱或进入 Fresh Context 后，仅靠 README、功能产物和任务状态无法稳定恢复真正的项目阶段、当前核心目标与已决定的下一步，常常需要重新分析整个仓库且仍可能得出错误状态。通用的“只检查本次新增或重大修改产物”规则也无法发现一个根本未被修改、却已因里程碑完成而陈旧的既有路线图。

条件性 Project Roadmap 补足的是项目级发现与恢复入口；窄范围的收敛检查闭合其更新责任，同时避免把所有项目模板化或扩张 Skill 清单。

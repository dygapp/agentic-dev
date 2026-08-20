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

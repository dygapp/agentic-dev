---
id: project:post-v0.1.0-consumer-feedback-evolution-plan
type: project
status: active
---

# v0.1.0 后 Consumer 反馈演进计划

## 1. 目的

把 `agentic-dev-v0.1.0` 之后仍有效的 Consumer 反馈收敛为**小粒度、顺序执行、逐项闭环**的演进事项，避免多个问题在同一上下文中一起分析，重新形成过长上下文和过度设计。

本文件只拥有演进事项、顺序、边界和统一闭环协议；Issue / Research 提供 Evidence，Skill / Guide / governance 继续拥有各自正式语义。

## 2. 基线与约束

当前稳定 baseline：

- Release：`agentic-dev-v0.1.0`
- Integration commit：`ae8ee8032e34c046d619c719dad408edda2d2d8a`
- `skills/**` 是唯一正式 Consumer runtime product；
- Guides 只做按需 Bootstrap、方法理解和导航；
- Consumer 拥有项目事实、架构、current work、技术政策、授权和本地约束；
- 不恢复 Method selector、Rule Discovery、Capability Runtime、custom Release Builder、批量模型 grader 或多级 Gate。

所有 Issue 都必须从这个 baseline 重新解释，旧架构中的候选方案不自动进入当前设计。

## 3. 单项执行协议

一次只推进一个演进事项。当前事项收口前，不展开下一事项的详细分析或实现。

单项的详细 Evidence、方案草稿、交叉评审记录与实施过程默认由对应 GitHub Issue / PR / Git 历史承载；`docs/project/**` 只保留仍具有稳定消费者的长期 Project Authority、Roadmap、当前阶段级演进协议与必要 locator，不为每个演进事项保留一次性详细方案文档。

每个事项统一执行：

1. **证据重新分析**
   - 固定当前精确基线；
   - 读取该事项对应的 Issue / Consumer Evidence；
   - 读取当前真正受影响的 Skill / Guide / governance；
   - 区分：已被当前模型消除、仍存在、Consumer-local、未验证。
2. **必要外部研究**
   - 只研究 Repository / Consumer Evidence 无法回答的具体技术事实；
   - 无必要则显式跳过，不建立大而全研究阶段。
3. **方案收敛**
   - 明确真正的语义 owner、修改范围、Consumer-local 边界、非目标、验收条件与负向约束；
   - 先判断是否无需 Provider 修改，再判断 Guide / 现有 Skill 调整，最后才考虑新增长期能力。
4. **实施**
   - 只实现冻结范围；
   - 不为后续事项预埋 Framework、registry、metadata 或 orchestration。
5. **聚焦验证与必要复核**
   - deterministic test / bounded fixture 优先；
   - 只有当前声明需要时才使用真实 Consumer 或 Runtime Under Test；
   - 高影响 Authority / canonical Skill contract / governance 变化才进入 Fresh / Independent Review。
6. **收口**
   - 回写 Evidence 与最终 owner；
   - 更新本计划 / Roadmap / 对应 Issue；
   - 重新读取最新 baseline，再决定下一个事项是否仍成立。

Issue 中已有判断和候选方案只作为 Evidence。每个事项都必须优先问：

> 当前能力是否已经解决？是否只是 Guide / trigger / input contract 缺口？是否应留在 Consumer-local？是否真的存在稳定、跨 Consumer、可独立触发的新 procedure？

## 4. 后续演进事项

前置状态收口已经完成：Issue #172 已按 `v0.1.0` 当前产品模型明确 superseded / completed 并关闭；旧 Gate H / custom Release 路线不再是 Current responsibility。

### 演进事项 1 — Skill 与项目权威的适配边界

**来源**：Issue #58 最新 Design Authority feedback。

**问题**：重新判断 Agent 在使用现有 Skill 完成软件开发责任时，面对 Consumer 新增的合法 Current Authority，是否能够从当前 Repository 按需解析、消费、跨 Fresh Context 恢复、验证并把长期语义返回真实 owner；同时保持 Authority 与 Consumer-local Constraint 的语义边界。

**分析范围**：

- 当前 Skill 对项目权威的输入、使用和反馈回写边界；
- Guide 是否提供了足够的方法导航；
- Consumer-local Authority 是否已经足以解决问题；
- Agent / Skill / Guide / Authority / Constraint / Execution Unit 的主体与责任关系；
- Authority 在 planning / slicing / readiness / execution / debug / convergence / review 中的生命周期；
- 新的项目权威类型是否暴露真正的 Provider 通用缺口。

**非目标**：预设 Design 专用 Skill、通用 Authority registry，或把 Consumer 的 `DESIGN.md` 格式提升为 Provider 标准。

**当前工作入口**：GitHub Issue #183 — `演进事项 1：Skill 与 Consumer 项目权威适配`。Issue 承载详细冻结方案、实现前交叉评审与后续实施 Evidence；长期稳定结论回写真实 Architecture / Guide / Skill / Governance owner。

当前已完成 Evidence 重新分析、必要外部研究与第一版方案收敛。方案把问题冻结为“开放 Consumer Authority 与 canonical Skill 生命周期集成”，而不是新增 Design-specific procedure；具体实现尚未开始。实现前优先使用 GPT-6 Sol 做一次独立交叉评审，但该增强评审不作为计划成立或 Roadmap 推进的硬 Gate，是否等待 / 跳过由 Human Authority 决定。最终高影响 Skill contract 变更仍服从 Provider Fresh / Independent Review。

### 演进事项 2 — 小规模变更的执行粒度

**来源**：Issue #179。

**问题**：重新判断对于产品、需求和架构已经稳定的局部、低风险、可逆修改，当前执行路径需要保留多少正式生命周期。

重新分析必须分开：

- execution granularity；
- branch / commit / CI / PR integration policy。

当前 `v0.1.0` 已经允许 persistent Repository Runtime，并明确 PR 是否需要由 Consumer Repository / Human Authority 决定，因此不得重新建立 WebCodex-specific Method 或 GitHub transport Framework。

核心问题：

> 什么条件真正要求 Formal Execution Unit；什么情况下 bounded change + scoped verification 已经足够？

“Direct Change / Work Batch”目前只作为分析词，不预先成为 artifact type 或 Skill。

### 演进事项 3 — 多仓库项目的工作区与权威边界

**来源**：Issue #181。

**问题**：一个软件项目由多个独立 Git Repository 组成时，如何划分项目级权威、仓库级权威、工作区、跨仓工作和精确组合关系。

优先验证：

- Project Repository + nested independent repositories 是否适合作为推荐模式之一；
- root / component `AGENTS.md` 边界；
- 跨仓 Fresh Context 与权限隔离；
- Project-level work 与 repository-local implementation；
- 何时真正需要 machine-readable topology；
- 何时真正需要 exact multi-repository baseline。

首轮优先澄清方法导航和 Authority 边界，不预设 `repositories.yaml`、bootstrap orchestrator、cross-repository runtime 或 central registry。

### 演进事项 4 — 本地验证环境的资源生命周期

**来源**：Issue #180。

**问题**：持久本地 Runner 中，验证镜像、BuildKit cache 和临时 container / volume / network 怎样避免无界增长和跨项目误删。

排在演进事项 3 之后，避免提前假设 project / component identity。

重新分析先区分：

- 与 Docker 无关的通用 resource lifecycle invariant；
- Docker / BuildKit / GHCR / WSL specialization；
- 已由 `external-operation` / `github-actions-verification` 覆盖的责任；
- Consumer-local 实现政策。

当前不预设新增 Docker Skill。只有新的 Evidence 证明存在稳定、跨 Consumer 的 reusable procedure 时，才重新评估 Provider 能力。

## 5. 默认顺序

```text
演进事项 1 — Skill 与项目权威的适配边界
→ 演进事项 2 — 小规模变更的执行粒度
→ 演进事项 3 — 多仓库项目的工作区与权威边界
→ 演进事项 4 — 本地验证环境的资源生命周期
```

顺序只表达当前规划：

- 先处理 Skill 与项目权威的适配边界；
- 再收敛小规模变更的执行粒度；
- 再澄清多仓库项目的工作区与权威边界；
- 最后评估依赖项目 / 组件身份的本地验证资源治理。

每个事项收口后都可以基于新 Evidence 调整、拆分或删除后续事项。

## 6. 当前停止点

当前演进事项 1 已完成：

- 当前 baseline 与 Issue / Consumer Evidence 重新分析；
- Authority 与 Consumer-local Constraint 边界澄清；
- Agent / Skill / Guide / Authority / Constraint / Execution Unit 核心运行模型收敛；
- 开放 Consumer Authority lifecycle 方案、修改范围、验证与负向约束冻结。

演进事项 1 尚未开始 canonical Skill / Guide 的具体实现；演进事项 2～4 仍未展开。

下一责任：对 GitHub Issue #183 中的冻结方案执行实现前交叉评审；优先 GPT-6 Sol，若当前模型额度 / Runtime 不可用则由 Human Authority 明确决定是否跳过，然后才进入冻结范围实施。

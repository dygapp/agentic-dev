---
id: project:post-v0.1.0-consumer-feedback-evolution-plan
type: project
status: active
---

# v0.1.0 后 Consumer Feedback 演进计划

## 1. 目的

把 `agentic-dev-v0.1.0` 之后仍有效的 Consumer feedback 收敛为**小粒度、顺序执行、逐项闭环**的主题，避免多个问题在同一上下文中一起分析，重新形成过长上下文和过度设计。

本文件只拥有主题队列、顺序、边界和统一闭环协议；Issue / Research 提供 Evidence，Skill / Guide / governance 继续拥有各自正式语义。

## 2. 基线与约束

当前稳定 baseline：

- Release：`agentic-dev-v0.1.0`
- Integration commit：`ae8ee8032e34c046d619c719dad408edda2d2d8a`
- `skills/**` 是唯一正式 Consumer runtime product；
- Guides 只做按需 Bootstrap、方法理解和导航；
- Consumer 拥有项目事实、架构、current work、技术政策、授权和本地约束；
- 不恢复 Method selector、Rule Discovery、Capability Runtime、custom Release Builder、批量模型 grader 或多级 Gate。

所有 Issue 都必须从这个 baseline 重新解释，旧架构中的候选方案不自动进入当前设计。

## 3. 单主题执行协议

一次只激活一个主题。当前主题闭环前，不展开下一主题的详细分析或实现。

每个主题统一执行：

1. **Evidence Re-analysis**
   - 固定当前 exact baseline；
   - 读取该主题 Issue / Consumer Evidence；
   - 读取当前真正受影响的 Skill / Guide / governance；
   - 区分：已被当前模型消除、仍存在、Consumer-local、未验证。
2. **必要外部研究**
   - 只研究 Repository / Consumer Evidence 无法回答的具体技术事实；
   - 无必要则显式跳过，不建立大而全研究阶段。
3. **Design Freeze**
   - 冻结唯一 semantic owner、修改范围、Consumer-local 边界、非目标、acceptance 与 negative controls；
   - 先判断是否无需 Provider 修改，再判断 Guide / 现有 Skill 调整，最后才考虑新增长期能力。
4. **Implementation**
   - 只实现冻结范围；
   - 不为后续主题预埋 Framework、registry、metadata 或 orchestration。
5. **Focused Validation / Review**
   - deterministic test / bounded fixture 优先；
   - 只有 claim 需要时才使用真实 Consumer 或 Runtime Under Test；
   - 高影响 Authority / canonical Skill contract / governance 变化才进入 Fresh / Independent Review。
6. **Closure**
   - 回写 Evidence 与最终 owner；
   - 更新本计划 / Roadmap / 对应 Issue；
   - 重新读取最新 baseline，再决定下一个主题是否仍成立。

Issue 中的方案只作为 Evidence。每个主题都必须优先问：

> 当前能力是否已经解决？是否只是 Guide / trigger / input contract 缺口？是否应留在 Consumer-local？是否真的存在稳定、跨 Consumer、可独立触发的新 procedure？

## 4. Theme Queue

### Theme 0 — v0.1.0 状态与旧入口收口

**状态：已完成。** Issue #172 已按 `v0.1.0` 当前产品模型明确 superseded / completed 并关闭；旧 Gate H / custom Release 路线不再是 Current responsibility。

**来源**：Issue #172、当前 Roadmap、`agentic-dev-v0.1.0`。

**目标**：消除旧发布路线对 Fresh Context 的干扰。

当前已知：

- #172 仍为 Open，但 custom Release Build、Gate H 等路线已经被当前极简产品模型取代；
- Roadmap 在本计划建立前仍停留在 Integration / Release Preparation。

本主题只做状态 closure，不设计新功能。

**退出条件**：

- Project 状态明确指向 `v0.1.0`；
- #172 明确 superseded / completed 并关闭；
- 旧 Gate H / custom Release 不再被视为 current next responsibility。

### Theme 1 — Skill Authority Contract Extensibility

**来源**：Issue #58 最新 Design Authority feedback。

**问题**：Consumer 可以增加新的合法 semantic owner；当前部分 Skills 是否把 Requirement / Specification / Architecture / Technical 等 Authority 类型硬编码得过窄。

**优先检查**：

- `human-review`、`readiness-check`、`execute-unit`；
- `review-change`、`converge`；
- `clarify-intent` / `specify` 的责任返回边界。

**待验证，不预设**：

- Design Authority 是真实样本，但不等于需要 `design` Skill；
- 可能的通用缺口是 applicable semantic owner contract；
- 必须防止“开放 Authority”退化为全仓扫描或 Authority registry。

**非目标**：Design 专用 Skill、通用 Authority registry、把 Consumer 的 `DESIGN.md` 格式提升为 Provider 标准。

### Theme 2 — Lightweight Change Execution

**来源**：Issue #179。

**问题**：对于产品/需求/架构已稳定、局部、低风险、可逆的实现修改，当前路径是否仍不必要地要求 Formal Execution Unit 生命周期。

重新分析必须分开：

- execution granularity；
- branch / commit / CI / PR integration policy。

当前 `v0.1.0` 已经允许 persistent Repository Runtime，并明确 PR 是否需要由 Consumer Repository / Human Authority 决定，因此不得重新建立 WebCodex-specific Method 或 GitHub transport Framework。

核心问题：

> 什么条件真正要求 Formal Execution Unit；什么情况下 bounded change + scoped verification 已经足够？

“Direct Change / Work Batch”目前只作为分析词，不预先成为 artifact type 或 Skill。

### Theme 3 — Multi-Repository Project Workspace

**来源**：Issue #181。

**问题**：一个软件项目由多个独立 Git Repository 组成时，如何划分 Project Authority、Repository Authority、Workspace、跨仓工作和 exact composition。

优先验证：

- Project Repository + nested independent repositories 是否适合作为推荐模式之一；
- root / component `AGENTS.md` 边界；
- 跨仓 Fresh Context 与权限隔离；
- Project-level work 与 repository-local implementation；
- 何时真正需要 machine-readable topology；
- 何时真正需要 exact multi-repository baseline。

首轮优先形成 Guide / Authority 边界，不直接实现 `repositories.yaml`、bootstrap orchestrator、cross-repository runtime 或 central registry。

### Theme 4 — Local Validation Runtime Resource Lifecycle

**来源**：Issue #180。

**问题**：持久本地 Runner 中，验证镜像、BuildKit cache 和临时 container / volume / network 怎样避免无界增长和跨项目误删。

排在 Theme 3 之后，避免提前假设 project / component identity。

重新分析先区分：

- 与 Docker 无关的通用 resource lifecycle invariant；
- Docker / BuildKit / GHCR / WSL specialization；
- 已由 `external-operation` / `github-actions-verification` 覆盖的责任；
- Consumer-local 实现政策。

当前不预设新增 Docker Skill。只有新的 Evidence 证明存在稳定、跨 Consumer 的 reusable procedure 时，才重新评估 Provider capability。

## 5. 默认顺序

```text
Theme 0 — 状态 / 旧入口收口
→ Theme 1 — Authority Contract Extensibility
→ Theme 2 — Lightweight Change Execution
→ Theme 3 — Multi-Repository Project Workspace
→ Theme 4 — Local Validation Runtime Resource Lifecycle
```

顺序只表达当前规划：

- 先消除旧状态；
- 再处理跨 Skill 的 Authority 基础边界；
- 再收敛普通 persistent-workspace 开发粒度；
- 再处理多仓项目边界；
- 最后评估依赖 project / component identity 的本地验证资源治理。

每个主题闭环后都可以基于新 Evidence 调整、拆分或删除后续主题。

## 6. 当前停止点

本计划现在只完成：

- Consumer feedback 概览；
- 主题划分和顺序；
- 单主题闭环协议；
- baseline / non-goal 固化。

**Theme 0 已完成；Theme 1～4 尚未开始详细 Evidence re-analysis、外部研究、Design Freeze 或实现。**

下一责任：以新的 Fresh Context 单独进入 Theme 1 — Skill Authority Contract Extensibility 的 Evidence Re-analysis。

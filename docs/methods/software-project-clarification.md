---
id: method:software-project-clarification
type: method
status: active
---

# 软件项目澄清方法

## 1. 目标

本方法面向普通软件 Consumer 项目的项目级或重大范围前置澄清，用于在多个当前或预期 Feature 无法安全进入 Specification 时，建立或重建可持续使用的 Requirement / Architecture Context。

它不替代 `method:ai-development`。本方法解决“后续多个 Feature 可以依赖什么长期上下文”；`method:ai-development` 继续解决“当前具体 Feature / change 做什么、如何规划并完成”。

本方法也不因为存在于 `agentic-dev` 就自动适用于 `agentic-dev` 自身的 capability evolution；是否采用始终由目标 Repository 的 local Method selector 决定。

## 2. 进入条件

最小进入判据：

> 普通 Feature Development 无法安全继续，因为多个当前或预期 Feature 共同依赖的长期 Requirement / Architecture Context 缺失、冲突或需要重建。

常见场景包括：

- greenfield software project / new product；
- legacy modernization / rewrite；
- Requirement Authority 已碎片化、冲突或不足；
- major domain / product boundary restructuring；
- 多个计划 Feature 共同被同一个尚未解决的长期 architecture driver 阻塞。

不得仅因为项目较大、技术复杂、文档很多，或单个 Feature 存在局部不确定性而进入本方法。

普通单 Feature、bugfix、小范围变更，以及已有稳定 Requirement / Architecture Context 下的日常开发，继续使用目标 Repository 当前适用的普通开发 Method 或 direct responsibility。

## 3. 生命周期

```text
Establish Context
→ Requirement Clarification
→ Architecture Clarification? (conditional)
→ Clarification Convergence
→ Clarified Project Context Ready
```

正式阶段四个：

1. Establish Context；
2. Requirement Clarification；
3. Architecture Clarification（条件阶段）；
4. Clarification Convergence。

### 3.1 Stable phase identities

- Establish Context → `establish-context`；
- Requirement Clarification → `requirement-clarification`；
- Architecture Clarification → `architecture-clarification`；
- Clarification Convergence → `clarification-convergence`。

这些 token 只属于 `method:software-project-clarification`。

## 4. Establish Context

先明确本次澄清的项目 / 产品范围与证据边界：

- 识别当前可作为 Requirement / Domain / Architecture Authority 的来源；
- 区分 current、legacy、reference、analysis、conversation 与 unknown；
- 确认现有 semantic owner 是否存在、是否冲突、是否足以承担长期责任；
- 明确哪些信息只能作为 Evidence，不能自动提升为 Authority；
- 冻结当前分析范围，避免历史材料和平级材料污染当前事实。

不要求建立完整 source catalog。只有具有当前澄清价值或跨上下文协调价值的 source inventory 才需要暂存。

退出条件：当前 Evidence / Authority 范围足以支持 Requirement Clarification，且不存在会让后续事实抽取失去来源边界的未决问题。

## 5. Requirement Clarification

本阶段只处理 Problem / Behavior / Constraint / Acceptance 及其长期语义，不生成具体实现方案。

核心责任：

```text
extract requirement facts
→ normalize ownership / terminology
→ detect gap / conflict / ambiguity
→ classify requirement / external / design
→ resolve high-impact unknowns
→ promote confirmed facts to durable Authority
→ cross-authority consistency check
```

重点语义包括：

- product / domain goal and boundary；
- actor / stakeholder；
- business object / data semantics；
- workflow / scenario；
- business rule；
- state / lifecycle；
- failure / exception behavior；
- quality / compliance obligation；
- project-level acceptance intent / invariant。

### 5.1 Uncertainty classification

未知项至少应区分：

- confirmed / derivable fact；
- gap；
- conflict；
- ambiguity；
- unsupported assumption；
- external dependency；
- design item。

不能把所有未知都变成人工问题。只有现有 Authority 无法唯一裁决，且不同合理答案会实质改变产品行为、长期边界或验收时，才需要 Human Authority。

### 5.2 Authority promotion

确认的长期事实必须进入真实的 Consumer-local Requirement / Domain owner；聊天、分析报告、候选清单、比较表和派生视图不自动成为长期 Authority。

若有效 owner 不存在、冲突或结构性不足，本阶段负责建立或重建可被 Repository Authority 明确定位的 semantic owner；不要求统一目录、文件名或 schema。

### 5.3 与 Feature Specification 的边界

Project-level Requirement Authority 拥有跨多个 Feature 持续成立的事实与约束；Feature Specification 只拥有当前 change 的具体范围、可观察行为、失败行为与验收标准。

Specification 应引用长期 Requirement / Domain Authority，而不是为了“自包含”复制整个项目 Requirement Baseline。Feature 中确认的新事实如果具有长期、跨 Feature 的价值，应提升并回写到真实长期 owner。

## 6. Architecture Clarification

本阶段是条件阶段，不是 Big Design Up Front，也不把 Feature Technical Planning 整体提前。

核心进入条件：

> 多个当前或预期 Feature / change 在进入可靠 Specification 前，共同依赖一个尚未解决的长期 architecture driver。

可能的 architecture driver 包括：

- shared capability / shared contract；
- core data or system boundary；
- security / integration / deployment topology；
- high-cost-to-reverse structural decision；
- 成熟 reference implementation 能显著降低系统性探索成本；
- 多个局部实现已经显示需要抽取 shared capability。

本阶段可以形成或更新：

- Architecture Context / constraints；
- architectural capability boundaries；
- 长期 Architecture State；
- ADR（仅当背景、替代关系与主要权衡具有长期历史价值时）。

局部、低风险、可逆、只影响单个 Feature 的 HOW 留给 `method:ai-development` 的 Technical Planning / JIT Execution。

Architecture Clarification 与 Feature Technical Planning 必须共享同一个长期 Architecture owner，不形成平行 Authority。

若 Architecture Clarification 过程中暴露出新的业务多解、Requirement conflict 或未定义 Product Boundary，必须返回 Requirement Clarification；Architecture 不自行创造 Product Requirement。

## 7. Clarification Convergence

Convergence 验证的是后续 Feature Development 的输入是否可靠，而不是文档是否“写完”。

只有同时满足以下条件，才可以声明 `Clarified Project Context Ready`：

1. 多个 Feature 依赖的主要 product / domain boundary 有明确的 Consumer-local owner；
2. 长期 Requirement conflict / ambiguity 已关闭；仍会阻止后续可靠 Specification 的问题一律视为 blocker；
3. 已确认的长期事实已进入真实 Requirement / Domain Authority；
4. 普通 design choice 没有被静默提升为 Requirement；
5. 必须在多个 Feature 进入 Specification 前解决的 architecture driver 已进入同一长期 Architecture owner；
6. 普通 Feature-specific HOW 没有被提前吸入 Architecture Clarification；
7. 缺失、冲突或不足的 semantic owner 已建立或重建；
8. 命中强制独立语义复核条件时，review 已通过；
9. 剩余 open item 均明确为 non-blocking，且有 owner；
10. Fresh Context Feature Agent 可以从 Consumer-local Authority 恢复当前 Feature 所需的最小 Requirement / Architecture Context。

真正存在 blocker 时必须保持 NOT READY。

## 8. Independent semantic review

以下任一情况成立时，在声明 Ready 前必须执行 independent semantic review：

1. 从 legacy / heterogeneous sources 重建新的 Requirement Baseline；
2. 现有 Requirement Authority 发生大规模重构、批量迁移、结构化改写、摘要化或 AI 辅助语义收敛；
3. 多个 Authority 来源存在冲突，澄清过程对长期事实进行了实质合并、取舍或覆盖；
4. 一次澄清批量改变长期业务状态、生命周期、权限、业务范围、数据语义或验收不变量。

Review 必须能够核对 source / decision / resulting Authority，不能只检查格式、lint、链接或最终文档可读性。

若是小规模 greenfield clarification，长期事实直接来自明确的 authoritative decision，且不存在上述高风险变换或冲突，则是否增加 independent Reviewer 由 Consumer Repository policy、风险等级或 Human Authority 决定。

## 9. Artifact lifecycle

默认 durable：

- Requirement Authority；
- Domain / Terminology Authority（确有跨 Feature 长期价值时）；
- Architecture Context / State；
- ADR（条件性）；
- 已跟踪的 non-blocking open item / external dependency 及其明确 owner。

默认 transitional / disposable：

- source inventory；
- ambiguity candidate list；
- comparison matrix；
- flow / state / relationship view；
- extraction table；
- human-review batch；
- review scratchpad。

只要派生表达能够从 Authority 唯一再生，就不应默认成为长期同步对象。本方法不要求固定 Handoff Artifact，也不要求 Consumer 采用固定目录或统一 schema。

## 10. Return contract

本方法完成后只声明：

```text
Clarified Project Context Ready
```

它不等于：

```text
Specification created
Execution Unit created
Execute / Integrate authority granted
```

后续具体 Feature / Change 必须重新按 Consumer-local Method selector 选择适用流程。

普通 Feature Development 中发现上游缺口时：

- 只影响当前 Feature 的 Requirement ambiguity，且有效 owner 明确 → 返回并更新当前 Requirement owner，解决后恢复当前 Feature；
- systemic Requirement gap 影响多个 Feature / core domain semantics → 升级到项目级 Requirement Clarification 责任；
- 局部技术不确定性 → Technical Planning / JIT Execution；
- 长期 Architecture gap 跨多个 Feature 且阻塞可靠 Specification → 升级到 Architecture Clarification 责任；
- owner 缺失、冲突或不足 → 由项目级澄清负责建立或重建 owner。

只有问题本身再次形成独立复杂 work kind 时，才重新选择完整 `method:software-project-clarification`；不机械重跑整个 Method。

## 11. Skill / Rule 边界

本 Method 不要求每个阶段都存在独立 Skill。当前没有证据支持为了阶段命名预建 `requirement-analysis`、`architecture-framing` 等 Skill；只有未来真实 Consumer 工作证明某个 procedure 在多个 Repository 中稳定、可独立调用并能减少重复错误时，才评估 Skill admission。

同样不因为新增本 Method 就批量创建 Clarification Rules。只有真实存在独立 policy gap 时，才进入 Rule owner。

## 12. Evidence maturity

Requirement Clarification 的 v1 contract 来自真实 Consumer 项目的正向与负向历史证据；其方法目标不是复制历史流程，而是保留能够解释输入、责任、Authority promotion、Gate 与失败机制的可复用部分。

Architecture Clarification 当前 Evidence 较弱，因此 v1 只固化 bounded、conditional、anti-BDUF 的最小 contract。后续真实 Consumer 案例可以继续修订其进入条件与责任细节，但不能因此把它扩张为默认的完整 upfront architecture。

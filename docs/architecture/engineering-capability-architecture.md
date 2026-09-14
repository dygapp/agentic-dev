---
id: architecture:engineering-capability
type: architecture
status: active
---

# 工程能力架构

## 1. 目标

本 Architecture 定义 `agentic-dev` 的长期能力类型、语义所有权、组合关系与 Human / Agent 双视窗。具体 Method、Skill、Rule 与运行机制可以演进，但不得通过目录位置或文档重复形成第二套隐藏 Authority。

核心原则：

> **Single Semantic Ownership, Multiple Views — 单一语义所有权，多视窗表达。**

规范语义只由真实 canonical owner 持有；Guide / README 可以为人类重新组织、解释和导航这些语义，但不得成为第二套规范定义、运行时路由表或项目事实来源。

## 2. 能力类型

### Method

Method 是针对一类复杂工作的**规范过程模型**。它定义：

- 适用范围与进入条件；
- 工作阶段 / 状态及其责任；
- 主要长期产物与必要 Gate；
- 阶段转换、返回 / 回退关系；
- 整体完成条件；
- 过程中如何组合必要 Architecture、Skill 与 Rule。

Method 是可扩展的一等能力类型，而不是 `ai-development.md` 的同义词。一个仓库可以存在多个 Method，例如 AI Development、Consumer Adoption、Consumer Upgrade；未来只有在真实证据支持时，才增加大型项目 Requirements Analysis 等新 Method。

Method 可以跨多个 Agent Context、多个 Artifact、多个 Skill 与人工 Gate。Method 不要求每个阶段都有独立 Skill，也不得把 repository-specific policy 复制成自身隐藏规则。

### Architecture

Architecture 定义长期结构、能力边界、ownership、组合关系和运行不变量。Architecture 回答“这些能力如何组成系统、哪些语义归谁拥有”，不替代 Method 的过程生命周期，也不保存项目临时状态。

### Skill

Skill 是在责任已经明确后可独立调用的**有界、稳定、可复用执行能力**：

```text
Trigger / Purpose
→ Inputs
→ Procedure
→ Outputs
→ Exit Conditions
→ Escalation
```

Skill 可以被 Method 阶段调用，也可以由其他明确责任直接调用。Skill 不拥有跨多个 Method stage 的长期工作生命周期，不因自身存在取得仓库写入、集成、发布或部署授权。

容易因 Consumer / Repository Authority 不同而变化的 policy、格式约束、授权约束和完成声明要求，不应为了方便而固化进通用 Skill；它们优先由 Rule 或目标仓库 Authority 持有。

### Rule

Rule 是按当前工作事实条件性适用的 **policy / constraint / default / invariant / completion requirement**。

Rule 与 Skill 是正交关系，不是 `Skill → Rule` 的固定流水线。Rule 可以：

- 约束 Method 的某个阶段；
- 约束 Skill execution；
- 约束没有独立 Skill 的 direct Agent work；
- 约束 repository / external operation；
- 约束 verification 或 completion claim。

Rule 可以完全独立于 Skill 存在。一个 Rule 文件是否值得独立存在，以“是否具有独立发现、独立适用和独立演进的规范语义”为判断标准，而不是正文长度。

Rule 天然允许 Consumer-local specialization。通用 Skill 可以保持稳定 procedure，而不同 Consumer 根据自己的 Authority 定义或适配不同 Rule，例如 Git commit type / scope、术语、验证要求或局部技术 policy。

### Guide

Guide 是 **Human-facing explanatory / usage layer**。它面向人类说明项目概念、完整使用方法、adoption、upgrade、恢复、示例和导航。

Guide 可以完整讲述规范模型，但不拥有 canonical Gate、Rule routing、Skill contract、Method transition 或项目 current state。ordinary Agent runtime 默认不依赖 Guide；只有任务 / Authority 明确要求阅读人类说明、维护 Guide 或执行特定人工辅助场景时才读取。

### Research

Research 保存非规范性的外部证据、比较、实验与技术参考。Research 可以触发候选演进，但只有结论进入真实 Method / Architecture / Skill / Rule owner 后才成为规范。

## 3. Agent View 与 Human View

### Agent View

ordinary Agent 工作必须拥有不依赖 Guide 的规范入口。进入当前 responsibility 后，Architecture、Skill 与 Rule 是按责任并列选择的能力面，不是固定串行流水线：

```text
Repository Authority / Agent Bootstrap
→ Method selection（若当前工作属于某个 Method）
→ current Method stage / direct responsibility
    ├─→ relevant Architecture context
    ├─→ Skill discovery / invocation（如需要独立执行能力）
    └─→ Rule Discovery → applicable Rule bodies
→ execute / verify / return
```

Skill 可以在没有额外 Rule 时独立执行；Rule 也可以在没有 Skill 时约束 direct work。只有当前 task facts 与 responsibility 决定三者是否需要加载。

### Human View

人类入口通常为：

```text
README
→ Guides / directory README
→ 对 Method / Architecture / Skill / Rule 的解释与导航
```

Human View 可以为了教学和理解重复表达 canonical 语义，但必须清楚指向真实 owner。重复解释允许，重复拥有规范语义禁止。

## 4. Discovery / Selection 责任

不同能力类型不必共享一种发现机制，但每类 Agent-facing capability 必须有明确入口：

- Method：必须存在稳定的 selection / discovery contract，使 Agent 能从当前 work kind 进入正确 Method；不能依赖 Human Guide 猜测；
- Skill：使用 Agent Skills 原生 discovery，并由其 Trigger / Purpose 决定是否加载；
- Rule：由 Rule Discovery 根据当前 task facts 返回少量 locator，再由 Agent 阅读候选正文做最终语义确认；
- Architecture：由当前 Method / Skill / Rule contract 或 Repository Authority 按明确引用加载，不作为 ordinary runtime 全量扫描资源；
- Guide / Research：ordinary runtime 默认不发现，按明确的人类说明或研究任务读取。

Method selection 是否需要独立工具，应由规模和 eval 决定；在 Method 数量较少时可以使用稳定、可审计的 bootstrap contract，但不得形成与 Method 本身长期漂移的手工第二套流程正文。

## 5. Consumer-local specialization

Consumer Repository 始终拥有自己的项目事实与 local Authority。`agentic-dev` 提供可采用的 Method / Skill / Rule / Architecture，但 adoption 不等于全量复制。

- Method 可以 adopt / adapt，只要 Consumer 明确本地 canonical owner；
- Skill 应优先保持可复用 procedure，避免吸收 Consumer-specific policy；
- Rule 可以根据 Consumer Authority 本地化、替代或新增；
- Guide 可以针对 Consumer 提供本地 Human View，但不得改变 Agent canonical semantics；
- upstream provenance 与 Consumer-local Authority 必须区分。

## 6. 演进判定

当真实 Evidence 需要长期沉淀时，先判断 semantic owner：

- 改变一类复杂工作的过程模型、阶段、Gate 或完成语义 → Method；
- 改变长期能力边界、ownership、组合关系或运行不变量 → Architecture；
- 形成稳定、有界、可独立调用的执行能力 → Skill；
- 形成按条件适用的 policy / constraint / default / invariant / completion requirement → Rule；
- 只是面向人的解释、使用说明、示例或导航 → Guide；
- 只有证据 / 探索价值 → Research。

不得为了兼容历史载体保留重复 owner，也不得仅因为内容“重要”“有步骤”“很短”就决定其能力类型。
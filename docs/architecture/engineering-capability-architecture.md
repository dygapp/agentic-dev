---
id: architecture:engineering-capability
type: architecture
status: active
distribution: source-only
---

# 工程能力架构

## 1. 目标

本 Architecture 定义 `agentic-dev` **Source / Authoring Model** 中的长期 capability 类型、语义所有权、组合关系与 Human / Agent 双视窗。这里的 capability type 回答“源码语义由谁拥有”，不等于“普通软件 Consumer 最终安装什么目录或文件”。Consumer-facing Distribution Model 通过显式分类、构建与发布把 Source semantics 投影为版本化 Agent Skills，不得把 Source type / path 机械复制成 Consumer runtime namespace。

核心原则：

> **Single Semantic Ownership, Multiple Views — 单一语义所有权，多视窗表达。**

规范语义只由真实 canonical owner 持有；Guide / README 可以为人类重新组织、解释和导航这些语义，但不得成为第二套规范定义、运行时路由表或项目事实来源。

`Project Knowledge` 不是第六种 reusable capability。它是 Repository-local 的项目知识层，用于保存当前项目使命、capability instance、Roadmap 与稳定演进摘要。Project / Capability 的长期边界由 `docs/architecture/project-knowledge-architecture.md` 定义。

## 2. 能力类型

### Method

Method 是针对一类复杂工作的**规范过程模型**。它定义：

- 适用范围与进入条件；
- 工作阶段 / 状态及其责任；
- 主要长期产物与必要 Gate；
- 阶段转换、返回 / 回退关系；
- 整体完成条件；
- 过程中如何组合必要 Architecture、Skill 与 Rule。

Method 是可扩展的一等能力类型，而不是某个具体 Method 文件的同义词。一个 Repository 可以采用多个 Method；当前到底采用哪些 Method、怎样从本地 work kind 选择它们，属于该 Repository 的 Project capability instance。

Method 可以跨多个 Agent Context、多个 Artifact、多个 Skill 与人工 Gate。Method 不要求每个阶段都有独立 Skill，也不得把 repository-specific policy 复制成自身隐藏规则。

### Architecture

Architecture 定义可复用的长期结构、能力边界、ownership、组合关系和运行不变量。Architecture 回答“这种能力如何组成系统、哪些语义归谁拥有”，不替代 Method 的过程生命周期，也不持有某个 Repository 当前 capability inventory、Roadmap、baseline 或历史状态。

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

Guide 可以完整讲述规范模型，但不拥有 canonical Gate、Rule routing、Skill contract、Method transition 或 Project current state。ordinary Agent runtime 默认不依赖 Guide；只有任务 / Authority 明确要求阅读人类说明、维护 Guide 或执行特定人工辅助场景时才读取。

### Research

Research 保存非规范性的外部证据、比较、实验与技术参考。Research 可以触发候选演进，但只有结论进入真实 Method / Architecture / Skill / Rule owner 后才成为 reusable capability；只有进入 Project owner 后才成为当前 Repository 的长期项目事实。

## 3. Source Model 与 Distribution Model

Capability type 与 Distribution disposition 是两套正交分类。

### Source / Authoring Model

Source owner 继续按长期语义责任划分为 Method、Architecture、Skill、Rule 等。一个 Source owner 是否独立存在，取决于 single semantic ownership、演进责任与 provider runtime，而不是它是否会以同名文件发布给 Consumer。

### Distribution Model

Gate B 建立的 distribution metadata 只回答该 Source asset 如何参与发布：

- `source-only`：只服务 `agentic-dev` 项目、自身 runtime、研究、验证或维护，不进入 Consumer Release；
- `release-input`：其语义会进入 Release，但需要 build transformation / composition，不能按 Source path 原样投影；
- `release-direct`：自身已经是可直接进入 Release 的运行资产；
- `retired`：退出 Current model。

首版普通软件 Consumer 以 **Skill package** 为主要 Distribution Unit。一个发布 Skill 可以按 Agent Skills Specification 使用 `SKILL.md`、`references/`、`scripts/`、`assets/` 承载被编译后的必要运行语义。

这不改变 Source canonical ownership：

```text
Method / Architecture / Rule / Tool source owner
→ release-input
→ deterministic build / transformation
→ one or more Skill packages
```

发布 projection 只是 distribution result，不取得被编译 Source semantics 的 canonical authoring ownership；后续 Source 变更仍回到真实 Source owner。

`release-direct` Skill 也不因此取得完整软件开发生命周期。Skill 仍保持有界 Trigger / Purpose / Procedure / Exit；复杂 lifecycle 可以由多个可组合 Skill 与按需 references 共同支撑，不能为了获得简单目录退化成单一超级 Skill。

## 4. Agent View 与 Human View

### Agent View

ordinary Agent 工作必须拥有不依赖 Guide 的规范入口。Repository-local Project Capability Profile 负责把当前 Repository 的实例选择连接到 reusable capability；进入当前 responsibility 后，Architecture、Skill 与 Rule 是按责任并列选择的能力面，不是固定串行流水线：

```text
Repository Authority / Agent Bootstrap
→ Project Capability Profile + current Repository facts
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
→ 对 Project / Method / Architecture / Skill / Rule 的解释与导航
```

Human View 可以为了教学和理解重复表达 canonical 语义，但必须清楚指向真实 owner。重复解释允许，重复拥有规范语义禁止。

## 5. 发现与选择责任

不同能力类型不必共享一种发现机制，但每类 Agent-facing capability 必须有明确入口：

- Method：Architecture 定义 selection contract；当前 Repository 的 selector mapping 由 local Project capability instance 持有；不能依赖 Human Guide 猜测；
- Skill：使用 Agent Skills 原生 discovery，并由其 Trigger / Purpose 决定是否加载；当前 Skill root / discovery entry 由 Repository-local instance 声明；
- Rule：由 Rule Discovery 根据当前 task facts 返回少量 locator，再由 Agent 阅读候选正文做最终语义确认；当前 Rule root / Tool locator 由 Repository-local instance 声明；
- Architecture：由当前 Method / Skill / Rule contract、Project Capability Profile 或 Repository Authority 按明确引用加载，不作为 ordinary runtime 全量扫描资源；
- Guide / Research：ordinary runtime 默认不发现，按明确的人类说明或研究任务读取。

Method selection 是否需要独立工具，应由规模和 eval 决定；在 Method 数量较少时可以使用稳定、可审计的 Repository-local selector instance，但不得形成与 Method 本身长期漂移的第二套流程正文。

## 6. Consumer 本地特化

Consumer Repository 始终拥有自己的项目事实、Project Knowledge 与 local Authority。普通软件 Consumer **安装版本化 Release**，而不是按 upstream Source type 逐类复制 Method / Architecture / Rule / Tool。

- 通用 Source Method / Architecture / Rule 可以作为 `release-input` 被编译进一个或多个 Skill package；
- 发布 Skill 应保持有界 procedure，并通过 references / scripts / assets 按需承载复杂 supporting content；
- Consumer-specific 产品事实、Requirement、System Architecture、技术 policy、授权、术语、当前状态与其他本地治理继续由 Consumer Repository Authority 持有；
- 某项通用 Rule 语义若进入 Release，只能以适合发布 Skill 的运行约束被投影；Consumer-local Rule / policy 不因上游发布而失去本地 owner；
- Guide 默认是 provider Human View，不作为 Release object；
- Consumer 必须拥有自己的 Project Knowledge / Roadmap / current work，不复制 upstream Project state；
- upstream provenance 与 Consumer-local Authority 必须区分。

## 7. Project 与 Capability 分类

当一个长期事实需要沉淀时，先问两个问题：

1. 它是在定义**跨 Repository 可复用的能力语义**吗？
2. 还是在描述**当前 Repository 自身的使命、能力实例、状态或历史**？

前者进入真实 Capability owner；后者进入 Project Knowledge。具体判断见 `docs/architecture/project-knowledge-architecture.md`。

## 8. 演进判定

当真实 Evidence 需要长期沉淀时，先判断 semantic owner：

- 改变一类复杂工作的过程模型、阶段、Gate 或完成语义 → Method；
- 改变可复用的长期能力边界、ownership、组合关系或运行不变量 → Architecture；
- 形成稳定、有界、可独立调用的执行能力 → Skill；
- 形成按条件适用的 policy / constraint / default / invariant / completion requirement → Rule；
- 改变当前 Repository 自身使命、核心项目需求、capability instance、Roadmap 或稳定演进摘要 → Project；
- 只是面向人的解释、使用说明、示例或导航 → Guide；
- 只有证据 / 探索价值 → Research。

不得为了兼容历史载体保留重复 owner，也不得仅因为内容“重要”“有步骤”“很短”或“当前 agentic-dev 正在使用”就决定其能力类型或放入 Architecture。
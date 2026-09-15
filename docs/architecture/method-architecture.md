---
id: architecture:method
type: architecture
status: active
---

# Method 架构

## 1. Method 是一等过程能力

Method 是针对一类复杂工作的规范过程模型，不等同于某个单一“软件开发方法”文件。

一个 Method 至少定义：

- 适用工作类型与进入条件；
- 阶段 / 状态与每个阶段的责任；
- 必要长期产物或 Gate；
- 阶段转换、返回 / 回退条件；
- 整体完成条件；
- 需要组合的 Architecture、Skill、Rule responsibility。

Method stage 首先表示**工作状态与当前责任**，不是必须创建一份同名 Markdown 的要求。只有当阶段信息具有跨上下文协调、权威、追溯或长期知识价值时才持久化；临时推理、探索和施工步骤可以随当前上下文结束。

Method 可以跨多个 Fresh Context、多个 Artifact、多个 Skill 与人工 Gate。它不要求每个阶段都存在 Skill，也不要求每个阶段都产生独立长期文档。

## 2. Method 与其他能力

- Architecture 定义 Method 所处的长期结构、ownership 和运行不变量；
- Skill 为已明确的责任提供稳定有界执行能力；
- Rule 横切约束 Method stage、Skill 或 direct work；
- Guide 只向人解释 Method，不拥有 Method transition / Gate；
- Repository-local Project Authority 决定当前项目实际采用哪些 Method、如何选择，以及外部副作用权限。

Method 不应吸收容易因 Consumer / Repository 改变的局部 policy，也不应复制 Skill Procedure 或 Rule body。

## 3. Method Selection Contract

Agent 必须能够在不读取 Human Guide 的情况下，从当前 Repository-local Authority 选择适用 Method。

通用 selection contract 是：

```text
current repository facts + work kind
→ repository-local Method selector instance
→ canonical Method id / locator
→ read selected Method body
```

Architecture 只规定 selector **必须存在什么语义**；具体 Repository 当前的 `work kind → Method locator` 映射属于 Project capability instance，不属于 reusable Architecture。

一个最小 selector 只持有：

- 可稳定识别的 work kind；
- canonical Method id；
- canonical Method locator。

它不得持有：

- Method stages；
- Gate / completion conditions；
- Method 内部 Skill / Rule routing；
- 当前 Issue / PR / work state；
- Human Guide 解释正文。

因此具体 Method 正文仍是过程语义的唯一 owner，Repository-local selector 只是进入该 owner 的薄实例映射。

## 4. Method 可以形成上下游关系，但不建立 Super-Method

不同 Method 可以通过 Return Contract 与下一 work kind 自然衔接，例如：

```text
Requirement Baseline Establishment
→ Requirement Baseline Ready
→ Architecture Clarification?（条件性）
→ AI Development
```

这种关系不要求再建立一个只负责“串联其他 Method”的 super-method。只要每个 work kind 的进入条件、Return Contract 与 local selector 足以决定下一责任，就应保持 Method 单一职责。

同样，一个上游 Method 完成后不自动授予下游 Method 的 Execute / Integrate Authority；Repository-local Authority 仍决定下一实际工作。

## 5. 无匹配时的行为

如果当前工作不属于任何已定义 Method：

- 不得为了获得流程而强行套用最接近的 Method；
- 按 Repository Authority 与当前 direct responsibility 工作；
- 如果同类复杂过程反复出现并具有跨上下文长期复用价值，再以真实 Evidence 评估新增 Method。

Repository-local selector 缺失、陈旧或歧义时应失败关闭到当前 Project / Repository Authority，不从 Guide、历史聊天或目录名猜测 Method。

## 6. Selection 规模演进

Method 数量较少时，稳定、可审计的 Repository-local 静态 selector 足够。

只有当 Method 数量、work-kind 歧义或 selector 维护成本真实增长，并由 eval 证明静态映射不再可靠时，才评估 Method metadata discovery / selector tool。

不得仅为形式统一复制 Rule Discovery 的工具、metadata 或复杂度。

## 7. Phase Identity

如果 Rule Discovery 或其他 runtime contract 需要引用 Method stage，**稳定 phase identity 必须由具体 Method canonical owner 定义**。

Architecture 不维护跨 Method 的固定 phase token 列表，也不假设不同 Method 共享同一阶段身份。当前 Method 没有定义稳定 phase identity 时，调用方不得从自然语言阶段名或其他 Method 猜测机器 token。

## 8. Method 演进与新增门禁

新增 Method 至少证明：

1. 存在稳定且可识别的一类复杂工作；
2. 该工作具有跨单次 action 的阶段 / 状态与责任转换；
3. 需要跨上下文保持 Gate、返回或完成语义；
4. 仅靠一个有界 Skill 无法完整表达；
5. 与现有 Method 不只是命名或局部步骤差异；
6. 有真实项目 / Consumer Evidence 支持长期复用价值。

`method:requirement-baseline-establishment` 的加入基于真实大型 Consumer 的多轮需求分析正向与负向历史 Evidence，并拥有独立的 source classification、fact extraction、semantic ownership、Question Gate、Human Review 与 `Requirement Baseline Ready` Gate，因此不是 `ai-development` 的局部步骤。

`method:architecture-clarification` 与 Requirement Baseline work kind 分离，是因为它具有独立进入条件、低于 Requirement 的 Evidence maturity、条件性执行语义和不同 Return Contract；简单项目可以不运行该 Method。
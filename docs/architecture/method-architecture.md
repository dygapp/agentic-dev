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

Method 可以跨多个 Fresh Context、多个 Artifact、多个 Skill 与人工 Gate。它不要求每个阶段都存在 Skill。

## 2. Method 与其他能力

- Architecture 定义 Method 所处的长期结构、ownership 和运行不变量；
- Skill 为已明确的责任提供稳定有界执行能力；
- Rule 横切约束 Method stage、Skill 或 direct work；
- Guide 只向人解释 Method，不拥有 Method transition / Gate；
- Repository Authority 决定当前项目允许进入哪些 Method，以及外部副作用权限。

Method 不应吸收容易因 Consumer / Repository 改变的局部 policy，也不应复制 Skill Procedure 或 Rule body。

## 3. Method Selection

Agent 必须能够在不读取 Human Guide 的情况下选择 Method。

当前 Method 数量较少，使用 Repository Bootstrap 中的**稳定 work-kind selector**：`AGENTS.md` 只维护 `work kind → Method locator`，不复制 Method 阶段、Gate 或正文。

当前 canonical work kinds：

- 普通软件 / 产品变更的需求到收敛生命周期 → `method:ai-development`；
- Consumer 首次显式采用 `agentic-dev` 能力 → `method:consumer-adoption`；
- Existing Consumer 显式评估并升级 upstream baseline → `method:consumer-upgrade`。

如果当前工作不属于任何已定义 Method，不得为了获得流程而强行套用最接近的 Method。按 Repository Authority 和当前直接责任工作；若同类复杂过程反复出现并具有长期复用价值，再以 Evidence 评估新增 Method。

当 Method 数量、歧义或选择成本增长到 bootstrap selector 无法稳定维护时，应通过独立 eval 决定是否引入 Method metadata discovery / selector tool；不得预先复制 Rule Discovery 的复杂度。

## 4. Method Selection 不是第二套 Method

Bootstrap selector 只能持有：

- work kind 的稳定身份；
- canonical Method id / locator。

它不得持有：

- Method stages；
- Gate / completion conditions；
- Method 内部 Skill / Rule routing；
- 当前项目状态。

因此 Method 正文仍是过程语义的唯一 owner。

## 5. Method 演进与新增门禁

新增 Method 至少证明：

1. 存在稳定且可识别的一类复杂工作；
2. 该工作具有跨单次 action 的阶段 / 状态与责任转换；
3. 需要跨上下文保持 Gate、返回或完成语义；
4. 仅靠一个有界 Skill 无法完整表达；
5. 与现有 Method 不只是命名或局部步骤差异；
6. 有真实项目 / Consumer Evidence 支持长期复用价值。

例如大型项目前期 Requirements Analysis 可以成为未来 Method 候选，但应先从已验证实践提炼其阶段、产物、Gate 与适用边界，而不是只因历史上使用过就直接固化。
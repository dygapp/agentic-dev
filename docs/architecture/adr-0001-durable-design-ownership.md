---
id: adr:0001
type: decision-record
status: proposed
---

# ADR-0001：长期设计知识按语义归属，不按执行单元数量归属

## 背景

来自 `agentic-dev#189` 的 Consumer 反馈表明：现行 `technical-plan` 将长期 HOW 限制为跨多个 EU 的决定；一个 EU 中形成的稳定组件 / 接口约束会被留在短生命周期的工作材料中，影响 Fresh Context 恢复与实现替换。已有开放 Current Authority 解决了合法 owner 的消费与回写，却不能独立决定设计应何时形成及如何维护。

## 候选决定

1. **长期约束价值而非 EU 数量**决定是否应固化设计。Consumer 自有 Current Authority 维护稳定 Design；局部可逆 HOW 留在代码或 JIT。
2. 明确 **Technical Planning（活动）／Technical Plan（条件性实施方案）／Durable Design（长期当前语义）／ADR（重大取舍历史）** 的责任差别。ADR 不取代 Current Design。
3. 扩展现有 `technical-plan` 的必要设计形成职责，协调 `execute-unit` 的增量发现和 `converge` / `review-change` 的设计一致性检查，不新增独立 `detailed-design` Skill。
4. 继续支持 Consumer 自由选择合法 owner 与 Markdown、IDL、Schema、代码契约等载体；不引入 Provider 固定类型、目录、Registry 或新 Runtime。

## 主要备选及权衡

- **仅修改 Guide / Consumer-local 约定**：最少代码变化，但 canonical Skill 的“跨多个 EU”硬性门槛仍在，Consumer 只安装 Skills 时问题继续存在。
- **新增 `detailed-design` Skill**：职责看似独立，但现有证据尚未证明其独立 Trigger、过程和退出条件；容易与 `technical-plan`、`clarify-architecture` 发生重叠，并增加 Consumer 认知成本。
- **全部设计纳入 Architecture 或 Technical Plan**：实现简单，但会将组件专属设计升级为系统架构，或使一次性施工方案成为第二套 Current truth。
- **增强现有 Skills + 最小 Guide**（本候选）：改动数个责任边界，但保留原有产品结构，允许设计在实施前与实施中逐步形成。

## 后果与验证义务

- 以 Consumer 指定的 owner 和审批程序为前提；owner 不明时先解决缺口，不以生成新文档当作完成。
- 必须有单 EU 稳定接口、技术替换、执行中设计回流、设计 / 代码漂移、owner 退役及小修改不生成设计产物的正反例验证。
- `work/`、EU 归档与任务管理系统不是本决定的实施范围。

## 决策状态

本文件是 **待 Fresh / Independent Review 的 proposed ADR**；在审查与最终集成授权前，不声称该方法已经被发布或任何真实 Consumer 已完成采用。当前可执行语义以拟修改的 canonical Skills 为准；本 ADR 只保存背景与取舍。

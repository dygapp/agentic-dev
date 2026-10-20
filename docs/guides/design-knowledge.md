---
id: guide:design-knowledge
type: guide
status: active
---

# 长期设计知识：建立、维护与收敛

本文帮助人和 AI 判断软件 Consumer 中哪些设计值得成为长期 Current Authority，以及如何在规划或执行时使用现有 Skills 完成回流。它不是新的开发阶段、固定文档规范或 Skill procedure；具体操作以 Consumer Authority 与 installed Skills 为准。

## 1. 设计知识不是 EU 的附属品

项目的长期知识至少要区分：

| 责任 | 回答什么 | 默认权威 |
|---|---|---|
| Requirement / Specification | 为什么做、做什么、哪些外部可观察行为与失败语义必须成立、怎样验收 | Consumer 指定的 Product / Requirement / Specification owner |
| Architecture | 跨 Feature 持续成立的系统职责、结构和替换边界 | Consumer 指定的 Architecture owner |
| Durable Design | 会长期影响实现、组件协作、接口 / 协议、数据 / 状态、重要算法与不变量的逻辑或物理设计 | Consumer 指定的实际 Design owner |
| Technical Plan | 某次变更如何组织施工、迁移、集成和验证 | 条件性的工作方案，不自动成为长期设计 owner |
| ADR（Consumer 可选） | 在既有历史渠道不足且确需独立保留时，说明重要决定的原因、备选与权衡 | 条件性决策记录，不能替代当前设计 |
| EU / JIT Plan | 某次需要独立恢复与验证的执行责任 / 当前施工步骤 | 短生命周期执行材料，不复制长期 Current truth |
| Code / IDL / Schema / Tests | 当前实现、机器可读合同及其验证 | 可承载 Consumer 指定的部分 Design Authority；其余部分是实现 / 验证证据 |

“逻辑设计”描述独立于某一技术实现的职责与契约；“物理设计”描述特定实现及其版本条件。二者可以由同一真实 owner 管理，不要求两份文档。一个文件也可承载多种语义，但每项长期事实仍必须能确定单一 Current owner。

## 2. 什么时候固化设计

发现 HOW 时，优先判断它是不是某个长期约束，而不是它处于第几个开发阶段或横跨几个 EU：

- 会不会影响其他组件 / 接口消费者，或未来一次新 Feature、实现替换和迁移？
- 是否约束安全、状态、关键不变量、兼容边界、失败处理、重要算法或需要独立验证的质量属性？
- 新 Agent 不读旧 EU、旧 Technical Plan 或聊天记录，是否仍需恢复这项决定才能正确开发？

若答案表明长期价值，按 Consumer 的现有合法 owner 与维护程序建立或更新对应 Authority，即使决定只来自一个 EU。若只是局部、低风险、可逆的内部施工细节，留在代码、必要注释或临时 JIT 即可；不为每个类 / 函数生成 Markdown。

设计事实的载体可为 Markdown、图、OpenAPI / IDL、Schema、代码中的契约或契约测试。要避免文档、生成物与代码形成平行竞争的 Current truth：明确哪个位置拥有该语义，哪些只是生成或验证投影。

## 3. 合法 owner、发现与生命周期

1. 从当前任务及 Consumer 自有 locator / navigation、现有组件 / 架构约定恢复适用 Current owner；不靠文件名猜测，也不全仓枚举兜底。
2. 已有 owner 时沿原维护程序更新；没有时先由 Consumer Repository Authority 指定 / 授权 owner、责任范围及可恢复入口。横向 Skill 不擅自创建新的第二套 Authority。
3. 重大变更说明适用范围和版本条件、受影响的消费者 / 接口与测试、替代或退役关系；跨组件共同 contract 通常由共同项目 owner 管理，组件局部实现设计可由组件仓 owner 管理。
4. 更新长期 owner 后同步检查 locator、实现、IDL / Schema、契约测试、引用者及 Current wording。旧 owner 退出后只保留明确的历史 / provenance 角色；不能继续作为普通执行的 Current dependency。

无需统一中央 Registry、固定 `component-design/` / `interfaces/` 目录、ADR 制度或为每条设计维护复杂元数据。Consumer 已存在可靠的目录、Issue / PR / Git 历史和导航方式时直接复用。

## 4. 什么责任触发哪项能力

- WHAT / 业务失败语义或 Acceptance 尚不清：返回 Requirement / `specify`，不让设计擅自决定。
- 跨 Feature 的系统性、高成本难逆 Architecture driver：`clarify-architecture`。
- 需要稳定 HOW、确立长期接口 / 组件契约，或为实现消除技术不确定性：`technical-plan`；一个 EU 也可能触发，但不意味着必须形成独立 Technical Plan 文档。
- `slice-work` 记录当前设计 owner 的恢复线索，不复制正文；`execute-unit` 可产生设计候选，但应完成合法回流或升级，不在 EU 中静默固化长期约束。
- `converge` / `review-change` 按当前设计 owner 检查实现、接口消费者、IDL / Schema / 测试与验证证据的符合性；发现长期设计漂移不能仅靠功能测试 PASS 宣布 READY。

## 5. 两类正反例

**单 EU 的稳定接口**：一次开发明确了证书编码与签名组件之间可复用的接口约束，未来实现需要消费。即使只涉及单个 EU，该接口仍应归于 Consumer 指定的长期 Design owner；EU 结束后，Fresh Context 不依赖历史工作记录。

**替换技术实现**：公开站的业务导航、用户行为与可观察错误语义保持在 Specification；跨实现兼容接口与逻辑职责在对应长期 owner；旧框架专属组件设计只在旧实现范围内有效。替换时更新组件设计并验证共享 contract，不能改动未授权 WHAT。

**无需长期设计的小修改**：已有稳定契约下的局部可逆 bug fix，只需按范围修改并验证，不必创建 Design、Technical Plan、ADR 或 EU。

**负向收敛**：旧接口设计仍被读取、实现 / Schema / 消费者与设计不一致、或新稳定约束只写在历史 EU 中时，不能因为代码编译成功而宣称 READY；必须归属到正确 owner 并补充对应 Evidence。

## 6. 与 works / tasks 的边界

长期设计固化后，EU、JIT / 工作日志不需要承担长期知识真值；但这些执行材料保存、归档和任务管理系统的选择仍由 Consumer 自己决定，本 Guide 不规定统一 `work/` 策略。

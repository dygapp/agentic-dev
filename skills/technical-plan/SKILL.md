---
name: technical-plan
description: Resolves consequential technical HOW and establishes or updates consumer-owned durable design contracts when needed, including for a single execution unit. Use for stable component/interface/data decisions, integration, migration, shared contracts, or significant technical risks; skip for local reversible implementation details.
---

# technical-plan

## 目的

按当前责任收敛必须明确的 HOW，以及会长期约束后续实现、协作、替换或验证的设计知识；是否跨多个 Execution Unit 不是长期价值的判据。局部可逆施工细节留给 JIT Execution Plan，本 Skill 不承担所有代码细节的事前设计。

## 输入

- Ready Specification；
- 当前 Architecture / ADR / code state、已有组件 / 接口 / 数据等 Design Authority（如适用），以及会约束当前 HOW 的其他 Consumer Current Authority；
- 技术约束；
- Consumer-local constraints。

## 流程

1. 判断是否存在必须收敛的技术不确定性或长期设计约束；即使只有一个 Unit，稳定接口、关键不变量、组件替换边界等仍可能需要设计固化。仅有局部、低影响、可逆 HOW 且已有模式足以实施时，跳过独立 Technical Planning / Technical Plan，不额外建立文档。
2. 在最小必要范围收敛组件职责、接口 / 协议、数据与状态、错误处理、依赖、集成、迁移、部署、验证和关键风险；分别判断哪些是产品可观察 WHAT（返回 Requirement / Specification owner）、哪些是跨 Feature 的系统性 Architecture、哪些是有长期约束力的逻辑或技术实现 Design、哪些仅为本次施工步骤。不得让 HOW 覆盖其他 semantic owner。
3. 设计集合型数据访问时确认真实消费范围与 bounded / growing / unknown 性质；不得为了实现方便默认全量读取持续增长数据，也不得用固定小上限静默截断正确集合。
4. 涉及 legacy / historical / business data migration 时，明确 source role、semantic preservation、identity / duplicate、replay / idempotency、exception / conflict disposition、reconciliation 与 provenance；legacy source / mapping 不反向成为新 Requirement Authority。数据库 schema / initialization migration 与业务数据迁移是不同责任，不因名称相同混用。
5. 对会持续影响后续实现、接口消费者、技术替换、安全或验证的 Design 决定，即使仅由一个 Unit 产生，也要确认 Consumer 指定的合法 Current owner、适用范围、版本 / 替代关系及消费者，并在授权内写入真实 owner（Markdown、IDL / Schema、代码中的契约及其测试等载体依项目约定，不能制造互相竞争的真值）。Technical Plan 是可选施工方案，不因包含设计内容就自动成为 Current Design Authority。
6. 需要跨 Feature 持续约束的系统性架构 driver 返回 `clarify-architecture` 或既有 Architecture owner；已有合法 Design / Requirement 等 owner 时依其维护 procedure 更新。没有 owner 或建立程序时，依据 Consumer Repository Authority 请求确立 / 授权 owner，不能擅自创建第二套 Current truth；新建、替换或退役合法 owner 时同步检查 locator、适用版本、依赖的 consumer、验证契约和 current-state wording。
7. 对会持续影响后续维护或重新决策的关键技术取舍，连同稳定结论与适用边界写回 Consumer Git 版本化的合法 Current owner，不能仅保存在 Issue / PR / 聊天中；不要求逐字保存讨论。只有 Consumer 现有决策记录约定确需独立 ADR 且有稳定消费者时才形成 / 更新 ADR；普通局部选择和已有 owner 可充分说明的决定不额外创建 ADR。
8. 清除仍会阻塞安全实施的技术不确定性。每个分析或工具步骤结束后重新判断剩余 planning responsibility，只要当前范围内仍可自动收敛就继续。

## 输出

- 必要的 Current Design / Architecture owner updates（条件性，保留单一语义 owner）；
- Technical Plan（仅当确需独立实施方案时）；
- ADR（仅在 Consumer 有合法独立决策记录责任时）；
- Remaining technical blockers。

## 退出条件

当前范围中必需的技术不确定性已关闭，具有长期约束价值的 Design / Architecture 已进入合法可恢复的 owner，或已明确只需局部可逆实施而无需独立 Technical Planning / Technical Plan。

## 升级

重大架构方向、高影响难逆权衡、Authority 冲突或超出授权的共享 contract 改变需要升级。发出人工请求前先检查当前 Authority、代码 / 配置 facts、已有 Evidence 和已授权工具是否足以裁决，并把请求缩到最小不可替代决定。Skill 不创建 Execute Authority。

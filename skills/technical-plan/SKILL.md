---
name: technical-plan
description: Resolves durable cross-unit HOW decisions, maintains cross-feature architecture context changes, and conditionally persists ADRs for decisions whose background or trade-offs need durable history. Use for cross-module, data, integration, migration, shared contract, deployment topology, or significant architecture work; skip when only local reversible implementation details remain.
---

# technical-plan

## 目的

只解决实施前必须稳定、且跨一个以上执行单元持续有价值的 HOW；局部可逆施工细节留给 JIT Execution Plan。

## 输入

- Ready Specification；
- 当前 Architecture / ADR / code state，以及会约束当前 HOW 的其他适用 Consumer Current Authority（如存在）；
- 技术约束；
- Consumer-local constraints。

## 流程

1. 确认 Technical Planning 是否真的需要；若 Specification 可直接安全映射到当前系统已有模式，则返回无需独立 Technical Plan，局部可逆施工细节留给 JIT Execution Plan。
2. 只收敛跨执行单元需要共享的组件边界、数据 / contract、集成、迁移、部署、测试策略与关键风险，并应用 Consumer-local constraints；Technical Plan 必须与当前责任实际适用的 Current Authority 一致，不得把 HOW 规划变成覆盖其他 semantic owner 的后门。
3. 设计集合型数据访问时确认真实消费范围与 bounded / growing / unknown 性质；不得为了实现方便默认全量读取持续增长数据，也不得用固定小上限静默截断正确集合。
4. 涉及 legacy / historical / business data migration 时，明确 source role、semantic preservation、identity / duplicate、replay / idempotency、exception / conflict disposition、reconciliation 与 provenance；legacy source / mapping 不反向成为新 Requirement Authority。数据库 schema / initialization migration 与业务数据迁移是不同责任，不因名称相同混用。
5. 判断是否改变长期 Architecture Context；需要跨 Feature 持续约束时更新真实 Architecture owner。新 owner、replace / retire / archive transition 同步检查 locator / navigation、verification consumer 与 current-state wording。
6. 如果规划过程中暴露的长期语义属于 Consumer 其他既有 Current owner，返回该 owner / maintenance procedure；没有对应 owner 时显式暴露 gap，不为了完成 Technical Plan 临时创造第二套 Authority。
7. 只有决定背景、主要权衡或替代关系具有长期价值时才形成 / 更新 ADR；普通局部选择不创建 ADR，也不为了对称性创建无真实消费者的抽象。
8. 清除仍会阻塞安全实施的技术不确定性。每个分析或工具步骤结束后重新判断剩余 planning responsibility，只要当前范围内仍可自动收敛就继续。

## 输出

- Technical Plan（必要时）；
- Architecture / ADR updates（条件性）；
- Remaining technical blockers。

## 退出条件

实施前必须解决的技术不确定性已关闭，长期架构责任已进入正确 owner；或已明确本工作无需独立 Technical Plan。

## 升级

重大架构方向、高影响难逆权衡、Authority 冲突或超出授权的共享 contract 改变需要升级。发出人工请求前先检查当前 Authority、代码 / 配置 facts、已有 Evidence 和已授权工具是否足以裁决，并把请求缩到最小不可替代决定。Skill 不创建 Execute Authority。

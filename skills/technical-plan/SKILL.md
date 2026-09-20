---
name: technical-plan
description: Resolves durable cross-unit HOW decisions, maintains cross-feature architecture context changes, and conditionally persists ADRs for decisions whose background or trade-offs need durable history. Use for cross-module, data, integration, migration, shared contract, deployment topology, or significant architecture work; skip when only local reversible implementation details remain.
metadata:
  agentic-dev-id: "skill:technical-plan"
  agentic-dev-type: "skill"
  agentic-dev-status: "active"
  agentic-dev-distribution: "release-direct"
  agentic-dev-release-target: "software-development"
  agentic-dev-release-inputs: "method:ai-development;architecture:data-migration;rule:data-access-boundedness;rule:human-intervention-necessity;rule:authoritative-artifact-lifecycle-review"
---

# technical-plan

## 目的

只解决实施前必须稳定、且跨一个以上执行单元持续有价值的 HOW；局部可逆施工细节留给 JIT Execution Plan。

## 输入

- Ready Specification；
- 当前 Architecture / ADR / code state；
- 技术约束；
- 当前运行环境提供的适用约束 / references 与 Consumer-local policy。

## 流程

1. 确认 Technical Planning 是否真的需要；若 Specification 可直接安全映射到已有模式，则返回无需独立 Technical Plan。
2. 读取并应用当前运行环境为本职责提供的适用约束；Consumer Release 使用随 Skill 打包的 references 与 Consumer-local policy，provider runtime 服从当前 Repository Bootstrap。
3. 只收敛跨执行单元需要共享的组件边界、数据/契约、集成、迁移、部署、测试策略与关键风险。
4. 判断是否改变长期 Architecture Context；需要跨功能持续约束时更新真实架构 owner。
5. 只有决定背景、主要权衡或替代关系具有长期价值时才形成/更新 ADR；普通局部选择不创建 ADR。
6. 清除仍会阻塞安全实施的技术不确定性。

## 输出

- Technical Plan（必要时）；
- Architecture / ADR updates（条件性）；
- Remaining technical blockers。

## 退出条件

实施前必须解决的技术不确定性已关闭，长期架构责任已进入正确 owner；或已明确本工作无需独立 Technical Plan。

## 升级

重大架构方向、高影响难逆权衡、Authority 冲突或超出授权的共享契约改变需要升级。Skill 不创建 Execute Authority。

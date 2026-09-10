# 规则治理与知识激活 v2 协调计划

## 目标

协调 Issue #92 所跟踪的“规则治理与知识激活 v2”有限里程碑。

长期目标、设计约束、阶段边界与完成定义统一以：

`docs/project/rule-governance-knowledge-activation-v2.md`

为准。本计划只维护当前协调状态，不复制第二份长期 Authority。

启动基线：`master@b6a20053a7a6f4f53915bea8218604720412c302`  
跟踪入口：Issue #92

## 已完成

### Phase A — Consumer-local Runtime Target / Acceptance

结果：

- `docs/project/consumer-local-rule-runtime-target-v2.md`
- `docs/project/consumer-local-rule-runtime-acceptance-v2.md`

### Phase B — Rule Ownership / Guide Decomposition

结果：

`docs/project/rule-ownership-decomposition-audit-v2.md`

### Phase C — Minimal Metadata / Catalog Contract

结果：

`docs/project/consumer-local-activation-metadata-contract-v2.md`

### Repository Entry-point Convergence

已完成根入口职责收敛：

- `AGENTS.md` 只维护稳定 Repository Governance / Authority Boundary / Agent 工作约束；
- 当前状态迁移到 README / Roadmap / v2 项目记录；
- Method / Principle / Skill / Guide 的重复正文不再由 `AGENTS.md` 承载；
- Fresh Context 不默认从 `AGENTS.md` 加载当前里程碑、候选路线、实验进展或历史状态。

该修订属于 v2 的直接设计约束：Consumer-local Bootstrap 也不得把易变化项目状态堆入最高优先级治理入口。

## 当前工作项

### Phase D — Discovery → Routing → Skill Interface

当前只冻结运行接口，不增加 Runtime Rule Index、Stage Router Skill 或新的超级控制器。

需要形成可复核结果：

1. 当前 task signals 如何映射候选 responsibility；
2. 如何确定 primary responsibility 与 supporting context；
3. routing-only 何时停止而不加载 Skill；
4. execution responsibility 何时加载对应 Skill；
5. constraint module 如何附加到 primary responsibility；
6. Stage Return 后如何重新解析责任并使旧 routing / Readiness 失效；
7. 多命中如何形成最小充分集合；
8. stale / missing / ambiguity / conflict / high-impact 如何 fail-closed；
9. Runtime Adapter 如何只承担 discovery / delivery / loading，不拥有 Method 语义；
10. 接口如何直接映射 Phase A 的 Consumer-local acceptance scenarios。

Phase D 输出应进入必要的独立设计文档，并回写 v2 项目记录；不把过程推理保存为长期 Research。

## 后续顺序

```text
Phase D Discovery / Routing / Skill Interface
→ Phase E Baseline Adoption / Consumer-local Projection
→ Phase F 真实 Consumer 验证
→ Phase G 收敛、回归、最终 AI Review 与集成准备
```

## 当前最小输入

- `AGENTS.md`
- `README.md`
- `docs/project/project-roadmap.md`
- `docs/project/rule-governance-knowledge-activation-v2.md`
- Phase A～C 四个直接设计结果
- `docs/architecture/skill-contracts.md`，只读 Phase D 需要的职责 / Stage Return 部分
- `docs/guides/rule-activation-guide.md`，用于与 v1 navigation 边界对照
- Issue #92

只有需要核对具体 Consumer / upstream adoption 语义时，再读取 `using-agentic-dev.md`、Issue #58 或真实 Consumer Authority；不要默认恢复 v1 完整过程文档或全部 eval 输出。

## 范围控制

Phase D 不：

- 修改核心 Method / Principles；
- 修改正式 Skill；
- 产品化 eval manifest；
- 修改 Consumer Repository；
- 引入 Runtime Rule Index、数据库、MCP 或服务；
- 创建 Stage Router / Rule Super Skill；
- 启动 WI-06 / WI-07 / WI-09 或 Issue #71 候选实施；
- 继续增加昂贵模型 Runtime Eval，除非设计出现无法通过现有证据区分的关键分歧。

## 阻塞与升级

只有出现以下情况才升级：

- 必须改变 Consumer Authority 优先；
- 必须增加新的核心 Method Stage；
- 无法在不形成第二 Authority 的情况下完成 routing；
- Runtime responsibility interface 与现有 Skill Contract 发生不可调和冲突；
- 必须选择新的重大、难逆运行时基础设施。

普通命名、接口表示、可逆 metadata 细节和文档归位由当前工作继续收敛。

## Phase D 完成条件

必须能用一个明确、无超级控制器的模型回答：

```text
Fresh Consumer Task
→ Local Bootstrap / Current Authority
→ Candidate Discovery
→ Primary Responsibility + Supporting Constraints
→ Routing-only Stop 或按需 Skill Load
→ Execute / Verify
→ Stage Return 时重新解析
```

并确保 ordinary runtime 不访问 upstream、Consumer-specific Authority 始终优先、fail-closed 路径明确、metadata 不拥有规则正文。
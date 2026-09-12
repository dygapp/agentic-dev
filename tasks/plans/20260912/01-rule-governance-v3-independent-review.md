# V3 Independent Review 协调计划

## 目标

协调 Issue #118 — 规则治理与知识激活 v3 独立复核，在不重新设计 V3-01～V3-08 的前提下，以新的 Fresh Context 挑战当前长期架构、Evidence 泛化边界与 v3 closure 条件。

## 基线边界

- Repository：`dygapp/agentic-dev`
- Parent：Issue #94
- Planning / Evidence Authority：Issue #118
- **复核对象冻结基线：** `agentic-dev@86fe96756c7b3678d7b0bac10f32358a9372e84c`
- **执行恢复基线：** Independent Review 真正开始时的 GitHub current `master`，必须在新的 Fresh Context 中重新读取，不预先固定 SHA。

`86fe967…` 是 PR #117 集成后的 V3 closure candidate subject baseline，不代表执行时 current Repository State。Gate A planning / recovery-only 变更可以在执行时作为 current state 被读取，但不能静默改变冻结 subject 的 Architecture / Evidence claim；如果 Gate A 之后出现实质改变 V3 subject semantics 的提交，必须先明确刷新 subject baseline，而不是自动扩大复核对象。

## 直接 Authority / 输入

复核执行上下文先按 `AGENTS.md` 的 Fresh Context 恢复规则读取执行时当前 Repository State；随后按 Issue #118 的 review scope 最小扩读：

- `docs/project/rule-governance-knowledge-activation-v3.md`
- V3-01 / V3-02 项目记录；
- `docs/architecture/consumer-lifecycle.md`
- `docs/architecture/skill-architecture.md`
- `docs/architecture/skill-contracts.md`
- `docs/architecture/agent-resource-model.md`
- `docs/architecture/resource-discovery-architecture.md`
- V3-07 / V3-08 项目记录与其精确 Issue Evidence；
- `docs/method/ai-development-method.md` 与其他被 finding 直接涉及的更高优先级 Authority；
- PR #117 集成后的最终状态。

已完成阶段的 PASS、作者总结和历史聊天都只能作为待验证 claim，不作为独立复核结论前提。

## 范围

1. Ownership / Authority 一致性；
2. Artifact lifecycle closure；
3. Skill / capability boundary；
4. Resource / discovery semantics；
5. Consumer Evidence generalization；
6. v3 closure / ADR necessity。

## 非目标

- 不修改 Consumer Repository；
- 不预设必须产生 ADR；
- 不重新设计 V3-01～V3-08；
- 不自动启动 WI-06 / WI-07 / WI-09、Issue #71 或其他候选；
- 不把独立复核变成第二套长期 Method / Architecture；
- 不因为上下文成本而牺牲 correctness、Authority 或 fail-closed。

## 独立执行协议

真正 Independent Review 必须在新的 Fresh Context 中执行：

1. 不带入本计划之外的作者会话推理；
2. 从执行时当前 GitHub Repository 重新恢复事实；
3. 明确区分 current repository state 与冻结 subject baseline `86fe967…`；
4. 不先读取历史 AI Review verdict 作为判断依据；
5. 先完成 Authority / Architecture 语义审查，再按需追溯 Evidence；
6. 每个 Finding 必须包含：`severity / locator / claim / impact / evidence / minimal recommendation`；
7. 如果证据不足，明确标记 `insufficient evidence`，不得猜测；
8. 最终分别给出 Blocking / Medium / Low 数量、ADR candidate、v3 closure recommendation。

## 工作顺序

### IR-1 — Protocol / Recovery Entry

- [x] 建立 Issue #118 Planning Authority；
- [x] 冻结复核对象 subject baseline；
- [x] 建立 execution-time current-state recovery 规则；
- [x] 建立独立复核范围、Finding schema 与 Gate；
- [x] 对齐 README / Roadmap / v3 项目记录的拟集成恢复状态；
- [x] 形成 Planning PR #119 并进入高影响 AI Review / 人工集成决策链。

Final AI Review、Draft / Ready、是否合并与集成提交都属于 GitHub 原生事实，直接从 PR #119 恢复，不在计划中用 checkbox 复制。PR #119 的候选文档表达**拟集成后的稳定状态**：Gate A protocol 已建立，真正下一实际步骤为新的 Fresh Context Independent Review；因此不需要再派生只用于记录“PR 已合并”的尾部状态提交。

### IR-2 — Independent Fresh Context Review

- [ ] 新 Fresh Context 从执行时 current `master` 恢复 Repository State；
- [ ] 以 `86fe967…` 作为冻结 V3 subject baseline；
- [ ] 完成 A～F 六个审查面；
- [ ] 回写完整 Finding Evidence 到 Issue #118；
- [ ] 明确 Blocking / Medium / Low 与 ADR candidate。

### IR-3 — Finding Resolution

- [ ] Blocking / Medium 为 0 时直接进入 Closure Decision；
- [ ] 如存在 Blocking / Medium，只做 finding 支持的最小修订；
- [ ] 修订后使用新的独立复核上下文定向复评。

### IR-4 — V3 Closure Decision

- [ ] Blocking=0 / Medium=0；
- [ ] 判断是否存在真实 ADR candidate；
- [ ] 无 ADR candidate 时形成 v3 Closure；
- [ ] 有 ADR candidate 时只启动必要 ADR，不自动扩展为 formal design / implementation planning。

## 完成条件

- Independent Review 以新的 Fresh Context 完成；
- current execution state 与冻结 subject baseline 的边界可恢复；
- Finding 可追溯且无未解决 Blocking / Medium；
- Evidence generalization 未超出来源；
- v3 closure / ADR necessity 有明确结论；
- README / Roadmap / Issue #94 / #118 能恢复同一 Current State；
- 高影响状态变更完成 AI Review；
- 没有因独立复核机械产生新的长期框架、Skill 或 Consumer 规则。

# 规则治理与知识激活 v1 — 协调计划

## 目标

在不继续机械增加 Guide、Skill、Technology Profile 或 Runtime Layer 的前提下，完成当前规则体系的激活审计、最小检索模型、历史场景专项评估、必要权威收敛和 Consumer Fresh Context 验证，使 Agent 能在具体任务中以更小活动上下文可靠取得正确规则。

## 权威 / 输入

开始或恢复本计划时按当前 GitHub 状态重新核验，并读取：

1. `AGENTS.md`；
2. `docs/project/project-roadmap.md`；
3. Issue #73；
4. `docs/project/rule-governance-knowledge-activation-v1.md`；
5. `docs/research/knowledge-activation-and-code-intelligence-analysis.md`；
6. `docs/guides/using-agentic-dev.md`；
7. `docs/guides/external-operation-guidelines.md`；
8. 按当前工作需要读取 `skill-architecture.md`、`skill-contracts.md`、Engineering Disciplines、历史治理评估与 Consumer Evidence；
9. Open PR / Issue 和当前 `master`，确认没有晚于本计划的人工路线决定或集成事实。

本计划只负责协调，不复制上述长期 Authority 的完整规则。

## 启动状态

人工决策日期：2026-09-08

启动基线：

`master@0895ca30f76c666f3a0d4d9c2f9af6f14cded5d6`

活动里程碑：

**规则治理与知识激活 v1**

跟踪入口：Issue #73

当前分支：

`docs/rule-governance-knowledge-activation-v1`

当前门禁：

> **Phase A — Activation Audit**

## 范围

本计划负责：

- 高影响 Guide 规则激活单元审计；
- Always-on / Task / Conditional Context 分层候选；
- Rule duplication / conflict / supersession 检查；
- Minimal Retrieval Model；
- Retrieval / Activation Targeted Eval；
- 必要 Authority / Guide / activation pointer 收敛；
- Consumer Fresh Context 验证；
- 最终 AI 复核与集成前状态闭环。

## 非目标

- 不实现 Code Review Skill；
- 不启动 WI-06；
- 不启动 WI-09；
- 不新增第四 Engineering Discipline；
- 不强制采用 Obsidian；
- 不强制采用 CodeGraph；
- 不预先建立 Rule Graph DB、MCP、Marketplace、Plugin Bundle；
- 不把大 Guide 机械按文件大小拆分；
- 不把现有规则复制到多个 Skill / Guide 中；
- 不把本计划写成完整会话记录。

## 工作项与顺序

### A1 — 建立审计基线

- [ ] 重新确认 `master`、Open PR / Issue 与当前活动里程碑；
- [ ] 确认 `using-agentic-dev.md`、`external-operation-guidelines.md` 当前 exact blob / commit identity；
- [ ] 枚举当前 AGENTS / README / Skill / Guide / Project 入口中与两份 Guide 重复或交叉的高影响规则；
- [ ] 冻结历史失效场景候选清单。

输出：Activation Audit 基线与场景清单。

### A2 — `using-agentic-dev.md` Activation Map

- [ ] 按语义而不是标题机械切分规则激活单元；
- [ ] 对每个单元记录 Trigger / Consumer / Strength / Authority Pointer；
- [ ] 标记 Always-on 候选；
- [ ] 标记只在新项目 / Existing Consumer / Fresh Context / Roadmap / Integration / Verification 等条件下需要的单元；
- [ ] 标记重复 / overlap / stale / superseded 候选；
- [ ] 关联已知 Consumer / PR / Eval 证据。

### A3 — `external-operation-guidelines.md` Activation Map

- [ ] 同 A2；
- [ ] 特别区分普通写操作、跨仓库、人工介入、异步闭环、媒体资源、共享资源 / lease、证据晋升、PR 拓扑等独立条件；
- [ ] 检查是否存在“任何外部操作都要加载整份 Guide”的隐式入口。

### A4 — Cross-authority Duplication Audit

- [ ] 比较 AGENTS / README / Guide / Skill / Project rules；
- [ ] 区分合理摘要 / pointer 与实质重复 Authority；
- [ ] 标记同义但不同强度的规则；
- [ ] 标记可能导致冲突选择的规则；
- [ ] 不在本步骤立即删除规则。

### A5 — Activation Failure Taxonomy Evidence

对历史场景逐项分类：

- [ ] Discovery / Activation Failure；
- [ ] Selection / Conflict Failure；
- [ ] Instruction Density；
- [ ] Misleading / stale context；
- [ ] Genuine Rule Gap。

至少覆盖：

- [ ] Roadmap / Milestone 集成后状态闭环；
- [ ] Planning Candidate / Execution Unit 身份边界；
- [ ] Verification trigger / readiness re-entry；
- [ ] External async operation closure；
- [ ] Consumer Fresh Context authority discovery。

Phase A 完成条件：A1～A5 有可复核结果，并且能够说明下一步需要解决的是 Retrieval / Activation，而不是直接新增规则。

---

### B1 — 冻结 Minimal Retrieval Contract

- [ ] 定义最小输入：Task / Risk / Artifact / Stage 中哪些字段确有辨识力；
- [ ] 定义最小输出：Authority Pointer + Activated Rules + Required Checks；
- [ ] 定义 fallback：无索引 / 索引 stale 时回退 Repository 直接读取；
- [ ] 定义 duplicate / supersession 最小语义；
- [ ] 避免建立无法由当前证据证明必要的复杂 schema。

### B2 — Prototype 选择

按最小实现原则在以下方案中选择足够的一种：

- Markdown section index；
- YAML / JSON derived index；
- 小型 query script；
- 其他等价可重建方案。

选择标准：

- 可从 Repository Authority 重建；
- 能精确回指 source / section；
- 能检测 source drift；
- 能支持 Eval；
- 不需要先引入新 Runtime Layer。

### B3 — Prototype 验证

- [ ] 对 Phase A 的规则单元建立最小索引；
- [ ] 手工检查查询结果；
- [ ] 确认删除索引不损失任何长期事实；
- [ ] 确认同一规则没有复制成第二 Authority。

---

### C1 — Targeted Eval 设计

至少设计能区分以下行为的场景：

- 正确召回必要规则；
- 避免装入大量不相关 Guide 内容；
- 处理冲突 / superseded 规则；
- 当前 Context 不满足 Trigger 时不激活规则；
- source stale 时回退；
- genuine rule gap 时不能靠错误检索伪装成已有规则。

### C2 — A/B 基线

比较：

```text
A：现有完整 / 粗粒度上下文
B：薄 Kernel + Task / Risk 按需检索
```

记录可取得指标：

- Rule Recall；
- Context Noise / Precision；
- Input Context；
- File / Tool Reads；
- 语义断言；
- 误停 / 误升级 / 误执行；
- 是否发生权威混淆。

### C3 — 隔离运行时与人工评分

- [ ] 使用 Fresh Context / isolation；
- [ ] 隐藏 expected behavior / assertions；
- [ ] 进程退出码与 Semantic PASS 分离；
- [ ] 人工按 assertions 评分；
- [ ] 对失败场景先判断 Activation / Retrieval / Rule Gap 类型再修订。

Phase C 完成条件：存在足够证据判断新激活模式是否优于当前粗粒度加载。

---

### D1 — 基于证据实施 Guide / Authority 收敛

只实施 C 阶段证明有价值的动作，例如：

- [ ] 缩减 Always-on 内容；
- [ ] 增加 section-level pointer；
- [ ] 拆出真正独立 Activation Unit；
- [ ] 合并重复规则；
- [ ] 删除 stale / superseded 规则；
- [ ] 修正 Skill activation pointer；
- [ ] 固化最小 Rule Metadata / Derived Index；
- [ ] 定义 Rule deletion / supersession lifecycle。

禁止无证据全量重构。

### D2 — 回归

- [ ] 原有治理评估不回退；
- [ ] 新 Retrieval Eval 继续通过；
- [ ] Fresh Context 不需要读取整个历史；
- [ ] 当前正式术语与中文规则不回退。

---

### E1 — Consumer Fresh Context 验证

选择真实 Consumer，重新读取其 Repository Authority，验证：

- [ ] Consumer-local Authority 始终优先；
- [ ] 能取得当前任务最小 `agentic-dev` Rule Set；
- [ ] 不机械读取全部 Guide；
- [ ] 不把 `agentic-dev` 项目级规则带入 Consumer；
- [ ] 关键规则没有因缩减 Context 丢失。

### E2 — Consumer CodeGraph 可选 A/B

这不是本里程碑完成的强制依赖；如果当前 Consumer 环境适合，可以并行收集：

- [ ] 传统 Read / Grep / Find；
- [ ] Local Codex + CodeGraph；

在代码入口发现、调用路径、影响范围、Debug / Review 上比较效率和正确性。

任何结果只作为 Consumer Code Intelligence Adoption Evidence，不把 CodeGraph 直接固化为核心方法强依赖。

---

### F1 — Final Verification

- [ ] 静态文件 / schema / link 检查；
- [ ] 必要 Targeted Eval；
- [ ] 历史直接回归；
- [ ] Consumer 验证证据；
- [ ] 人工语义评分完成。

### F2 — Final AI Review

- [ ] 重新读取当前 target base / PR / diff；
- [ ] 检查 Authority 一致性；
- [ ] 检查是否制造新超级 Guide / Skill / Index Authority；
- [ ] 检查是否发生未授权 WI-06 / WI-07 / WI-09 范围扩张；
- [ ] 未解决阻塞 / 中等级问题必须为 `0 / 0`。

### F3 — Integration-state Closure

- [ ] Roadmap；
- [ ] AGENTS；
- [ ] README；
- [ ] 本里程碑 project record；
- [ ] Issue #73；
- [ ] 本计划；

全部形成拟集成后的自洽状态，再进入人工集成决策。

## 后继计划门禁：WI-07 — Code Review Capability v1

本计划完成不自动启动 WI-07。

只有规则治理与知识激活 v1 已完成并集成后，新的 Fresh Context 才可以基于 Roadmap 决定是否正式启动 Code Review Capability v1。

未来 Code Review Planning 必须继承以下已冻结边界：

1. 独立高信噪比 Review 职责；
2. 非通用 Method 新 Stage；
3. 非超级 Skill；
4. 与 Planning Review 分离；
5. 默认检查规格符合性、真实缺陷 / 回归、数据 / 状态 / 生命周期、边界 / 依赖 / 副作用、复杂度、Diff Scope、Verification Evidence；
6. 技术规则按风险激活，不创建按技术名称的 Review Skill；
7. CodeGraph 等 Code Intelligence 只能是可选结构发现辅助；
8. 无 CodeGraph 时必须可回退；
9. WI-06 是否启动由 Code Review / Consumer Eval 暴露的真实技术知识缺口决定。

## 当前下一步

本计划当前只进入：

> **A1 — 建立审计基线**

后续 Fresh Context 不得从聊天记忆恢复本轮讨论，应从 GitHub 当前状态和本计划列出的 Authority / Research 入口重新开始。
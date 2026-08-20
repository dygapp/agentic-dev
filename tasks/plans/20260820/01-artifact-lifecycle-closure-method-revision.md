# Artifact 生命周期闭环修订计划

**状态：** CLOSED（原范围已由 PR #28 合并）

**集成基线：** `master@8882c98`

**后继计划：** `tasks/plans/20260820/02-artifact-lifecycle-operationalization-recovery.md`

## 1. 目标

修复 agentic-dev 中长期产物（Artifact）仅被引用但缺少完整生命周期定义的问题，并同步收敛 Skill 清单、项目治理规则和相关派生文档的一致性。

本次修订重点解决：

- 长期上下文和权威产物的产生入口不明确；
- Artifact 缺少 Producer（产生者）、Trigger（触发条件）、Update（更新）、Supersede（替代）等生命周期语义；
- Skill Inventory 与实际 Skill 数量存在偏差；
- AI Review 缺少 Artifact Lifecycle Closure（产物生命周期闭环）检查维度。

## 2. 背景 Findings

### Finding-01：领域上下文生命周期缺口

Domain Context（领域上下文）被多个阶段消费，但当前未明确：

- Durable Domain Fact（长期领域事实）如何产生；
- 什么情况下从 Feature Context（功能上下文）提升为长期权威；
- 谁负责更新 Domain Authority（领域权威）；
- Execute / Debug 阶段发现冲突时如何回流。

### Finding-02：架构上下文生命周期缺口

当前 ADR（Architecture Decision Record，架构决策记录）已经定义了产生规则，但 Architecture Context（架构上下文）本身缺少明确定位。

需要明确：

- Architecture Context 与 Domain Context 的边界；
- ADR 是架构决策记录，而不是全部架构状态；
- Architecture Artifact 的产生、维护和更新规则。

### Finding-03：Skill Inventory 一致性问题

当前仓库实际 Skill：

- 8 个 Core Skills（核心 Skill）；
- 1 个 Platform-specific Skill（平台专项 Skill）。

总计 9 个 Skill。

部分入口文档仍容易被理解为仓库只有 8 个 Skill，需要统一表达。

### Finding-04：AI Review 缺少 Artifact 生命周期检查

当前 AI Review 已覆盖 Authority、Method、Contract、Skill 等一致性，但缺少对新增或修改 Artifact 的生命周期检查。

## 3. 修改范围

### 包含

- docs/method/ai-development-method.md
- docs/architecture/skill-architecture.md
- skills/README.md
- README.md
- docs/project/ai-review-guidelines.md

根据实际影响可能调整：

- docs/architecture/first-batch-skill-design.md

### 不包含

- 新增核心 Skill；
- 新增方法阶段；
- 创建 Domain Context Skill；
- 创建 Architecture Management Skill；
- 强制 Consumer 项目目录结构；
- 将 agentic-dev 项目治理规则传播给 Consumer。

## 4. 预期修改

### Method / Architecture

增加：

- Domain Context 生命周期规则；
- Architecture Context 定义；
- Artifact Lifecycle Closure 语义。

明确：

- Producer；
- Trigger；
- Consumer；
- Persistence；
- Update；
- Supersede；
- Escalation。

### Skill Architecture

明确 Skill 分类：

- Core Skills：8 个；
- Platform-specific Skills：当前 1 个；
- Future Experimental Skills：按真实证据评估。

保持：

- Core Skill Engineering CLOSED；
- 不因存在非核心 Skill 而重新打开核心 Skill 扩展。

### AI Review Governance

增加 Artifact Lifecycle Check：

检查新增或重大修改 Artifact 是否具备：

- Producer；
- Trigger；
- Consumer；
- Persistence；
- Update；
- Supersede；
- Escalation。

## 5. 完成条件

完成后应满足：

- Method / Architecture 文档无生命周期断层；
- ADR、Domain Context、Architecture Context 定位清晰；
- Skill Inventory 与实际仓库状态一致；
- AI Review 能发现类似 ADR 初始问题；
- 无新增 Core Skill；
- 无 Consumer Boundary Regression（Consumer 边界回归）。

## 6. 执行方式

本计划用于 Fresh Context（新鲜上下文）执行。

执行会话不得依赖当前聊天历史，应重新读取：

1. AGENTS.md；
2. 当前 master Authority；
3. 本计划；
4. 目标文档。

执行完成后：

- 重新读取最终变更；
- 执行 AI Review；
- 创建 PR；
- 等待 Human Review / Merge。

## 7. Closure / Successor Record

本计划定义的 Method、Skill Architecture、Skill Inventory 与 AI Review Governance 修订已经通过 PR #28 合并到 `master@8882c98`；PR 讨论中已记录当轮 `AI Review: PASS`。该范围已经关闭，不应在 Fresh Context 中被误判为尚待重新执行。

PR #28 合并后确认仍需把既有 Method 语义映射到 Skill Contract、核心 Skill 实现、Consumer Operating Guide 与针对性 Eval。该后续工作不改变本计划的已完成结论，统一由后继恢复计划管理：

`tasks/plans/20260820/02-artifact-lifecycle-operationalization-recovery.md`

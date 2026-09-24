---
id: project:roadmap
type: project
status: active
---

# 项目路线图

## 当前基线

`agentic-dev` 当前稳定 baseline 聚焦 **AI Agent 从需求 / 架构澄清到代码、验证、收敛与 Ready to Integrate** 的可复用软件开发能力。

当前稳定基础包括：

- Requirement Baseline Establishment、条件式 Architecture Clarification 与 `method:ai-development`；
- V4 Rule Discovery、Capability Model v2、Project / Capability knowledge boundary 与 Consumer-local adoption / upgrade；
- Review Governance、Human Review、Project Terminology 与 Data Migration governance；
- GitHub / Chat runtime 的 Repository Authority、Rule Discovery、execution transport、deterministic verification 与 human-escalation closure；
- upstream 不维护具体语言 / framework 技术知识 Rule family；technology specialization 由 Consumer-local Authority 持有；
- Issue #164 已完成 R1～R4：核心边界、评估入口、Rule Discovery / Evidence contract、Bootstrap 成本与真实 Consumer applicability 均已完成收敛和独立验证。

上述 baseline 仍是当前已集成运行事实，直到新的产品边界规范完成独立复核并进入后续实施；本轮 Specification 只冻结目标模型，不把尚未实施的语义冒充为当前 runtime。

稳定演进里程碑与历史原因由 `docs/project/project-evolution.md` 持有；精确 branch / Issue / PR / Actions / commit 状态始终从 GitHub 当前事实读取。

## 当前演进

当前进入 **AI 驱动软件开发方法论产品边界重构**。

目标模型已在 exact SHA `6eae3cf192c9ae67eed7f9d3e0aa33ef14d2c338` 完成 Fresh Independent Semantic Review（`Blocking=0`、`Medium=0`）并冻结。当前规范 Authority：

- `docs/project/methodology-product-boundary-specification.md`

Repository-wide disposition 已形成：

- `docs/research/methodology-product-boundary-asset-disposition.md`

实施计划与资产处置已在 exact SHA `0c51232f17738d1351ca638c0f4a184f8524efbf` 完成第二次 Fresh Independent Semantic Review（`Blocking=0`、`Medium=0`）：

- `docs/project/methodology-product-boundary-implementation-plan.md`
- `../research/methodology-product-boundary-asset-disposition.md`

核心方向是重新限定方法论面向普通软件项目，并审查是否可以将：

```text
Guides / Project Knowledge
→ 方法理解与导航

skills/**
→ 唯一 Consumer-facing runtime product

Consumer-local Rules / Policies
→ 项目特有约束
```

作为长期最小模型，同时取消 Provider 与 Consumer 必须运行同构 Capability Runtime 的假设。

上一轮 Issue #172 的 Gate A～G、Release Candidate 与验证 Evidence 保留为历史成果；原 Gate H 暂停且不再作为当前执行路径。旧 `distribution-rebuild-specification.md` 已退出 Current Authority。

## 已完成阶段与当前收敛

Gate P1 — 标准 Skills Distribution 可行性验证已在 exact SHA `f5b1d90e8d3e642045f5ae57b6afb207f6cdbae3` 完成 Fresh Independent Review（`Blocking=0`、`Medium=0`）。Evidence：

- `../research/standard-skills-distribution-feasibility.md`

P1 已确认 GitHub exact tag + 标准 Skills CLI + `skills-lock.json` + Codex native discovery 可以承担普通安装路径；arbitrary commit SHA URL 不是标准 CLI 支持的安装 UX，无版本 generic `update` 也不作为已验证升级协议。

Gate P2 — Canonical Skills 重构已在 exact Skill subject `4918846e411b9797fb705fa0b6695891f190a51e` 完成 Fresh Independent Review（`Blocking=0`、`Medium=0`）。Evidence：

- `../research/canonical-skill-semantic-migration.md`

P2 已完成 15 个 canonical Skill 的语义迁移，移除旧 Release composition metadata 与 Provider docs runtime dependency；28/28 旧 release-input owner 已有明确投影 / disposition；标准安装、Codex native discovery 与 15/15 代表性 behavior semantic grading 均通过。

Gate P3 — Guides / Bootstrap / Navigation 已在 exact candidate `c104b58de4cb5ea78db8e408c8fe37480256a6ef` 完成 Fresh Independent Review（`Blocking=0`、`Medium=0`）。Evidence：

- `../research/methodology-guide-bootstrap-navigation-evidence.md`

P3 已完成 Guide 的 Human + AI 按需导航重构、greenfield Bootstrap、Existing Project 最小 adoption、exact-version Guide locator 和三类 next-step AI 行为验证。Greenfield 首次长任务存在一个非阻塞 Runtime limitation：目标工件已真实建立，但原 Agent process 未正常返回终态；独立只读收口与 Codex native discovery 已验证实际完成边界。该 limitation 不通过增加新的 Bootstrap Framework 解决。

Gate P4 — Consumer-local Constraints 最小方案已在 exact candidate `f7fc76396e50f8524873ba38121564e8031de125` 完成 Fresh Independent Review（`Blocking=0`、`Medium=0`）。Evidence：

- `../research/consumer-local-constraints-minimal-evidence.md`

P4 已冻结第一版最小约定：root `AGENTS.md` 承担极少量 repository-wide stable policy；nested `AGENTS.md` / 宿主原生 scoped instructions 承担 path / module policy；Consumer-local policy docs + 薄 locator 承担 activity / semantic policy；verified no-match 正常继续，broken / uncertain locator fail closed。Codex local 与 ChatGPT + WebCodex 均有验证路径，Skills 安装不覆盖 Consumer policy。

Disposable fixture 没有暴露前三种简单机制的缺口，因此按冻结前置条件没有触发真实软件 Consumer applicability challenge，也没有进入 metadata/filter 设计。旧 `rule-activation-guide.md` 与 `consumer-local-rule-activation.md` 已退出。

当前旧 Provider `rule-discovery lint` 因 P2 已删除 Skill composition metadata 而 fail closed；该 stale verification contract 在 S2 随旧 Rule Discovery current path 一并退出，不通过恢复旧 metadata 处理。

**当前阶段：Minimal Convergence / S1 — Authority Freeze。**

P1～P4 已完成成果保留，不重新执行。原 P5～P9 路线停止继续扩张，剩余工作压缩为：

```text
S1 — Authority Freeze
→ Fresh Independent Semantic Review
→ S2 — Subtractive Cutover
→ S3 — Minimal Validation
→ Provider 极简切换完成，可供采用
```

真实 Consumer adoption 已取消为本轮完成门槛；本轮不修改 `jilinjobs-cms`，也不声称真实 Consumer 已验证。未来采用问题进入正常产品反馈，除非证明产品边界本身存在 Blocking 缺陷，否则不自动重开基础设施重构。

WebCodex Runner 继续禁止直接或间接调用 `codex-cli`；Codex-specific Runtime Under Test 只允许拆成非 WebCodex 独立子任务并由人工临时授权。原 P5 中已产生的 runtime / eval Evidence 保留为历史证据，但不要求把旧批量 authenticated acceptance 路径继续跑绿。

## 后续候选

在 S1～S3 极简收敛完成前，与当前阶段无关的能力扩展保持非活动。尤其不提前新增：

- 新 Method / Rule / Architecture runtime 类型；
- 新中央 discovery / registry；
- 新 custom package / installer；
- 与本轮产品边界无关的 Skill 扩展。

历史 Consumer feedback、Runtime Evidence 与旧 Coverage Audit 可以作为设计证据，但不能反向要求新模型兼容旧实现。

## 已知约束

- 当前已集成 Repository Authority 在新规范正式集成前仍约束本仓 ordinary runtime；
- 新模型必须保留 Progressive Disclosure、Consumer-local Authority、Evidence 与 Fresh Context 等已验证需求；
- Guide 可供 AI 按需使用，不等于进入 ordinary Agent 固定 Bootstrap；
- `skills/**` 成为唯一 Consumer runtime product 不等于把所有知识塞入一个超级 Skill；
- Consumer-local Product / Requirement / System Architecture / technology policy / authorization / current state 不得被通用 Skill 吸收；
- Consumer-local Rules 的需求必须保留，但其发现机制需要重新从最小方案证明；
- 已冻结 Specification 不因实施便利静默改变；若实施计划暴露目标级冲突，必须返回 Specification 重新复核。

## 状态归属

- Repository live state：GitHub；
- 当前已集成项目使命 / 核心要求：`project-charter.md`；
- 当前已集成 Repository runtime instance：`project-capability-profile.md`；
- 新一轮产品边界与 Acceptance：`methodology-product-boundary-specification.md`；
- Repository-wide disposition Evidence：`../research/methodology-product-boundary-asset-disposition.md`；
- 当前实施计划：`methodology-product-boundary-implementation-plan.md`；
- 上一轮发布模型规范：`distribution-rebuild-specification.md`，仅作为历史规范 / Evidence locator；
- 当前 evolution / gate / compact next candidates：本 Roadmap；
- 稳定历史里程碑：`project-evolution.md`；
- bounded unit 的完整 Review / Actions / commit Evidence：对应 GitHub Issue / PR / Actions。

Roadmap 不复制完整重构规范、Architecture、Capability body、历史实施日志或完整 Review Evidence。

---
id: architecture:skill
type: architecture
status: active
distribution: source-only
---

# Skill 架构

## 1. Skill 定义

Skill 是在当前责任已经明确后，拥有稳定独立执行闭环的有界能力：

```text
Trigger / Purpose
→ Inputs
→ Procedure
→ Outputs
→ Exit Conditions
→ Escalation
```

Skill 实现或支持既定 Method responsibility，也可以被其他明确任务直接调用；它不创建隐藏生命周期，不拥有跨多个 Method stage 的项目过程，也不通过自身存在取得仓库写入、集成、发布或部署授权。

## 2. Skill 与 Method

Method 拥有一类复杂工作的过程生命周期；Skill 拥有其中某个明确责任下可复用的执行能力。

判断一个候选是否应成为 Skill，不使用“它有若干步骤”作为充分条件。只有当候选存在稳定 Trigger、Inputs、可重复 Procedure、Outputs、Exit / Escalation，并能作为独立能力被调用和评估时，才 Skill 化。

Method stage 不要求一一对应 Skill。某些阶段可以由 Agent 在当前 Authority 与 Rules 下直接完成；某个 Skill 也可以在多个 Method 中复用。

## 3. Skill 与 Rule

Skill 与 Rule 是正交关系，而不是固定 `Skill → Rule` 流水线。

- Skill 回答“已经决定要做这件事，怎样稳定地完成”；
- Rule 回答“当前条件成立时，必须 / 不得 / 默认怎样做，或完成前必须证明什么”。

Rule 可以约束 Skill execution，也可以独立约束 Method stage、direct Agent work、repository operation、verification 或 completion claim。

容易因 Consumer / Repository Authority 不同而变化的 policy 不应写死进通用 Skill。例如通用 Git / external-operation procedure 可以稳定复用，而不同仓库的 commit type / scope、远程操作授权或表达规范应由目标仓库 Rule / Authority 持有。

具体 Rule 语义边界见 `docs/architecture/rule-architecture.md`。

## 4. Skill 清单归属

Architecture 不持有某个 Repository 当前有哪些 Skill、Skill 总数或当前分类清单。

- `SKILL.md` corpus 是实际 Skill 资源；
- Repository-local Human inventory 可以由 `skills/README.md` 等导航表达，并通过 deterministic validation 与真实 corpus 保持一致；
- Repository 当前是否采用某类 Skill、Skill root 在哪里，属于 Project capability instance；
- Architecture 只定义 Skill 的身份、准入、互操作和组合边界。

因此新增 / 删除 / 重分类某个具体 Skill 不应为了同步 inventory 而修改本 Architecture，除非它暴露了 Skill 类型定义本身的缺陷。

## 5. Agent Skills 互操作

每个 `SKILL.md` 必须遵守当前 Agent Skills Specification。`name` 与 `description` 为 required top-level fields；本仓逻辑 `id/type/status` 通过官方 `metadata` string map 扩展：

```yaml
metadata:
  agentic-dev-id: "skill:example"
  agentic-dev-type: "skill"
  agentic-dev-status: "active"
```

不得添加规范未定义的自定义 top-level metadata key。

具体 Repository 的 Skill root / discovery entry 由其 local capability profile 或等价 Repository Authority 声明；Architecture 不固定仓库路径。

## 6. Skill 作为主要发布单元

首版 Consumer Distribution 以 Agent Skill 为主要运行单元，但这不改变 Skill 的有界职责。

一个发布 Skill 可以按 Agent Skills Specification 使用：

```text
<skill>/
├── SKILL.md
├── references/
├── scripts/
└── assets/
```

其中：

- `SKILL.md` 持有激活后必须整体理解的 bounded instructions；
- `references/**` 按需承载从 Method / Architecture / Rule 等 Source owner 编译出的详细运行参考；
- `scripts/**` 承载适合确定性执行的工具代码；
- `assets/**` 承载模板和静态资源。

supporting resource 只是发布 projection，不取得其来源语义的 Source canonical ownership。

所有 `release-direct` Skill 都必须把 `rule:execution-continuity-and-stop-condition` 声明为 `release-input`，使子操作终态后的责任重算、合法停止条件和成本边界随版本化 Release 进入 Consumer。Skill 只引用该 Rule，不复制其正文；未来新增发布 Skill 也必须满足同一 composition contract，并由确定性测试检查。

`release-direct` 表示当前 Skill 自身可以直接进入 Release；`release-input` 则表示还需要 build transformation / composition。无论哪种 disposition，都不得绕过 Trigger / Inputs / Procedure / Outputs / Exit / Escalation 边界。

首版 repository-local deployment target 可以是 `.agents/skills/**`，但 Architecture 不把这一物理路径提升为 Skill 的跨 Runtime identity。未来其他 Runtime / Plugin target 可以消费同一 canonical Skill source。

## 7. 准入门禁

新增 Skill 至少证明：

- 独立 trigger / purpose；
- 稳定 inputs；
- 可重复 procedure；
- 稳定 outputs；
- 明确 exit / escalation；
- 有界上下文与可组合性；
- 单一语义 owner；
- 有辨识力的行为评估。

仅“重要”“多个阶段都会用”“存在步骤”“多个 Rule 都涉及”“希望减少 Rule 数”不足以升级为 Skill。
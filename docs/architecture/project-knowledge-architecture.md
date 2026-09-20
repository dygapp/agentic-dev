---
id: architecture:project-knowledge
type: architecture
status: active
distribution: source-only
---

# Project Knowledge 架构

## 1. 目标

本 Architecture 定义 **Project Knowledge**、Source capability 与 Consumer Distribution 的长期边界。

旧的“Project 不传播，Capability 传播”需要进一步精确化为：

> **Project 不传播；Source capability semantics 通过 Distribution Build 发布；Source type / path 不直接传播。**

上游 Repository 的 Project Knowledge 描述“这个项目是谁、当前怎样实例化能力、现在走到哪里以及如何演进”；Source Architecture / Method / Skill / Rule 描述 `agentic-dev` 如何拥有和维护长期能力语义；真正给普通软件 Consumer 安装的是经过分类、构建和验证的版本化 Release。

Consumer 可以参考 upstream Project Knowledge 理解 provenance、背景和演进原因，但不得把它机械复制为 Consumer 当前 Authority。

## 2. Project Knowledge 拥有什么

Project Knowledge 只持有当前 Repository / Project 自身的长期事实与稳定摘要，包括：

- 项目使命、要解决的问题、目标、非目标、核心项目需求与成功判据；
- 当前 Repository 如何实例化自身 Source capability / runtime；
- 当前 baseline、当前 evolution、当前 Gate 与下一候选；
- 对理解当前项目仍有长期价值的演进里程碑摘要。

这些内容可以影响本 Repository 的 Agent runtime 与维护决策，但默认不进入 Consumer Release。

## 3. Source capability 拥有什么

Source Architecture / Method / Skill / Rule 等 canonical owner 只持有：

- capability 类型与 semantic ownership；
- 复杂工作生命周期；
- 稳定有界执行 Procedure；
- 条件性 policy / invariant；
- selection / discovery contract；
- provider runtime invariant；
- local specialization / upstream decoupling 等长期边界。

这些 Source owner 是否独立存在，由 authoring / governance responsibility 决定，不由最终 Consumer 目录决定。

一个 Source owner 标记为 `release-input`，只说明它的部分语义需要参与 Release Build；这**不等于**它会以相同类型、文件名或路径出现在 Consumer。

## 4. Distribution 属于独立维度

Distribution classification 不改变 semantic owner。

```text
Project / Research / Guide / Eval
→ 通常 source-only

Method / Architecture / Rule / Tool
→ 可能 release-input
→ build transformation
→ Skill package

Skill
→ 可能 release-direct
→ versioned release
```

真正发布给 Consumer 的 projection 不取得 Source canonical ownership。Release 结构、版本、manifest 和安装 contract 由 Distribution / Build owner 持有，而不是由 Project Knowledge 或某个被编译的 Source owner持有。

## 5. 分类判据

当一个长期事实需要固化时，依次判断：

1. 它只描述当前 `agentic-dev` 的使命、选择、实例、状态或历史吗？  
   → Project Knowledge。
2. 它定义 provider-side 可复用能力的长期语义 owner 吗？  
   → Architecture / Method / Skill / Rule 等 Source owner。
3. 它只是决定某个 Source asset 是否参与 Release、如何转换或落到哪个发布目标吗？  
   → distribution metadata / Build contract。
4. 它只是面向人的解释吗？  
   → Guide / README。
5. 它只是证据 / 探索吗？  
   → Research / Eval / GitHub Evidence。

目录位置不能覆盖这个 semantic-owner 判断。

## 6. Project Knowledge 最小结构

一个成熟 Repository 可以按实际需要维护：

```text
Project Charter
→ Project Capability Profile
→ Project Roadmap
→ Project Evolution
```

它们不是强制文件名，但职责应保持分离。

### Project Charter

回答“项目为什么存在、要解决什么、目标与非目标是什么、哪些项目级需求必须长期满足”。

### Project Capability Profile

回答“当前 Repository 如何实例化自身 capability / runtime”。它可以持有少量 Repository-local selector / locator，但不得退化为中央 catalog，也不得承担 Consumer Release inventory。

### Project Roadmap

只回答“当前正式 baseline、当前 evolution / Gate、下一候选与持续观察事项”。精确 branch / PR / Action / comment 状态仍以 GitHub 为准。

### Project Evolution

只保留对理解今天设计仍有价值的稳定里程碑；完整实施 Evidence 继续由 Git / Issue / PR / Actions 保存。

## 7. Project Capability Profile 不是 Consumer package

`agentic-dev` 的 Project Capability Profile 只描述本仓库自己的 runtime instance，例如 Method selector、Rule Discovery Tool locator、Skill root、execution transport。

它不能：

- 成为 Consumer Release manifest；
- 被 Consumer 复制为本地 profile；
- 决定 Consumer `.agents/**` 的物理结构；
- 保存发布 Skill 的手工 inventory；
- 把 upstream current state变成 Consumer runtime dependency。

Consumer 安装版本化 Release 后，只保留其自己需要的 Repository Authority、installed-release provenance 与 bounded bootstrap integration。

## 8. 演进与退出

Project 文档不因为一次 bounded rebuild 就永久膨胀。Issue #172 的 `distribution-rebuild-specification.md` 只在本轮重构期间拥有冻结 Acceptance；当稳定语义已经回写真实 Architecture / Method / Skill / Build / Release owner，并完成最终 Consumer 验证后，该 bounded specification 按其自身合同退出 Current Authority。

这继续遵守：

> 长期 Project Knowledge 只保存无法由真实 capability owner 或 GitHub native state合理承担的项目事实。

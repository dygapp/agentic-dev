---
id: architecture:project-knowledge
type: architecture
status: active
distribution: source-only
---

# Project Knowledge 架构

## 1. 目标

本 Architecture 定义 **Project Knowledge** 与可复用 Capability 的长期边界。

核心原则：

> **Project 不传播，Capability 传播。**

上游 Repository 的 Project Knowledge 描述“这个项目是谁、当前怎样实例化能力、现在走到哪里以及如何演进”；可复用 Architecture / Method / Skill / Rule 则描述可以被其他 Repository adopt / adapt 的工程能力。

Consumer 可以参考 upstream Project Knowledge 理解 provenance、背景和演进原因，但不得把它机械复制为 Consumer 当前 Authority。Consumer 必须建立并维护自己的 Project Knowledge 与 capability instance。

## 2. Project Knowledge 拥有什么

Project Knowledge 只持有当前 Repository / Project 自身的长期事实与稳定摘要，包括：

- 项目使命、要解决的问题、目标、非目标、核心项目需求与成功判据；
- 当前 Repository 如何实例化通用 Capability contract；
- 当前 baseline、当前 evolution、当前 Gate 与下一候选；
- 对理解当前项目仍有长期价值的演进里程碑摘要。

这些内容可以影响本 Repository 的 Agent runtime 与维护决策，但默认不是可向 Consumer 传播的 reusable capability。

## 3. Architecture 拥有什么

Architecture 只持有能够跨 Repository 复用或被 Consumer adopt / adapt 的长期：

- 能力类型与 semantic ownership；
- 结构关系与组合方式；
- selection / discovery contract；
- runtime invariant；
- local specialization / upstream decoupling 等可复用边界。

Architecture 不应持有某个 Repository 当前恰好存在的 Method 列表、Skill 数量、当前工具路径、当前 baseline、Issue / PR 状态或历史里程碑。

## 4. 分类判据

当一个长期事实需要固化时，优先问：

> 如果一个新的 Consumer 采用了相关 capability，这条事实是否仍应作为它需要考虑的通用结构或运行约束？

- **是**：优先进入 Architecture / Method / Skill / Rule 等 capability owner；
- **否，只描述当前 Repository 的使命、选择、实例、状态或历史**：进入 Project Knowledge；
- **只是面向人的解释**：进入 Guide / README；
- **只是过程证据或临时状态**：优先留在 Git / Issue / PR / Actions。

目录位置不能覆盖这个 semantic-owner 判断。

## 5. Project Knowledge 最小结构

一个成熟 Repository 可以按实际需要维护以下 Project owners：

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

回答“当前 Repository 如何实例化 reusable capability contract”。典型内容包括：

- 当前 work kind → Method locator；
- 当前 Rule root / Rule Discovery implementation locator；
- 当前 Skill discovery entry；
- 当前 Human / Agent entry。

它不得复制完整 Rule / Skill inventory、Rule activation metadata、Method stages 或当前 Issue / PR 状态。

### Project Roadmap

只回答“当前正式 baseline、当前 evolution / Gate、下一候选与仍需持续观察的事项”。

Roadmap 是可恢复的稳定摘要，不代替 GitHub 当前事实。精确 branch / PR / Action / comment 状态仍以 GitHub 为准。

### Project Evolution

只保留对理解今天设计仍有价值的稳定里程碑与主要转折；完整实施证据继续由 Git / Issue / PR / Actions 保存。

Project Evolution 不重新保存每个 Gate、commit 或实验流水账。

## 6. Project Capability Profile 不是运行时目录

Project Capability Profile 可以持有少量**Repository-local capability instance pointers**，但不得退化为中央 catalog：

- 不列出全部 Rule locator；
- 不复制 Rule scope / routing；
- 不复制全部 Skill inventory；
- 不维护当前 Rule candidate set；
- 不保存 Method stages / Gate 正文；
- 不根据 Issue / PR 动态生成 runtime decision。

Rule Discovery、Agent Skills discovery 和具体 Method 正文继续由其真实 owner 工作。

## 7. 使用方边界

Consumer adoption / upgrade 的传播对象是 Capability，而不是 upstream Project state：

```text
upstream Project Knowledge ──→ provenance / understanding only
upstream Capability ─────────→ adopt / adapt / reject
                                ↓
                        Consumer-local Capability
                                +
                        Consumer-local Project Knowledge
```

Consumer-local Project Knowledge 可以使用不同路径和组织形式，但必须独立拥有：

- Consumer 自身使命 / 产品与项目事实；
- Consumer capability instance；
- Consumer current roadmap / work state；
- Consumer 自身演进历史。

upstream Project Charter、Roadmap、Capability Profile 或 Evolution 不因 baseline adoption 自动成为 Consumer Authority。

## 8. 当前状态与证据

Project Knowledge 只保存值得跨上下文长期恢复的稳定摘要。以下内容默认不进入长期 Project 文档：

- 临时施工计划；
- 当前一次 review 的逐条过程；
- 可从 GitHub 直接读取的 Open PR / Issue 列表；
- Actions 日志全文；
- 每个 Gate 的流水账；
- 已由 Git 历史完整保存的中间版本。

当长期 Project 文档与 GitHub 当前事实冲突时：

- 项目使命 / 核心需求以其 Project owner 为准；
- 可变 Repository state 以 GitHub 当前事实为准，并修复陈旧 Project summary；
- reusable capability semantics 仍回到真实 Architecture / Method / Skill / Rule owner。

## 9. 演进原则

新增 Project 文档必须证明存在独立、长期、不可由现有 owner 或 GitHub native state 合理承担的职责。

不得因为“信息重要”就建立新的 `*-design` / `*-audit` / `*-validation` / `*-closure` Project 文档。过程信息优先进入 Issue / PR；稳定结论进入真实 semantic owner。
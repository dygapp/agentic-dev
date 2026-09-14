---
id: architecture:rule
type: architecture
status: active
---

# Rule 架构

## 1. Rule 定义

Rule 是在当前工作事实满足其适用条件时，对工作施加的规范性：

- policy；
- constraint；
- default；
- invariant；
- completion requirement。

Rule 本身不需要形成完整 Procedure，也不要求依附任何 Skill。

## 2. Rule 是横切能力

Rule 可以作用于不同责任表面：

```text
Method stage ─────┐
Skill execution ──┤
direct Agent work ├─→ applicable Rules
repository work ──┤
verification ─────┤
completion claim ─┘
```

因此不得把 Rule Discovery 理解成 `Method → Skill → Rule` 的末端步骤。只要当前 task facts 发生变化并可能改变适用 Rule，当前责任就应重新执行 Rule Discovery。

## 3. Rule 与 Skill

Skill 拥有稳定、有界、可复用的执行 Procedure；Rule 拥有条件性规范约束。二者可以组合，但互不从属。

一个内容更适合 Rule 的典型信号包括：

- 它主要表达“必须 / 不得 / 默认 / 完成前必须证明”；
- 它没有独立 Trigger / Inputs / Procedure / Outputs / Exit 的完整执行闭环；
- 它可能在多个 Skill、Method stage 或 direct work 中横切适用；
- 它容易因 Repository / Consumer Authority 不同而变化。

一个内容不应仅因为“有若干步骤”就自动 Skill 化，也不应为了减少 Rule 文件数量把多个独立 policy 合并成大 Skill。

## 4. Rule granularity

默认一个独立发现单元对应一个 Rule Markdown，但判断粒度的依据不是文件长度，而是**独立规范语义**。

一个 Rule 应独立存在，当它能够：

- 被独立发现；
- 被独立判断适用 / 不适用；
- 被独立修改而不要求同步改变同组其他 policy；
- 单独阅读仍具有完整的约束语义。

如果多条候选 Rule scope 基本相同、运行时总是共同激活、拆开后单独语义不完整且必须共同修改，则应评估合并。反之，即使正文只有一两句，只要拥有独立适用条件和独立演进价值，就不因“太短”而合并。

## 5. Consumer-local specialization

Rule 是 Consumer-local specialization 的主要承载面之一。

例如通用 Skill 可以定义稳定的 Git / external operation procedure，而：

- `agentic-dev` 的 commit type / scope；
- `jilinjobs-cms` 的 commit type / scope；
- 不同仓库的术语、审批、验证、迁移约束；

可以由各自 Consumer / Repository Rule 根据本地 Authority 独立定义。

Consumer adoption / upgrade 可以 adopt、adapt、replace、reject upstream Rule；upstream Rule id、metadata 或正文不会因为 provenance 自动成为 Consumer Authority。Consumer-local Rule 仍应保持 metadata 与规范正文同源维护。

## 6. Discovery metadata 与正文

Rule Front Matter 只负责可确定性筛选的 discovery metadata；Rule body 持有最终规范语义。

metadata 不能成为正文摘要、decision logic 或 exception catalog。目录分类只服务维护和人类导航，不参与匹配。具体 task-signal、locator-only、fail-closed 与规模约束由 `docs/architecture/rule-discovery-architecture.md` 定义。

## 7. Human navigation

`docs/rules/README.md` 或分类 README 可以存在，用于人类说明目录结构、Rule 类别和当前 inventory，但它们：

- 不是 Rule；
- 不进入 ordinary Rule Discovery；
- 不拥有 Rule activation metadata；
- 不维护 Rule → token / keyword / priority 路由；
- 不成为 runtime catalog。

如果 inventory 可以由 Rule 文件机械得到，应优先自动生成或验证，避免人工维护第二份规范事实。

## 8. Rule 演进判断

新增或修改 Rule 时，至少回答：

1. 它表达的是条件性规范约束，而不是完整 Method / Skill Procedure 吗？
2. 它是否拥有独立发现 / 独立适用价值？
3. 它的 semantic owner 是否应由当前 Repository / Consumer 持有？
4. metadata 是否只描述适用范围，而没有复制正文决策逻辑？
5. 是否有足够 Evidence 证明这条约束应长期存在？

只有全部边界清楚后，才进入 Rule Discovery corpus。
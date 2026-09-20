---
id: architecture:rule
type: architecture
status: active
distribution: source-only
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

一个 Rule 文件可以包含围绕同一具体任务或责任、通常共同发现和共同消费的一组相关 policy；**一条 assertion 不等于一个 Rule 文件。**

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

一个内容不应仅因为“有若干步骤”就自动 Skill 化，也不应为了减少 Rule 文件数量把多个不相关 policy 合并成大 Skill。

## 4. Rule 粒度

### 4.1 任务级自然边界

Rule 的默认自然边界是**一个可独立发现的具体任务或责任所需的有界规范语义集合**，而不是最小可陈述句子。

同一任务下的多条 policy 满足以下特征时，应优先聚合为一个 Rule：

- 由相同或高度重叠的 task facts 触发；
- ordinary runtime 中通常共同进入候选并共同消费；
- Agent 完成该任务时通常需要一起知道；
- 合并后仍能整体清楚判断“该 Rule 是否值得加载 / 是否适用于当前责任”；
- 合并不会把明显不同的技术、artifact、risk 或 lifecycle 强行绑在一起。

因此“某条 policy 理论上可以单独表述或单独修改”**不是**必须拆文件的充分理由。

拆分一个候选 Rule 必须证明独立 discovery 具有实际收益，例如：

- 它拥有明显不同的 activity / technology / artifact / risk / lifecycle；
- 独立 metadata 能稳定排除大量不相关任务；
- 仅在少数任务中才需要加载，拆开能显著减少普通上下文；
- 与同组内容具有不同 semantic owner 或独立 Consumer specialization 边界；
- 合并会造成容易误激活的大而杂规范集合。

核心判断是：

> **拆分必须能够减少不必要的规则加载或错误激活，而不能仅证明两条 policy 在逻辑上可以分别表述。**

如果多个候选 Rule scope 基本相同、运行时通常共同激活、共同消费且总是围绕同一任务目的，默认评估合并。反之，即使正文很短，只要拥有真实的独立 discovery 价值，也可以保持独立。

### 4.2 文件大小与渐进披露

Rule 被 Discovery 选中后，模型会读取完整 Rule 正文。因此文件大小应从“单次任务的总发现 + 加载成本”判断，不以“越小越好”为目标。

Agent Skills Specification 的 Progressive Disclosure 提供当前外部工程参照：Skill 被激活后完整加载 `SKILL.md`，官方推荐 instructions 小于约 `5000 tokens`、主 `SKILL.md` 小于 `500 lines`，更细资源再按需加载。研究基线见 `docs/research/agent-skills-specification-analysis.md`。

Rule 比完整 Skill Procedure 更简单，因此本仓把上述 `5000 tokens / 500 lines` 作为**上限复核参照**，不是推荐目标，也不是机械拆分阈值：

- 正常 Rule 应明显小于完整 Skill；
- 接近或超过任一参照时，必须重新检查是否混入多个独立任务、过量示例或非规范参考材料；
- 如果内容仍属于一个任务级规范集合，不为了追求微小文件机械拆成多条 discoverable Rule；
- 详细研究证据、长参考说明或人类教程应回到对应 Architecture / Research / Guide / 其他真实 owner，而不是通过制造 micro-rules 解决文件长度。

本仓不再定义更小的固定行数 / token 数硬门槛；真正优化目标是 ordinary runtime 的候选数量、总正文加载量与语义完整性。

### 4.3 典型任务级分组

例如 `safe-external-write` 可以在同一个外部写责任中共同持有授权确认、最小变更、已有对象复用 / 幂等与写后重新读取，因为这些 policy 通常围绕同一次外部 mutation 共同消费。

而数据库迁移完成证据与通用 completion evidence 可以保持不同 Rule：前者只在特定 artifact responsibility 下有额外完成义务，后者横切更广的 verification claim，独立 discovery 能减少无关加载。

## 5. Rule 目录与人类信息架构

目录只服务维护和人类导航，不参与 runtime matching。Rule Discovery 必须继续只根据每个 Rule 自己的 Front Matter 做候选过滤。

允许按稳定的人类维护维度建立子目录。Consumer 如果确实拥有 local technology Rules，可以按自己的技术栈组织，例如 `docs/rules/technology/<stack>/`；这只是 Consumer-local Human IA，不形成 upstream 必备分类。

`agentic-dev` 自身不为 Vue、TypeScript、Spring 或其他具体技术栈预建 / 维护 Rule family。不得为了目录整齐预建空技术栈，也不得把目录路径当作隐藏 routing signal。

## 6. Consumer 本地特化

Rule 是 Consumer-local specialization 的主要承载面之一。

例如通用 Skill 可以定义稳定的 Git / external operation procedure，而：

- `agentic-dev` 的 commit type / scope；
- `jilinjobs-cms` 的 commit type / scope；
- 不同仓库的术语、审批、验证、迁移约束；

可以由各自 Consumer / Repository Rule 根据本地 Authority 独立定义。

普通软件 Consumer 不再默认逐文件 adopt / adapt upstream Rule。上游通用 Rule 如果标记为 `release-input`，其 Consumer runtime 所需约束应经过 Distribution Build 投影到相关 Skill 的 instructions / references，或在确有必要时形成其他显式 Release owner。

Consumer-local Rule / policy 仍由 Consumer Repository Authority 自己持有。upstream Rule id、metadata 或正文不会因为进入 Release provenance 就成为 Consumer Authority，也不得把 Consumer-specific 授权、术语、技术专项 policy 静默编译进通用 Skill。

## 7. Rule 的 Source / Distribution 边界

Rule 是 `agentic-dev` Source / provider runtime 的条件性规范 owner。Rule Discovery 继续服务本仓自身运行与治理，但**Rule 文件不是首版普通软件 Consumer 的默认发布单元**。

当 Rule 为 `release-input`：

```text
Rule canonical body
→ Distribution Build
→ matching Skill instructions / references
```

Build 必须保留真正与发布 Skill 运行有关的约束，同时避免：

- 把 Rule discovery metadata 当作 Consumer runtime taxonomy；
- 复制 upstream Rule tree 到 Consumer；
- 把多个 Consumer 必然不同的 local policy 固化进通用 Skill；
- 形成需要与 Source Rule 手工同步的第二套 Rule catalog。

Rule Source body 仍是 provider authoring semantics 的唯一 owner；发布 projection 由 deterministic build 从 Current Source 生成。

## 8. 发现元数据与正文

Rule Front Matter 只负责可确定性筛选的 discovery metadata；Rule body 持有最终规范语义。

metadata 不能成为正文摘要、decision logic 或 exception catalog。目录分类只服务维护和人类导航，不参与匹配。具体 task-signal、locator-only、fail-closed 与规模约束由 `docs/architecture/rule-discovery-architecture.md` 定义。

任务级聚合不要求 metadata 精确编码正文中的每个条件分支。metadata 只需要回答“当前任务是否值得加载这一组规范”，更细的适用性继续由读取正文后的语义确认完成。

## 9. 人类导航

`docs/rules/README.md` 或分类 README 可以存在，用于人类说明目录结构、Rule 类别和当前 inventory，但它们：

- 不是 Rule；
- 不进入 ordinary Rule Discovery；
- 不拥有 Rule activation metadata；
- 不维护 Rule → token / keyword / priority 路由；
- 不成为 runtime catalog。

如果 inventory 可以由 Rule 文件机械得到，应优先自动生成或验证，避免人工维护第二份规范事实。

## 10. Rule 演进判断

新增、拆分、合并或修改 Rule 时，至少回答：

1. 它表达的是条件性规范约束，而不是完整 Method / Skill Procedure 吗？
2. 它面向的具体任务 / 责任是什么？
3. 与相邻 Rule 是否通常共同发现、共同消费；如果拆开，是否真的减少无关加载或错误激活？
4. 合并后是否仍保持清晰、有界、可整体判断适用性？
5. 文件大小是否仍适合一次完整加载；接近 Agent Skills 的上限参照时是否完成重新分解复核？
6. semantic owner 是否应由当前 Repository / Consumer 持有？
7. metadata 是否只描述值得加载的范围，而没有复制正文决策逻辑？
8. 是否有足够 Evidence 证明这组约束应长期存在？

只有这些边界清楚后，才进入 Rule Discovery corpus。
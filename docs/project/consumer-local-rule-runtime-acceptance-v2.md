# Consumer-local 规则运行验收矩阵 v2

## 状态

**Phase A / A2 结果 — Consumer-local Acceptance Baseline**

上层目标模型：

`docs/project/consumer-local-rule-runtime-target-v2.md`

上层里程碑：Issue #92 / `docs/project/rule-governance-knowledge-activation-v2.md`

本文把 A1 目标模型转换为后续设计、实现与真实 Consumer 验证必须满足的可观察行为。它不预设 metadata schema、物理目录或运行时工具。

## 1. 验收原则

v2 的最终有效性优先由 **Consumer-local 行为正确性**判断。

以下指标不能单独构成 PASS：

- token 减少；
- 文件读取减少；
- Catalog 命中；
- Skill 被成功加载；
- eval 进程退出码为 0；
- `agentic-dev` 自身场景表现良好。

必须先证明：

1. Consumer Repository Authority 没有被覆盖；
2. ordinary runtime 不依赖 upstream；
3. 当前任务取得最小充分规则与 Authority；
4. responsibility / Stage Return 正确；
5. stale / missing / conflict 能安全 fail-closed；
6. baseline adoption 后的本地状态可以跨 Fresh Context 持续恢复。

效率指标只在语义正确后用于比较候选设计。

## 2. 验收层级

### L1 — 静态一致性

不调用 Agent 也能检查：

- discovery entry 可定位；
- metadata / pointer 指向存在的 Consumer-local owner；
- provenance 与 exact baseline 可追溯；
- 没有同一规范性规则的多份正文 owner；
- stale / superseded relation 可检测；
- rejected / not-applicable candidate 不进入普通 runtime 激活集合。

### L2 — 隔离 Fresh Context 行为

在新的、无历史聊天依赖的 Agent Context 中验证：

- 只从 Consumer Repository 启动；
- 不允许读取 upstream；
- 只暴露当前 Consumer 实际本地资产；
- 观察 discovery、routing、Skill activation 与 Authority 读取路径；
- 人工按隐藏 expected behavior 评分。

### L3 — 真实 Consumer 持续使用

在真实 Consumer 的正常工作流中验证：

- baseline adoption / upgrade 后普通工作恢复 Consumer-local；
- 新任务可以持续发现本地规则；
- Consumer-native rule 与 adopted reusable rule 能共同工作；
- 项目演进后 metadata / owner 更新没有形成长期维护失控；
- upstream 后续提交不会静默改变 Consumer runtime。

v2 最终完成至少要求 L1 + L2 + 一个真实 Consumer 的 L3。

## 3. 场景矩阵

### CL-01 — 普通单一职责发现

**目的**：证明明确任务不需要读取完整 Consumer Method / Guide 栈。

输入特征：

- Consumer Repository Authority 已存在；
- 当前任务明显属于一个稳定职责，例如技术规划或单 Unit 执行；
- 没有产品、架构或授权冲突。

必须：

- 从 Consumer-local discovery entry 找到正确 primary responsibility；
- 只读取该职责必要的 rule/module/Authority；
- 真正执行职责时才加载对应 Skill；
- 不访问 upstream。

不得：

- 默认读取所有 Skill / Guide / Method；
- 因为任务简单而跳过 Consumer Authority。

### CL-02 — 多信号职责与 Stage Return

**目的**：证明 discovery 不是关键词式平铺激活。

输入特征：

- 当前已处于 Execute；
- 新证据表明一个决定需要跨 Unit 持续协调或改变共享 Architecture Context；
- 没有 Observed Defect / Unexpected Failure。

必须：

- `technical-plan` 成为 primary responsibility；
- execution / readiness 只作为 supporting context；
- 当前 Execute 停止并 Stage Return；
- 不误进 `systematic-debug`；
- 如果上游 HOW / Architecture basis 实质变化，旧 Readiness 不继续授予 Execute。

### CL-03 — Consumer-specific rule 覆盖 reusable default

**目的**：证明统一发现不等于上游规则优先。

输入特征：

- adopted reusable rule 提供一般默认值；
- Consumer Architecture / Repository Rule 对当前项目有更具体、合法的约束；
- 两者都能被 discovery 找到。

必须：

- 明确识别 Consumer-specific Authority 的更高适用性；
- 使用 Consumer-specific rule；
- reusable default 只保留背景 / fallback 角色；
- 不把差异自动判断为 Consumer 错误。

如果无法确认 Consumer override 的 current identity，应 fail-closed 到 Consumer Authority，而不是在线拉取新 upstream 取代它。

### CL-04 — Consumer-native Domain / Architecture Rule 发现

**目的**：证明 v2 不只是 `agentic-dev` Skill 路由器。

输入特征：

- 当前任务需要一个只存在于 Consumer Domain / Architecture / Verification Authority 的项目规则；
- upstream 没有等价项目事实。

必须：

- 本地 discovery 能定位 Consumer-native owner；
- Agent 读取并遵守该项目规则；
- 不尝试从 reusable Skill 推断或补造业务 / 架构事实；
- 不访问 upstream。

### CL-05 — Routing-only 不机械加载 Skill

**目的**：验证 Discovery 与 Skill Execution 解耦。

输入特征：

- 当前问题只要求判断下一职责 / Stage Return；
- 不需要真正执行该职责。

必须：

- 能通过 metadata / small rule module 完成正确 routing；
- 如果现有 module 已足够，不要求读取完整 Skill；
- 最终指出下一责任与理由。

不得因为“发现了 Skill”就把 Skill 正文作为固定 runtime 成本。

### CL-06 — 真正进入职责时按需加载 Skill

**目的**：证明 routing 成功后仍能执行完整职责。

输入特征：

- 当前任务已经明确进入某项稳定职责；
- 对应 Skill 已在 Consumer-local capability set 中采用并可解析。

必须：

- 只加载当前 primary responsibility 所需 Skill；
- supporting rule 不导致无关 Skill 批量加载；
- Skill 读取 Consumer Current Authority 后执行；
- Skill 不覆盖 Consumer-specific facts。

### CL-07 — Stale metadata / source pointer

**目的**：证明派生发现信息不会变成陈旧第二 Authority。

输入特征：

- semantic owner 已变化、移动、被取代或内容 identity 改变；
- discovery metadata 仍对应旧 source identity。

必须：

```text
检测 stale
→ 停止信任旧 metadata
→ fail-closed 到 Consumer Current Authority / Authority Map
→ 重建或修正本地 discovery
```

不得继续用旧 metadata 声称规则集合完整。

### CL-08 — Missing / no-match / ambiguous discovery

**目的**：验证安全回退而不是追求强制命中率。

至少覆盖：

- pointer missing；
- metadata 无匹配；
- 多个候选无法可靠区分；
- 当前任务具有新的未知 condition / risk。

必须：

- 明确报告发现不充分；
- 回到 Consumer-local Current Authority；
- 必要时扩大本地读取范围；
- 高影响场景不在不确定状态下继续。

不得默认访问 upstream 作为 ordinary runtime fallback。

### CL-09 — Baseline adoption：adopt / retain-or-override / reject

**目的**：验证 upstream 能力真正变成 Consumer-local 长期状态。

输入特征：

- 当前 Consumer 已记录 baseline；
- 新 baseline 包含多项规则 / Skill / Guide 变化；
- 其中至少一项适合 adopt、一项应保留 Consumer override、一项不适用。

必须：

- 精确比较 baseline；
- 区分 reusable 与 `agentic-dev` project-only；
- 对候选逐项分类；
- 只把需要持续约束的 adopted change 投射为本地可发现资产；
- 保留 provenance；
- rejected candidate 不进入普通 runtime；
- 完成后 ordinary runtime 再次只依赖 Consumer-local。

### CL-10 — Upstream 演进不自动改变 Consumer runtime

**目的**：验证 Consumer 自治。

输入特征：

- Consumer 已完成某 baseline adoption；
- upstream 后续出现新提交或新规则；
- Consumer 尚未执行新的 baseline upgrade。

必须：

- Consumer ordinary Fresh Context 行为保持不变；
- discovery 只依据本地已采用状态；
- 不因为远端最新版本存在就自动升级、覆盖或新增规则。

### CL-11 — Supersede / removal 不残留双重激活

**目的**：验证长期演进后不会新旧规则同时有效。

输入特征：

- 一个已采用 reusable rule 或 Consumer-native rule 被新本地决定取代；
- 旧 metadata / pointer 曾可被发现。

必须：

- 新 owner / current state 可发现；
- 旧 owner 明确 superseded / inactive，或从普通激活集合移除；
- provenance / history 可以保留，但不参与 Current routing；
- 不出现新旧规则正文同时作为 current owner。

### CL-12 — Discovery layer 可删除 / 可重建

**目的**：证明 Catalog 不成为 Authority。

输入特征：

- 删除纯派生 discovery catalog，保留所有 Consumer semantic owners 与 adopted local assets。

必须：

- 不损失任何规范性项目事实；
- 能从当前 Consumer-local Authority / adopted asset identities 重建 discovery；
- 重建后行为与删除前的 current semantics 一致；
- 如果无法重建完整集合，应 fail-closed，而不是猜测恢复。

## 4. 真实 Consumer 最终验证的最小组合

最终 L3 不要求把 CL-01～CL-12 每项都做成昂贵独立模型运行，但必须覆盖以下组合：

### 组合 R1 — Ordinary Fresh Context

覆盖：CL-01 + CL-04 + CL-06。

证明 Consumer-local discovery 能同时找到一个 Consumer-native rule 与一个 adopted reusable responsibility，并真正进入一个 Skill。

### 组合 R2 — Stage Return / ambiguity

覆盖：CL-02 + CL-05 + CL-08。

证明复杂任务不会靠批量激活解决歧义，并能在只需 routing 时停止。

### 组合 R3 — Consumer override

覆盖：CL-03。

必须存在一个真实 Consumer-specific override 与 reusable default 的竞争场景；这是 Consumer Authority 优先的核心门禁。

### 组合 R4 — Baseline upgrade lifecycle

覆盖：CL-09 + CL-10 + CL-11。

至少观察一次真实 baseline upgrade 或受控 adoption fixture，证明 adopt / override / reject 与后续 upstream 演进边界。

### 组合 R5 — Stale / rebuild

覆盖：CL-07 + CL-12。

可以使用受控、无语义的 source identity 漂移或临时 catalog 删除，不要求为了测试破坏真实 Consumer Authority。

## 5. 评分维度

每个隔离行为场景至少记录：

### 5.1 语义正确性

- primary responsibility；
- supporting context；
- Authority precedence；
- Stage Return / Continue；
- Skill activation；
- fail-closed；
- Human escalation；
- completion / evidence claim。

### 5.2 发现质量

- 必需规则是否遗漏；
- 无关规则是否过激活；
- 是否加载完整大文档作为“保险”；
- 是否因为关键词命中选择错误责任；
- 是否能解释每个 supporting module 的任务关系。

### 5.3 Consumer-local 独立性

- ordinary runtime 是否访问 upstream；
- 是否依赖旧聊天 / memory；
- 当前结果能否只由 Consumer Repository / local capability set 重现；
- upstream 后续变化是否静默影响本地行为。

### 5.4 维护与 Authority 健康度

- 是否出现重复规范性规则正文；
- metadata 是否只保留发现信息；
- owner / provenance / supersede 是否可追溯；
- stale 是否可检测；
- catalog 是否可重建。

### 5.5 效率

只在前四项通过后比较：

- repository / local context bytes；
- input tokens；
- command / file reads；
- wall-clock；
- full Guide / Method / Skill loads；
- fallback 成本。

不预先规定所有 Consumer 都必须达到 v2 临时实验的约 `85%` 降幅；最终要求是相对 Consumer 当前粗粒度恢复路径具有可证明的实际收益，同时不降低正确性。

## 6. PASS / INCONCLUSIVE / REJECT

### PASS

一个候选设计只有同时满足以下条件才可进入下一阶段：

- 所覆盖场景无 Blocking / Medium 语义错误；
- Consumer Authority precedence 正确；
- ordinary runtime 不依赖 upstream；
- 没有无理由规则 / Skill 过激活；
- stale / missing / ambiguity fail-closed 正确；
- adopted capability 可以跨 Fresh Context 本地恢复；
- 没有形成第二套 Authority。

### INCONCLUSIVE

例如：

- 只能证明 token 减少，无法证明 semantic owner；
- 某些行为依赖 eval prompt 暗示；
- Consumer-local 与 upstream 的边界无法从运行证据确认；
- supporting context 是否合理无法判定；
- baseline lifecycle 尚未实际验证。

INCONCLUSIVE 不得被描述为 v2 已验证。

### REJECT

任何以下情况直接拒绝当前候选设计：

- Consumer Requirement / Architecture 被 reusable default 覆盖；
- ordinary runtime 必须持续读取 upstream；
- stale discovery 继续授权高影响动作；
- metadata / Catalog 保存第二份规范性正文；
- baseline upgrade 自动覆盖 local override；
- rejected / superseded rule 仍参与 Current routing；
- 为了发现必须批量加载全部规则 / Skill；
- 真实 Consumer 无法在 Fresh Context 中恢复同一行为。

## 7. Phase A 结论

A1 与 A2 共同冻结了 v2 的 Consumer-local 目标和验收基线，但仍没有冻结具体实现。

后续 Phase B 必须以本矩阵反向审计规则 ownership：

> 哪些规则真的需要成为独立激活单元？它们的唯一 semantic owner 在哪里？哪些应该由现有 Skill 拥有？哪些是跨 Skill conditional rule？哪些只属于 Consumer adoption / bootstrap？哪些只是 `agentic-dev` 项目规则、解释性内容或重复内容？

只有完成这项 ownership 审计，Phase C 才能定义最小 metadata / Catalog schema；不得根据临时 G-min manifest 直接开始实现。

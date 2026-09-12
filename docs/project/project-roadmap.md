# 项目演进路线与当前状态

本文是 `agentic-dev` 仓库自身的 Project Roadmap，只维护**当前有效路线、活动状态、候选库、下一门禁与 Fresh Context 恢复入口**。

本文属于 `docs/project/*` 项目级 Authority，不覆盖更高优先级的方法、架构、契约、工程纪律或技术画像，也不得被 Consumer 自动继承。历史实施流水、精确 PR / Run / Review 证据由对应项目记录、Git、PR、Issue、Actions 与 `evals/` 保存；本文不重复维护完整历史证据。

## 1. 当前状态

长期阶段：

> **工程能力扩展与方法演进**

最近完成并已集成的有限里程碑：

> **规则治理与知识激活 v3 — 知识与能力所有权收敛**

当前活动有限规划里程碑：

> **无。下一有限里程碑尚未选择。**

v3 跟踪入口：Issue #94；Independent Review：Issue #118。  
V3-01 — 知识与能力所有权模型已完成并集成。  
V3-02 — 当前仓库所有权审计已完成并集成。  
V3-03 — 使用方初始化、采用、升级与普通运行生命周期已完成并集成。  
V3-04 — 技能重分类与准入已完成并集成。  
V3-05 — 面向 Agent 的结构化资源模型已完成并集成。  
V3-06 — 资源发现架构已完成并集成。  
V3-07 — `agentic-dev` 自采用与发现机制切换已完成并集成。  
V3-08 — Consumer 验证与持续有效性复核已完成；Issue #115 已以 `completed` 关闭。  
V3-08 工作产物：`docs/project/rule-governance-v3-v3-08-consumer-validation.md`、`tasks/plans/20260911/06-rule-governance-v3-v3-08-consumer-validation.md`；历史精确 Evidence 以 Issue #115 为准。  
V3-08 启动基线：`master@2fe193035c629f6b8805fd473bd322f70fe6e172`。

v3 Independent Review 已完成 Gate A～Gate D：

- 复核对象冻结基线：`agentic-dev@86fe96756c7b3678d7b0bac10f32358a9372e84c`；
- Gate B 独立复核结果：Blocking=0 / Medium=3 / Low=0 / ADR candidate=0；
- Gate C 已对 current-state / recovery surface、completed project-record lifecycle、first-adoption Evidence durability 三项 Medium 做最小修复并完成定向复核；
- Gate D 最终结果：**Blocking=0 / Medium=0 / ADR candidate=0**；
- Closure Decision：**直接关闭 v3**，不创建 ADR，不启动 formal v3 design / implementation planning。

协调计划：`tasks/plans/20260912/01-rule-governance-v3-independent-review.md`。精确 Finding / resolution / closure Evidence 由 Issue #118 保存。

V3-07 已把 `agentic-dev` 自身 ordinary runtime 收敛为：

```text
Local Discovery Entry
+ Reviewed Discovery Map
```

Reviewed Discovery Map 是非规范性派生输入，不进入 Repository Authority；当前没有证据要求额外 Runtime View / Catalog / generator。

V3-08 已用成熟 Existing Consumer 与 first-adoption Evidence 验证 V3-03～V3-07 的长期语义。Independent Review 没有发现要求修改 V3-03 / V3-05 / V3-06 / V3-07 reusable Architecture 的 Blocking / Medium；原 E-02 `/tmp` fixture 的底层 Evidence durability 缺口已由 `docs/project/evidence/v3-08-first-adoption-fixture/` 的 GitHub-addressable replacement fixture 与 targeted revalidation 收敛，不把它提升为 Consumer template 或 mandatory runtime structure。

v3 已关闭后，Issue #94 / #118 及相关 `docs/project/*` 记录继续作为项目历史与 Evidence；它们不再提供新的 Planning / Execute / Review Authority。当前没有活动 v3 Gate，也没有自动获得权限的后续候选。

当前门禁：

> **无活动有限里程碑。下一步只允许恢复当前 Repository State、处理已存在的明确维护 / feedback 工作，或由人工选择新的有限里程碑；不得从 v3 closure 自动启动 WI-06、WI-07、WI-09、Issue #71 或其他候选。**

详细已完成规划 / 审计 / 架构 / 自采用 / Consumer 验证：

- `docs/project/rule-governance-knowledge-activation-v3.md`
- `docs/project/knowledge-capability-ownership-model-v3.md`
- `docs/project/current-repository-ownership-audit-v3.md`
- `docs/architecture/consumer-lifecycle.md`
- `docs/project/skill-reclassification-admission-v3.md`
- `docs/architecture/agent-resource-model.md`
- `docs/architecture/resource-discovery-architecture.md`
- `docs/project/rule-governance-v3-v3-07-self-adoption.md`
- `docs/project/rule-governance-v3-v3-08-consumer-validation.md`
- `docs/project/evidence/v3-08-first-adoption-fixture/README.md`
- `docs/project/evidence/v3-08-first-adoption-fixture/revalidation.md`
- `docs/discovery/README.md`
- `tasks/plans/20260911/06-rule-governance-v3-v3-08-consumer-validation.md`
- `tasks/plans/20260912/01-rule-governance-v3-independent-review.md`

## 2. v3 当前路线

v3 已按以下顺序完成：

1. V3-01 — 知识与能力所有权模型 — **已完成并集成**；
2. V3-02 — 当前仓库所有权审计 — **已完成并集成**；
3. V3-03 — 使用方初始化、采用、升级与普通运行生命周期 — **已完成并集成**；
4. V3-04 — 技能重分类与准入 — **已完成并集成**；
5. V3-05 — 面向 Agent 的结构化资源模型 — **已完成并集成**；
6. V3-06 — 资源发现架构 — **已完成并集成**；
7. V3-07 — `agentic-dev` 自采用与发现机制切换 — **已完成并集成**；
8. V3-08 — Consumer 验证与持续有效性复核 — **已完成**；
9. Independent Review — **Gate A～Gate C 已完成**；
10. V3 Closure Decision — **Gate D 已完成：Blocking=0 / Medium=0 / ADR candidate=0，直接关闭 v3**；
11. 必要 ADR — **未进入；Independent Review 没有形成真实 ADR candidate**。

上述顺序是已完成路线记录，不授予任何后续候选执行权限。

V3-01 建立四维所有权判断：

```text
语义所有者
+ 适用范围 / 来源状态
+ 运行 / 生命周期角色
+ 载体 / 权威形式
```

V3-02 完成当前仓库语义所有权审计。V3-03 将使用方生命周期提升为长期可复用工程能力。V3-04 确认当前 9 个 Skill 身份并固定 Skill 准入 / 支持资源边界。V3-05 建立：

```text
规范 / 事实正文
→ 资源固有结构
→ 派生发现投影
```

V3-06 建立长期发现架构：

```text
本地当前资源与稳定入口
→ 可选 Reviewed Discovery Map
→ 可选纯生成 Runtime View
→ 临时发现决策
```

V3-07 根据本仓库真实复杂度选择**一个 Reviewed Discovery Map、无 Runtime View**，并把 `agentic-dev` 自身 ordinary runtime 入口切换到 `docs/discovery/README.md`。旧手工 Guide routing 已显式退出 current discovery responsibility。

V3-08 通过真实 Existing Consumer、完整持续演进和 first-adoption coverage 验证上述 owner / lifecycle / discovery semantics 可以被局部采用、保持 Consumer Authority 优先，并在 ordinary runtime 中持续运转。

Independent Review 又独立挑战 `86fe967…` 冻结 subject 上的 V3-01～V3-08 与 PR #117 后的一致性状态；Gate B 发现的三项 Medium 均在 Gate C 以最小范围解决并重新复核。Gate D 最终确认 Blocking=0 / Medium=0 且无真实 ADR candidate，因此没有继续制造 ADR / formal design / implementation work 的依据。

## 3. v2 已集成基线与兼容退出

规则治理与知识激活 v2 已通过 PR #93 集成。其 Phase A～G 已验证并继续受 v3 保护的行为至少包括：

- 薄启动入口；
- 仓库 / Consumer 权威优先；
- 渐进式披露；
- 证据先于结论；
- 规范正文单点所有权；
- 派生发现机制不拥有规范正文；
- 陈旧 / 缺失 / 歧义时失败关闭；
- 主职责与最小辅助上下文分离；
- routing-only 不机械加载完整 Skill；
- 真正进入职责时按需加载 Skill；
- Stage Return 后重新判断；
- Consumer 普通运行只依赖 Consumer-local current resources；
- 基线逐项采用；
- 同一运行范围 / 发现职责不并行维护多个 current 派生机制。

V3-03～V3-06 已把这些长期语义分别提升到使用方生命周期、资源模型和资源发现架构。V3-07 已把 `agentic-dev` 自身仍 current 的 v2 手工发现 surface 降级为 Guide / historical / compatibility 角色，并建立唯一 current self-runtime discovery mechanism。

V2 项目记录继续保留历史设计与验证证据价值；它们不因为被长期架构取代而删除。V3-08 按 claim-level Evidence reuse 规则复用仍未被新语义改变的历史 Consumer evidence，并用隔离 fixture 补齐无法复用的 first-adoption 语义；Independent Review Gate C 进一步把该 first-adoption raw Evidence 固化为 GitHub-addressable replacement fixture。任何这些项目记录都不因为保留而重新取得 ordinary runtime 或 current-state Authority。

## 4. 当前范围边界

v3 与 Independent Review 已完成并关闭当前有限里程碑；**当前没有继承自 v3 的活动 Planning / Execute / Review Authority**。

当前可以：

- 按 AGENTS / README / Roadmap / GitHub current state 恢复仓库状态；
- 处理已经存在且具有明确 Authority 的维护、缺陷、Consumer feedback 或研究 Evidence；
- 在人工选择新的有限里程碑后，为该里程碑建立新的 Planning Authority；
- 继续维护 v3 已建立的长期 Architecture / Method / Skill / discovery 资产，但变更必须由新的真实需求与当前 Authority 支持。

当前仍不自动：

- 重新打开 V3-01～V3-08；
- 修改 Consumer Repository；
- 把 `agentic-dev/docs/discovery/*` 实例复制给 Consumer；
- 强制 Consumer 建立 Reviewed Discovery Map / Runtime View / Manifest / Catalog；
- 用文件大小 / token 优化覆盖 correctness / Authority / fail-closed；
- 把单一 Consumer 或 fixture 事实泛化成所有 Consumer 的通用结论；
- 因 v3 closure 自动创建 ADR、正式设计或实现规划；
- 自动启动 WI-06、WI-07、WI-09、第四工程纪律或 Issue #71 候选实施。

临时 GPT-6 / 其他 AI 评估只作为挑战和复核证据，不自动提升为长期架构，也不授予后序执行权限。

## 5. 候选库

### WI-07 — 代码复核能力 v1

仍是独立候选，当前不启动。是否成为下一有限里程碑，需要新的人工路线选择与当时 Repository Evidence 支持。

### WI-06 — 第二及后续技术画像

未启动。Spring / Spring Boot / Gradle / Element Plus 等继续作为候选；是否进入下一有限里程碑仍需当前证据和人工路线决策。

### WI-09 — 运行时适配与分发

未启动。Marketplace、Plugin Bundle、Controller、统一安装 / 分发和 Codex 多模型协同采用适配继续作为候选。

### Issue #71 — 模型路由与盲测对照证据

继续作为独立规划 / 研究输入，不构成常规 Method Gate、新 Skill 或默认模型策略。

Issue #58 继续承担长期 Consumer feedback 入口；其中新证据只有经过 `agentic-dev` 自身分类与准入后才能改变长期权威。

## 6. 已完成里程碑 / 子阶段索引

普通 Fresh Context 不默认读取以下已完成工作的完整过程记录：

1. 工程能力基础 v1 — `docs/project/engineering-capability-foundation-v1-closure.md`
2. 工程纪律扩展 v1 — `docs/project/engineering-discipline-expansion-v1*.md`
3. 中文交互与上下文清理 v1 — `docs/project/chinese-interaction-context-cleanup-v1.md`
4. 工程术语语义安全与现行文档收敛 v1 — `docs/project/terminology-semantic-safety-v1.md`
5. Squash Merge 下 Stacked PR 集成拓扑安全 v1 — `docs/project/stacked-pr-squash-topology-v1.md`
6. 规则治理与知识激活 v1 — `docs/project/rule-governance-knowledge-activation-v1.md`
7. 规则治理与知识激活 v2 — `docs/project/rule-governance-knowledge-activation-v2.md`
8. v3 / V3-01 — `docs/project/knowledge-capability-ownership-model-v3.md`
9. v3 / V3-02 — `docs/project/current-repository-ownership-audit-v3.md`
10. v3 / V3-03 — `docs/architecture/consumer-lifecycle.md`
11. v3 / V3-04 — `docs/project/skill-reclassification-admission-v3.md`
12. v3 / V3-05 — `docs/architecture/agent-resource-model.md`
13. v3 / V3-06 — `docs/architecture/resource-discovery-architecture.md`
14. v3 / V3-07 — `docs/project/rule-governance-v3-v3-07-self-adoption.md`、`docs/discovery/README.md`
15. v3 / V3-08 — `docs/project/rule-governance-v3-v3-08-consumer-validation.md`、Issue #115
16. v3 / Independent Review — Issue #118、`tasks/plans/20260912/01-rule-governance-v3-independent-review.md`
17. 规则治理与知识激活 v3 总体 — Issue #94、`docs/project/rule-governance-knowledge-activation-v3.md`

**Completed project-record lifecycle boundary：** 上述 `docs/project/*` 已完成项目记录继续保留项目历史、设计过程与 Evidence 价值；其中写下的 `状态`、`当前 Gate`、`下一步`、`剩余门禁` 只表示该记录形成时的 snapshot。完成后的 current project state、授权与下一 Gate 统一由本 Roadmap + 对应 current Issue + GitHub native state 恢复。旧 project record 即使仍被本索引引用，也不能恢复已经终止的 Planning / Execute / Review Authority。

V3-03 / V3-05 / V3-06 的 `docs/architecture/*` 文件不是历史 project record；它们继续作为 current reusable Architecture owner。V3-07 的 `docs/discovery/README.md` 也继续作为本仓库 current Local Discovery Entry；只有同阶段的 `docs/project/rule-governance-v3-v3-07-self-adoption.md` 属于完成项目记录 / Evidence snapshot。

因此：

- `knowledge-capability-ownership-model-v3.md` header 中旧“候选基线”状态不再表示 V3-01 未完成；
- `rule-governance-v3-v3-07-self-adoption.md` 中旧“剩余门禁”不再具有当前执行意义；
- `rule-governance-v3-v3-08-consumer-validation.md` 中 Gate A / Consumer write 尚未开始等表述只表示当时设计 snapshot；
- `rule-governance-knowledge-activation-v3.md` 中旧“规划中”与早期 Independent Review Gate 表述只表示 v3 执行时 snapshot；
- 当前精确完成状态以本 Roadmap、Issue #94 / #118 closure Evidence、已关闭子 Issue 与 GitHub state 为准。

该边界不把 Roadmap 变成这些文档长期语义的第二 owner；它只拥有**当前项目状态与完成记录的生命周期解释**。

## 7. Root Bootstrap 与本地发现职责

为控制 Fresh Context 成本：

- `AGENTS.md`：稳定 Repository Governance、Authority Boundary 与 Agent 工作约束；不维护当前项目状态；
- `README.md`：简短当前状态与稳定导航；
- 本 Roadmap：详细项目路线、活动状态、候选与下一门禁；
- Git / PR / Issue / Actions：精确外部状态与执行证据；
- `docs/discovery/README.md`：只有需要跨资源判断职责 / 条件性能力时才进入的 Local Discovery Entry；
- `docs/discovery/reviewed-discovery-map.md`：非规范性派生发现映射，不保存项目状态或第二 current truth。

如果当前工作只是状态恢复、确认 Gate 或回答仓库事实，在读取 AGENTS / README / Roadmap / GitHub 当前状态后即可停止，不机械读取 Map 或所有 Skill。

Consumer 的采用与 ordinary runtime 始终遵守 Consumer 自己的 Repository Authority；`agentic-dev` 自身发现入口和 Map 不自动成为 Consumer runtime input。

## 8. Fresh Context 恢复顺序

新的 `agentic-dev` 上下文应：

1. 读取根 `AGENTS.md`，恢复稳定 Repository Governance 与 Authority Boundary；
2. 读取根 `README.md`，取得简短当前状态；
3. 读取本文，确认当前路线、门禁和候选边界；
4. 重新读取执行时当前 GitHub `master`、Open PR / Issue 和必要 Actions；
5. 当前没有活动有限里程碑时，不默认读取已关闭的 Issue #94 / #118；只有追溯 v3 closure 或 Independent Review Evidence 时才读取；
6. V3-01～V3-08、Independent Review 与相关项目记录均属于已完成项目 / Evidence；只有当前任务需要挑战具体 claim 时才按 locator 最小扩读；
7. M-03 first-adoption durable Evidence 位于 `docs/project/evidence/v3-08-first-adoption-fixture/`，只有复核历史 Finding 或 Track E claim 时读取，不加入 ordinary self-runtime discovery；
8. 只有当前 `agentic-dev` 任务需要跨资源发现时读取 `docs/discovery/README.md`，并按需进入 Reviewed Discovery Map / current semantic owner；
9. 只有具体工作需要追溯时才最小读取 v2 historical Evidence、Research 或 Eval；不重新做已完成阶段设计；
10. 新的有限里程碑必须由当前 Repository Evidence 与人工路线选择建立新的 Planning Authority，不能从 v3 closure、候选库排序或历史会话自动继承；
11. 不依赖其他聊天、历史会话或个人记忆补充未固化项目事实。

## 9. 更新触发

出现以下情况时更新本文：

- 当前有限里程碑或子任务门禁实质变化；
- 人工选择新的活动里程碑；
- 长期路线、候选优先级或完成定义改变；
- 新能力正式集成并改变 Fresh Context 恢复路径。

单次 Run ID、临时分支删除、PR 从 Draft 变为 Ready、PR 合并提交等纯 GitHub 原生状态不为了记录而机械写入 Roadmap；需要时直接从 Git / PR / Issue 恢复。
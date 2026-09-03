# 工程纪律基线

**状态：** Baseline v0.2 Validated Draft / Pending Integration  
**性质：** 工程纪律（Engineering Discipline）规范性基线

## 1. 目的

本文定义 `agentic-dev` 当前三个跨技术栈工程纪律：

1. **Implementation Minimality & Speculative Complexity Control（实现最小化与推测性复杂度控制）**；
2. **Surgical Change & Diff Scope Control（精准修改与差异范围控制）**；
3. **Data Access Scope & Boundedness Control（数据访问作用域与有界性控制）**。

本文不增加新的 Method Stage，不改变 Execution Unit、Human Escalation、Ready to Integrate 或 Integration Boundary，也不因为新增工程纪律创建新的 Task-oriented Skill。

首批两个 Discipline 已由 PR #48 完成 Fresh Runtime Targeted Eval 并进入当前 Repository Authority。第三项 Discipline 已在 Engineering Discipline Expansion v1 中完成 Draft 与 Fresh Runtime Targeted Eval，当前为 Validated Draft / Pending Integration；只有包含本 Draft 的变更实际进入当前集成分支后，第三项 Discipline 才成为现行 Repository Authority，未合并 PR / Draft 分支不提前覆盖 `master`。

## 2. Architecture Fit Review

### 2.1 首批两个 Discipline

WI-02 / WI-03 的 Research 与 Candidate Design 复核结论为：

- 两个 Candidate 都描述**阶段内部如何高质量实施**，而不是新的开发生命周期，因此属于 Engineering Discipline；
- 两者跨 Vue、Spring、数据库等具体技术栈成立，不属于 Technology Profile；
- 两者没有独立任务入口、Stage Return、稳定独立输出或单独调度价值，不满足 Task-oriented Skill 的独立职责条件；
- 两者可以被 `execute-unit`、未来 Engineering Quality Review、Refactoring Discipline 和 Technology Profile 共同消费，因此不应只写死在单个 Skill 内；
- `execute-unit` 仍是当前主要执行消费者，只需要保留薄执行规则，不复制完整纪律正文；
- 两个纪律职责独立且可组合：前者判断**复杂度为什么需要存在**，后者判断**最终变更为什么属于当前逻辑变化**。

### 2.2 Data Access Scope & Boundedness Control

Engineering Discipline Expansion v1 的 Research / Candidate 见：

`docs/research/data-access-scope-boundedness-analysis.md`

Architecture Fit 结论：**PASS — Engineering Discipline**。

理由：

- 该判断跨前端、后端、REST / GraphQL、数据库和后台任务成立，不依赖单一技术栈，因此不是 Technology Profile；
- 它决定数据访问的正确集合边界、增长 / 有界性、生命周期、window / pagination 和验证边界，不只是数据库性能技巧；
- 它发生在 Execution Unit 实施内部，不改变 Core Method lifecycle；
- 它没有独立任务入口、稳定独立输出或单独调度价值，不满足 Task-oriented Skill 条件；
- `execute-unit` 可以以薄判断消费，不需要新的 Stage Return、持久化 Checklist 或人工确认步骤；
- 它与 Implementation Minimality、Surgical Change 职责独立：分别判断数据边界、复杂度正当性和 diff 责任链。

当前没有证据要求修改 Core Method 或 Engineering Capability Architecture。

## 3. 权威关系

本文受以下更高层权威约束：

1. `AGENTS.md`；
2. `docs/method/ai-development-method.md`；
3. `docs/method/principles.md`；
4. `docs/architecture/engineering-capability-architecture.md`；
5. `docs/architecture/skill-architecture.md`；
6. `docs/architecture/skill-contracts.md`；
7. `docs/decisions/method-decisions.md`。

本文不得：

- 覆盖 Specification / Technical Plan / Architecture / ADR / Consumer Repository Authority；
- 把低影响局部实现判断重新升级成人工确认循环；
- 授予 Merge / Push / Release / Deploy 权限；
- 以“工程质量”为理由扩大当前 Execution Unit 的授权范围。

## 4. 实现最小化与推测性复杂度控制

### 4.1 核心规则

> 在满足当前权威需求、验证责任、有效长期约束和当前工程健康的前提下，选择当前证据能够支持的最低必要复杂度。仅服务假想未来需求的功能、抽象、配置、扩展点、依赖、层次或条件分支，默认不进入当前实现。

最低必要复杂度不是最少代码行、最少文件或最少函数。

### 4.2 当前正当性来源

新增复杂度至少应能追溯到以下一种当前责任：

- 当前 Specification / Execution Unit 的行为或验收义务；
- 当前 Technical Plan、Architecture、ADR、公共契约或迁移义务；
- 当前安全、隐私、性能、可靠性、可观察性、测试性等非功能责任；
- 当前真实存在的多个消费者、变体或共享语义；
- 当前 Repository Rule / Engineering Rule；
- 正确复用现有框架、标准库或依赖所需的薄适配；
- 有当前证据支持、几乎不增加持续理解和维护成本的低复杂度高收益准备。

以下理由默认不足：

- “以后可能会有第二种实现”；
- “以后更灵活”；
- “看起来更企业级”；
- “设计模式一般这么写”；
- “所有值都做成配置更通用”；
- “也许以后会换框架”；
- “先留插件 / Factory / Registry 不会有坏处”。

### 4.3 判断规则

实施前或 JIT Plan 中按需检查：

1. 新增元素解决当前什么责任？
2. 删除它后，当前正确性、验收、验证或有效长期约束会失去什么？
3. 当前仓库、框架、标准库或已有依赖是否已经满足契约？
4. 共享抽象是否来自真实共同语义，而不是表面重复或假想消费者？
5. 现在引入的持续理解、维护和修改成本是否由当前价值支持？
6. 更少元素是否会损害正确性、清晰性、安全、验证或可修改性？

### 4.4 允许的当前复杂度

以下内容不能被机械视为 YAGNI 违规：

- 当前行为所需的失败路径、安全检查和边界处理；
- 当前变更所需测试和验证入口；
- 为安全实施和可验证性直接服务的小规模行为保持重构；
- 已经存在多个真实消费者且语义稳定的抽象；
- Repository Authority 明确要求的配置、迁移、兼容性或非功能措施；
- 为正确复用已有能力所需的薄适配。

### 4.5 配置与能力复用

配置责任和已有能力复用继续遵循现有 `execute-unit` 精确规则：

- 不因字面量存在就机械外部化；
- 没有真实维护者 / 变化来源的动态配置通常属于推测性复杂度；
- 当前运营、部署或流程维护责任已经明确的值不属于 YAGNI 禁止对象；
- 已有框架 / 标准库 / 依赖满足当前契约时优先复用；
- 不把“框架优先”绝对化，也不为了复用扩大依赖面或改变产品行为。

## 5. 精准修改与差异范围控制

### 5.1 核心规则

> 当前 Execution Unit 完成前，应基于最终 diff 重新检查范围。每个有意义的变更区域都必须能够追溯到当前 Unit 的实现责任、验证责任、当前权威同步责任，或本次修改直接产生且必须闭合的必要清理。为当前变化建立安全实施路径所必需的、范围受控且可验证的行为保持重构可以属于当前责任；无法形成责任链的顺带修改应移除、记录或拆分。

范围判断的基本单位是**一个可解释、可验证的逻辑变化**，不是最少行数、最少文件或用户请求的逐字映射。

### 5.2 允许进入当前 diff 的责任类别

有意义的变更区域至少应属于以下一类：

1. **直接实现**：满足当前 Unit Goal / Required Behavior / Completion Condition；
2. **验证责任**：当前 test、fixture、reproduction、verification hook 或验证配置；
3. **当前权威同步**：当前已授权行为变化要求同步的 API / contract / migration / schema / generated reference / operation doc；
4. **必要准备性重构**：当前变化直接触发、行为保持、有当前证据、范围受控的 restructuring；
5. **当前修改直接产生的必要清理**：unused import、orphan branch、stale renamed reference、失去最后消费者的局部 helper 等；
6. **确定性机械伴随变更**：当前变化和 Repository Rule 确定触发的 formatter、generator、lockfile、schema compiler 等结果。

### 5.3 默认不进入当前 diff

以下理由默认不足以加入当前 change：

- “就在旁边，顺手修了”；
- 无关 TODO / typo；
- 当前变化之前就存在的 dead code；
- 邻近独立 Bug；
- 个人命名或风格偏好；
- 与当前行为无关的大规模 rename / cleanup；
- “既然改这个文件，就全部格式化”；
- 独立优化机会。

如果相邻问题实际阻塞当前 Unit，应按现有 Stage Return / Reslicing 处理，而不是静默吸收。

### 5.4 必要重构边界

准备性重构可以属于当前逻辑变化，但至少要求：

- 当前实现 / 验证直接需要；
- 不引入新的产品行为；
- 有行为保持证据；
- 不扩大到独立重大设计；
- 当前 Reviewer 仍能区分结构变化与行为变化。

如果重构已经形成独立目标、独立设计判断或显著降低当前 change 的可复核性，应拆成前置 Execution Unit / change。

### 5.5 多文件与机械差异

- 多文件本身不是越界证据；
- 当前已授权公共契约变化要求同步 DTO、migration、tests、generated reference 时，这些可以共同属于同一逻辑变化；
- “同一逻辑变化”不能反过来绕过公共契约、重大架构或其他高影响事项的上游授权；
- formatter / generator 产生大面积机械变化时，应确认最小合法范围，并在必要时分离机械 change 或提供清晰 Review 边界；
- 不为了保持小 diff 跳过 Repository Rule 强制的机械产物和验证。

### 5.6 Final Diff Scope Check

在 `execute-unit` 声明 Completed 前，应能完成以下轻量检查：

1. 识别主要 changed regions；
2. 为每个区域找到当前责任类别；
3. 检查是否隐藏第二个独立逻辑变化；
4. 检查 preparatory refactoring 是否仍受当前 Unit 约束；
5. 检查 generated / formatting noise 是否掩盖语义变化；
6. 移除、记录或拆分无法形成当前责任链的顺带修改。

不要求为每个 Unit 生成新的持久化 Diff Scope Artifact。

## 6. 数据访问作用域与有界性控制

### 6.1 核心规则

> 设计或修改集合型数据访问时，应先确认当前消费者真正需要的数据作用域，以及集合是稳定有界、可能持续增长还是当前无法可靠界定；再根据 freshness、consistency 和应用生命周期选择过滤、排序、window / pagination、字段表示与复用方式。页面最终展示数量、现有 `LIMIT/OFFSET` 或客户端过滤不能替代业务作用域。若业务 scope 决定集合成员资格，应在 window / pagination 之前形成该 scope；只有当前权威明确把全局 window / ranking 本身定义为业务语义时才例外。规模稳定有界且语义上属于共享快照的数据可以完整读取并按当前生命周期复用，不应为了形式一致机械分页。

该规则首先保护正确性，其次才是性能优化。

### 6.2 判断模型

按当前 Unit 风险和数据路径复杂度，按需检查：

1. **Consumer Scope**：当前页面、API、Job 或模块真正消费哪个业务集合？是否存在 parent、tenant、栏目、状态、组织或其他明确 membership boundary？
2. **Boundedness**：集合是否有当前证据支持的真实稳定上界，还是会随业务持续增长 / 无法可靠界定？
3. **Lifecycle / Freshness**：数据是 request-local、page-local、application snapshot，还是要求持续刷新 / invalidation？同一生命周期是否重复获取同一稳定快照？
4. **Filter / Ordering Boundary**：哪些条件定义集合成员资格或业务顺序？window / pagination 前是否已经形成正确候选集合？
5. **Window Strategy**：是否需要 page、cursor、chunk、Top-N？是否存在稳定 ordering / continuation 语义？
6. **Representation**：list 是否只需要 summary/basic fields？detail 是否需要 full representation？额外 projection 的复杂度是否由当前成本或契约支持？
7. **Verification Boundary**：当前验证是否真正越过 page / Top-N / scope 边界，并包含足以暴露截断 / 顺序问题的 competing records？

不是每个 Unit 都需要显式回答七项；只有当数据访问策略会影响当前正确性、规模、生命周期或验收义务时才加载这一判断。

### 6.3 Scope 与 Window 的边界

当业务规则定义了明确集合，例如：

- 某栏目文章；
- 某租户资源；
- 某组织成员；
- 某状态下订单；
- 某项目下任务；

则该 scope 应进入数据访问契约或查询边界，不能默认先读取一个全局固定窗口再由客户端补救式过滤。

尤其禁止把：

```text
全局 Top-N
→ client filter
→ 页面显示某 scope 的少量条目
```

机械解释为“页面只显示 N 条，所以查询 N 条已经足够”。

但如果 Specification / Domain Authority 明确定义：

> 先选全局排名前 N，再在该已限定集合上进行派生展示

则 global window 本身属于业务语义，不应被本纪律擅自改写为 scope-first。

### 6.4 Bounded / Unbounded 判断

**稳定有界集合**可以包括当前 Authority 能解释其长期上界或小规模性质的数据，例如有限导航树、稳定站点配置、枚举式结构数据。

在当前证据支持下，可以：

- 完整获取；
- 在 application / request 的适当生命周期内作为 snapshot 复用；
- 不为了统一接口外形机械分页。

但“当前测试数据只有十几条”不是有界性的充分证据。

**持续增长或无法可靠界定的集合**默认不能依赖永远完整加载。应结合当前产品与技术责任考虑：

- server-side filtering；
- page / cursor / chunk；
- stable ordering；
- summary representation；
- freshness / consistency；
- 可接受的响应与资源成本。

本纪律不固定具体 pagination 技术、page size、cursor 格式或数据库方案。

### 6.5 Lifecycle / Freshness

完整 snapshot 是否合理，不能只由集合大小决定。

还应检查：

- 同一 application lifecycle 是否重复装配同一稳定数据；
- 当前 Product / Architecture 是否要求实时、定时或事件驱动刷新；
- cache / memoization / shared state 是否已经由当前框架或项目架构提供；
- snapshot 复用是否会违反 freshness、tenant、security 或 consistency boundary。

不因为“避免重复请求”就机械创建全局 cache、registry 或新状态层；新增机制继续受 Implementation Minimality 约束。

### 6.6 Representation

List / collection consumer 与 detail consumer 可以需要不同表示。

当完整 resource 很大、昂贵或包含列表不需要的信息时，可以在当前证据支持下采用 summary/basic representation；但不因为存在 list/detail 两种入口就机械创建第二套 DTO、projection 或 mapping layer。

representation 选择同时受：

- 当前消费字段；
- 响应 / 计算成本；
- 公共契约；
- 兼容性；
- Implementation Minimality；

约束。

### 6.7 Verification

验证必须针对本 Discipline 声称解决的边界，而不是只在小数据主路径上检查“页面有内容”。

按风险需要覆盖：

- 数据数量超过单页 / Top-N / 当前 window；
- competing records 来自其他 scope，足以暴露“global window 后过滤”截断；
- page / cursor / chunk 的 stable ordering 与 continuation；
- bounded snapshot 在当前 lifecycle 中的装配 / refresh 行为；
- list summary 与 detail full representation 的契约；
- 当前 Consumer Authority 明确的 freshness / consistency 责任。

如果验收义务要求分页或 scope correctness，少量 fixture、代码存在 `LIMIT/OFFSET` 或客户端过滤实现都不能单独成为 Completion Evidence。

### 6.8 非规则

本 Discipline 不等于：

- 所有接口必须分页；
- 所有列表必须 server-side pagination；
- 所有 filter 必须无条件先于所有 limit；
- 所有小型结构数据都禁止全量读取；
- 所有 list 都必须建立 Summary DTO；
- 必须引入 cache / repository abstraction / cursor framework；
- 固定任何 page size；
- 仅凭性能猜测扩大当前 Product Scope。

## 7. 三个纪律的组合

三个纪律可以组合使用，但不得合并成一个模糊的“工程最佳实践”口号：

```text
实现最小化
这个设计元素为什么需要存在？
        ↓
复杂度正当性

精准修改
最终这些改动为什么属于当前变化？
        ↓
差异范围正当性

数据访问作用域与有界性
当前消费者真正属于哪个数据集合？
该集合的增长 / 生命周期性质要求怎样的访问边界？
        ↓
数据边界正当性
```

典型结果：

- 为持续增长集合增加分页可能由 Data Access Discipline 证明需要，同时仍需 Minimality 防止引入不必要的通用 pagination framework；
- 修正 global Top-N 截断可能跨 API、service、client 和 test，多文件由 Surgical Change 判断是否仍属于同一逻辑变化；
- 小型稳定 snapshot 可以被 Data Access Discipline 允许完整读取，同时 Minimality 可以阻止为了“规范统一”新增无必要分页层。

## 8. `execute-unit` 消费边界

`execute-unit` 是当前主要执行消费者，但只应保留足够实施本纪律的薄规则：

- 实施前 / JIT 判断新增复杂度是否有当前正当性；
- 完成前检查最终 diff 是否只有当前逻辑变化及必要责任；
- 当 Unit 涉及集合 / 列表 / snapshot 数据访问时，按风险判断 consumer scope、boundedness / growth、lifecycle / freshness、filter / ordering、window / pagination、representation 与验证边界；
- 继续服从现有 Unit Boundary、Stage Return、Human Escalation、配置责任、已有能力复用和 Evidence Before Claim；
- 不因三个纪律新增独立 Skill invocation、持久化检查表或人工确认步骤。

完整规范以本文为准；`SKILL.md` 的执行摘要不得覆盖或放宽本文。

## 9. 非目标

本文不定义：

- 完整 Code Review Discipline；
- 完整 Testing Discipline；
- 完整 Refactoring Discipline；
- 完整 Data Architecture Method；
- 固定复杂度分数、行数、文件数或 diff 大小阈值；
- 所有项目统一的 formatter / generator / test command；
- 所有技术栈统一的分页 API / cursor / page size / cache strategy；
- 新的 `minimality`、`surgical-change`、`diff-scope`、`data-access` 或 `pagination` Skill；
- Consumer 项目的具体目录、代码风格、数据模型或架构事实。

## 10. 生命周期

- **Producer：** 当前 `agentic-dev` Repository Authority 授权的 Engineering Capability / Architecture 维护职责；
- **Trigger：** 首批两个 Discipline 由 WI-02 / WI-03 Research 触发；第三项由 Foundation v1 Closure 后 Issue #33 已核验 Data Access Candidate 与 Engineering Discipline Expansion v1 触发；
- **Consumer：** `execute-unit`、未来 Engineering Quality Review / Refactoring Discipline / Technology Profile，以及采用当前 baseline 的 Consumer Agent；
- **Persistence：** 实际集成后，本文作为当前工程纪律规范入口；Research 继续只保存证据，不与本文竞争权威；
- **Update：** 新 Targeted Eval、Consumer Feedback、上游 Method / Architecture / Contract 变化或高质量外部证据暴露边界问题时重新检查；
- **Supersede：** 后续版本必须明确取代当前内容，并保持单一当前规范入口；
- **Escalation：** 如果修订要求改变 Method 生命周期、Execution Unit 定义、重大架构、Skill Contract、Human / Integration Boundary 或 Consumer Authority，返回对应更高权威处理。

## 11. WI-03V Targeted Eval 证据

2026-09-02，在 PR #48 的待测语义 Head：

`a7d50795a968f279a68d9dfd62df57b7c1480de5`

上完成 Fresh Runtime Targeted Eval 与回归。提交的运行产物包含 13 个场景各自的 `.jsonl`、`.run.json` 和 `.stderr.txt`：

```text
场景：  13 / 13 PASS
断言：  62 / 62 PASS
```

新增 Engineering Discipline 场景：

- `B-EU-09`～`B-EU-12`：Implementation Minimality；
- `B-EU-13`～`B-EU-17`：Surgical Change / Diff Scope。

历史回归：

- `B-EU-01`：真实 one-unit fixture 修改、预期失败证据与当前 unittest 闭环；
- `B-EU-02`：one-unit boundary；
- `B-EU-07`：配置责任；
- `B-EU-08`：已有框架能力复用与项目差异薄适配。

关键观察：

- `B-EU-01` 实际先取得空字符串 / 纯空白输入的失败证据，再完成最小实现并执行仓库声明的 `python3 -m unittest discover -s tests -v`，3 项测试全部通过后才声明 `Completed`；
- 9 个新场景均能区分“当前复杂度 / 范围正当性”与机械少代码、少文件、DRY、YAGNI 或顺手 cleanup；
- 必要 preparatory refactoring、当前测试、安全责任、已授权公共契约同步、直接产生的 orphan cleanup 和 Repository Rule 确定触发的机械差异没有被错误排除；
- 无关 TODO / typo / 历史 dead code、假想扩展结构和无证据动态配置没有被自动吸收；
- `B-EU-02`、`B-EU-07`、`B-EU-08` 没有发生语义回归；
- 所有 Run 均使用独立隔离 workspace，没有发现读取 `evals/behavior/*`、`evals/results/*`、grading assertions、历史答案或当前工作区之外路径的污染轨迹；
- 13 个进程均以状态码 `0` 结束并包含 `turn.completed`，但退出码没有被作为 PASS 依据；
- `B-EU-02` 的 stderr 出现一次模型列表刷新 timeout，未中断场景执行，也未影响最终语义判断；其余 stderr 为空；
- 提交产物没有暴露精确 Runtime 版本或模型名，本轮结论不依赖该信息。

运行结果压缩包 SHA-256：

`17133821e31077f6196296298e371f897f4dc180f72b0471d0afe0e32806388e`

该历史 Targeted Eval Gate 已通过。

## 12. Engineering Discipline Expansion v1 Targeted Eval

2026-09-04，在 PR #56 冻结待测 Head：

`31e8d7597cbe9ea37746b34a6c50907e6dea37b0`

完成第三项 Discipline 的 Fresh Runtime Targeted Eval 与必要历史回归：

```text
新场景： 8 / 8 PASS，41 / 41 assertions PASS
历史回归：4 / 4 PASS，19 / 19 assertions PASS
合计：   12 / 12 PASS，60 / 60 assertions PASS
```

新增场景：

- `B-EU-18`：global Top-N 后 client filter 的 scope truncation；
- `B-EU-19`：bounded stable snapshot，拒绝机械 pagination，并在没有 freshness Authority 时不发明实时刷新；
- `B-EU-20`：unbounded operational collection 的 server filtering / pagination / summary；
- `B-EU-21`：presentation N 与 retrieval scope 分离；
- `B-EU-22`：Authority 明确 global ranking 时允许 window-first 业务语义；
- `B-EU-23`：验证数据必须越过 page / Top-N / competing-scope boundary；
- `B-EU-24`：pagination ordering / continuation stability；
- `B-EU-25`：bounded snapshot 仍需遵守明确 freshness / invalidation responsibility。

历史回归：

- `B-EU-01`；
- `B-EU-06`；
- `B-EU-09`；
- `B-EU-13`。

关键观察：

- `B-EU-18` 与 `B-EU-21` 均正确识别页面展示 N 与真实 retrieval scope 不等价，没有用扩大固定 Top-N 魔法数字掩盖错误集合边界；
- `B-EU-19` 正确使用明确 Domain Authority 上界判断 boundedness，保留完整 snapshot，并复用既有 app store；没有因为缺少 freshness Authority 而发明 TTL、轮询或实时刷新；
- `B-EU-20` 正确把持续增长 operational collection 的筛选与分页责任放到服务端，并保持 summary/full representation 的当前证据边界，没有创建通用分页框架；
- `B-EU-22` 正确保留 Specification 明确的 global Top-100 → sponsored 派生语义，证明本 Discipline 没有退化为“所有 filter 必须先于 limit”的教条；
- `B-EU-23` 没有把小数据 fixture 或实现形状当作 scope + pagination Completion Evidence；
- `B-EU-24` 要求稳定 `createdAt` ordering 与必要 tie-break，并检查跨页无重复 / 无遗漏；cursor / snapshot 只作为一致性语义明确要求时的条件路径，没有因 OFFSET 潜在性能成本机械引入 cursor framework；
- `B-EU-25` 正确区分 boundedness 与 freshness：保留完整 12 条 snapshot，同时依据明确 30 秒 Product Authority 复用现有 refresh 机制；
- `B-EU-01` 实际建立预期失败证据，完成最小实现并运行当前 unittest；2 个测试方法覆盖空字符串、纯空白与非空名称并 PASS；
- `B-EU-06`、`B-EU-09`、`B-EU-13` 的验收证据、推测性复杂度控制与 diff scope 行为没有回归；
- 12 个 Run 均使用独立隔离 workspace，只访问场景提供的 Skill / fixture，没有发现读取 `evals/behavior/*`、`evals/results/*`、grading assertions、历史答案或工作区外路径的污染轨迹；
- 12 个进程均以状态码 `0` 完成并包含 `turn.completed`，但退出码没有被作为 PASS 依据；
- 12 个 stderr 全空。

运行结果 ZIP SHA-256：

`d32233916e2ce923f2f052fe6750eda4bf0674992906bd18223b43f83f21a855`

冻结 Head 的关键受测 / 契约 Blob：

- `skills/execute-unit/SKILL.md`：`c71ddd23d20b3a14c9cb19a38f6e8d6cbedcf46e`；
- `docs/architecture/skill-contracts.md`：`b68e9c9cd6f47d9433f22bd5aab78ae3c8a21a42`；
- `evals/behavior/execute-unit.json`：`39676d46a1502d6da3050e7cbba484ad58733fa4`；
- 本文 Draft 规范语义 Blob：`cc7e44ba42f4f2cee90f8535eac2111d30856fc2`。

Fresh Runtime Gate：**PASS**。

当前只允许继续回写 Evidence / Project Status / Review metadata。若第三项 Discipline 的规范语义、`execute-unit` 薄消费语义、Skill Contract 或 Eval corpus 发生实质变化，必须重新运行受影响场景与必要回归；纯证据和状态回写不使上述 Runtime Evidence 失效。

# 工程纪律基线

**状态：** Draft v0.1 — WI-03V Targeted Eval Pending  
**性质：** 工程纪律（Engineering Discipline）规范性 Draft

## 1. 目的

本文定义 `agentic-dev` 首批两个跨技术栈工程纪律的规范性 Draft：

1. **Implementation Minimality & Speculative Complexity Control（实现最小化与推测性复杂度控制）**；
2. **Surgical Change & Diff Scope Control（精准修改与差异范围控制）**。

本文不增加新的 Method Stage，不改变 Execution Unit、Human Escalation、Ready to Integrate 或 Integration Boundary，也不创建新的 Task-oriented Skill。

在 WI-03V 完成 Fresh Runtime Targeted Eval、必要回归和最终 AI Review 之前，本文仅为拟集成 Draft；只有实际合并到当前 Repository Authority 后，才成为 `agentic-dev` 的正式工程纪律基线。

## 2. Architecture Fit Review

WI-02 / WI-03 的 Research 与 Candidate Design 在当前 `master` 上重新复核后，Architecture Fit 结论为：

- 两个 Candidate 都描述**阶段内部如何高质量实施**，而不是新的开发生命周期，因此属于 Engineering Discipline；
- 两者跨 Vue、Spring、数据库等具体技术栈成立，不属于 Technology Profile；
- 两者没有独立任务入口、Stage Return、稳定独立输出或单独调度价值，不满足 Task-oriented Skill 的独立职责条件；
- 两者可以被 `execute-unit`、未来 Engineering Quality Review、Refactoring Discipline 和 Technology Profile 共同消费，因此不应只写死在单个 Skill 内；
- `execute-unit` 仍是当前主要执行消费者，只需要保留薄执行规则，不复制完整纪律正文；
- 两个纪律职责独立且可组合：前者判断**复杂度为什么需要存在**，后者判断**最终变更为什么属于当前逻辑变化**。

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

## 6. 两个纪律的组合

两个纪律必须组合使用，但不能合并为一个模糊的“保持简单”口号：

```text
实现最小化
这个设计元素为什么需要存在？
        ↓
复杂度正当性

精准修改
最终这些改动为什么属于当前变化？
        ↓
差异范围正当性
```

典型结果：

- 假想插件接口可能同时违反两个纪律；
- 当前必要的 preparatory refactoring 可能增加 diff，但可以同时满足两个纪律；
- 无关 typo 几乎没有复杂度成本，却仍违反差异范围纪律。

## 7. `execute-unit` 消费边界

`execute-unit` 是当前主要执行消费者，但只应保留足够实施本纪律的薄规则：

- 实施前 / JIT 判断新增复杂度是否有当前正当性；
- 完成前检查最终 diff 是否只有当前逻辑变化及必要责任；
- 继续服从现有 Unit Boundary、Stage Return、Human Escalation、配置责任、已有能力复用和 Evidence Before Claim；
- 不因两个纪律新增独立 Skill invocation、持久化检查表或人工确认步骤。

完整规范以本文为准；`SKILL.md` 的执行摘要不得覆盖或放宽本文。

## 8. 非目标

本文不定义：

- 完整 Code Review Discipline；
- 完整 Testing Discipline；
- 完整 Refactoring Discipline；
- 固定复杂度分数、行数、文件数或 diff 大小阈值；
- 所有项目统一的 formatter / generator / test command；
- 新的 `minimality`、`surgical-change` 或 `diff-scope` Skill；
- Consumer 项目的具体目录、代码风格或架构事实。

## 9. 生命周期

- **Producer：** 当前 `agentic-dev` Repository Authority 授权的 Engineering Capability / Architecture 维护职责；
- **Trigger：** WI-02 / WI-03 Research Candidate 经 WI-03V Architecture Fit Review 确认适合 Engineering Discipline；
- **Consumer：** `execute-unit`、未来 Engineering Quality Review / Refactoring Discipline / Technology Profile，以及采用当前 baseline 的 Consumer Agent；
- **Persistence：** 实际集成后，本文作为当前工程纪律规范入口；Research 继续只保存证据，不与本文竞争权威；
- **Update：** 新 Targeted Eval、Consumer Adoption、上游 Method / Architecture / Contract 变化或高质量外部证据暴露边界问题时重新检查；
- **Supersede：** 后续版本必须明确取代当前内容，并保持单一当前规范入口；
- **Escalation：** 如果修订要求改变 Method 生命周期、Execution Unit 定义、重大架构、Skill Contract、Human / Integration Boundary 或 Consumer Authority，返回对应更高权威处理。

## 10. WI-03V 验证门禁

本 Draft 只有在以下条件同时成立时才可以改为正式 Baseline 并进入最终 AI Review：

- 4 个 Implementation Minimality 新场景通过；
- 5 个 Diff Scope 新场景通过；
- 至少回归 `B-EU-02`、`B-EU-07`、`B-EU-08`；
- 必要重构组合边界通过；
- 不产生新的 Human Confirmation Loop；
- 不削弱配置责任、已有能力复用、Stage Return、Human Escalation 或 Integration Boundary；
- 失败场景完成 Fresh Runtime 修订与重跑，而不是使用当前聊天推演替代。

在上述门禁完成前，状态保持 `Draft v0.1 — WI-03V Targeted Eval Pending`。
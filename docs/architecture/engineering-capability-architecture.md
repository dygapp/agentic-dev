# 工程能力架构

**状态：** Baseline v0.1  
**性质：** 规范性架构文档

## 1. 目标

本文定义 `agentic-dev` 在核心开发方法已经形成并完成首轮真实 Consumer 验证后，如何继续扩展工程能力。

核心目标不是继续增加方法阶段，而是建立一套能够承载工程纪律、技术栈实践、验证策略、任务型 Skill 与运行时适配的分层能力架构，使 `agentic-dev` 可以主动吸收成熟外部经验，再通过专项评估和 Consumer 集成持续修正。

本文不改变 `docs/method/ai-development-method.md` 已定义的开发生命周期，也不允许 Technology Profile、Skill 或 Runtime Adapter 反向覆盖 Method、Principles 或 Consumer Repository Authority。

## 2. 演进驱动原则

`agentic-dev` 的后续演进不再把 Consumer Evidence 作为唯一前置触发条件。

以下来源都可以成为能力建设输入：

1. **官方权威实践**：框架、语言、平台或工具的官方文档、官方指南、官方示例与稳定规范；
2. **成熟开源工程实践**：长期维护、高质量项目中已经稳定使用的工程规则、测试方式与架构模式；
3. **专家方法与研究**：具有明确工程价值、可以被独立分析和验证的方法、纪律或经验总结；
4. **专项评估证据**：`agentic-dev` 为某项候选能力建立的针对性行为评估、实现评估或验证评估；
5. **Consumer 实践证据**：真实 Consumer 在采用、升级和持续开发过程中产生的成功经验、缺口、回归或冲突。

成熟外部证据可以主动推动候选能力形成，不要求先等待多个 Consumer 重复暴露同一问题。

但“外部已有成熟做法”也不等于“自动成为 `agentic-dev` 权威”。任何长期能力仍必须经过：

```text
Research / Evidence
        ↓
Architecture Fit
        ↓
Candidate Capability
        ↓
Targeted Evaluation
        ↓
AI Review
        ↓
Repository Authority Integration
        ↓
Consumer Adoption / Feedback
```

Consumer Evidence 在新的演进模型中主要承担现实验证、纠偏、优先级调整和长期适用性确认，不再承担所有能力建设的唯一启动职责。

### 2.1 证据质量门槛

允许主动使用外部成熟经验，不等于降低证据要求。候选能力在离开 Research、进入规范性设计前，至少应能够说明：

- **来源（Provenance）**：可以追溯到官方文档、明确的仓库 / 文件 / 版本、专家原始材料、专项评估结果或具体 Consumer Evidence；
- **基线（Baseline）**：记录研究时实际使用的版本、Commit、发布日期或其他能够识别当时状态的锚点；
- **证据类型**：区分官方规范 / 官方推荐、成熟工程实践、专家观点、专项评估结论和 Consumer 观察，不把不同强度的来源混成同一等级；
- **适用范围**：明确该结论适用于哪些框架版本、运行条件、任务类型或工程假设，避免把局部实践直接泛化为通用规则；
- **时效性（Freshness）**：对快速演进的框架、Runtime、API 或工具检查当前有效性，不能仅凭已经过时的最佳实践建立新的长期能力；
- **冲突与替代方案**：当官方实践、成熟项目或专家观点存在实质冲突时，应保留冲突事实并说明选择依据，不得静默挑选最符合预期的单一来源；
- **可验证性**：能够把候选规则转换为有辨识力的 Targeted Eval、Review Heuristic 或其他可观察检查，而不是只形成无法验证的口号。

对于框架语义、API 使用方式、生命周期和官方支持边界，当前有效的官方资料通常具有最高外部参考优先级；成熟开源项目和专家经验用于补充工程化实践，而不应无依据覆盖官方语义。

单一低权威观点、二手总结、缺少版本信息的旧文章或无法复现的个案，可以继续作为 Research 线索，但通常不足以单独把候选结论提升为规范性 Technology Profile、Verification Profile 或 Skill。

外部证据之间存在重大冲突，且现有 Repository Authority、专项评估和 Consumer Evidence 都不足以裁决时，应保持候选状态或升级，而不是为了推进路线强行固化。

## 3. 能力分层

`agentic-dev` 的工程能力分为以下层次：

```text
Core Method
    │
    ├── Engineering Disciplines
    │
    ├── Technology Profiles
    │       └── Verification Profiles
    │
    ├── Task-oriented Skills
    │
    └── Runtime Adapters

Consumer Repository Authority
    └── 选择、限制、补充或覆盖具体项目规则
```

这些层次解决不同问题，不应因为内容都“可复用”就合并成一个大型 Skill。

## 4. Core Method

核心方法（Core Method）定义跨技术栈成立的软件开发生命周期、阶段职责、权威边界和完成语义。

当前主要由以下文档定义：

- `docs/method/ai-development-method.md`
- `docs/method/principles.md`

典型内容包括：

- 意图澄清；
- 规格说明；
- 条件性技术规划；
- 执行单元切分；
- 就绪检查；
- Fresh Context 执行；
- 验证证据；
- 整体收敛；
- 人工升级与集成边界。

Core Method 应保持技术栈无关。Vue、Spring、Gradle、数据库或具体测试框架的使用规则不得直接变成新的通用方法阶段。

新的外部经验只有在确实揭示生命周期、权威、阶段职责或完成语义的通用缺口时，才评估是否修改 Method。

## 5. Engineering Disciplines

工程纪律（Engineering Discipline）描述阶段内部如何高质量工作，通常跨多个技术栈成立。

典型候选包括：

- 最小实现与避免推测性复杂度；
- 精准修改与差异范围控制；
- Code Review；
- Testing；
- Refactoring；
- Debugging；
- Performance；
- Security；
- Dependency Management；
- API Evolution；
- Error Handling；
- Configuration；
- Existing Capability Reuse。

工程纪律默认优先作为 Method / Skill 内嵌规则或独立规范存在，不因为它重要就自动创建 Skill。

只有当某项工程纪律形成稳定、独立、可组合的执行过程，具有明确输入、步骤、输出和退出条件时，才进一步评估是否升级为正式 Skill。

## 6. Technology Profiles

技术配置档（Technology Profile）描述 Agent 在特定技术体系下进行工程开发时应采用的默认知识、边界、惯例和验证关注点。

Technology Profile 的职责是：

- 提炼官方权威实践和成熟工程经验；
- 说明当前技术的职责模型、主要扩展点和常见误用；
- 指导 Agent 优先复用框架、标准库和现有生态能力；
- 说明何时应该使用框架能力，何时应该保留项目自有实现；
- 为 Task-oriented Skill 和 Verification Profile 提供技术上下文；
- 为 Consumer 提供可选择、可局部覆盖的默认工程基线。

Technology Profile 不是：

- 框架官方文档的完整复制；
- 某个 Consumer 的项目事实；
- 自动执行完整开发任务的 Skill；
- 新的方法阶段；
- 强制所有使用同一技术的项目采用完全相同的目录、代码风格或架构。

首批规划研究对象可以包括：

- Vue 3；
- TypeScript；
- Element Plus；
- Spring Framework；
- Spring Boot；
- Spring MVC；
- Gradle。

后续是否扩展到 MyBatis、Flyway、Redis、Playwright、Vitest、JUnit 等技术，由路线优先级和研究价值决定，不要求一次建立完整技术百科。

## 7. Verification Profiles

验证配置档（Verification Profile）定义某类技术变更通常需要哪些验证层级、证据类型和风险判断。

其目标不是固定一套命令，而是帮助 Agent 将：

```text
规格验收义务
→ 当前技术变更类型
→ 验证责任
→ 计划验证证据
→ 已执行的当前证据
```

可靠映射起来。

例如，一个前端组件变更可能需要静态类型检查、单元 / 组件测试、构建验证、浏览器行为验证和按需视觉复核；一个 Spring MVC 接口变更可能需要编译、服务层测试、MVC 测试、应用上下文验证和按需集成 / API 验证。

具体命令、测试框架和证据载体仍由 Consumer Repository Authority、项目依赖和当前代码状态决定。

Verification Profile 可以：

- 作为 Technology Profile 的一部分；
- 在跨多个 Technology Profile 重复且具有独立价值时单独维护；
- 被 `execute-unit`、专项 Skill 或平台验证 Skill 按需引用。

它本身不替代执行单元中的计划验证证据，也不允许以“跑过某个固定检查”代替规格验收义务闭环。

## 8. Task-oriented Skills

任务型 Skill（Task-oriented Skill）用于执行稳定、可复用且边界清晰的工程工作过程。

候选 Skill 必须具备：

- 清晰职责；
- 明确使用条件与不使用条件；
- 可识别输入；
- 稳定过程；
- 可观察输出；
- 退出条件；
- 升级条件；
- 与 Repository Authority 的明确关系。

Technology Profile 是“在某个技术体系下应如何正确工作”的知识与默认规则；Task-oriented Skill 是“完成某类稳定任务应执行什么过程”。二者不得混淆。

因此不建议仅因为技术重要就创建：

```text
vue-skill
spring-skill
element-plus-skill
```

更合理的 Skill 候选应围绕明确任务形成，例如：

```text
frontend-component-change
frontend-visual-convergence
spring-web-endpoint-change
database-schema-change
dependency-upgrade
framework-upgrade
```

上述名称只是能力形态示例，不表示这些 Skill 已进入当前 Skill Inventory。

### 8.1 Skill 形成证据

新的 Skill 不再要求必须先拥有多个 Consumer 的重复失败证据。

如果以下条件已经满足，也可以进入候选设计和专项评估：

- 官方或成熟外部实践支持该职责长期稳定存在，并满足本架构的证据质量门槛；
- 该职责可以从 Method / Architecture 中明确定位；
- 输入、过程、输出和退出条件可以独立定义；
- 与现有 Skill 不形成职责重叠或 Super-skill；
- 可以建立有辨识力的 Targeted Eval；
- AI Review 能确认没有改变更高层 Method / Authority 边界。

Consumer 实际采用仍是后续重要验证环节，但不是所有 Skill 设计的绝对前置条件。

## 9. Runtime Adapters

运行时适配层（Runtime Adapter）负责把同一套 Method、Profile 或 Skill 以适合特定 Agent Runtime 的方式交付、发现或加载。

可能涉及：

- Codex；
- Claude Code；
- Cursor；
- 其他支持 Skill、Rule、Plugin、Prompt Package 或类似机制的 Runtime。

Runtime Adapter 不拥有方法语义。推荐关系是：

```text
Method / Profile / Skill Authority
              ↓
      Runtime-specific Adapter
```

而不是为每个 Runtime 复制一套方法。

运行时适配可以进入正式规划，但具体 Marketplace、Plugin、自动安装器或 Controller 只有在对应阶段明确设计和验证后才实施。

## 10. Consumer Repository Authority

Consumer Repository 决定自身最终采用哪些能力以及如何本地化。

Consumer 可以：

- 选择适用的 Technology Profile；
- 固化项目自己的技术约束、目录规则和架构决定；
- 指定实际验证命令和 CI / Human Review 策略；
- 禁用或限制不适合当前项目的 Skill；
- 在不违反上游方法语义的前提下补充项目级规则；
- 通过 Existing Consumer Baseline Upgrade 选择性吸收新的 `agentic-dev` 能力。

Technology Profile、Verification Profile 和 Skill 都不得覆盖 Consumer 已明确建立的更具体项目事实或仓库策略。

当 Consumer 规则与 `agentic-dev` 通用能力冲突时，必须先区分：

- Consumer 合理的项目特化；
- Consumer 已陈旧的旧基线；
- `agentic-dev` 自身存在的通用设计缺口。

不能因为 Profile 是“最佳实践”就无条件改写 Consumer 项目。

## 11. 能力生命周期

长期工程能力采用以下生命周期：

```text
Research / Evidence
        ↓
Candidate
        ↓
Architecture Fit Review
        ↓
Draft Capability
        ↓
Targeted Eval
        ↓
AI Review
        ↓
Integrate
        ↓
Consumer Adoption
        ↓
Feedback / Revision / Supersede
```

### 11.1 Producer

- Research 可以由当前仓库授权的 Agent、维护者或研究工作形成；研究结果只产生证据和候选结论，不自动写入更高权威；
- Architecture 由当前 `agentic-dev` Repository Authority 授权的架构职责确定能力层次和职责边界；
- Profile、Skill 或 Adapter 的正式建立与重大修改必须由当前仓库授权的对应维护职责执行，并遵循其上游 Architecture / Contract；
- Consumer 可以提交实践证据和采用反馈，但不能通过 Consumer-local 文档直接改写 `agentic-dev` 上游权威；
- Consumer 负责自身项目采用、本地化事实和项目规则。

### 11.2 Trigger

能力可以由以下任一信号触发：

- 成熟官方或开源实践显示存在稳定工程能力；
- 研究发现当前体系存在明显可复用缺口；
- Targeted Eval 暴露当前 Agent 行为不足；
- Consumer Evidence 暴露真实缺口或回归；
- Runtime 生态变化产生新的稳定交付需求。

### 11.3 Consumer

能力的消费者可能是：

- Workflow Skill；
- `execute-unit`；
- `systematic-debug`；
- 平台专项 Skill；
- Consumer Agent；
- Runtime Adapter。

### 11.4 Persistence

长期能力必须进入与其层次匹配的 Repository Authority，不能只停留在聊天、Issue 评论或研究报告。

Research 只保存证据；Architecture 决定职责；Profile / Skill / Adapter 保存可执行的稳定能力。

### 11.5 Update 与 Supersede

以下变化会触发对应能力的重新检查：

- 官方框架、语言、Runtime 或 API 版本变化；
- 原始外部依据被撤回、取代或证明已经过时；
- Targeted Eval 暴露新的失败模式；
- Consumer Adoption 证明默认规则不适用或出现回归；
- 上游 Method、Architecture、Contract 或 Repository Authority 发生相关变化。

更新责任仍属于当前 `agentic-dev` Repository Authority 授权的对应能力维护职责。Consumer 或外部来源只能提供 Trigger / Evidence，不能直接完成上游权威更新。

重大更新应重新检查证据基线、适用范围和 Targeted Eval；如果属于 `AGENTS.md`、Method、Architecture、Contract、核心 Skill 或其他高影响规则变更，还必须重新执行适用的 AI Review。

旧 Profile、Skill 或 Adapter 被新版本取代时，必须更新当前可发现入口并显式处理 Superseded / Replaced 关系，避免旧版与新版同时被解释为当前规范性能力。历史内容可以保留用于追溯，但只能有一个明确的当前有效入口。

### 11.6 Escalation

以下情况必须升级：

- 候选能力会改变 Core Method 生命周期或完成语义；
- 会改变重大架构方向；
- 会扩大 Skill 到完整生命周期；
- 会覆盖 Consumer Repository Authority；
- 会引入高风险、安全、隐私或难逆默认行为；
- 外部成熟实践之间存在无法在现有 Authority 内裁决的重大冲突。

## 12. 评估策略

工程能力扩展应建立比“等待真实项目碰巧出现问题”更主动的专项评估。

评估应围绕能力实际声称解决的问题设计，而不是为了数量建设大型 Benchmark。

例如 Technology Profile / Task Skill 可以评估：

- 是否识别并复用框架已有能力；
- 是否避免无证据的推测性抽象；
- 是否遵守框架推荐的职责边界；
- 是否选择与变更类型匹配的验证路径；
- 是否避免无关顺带修改；
- 是否在框架约定与 Consumer Authority 冲突时正确升级或服从项目规则。

通过专项评估只能证明对应能力在测试场景中满足预期，不自动证明所有 Consumer 都应该采用。

## 13. 与 Skill Architecture 的关系

本文定义更高层的工程能力分层；`docs/architecture/skill-architecture.md` 继续专门定义 Skill 的分类、调用关系、Contract 形状和 Skill Inventory。

当一个候选能力需要 Skill 化时：

1. 先用本文确定它是否真的属于 Task-oriented Skill；
2. 再按 `skill-architecture.md` 和 `skill-contracts.md` 定义 Skill 职责与契约；
3. 最后进入实现与专项评估。

不得绕过能力分层，直接因为发现一个优秀外部 Skill 就复制进本仓库。

## 14. Non-goals

本架构当前不要求：

- 一次建立所有语言和框架的 Technology Profile；
- 为每个 Technology Profile 创建一个 Skill；
- 为每个框架复制官方文档；
- 固定所有 Consumer 的目录、代码风格和测试命令；
- 立即建立 Marketplace、Plugin Bundle 或统一 Controller；
- 让 `jilinjobs-cms` 成为所有能力设计的唯一实验来源；
- 因为进入工程能力扩展阶段就重新设计已经稳定的 Core Method。

标准化的是能力层次、证据进入方式、职责边界和验证闭环，而不是把所有工程知识集中成一个大而全的系统。

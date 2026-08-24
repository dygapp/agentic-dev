# AI 开发方法原则

**状态：** Baseline v0.1  
**性质：** 规范性文档

本文定义所有方法阶段和 Skills 必须遵守的顶层原则。

## P1. 阶段是状态，不是文档

开发阶段描述当前工作所处的状态以及正在解决的问题。

阶段存在，并不意味着必须创建一份独立 Markdown 文档。

只有当信息具有独立的协调价值、权威价值、可追溯价值或长期知识价值时，才应持久化。

## P2. 需求事实与实现选择分离

统一采用：

```text
Specification = WHAT / WHY
Technical Plan = HOW
```

Specification 负责：

- 必须实现的行为；
- Scope；
- Boundary；
- Acceptance Criteria；
- 必要的 Non-functional Constraints。

Technical Plan 负责：

- 技术路线；
- 架构映射；
- Contract；
- Data Design；
- Migration；
- Technical Seam；
- Test Strategy。

实现方案发生变化，不应自动改写需求。

## P3. 持久化知识，不持久化推理过程

Conversation、scratch reasoning、探索过程和临时 implementation plan 都不是长期项目事实。

需要长期保留的信息，应进入合适的权威载体，例如：

- Repository Instructions；
- Project Roadmap（满足跨里程碑 / 阶段 / Fresh Context 的长期协调与恢复条件时）；
- Domain Context / Glossary；
- Architecture Context；
- ADR；
- Specification；
- 必要的 Technical Plan；
- Code / Tests。

其中，Project Roadmap 只承载项目整体的已完成里程碑、当前阶段 / 核心目标、已决定的下一步和条件性方向，不替代 Feature Specification、Technical Plan 或临时任务计划；ADR 只用于保留需要跨功能（Feature）长期约束后续工作的架构决定及其关键理由，不用于记录普通局部实现选择或尚未收敛的探索过程。

没有长期价值的信息可以随 context 一起结束。

## P4. Context Capacity 是执行约束

Execution Unit 必须控制在一个 fresh agent 可以完成以下全过程的范围内：

1. 理解；
2. 检查当前仓库状态；
3. 实现；
4. 验证。

该属性称为 **context-fit**。

## P5. 优先纵向、可验证的工作单元

Execution Unit 应尽量形成窄而完整的端到端行为，并满足：

- vertical；
- independently verifiable；
- bounded；
- traceable；
- context-fit；
- low hidden dependency。

能够形成纵向切片时，不应默认拆成“数据库 → 后端 → 前端 → 测试”的横向阶段。

## P6. Fresh Context 是逻辑属性

Fresh Context 不绑定某一种产品功能。

可以通过：

- 新 Chat；
- Subagent；
- Fresh CLI Session；
- Isolated Worker；
- Ephemeral Agent；

等方式实现。

其核心判定标准是：

> 当前执行 Agent 不依赖此前未持久化的 reasoning history。

## P7. 使用 Progressive Disclosure

不要给每个执行 Agent 加载全部项目文档。

默认只加载：

- Repository Rules；
- Current Execution Unit；
- Relevant Specification Sections；
- Relevant Technical Plan Decisions；
- Relevant Architecture / ADR / Domain Context；
- Relevant Code / Tests。

## P8. Evidence Before Claims

任何状态声明都必须有当前证据。

例如：

- “build passes”必须有当前 build 结果；
- “tests pass”必须有当前 test 结果；
- “API works”必须有当前行为验证结果。

当前证据必须能追溯到所声明完成的必需行为 / 验收义务，并足以区分该义务是否真实满足。

以下关系不能自动成立：

```text
实现存在 ≠ 验证覆盖
计划证据 ≠ 已执行的当前证据
主路径通过 ≠ 执行单元负责的全部验收义务已闭环
```

历史测试、代码阅读或其他 Agent 的无证据声明不能证明当前状态。

## P9. Human Escalation 依据 Authority、Impact、Reversibility

不能因为“存在歧义”就默认升级给人。

当一个选择：

- 影响局部；
- 可以安全回滚；
- 不改变外部可观察业务行为；
- 不超出 Agent 授权；

Agent 应自主作出合理裁决。

以下情况需要升级：

- 改变产品意图或 Scope；
- 多种选择产生不同用户可观察行为；
- 数据操作不可逆或难以恢复；
- Security / Privacy Sensitive；
- 重大 Architecture Direction；
- 权威来源冲突；
- 超出授权的 Shared / Production / External Side Effect。

简化表达：

> **Human owns irreversible intent; AI owns reversible execution.**

## P10. Verification、Review、Convergence 必须分离

**Verification：** 当前事实是什么？

**Review：** 这个实现本身是否正确、合理、高质量？

**Convergence：** 整个 Feature 是否最终符合权威意图？

不能把三者统一模糊为“Review”。

## P11. Technical Planning 是条件阶段

只有当 Specification 无法直接、安全地映射到当前架构时，才创建长期 Technical Plan。

典型触发包括：

- Cross-module Work；
- New Data Model；
- External Integration；
- Migration；
- Public Contract Change；
- Deployment Topology Change；
- Significant Architecture Trade-off。

小型、常规、已有稳定实现模式的修改可以直接进入 Slice。

Technical Planning 需要同时判断其中形成的长期技术决策（Durable Technical Decision）是否已经超出当前功能的协调范围并形成长期架构权威（Architecture Authority）；只有满足 ADR 条件的决定才单独持久化为 ADR。

## P12. Durable Technical Design 与 JIT Execution Planning 分离

Technical Plan 是按需持久化的设计协调产物，主要服务当前功能或一组执行单元（Execution Units）的长期 HOW 协调。

JIT Execution Plan 是 Agent 在查看当前代码状态后生成的临时施工计划，可以包含：

- 当前相关 File Paths；
- Exact Test Commands；
- Concrete Edit Sequence。

默认不作为长期项目知识保存。

跨功能、需要长期约束后续工作的重大架构决定不应只埋在 Technical Plan 或 JIT Plan 中；应按 P15 评估并进入适当的架构 / ADR 权威。

## P13. Skills 必须小型、可组合

一个 Skill 只承担一个清晰、可复用的职责。

禁止创建自动接管以下完整生命周期的超级 Skill：

```text
clarify
→ specify
→ plan
→ execute all
→ converge
→ merge/release
```

Workflow Transition 必须保持可观察、可控制。

## P14. Integration 是授权边界

通用方法的终点是：

> **Ready to Integrate**

Commit Policy、Merge、Push、PR、Release、Deploy 和 Destructive Cleanup 由 Repository Policy 或 Human Authority 决定。

## P15. ADR 是条件性长期架构权威

架构决策记录（Architecture Decision Record，ADR）不是方法阶段，也不是 Technical Plan 的同义词。

一个技术决定只有在需要跨越当前功能持续约束后续工作，并且保留其选择理由、主要权衡（Trade-off）或替代关系具有长期价值时，才应形成或更新 ADR。

典型信号包括：

- 约束多个未来功能、模块或独立工作流；
- 改变系统级组件、数据、集成、部署或共享契约边界（Contract Boundary）；
- 替换成本高、难以安全回滚，或形成长期兼容 / 迁移义务；
- 多个合理方案具有实质不同的长期后果；
- 缺少该决定会导致后续 Agent 反复重新决策或产生冲突实现。

以下内容不应为了形式完整性创建 ADR：

- 只服务当前功能的普通技术计划决策（Technical Plan Decision）；
- 单个执行单元内低影响、可逆的局部实现选择（Local Implementation Choice）；
- 即时文件、命令或编辑细节（JIT File / Command / Edit Detail）；
- 尚未收敛的探索与推理过程。

ADR 的创建、更新与取代仍受仓库权威（Repository Authority）和人工升级（Human Escalation）规则约束。重大架构方向（Major Architecture Direction）或高影响、难逆的权衡必须按权限（Authority）、影响（Impact）、可逆性（Reversibility）升级；新 ADR 取代旧 ADR 时，应显式保留被取代 / 替换（Superseded / Replaced）关系。

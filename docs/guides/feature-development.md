---
id: guide:feature-development
type: guide
status: active
---

# Feature Development 使用指南

本文帮助人和 AI 理解：当 Consumer 已经拥有足够稳定的 Requirement 与当前 Feature 所需的最小 Architecture Context 后，怎样组合 installed Skills 完成一个普通 Feature / change。

本文只负责导航，不维护第二套执行 procedure。每个责任的精确 Trigger、Procedure、Completion 和 Escalation 以对应 installed Skill 为准。

## 1. 什么时候进入 Feature Development

至少应满足：

- 当前 Repository Authority 可以恢复；
- 当前 Feature 依赖的 Requirement / Domain facts 有明确 owner；
- Goal、Scope、主要业务边界与 Acceptance 不需要重新做全项目需求分析；
- 当前 Feature 必需的 Architecture Context 已足够，或剩余只是局部可逆技术选择。

如果多个 Feature 同时被同一 Requirement gap 阻塞，先使用 `establish-requirement-baseline`。

如果多个 Feature 共同依赖长期、高成本难逆的 systemic architecture driver，先使用 `clarify-architecture`。

## 2. 先判断执行粒度

目标和验收已能从当前 Consumer Authority 恢复、修改局部且低风险可逆、不需要独立恢复或验收生命周期时，Agent 可以直接完成有界变更，并按当前 claim 做范围相称的验证。典型情况是既有实现中的小范围整理或明确的局部修复；是否满足条件由当前 Repository 事实判断，不能只凭文件数量或代码行数决定。相关修改可以在持续工作区中一起检查、修正和验证，不因此建立新的长期工作产物。

若目标、Acceptance 或适用 Authority 不清楚，先返回真实语义 owner。若工作需要独立恢复、依赖协调或独立验收，则形成 Execution Unit，并使用 `slice-work`、`readiness-check`、`execute-unit`。在直接变更中发现范围、风险或语义责任扩大时重新判断粒度；不把最初的轻量判断当作永久豁免。两种路径都须遵守 Consumer-local constraints，并用当前证据支持完成声明。

当同一 change 跨多个独立 Git Repository，先按 [多仓库软件项目](multi-repository-projects.md) 确认项目级与组件级 owner、逐仓授权，以及当前完成声明是否需要精确仓库组合；跨仓本身不规定 Unit 数量或 PR 形状。

## 3. 常见 Feature 路径

```text
Current Consumer Authority
        ↓
clarify-intent
        ↓
specify
        ↓
technical-plan?   # 仅按需
        ↓
slice-work
        ↓
readiness-check
        ↓
execute-unit
   failure? → systematic-debug
        ↓
converge
        ↓
Ready to Integrate
```

这是需要正式执行单元时的常见组合，不是每次 Repository 修改的强制状态机。当前项目事实已经满足某个责任时可以跳过；执行过程中发现上游缺口时返回真实 owner。`execute-unit` 只用于 Ready Unit，不把无正式 Unit 的有界变更伪装成 Unit。

## 4. clarify-intent

只解决会实质改变当前 Feature 的：

- Goal；
- Scope；
- 用户可见行为；
- Business Boundary；
- Acceptance；
- 重大非功能义务。

Authority 已能唯一决定的事情不重复询问。

局部、低影响、可逆 HOW 可留给直接有界变更；进入正式 Unit 时由 `execute-unit` 处理。只有跨 Unit 持续有价值的 HOW 才需要 `technical-plan`。

如果发现的是系统性 Requirement gap，返回 `establish-requirement-baseline`；如果是 systemic architecture driver，返回 `clarify-architecture`。

## 5. specify

`specify` 负责把当前 Feature 的 WHAT / WHY / Acceptance 写清楚。

一个新的 Fresh Context 执行者应能从当前 Authority + Specification 判断：

- 为什么做；
- 做什么；
- 明确不做什么；
- 用户 / 外部系统能观察到什么；
- 哪些 Business Rules 适用；
- Boundary / Failure Behavior 是什么；
- 什么 Evidence 能证明完成。

类名、文件路径、framework 构造、施工顺序等 HOW 默认不进入 Specification。

## 6. technical-plan 只在需要时使用

只有实施前存在跨多个 Execution Unit 需要稳定的 HOW 时，才值得形成独立 Technical Plan，例如：

- shared contract；
- 核心数据结构；
- 跨模块边界；
- integration；
- migration；
- deployment topology；
- 跨 Unit verification strategy；
- 高成本技术风险。

如果 Specification 可以直接映射到仓库已有模式，剩余只是局部可逆施工细节，跳过长期 Technical Plan。

Feature-specific 技术规划不能重新定义产品语义；发现产品歧义时返回 Requirement / Specification owner。

## 7. slice-work

当工作需要独立、可恢复和可验收的执行责任时，把 Ready Specification、必要 Technical Plan 与当前责任实际适用的 Consumer Current Authority 转成 context-fit Execution Units。有界变更不因发生代码修改而自动进入切分。

每个 Unit 至少明确：

- Scope；
- Authority inputs / 可恢复 Current owner 线索；
- Dependencies；
- Completion Conditions；
- Verification responsibility；
- Out of Scope。

优先切窄而完整的纵向单元，使新的 Fresh Context 能独立完成：

```text
理解
→ 实现
→ 验证
```

避免机械拆成“数据库 → 后端 → 前端 → 测试”而让责任跨多个 Unit 漂移。

Unit 的 Authority inputs 只记录切分时已知的恢复线索，不复制 Authority 正文，也不冻结后续所有适用 owner。新的 Fresh Context 必须结合当前 task / claim、Consumer locator 和当前 Repository facts 重新判断 applicability；切分后新增 / 替换 owner 或 Unit 漏记 owner，不能仅因为 Unit 未列出就忽略。

## 8. readiness-check

这是 Execute 前的只读 Gate。

它重新检查：

- 当前 Unit 的 Authority 线索能否在当前 Repository 中恢复，且当前责任实际适用的 Current Authority 是否完整、current；
- Scope / Dependencies 是否明确；
- 必要技术决定是否关闭；
- Completion / Verification 定义是否足够；
- base drift 是否使原计划失效；
- 是否存在权限、artifact lifecycle 或 local constraint blocker。

发现问题时报告 finding 并返回真实 owner，不在 Readiness 中顺手修改 Authority、Plan、代码或配置。

`PASS` 只表示当前 Unit 可以进入 Execute，不代表 Unit 已完成，也不授予 merge / release / deploy。

## 9. execute-unit

一次只执行一个 Ready Unit。

执行前重新读取：

- Unit；
- Unit 中已有 Authority 线索，以及按当前 task / claim 与 Consumer locator 重新解析出的直接 Current Authority；
- 当前代码 / runtime facts；
- 当前任务适用的 Consumer-local constraints。

即使上游规划充分，也可以形成一个临时 JIT Execution Plan 决定当前代码库里的施工顺序；它是工作材料，不自动成为长期 Authority。

意外 failure / defect 使用 `systematic-debug`。实现暴露任何适用 Current Authority 的长期语义缺口时返回真实 owner；没有对应 owner / procedure 时明确升级，不在代码里静默创造新规则。

## 10. Evidence 必须匹配 claim

自动化验证可按 Consumer 实际执行环境选择[GitHub Actions 路径](github-actions-automated-verification.md)或[本地 Docker 路径](docker-automated-verification.md)；两者均不改变当前 Authority、验收和证据责任，也不要求项目同时维护两套 CI。

不要用以下证据替代真实完成：

- “代码写完了”；
- “能编译”；
- “静态检查通过”；
- “主路径能打开”；
- “历史上跑过一次”；
- “某个脚本 exit 0”。

正确问题是：

> 哪些当前 Evidence 能真正区分这个有界变更 / Unit / Feature 的完成声明是真还是假？

Verification obligation 来自当前适用 Authority 与当前 claim，而不是来自某个固定 Authority 类型。只要适用 Authority 对视觉 fidelity、安全、可访问性或其他质量属性提出可验证义务，就必须选择能够区分该义务是否成立的 Evidence。

权限、失败边界、数据库迁移、业务数据迁移、视觉表现、外部系统或生产行为都可能需要不同 Evidence。

## 11. systematic-debug

Unexpected failure 进入 `systematic-debug`：

```text
稳定复现
→ 从 Current Authority 确认 expected behavior
→ 区分 implementation / stale verification / runtime / external dependency
→ 建立可证伪 hypothesis
→ 最低必要修复
→ regression evidence
```

不要通过猜测性大改掩盖未确认根因，也不要让旧测试反向覆盖 Current Requirement。

## 12. converge

Converge 判断完整 change 是否真正 Ready，不是“再跑一次测试”。

需要检查：

- Specification Acceptance 是否都有实现与 Evidence；
- 存在多个 Unit 时，组合后是否出现边界冲突；
- 长期 artifact responsibility 是否正确；
- 当前实现是否仍符合本 change 实际适用的 Current Authority；
- verification contract 是否仍 current；
- 是否还有已知 blocker。

缺口返回真实 owner，不在 Converge 中静默重设计。

只有 Authority、实现和当前 Evidence 一致时才返回 `Ready to Integrate`。有界变更没有正式 Unit 时，仍从当前 Authority、实际 diff 和验证证据判断完整变更是否就绪；不补造 Unit 来满足输入形式。

## 13. Human Review 与独立变更复核

Human Review 不是固定开发阶段。

当产品、业务、架构或高风险技术责任需要人工理解 / 确认时，使用 `human-review`，并把 durable semantic change 回写真正 owner。

高影响 Repository change 需要独立复核时使用 `review-change`。

两者都不自动授予 merge / release / deploy。

详见 [human-review.md](human-review.md)。

## 14. Ready to Integrate 之后

`Ready to Integrate` 表示当前 change 的通用开发责任已经收敛。

之后的：

- PR；
- human integration decision；
- merge；
- release；
- deploy；
- post-integration closure

由目标 Consumer Repository 自己的治理与授权决定。编辑、验证、commit、CI、PR 与 Execution Unit 不存在固定的一一对应关系；持续工作区中的未提交 diff 和本地验证是合法的当前执行态证据，但需要跨上下文长期成立的事实仍须进入可恢复的 Repository / GitHub 状态。

## 15. 常见误用

- **没有恢复 Authority 就写 Specification** → 先恢复 Consumer facts。
- **HOW 塞进 Specification** → WHAT / WHY 与 HOW 分开。
- **每个 Feature 都建长期 Technical Plan** → 只有跨 Unit 稳定 HOW 才需要。
- **每次小修改都创建 Execution Unit** → 先判断是否真的需要独立恢复、依赖协调或独立验收。
- **机械按技术层切 Unit** → 优先 context-fit 纵向单元。
- **Readiness 中直接修问题** → 只读 Gate，finding 返回真实 owner。
- **低强度 Evidence 冒充 completion** → Evidence 必须匹配 claim。
- **Converge 时降低目标** → 缺口返回上游 Authority。
- **Unit 完成自动开始下一 Unit** → 依赖顺序不等于新增 Execute Authority。
- **Ready to Integrate 自动 merge** → 集成仍由 Consumer Repository 决定。
- **每次 Feature 都加载整套 Guides** → 只按当前责任读取必要 Guide / Skill。

## 16. Canonical execution owners

本 Guide 只解释组合关系。真正执行责任在 installed Skills：

- `clarify-intent`
- `specify`
- `clarify-architecture`
- `technical-plan`
- `slice-work`
- `readiness-check`
- `execute-unit`
- `systematic-debug`
- `converge`
- `human-review`
- `review-change`

Consumer 自己的 Requirement、Architecture、Current Work 与 local constraints 仍由 Consumer Repository 持有。

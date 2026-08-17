# converge

## Purpose

从 Feature-wide 视角判断 Current Implemented System 与 Current Verification Evidence 是否真正符合权威 Specification，并形成 `READY` 或 `GAPS`。

本 Skill 负责 Feature 收敛，不负责单个 Execution Unit 的实施，也不把 Unit / Ticket 状态汇总当作完成结论。

`READY` 只表示 Feature 已达到 **Ready to Integrate**。本 Skill 不执行 Merge、Push、Release、Deploy 或其他 Integration 动作。

## Use When

- 相关 Execution Units 已完成或已经达到可进行 Feature-wide 收敛检查的状态；
- 需要判断整个 Feature，而不是单个 Unit；
- 需要在 Ready to Integrate 前进行 Feature-wide Review / Full Verification；
- 需要确认 Specification、Optional Technical Plan、Current System 和 Current Evidence 是否彼此收敛。

## Do Not Use When

- 当前只是验证或实施一个 Execution Unit，应使用 `execute-unit`；
- 当前仍存在明显未执行的必要 Unit，尚未达到可收敛检查状态；
- 期望用“所有 Unit / Ticket Done”直接替代 Feature Evidence；
- 当前主要问题是 Product Intent 未定义，应返回 `clarify-intent` / `specify`；
- 当前主要问题是跨 Unit Durable Technical Design 未解决，应返回 `technical-plan`；
- 当前只是需要把已确认的执行缺口塑形成 Units，应使用 `slice-work`。

不要为了“走完流程”而在 Feature 明显未达到可收敛状态时机械运行本 Skill。

## Inputs

- Specification
- Technical Plan（如存在）
- Execution Units / Status
- Current Implemented System
- Current Verification Evidence

按需还可读取：

- Repository Rules
- Relevant ADR / Domain Context
- Repository-specific Verification Configuration
- 与 Feature 直接相关的 Current Code / Tests / Runtime Evidence

只加载判断 Feature 收敛所需的最小 Feature-wide 上下文，不依赖完整 Conversation History。

## Authority Sources

遵循当前 Repository Authority Hierarchy，并坚持 Authority First。

收敛判断遵守以下规则：

1. Specification 是 Feature Intent 的主要权威，定义必须实现的 Product Behavior、Scope、Boundary 与 Acceptance。
2. Technical Plan（如存在）只约束跨 Unit Durable HOW，不能覆盖或重定义 Product Intent。
3. Execution Units / Status 用于理解执行覆盖和已完成工作，但不是 Feature Completion Authority。
4. Current Implemented System 用于判断实际系统状态，不能反向覆盖更高层 Product Authority。
5. Current Verification Evidence 用于证明当前系统行为是否满足 Specification；历史证据、旧日志或未执行的验证不能替代当前证据。
6. ADR / Domain Context 提供相关长期约束和事实。
7. Conversation History 不构成权威事实或完成证据。

如果权威来源冲突，停止相关 `READY` 判断并按 Escalation Conditions 处理；不得为了收敛而选择一个方便的解释。

## Procedure

### 1. Confirm Feature-wide Convergence Scope

确认当前目标是一个 Feature 的整体收敛，而不是单 Unit 验证。

识别：

- Feature Goal 与 Scope；
- Specification 中的 Observable Behaviors、Business Rules、Boundary / Failure Behavior、Acceptance Criteria 与 Relevant NFR；
- Optional Technical Plan 中仍然有效的 Durable Decisions；
- Execution Unit Set 及其当前状态；
- Current Implemented System；
- Current Verification Evidence。

如果仍存在明显未执行的必要 Unit，则返回执行路径并停止本 Skill；不通过形式化 `GAPS` 报告代替尚未完成的正常执行。

### 2. Build a Specification-to-System Coverage View

以 Specification 为主线建立 Feature-wide Coverage View。

对每个 Required Behavior / Acceptance Obligation 判断：

- 当前系统中是否存在对应实现；
- 实现是否完整覆盖该义务；
- 是否存在当前证据；
- 当前证据是否真正证明该义务；
- 是否存在跨 Unit 组合后才暴露的行为问题。

Coverage View 是收敛过程中的工作视图，不要求持久化成独立长期 Artifact。

### 3. Check Missing Behavior

检查 Specification 要求但 Current System 中不存在的行为。

发现 Missing Behavior 时形成 Gap，并记录：

- 缺失内容；
- 对应 Specification / Authority Reference；
- 当前系统或证据依据；
- Required Stage Return / Execution-work Direction。

不要因为关联 Unit 标记为 Done 就忽略 Missing Behavior。

### 4. Check Partial Implementation

检查行为虽已存在，但只完成部分 Scope、Boundary、Failure Handling、Acceptance 或 NFR 的情况。

Partial Implementation 仍然是 Gap。

不要把“主要路径可用”自动等同于整个 Specification 已满足。

### 5. Check Contradiction with Specification

检查 Current System 是否存在与 Specification 明确冲突的行为。

包括但不限于：

- User-visible Behavior 与要求不同；
- Business Rule 被错误实现；
- Boundary / Failure Behavior 与权威定义矛盾；
- Acceptance Result 被局部实现改变；
- 技术实现通过自身现状反向定义了新的 Product Behavior。

存在 Contradiction 时必须形成 Gap，不能通过静默修改 Specification 来让实现“变正确”。

### 6. Check Unrequested Behavior

检查 Feature 实现是否引入未经 Specification 授权、且会影响 Product Behavior、Scope、External State 或重要约束的行为。

并非所有额外代码都属于 Gap。只有具有产品、边界、风险或收敛意义的 Unrequested Behavior 才应作为 Feature Gap。

普通内部实现细节不因为 Specification 没有逐项描述就自动判定为 Unrequested Behavior。

### 7. Check Technical Plan Validity

如果存在 Technical Plan，检查其 Durable Decisions 是否仍然：

- 与 Specification 一致；
- 与 Current Architecture / System Reality 一致；
- 对当前 Feature 实施仍然有效；
- 没有被后续权威决定或系统事实淘汰。

如果 Technical Plan 已 Obsolete：

- 不要求 Current System 机械服从过时 Plan；
- 判断是否需要返回 `technical-plan` 更新 Durable Design；
- 如果 Obsolete Plan 只是不再需要、且 Current System 已由更高或更新权威充分支持，应记录相应权威状态，而不是制造虚假实现 Gap。

`converge` 不静默重写 Technical Plan。

### 8. Check Current Verification Evidence

对所有 Critical Behavior / Acceptance Obligation 检查是否具有当前证据。

Current Evidence 应满足：

- 来自当前系统状态；
- 实际执行或观察过；
- 能与具体 Required Behavior / Acceptance 对应；
- 没有被后续变更失效。

如果仓库存在适用、已授权且可发现的 Feature-wide Verification Mechanism，可按 Repository Rules 与 Current Repository State 使用它刷新关键证据。

不要硬编码通用测试命令，也不要把未运行命令、历史 CI、旧日志、推测结果或 Conversation History 当作 Current Evidence。

Critical Behavior 缺少当前证据时形成 `Unverified Critical Behavior` Gap，并阻止 `READY`。

### 9. Check Cross-unit Integration Gaps

检查各 Unit 单独通过后，组合起来是否仍存在：

- Contract / Interface mismatch；
- Data / State transition gap；
- Ordering / Dependency issue；
- End-to-end behavior break；
- Shared boundary inconsistency；
- Feature-level Acceptance 无法满足。

单 Unit 都 Completed 不代表不存在 Cross-unit Integration Gap。

### 10. Classify Each Gap by Required Return Direction

对每个 Gap 判断应该回到哪个职责层。

**Execution Work Gap**

如果 Product Intent 和 Durable Design 都仍然有效，只需要新增或修正实现工作：

- 描述所需 Execution Work；
- 交回 `slice-work` 塑形为新的或修正后的 Execution Units；
- 不在 `converge` 内直接执行这些 Units。

**Product / Requirement Gap**

如果 Gap 暴露 Product Intent、Scope、Required Behavior 或 Acceptance 本身需要改变或澄清：

- 返回 `clarify-intent` / `specify`；
- 必要时升级 Human Authority。

**Major / Durable Technical Design Gap**

如果需要新增或改变跨 Unit Durable Technical Decision：

- 返回 `technical-plan`；
- Major Architecture Direction 需要 Human Authority 时升级。

**Authority / External Action Gap**

如果需要未授权 Shared / Production / External Side Effect、不可逆操作或存在 Authority Conflict：

- 停止相关动作；
- 按 Escalation Conditions 处理。

### 11. Form the Main Verdict

主结果只能是：

```text
READY
```

或：

```text
GAPS
```

#### READY

只有在以下条件同时满足时输出 `READY`：

- Specification Required Behavior 得到完整覆盖；
- Current Implemented System 与 Specification 不冲突；
- 不存在具有收敛意义的 Unrequested Behavior；
- Optional Technical Plan 没有阻塞性的 Obsolete / Invalid Durable Decision；
- Critical Behavior 有 Current Verification Evidence；
- 不存在 Cross-unit Integration Gap；
- 当前 Feature 不存在需要阶段回退的 Blocking Gap；
- `READY` 结论由 Current System + Current Evidence 支持。

#### GAPS

只要存在阻止 Feature 与 Specification 收敛的 Gap，就输出 `GAPS`。

每个 Gap 至少包含：

- **Gap Description** — 什么没有收敛；
- **Authority / Evidence Reference** — 依据什么权威或当前证据判断；
- **Required Stage Return / Execution-work Direction** — 应回到哪里处理。

按需还可包含 Gap Type、Impact、相关 Units 等辅助信息，但不要求固定机器协议。

### 12. Apply Verification-before-claim

在输出 `READY` 前再次检查：

- 关键证据是否确实来自当前状态；
- 是否只是因为 Unit / Ticket 全部 Done 而放宽了判断；
- 是否遗漏关键 Boundary / Failure / Integration Behavior；
- 是否存在未经验证但被假设成立的 Critical Behavior；
- 是否把 Historical Evidence 当作 Current Evidence；
- 是否通过忽略 Gap 或静默改写权威获得“收敛”。

没有当前证据，不得声明 `READY`。

### 13. Stop at Ready to Integrate

输出 `READY` 后，本 Skill 到此结束。

`READY` 的含义是：

> Feature Behavior、Implementation State 和 Current Verification Evidence 已与 Specification 收敛，可以进入 **Ready to Integrate**。

它不意味着：

- 已 Merge；
- 已 Push；
- 已 Release；
- 已 Deploy；
- 已执行 Production / Shared Integration；
- 已完成任何 Repository-specific Integration Policy。

Integration 由 Human / Repository Policy 或专门的后续能力决定，不属于 `converge`。

## Outputs

主结果只有两类。

### READY

```text
READY
```

应有足够的 Current Evidence 依据支持该结论。可以按需附带简短 Evidence Summary，但不要求固定模板。

### GAPS

```text
GAPS
- Gap Description
- Authority / Evidence Reference
- Required Stage Return / Execution-work Direction
```

存在多个 Gap 时，逐项组织；可以按阻塞程度或影响排序。

`converge` 不在输出 Gaps 的同时静默修改 Specification、Technical Plan 或执行实现工作。

## Exit Conditions

只有当以下条件成立时，Feature 才从 `converge` 成功退出：

- Feature Behavior 与 Specification 收敛一致；
- Current Implementation State 与权威 Intent 一致；
- Critical Behavior 有 Current Verification Evidence；
- 不存在阻塞性的 Missing / Partial / Contradicting / Unrequested / Obsolete-plan / Unverified / Cross-unit Integration Gap；
- `READY` 由当前证据支持。

满足后进入：

> **Ready to Integrate**

如果形成 `GAPS`，本轮收敛检查结束，但 Feature 尚未满足成功 Exit Condition；应按每个 Gap 的 Return Direction 回到相应职责层。

## Escalation Conditions

出现以下情况时必须停止相关自主处理并升级或返回上游：

- Gap 需要 Product Authority 才能决定；
- Gap 需要 Major Architecture Authority；
- Authoritative Sources Conflict；
- 证明收敛需要未授权 Shared / Production / External Side Effect；
- 需要 Destructive / Hard-to-reverse Action；
- Security / Privacy Sensitive Decision；
- Agent 无权自主决定的高影响或不可逆事项。

普通、低影响、可逆且不改变 Product Intent / Major Design 的 Execution Gap 不直接升级给 Human，应交回正常执行路径。

## Context Rules

- Authority First；
- Feature-wide，但仍遵循 Progressive Disclosure；
- Specification 是 Feature Intent 的主要权威；
- Technical Plan 不能覆盖 Product Intent；
- Current System / Evidence 用于判断收敛，不反向定义 Requirement；
- Conversation History 不作为权威知识或完成证据；
- 不因 Unit / Ticket 状态为 Done 就声明 `READY`；
- `READY` 必须由 Current System + Current Evidence 支持；
- Gaps 只定位与路由，不由本 Skill 静默修复权威 Artifact 或自动执行新 Units；
- 不绑定特定语言、框架、Issue Tracker、CI、Agent Runtime 或 Verification Command；
- 不自动 Merge / Push / Release / Deploy；
- `Ready to Integrate` 是本 Skill 的终点。

## Allowed Sub-skills / Disciplines

- Verification-before-claim
- Code Review（risk-based discipline）
- Context Discipline
- Human Escalation

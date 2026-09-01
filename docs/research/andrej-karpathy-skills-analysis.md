# `multica-ai/andrej-karpathy-skills` 调研与适用性分析

**研究日期：** 2026-09-01  
**外部项目基线：** `multica-ai/andrej-karpathy-skills` `main@2c606141936f1eeef17fa3043a72095b4765b9c2`  
**本项目对照基线：** `dygapp/agentic-dev` `master@a82e559cb67cafbcf96265a70a1167a9a75db5ba`  
**性质：** Research，非规范性权威

## 1. 研究目的

本报告分析 `multica-ai/andrej-karpathy-skills` 的实际结构、方法表达和 Skill 设计，并判断其对 `agentic-dev` 当前阶段是否存在可吸收价值。

本报告遵循当前仓库的 Research 边界：

- 外部项目只作为研究输入，不自动改变 Method / Architecture / Contract Authority；
- 不因为外部项目存在一个 Skill，就默认在本仓库增加同名或等价 Skill；
- 先区分方法语义、工程纪律、Skill Packaging 与 Runtime-specific 细节；
- 只有真实 Consumer Evidence 暴露稳定职责缺口时，才考虑把研究结论提升为规范性修改。

## 2. 项目定位与结构

目标仓库不是完整的软件开发生命周期方法，而是一组面向编码 Agent 的行为约束（Behavioral Guidelines）。README 将它描述为从 Andrej Karpathy 对 LLM 编码常见问题的观察中提炼出的四条原则，并提供多种交付方式：

1. 根目录 `CLAUDE.md`：作为 Claude Code 项目级或全局行为规则；
2. `.cursor/rules/karpathy-guidelines.mdc`：作为 Cursor Rule；
3. `skills/karpathy-guidelines/SKILL.md`：作为一个可安装 Skill；
4. `.claude-plugin/`：提供 Claude Code Plugin / Marketplace Packaging。

当前 `skills/` 下实际只有一个 Skill：

- `karpathy-guidelines`

该 Skill 本身没有独立执行工作流，而是把四条横切工程纪律打包为一组行为提示。

需要特别区分：该仓库由 `multica-ai` 维护，README 表述为“derived from Andrej Karpathy's observations”。因此，本报告把它视为**对 Karpathy 观点的第三方工程化整理**，而不是 Karpathy 官方方法或官方 Skill。

## 3. 四条核心原则

### 3.1 Think Before Coding

核心意图：

- 不静默假设；
- 暴露不确定性；
- 当存在多种解释时显式提出；
- 在有更简单方案时主动指出；
- 无法理解时停止并提问。

它主要针对 Agent “选一个解释直接实现”的倾向。

### 3.2 Simplicity First

核心意图：只实现解决当前问题所需的最小代码，不增加推测性设计。

典型规则包括：

- 不增加未要求的 Feature；
- 不为单次使用建立抽象；
- 不增加未要求的 flexibility / configurability；
- 不为不可能发生的场景增加错误处理；
- 如果实现明显可以大幅缩短，应主动简化。

这组规则主要针对 overengineering、abstraction bloat 和 speculative generalization。

### 3.3 Surgical Changes

核心意图：只修改当前任务真正需要修改的内容。

典型规则包括：

- 不顺手改相邻代码、注释或格式；
- 不重构没有坏掉的代码；
- 遵循现有风格；
- 发现无关 dead code 时只报告，不自动删除；
- 当前修改产生的 unused imports / variables / functions 则应一并清理。

README / Skill 使用了一个非常强的判断句：每一处修改都应该能够追溯到用户请求。

### 3.4 Goal-Driven Execution

核心意图：把命令式任务转成可验证的成功条件，并持续循环直到取得验证证据。

典型转换：

```text
Add validation
→ write tests for invalid inputs
→ make them pass

Fix the bug
→ write a reproduction test
→ make it pass

Refactor X
→ verify tests pass before and after
```

对于多步骤工作，仓库建议使用轻量：

```text
step
→ verify
```

形式组织计划。

## 4. 与 `agentic-dev` 当前方法的对照

### 4.1 Think Before Coding：高重叠，但存在关键冲突

`agentic-dev` 已经通过以下机制覆盖其主要问题：

- `Clarify Intent` 只澄清会显著改变 Goal、Scope、Product Behavior 或 Acceptance Result 的关键歧义；
- Authority First 防止 Agent 依靠自己的猜测覆盖 Specification / Domain / Architecture；
- Human Escalation 使用 Authority / Impact / Reversibility，而不是“有不确定性就问人”；
- 普通、低影响、可逆的 Local Implementation Choice 明确由 Agent 自主裁决。

因此，目标仓库的“不要静默假设”和“暴露关键 trade-off”有价值，但它的通用表达：

> uncertain → ask

不能直接吸收到 `agentic-dev`。

如果机械采用，会削弱当前已经建立的 Agent Autonomy，重新造成过度人工确认。

**判断：** 不需要增加新 Method Stage 或新 Skill；现有方法更精细。只保留为“关键假设必须可观察、但低影响可逆实现选择不应升级”的支持性研究证据。

### 4.2 Simplicity First：当前已有基础，但表达可进一步收敛

`execute-unit` 已明确要求：

- 实现 Current Unit 所需的最小变更；
- 不扩大未经授权的 Product Scope；
- 不自动修复无关相邻问题；
- 不把当前 Unit 变成整个 Feature 的重构机会；
- 实现通用能力前先检查当前代码库、框架、标准库和已有依赖；
- 已有能力满足真实契约时优先复用；
- 不为消除字面量机械引入配置机制。

这些规则已经覆盖目标仓库“最小实现”的大部分核心意图，而且在配置治理和能力复用方面比目标仓库更精确。

目标仓库仍提供两点值得保留的补充视角：

1. **Speculative Abstraction Warning**：不要因为“未来可能复用”就在当前 Unit 创建抽象层；
2. **Speculative Flexibility Warning**：没有 Authority / Requirement / Evidence 支持时，不为未来不确定变化提前增加 configurability。

这两点目前在 `agentic-dev` 中可以从“最小变更”“不扩大范围”“复用现有能力”推导出来，但没有同样直接地表达。

**判断：** 有吸收价值，但更适合作为现有 `execute-unit` 的 Embedded Engineering Discipline 候选，而不是新 Skill。是否升级为规范规则，应等待真实 Consumer Evidence 证明 overengineering / speculative abstraction 是稳定问题。

### 4.3 Surgical Changes：与 Unit Boundary 高度一致，适合形成更强的 Review Heuristic

`agentic-dev` 已有：

- one-unit execution boundary；
- 不顺手处理相邻问题；
- 发现超出 Unit 边界的阻塞问题时返回上游职责；
- Integration / cleanup 不由执行 Skill 自动接管；
- 变更必须可追溯到 Specification / Execution Unit。

因此不存在明显的职责缺口。

但目标仓库提供了一个非常有用的工程检查视角：

> 当前 diff 中的每一处变化，都应该有当前任务范围内的理由。

原文使用“Every changed line”作为强测试。直接逐行采用可能过度机械，因为格式化、生成文件、测试夹具、必要重命名或连带清理可能不是逐行映射到用户原始措辞，却仍是完成 Unit 的必要变化。

对 `agentic-dev` 更合适的候选表达是：

> 每一个 changed region 都必须能够追溯到 Current Unit、其 Verification Responsibility，或由本次修改直接产生且必须完成的必要 cleanup；无法解释的 drive-by change 应移除或单独处理。

**判断：** 值得借鉴为 Review / Execution Heuristic，但不需要独立 `surgical-change` Skill。

### 4.4 Goal-Driven Execution：当前项目已经有更完整的闭环

目标仓库最有影响力的观点是：不要只告诉 Agent 做什么，而要给出可验证的成功条件。

`agentic-dev` 当前已经把这一点发展成更完整的责任链：

```text
Specification Acceptance Obligation
→ Implementation / Verification Responsibility
→ Planned Verification Evidence
→ Executed Current Evidence
```

同时已有：

- Acceptance Criteria；
- Observable Completion Condition；
- Readiness Gate；
- when useful 的 Failing Evidence；
- Evidence Before Claims；
- Targeted Verification；
- Feature-wide `converge`。

所以目标仓库的 `step → verify` 模式对当前方法不是缺失能力，只能作为 JIT Execution Plan 的一种可选轻量表达。

**判断：** 不需要方法或 Skill 修改。当前 `agentic-dev` 的目标驱动与验证闭环明显更系统。

## 5. Skill 层面的判断

### 5.1 不建议直接引入 `karpathy-guidelines`

原因：

1. 它同时打包 Clarification、Implementation Minimality、Diff Scope、Verification 四类不同职责；
2. 它更接近 always-on Behavioral Policy，而不是具有独立输入、Procedure、Output、Exit Condition 的可组合工作流；
3. 当前 `agentic-dev` 已明确“不把每个 Discipline 都做成 Skill”；
4. `agentic-dev` 当前核心 Skill Engineering 已关闭，新 Skill 必须由真实 Consumer Evidence 暴露稳定职责缺口；
5. 直接加载该 Skill 还会引入“有不确定性就提问”的过度保守语义，与当前 Human Escalation / Agent Autonomy 冲突。

因此，不建议新增：

- `karpathy-guidelines`
- `simplicity-first`
- `surgical-change`
- `think-before-coding`
- `goal-driven-execution`

中的任何独立 Skill。

### 5.2 更合适的吸收位置

如果后续 Consumer Evidence 支持，可考虑：

| 外部原则 | `agentic-dev` 更合适的落点 |
|---|---|
| Think Before Coding | 保持在 `clarify-intent` + Human Escalation / Authority 规则，不新增 Skill |
| Simplicity First | `execute-unit` 的 Embedded Engineering Discipline / Implementation Rule |
| Surgical Changes | `execute-unit` + Review Semantics 的 diff-scope heuristic |
| Goal-Driven Execution | 已由 Specification / Slice / Readiness / Verification / Converge 覆盖 |

## 6. Packaging / Distribution 的价值

目标仓库采用“一份核心行为规则，多种 Runtime Packaging”的做法：

```text
Behavioral Guidelines
├─ CLAUDE.md
├─ Claude Code Skill
├─ Claude Code Plugin / Marketplace
└─ Cursor Rule
```

这说明同一稳定能力可以有多个 Runtime Adapter，而不必复制多套方法定义。

这一点对 `agentic-dev` 的长期 Distribution 方向具有参考价值：未来如果真实用户需要 Claude Code、Cursor、Codex 或其他 Runtime 的直接安装体验，可以考虑：

```text
Method / Skill Authority
        ↓
Runtime-specific Packaging / Adapter
```

而不是为每个平台复制一套方法。

但当前 Project Roadmap 已把 Distribution / Bootstrap Automation / Runtime Orchestration 放在条件性后续方向。目标仓库只能说明这种 Packaging 模式可行，**不足以证明 `agentic-dev` 现在应该建立 Marketplace、Plugin Bundle 或多 Runtime Distribution Layer**。

**判断：** 作为未来 Distribution 设计参考保留，不立即实施。

## 7. 证据强度与局限

本项目当前研究基线中可以确认：

- README、`CLAUDE.md` 与 `SKILL.md` 的四条原则语义基本一致；
- Skill Packaging 很轻量，当前只有一个 Behavioral Skill；
- 仓库提供大量示例说明这些规则如何改变 Agent 的编码行为；
- 仓库支持 Claude Code Plugin 和 Cursor Rule 两类 Runtime Packaging。

同时存在以下局限：

1. 当前仓库中未发现独立 eval / benchmark / behavior test 体系；
2. README 中“guidelines are working if ...”主要给出观察指标，而不是已执行的量化验证结果；
3. 该项目的主要目标是提示词 / 行为规则简化，不解决 Specification、Architecture、Execution Unit、Fresh Context、Authority、Convergence 等完整工程治理问题；
4. 其“ask when uncertain”策略与 `agentic-dev` 对低影响可逆歧义的自主裁决存在设计目标差异。

因此，它适合作为**编码行为纪律样本**，不适合作为新的总体方法论基线。

## 8. 最终价值判断

### 8.1 对当前项目是否有价值

**有价值，但属于定向补强价值，不属于方法重构价值。**

最有价值的不是它的 Skill 形式，而是两个简洁而有辨识度的工程约束：

1. **Simplicity First**：拒绝 speculative abstraction / speculative configurability；
2. **Surgical Changes**：diff 中的变化必须能够解释为当前 Unit、验证责任或本次变更必要 cleanup 的直接结果。

### 8.2 建议吸收等级

#### A. 建议保留并优先作为候选规则

**Implementation Minimality / Simplicity**

候选语义：

- 不为单次需求建立没有当前复用证据的抽象；
- 不为未确认的未来需求提前增加 flexibility / configurability；
- 先使用当前系统已经存在且满足契约的能力；
- 只有真实 Requirement、Architecture Constraint 或 Consumer Evidence 支持时才增加复杂度。

**Diff Scope / Surgical Change Heuristic**

候选语义：

- 每个 changed region 必须能够追溯到 Current Unit、Verification Responsibility 或本次变更直接产生的必要 cleanup；
- 无关 refactor、格式调整、注释改写和 dead-code cleanup 不应混入当前 Unit。

这两组规则如果进入规范，优先落到现有 `execute-unit` / Review Discipline，而不是增加新 Skill。

#### B. 已充分覆盖，不建议继续增加规则

- Goal-Driven Execution；
- tests-first / reproduction-first；
- Evidence Before Claims；
- success criteria；
- multi-step `step → verify`。

当前 `agentic-dev` 已经通过 Acceptance Obligation、Planned Verification Evidence、Current Evidence 与 Convergence 建立更严格闭环。

#### C. 不建议吸收

- “只要不确定就停止并询问人工”的通用规则；
- 将四条行为纪律整体作为一个 always-on Super Discipline Skill；
- 仅因为 Claude / Cursor Packaging 成熟就立即建立 `agentic-dev` Marketplace / Plugin Distribution；
- 用 line-by-line literal traceability 代替 Execution Unit / Specification / Verification Responsibility 的语义追溯。

## 9. 对当前路线的建议

本次研究本身**不构成重新打开 Skill Engineering 的证据**。

建议当前仍保持：

```text
真实 Consumer 工作
      ↓
观察是否反复出现 overengineering / drive-by changes
      ↓
形成 Consumer Evidence
      ↓
如果问题稳定、跨场景重复
      ↓
定向强化 execute-unit / Review Discipline
      ↓
Fresh Runtime Eval
```

不要反向执行：

```text
发现外部优秀规则
      ↓
立即新增 Skill / Method Stage
```

如果后续 `dygapp/jilinjobs-cms` 或其他 Consumer 多次出现：

- 为当前需求引入不必要抽象；
- 为未确认未来变化提前配置化；
- 顺手修改无关代码；
- PR diff 中存在无法追溯到 Execution Unit 的 drive-by changes；

则本报告可以作为定向修改 `execute-unit` 或 Review Discipline 的研究依据。

## 10. 结论

`multica-ai/andrej-karpathy-skills` 是一个高信噪比的 Agent 编码行为规则样本，优势是短、小、易记、容易跨 Runtime 分发；其四条原则中，Goal-Driven Execution 与 `agentic-dev` 已高度重叠，Think Before Coding 的部分语义还与当前 Agent Autonomy 规则冲突。

对 `agentic-dev` 最值得保留的增量价值是：

> **不要只控制功能范围，还要显式控制实现复杂度和 diff 范围。**

当前不建议新增任何 Skill，也不建议立即修改 Method。建议把 **Speculative Abstraction / Configurability Warning** 与 **Surgical Diff Scope Heuristic** 作为候选 Embedded Discipline，等待真实 Consumer Evidence 后再决定是否固化。

## 11. 主要研究来源

目标项目：

- <https://github.com/multica-ai/andrej-karpathy-skills>
- `README.md`
- `CLAUDE.md`
- `skills/karpathy-guidelines/SKILL.md`
- `.claude-plugin/`
- `.cursor/rules/karpathy-guidelines.mdc`
- `EXAMPLES.md`

本项目对照：

- `AGENTS.md`
- `docs/method/ai-development-method.md`
- `docs/method/principles.md`
- `docs/architecture/skill-architecture.md`
- `skills/execute-unit/SKILL.md`
- `docs/project/project-roadmap.md`

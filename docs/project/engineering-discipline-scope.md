# 工程纪律研究范围

**状态：** Phase 3 Scope Baseline v0.1  
**性质：** `agentic-dev` 项目级范围与优先级决策  
**分析基线：** `master@1eb729333b4aa239dfbb1906b623b61e7c1524a9`

## 1. 目的

本文完成工程能力扩展实施计划中的 **WI-01 — 工程纪律范围设计**，用于确定 Phase 3 首批工程纪律（Engineering Discipline）的研究范围、优先级和进入顺序。

本文只决定“先研究什么以及为什么”，不直接新增 Method 阶段、Skill、Technology Profile，也不把研究候选自动提升为规范性工程规则。

后续候选能力仍必须遵循 `docs/architecture/engineering-capability-architecture.md` 定义的：

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
```

## 2. 当前输入与覆盖基线

本轮范围设计主要检查以下当前权威与既有证据：

- `docs/method/principles.md`；
- `docs/architecture/engineering-capability-architecture.md`；
- `docs/architecture/skill-architecture.md`；
- `skills/execute-unit/SKILL.md`；
- PR #41“配置责任与已有能力复用边界”的定向强化；
- PR #42 `multica-ai/andrej-karpathy-skills` 定向研究；
- 当前已有 Verification-before-claim、TDD、Review Semantics、Context Discipline、Human Escalation 与 `systematic-debug` 等能力。

现状不是“缺少工程纪律”，而是已有纪律成熟度不均衡：有些已经具备完整方法 / Skill 支撑，有些只存在分散规则或单次研究结论。

因此首批研究优先处理“已有明确价值和证据，但尚未形成系统纪律边界与专项评估”的方向，而不是重复研究已经相对成熟的能力。

## 3. 选择标准

候选方向按以下维度判断优先级。

### 3.1 跨技术栈价值

优先选择不依赖 Vue、Spring 或某个具体框架，也能够改善多数软件工程任务的规则。

### 3.2 当前体系缺口

优先选择当前已有局部规则、但职责边界、判断标准或验证模型仍不完整的方向。

已经由 Method / Skill / Guide 形成较完整闭环的方向，本阶段不重复建设。

### 3.3 证据成熟度

优先选择已经有以下一种或多种支撑的方向：

- 当前 Repository Authority 中存在相关规则；
- 既有 Consumer Evidence 已暴露相关问题；
- 已有定向 Research 提供外部成熟实践证据；
- 后续能够继续取得高质量官方、开源或专家原始来源。

### 3.4 专项评估可辨识度

优先选择能够构造“有该纪律”和“无该纪律”会产生明显不同结果的 Targeted Eval，而不是只能形成抽象口号的方向。

### 3.5 对后续 Technology Profile 的支撑价值

首批 Discipline 应尽量成为后续 Vue / TypeScript / Element Plus / Spring 等 Technology Profile 的通用底层纪律，而不是与 Profile 重复。

### 3.6 重叠与扩张风险

如果候选方向与现有 Verification、Debugging、Human Escalation 或 Skill 职责高度重叠，或者必须一次处理过大的安全 / 性能领域，优先后置并进一步拆分。

## 4. 候选方向覆盖检查

| 候选方向 | 当前覆盖 | 当前主要缺口 | Eval 可辨识度 | 本阶段判断 |
|---|---|---|---|---|
| 实现最小化 / 推测性复杂度控制 | 中 | 已有“最小 Current Unit Change”“不扩大范围”“已有能力优先复用”，但对推测性抽象、未来式灵活性、无证据扩展点仍缺少系统判断框架 | 高 | **首批第 1 项** |
| 精准修改 / 差异范围控制 | 中 | 已有单 Unit 边界和“不顺手修复”，但缺少针对最终 diff 的系统可追溯检查、必要连带清理与无关修改的边界 | 高 | **首批第 2 项（条件性）** |
| Code Review | 中 | 已有 Specification Compliance / Engineering Quality 双 Verdict 和项目级 AI Review，但工程级 Review Heuristic 仍较宽 | 中高 | 后续；优先让首批两项先形成可复用 Review Heuristic |
| Testing | 高 | 已有验收义务闭环、Readiness、Targeted Verification、TDD、Evidence Before Claims | 高 | 暂不优先，避免重复建设 |
| Refactoring | 中 | 已有“不把 Unit 变成 Feature 重构机会”，但何时允许 / 需要重构仍可深化 | 中高 | 后续；与首批两项存在前置关系 |
| Dependency Management | 中低 | 已有“检查已有依赖、避免为复用扩大依赖面”，但版本、升级、替代和供应链规则未系统化 | 高 | 后续；适合与 Technology Profile / upgrade 类任务结合 |
| API Evolution | 低至中 | Method 已识别 Public Contract Change，但兼容、弃用、迁移与版本演进纪律尚未系统化 | 高 | 后续高价值方向；先等待 Profile 最小契约与更多技术上下文 |
| Performance | 低 | 当前主要作为约束和验证关注点存在 | 中 | 领域过大，后续单独拆分 |
| Security | 低至中 | 已有高风险升级边界，但安全工程本身远大于单一纪律 | 中 | 不作为首批泛化纪律，后续按独立安全能力规划 |
| Error Handling | 低至中 | `systematic-debug` 解决未知故障路径，但设计期错误模型尚未系统化 | 中高 | 后续，可与 Technology Profile 结合 |
| Configuration | 中高 | PR #41 已明确配置责任、变化来源和不机械外部化原则 | 高 | 当前作为已有纪律证据保留，不单独重复研究 |
| Existing Capability Reuse | 中高 | PR #41 已明确先检查代码库、框架、标准库、依赖以及真实契约匹配 | 高 | 作为“实现最小化”的重要支撑维度，不单独列为首批第二项 |

## 5. 首批研究决定

### 5.1 第一项：实现最小化与推测性复杂度控制

正式研究名称暂定：

> **Implementation Minimality & Speculative Complexity Control（实现最小化与推测性复杂度控制）**

选择原因：

1. **跨技术栈价值高。** 无论后续进入 Vue、Spring 还是其他框架，Agent 都必须先判断当前需求真正需要多少实现复杂度。
2. **当前已有基础但未闭合。** `execute-unit` 已要求最小变更、不扩大产品范围、优先复用已有能力，并通过 PR #41 增加配置责任和已有能力复用规则；但“未来可能有用”的抽象、灵活性、扩展点、配置化等仍主要依靠隐含推导。
3. **PR #42 已提供直接外部证据。** `Simplicity First` 明确指出不要增加未要求的功能、单次使用抽象、未要求的灵活性和可配置性；当前研究已判断这些内容适合作为现有执行纪律候选，而不是新 Skill。
4. **能够形成强 Targeted Eval。** 可以设计同一需求下的多个实现选择，检查 Agent 是否添加未经要求的抽象层、配置项、扩展接口、额外错误处理、重复基础能力或新依赖。
5. **直接支撑 Technology Profile。** 后续框架 Profile 必须避免变成“最佳实践堆叠器”；这一纪律可以约束 Agent 只采用与当前任务和 Consumer Authority 相称的框架能力。

研究边界至少应区分：

- 必要复杂度与推测性复杂度；
- 当前需求支持的抽象与“未来可能复用”的抽象；
- 当前变化证据支持的配置化与未来式配置化；
- 复用已有能力与为了复用强行改变契约；
- 必要健壮性与无证据的防御性复杂度；
- 简单实现与“为了代码更短而牺牲可读性 / 正确性 / 安全性”的伪简化。

### 5.2 第二项：精准修改与差异范围控制

正式研究名称暂定：

> **Surgical Change & Diff Scope Control（精准修改与差异范围控制）**

该方向作为 WI-03 的条件性第二项。只有第一项研究没有暴露需要先修订工程能力架构的问题时再进入。

选择原因：

1. 当前单 Execution Unit 边界已经能够限制“做什么”，但仍需要更强的最终差异检查来判断“实际改了什么”。
2. PR #42 的 `Surgical Changes` 提供了清晰的成熟启发式：每处变更都应能解释为什么属于当前任务。
3. 它可以与实现最小化保持职责分离：
   - 实现最小化关注**方案复杂度是否必要**；
   - 差异范围控制关注**最终变更区域是否属于当前工作**。
4. 可建立强 Targeted Eval，例如在任务附近故意放置可重构代码、无关格式问题、旧 TODO、无效代码或相邻缺陷，检查 Agent 是否产生 drive-by change。
5. 该纪律未来可以直接提供给 Code Review、Refactoring 与 Technology Profile 使用。

研究边界至少应区分：

- 当前执行单元直接变更；
- 为完成验证责任必须新增 / 修改的测试和证据；
- 当前修改直接产生的必要连带清理；
- 工具格式化或生成机制产生的不可避免差异；
- 与当前工作无关、只是“顺手更好”的修改；
- 发现但不应在当前 diff 中修复的邻近问题。

## 6. 本轮不优先选择 Code Review / Testing 的原因

### Code Review

Code Review 很重要，但当前已经存在：

- P10 对 Verification、Review、Convergence 的分离；
- Specification Compliance / Engineering Quality 两类 Review Verdict；
- `agentic-dev` 自身的高影响 AI Review 机制。

当前更缺的是可以供 Engineering Quality Review 使用的具体工程启发式。先把“实现最小化”和“差异范围控制”研究扎实，可以为后续 Code Review 提供可操作检查项，而不是先建立一个宽泛 Review Discipline 再反向寻找规则。

### Testing

Testing 目前已经被以下机制较深覆盖：

- 验收义务 → 验证责任 → 计划验证证据 → 当前证据；
- Readiness Gate；
- `execute-unit` Targeted Verification；
- TDD when useful；
- `systematic-debug` 的回归验证；
- `converge` 的 Feature-wide completion check。

因此 Testing 仍是长期重要 Discipline，但当前边际收益低于首批两个方向。

## 7. 与 PR #41 的关系

PR #41 不需要被重复建设成新的 Configuration Skill 或 Existing Capability Reuse Skill。

其两项关键结论作为第一项研究的当前本地证据：

1. **配置责任判断**：不能把字面量本身视为问题；应根据维护者、变化来源、稳定性、安全 / 协议约束等判断真正责任层。
2. **已有能力复用**：实现通用能力前先检查代码库、框架、标准库和已有依赖；满足真实功能契约时优先复用，只用薄适配承载项目差异；契约不匹配时允许自有实现。

WI-02 应研究这些规则与“最小实现 / 推测性复杂度”的关系，但不得为了统一概念削弱 PR #41 已经形成的精确边界。

## 8. 与 PR #42 的关系

PR #42 已经证明 `Simplicity First` 和 `Surgical Changes` 与当前体系具有高价值重叠，并给出两个候选增强方向：

- 推测性抽象警示；
- 推测性灵活性警示；
- 变更区域对当前 Unit / 验证责任 / 必要连带清理的可追溯性。

但 PR #42 是单一外部项目的定向 Research，且其中部分“必须等待 Consumer Evidence”的历史准入表述已经由 PR #43 的 D-022 和工程能力架构取代。

因此 WI-02 / WI-03 不应直接把 PR #42 的候选句子复制进 `execute-unit`，而应按当前证据质量门槛继续补充成熟来源、处理冲突、形成候选纪律和 Targeted Eval。

## 9. 后续执行顺序

本轮范围设计完成后，按以下顺序推进：

1. **WI-02：实现最小化与推测性复杂度控制**
   - 获取高质量外部成熟来源；
   - 与当前 Method / Skill / PR #41 / PR #42 做详细对照；
   - 形成 Candidate Capability；
   - 设计 Targeted Eval；
   - 判断最终落点是 Embedded Discipline、独立规范还是其他形态。
2. **WI-03：精准修改与差异范围控制（条件性）**
   - 只有 WI-02 没有暴露能力架构缺口时进入；
   - 独立研究差异可追溯、连带清理和 drive-by change 边界。
3. 完成首批 Discipline 后，再进入 **WI-04 — Technology Profile 最小契约**。

## 10. 非目标

WI-01 不负责：

- 修改 `docs/method/*`；
- 修改任何 `SKILL.md`；
- 新增正式 Engineering Discipline 规范；
- 新增 Skill；
- 建立 Vue / Spring Technology Profile；
- 为所有工程纪律一次性建立完整路线；
- 因为选中候选方向就预先认定其最终一定进入规范性基线。

本轮只关闭一个问题：**首批工程纪律研究从哪里开始，以及为什么从这里开始。**

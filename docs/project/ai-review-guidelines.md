# AI 复核项目规则

本文定义 `agentic-dev` 仓库自身的 AI 复核（AI Review）规则。

**适用边界：** 本文属于 `agentic-dev` 的项目级治理（Project-specific Governance），不是通用方法（Method）、Skill 契约（Contract）、Skill 实现或 Consumer 使用指南（Operating Guide）。Consumer Repository 不得因为读取到本文而自动继承这些规则；只有 Consumer 自身仓库权威明确采纳时才适用。

## 1. 目标

AI Review 用于在高影响变更进入人工复核（Human Review）或集成决策前，基于当前仓库权威和最终变更状态发现：

- 权威层级不一致；
- 方法语义回归；
- Contract 与 Skill Implementation 断层；
- 未授权的范围扩大；
- 术语表达偏差；
- Human / Integration Boundary 被弱化；
- 证据不足却被提升为长期结论。

AI Review 不替代 Verification，也不构成 Human Approval 或 Merge Authorization。

## 2. 必须执行 AI Review 的变更

以下 PR 在进入 Human Review / Merge 前必须完成与风险相称的 AI Review：

- 修改 Method 或 Principles；
- 修改 Architecture 或 Skill Contract；
- 修改核心 Skill Implementation；
- 修改 `AGENTS.md`、`docs/project/*` 或其他会改变本仓库长期治理行为的规则；
- 修改会实质改变 Agent 行为的 Operating / Governance Guide；
- 同时跨越 Method、Contract、Skill、Governance 等多个权威层的同步变更。

普通低风险文字修正、链接修正、无语义影响的排版调整，不要求为了形式完整性执行重型 Review；如果它们属于上述高影响 PR 的一部分，则随该 PR 一并检查。

## 3. Review 输入

Review 不得只依赖作者的说明或此前聊天结论。至少重新读取：

1. 当前目标分支 / `master` 的仓库权威（Repository Authority）；
2. PR metadata；
3. changed files；
4. 最终 PR diff / patch；
5. 当前变更层适用的更高优先级 Authority；
6. 面向人的文档发生变化时，适用的术语表达规范；
7. 如果变更声称由 Consumer Experiment / Evidence 驱动，相应 Issue 与可验证 Evidence Reference。

Review 依据必须来自当前可验证状态，不以 Conversation History 代替仓库事实。

## 4. Review 维度

根据变更性质选择必要维度，不要求每个 PR 机械检查全部项目。

### 4.1 权威一致性（Authority Alignment）

检查低层变更是否符合更高层 Authority，是否通过 Skill、Guide 或 Project Rule 暗中改写 Method / Contract。

### 4.2 语义回归（Semantic Regression）

检查措辞、重构或补充规则是否改变已有方法意图、阶段边界、授权边界或完成语义。

### 4.3 跨层一致性（Cross-layer Consistency）

当 Method / Contract / Skill Implementation / Operating Guide 存在映射关系时，检查是否出现一层已修改、其他受影响层仍按旧规则运行的断层。

### 4.4 范围控制（Scope Control）

检查 PR 是否出现与目标无关的顺带修改、额外框架、额外 Skill、固定模板或其他缺乏证据的范围扩张。

### 4.5 术语规范（Terminology）

面向人的新增或修改文本应遵循 `docs/guides/terminology-guidelines.md`。重点检查中文主述、必要英文锚点、固定标识符保留，以及是否存在术语语义偏移或过度双语。

### 4.6 人工与集成边界（Human / Integration Boundary）

检查变更是否错误地把工具能力等同于授权，或弱化 Human Escalation、Ready to Integrate、Merge / Release / Deploy 等既有边界。

### 4.7 证据一致性（Evidence Alignment）

当变更基于实验、Consumer 或 Runtime Finding 时，检查结论是否超出了现有 Evidence 能支持的范围，并确认分类层级正确。

## 5. Finding 与结论

Review Finding 使用以下严重程度：

- **Blocking**：会导致 Authority 冲突、错误方法语义、错误授权边界、明显 Contract / Skill 断层，或使 PR 不应按当前状态进入 Human Review / Merge；
- **Medium**：不会立即破坏核心语义，但会造成持续歧义、治理不一致、术语误导或明显维护风险，应在当前 PR 收敛；
- **Low / Non-blocking**：可改进但不影响当前 PR 的安全接受。

只有在已检查维度中不存在未解决的 Blocking 或 Medium Finding 时，才能报告：

```text
AI Review: PASS
```

`PASS` 只表示当前 AI Review 未发现阻塞当前 PR 的问题，不代表 Human 已批准，也不授予 Merge 权限。

## 6. 修复后的重新复核

必须使用以下闭环：

```text
Review
  ↓
Finding
  ↓
Fix
  ↓
Re-read Final PR State
  ↓
Targeted Re-review
  ↓
PASS / Remaining Findings
```

如果 Review 后发生可能影响已检查结论的实质修改，旧 Review 不能自动覆盖新状态。必须重新读取最终 PR patch，并至少对受影响维度重新 Review。

纯粹不影响语义的 metadata 或格式变化可以采用轻量复核，不为了形式完整性重复全部检查。

## 7. Review 独立性与上下文

AI Review 不要求固定 Reviewer Agent，也不要求每次创建新会话，但 Reviewer 必须：

- 重新读取当前 Repository Authority 与最终变更状态；
- 不把作者此前未持久化的推理当作 Review 依据；
- 对高影响 Method / Contract / Governance 变更，在 Runtime 支持且成本合理时优先采用 Fresh Context 或等价的独立复核方式。

关键要求是**独立重新建立证据与判断**，而不是机械要求新的窗口或新的 Agent 实例。

## 8. Review 结果的记录

不要求为每次 AI Review 创建独立长期文档。

至少应在当前工作上下文、PR 讨论或交付汇报中明确说明：

- Review 范围 / 维度；
- Blocking / Medium Finding 数量及必要的证据引用；
- 是否经过修复后的重新复核；
- 最终结论。

如果 Review 本身产生外部写操作，继续遵循 `docs/guides/external-operation-guidelines.md` 的 Analyze → Act → Verify → Report 闭环。

## 9. 与 Human Review 的关系

以下关系必须保持明确：

```text
AI Review PASS
≠ Human Approval
≠ Merge Authorization
```

会改变 Method、Contract、核心 Skill 行为、Repository Authority 或长期治理规则的变更，即使 AI Review 已 PASS，仍应由适用的 Human Authority / Repository Policy 决定是否接受和集成。

AI 的职责是尽可能在 Human 决策前发现一致性、证据和语义问题；Human 的职责是决定高影响长期规则是否被项目接受。

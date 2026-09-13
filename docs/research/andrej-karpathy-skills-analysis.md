---
id: research:andrej-karpathy-skills
type: research
status: active
---

# `multica-ai/andrej-karpathy-skills` 调研与适用性分析

**研究日期：** 2026-09-01  
**外部项目基线：** `multica-ai/andrej-karpathy-skills` `main@2c606141936f1eeef17fa3043a72095b4765b9c2`  
**性质：** 非规范性研究输入

## 1. 研究对象

该仓库把源自 Andrej Karpathy 观点的编码行为约束整理为四类原则，并通过 `CLAUDE.md`、Cursor Rule、Skill 与 Claude Code 插件等多种运行时形式分发。它不是完整 SDLC，也不是 Karpathy 官方 Skill。

四类原则：

- Think Before Coding；
- Simplicity First；
- Surgical Changes；
- Goal-Driven Execution。

其 `karpathy-guidelines` Skill 更接近横切行为规则集合，而不是拥有独立 Trigger / Inputs / Procedure / Outputs / Exit / Escalation 的任务闭环。

## 2. 对 `agentic-dev` 的长期研究价值

### Think Before Coding

“不静默假设、暴露关键不确定性”有价值，但通用的 `uncertain → ask` 过于保守。`agentic-dev` 仍应按 Authority、影响与可逆性区分真正需要人工的高影响歧义和 Agent 可自主处理的局部可逆选择。

### Simplicity First

最重要的增量是反对没有当前证据支持的：

- 推测性抽象；
- 推测性灵活性；
- 未要求的功能 / 配置；
- 仅为假想未来复用增加的复杂度。

该结论已经由 V4 `rule:implementation-minimality` 持有；Research 不再充当第二规范 owner。

### Surgical Changes

最有辨识度的检查视角是：每个 changed region 都应能追溯到当前工作、验证责任，或由本次修改直接产生的必要清理；无法解释的 drive-by change 应移除或单独处理。

该结论已经由 V4 `rule:surgical-change` 持有。

### Goal-Driven Execution

“任务必须转成可验证成功条件”与当前 Specification、Execution Unit Completion Conditions、Verification Evidence 和 Converge 责任高度重叠，不需要新增 Skill 或方法阶段。

## 3. Skill 边界结论

不建议把以下任一项直接升级成独立 Skill：

- `karpathy-guidelines`；
- `simplicity-first`；
- `surgical-change`；
- `think-before-coding`；
- `goal-driven-execution`。

原因是它们主要是横切约束，不具备稳定独立执行闭环。V4 以 Rule 承载这类最小可发现约束。

## 4. Packaging 研究价值

同一稳定能力可以有多个 Runtime Adapter，而不需要复制多套方法定义：

```text
Method / Skill Authority
        ↓
Runtime-specific Packaging / Adapter
```

该模式可作为未来分发设计参考，但不足以证明当前应立即建立 Marketplace、插件包或多运行时分发层。

## 5. 证据局限

该外部仓库主要提供行为规则、示例与多运行时包装；研究基线中没有发现独立的量化评估 / benchmark 体系。它适合作为编码纪律样本，不适合作为新的总体方法论基线。

## 6. 结论

最值得长期保留的研究结论是：

> 不仅要控制功能范围，还要显式控制实现复杂度与差异范围。

V4 已把这两类规范语义迁入独立 Rule；本文件只保留外部来源、判断依据与 Skill/Rule 边界证据。

## 7. 主要来源

- <https://github.com/multica-ai/andrej-karpathy-skills>
- `README.md`
- `CLAUDE.md`
- `skills/karpathy-guidelines/SKILL.md`
- `.claude-plugin/`
- `.cursor/rules/karpathy-guidelines.mdc`
- `EXAMPLES.md`
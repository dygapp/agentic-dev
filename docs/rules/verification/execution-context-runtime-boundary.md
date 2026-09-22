---
id: rule:execution-context-runtime-boundary
type: rule
status: active
distribution: release-input
release-target: software-development
scope:
  phases: []
  activities: [verification, review]
  technologies: []
  artifacts: []
  risks: []
---

# 执行上下文与被测 Runtime 边界

执行当前责任的 **Execution Context** 与为了证明某项声明而调用的 **Runtime Under Test** 必须显式区分。独立性、验证深度或“换一个模型”本身，不构成启动另一个 provider、CLI、authenticated model runtime 或高成本执行面的充分理由。

默认遵守以下边界：

1. ordinary repository work、deterministic verification 与能够在当前执行面完成的语义复核，优先复用当前 Primary Agent + Repository Runtime；不得仅为了制造“第二执行者”而嵌套启动额外模型 Runtime。
2. independent review 的独立性主要来自 fresh / isolated context、重新恢复 Authority、不得继承作者结论与独立形成 findings；除非当前 Repository Authority 或 review claim 明确要求，独立 Review 不要求不同 provider、不同模型或 CLI。
3. 只有当前 claim 本身针对某个特定 Runtime 的 native discovery、authenticated behavior、provider-specific capability、permissions / isolation 或其他只有该 Runtime 能区分真假的行为时，才把该 Runtime 作为被测对象启动。Fresh Context 可以组织验证，但不能冒充 Runtime-specific Evidence。
4. 启动 authenticated model、外部 Agent 或其他明显高成本 / 长耗时 Runtime 时，执行范围必须缩到当前 claim 所需的最小场景，设置有界 timeout / cancellation / evidence recovery，并优先复用仍与 exact subject 匹配的有效证据；不得用无界模型运行替代可确定性完成的检查。
5. Runtime-specific 验证完成后，Primary Agent 仍负责重新读取结果并形成 completion claim；被测 Runtime 的自述、退出码或 `turn.completed` 等单一信号不能替代与声明相匹配的 Evidence。

如果 Consumer-local policy 指定了不同的 Primary execution surface，应替换具体执行实例，但不能取消上述“执行上下文 ≠ 被测 Runtime”、最低必要执行成本和证据类型匹配原则。
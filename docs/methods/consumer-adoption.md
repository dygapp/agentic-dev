---
id: method:consumer-adoption
type: method
status: active
distribution: release-input
release-target: consumer-installation
---

# Consumer Adoption Method

## 1. 目标与适用范围

本 Method 用于一个 Consumer Repository **首次显式采用** `agentic-dev` 的可复用 capability。

它不用于 ordinary runtime，也不意味着把 upstream 仓库完整复制进 Consumer。Consumer 始终拥有自己的 Repository Authority、Project Knowledge、项目事实和最终 local canonical owners。

核心边界：**Project 不传播，Capability 传播。** upstream Project Charter / Capability Profile / Roadmap / Evolution 只可作为 provenance / understanding context；它们不是 adoption object。

## 2. 生命周期

```text
Restore Consumer Authority
→ Select Evaluated Upstream Baseline
→ Capability Assessment
→ Local Adoption / Adaptation
→ Establish Local Project & Runtime Instance
→ Validate Adoption
→ Close Evaluated Baseline
```

## 3. Restore Consumer Authority

先恢复 Consumer 自身当前事实、Project Knowledge、Authority、现有 Method / Architecture / Skill / Rule、当前工作状态和允许修改范围。

不得把 `agentic-dev` README、Project Charter、Capability Profile、Roadmap、Issue、PR 或历史会话当成 Consumer 当前项目事实。

退出条件：Consumer 当前 canonical owners 与允许 adoption 的边界已明确。

## 4. Select Evaluated Upstream Baseline

选择一个精确、可追溯的 upstream baseline，并只读取 adoption 所需 reusable capability、其直接 Architecture 与必要 provenance / Evidence。

baseline 必须可被记录和复核；不得使用“latest”作为最终 provenance。

upstream Project Knowledge 可以帮助理解该 baseline 的目的和实例化方式，但不得因为被读取就进入 Consumer Authority。

退出条件：目标 upstream baseline 与待评估 capability 集合明确。

## 5. Capability Assessment

逐类判断 Method / Architecture / Skill / Rule / 必要 Tool contract：

- adopt：可直接接受语义；
- adapt：接受目标能力但需 Consumer-local 适配；
- reject：当前 Consumer 不采用。

Guide 只作为人类解释材料。upstream Project Knowledge 只作为 provenance / context。二者都不自动进入 Agent ordinary runtime。

不得为了省事全量复制 upstream 文档树或把 upstream Project capability profile 当作 Consumer selector / runtime catalog。

退出条件：每个目标 capability 都有明确 disposition 与 local owner 计划。

## 6. Local Adoption / Adaptation

将接受的 capability 写入 Consumer-local canonical owner。

- Method / Architecture 必须与 Consumer 自身流程和结构一致；
- Skill 尽量保持稳定 procedure；
- Rule 可根据 Consumer Authority 本地化、替代或新增；
- Tool contract 可以按 Consumer 环境实现本地 instance；
- Rule metadata 与 body 保持同源；
- upstream provenance 不替代 local Authority。

退出条件：接受能力已在 Consumer 中拥有明确、可恢复的 local owner。

## 7. Establish Local Project & Runtime Instance

Consumer 必须建立自己的 Repository-local capability instance，而不是复制 upstream Project Profile。

至少明确：

- Consumer-local Agent Bootstrap；
- 当前采用 Method 的 selector / entry；
- Skill discovery entry；
- Rule root / Rule Discovery Tool locator；
- Consumer-local Project / Roadmap / current work owner；
- 必要 Human View / recovery entry。

对于依赖 Tool、compute 或 external integration 的 accepted capability，还必须建立 Consumer-local executable instance，至少明确：

- 当前 obligation 与 canonical locator；
- Consumer 可用时的 direct execution path；
- direct path 不可用时的 automated alternate path；
- execution result / logs / artifact / terminal state 等 Evidence recovery；
- 所有 declared path 不可用、baseline 不一致或结果不可恢复时的 fail-closed behavior。

只复制 Method、Architecture、Rule、Tool source 或 Tool locator，而没有建立上述可执行闭环，不满足本阶段退出条件。具体 transport 由 Consumer 环境决定，不要求采用 upstream 的平台实例。

物理文件名和目录可由 Consumer 自己决定，只要 semantic owner 清楚。

ordinary runtime 不得要求在线读取 upstream current state，也不得在本地 discovery failure 时自动回退 upstream。

退出条件：Consumer 可仅依赖 local Project / capability state 恢复并执行普通工作。

## 8. Validate Adoption

验证至少覆盖：

- local Repository / Project Authority 恢复；
- Method entry / relevant Skill selection；
- Rule Discovery / fail-closed；
- upstream decoupling；
- Consumer-local specialization 未被 upstream 覆盖；
- upstream Project state 未成为 local current Authority；
- adoption 引入的关键行为与 completion claim。
- 依赖 Tool / compute / external integration 的 capability 能从 Consumer-local Authority 恢复 direct path、automated alternate path、result recovery 与 fail-closed behavior；
- Fresh Runtime 在不读取 upstream、Human Guide、历史聊天或 memory 的条件下实际完成上述恢复，并对目标 subject 取得 required Current Evidence。

验证范围按实际 adopted capabilities 决定，不要求无差别执行全部 upstream eval。

## 9. Close Evaluated Baseline

记录已评估 upstream exact baseline、Consumer-local adoption 状态和必要 Evidence。

完成 adoption 不产生未来自动升级义务。后续 upstream 变化只有显式进入 `method:consumer-upgrade` 才能改变 Consumer local state。

完成条件：Consumer ordinary runtime 可独立运行，local Project / capability instance 及其必要 executable path 可恢复，provenance 可追溯，Fresh Runtime Evidence 支持 adoption completion claim，且没有未声明的 upstream runtime dependency。

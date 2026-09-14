---
id: method:consumer-adoption
type: method
status: active
---

# Consumer Adoption Method

## 1. 目标与适用范围

本 Method 用于一个 Consumer Repository **首次显式采用** `agentic-dev` 的可复用能力。

它不用于 ordinary runtime，也不意味着把 upstream 仓库完整复制进 Consumer。Consumer 始终拥有自己的 Repository Authority、项目事实和最终 local canonical owners。

## 2. 生命周期

```text
Restore Consumer Authority
→ Select Evaluated Upstream Baseline
→ Capability Assessment
→ Local Adoption / Adaptation
→ Establish Local Runtime
→ Validate Adoption
→ Close Evaluated Baseline
```

## 3. Restore Consumer Authority

先恢复 Consumer 自身当前事实、Authority、现有 Method / Architecture / Skill / Rule、当前工作状态和允许修改范围。

不得把 `agentic-dev` README、Roadmap、Issue、PR 或历史会话当成 Consumer 当前项目事实。

退出条件：Consumer 当前 canonical owners 与允许 adoption 的边界已明确。

## 4. Select Evaluated Upstream Baseline

选择一个精确、可追溯的 upstream baseline，并只读取 adoption 所需能力及其直接 Architecture。

baseline 必须可被记录和复核；不得使用“latest”作为最终 provenance。

退出条件：目标 upstream baseline 与待评估能力集合明确。

## 5. Capability Assessment

逐类判断 Method / Architecture / Skill / Rule：

- adopt：可直接接受语义；
- adapt：接受目标能力但需 Consumer-local 适配；
- reject：当前 Consumer 不采用。

Guide 只作为人类解释材料，不自动进入 Agent runtime。不得为了省事全量复制 upstream 能力。

退出条件：每个目标能力都有明确 disposition 与 local owner 计划。

## 6. Local Adoption / Adaptation

将接受的能力写入 Consumer-local canonical owner。

- Method / Architecture 必须与 Consumer 自身流程和结构一致；
- Skill 尽量保持稳定 procedure；
- Rule 可根据 Consumer Authority 本地化、替代或新增；
- Rule metadata 与 body 保持同源；
- upstream provenance 不替代 local Authority。

退出条件：接受能力已在 Consumer 中拥有明确、可恢复的 local owner。

## 7. Establish Local Runtime

建立 Consumer ordinary runtime 所需的本地入口：Repository Bootstrap、Method selection、Skill discovery、Rule Discovery 与必要验证能力。

ordinary runtime 不得要求在线读取 upstream current state，也不得在本地 discovery failure 时自动回退 upstream。

退出条件：Consumer 可仅依赖 local state 恢复并执行普通工作。

## 8. Validate Adoption

验证至少覆盖：

- local Authority 恢复；
- Method entry / relevant Skill selection；
- Rule Discovery / fail-closed；
- upstream decoupling；
- Consumer-local specialization 未被 upstream 覆盖；
- adoption 引入的关键行为与 completion claim。

验证范围按实际 adopted capabilities 决定，不要求无差别执行全部 upstream eval。

## 9. Close Evaluated Baseline

记录已评估 upstream exact baseline、Consumer-local adoption 状态和必要 Evidence。

完成 adoption 不产生未来自动升级义务。后续 upstream 变化只有显式进入 `method:consumer-upgrade` 才能改变 Consumer local state。

完成条件：Consumer ordinary runtime 可独立运行，provenance 可追溯，且没有未声明的 upstream runtime dependency。
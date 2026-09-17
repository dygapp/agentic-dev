---
id: method:consumer-upgrade
type: method
status: active
---

# Consumer Upgrade Method

## 1. 目标与适用范围

本 Method 用于 Existing Consumer **显式**评估新的 `agentic-dev` upstream baseline，并决定是否改变 Consumer-local capability。

upstream 新 commit、release、Project Roadmap 或其他项目状态本身不会自动改变 Consumer；ordinary runtime 也不得触发隐式 upgrade。

核心边界：**Project 不传播，Capability 传播。** upgrade 比较 reusable capability semantic delta，而不是把 upstream Project state 同步到 Consumer。

## 2. 生命周期

```text
Restore Current Consumer
→ Select Candidate Upstream Baseline
→ Evaluate Capability Delta
→ Apply Local Decisions
→ Refresh Local Capability Instance
→ Targeted Revalidation
→ Close New Evaluated Baseline
```

## 3. Restore Current Consumer

先从 Consumer Repository 恢复当前 Project Knowledge、Authority、local Method / Architecture / Skills / Rules、已记录 evaluated baseline 与当前有效 adaptation。

升级比较的起点是 Consumer 当前 local state，而不是旧 upstream baseline 的假想镜像。

退出条件：当前 Consumer canonical state、local capability instance 与 provenance 已明确。

## 4. Select Candidate Upstream Baseline

选择精确 upstream candidate baseline，并只读取本次升级直接相关的 canonical capability assets、Architecture 与必要 Evidence。

upstream Project Charter / Capability Profile / Roadmap / Evolution 可以作为 provenance / design context 读取，但不得带入 Consumer ordinary project facts，也不是需要逐文件同步的 upgrade object。

退出条件：candidate baseline 和 capability 比较范围可复核。

## 5. Evaluate Capability Delta

针对相关 Method / Architecture / Skill / Rule / Tool / runtime contract 逐项判断：

- retain：保留 Consumer-local 现状；
- adopt：采用 upstream 新能力 / 新语义；
- adapt：采用目标变化但保持 local adaptation；
- replace：明确用新 owner / 机制取代本地旧能力；
- reject：当前不接受 upstream 变化。

比较重点是语义责任，而不是目录或文件 diff。特别检查：

- Method stage / Gate / completion 是否变化；
- Architecture ownership / runtime invariant 是否变化；
- Agent-facing runtime / execution-routing 的 mode identity、selection precedence、transition、explicit override 或 fail-closed 是否变化；
- Skill Procedure / contract 是否变化；
- Rule policy / metadata / discovery contract 是否变化；
- Tool / runtime contract 是否变化；
- Consumer-local Rule 是否仍应保留差异。

upstream Project Profile 中出现的新 Method mapping、路径、execution surface 或工具 locator 只说明 upstream 自身 current instance；除非对应 reusable capability 已被接受且 Consumer 需要调整本地 instance，否则不自动复制。

退出条件：所有 in-scope capability semantic delta 都有明确 disposition。

## 6. Apply Local Decisions

只把已接受决定写入 Consumer-local canonical owner。不得用 upstream 文件覆盖未重新裁决的 local adaptation。

需要迁移或替换时，旧 owner 的退出必须明确，避免两个 current owner 并存。

如果 accepted delta 改变 Agent-facing runtime / execution-routing semantics，先更新 Consumer-local canonical owner，再刷新 Project capability instance；Guide 或 upstream Project Profile 不能暂时代替 local owner。

退出条件：local capability state 与升级决定一致，没有隐式双 Authority。

## 7. Refresh Local Capability Instance

如果 accepted delta 改变了 Consumer 的 Method selection、Skill discovery、Rule root / Discovery Tool、Agent-facing runtime / execution-routing locator、eligible execution surfaces、Human / Agent entry 或其他 local instance pointer，更新 Consumer-local Project Capability Profile 或等价 Repository Authority。

不得把 upstream `project-capability-profile.md` 直接复制成 Consumer profile；本地 profile 只记录 Consumer 实际接受并运行的 capability instance。

runtime availability 仍按 Consumer-local contract 与当前会话事实动态验证，不因 upstream 或 local profile 声明某个 surface 就假定始终可用。

如果 accepted delta 不影响 local instance，则不为“同步最新”机械修改 Project profile。

退出条件：Consumer-local Project instance 与已接受 capability 保持一致。

## 8. Targeted Revalidation

根据实际 semantic delta 选择验证：

- Method entry / transition；
- Skill behavior；
- Rule discovery / fail-closed；
- Consumer-local policy；
- local capability profile / runtime entry；
- Agent-facing runtime / execution-routing 的 default selection、responsibility transition、explicit override、unavailable-mode fail-closed 与 broken-locator negative control（如受影响）；
- ordinary runtime upstream decoupling；
- 受影响产品 / 工程行为。

如果 runtime / execution-routing 语义或 local locator / surface instance 发生变化，必须取得对应 Fresh Runtime Evidence；旧 baseline 的 runtime PASS 不能自动支撑新 claim。

不因 baseline upgrade 自动运行所有历史 eval，但不得用旧 Evidence 支撑已发生语义变化的新 claim。

## 9. Close New Evaluated Baseline

记录新的 exact evaluated upstream baseline、关键 disposition 与当前验证 Evidence。

完成条件：Consumer-local Project / capability owners 自洽，ordinary runtime 不依赖 upstream，upstream Project state 未泄漏成 Consumer current Authority，且所有受影响 claim 有当前 Evidence 支撑。若本次改变 Agent-facing runtime / execution-routing capability，则 local canonical owner、Bootstrap locator、runtime instance 与受影响 Fresh Runtime Evidence 必须全部 current；否则 upgrade 不得关闭。

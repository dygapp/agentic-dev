---
id: method:consumer-upgrade
type: method
status: active
---

# Consumer Upgrade Method

## 1. 目标与适用范围

本 Method 用于 Existing Consumer **显式**评估新的 `agentic-dev` upstream baseline，并决定是否改变 Consumer-local 能力。

upstream 新 commit、release 或项目状态本身不会自动改变 Consumer；ordinary runtime 也不得触发隐式 upgrade。

## 2. 生命周期

```text
Restore Current Consumer
→ Select Candidate Upstream Baseline
→ Evaluate Semantic Delta
→ Apply Local Decisions
→ Targeted Revalidation
→ Close New Evaluated Baseline
```

## 3. Restore Current Consumer

先从 Consumer Repository 恢复当前 Authority、local Method / Architecture / Skills / Rules、已记录 evaluated baseline 与当前有效 adaptation。

升级比较的起点是 Consumer 当前 local state，而不是旧 upstream baseline 的假想镜像。

退出条件：当前 Consumer canonical state 与 provenance 已明确。

## 4. Select Candidate Upstream Baseline

选择精确 upstream candidate baseline，并只读取本次升级直接相关的 canonical assets、Architecture 与必要 Evidence。

不得把 upstream Roadmap / Issue current state带入 Consumer ordinary project facts。

退出条件：candidate baseline 和比较范围可复核。

## 5. Evaluate Semantic Delta

针对相关能力逐项判断：

- retain：保留 Consumer-local 现状；
- adopt：采用 upstream 新能力 / 新语义；
- adapt：采用目标变化但保持 local adaptation；
- replace：明确用新 owner / 机制取代本地旧能力；
- reject：当前不接受 upstream 变化。

比较重点是语义责任，而不是目录或文件 diff。特别检查：

- Method stage / Gate / completion 是否变化；
- Architecture ownership / runtime invariant 是否变化；
- Skill Procedure / contract 是否变化；
- Rule policy / metadata / discovery contract 是否变化；
- Consumer-local Rule 是否仍应保留差异。

退出条件：所有 in-scope semantic delta 都有明确 disposition。

## 6. Apply Local Decisions

只把已接受决定写入 Consumer-local canonical owner。不得用 upstream 文件覆盖未重新裁决的 local adaptation。

需要迁移或替换时，旧 owner 的退出必须明确，避免两个 current owner 并存。

退出条件：local state 与升级决定一致，没有隐式双 Authority。

## 7. Targeted Revalidation

根据实际 semantic delta 选择验证：

- Method entry / transition；
- Skill behavior；
- Rule discovery / fail-closed；
- Consumer-local policy；
- ordinary runtime upstream decoupling；
- 受影响产品 / 工程行为。

不因 baseline upgrade 自动运行所有历史 eval，但不得用旧 Evidence 支撑已发生语义变化的新 claim。

## 8. Close New Evaluated Baseline

记录新的 exact evaluated upstream baseline、关键 disposition 与当前验证 Evidence。

完成条件：Consumer-local current owners 自洽，ordinary runtime 不依赖 upstream，且所有受影响 claim 有当前 Evidence 支撑。
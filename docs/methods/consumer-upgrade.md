---
id: method:consumer-upgrade
type: method
status: active
distribution: release-input
release-target: consumer-installation
---

# Consumer Upgrade Method

## 1. 目标与适用范围

本 Method 用于 Existing Consumer 从**当前已安装 Release** 显式升级到一个新的**版本化 Release**。该 Release 由 `agentic-dev` 发布，并具有可验证的 identity、provenance 与兼容 / migration metadata。

它不比较 upstream Source tree，也不把 upstream 新 commit、Method / Architecture / Rule 文件变化自动同步到 Consumer。

核心边界：

> **升级比较 Release 与 Consumer-local retained obligations，不比较 Consumer tree 与 upstream Source tree。**

## 2. 生命周期

```text
Restore Current Installation
→ Select Candidate Release
→ Evaluate Release & Migration Delta
→ Build Bounded Update Plan
→ Apply Release Update
→ Reconcile Consumer-local Obligations
→ Targeted Revalidation
→ Record Installed Release
```

## 3. Restore Current Installation

先从 Consumer Repository 恢复：

- 当前 installed release identity / provenance；
- 当前 `.agents/skills/**`；
- Consumer-owned `AGENTS.md` integration；
- Consumer-local Product / Requirement / Architecture / policy；
- 上一次安装后保留或新增的 local customization；
- 当前可执行路径与 runtime facts。

升级起点是**Consumer 当前真实状态**，不是旧 upstream Source baseline 的假想镜像。

退出条件：current installed release 与 retained local obligations 已明确。

## 4. Select Candidate Release

选择精确 candidate Release，并恢复：

- version / identity；
- source SHA provenance；
- included Skill identities；
- integrity；
- compatibility；
- release notes / migration metadata；
- verification evidence locator。

不得通过读取 upstream current Method / Architecture / Rule tree 来“推断这次升级是什么”。

退出条件：candidate Release 可复核。

## 5. Evaluate Release & Migration Delta

比较：

```text
current installed release
+ Consumer-local retained obligations
+ candidate release
```

重点判断：

- Skill add / remove / replace / breaking change；
- supporting references / scripts / assets 变化；
- runtime compatibility 变化；
- executable direct / alternate path 变化；
- Bootstrap integration contract 变化；
- migration / cleanup requirement；
- Consumer-local customization 是否会冲突。

合法 disposition 可以是：

- retain current release；
- update；
- update with local reconciliation；
- reject candidate。

不得重新建立旧式的 upstream Method / Architecture / Rule 逐项 adopt / adapt / replace 表。

退出条件：candidate Release 是否可升级以及需要保留的 Consumer-local obligations 已明确。

## 6. Build Bounded Update Plan

计划至少明确：

- 哪些 installed Skill package 被新增 / 替换 / 删除；
- 哪些 Release-owned supporting resource 更新；
- Consumer-owned `AGENTS.md` 需要的最小 bounded change；
- `.agents/README.md` / generated compatibility metadata 是否更新；
- Consumer-local policy / project docs 明确保留；
- migration / rollback / failure behavior；
- 重复执行的 idempotency 边界。

Release 不拥有的 Consumer-local 文件不得因为“同步最新”被覆盖。

退出条件：update diff、ownership 与 rollback 边界清楚。

## 7. Apply Release Update

先验证 candidate artifact integrity，再更新 Release-owned assets。

更新过程中：

- 不整文件覆盖 Consumer `AGENTS.md`；
- 不删除未声明为 Release-owned 的 local files；
- 不访问 upstream Source tree 补齐 candidate；
- 旧 Release-owned asset 的退出必须清楚，避免两个 current release owner 并存；
- 中途失败时保持可恢复 / 可重试状态。

退出条件：Repository 中的 Release-owned assets 与 candidate Release 一致。

## 8. Reconcile Consumer-local Obligations

升级后重新应用并核对 Consumer-local retained obligations，例如：

- Product / Requirement / System Architecture；
- technology policy；
- authorization；
- terminology；
- current work；
- local execution / environment adaptation；
- 经明确允许的 local Skill customization。

如果 candidate Release 与 local Authority 发生真实冲突，必须由 Consumer Authority 决定；upstream provenance 不能覆盖 local truth。

退出条件：Release-owned assets 与 Consumer-owned assets 不形成隐藏双 Authority。

## 9. Targeted Revalidation

根据真实 release delta 选择验证，至少考虑：

- installed identity / integrity；
- changed Skill activation / behavior；
- Bootstrap discovery；
- supporting references / scripts；
- direct execution path / automated alternate path；
- result / Evidence recovery；
- fail-closed behavior；
- Consumer-local retained policy；
- ordinary runtime `upstream access = 0`；
- Fresh Runtime 只依赖 Consumer-local Authority 恢复受影响路径；
- 受影响的软件开发行为。

不得用旧 Release 的 Evidence 支撑已发生语义变化的新 claim，也不因升级自动执行 provider-side 全部历史 eval。

## 10. Record Installed Release

更新 Consumer-local provenance：

- 新 installed release identity / version；
- source SHA provenance；
- migration / reconciliation summary；
- 当前验证 Evidence；
- retained local obligations。

完成条件：Consumer-local ownership 自洽、candidate Release 已成为唯一 current installed release、普通运行不依赖 upstream Source，受影响 claim 有 Current Evidence。

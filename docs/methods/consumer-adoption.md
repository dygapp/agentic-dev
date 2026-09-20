---
id: method:consumer-adoption
type: method
status: active
distribution: release-input
release-target: consumer-installation
---

# Consumer Adoption Method

## 1. 目标与适用范围

本 Method 用于一个**普通软件 Consumer Repository 首次安装** `agentic-dev` 的版本化 Software Development Agent Skills Release。

它是 provider-side installation process owner，不属于 Consumer ordinary runtime，也不要求 Consumer 理解或复制 `agentic-dev` 的 Source / Authoring Model。

核心边界：

> **Consumer 安装 Release，不采用 upstream Source tree。**

Consumer 始终拥有自己的 Repository Authority、Project Knowledge、Requirement、System Architecture、技术 policy、权限和当前工作状态。

## 2. 生命周期

```text
Restore Consumer Authority
→ Select Exact Release
→ Check Release Contract & Compatibility
→ Build Bounded Installation Plan
→ Install Skill Release
→ Integrate Consumer-owned Bootstrap
→ Validate Installation
→ Record Installed Release
```

## 3. Restore Consumer Authority

先恢复 Consumer 自身：

- 根 `AGENTS.md` / Repository Authority；
- 产品、Requirement、System Architecture 与项目文档；
- 当前 `.agents/**` / installed Skills（如存在）；
- Consumer-local technology / authorization / terminology policy；
- 当前工作与允许修改范围。

不得把 `agentic-dev` Source Repository、README、Project Charter、Roadmap、Issue、PR 或历史会话当成 Consumer 当前事实。

退出条件：Consumer-owned Authority、已有 Agent assets 与允许安装边界已明确。

## 4. Select Exact Release

选择一个精确、可追溯的版本化 Release，而不是 upstream source baseline。

至少恢复：

- release identity / version；
- exact source SHA provenance；
- included Skill identities；
- integrity / checksum；
- runtime compatibility；
- installation / migration metadata；
- verification evidence locator。

不得使用“latest”作为最终 installed provenance。

退出条件：candidate Release 身份完整、内容和来源可复核。

## 5. Check Release Contract & Compatibility

只评估**发布物合同**与目标 Consumer 环境，不重新逐类评估 upstream Method / Architecture / Rule source。

至少确认：

- 目标 Agent Runtime 是否能发现发布 Skills；
- 需要的 `scripts/**` / external execution 是否有 direct path；
- direct path 不可用时是否存在 automated alternate path；
- Consumer 是否已有同名 / 冲突 Skill；
- 根 `AGENTS.md` 的 bounded bootstrap integration point；
- Consumer-local policy / docs 是否需要保留；
- candidate Release 是否声明 breaking / migration requirements。

如果 Release contract 不完整、integrity 无法验证或 Runtime 不兼容，必须 fail closed。

退出条件：形成明确的 install / no-install 决定。

## 6. Build Bounded Installation Plan

安装计划只描述 Consumer-local 变化，例如：

- 哪些 Skill package 写入 `.agents/skills/**`；
- 是否创建 / 更新 `.agents/README.md`；
- 根 `AGENTS.md` 哪个最薄片段需要增加 Skill entry / compatibility locator；
- 是否需要平台原生 adapter；
- 哪些 Consumer-local assets 明确保持不变；
- rollback / conflict / idempotency 行为。

不得把 upstream `docs/methods/**`、`docs/architecture/**`、`docs/rules/**`、Project Knowledge 或 Eval tree 当作安装清单。

退出条件：安装 diff 有界、Consumer-owned assets 的保留边界明确。

## 7. Install Skill Release

按 Release artifact 执行安装：

```text
versioned release artifact
→ verify integrity
→ materialize selected repository-local Skill packages
→ preserve Consumer-local ownership
```

安装目标默认以：

```text
.agents/skills/**
```

为主要 runtime surface。

Skill supporting resources 可以包含 `references/`、`scripts/`、`assets/`；是否存在由 Release 决定，不要求机械创建空目录。

平台固定路径的 adapter 保持平台原生位置。

退出条件：Release 文件已经准确安装，未把 provider Project / Research / Guide / Eval source 泄漏为 Consumer runtime Authority。

## 8. Integrate Consumer-owned Bootstrap

根 `AGENTS.md` 始终由 Consumer 拥有。

安装只允许添加 / 更新 Release contract 所需的薄 Bootstrap / Skill locator，必须：

- 保留 Consumer 原有 Authority；
- 不整文件覆盖；
- 不复制 Skill Procedure；
- 不维护手工 Skill inventory；
- 重复安装具有 bounded / idempotent 行为；
- 能让非原生 Skill Runtime 按 Release compatibility contract 找到 discovery entry。

`.agents/README.md` 是 Human View，不成为第二套 runtime selector。

退出条件：Consumer Bootstrap 可以进入 installed release，同时本地 Authority 未被覆盖。

## 9. Validate Installation

验证至少覆盖：

- installed release identity / integrity；
- expected Skill package 完整性；
- Consumer-owned `AGENTS.md` 未被覆盖；
- Consumer-local Requirement / Architecture / policy 未被删除；
- repository-local Skill discovery；
- Release 声明的 runtime compatibility；
- 依赖 executable capability 时的 direct execution path；
- automated alternate path；
- result / Evidence recovery；
- fail-closed behavior；
- ordinary runtime `upstream access = 0`；
- Fresh Runtime 不读取 upstream Source、历史聊天或 memory 也能恢复已安装能力。

验证范围按 Release 实际包含能力决定，不要求无差别执行 provider-side 全部 eval。

退出条件：Current Evidence 支持“该 Release 已正确安装并可由 Consumer-local runtime 使用”。

## 10. Record Installed Release

在 Consumer 自己的合适 Authority / provenance owner 中记录：

- installed release identity / version；
- source SHA provenance；
- installation evidence；
- 必要 local retained obligations；
- 明确的 local customization（如有）。

记录 installed release 不创建未来自动升级义务。后续变化只有显式进入 `method:consumer-upgrade` 才能改变 Consumer-local installation。

完成条件：Consumer ordinary runtime 只依赖 local Repository + installed release，provenance 可追溯，没有未声明的 upstream Source dependency。

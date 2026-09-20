---
id: guide:consumer-local-rule-adoption
type: guide
status: active
distribution: source-only
---

# Consumer-local Rule Adoption

本文面向人类说明如何把 `agentic-dev` 的 Rule Discovery 模型本地化到 Consumer。

## 首次采用

- 选择需要的 Rule 正文，而不是复制全量上游规则；
- 每个本地 Rule 保持 YAML Front Matter 与正文同文件维护；
- 将 Rule Discovery Tool 作为 Consumer-local capability；
- task signals 只能来自 Consumer 当前任务与仓库事实；
- 验证 malformed metadata、duplicate id 与 incomplete scan 会 fail closed。

## 普通运行

工具只返回少量 `{id,path}` locator；Agent 再读取候选正文并做最终语义适用性确认。不得维护需要人工同步的 Map / Manifest / Catalog，也不得在 discovery failure 时自动访问 upstream。

## 升级

显式 upgrade 时比较目标 upstream Rule / Tool contract 与 Consumer-local adaptation。只迁入经过 Consumer Authority 接受的变化，并重新执行受影响 lint / discovery / runtime eval。
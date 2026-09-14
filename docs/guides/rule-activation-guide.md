---
id: guide:rule-adoption-navigation
type: guide
status: active
---

# 理解 Rule Discovery

本文只面向人类解释 Rule 如何被发现和使用，不参与 ordinary runtime routing。

## 为什么不维护中心 Rule Map

每条 Rule 的发现 metadata 与规范正文同文件维护。Agent 从当前任务事实提取少量 task signals，由 `tools/rule-discovery/` 扫描 Front Matter，返回少量 `{id, path}`；随后 Agent 只读取候选正文并确认真实适用性。

这避免了需要人工同步的 Reviewed Discovery Map / Activation Manifest / Runtime Catalog，也避免把全量 Rule metadata 塞进模型上下文。

## 人怎样浏览 Rule

人类可以直接查看 `docs/rules/README.md` 的分类与 inventory。这个 README 被 Rule Discovery 明确排除，但仍参加 repository lint，因此它不会成为 runtime index。

## Agent 怎样使用 Rule

Agent 不从 README、目录枚举或文件名集合反推候选。ordinary runtime 只把 Rule Discovery 返回的 locator 作为 Rule 入口；task facts 实质变化时重新发现。

Rule 可以约束 Method stage、Skill execution 或 direct Agent work，不存在固定 `Method → Skill → Rule` 顺序。

Rule 的语义与粒度见 `docs/architecture/rule-architecture.md`；确定性发现与 fail-closed contract 见 `docs/architecture/rule-discovery-architecture.md`。
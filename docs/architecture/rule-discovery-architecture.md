---
id: architecture:rule-discovery
type: architecture
status: active
---

# 规则发现架构

## 1. 目标

V4 的规则发现只解决一个问题：在不把全量规则 metadata 或正文发送给模型的前提下，从当前任务可观察事实中筛出少量值得读取的 Rule locator。

```text
当前任务 / 仓库事实
→ 提取少量 task signals
→ Rule Discovery Tool
→ 只扫描 Rule 自身 YAML Front Matter
→ 确定性候选初筛
→ 返回少量 {id, path}
→ LLM 读取候选正文
→ LLM 做最终语义适用性确认
```

规则 metadata 与规范正文必须同源、同文件维护。不得维护需要与 Rule 同步的 Reviewed Discovery Map、Activation Manifest、Runtime Catalog、rule-index 或其他中心路由表。

## 2. 资源边界

### Skill

Skill 拥有稳定独立执行闭环：Trigger / Purpose、Inputs、Procedure、Outputs、Exit Conditions、Escalation。Skill 的选择继续使用 Agent Skills 原生发现机制，不进入 Rule Discovery Tool。

### Rule

Rule 是执行工作时必须遵守的条件、约束、默认值、不变量或完成声明要求，但本身不是完整任务流程。一个独立发现单元对应一个最小 Rule Markdown 文件。

### Guide

Guide 只承担面向人的初始化、采用、升级、低频说明和导航。普通 Agent runtime 的生成、验证、外部操作、仓库治理约束不得以 Guide 作为规范 owner。

## 3. Rule Front Matter

```yaml
---
id: rule:implementation-minimality
type: rule
status: active
scope:
  phases: [execute]
  activities: [implementation]
  technologies: []
  artifacts: [code]
  risks: []
---
```

`scope` 只允许 `phases`、`activities`、`technologies`、`artifacts`、`risks` 五个维度。每个值都是 lowercase kebab-case string array。空数组表示该维度不限制。

Front Matter 只回答“当前任务是否值得加载这个 Rule”。required checks、正文摘要、decision logic、exception list、推荐方案和 completion condition 正文必须留在 Markdown body。

## 4. Task Signals

调用方从当前任务和当前仓库事实形成同构的五个数组。五个字段必须全部出现；空数组表示已经观察为无对应信号，不代表未知。不得把预期 Rule 名、推荐答案或会话记忆写入 signals。

目录路径不构成 task signal，也不参与匹配。

## 5. 确定性匹配

对每个 `type: rule`、`status: active` 的 Rule：

- Rule 某维度为空：该维度不限制；
- Rule 某维度非空：必须与 task 同维度至少一个 token 相交；
- 任一受限维度无交集：排除；
- 所有受限维度命中：进入候选。

不使用 score、priority、embedding、模型置信度或目录分类做隐式路由。候选按 `id` 稳定排序。

## 6. 输出与渐进式披露

成功输出只包含：

```json
{
  "status": "ok",
  "scanned": 100,
  "candidate_count": 2,
  "candidates": [
    {"id": "rule:implementation-minimality", "path": "docs/rules/generation/implementation-minimality.md"}
  ]
}
```

不得返回未命中 Rule、全量 metadata、正文摘要、score 或推荐方案。LLM 只读取候选路径的正文。

因此允许 Tool CPU / I/O 随 N 增长，但 ordinary runtime 的 LLM discovery context 只能随候选数 k 增长。

## 7. Fail-closed

YAML 无法解析、schema 不完整、未知 Rule 顶层字段、scope 类型错误、非法 token、重复 Rule id、discoverable Rule 非 active、task signals 非法、扫描不完整或重复扫描同一 Rule 时，Discovery 必须返回 `fail-closed`，不得跳过坏文件后继续给出候选。

## 8. 可删除缓存

实现可以使用缓存，但缓存必须由当前 Rule Front Matter 确定性重建：

- 不人工维护；
- 不拥有规范语义；
- 不作为普通 LLM prompt context；
- 删除后不影响从真实 Rule 文件恢复。

## 9. Consumer 边界

Consumer ordinary runtime 使用 Consumer-local current Rules 与本地 Rule Discovery Tool。上游 `agentic-dev` 只作为显式 adoption / upgrade 来源；普通任务发现失败不能自动在线回到 upstream 补规则。
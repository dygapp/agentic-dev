---
id: research:llm-wiki-rule-governance
type: research
status: active
---

# LLM Wiki 与规则治理适配分析

**研究日期：** 2026-09-09  
**性质：** 非规范性对照研究

## 1. 研究对象

本研究对照：

- Andrej Karpathy 的 `LLM Wiki` gist；
- `jackwener/llm-wiki` 工程实现；
- `llmwikis.org` 的补充社区治理实践。

原始 LLM Wiki 思路的核心是：避免每次从 raw sources 重新推导全部知识，通过长期综合、薄入口、索引优先和 lint 提高知识可导航性。

## 2. 与 V4 一致的思想

### 薄启动入口

常驻入口只应告诉 Agent 最重要不变量与如何找到条件性知识，不应承载全部规则正文。

### 先发现，再深入

Karpathy 模式中的 index-first 与 V4 的 pre-LLM discovery 具有共同方向：先缩小候选，再读取真正相关正文。

### 派生层必须可回到来源

导航 / 索引不能遮蔽真实 source identity。V4 进一步收敛为 Rule metadata 与正文同文件维护；可选缓存只允许作为可删除、可重建实现细节。

### Knowledge lint 的价值

矛盾、陈旧引用、孤立资源、失效指针等健康检查具有长期价值。V4-04 的 schema / metadata lint 是这一方向的最小工程化落点，但不因此建立完整 Wiki 治理系统。

## 3. 不适合直接采用的部分

### 不建立 LLM-maintained Wiki Authority

`agentic-dev` 的 Method / Architecture / Rule / Skill 本身已经是规范性长期知识。如果再加一层 LLM-generated Wiki，会形成第二套需要同步的长期语义并产生漂移风险。

### Query synthesis 不自动晋升规则

有价值的对话综合可以进入 Research / Evidence；只有经过当前 Authority lifecycle 后才可以改变 Method / Architecture / Rule / Skill。

### 不复制 immutable raw source 层

Git 历史已经承担规范文件演进追溯。外部证据可以记录精确来源，但不需要复制所有 current Authority 形成一套只读 raw mirror。

### 不因外部实现存在而增加 Skills / search infrastructure

`ingest/query/lint/research` 的 Skill 划分属于特定产品设计，不构成本仓 Skill 准入证据。BM25、vector、graph、MCP、Obsidian 也必须由本仓实际 scaling / retrieval evidence 证明需要。

## 4. V4 相比早期方案的进一步减法

早期实验曾支持“薄入口 + 条件检索 + source pointer + fail-closed”，但仍考虑过派生索引 / current mapping。

V4 进一步取消需要人工同步维护的中心发现层：

```text
Rule file
= YAML discovery metadata + normative body
```

Tool 直接扫描 Rule Front Matter；普通 LLM context 不接收全量 metadata；只接收少量 locator。不存在 Reviewed Discovery Map / Activation Manifest / Runtime Catalog / rule-index 作为 current runtime surface。

因此本文中涉及 D1、阶段 C、旧派生索引或旧 current map 的叙述只属于研究历史，不是 current contract。

## 5. 结论

LLM Wiki 对 V4 最有价值的外部启发是：薄入口、先导航后深入、长期知识健康检查、来源可追溯，以及不要把全部知识常驻上下文。

它不支持增加新的 Wiki Authority、自动知识晋升或提前建设复杂搜索基础设施。当前 Rule Discovery contract 以 `docs/architecture/rule-discovery-architecture.md` 为唯一架构 owner。
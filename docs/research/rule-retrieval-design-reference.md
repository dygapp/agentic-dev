---
id: research:rule-retrieval-design
type: research
status: active
---

# 规则检索设计参考

**性质：** 非规范性历史实验与设计证据

## 1. 长期研究问题

规则发现只解决一个问题：根据当前任务事实找到**足以正确执行且不引入大量无关上下文**的最小规则集合。

“最小”不是固定条数或 Top-K，而是：不漏掉当前必需规则，同时不加载当前职责不需要的规则。

## 2. v1 / v2 历史实验价值

早期 v1 使用 JSON 派生 rule-index + Python 薄查询器验证稀疏检索、source identity、currentness 与 fail-closed。v2 又把相同思想投射为 Consumer-local Manifest / optional Catalog。

这些机制都已经退出 V4 current runtime；其价值只在于提供以下历史证据：

- 一个查询 / routing 应描述一个当前职责，职责变化时重新发现；
- 作用域必须保真，尤其跨仓库不能把一个仓库的规则或授权扩张到另一个仓库；
- unknown / stale / no-match 不能被乐观解释为“没有规则”；
- 派生 discovery state 不应成为 Repository Authority；
- discovery mechanism 被替换后必须退出 current runtime / eval surface，不能保留“仍可执行但已陈旧”的第三状态。

## 3. 历史 A/B 信号

冻结的 v1 隔离 A/B 中：

- 9 / 9 pair 可比较；
- 按需检索组直接命中冻结的 29 / 29 必需规则；
- 3 / 3 安全回退 reason 正确；
- 按需检索组行为语义 9 / 9 PASS，对照完整相关文档组 8 / 9；
- 直接命中场景命令输出字节约下降 48.6%，wall-clock 约下降 49.8%；
- fallback 成本更高，但 stale / unknown / no-match 的安全回退正确。

机器可读历史评分仍保留在 `evals/rule-retrieval/c3-human-scoring.json`，场景设计在 `evals/rule-retrieval/targeted-evaluation-design.json`。

这些结果证明“稀疏发现值得继续研究”，不证明旧 JSON schema、Manifest / Catalog 或具体收益比例应成为永久架构。

## 4. V4 的断代变化

V4 不再维护独立于 Rule body 的中心发现映射。

旧模型：

```text
Rule semantic owner
→ manually synchronized index / manifest / catalog
→ LLM / retriever
```

V4：

```text
Rule Markdown
= YAML Front Matter + normative body
        ↓
Rule Discovery Tool scans metadata only
        ↓
small {id,path} candidates
        ↓
LLM reads candidate bodies
```

因此旧 v1 `source_pointer` / `activation_summary` / `required_checks`、v2 Manifest / Catalog 等都不是 V4 runtime schema。

## 5. Fail-closed 的 V4 继承

V4 保留并强化早期安全原则：

- malformed metadata、duplicate id、invalid state、invalid signals、scan incomplete 等直接 `fail-closed`；
- 不跳过坏 Rule 后继续声称候选完整；
- Consumer ordinary runtime 失败不能自动在线回 upstream 补规则。

但 V4 不再需要用额外 source pointer 证明 Rule metadata 与 body 的 currentness，因为两者位于同一文件；这正是取消中心映射后的重要简化。

## 6. Token scaling 边界

早期实验关注稀疏检索相对完整文档加载的行为和成本差异。V4 把该问题变成可直接验收的不变量：

```text
Tool scans N Rule Front Matters
LLM receives k locators
LLM reads k Rule bodies
k << N
```

V4-07 必须在 20 / 100 / 500 Rules 下对同一任务实测，不能用历史 v1 A/B 或本 Research 代替。

## 7. 当前 owner

当前规范性 Rule Discovery contract 只由：

`docs/architecture/rule-discovery-architecture.md`

持有。本文只解释旧检索实验如何支持 V4，并明确哪些旧机制已经被 supersede。
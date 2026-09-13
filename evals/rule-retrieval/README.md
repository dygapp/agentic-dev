---
id: eval:historical-rule-retrieval
type: eval-guide
status: active
---

# 旧规则检索冻结评估证据

本目录只保留 V4 之前稀疏检索实验的 frozen Evaluation Evidence：

- `targeted-evaluation-design.json`；
- `c3-human-scoring.json`。

它们不是 Repository Authority，也不是 V4 current Rule Discovery corpus。

历史结果包括 9 / 9 comparable pairs、29 / 29 必需规则命中、3 / 3 安全回退 reason 和相关成本观察。旧 `UG-*` / `EO-*` / `CON-*` keys、source identities、rule-index / Manifest / Catalog 语义都属于冻结实验身份，不得解释为 V4 Rule IDs 或 runtime entry。

V4 保留的长期启发只有：

- discovery state 不能成为 Authority；
- stale / invalid / unknown 情况必须保守处理；
- 检索追求最小正确集合，而不是固定 Top-K；
- retrieval quality 必须由漏检、噪声与最终行为证据验证；
- 历史工具链被 supersede 后应退出 current runtime surface。

V4 与旧机制的关键不同是：Rule discovery metadata 与 normative body 已同文件维护，不再需要中心 source-pointer map。当前架构见 `docs/architecture/rule-discovery-architecture.md`。

V4-06 / V4-07 必须建立新的 Rule Discovery / scaling corpus；不得直接复用本目录的旧 expected keys 作为通过标准。
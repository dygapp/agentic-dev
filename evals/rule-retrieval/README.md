# 规则检索与激活 v1 冻结评估证据

本目录保留“规则治理与知识激活 v1”阶段 C 的**冻结设计与人工评分证据**。

这些资产属于历史 Evaluation Evidence，不是 Repository Authority，也不是当前 Runtime Discovery 实现。v2 已将当前 Consumer 规则发现机制收敛为 Consumer-local `Activation Manifest + optional Runtime Catalog + local semantic owner / Skill`；普通 Runtime 不使用 v1 `rule-index.json`。

## 当前保留资产

- `targeted-evaluation-design.json`：C1 冻结的 9 个 A/B 场景、隐藏断言、当时的 B 组查询与预期命中；
- `c3-human-scoring.json`：C3 的 9 / 9 pair、公平性、29 / 29 必需规则命中、3 / 3 安全回退、行为评分与成本观察。

这两个文件用于回答“v1 当时验证了什么、证据是什么”，不用于对当前 HEAD 重新执行规则发现。

其中出现的 `UG-*` / `EO-*` / `CON-*` 键、旧章节号、`query_rule_index.py` 路径和旧 source identity 都属于**冻结实验身份**，不得解释为当前规则 ID、当前章节导航或当前可执行入口。

## 已退出当前树的 v1 运行原型

v1 曾使用：

```text
rule-index.json
../query_rule_index.py
../run_rule_retrieval_ab.py
../run_rule_retrieval_c3.py
result-schema.json
fixtures/consumer-local-authority/*
```

该工具链完成了当时的验证职责，但在 v2 Guide ownership 与 Consumer-local discovery 模型确定后已经失去 Current Runtime / Regression 职责。继续保留会形成一套来源已经陈旧、却看起来仍可执行的第二发现机制，因此从当前树移除。

需要复核其精确实现时，从 v1 的 Git 历史、PR #81 / #82 及后续阶段 C 相关提交恢复，不在当前树维护其 source identity。

## v1 结论仍然有效

移除旧运行原型不删除 v1 已验证的长期结论：

- Repository Authority 与派生发现层分离；
- 派生发现信息必须可删除、可重建；
- source stale / missing / unknown / no-match 时必须 fail-closed；
- 规则发现应追求最小正确集合，而不是固定 Top-K；
- 检索效果必须通过行为语义和 Current Evidence 判断，不能由“索引能运行”代替；
- 直接命中可以显著减少规则上下文，但安全 fallback 的成本不能成为取消 fallback 的理由。

长期技术解释见：

`docs/research/rule-retrieval-design-reference.md`

v1 里程碑记录见：

`docs/project/rule-governance-knowledge-activation-v1.md`

v2 当前 Consumer-local 机制见：

- `docs/guides/consumer-local-rule-activation.md`
- `docs/project/consumer-local-activation-metadata-contract-v2.md`
- `docs/project/rule-governance-knowledge-activation-v2.md`

## 历史文本解释边界

v1 项目记录中出现的“当前索引”“当前可执行证据”等措辞描述的是**v1 完成当时的里程碑状态**。在 v2 之后恢复当前规则发现机制时，不应从这些历史措辞重新启用已退出的 JSON/Python rule-index 工具链。

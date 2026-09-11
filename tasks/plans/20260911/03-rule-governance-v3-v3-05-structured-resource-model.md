# V3-05 面向 Agent 的结构化资源模型协调

## 目标

基于已集成的 V3-01～V3-04，定义面向 Agent 的长期资源语义与最小结构契约，使 V3-06 可以直接消费资源身份和生命周期信息设计发现架构，而不重新定义语义所有者。

跟踪：Issue #109。  
分支：`docs/rule-governance-v3-v3-05-structured-resource-model`。  
启动基线：`master@cd61ab06c0194cc1cf0703aabc8aff5261529950`。

## 直接权威 / 输入

- `AGENTS.md`
- `README.md`
- `docs/project/project-roadmap.md`
- `docs/project/rule-governance-knowledge-activation-v3.md`
- `docs/project/knowledge-capability-ownership-model-v3.md`
- `docs/project/current-repository-ownership-audit-v3.md`
- `docs/project/skill-reclassification-admission-v3.md`
- `docs/architecture/engineering-capability-architecture.md`
- `docs/architecture/consumer-lifecycle.md`
- `docs/architecture/skill-architecture.md`
- `docs/architecture/technology-profile-contract.md`
- 当前 `SKILL.md`、工程纪律、技术画像、仓库本地规则、项目权威、Guide、Research / Eval 控制体实例
- `docs/project/consumer-local-activation-metadata-contract-v2.md`（过渡输入，不自动继承）
- Issue #94 / #109

## 工作顺序

```text
恢复 V3-01 四维所有权模型
→ 消费 V3-02 资源审计处置结论
→ 消费 V3-03 生命周期与 V3-04 技能 / 支持资源边界
→ 复核 v2 metadata / Manifest / Catalog 契约
→ 确定需要结构化的资源范围
→ 定义资源固有身份与最小长期结构
→ 区分固有结构 / 派生发现信息
→ 定义 Markdown / SKILL.md / 画像 / 本地规则兼容方式
→ 裁决当前有效性 / 来源追溯 / 取代 / 派生语义
→ 逐项记录 v2 字段与两层模型处置结论
→ 更新稳定恢复入口
→ 对精确候选执行 AI 复核
→ V3-05 门禁
```

## 设计约束

- 资源结构必须遵守 V3-01 四维所有权模型，不能用单一 `type` 代替所有权判断；
- metadata 不复制规范正文、规则摘要、当前门禁、Issue / PR 状态或模型答案；
- 资源固有结构与 V3-06 的索引 / 查询 / 路由投影严格分层；
- 物理表示可多样，不默认要求全仓 Front Matter；
- `SKILL.md` 现有 `name` / `description` 兼容处理不得改变技能契约；
- 支持资源继续服从 V3-04 边界，不因结构化获得平级所有权；
- 使用方采用完成后的普通运行继续只依赖使用方本地当前资源；
- 派生发现产物可删除 / 重建而不损失规范性事实。

## 非目标

本计划不：

- 实现或冻结 Runtime Catalog / Activation Manifest / Rule Index / generator；
- 设计完整发现、查询、排序、路由或阶段返回算法；
- 全仓批量增加 Front Matter；
- 建立数据库、向量库、图数据库、MCP 服务或后台 daemon；
- 物理迁移全部 Guide / Policy / Project / Research-Eval 文件；
- 修改任何使用方仓库；
- 重新设计 V3-03 生命周期或 V3-04 技能身份；
- 启动 V3-06～V3-08。

## 完成条件

- 结构化资源范围有稳定判断；
- 最小资源身份与 V3-01 四维模型一致；
- 固有结构与派生发现信息边界明确；
- Markdown、`SKILL.md`、画像、本地规则与支持资源兼容方式明确；
- 当前有效性 / 来源追溯 / 取代 / 派生语义明确；
- v2 metadata / Manifest / Catalog 完成逐项处置；
- V3-06 可以直接消费资源模型而无需重新定义资源身份；
- AI 复核不存在未解决的 Blocking / Medium；
- 未越界实施 V3-06～V3-08。

## 最终复核记录原则

精确候选 Head、最终 AI Review 和集成状态属于 GitHub PR 原生状态，不写入本长期协调计划。最终门禁必须以 PR #110 当前实际 Head 为对象重新核验；只有该精确 Head 的 AI 复核不存在未解决的 Blocking / Medium，且不存在 base drift / 范围漂移，才能进入集成判断。
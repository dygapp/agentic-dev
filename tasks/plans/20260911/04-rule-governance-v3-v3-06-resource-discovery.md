# V3-06 资源发现架构协调

## 目标

基于已集成的 V3-01～V3-05，定义最小资源发现架构，使新上下文和按需职责只依赖当前仓库本地现行资源，可靠得到一个主职责、最小辅助上下文和可解释阶段动作，同时不重新定义资源身份或复制规范正文。

跟踪：Issue #111。  
分支：`docs/rule-governance-v3-v3-06-resource-discovery-architecture`。  
启动基线：`master@640f1e3a8e7b5a6e67ad9ea028e51ba621e37964`。

## 直接权威 / 输入

- `AGENTS.md`
- `README.md`
- `docs/project/project-roadmap.md`
- `docs/project/rule-governance-knowledge-activation-v3.md`
- `docs/project/knowledge-capability-ownership-model-v3.md`
- `docs/project/current-repository-ownership-audit-v3.md`
- `docs/architecture/consumer-lifecycle.md`
- `docs/project/skill-reclassification-admission-v3.md`
- `docs/architecture/agent-resource-model.md`
- `docs/architecture/skill-architecture.md`
- `docs/architecture/skill-contracts.md`
- `docs/guides/rule-activation-guide.md`
- `docs/guides/consumer-local-rule-activation.md`
- `docs/project/consumer-local-activation-metadata-contract-v2.md`
- `docs/project/consumer-local-runtime-routing-interface-v2.md`
- Issue #94 / #111

## 工作顺序

```text
恢复 V3-05 资源模型输入契约
→ 提取 v2 已验证发现 / 路由行为
→ 裁决最小发现层级
→ 定义当前资源集合形成规则
→ 定义任务事实与派生查询提示
→ 定义候选发现与最小集合
→ 定义一个主职责 + 最小辅助上下文
→ 定义 routing-only / 按需 Skill
→ 定义 Stage Return / 旧状态失效
→ 定义失败关闭与本地回退
→ 定义派生表示生成 / 更新 / 失效 / 重建
→ 逐项裁决 v2 discovery / routing 资产
→ 定义 V3-07 自采用输入契约
→ 更新稳定恢复入口
→ 对精确候选执行 AI 复核
→ V3-06 门禁
```

## 设计约束

- 发现对象是 V3-05 定义的资源，不是任意文件；
- 一个混合文件可包含多个独立资源单元，不能按目录 / 扩展名重新合并；
- 派生发现层不维护第二份 `active/current` 真值；
- 任务事实是当前运行输入，不写回资源固有结构；
- 资源原生 `name / description / applicability` 等信息继续由真实语义所有者维护；
- 跨资源职责 / 条件 / 风险等正规化信息只能是可重建派生提示；
- ordinary runtime 不自动访问 upstream；
- routing-only 不机械加载完整 Skill；
- Stage Return 后重新发现，不建立第二方法状态机；
- 同一发现职责只能有一个 current 派生机制；
- 现有 v2 兼容入口在 replacement 设计、验证并集成前继续有效。

## 非目标

本计划不：

- 重新定义 V3-01～V3-05；
- 创建 Rule Super Skill / Stage Router Skill / Runtime Controller；
- 全仓批量增加 Front Matter；
- 修改使用方仓库；
- 直接执行 V3-07 / V3-08；
- 在替代机制验证并集成前删除 v2 discovery / activation 入口；
- 建立数据库、向量库、图数据库、MCP 服务或后台 daemon；
- 启动 WI-06 / WI-07 / WI-09。

## 完成条件

- 最小发现架构已明确，且不机械继承 v2 Manifest + Catalog 两层；
- 当前资源集合形成规则不制造第二 current-state 真值；
- 任务事实、资源原生结构和派生查询提示边界明确；
- 候选发现、一个主职责、最小辅助上下文、routing-only / Skill execution、Stage Return、fail-closed 接口稳定；
- 派生表示的生成、更新、语义陈旧与确定性重建规则明确；
- v2 discovery / routing 资产完成逐项处置与 replacement / compatibility 设计；
- V3-07 可以直接消费该架构进行 `agentic-dev` 自采用；
- AI 复核不存在未解决的 Blocking / Medium；
- 未越界修改 Consumer 或提前实施 V3-07 / V3-08。
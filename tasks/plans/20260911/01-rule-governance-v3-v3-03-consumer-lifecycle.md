# V3-03 使用方生命周期协调

## 目标

基于已集成的 V3-01 所有权模型和 V3-02 审计矩阵，完成 V3-03 — 使用方初始化、采用、升级与普通运行生命周期的长期规范收敛。

跟踪：Issue #104。  
分支：`docs/rule-governance-v3-v3-03-consumer-lifecycle`。  
启动基线：`master@ce7ab292f8ddf8b8512d406061a31a7db8ad9409`。

## 直接权威 / 输入

- `AGENTS.md`
- `README.md`
- `docs/project/project-roadmap.md`
- `docs/project/rule-governance-knowledge-activation-v3.md`
- `docs/project/knowledge-capability-ownership-model-v3.md`
- `docs/project/current-repository-ownership-audit-v3.md`
- `docs/guides/using-agentic-dev.md`
- `docs/guides/consumer-local-rule-activation.md`
- `docs/project/consumer-local-baseline-adoption-projection-v2.md`
- `docs/project/consumer-local-rule-runtime-target-v2.md`
- Issue #94 / #104

## 范围

1. 建立使用方生命周期的单一规范所有者；
2. 收敛新使用方初始化与首次采用边界；
3. 收敛已有使用方基线升级与逐项采用决定；
4. 明确上游评估基线、当前本地资产来源与仅升级使用的决策历史；
5. 明确采用验证与基线推进门禁；
6. 明确仅依赖本地当前状态的普通运行不变量与显式重新进入上游条件；
7. 明确与核心方法、Guide、技能、V3-05、V3-06、V3-08 的责任边界；
8. 回写 README、Roadmap、v3 项目记录和必要稳定权威指针；
9. 对精确候选执行与风险相称的 AI 复核并裁决阻塞 / 中等级问题。

## 非目标

本计划不：

- 重做 V3-02 仓库盘点；
- 物理移动、拆分、删除或重命名 Guide / Authority；
- 修改现有 `SKILL.md`；
- 冻结 Front Matter / metadata schema；
- 实现 Rule Index / Manifest / Catalog / generator；
- 实现资源发现 / 路由架构；
- 创建新的采用 / 升级 Super Skill；
- 修改任何使用方仓库；
- 启动 V3-04～V3-08。

## 工作顺序

```text
读取 V3-02 生命周期处理候选
→ 提取 v2 过渡性现行生命周期证据
→ 形成单一使用方生命周期模型
→ 复核语义所有者与后序阶段边界
→ 更新稳定恢复入口
→ 对精确 Head 执行 AI 复核
→ 裁决并修复问题
→ V3-03 门禁
```

## 完成条件

- `docs/architecture/consumer-lifecycle.md` 足以作为 V3-03 的长期规范所有者；
- 生命周期状态与转换、首次采用、基线升级、采用验证、基线推进、普通运行、重新进入上游之间无相互冲突；
- v2 已验证行为得到明确保护；
- 后序 V3-04 / V3-05 / V3-06 / V3-08 可以直接引用该权威，不需要重做同义生命周期分析；
- 仓库恢复入口与 Issue #104 当前状态一致，并且不会因本 PR 集成立即陈旧；
- AI 复核不存在未解决的阻塞或中等级问题；
- 未越界实施后序处理候选。
# V3-03 Consumer 生命周期协调

## 目标

基于已集成的 V3-01 所有权模型和 V3-02 审计矩阵，完成 V3-03 — Consumer 初始化、采用、升级与普通运行生命周期的长期规范收敛。

跟踪：Issue #104。  
分支：`docs/rule-governance-v3-v3-03-consumer-lifecycle`。  
启动基线：`master@ce7ab292f8ddf8b8512d406061a31a7db8ad9409`。

## 直接 Authority / 输入

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

1. 建立 Consumer lifecycle 单点规范 owner；
2. 收敛新 Consumer 初始化与首次采用边界；
3. 收敛 Existing Consumer baseline upgrade 与逐项 adoption decision；
4. 明确 evaluated baseline、active asset provenance、upgrade-only decision history；
5. 明确 adoption verification 与 baseline advance Gate；
6. 明确 ordinary-runtime local-only invariant 与显式 upstream re-entry 条件；
7. 明确与 Method、Guide、Skill、V3-05、V3-06、V3-08 的责任边界；
8. 回写 README、Roadmap、v3 项目记录和必要稳定 Authority 指针；
9. 对精确候选执行与风险相称的 AI 复核并裁决 Blocking / Medium finding。

## 非目标

本计划不：

- 重做 V3-02 Repository inventory；
- 物理移动、拆分、删除或重命名 Guide / Authority；
- 修改现有 `SKILL.md`；
- 冻结 Front Matter / metadata schema；
- 实现 Rule Index / Manifest / Catalog / generator；
- 实现 discovery / routing architecture；
- 创建新的 adoption / upgrade Super Skill；
- 修改任何 Consumer Repository；
- 启动 V3-04～V3-08。

## 工作顺序

```text
V3-02 lifecycle dispositions
→ v2 transitional-current lifecycle evidence
→ single Consumer lifecycle model
→ owner / downstream boundary check
→ recovery entry update
→ exact-head AI review
→ finding adjudication
→ V3-03 Gate
```

## 完成条件

- `docs/architecture/consumer-lifecycle.md` 足以作为 V3-03 的长期规范 owner；
- lifecycle state / transition、首次采用、upgrade、verification、baseline advance、ordinary runtime、re-entry 无相互冲突；
- v2 已验证行为得到明确保护；
- 后序 V3-04 / V3-05 / V3-06 / V3-08 可以直接引用该 Authority，不需要重做 lifecycle analysis；
- Repository recovery entry 与 Issue #104 当前状态一致；
- AI 复核不存在未解决的 Blocking / Medium finding；
- 未越界实施后序 disposition。

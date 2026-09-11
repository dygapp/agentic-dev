# V3-04 技能重分类与准入协调

## 目标

基于已集成的 V3-01 所有权模型、V3-02 当前仓库所有权审计和 V3-03 使用方生命周期，完成 V3-04 — 技能重分类与准入的规则族裁决。

跟踪：Issue #107。  
分支：`docs/rule-governance-v3-v3-04-skill-reclassification`。  
启动基线：`master@3043e95193f462348dd9fcb99f8a1871145d503d`。

## 直接权威 / 输入

- `AGENTS.md`
- `README.md`
- `docs/project/project-roadmap.md`
- `docs/project/rule-governance-knowledge-activation-v3.md`
- `docs/project/knowledge-capability-ownership-model-v3.md`
- `docs/project/current-repository-ownership-audit-v3.md`
- `docs/architecture/engineering-capability-architecture.md`
- `docs/architecture/consumer-lifecycle.md`
- `docs/architecture/skill-architecture.md`
- `docs/architecture/skill-contracts.md`
- `docs/architecture/engineering-disciplines.md`
- `skills/README.md`
- 当前 9 个 `skills/*/SKILL.md`
- V3-02 指向 V3-04 的 Guide / 验证 / 外部操作 / 历史 Skill 设计输入
- Issue #94 / #107

## 工作顺序

```text
恢复当前 Skill 架构 / 契约
→ 逐一复核 9 个 Skill 身份
→ 对照 V3-02 重叠风险检查真实正文
→ 裁决 Guide / 工程纪律 / 验证 / 外部操作边界
→ 裁决第一批历史设计与当前权威
→ 收敛 Skill 准入 / 支持资源规则
→ 只做必要当前权威修正
→ 更新稳定恢复入口
→ 对精确 Head 执行 AI 复核
→ V3-04 门禁
```

## 非目标

本计划不：

- 重新设计 V3-03 使用方生命周期；
- 因阶段名称叫“重分类”就批量新增、删除或重写 Skill；
- 创建规则超级 Skill、阶段路由 Skill、采用 / 升级 Skill；
- 冻结 Front Matter / metadata 结构；
- 实现 Rule Index / Manifest / Catalog / generator；
- 实现完整资源发现 / 路由架构；
- 物理迁移 Guide / Policy / Authority；
- 修改任何使用方仓库；
- 启动 V3-05～V3-08。

## 完成条件

- 当前 9 个 Skill 的身份、作用域与重叠均有明确结论；
- `execute-unit` / `converge` / `github-actions-verification` 的跨语义所有者边界完成针对性复核；
- 验证规则族与外部操作规则族是否 Skill 化有明确结论；
- Guide / 派生路由中的 Skill 执行过程重复有明确处理结论；
- `first-batch-skill-design.md` 不再与当前 Skill 架构 / 契约 / `SKILL.md` 形成平行当前权威；
- 新 Skill 准入与支持资源边界稳定；
- AI 复核不存在未解决的阻塞或中等级问题；
- 未越界实施 V3-05～V3-08。

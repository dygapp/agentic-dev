# 规则治理与知识激活 v3 规划协调

## 目标

在规则治理与知识激活 v2 已集成后，正式启动下一有限规划里程碑，并先完成 V3-01 — 知识与能力所有权模型。

跟踪入口：

- Issue #94 — 规则治理与知识激活 v3；
- Issue #95 — V3-01 知识与能力所有权模型；
- 分支 `docs/rule-governance-knowledge-activation-v3-planning`。

## 权威 / 输入

- `AGENTS.md`
- `docs/project/project-roadmap.md`
- `docs/method/ai-development-method.md`
- `docs/method/principles.md`
- `docs/architecture/engineering-capability-architecture.md`
- `docs/architecture/skill-architecture.md`
- `docs/architecture/skill-contracts.md`
- `docs/architecture/engineering-disciplines.md`
- `docs/architecture/technology-profile-contract.md`
- Issue #94 / #95
- 临时 v3 GPT-6 评估只作为启动前挑战证据，不直接成为仓库权威。

## 当前范围

1. 固化 v3 的项目级规划权威；
2. 修正 README / Roadmap，使其与 v2 已集成及 v3 已启动的事实一致；
3. 形成 V3-01 四维所有权判断矩阵；
4. 用代表性现有资源验证分类规则；
5. 对候选变更完成与风险相称的 AI 复核；
6. 只有 V3-01 Gate 满足后，才判断是否进入 V3-02。

## 非目标

本轮不：

- 物理重构 `docs/guides/*`；
- 新增或重构技能；
- 设计或实现新的 Manifest / Catalog / Rule Index；
- 冻结 Front Matter schema；
- 修改 Consumer Repository；
- 合并当前规划分支。

## 工作顺序

```text
恢复当前仓库权威
→ 固化 v3 规划权威
→ 完成 V3-01 所有权模型
→ 更新 README / Roadmap 恢复入口
→ 建立 Draft PR
→ AI 复核
→ 修订 / 定向复核
→ V3-01 Gate 判断
```

## 完成条件

- v3 当前目标、阶段顺序、非目标和 Gate 已进入 `docs/project/*`；
- V3-01 明确区分语义所有者、适用范围 / 来源状态、运行 / 生命周期角色、载体 / 权威形式；
- 代表资源能够按同一判断矩阵分类，不依赖所在目录名称；
- Guide 不再被定义为“不属于核心方法 / 技能”的默认容器；
- 新技能准入不因“可复用”或“Agent 会读取”而放宽；
- 没有未解决的阻塞或中等级所有权歧义；
- 未越界进入 V3-02 的物理迁移或后续实现。

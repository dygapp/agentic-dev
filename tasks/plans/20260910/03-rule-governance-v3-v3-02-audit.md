# V3-02 当前仓库所有权审计协调

## 目标

基于已经集成的 `docs/project/knowledge-capability-ownership-model-v3.md`，完成 `agentic-dev` 当前长期资源与主要规则族的语义所有权审计，形成后续 V3-03～V3-06 可直接消费的 disposition 候选。

当前跟踪：Issue #101。  
当前分支：`docs/rule-governance-v3-v3-02-ownership-audit`。  
审计基线：`master@c646e4182cb32344feb9e0872bb3828d4be01481`。

## 当前范围

1. 盘点当前长期资源，并区分现行权威、可复用能力、仓库本地政策、Guide、研究 / 证据和历史项目记录；
2. 对高风险混合文件按规范正文 / 规则族分类；
3. 对仍支撑现行 v2 行为但位于已完成 `docs/project/*` 中的契约标记过渡状态；
4. 形成 `keep / move / merge / split / supersede / delete / reclassify` 候选；
5. 更新 README、Roadmap 与 v3 项目规划的当前工作入口；
6. 对审计矩阵执行高影响 AI 复核和独立一致性复核。

## 非目标

本轮不：

- 物理移动、拆分、重命名或删除现有 Guide / Authority；
- 修改任何 `SKILL.md`；
- 新增 Rule Index / Manifest / Catalog；
- 冻结 Front Matter / metadata schema；
- 修改 Consumer Repository；
- 提前形成 V3-03 / V3-04 的最终设计或新 Skill 准入结论。

## 审计顺序

```text
V3-01 所有权模型
→ 当前 Repository inventory
→ 高风险 Guide / Policy / Capability 混合体
→ Method / Architecture / Skill 稳定 owner
→ v2 过渡性现行契约 vs 历史证据
→ Research / Eval / Task 生命周期
→ disposition 矩阵
→ 独立复核
→ V3-02 Gate
```

## 完成条件

- `docs/project/current-repository-ownership-audit-v3.md` 覆盖当前重要长期资源与主要规则族；
- 每个高风险项都有语义所有者、适用范围、来源状态、生命周期、载体、重叠风险与 disposition；
- `docs/guides/*` 不再被整目录机械视为 Guide；
- v2 项目记录中仍承担现行可复用语义的部分与纯历史 / 证据部分已经区分；
- Skills 保持过程型能力单点 owner，工程纪律 / 画像不被机械 Skill 化；
- 当前没有执行物理迁移；
- 独立复核不存在未解决的阻塞或中等级所有权歧义。
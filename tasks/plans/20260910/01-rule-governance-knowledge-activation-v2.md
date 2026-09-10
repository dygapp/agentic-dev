# 规则治理与知识激活 v2 协调计划

## 目标

协调 Issue #92 所跟踪的“规则治理与知识激活 v2”有限里程碑。

项目级目标、设计约束、阶段路线与完成定义统一以：

`docs/project/rule-governance-knowledge-activation-v2.md`

为准。本计划不复制或改写该长期项目级 Authority。

## 启动基线

`master@b6a20053a7a6f4f53915bea8218604720412c302`

跟踪入口：Issue #92。

## 当前工作项

### A1 — 建立 Consumer-local 目标基线

当前只先完成 Consumer-local Runtime Target 的事实与边界审计，不提前冻结 metadata schema、物理目录、Guide 拆分方案或 runtime tooling。

A1 需要形成可复核结果：

1. Consumer 普通 Fresh Context 的最小启动输入是什么；
2. 当前 Consumer-local Authority / Rule / Skill / Evidence 中哪些属于运行时可发现对象；
3. Consumer-native rule 与 adopted reusable rule 如何保持不同来源身份但进入同一本地发现路径；
4. ordinary Consumer work 在什么边界下不得依赖 upstream；
5. Consumer-local discovery 的最小成功路径与 fail-closed 路径；
6. baseline adoption / upgrade 如何为本地发现资产提供 provenance、优先级和更新触发；
7. 后续真实 Consumer 验证必须证明哪些可观察行为。

A1 产物应优先进入当前 v2 项目记录的对应阶段结论或必要的专门设计文档；如果只是过程审计，不进入长期 Research。

## 后续顺序

A1 通过后才继续：

```text
A2 Consumer-local 验收场景矩阵
→ B Rule Ownership / Guide Decomposition 审计
→ C 最小 Metadata / Catalog 契约
→ D Discovery / Routing / Skill 接口
→ E Baseline Adoption / Consumer-local Projection
→ F 真实 Consumer 验证
→ G 收敛与最终复核
```

后续阶段可以根据证据细化工作项，但不得因为目录或编号提前把尚未完成上游设计的候选描述为已就绪执行单元。

## 输入

当前最小输入：

- `AGENTS.md`
- `docs/project/project-roadmap.md`
- `docs/project/rule-governance-knowledge-activation-v2.md`
- `docs/guides/rule-activation-guide.md`
- `docs/guides/using-agentic-dev.md` §6.1 / §7
- `docs/architecture/engineering-capability-architecture.md` §9 / §10 / §11
- Issue #58 中与 Existing Consumer 可发现性、baseline adoption 直接相关的证据
- Issue #92
- v2 临时 eval 分支中的已接受设计证据，只在需要复核实验细节时读取

不要默认恢复 v1 已关闭里程碑的完整过程文档或所有 eval 输出。

## 范围控制

A1 不：

- 修改核心 Method / Principles；
- 修改正式 Skill；
- 拆分正式 Guide；
- 产品化 eval manifest；
- 修改 Consumer Repository；
- 新增 Runtime Rule Index、数据库、MCP 或服务；
- 启动 WI-07 或其他候选；
- 继续增加 GPT-5.6 / GPT-6 Runtime Eval 场景。

## 阻塞与升级

只有出现以下情况才停止当前 A1 并升级：

- 需要改变 Consumer Authority 优先这一上游方法边界；
- 需要引入会改变核心开发生命周期的新方法阶段；
- 无法在不形成第二 Authority 的情况下定义 Consumer-local 发现模型；
- Consumer-local 独立运行与现有 baseline adoption 契约发生实质冲突；
- 需要人工决定新的重大、难逆运行时基础设施方向。

普通文档组织、命名、可逆 schema 候选和分析细节由当前工作继续收敛，不制造人工确认门槛。

## 完成条件

A1 完成时应能用一个明确模型回答：

```text
Fresh Consumer Task
→ Consumer-local Bootstrap / Repository Authority
→ Consumer-local Discovery
→ Applicable Rule / Responsibility Routing
→ 按需 Skill / Current Authority
→ Execute / Verify / Stage Return
```

并明确：

- upstream 在 ordinary runtime 路径中不出现；
- Consumer-specific rule 可以覆盖更通用 adopted default；
- adopted upstream capability 的来源关系仍可追溯；
- 发现层不成为第二套 Authority；
- stale / missing / ambiguous discovery 可 fail-closed 到 Consumer Repository Authority。

满足后将 A1 结果回写到长期项目级 Authority，并进入 A2；否则保持 A1 当前状态继续收敛。

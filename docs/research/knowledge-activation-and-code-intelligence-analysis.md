---
id: research:knowledge-activation-code-intelligence
type: research
status: active
distribution: source-only
---

# 知识激活、规则治理与使用方代码智能研究

**研究日期：** 2026-09-08  
**性质：** 非规范性 Research

## 1. 核心问题

随着仓库规则增多，主要风险会从“缺少规则”转向：

- 当前任务找不到真正相关规则；
- 相似 / 冲突规则一起进入上下文；
- 活动规则过多导致信噪比下降；
- 陈旧或重复知识误导当前执行；
- 把激活失败误判成规则缺口，继续堆叠同义规则。

因此知识存储与执行时知识发现必须分离。治理单位应是**可独立触发的最小规则语义单元**，而不是文件大小本身。

## 2. 渐进披露研究结论

更合理的活动上下文分层为：

1. 少量稳定 Repository / Method 不变量；
2. 当前职责真正需要的 Skill；
3. 根据 task / technology / artifact / risk 条件按需加载的 Rules。

上下文容量变大不意味着“把所有规则都给模型”更可靠。目标应是最小正确活动指令面。

V4 已把这一研究方向落实为：

```text
current task / repo facts
→ small task signals
→ deterministic pre-LLM Rule Discovery
→ small locator set
→ LLM reads candidate bodies
→ final semantic applicability
```

## 3. 先修激活，再增规则

出现失效时先区分：

1. 规则未进入当前上下文；
2. 冲突 / 相似规则选择失败；
3. 上下文规则过多；
4. 陈旧知识进入上下文；
5. 真正没有规则覆盖。

只有第 5 类天然指向新增 Rule。前四类优先修发现、metadata、owner、currentness 或上下文组装。

## 4. Obsidian 边界

Obsidian 的 backlinks、graph、properties、bases 等适合人类知识治理、浏览与可视化，但默认 note-link graph 不能天然表达精确 runtime applicability。

因此：

- Obsidian 不应成为 Repository Authority；
- Git 继续保存规范 Markdown 与 current facts；
- Obsidian 最多是投影视图 / 工作台；
- 使用 Obsidian 不能替代独立的 Agent Rule Discovery。

## 5. CodeGraph 的可借鉴部分

对 `colbymchenry/codegraph` 的研究提供了以下通用设计启发：

- **预处理稳定结构**：不要要求每个新上下文重新从全部长文档推导；
- **精确结构化查询**：发现机制应返回当前任务需要的最小上下文；
- **单一强入口**：避免暴露大量窄工具增加工具选择成本；
- **常驻指令保持很小**：把细节延迟到真正需要时加载；
- **派生状态可重建并处理陈旧性**：索引不是权威；
- **检索本身必须评估**：返回过少是漏检，过多是噪声，进程成功不等于语义成功。

CodeGraph 的 AST 关系大多可确定性推导，而 Rule applicability 带治理语义，不能照搬成自动推理图。V4 因此选择显式 Rule Front Matter + 确定性 Tool 初筛，而不是 LLM 自动建立权威知识图谱。

## 6. V4 与早期研究方案的差异

早期研究曾考虑更丰富的关系元数据和派生知识索引。V4 进一步减法收敛：

- Rule metadata 与正文同文件；
- 只保留能回答“是否值得加载”的五个 scope dimensions；
- 不维护 Reviewed Discovery Map / Manifest / Catalog / rule-index；
- Tool 可以扫描 N 个 Front Matter，但普通 LLM context 只接收 k 个 locator；
- 可选实现缓存必须可删除、可确定性重建、非 Authority。

因此本文中的旧 schema / map / index 示例只属于研究演进历史，不是 current contract。当前 contract 以 `docs/architecture/rule-discovery-architecture.md` 为准。

## 7. Consumer 代码智能边界

Consumer 同时有两类发现问题：

```text
Repository Authority / Rules
→ 应该怎样工作？

Source / dependency / runtime structure
→ 代码现在怎样工作？
```

`agentic-dev` 负责前者的方法与 Rule Discovery，不应为了后者自行重造代码知识图谱。成熟代码智能工具可以作为 Consumer-local 可选能力，但其本地索引仍是派生上下文，不是项目事实。

CodeGraph 可能对 `execute-unit`、`systematic-debug`、`review-change` 的源码发现有价值；是否采用应通过真实 Consumer A/B 验证，而不是根据外部项目宣称直接推导收益。

## 8. 技术知识方向

研究支持把长期技术知识从“大型生成教程”转向更具辨识力的：

- 当前版本必须重新确认的事实；
- 模型容易犯错的技术不变量；
- 必须额外验证的风险；
- type/build/runtime/visual 等证据边界。

V4 的 technology Rules 正是这种最小化、按条件发现的落点。

## 9. 代码复核边界

本研究发现独立代码复核具有稳定输入、过程、输出和退出条件，但不应成为新的 Method 阶段或超级技能。V4-03 已据此形成 `review-change` supporting Skill；其横切触发与约束仍由独立 Rules 持有。

## 10. 明确非结论

本研究不支持：

- 按文档 KB 数机械拆分；
- 必须采用 Obsidian；
- 必须建立图数据库 / MCP rule server；
- CodeGraph 成为所有 Consumer 必需依赖；
- 代码智能替代编译器、测试、Runtime Evidence 或 Review；
- 技术重要就建立大型 Technology Profile；
- Review 成为新的核心方法阶段。

## 11. 主要来源

- `colbymchenry/codegraph` 仓库及其 introduction / knowledge graph / MCP server / installer 资料；
- Obsidian 官方 Graph / Backlinks / Properties / Bases 文档；
- OpenAI 当时模型提示指导；
- 本仓当时的 Repository / Consumer evidence。

外部来源只作为研究证据；任何长期行为必须由当前 Method / Architecture / Rule / Skill owner 明确持有。
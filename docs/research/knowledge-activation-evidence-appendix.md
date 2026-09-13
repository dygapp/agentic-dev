---
id: research:knowledge-activation-evidence
type: research
status: active
---

# 知识激活关键证据附录

**研究日期：** 2026-09-08  
**性质：** 非规范性长期技术证据

本文件伴随 `knowledge-activation-and-code-intelligence-analysis.md`，保留支持“薄入口、按需激活、可重建派生状态、fail-closed 与检索专项评估”的具体证据。它不是 Fresh Context 入口或当前 Rule Discovery contract。

## 1. 历史大指南体量证据

2026-09-08 的仓库基线中，`docs/guides/` 四个文件合计约 76.9 KB，其中 `using-agentic-dev.md` 与 `external-operation-guidelines.md` 合计约 55.9 KB，约占 73%。

该数字只说明当时多个可独立触发职责集中在少数文件，**不构成按 KB 拆文档的规则**。V4 已把运行时约束拆为 Rule 单元，Guide 不再承担 ordinary runtime 规则 owner。

## 2. PR #72：规则存在不等于可靠激活

历史 PR #72 的证据显示：与项目路线图 / 集成状态有关的边界已经存在，但没有稳定进入高影响复核路径，仍产生了错误的尾部状态处理。

支持的最小结论：

> 长期规则已经写入仓库，不等于它会在需要它的任务中自动被发现和激活。

因此失效分析必须先区分规则缺口与 discovery / activation failure。

## 3. CodeGraph 激活提示实测

CodeGraph 源码记录的 Agent 行为测试中：

- 无短激活块时，子代理大约只有 1 / 9 次主动加载并使用 CodeGraph；
- 加入极短 marker-fenced 激活块后，子代理能稳定使用 CodeGraph，并出现零 `Read` / `grep` 回退的运行。

该证据不证明 `agentic-dev` 应复制同一实现，但支持：**一个小而精准的发现入口可能比常驻完整使用手册更可靠。**

## 4. 单一强入口与紧凑常驻指令

CodeGraph 虽有多个底层查询能力，MCP 默认只暴露 `codegraph_explore`。其实现还明确要求 server / installer instructions 保持紧凑，避免每个会话重复消耗长常驻说明。

这支持 V4 的方向：

- Rule Discovery 只有一个确定性发现入口；
- 细节保留在 Rule body；
- 普通 LLM context 不接收 N 条 metadata。

## 5. 外部 A/B 数值只作为参考

CodeGraph 当时公开的第一方 A/B 包括约：

- 58% fewer tool calls；
- 22% faster；
- 另一轮 README 测量报告约 44% lower cost / 62% fewer tokens on average。

这些数字不能外推为 `agentic-dev` 或任意 Consumer 的收益。可吸收的是评估方法：同模型、同任务、有界 A/B，并把最终正确性、漏检和噪声放在工具调用/令牌数量之前。

## 6. 派生索引不是 Authority

CodeGraph 的 `.codegraph/` 是本地、可更新、默认 gitignored 的派生 SQLite 索引；陈旧时应回到源码事实，而不是把旧索引当权威。

V4 对实现缓存采用更严格边界：

- 可删除；
- 可从 Rule Front Matter 确定性重建；
- 不人工维护；
- 不进入普通 prompt；
- 不拥有 Rule 语义。

V4 当前并不要求一定实现缓存。

## 7. Code intelligence 与 Rule Discovery 分工

CodeGraph 的主要 Consumer 交付是本地索引 + MCP / CLI + 极薄提示，不是复制其内部开发 Skills。它可以帮助源码结构发现，但不能替代：

- Repository / Product Authority；
- compiler / type-check；
- unit / integration / E2E tests；
- runtime validation；
- review 本身。

因此 V4 不把代码智能并入 Rule Discovery，也不强制 Consumer 采用 CodeGraph。

## 8. 当前解释边界

本附录中涉及旧 Guide、旧 Skill 数量、旧 Candidate 或旧 discovery design 的描述仅是当时证据背景。V4 当前规范分别由：

- `docs/architecture/rule-discovery-architecture.md`；
- `docs/architecture/skill-architecture.md`；
- `docs/rules/**`；
- 具体 `SKILL.md`

持有。
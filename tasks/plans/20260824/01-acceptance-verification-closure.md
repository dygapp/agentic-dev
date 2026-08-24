# 验收到验证的闭环定向强化

## 目标

基于 Issue #18 最后两条 Consumer 项目证据，补齐从规格验收义务到执行单元责任归属、计划证据与已执行的当前证据的生命周期闭环。

## 权威来源与输入

- `AGENTS.md`
- `docs/method/ai-development-method.md`
- `docs/architecture/skill-architecture.md`
- `docs/architecture/skill-contracts.md`
- Issue #18 证据：
  - `issuecomment-5389958865`
  - `issuecomment-5390031369`
- Consumer PR `dygapp/jilinjobs-cms#11`、PR `#12` 与关联 CI 证据

## 范围

1. 先更新方法 / 决策 / 架构中的验收到验证的闭环语义。
2. 对齐 `slice-work`、`readiness-check`、`execute-unit` 契约与 Skill 实现。
3. 保持 `converge` 的独立功能整体的安全网职责。
4. 更新使用指南、状态说明与最小针对性行为评估。
5. 基于最终 PR 状态完成验证与 AI 复核，并回写 Issue #18。

## 非目标

- 不重新处理 EU-06。
- 不修改 Consumer 产品实现。
- 不新增核心 Skill 或独立 `verify-evidence` Skill。
- 不强制一条验收义务对应一个测试。
- 不把 GitHub Actions、Playwright 或 E2E 提升为通用方法要求。
- 不自动执行合并。

## 完成标准

- 方法、架构、契约、Skill 与指南对同一闭环语义保持一致。
- 执行单元级与显式功能整体验证责任均有合法表达。
- 缺少计划验证覆盖时就绪检查不得 `PASS`。
- 执行单元负责的验收义务缺少已执行的当前证据时不得声明执行单元 `Completed`。
- `converge` 继续独立重新检查功能整体规格到证据的覆盖。
- 针对性评估定义通过结构验证，并完成与风险相称的全新运行时验证或明确记录不可执行原因。
- 最终 AI 复核不存在未解决阻塞性 / 中等级别发现。


## 当前状态

- PR 草稿：`dygapp/agentic-dev#30`
- 语义基线：`dc8e9f451155018a581c7c1a2739075e10650f74`
- 方法 / 原则 / 架构 / 契约 / Skills / 使用指南：已对齐
- Eval JSON 结构 / Runner 脚本的 Python 语法 / 场景注册：PASS
- 最终 AI 复核：阻塞性发现 0 / 中等级别发现 0 / `PASS`
- 全新运行时行为证据：PENDING
- 阻塞项：当前运行环境没有 `codex` 可执行文件
- 集成：未执行；PR 保持草稿状态

## 恢复步骤

在具备 Codex CLI、并符合 `evals/README.md` 隔离规则的环境中运行：

```bash
python3 evals/run_codex_evals.py --behavior \
  --scenario B-SW-01 \
  --scenario B-RC-05 \
  --scenario B-EU-06 \
  --scenario B-CG-06
```

然后：

1. 对四个场景逐项执行人工语义分级，不能把进程退出码当作 PASS；
2. 如果出现 Skill / 契约 / 方法发现，按权威层级修正并针对性重跑；
3. 全部 PASS 后更新 `evals/README.md`、仓库 / Skill 状态与 PR 证据；
4. 重新读取最终 PR 状态并执行受影响维度 AI 复核；
5. 只有验证与复核均闭环后，才将 PR 从草稿转为可供人工复核；合并仍由人工决定。

# 验收到验证的闭环定向强化

## 目标

基于 Issue #18 最后两条 Consumer 项目证据，补齐从规格验收义务到执行单元责任归属、计划验证证据与已执行的当前证据的生命周期闭环。

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

- PR：`dygapp/agentic-dev#30`
- 语义与评估基线：`5a894d28bddc4b427af0d3822ae3e2541e730512`
- 方法 / 原则 / 架构 / 契约 / Skills / 使用指南：已对齐
- Eval JSON 结构 / Runner 脚本的 Python 语法 / 场景注册：PASS
- 全新运行时行为评估：`4 / 4 PASS`
- 断言：`21 / 21 PASS`
- 最终 AI 复核：阻塞性发现 0 / 中等级别发现 0 / `PASS`
- 阻塞项：无
- 集成：未执行；PR 达到 `Ready to Integrate`，合并仍由人工决定

## 完成结果

1. `slice-work` 为规格验收义务建立实现责任、验证责任和计划验证证据；
2. `readiness-check` 在验收责任未归属或计划验证覆盖不足时阻止 `PASS`；
3. `execute-unit` 在缺少已执行的当前证据时不声明执行单元 `Completed`；
4. `converge` 继续独立检查功能整体覆盖，并将未执行的验证判为 `GAPS`；
5. 本次定向强化没有新增核心 Skill，没有绑定固定测试框架，也没有弱化人工集成边界。

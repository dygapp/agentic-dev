---
name: execute-unit
description: Implements and verifies exactly one ready execution unit in minimal fresh context using current repository evidence. Use when a single unit is ready to execute; discover repository-specific verification, route unexpected failures through systematic-debug, and stop after evidence supports or fails the unit completion condition.
---

# execute-unit

## 目的

在 Fresh Context 中只实现一个 Ready Execution Unit，并取得与该 Unit Completion Conditions 匹配的当前验证证据。

## 输入

- One Ready Execution Unit；
- Unit 中已有 Authority 恢复线索，以及按当前 task / claim 与 Consumer locator 重新解析的直接 Current Authority；
- 当前代码与测试状态；
- Consumer-local constraints。

## 流程

1. 重新读取 Unit、Consumer-local constraints 与当前仓库事实；结合 Unit 线索、当前 task / claim 和 Consumer locator / navigation 重新解析当前责任实际适用的直接 Current Authority，确认没有使 readiness 失效的 owner / locator / semantic drift。Unit 未列出某个 owner 不能成为忽略当前适用 Authority 的理由。
2. 形成临时 JIT Execution Plan，只包含本 Unit 的精确施工与验证步骤；最终差异中的每个有意义变化都必须能追溯到当前 Unit、验证责任或必要清理。
3. 按当前仓库既有模式实施最低必要复杂度，不顺带处理其他 Unit。集合型数据访问必须匹配真实消费边界；不得默认全量读取持续增长集合，也不得用固定小上限静默截断正确结果。
4. 当前 Unit 涉及 legacy / historical / business data migration 时，明确 source role、semantic preservation、identity / duplicate、replay / idempotency、exception / conflict disposition 与 provenance；legacy source 不反向成为新的 Requirement Authority。数据库 schema / initialization migration 仍按数据库迁移责任单独验证。
5. 从外部站点、接口、附件或其他仓库取得二进制 / 媒体资源时，在版本化或交给运行时消费前验证真实内容签名 / 类型和必要可解析属性；转换后重新验证，不用改扩展名掩盖格式错误。
6. 对预期 TDD 失败按计划推进；意外失败进入 `systematic-debug`，不得猜测绕过。验证失败先区分 implementation defect、stale verification contract、runtime / environment 与 external dependency，不因旧测试存在就让实现迎合失效断言。
7. 运行与 Completion Conditions、当前适用 Authority 和本 Unit claim 对应的当前验证。任何质量属性只要由适用 Authority 或当前 claim 提出可验证义务，就必须选择能区分该义务是否成立的 Evidence。涉及数据库 schema / migration lifecycle 且环境允许取得完整初始化证据时，至少覆盖一次 `Fresh Database → Full Migration Chain → Application Startup`；无法取得时明确保留 Evidence gap。
8. 当前适用 Authority 或本 Unit claim 要求视觉复刻、设计稿还原或其他 visual fidelity 时，功能 / 路由测试不能单独证明视觉通过；按当前风险取得真实页面、参考视觉、AI 对照和必要人工复核。Requirement 只是可能的义务来源之一。
9. 每个测试、构建、工具调用、修复或异步步骤进入终态后重新计算本 Unit 的剩余责任；只要仍可在当前授权内自动关闭就继续，直到全部 Completion Conditions 有匹配的当前证据或出现真实 blocker。
10. 停在 Unit 完成边界，不自动合并、发布、部署或启动下一 Unit。

## 输出

- Unit implementation；
- Current verification evidence；
- Completion result / blocker。

## 退出条件

当前证据支持全部 Unit Completion Conditions，或已准确识别无法在本 Unit 内关闭的 blocker。

## 升级

适用 Current Authority 缺口、无法可靠判断且影响当前 claim 的 Authority applicability / locator、未授权长期语义改变、不可逆外部操作或权限阻塞按责任层升级。请求人工前先检查当前已授权工具、Repository / CI / 日志 /文件中的可恢复 Evidence 与等价自动路径；只有不可替代的人类决定、权限或环境事实才升级，并把请求缩到最小必要动作。

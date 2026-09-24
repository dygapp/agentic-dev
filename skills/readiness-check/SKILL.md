---
name: readiness-check
description: Performs a read-only pre-execution gate across an execution unit, its currently applicable consumer authority, optional technical plan, artifact lifecycle responsibilities, and governance. Use immediately before execution to return PASS or evidence-backed findings; never repair authoritative artifacts inside the check.
---

# readiness-check

## 目的

在 Execute 前做只读门禁，判断目标 Execution Unit 是否具备清晰 Authority、边界、依赖、验证责任与当前可执行性。

## 输入

- Target Execution Unit；
- Current Specification / optional Technical Plan；
- Unit 中已有 Authority 恢复线索，以及按当前 task / claim 与 Consumer locator 重新解析的适用 Current Authority；
- Repository Authority；
- 当前仓库事实；
- Consumer-local constraints。

## 流程

1. 重新读取当前 Unit、Consumer-local constraints 与当前仓库事实；结合 Unit 线索、当前 task / claim 和 Consumer locator / navigation 重新判断当前责任实际适用的 Current Authority，不把切分时的 owner 清单或旧会话就绪结论当成永久事实。
2. 检查 Specification readiness、必要技术决定、Unit scope、依赖、artifact lifecycle、权限和 completion / verification 定义；验证 contract 必须覆盖当前责任实际适用的 Current Authority 及其可验证义务，旧测试或 Workflow 不能因为已存在就覆盖 Current Authority。
3. 检查 base drift、未提交 / 并发变化、当前 exact subject 与 Repository 状态是否使既有计划或旧 Evidence 失效。
4. 逐项完成当前门禁检查后重新计算剩余责任；单个检查、测试或工具调用完成不等于 readiness gate 完成。
5. 只报告 evidence-backed finding，并给出明确 Return To：Specification / Acceptance 的 WHAT/WHY 缺口返回 `specify`；只有底层 Product Intent 本身仍未决定时才先返回 `clarify-intent`。Execution Unit 的 scope、completion condition、traceability 或 dependency 形状问题返回 `slice-work`；跨 Unit 的持久 HOW 缺口返回 `technical-plan`；系统性长期 Architecture driver 返回 `clarify-architecture`；其他 Current Authority 缺口返回其真实 owner / Consumer-local maintenance procedure。applicability / owner / locator 无法可靠判断且会影响当前 readiness claim 时，只阻断受影响结论。本 Skill 内不修复 Authority、计划、代码或配置，也不把无法验证的假设降级为 PASS。

## 输出

- `PASS`；或
- Findings：事实、影响、责任层与最小返回路径。

## 退出条件

只有不存在阻塞执行的已知 finding 时返回 PASS；否则准确返回负责修复的上游层。

## 升级

Authority 冲突、产品 / 架构高影响决定或权限问题需要人工时升级。发出请求前先检查当前 Repository、Evidence 与已授权自动路径是否可以关闭问题；只把不可替代决定或权限缩成最小人工请求。PASS 不自动授予 merge / release / deploy 权限。

---
name: systematic-debug
description: Investigates an observed defect or unexpected failure through reproduction, authority-backed expected-versus-actual analysis, falsifiable root-cause hypotheses, minimal fix, and regression evidence. Use for unexpected failures or standalone defect work; not for expected initial TDD failures or undefined product behavior.
---

# systematic-debug

## 目的

对已观察到的 defect / unexpected failure 建立可证伪根因，再做最小修复和回归验证；不把猜测当根因。

## 输入

- Observable failure / defect；
- Expected behavior Authority；
- Relevant code / runtime state；
- Consumer-local constraints。

## 流程

1. 在当前 exact subject 上稳定复现问题，记录 actual behavior、最小触发条件、Consumer-local constraints 与相关 runtime / environment facts；无法复现时不猜测根因。
2. 结合当前 defect / failure claim、Consumer locator / navigation 与 Repository facts，重新判断并读取实际适用的 Current Authority，从中确认 expected behavior；Requirement / Specification / Architecture 只是常见来源，不构成封闭列表。若 expected behavior 未被任何可靠 Current owner 定义，返回真实责任层（产品行为缺口可返回 `clarify-intent` / `specify`），不得自行定义。测试或 Workflow 与 Current Authority 冲突时先判断 stale verification contract，而不是修改产品迎合旧断言。
3. 区分 implementation defect、stale verification contract、runtime / environment problem 与 external dependency problem，收集能区分原因的 Evidence，形成有限、可证伪的 root-cause hypotheses。
4. 逐一验证假设，直到 Evidence 支持根因；不得同时做多项无关“可能修复”，也不通过大规模重构掩盖尚未确认的原因。
5. 实施针对根因的最低必要修复，最终差异只包含当前 defect、验证责任和由修复直接产生的必要清理。
6. 运行与 claim 匹配的当前回归与必要邻接验证，确认原 failure 消失且没有已知相关回归；如果修复改变 commit / runtime subject，旧 Evidence 不自动支持新 subject。
7. 每次复现、假设验证、修复、测试、异步观察失败或超时后重新计算剩余诊断责任；只要仍有当前授权内可自动执行的区分性检查就继续，不因单个步骤终态提前停止。

## 输出

- Reproduction / expected-vs-actual；
- Evidence-backed root cause；
- Minimal fix；
- Regression evidence / unresolved blocker。

## 退出条件

根因有证据支持，修复与根因一致，当前回归证据支持预期行为；或已明确应返回上游 Authority。

## 升级

预期行为冲突、需要改变产品意图 / 重大架构、不可逆数据风险或权限不足时升级。请求人工前先检查当前 Repository、日志、测试、connector / API 与其他可恢复 Evidence 是否足以关闭问题；只升级不可替代的决定、权限或环境事实。

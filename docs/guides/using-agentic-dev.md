---
id: guide:using-agentic-dev
type: guide
status: active
---

# 使用 agentic-dev

本指南只面向人类说明初始化、首次采用和显式升级，不参与普通 Rule Discovery。

## 新 Consumer

1. 先建立 Consumer 自己的 `AGENTS.md` / Repository Authority；
2. 读取 `docs/architecture/consumer-lifecycle.md`；
3. 只选择当前项目真正需要的 Method、Skills、Rules；
4. 将接受能力本地化，不把 `agentic-dev` 项目状态带入 Consumer；
5. 接入 Consumer-local Rule Discovery Tool；
6. 验证普通工作只依赖 Consumer-local current state。

## Fresh Context

提示词保持简洁：声明 Fresh Context、目标仓库、必要的前置动作和特殊约束即可。Repository Authority、开发方法、当前路线和运行规则从仓库读取。

## 升级

已有 Consumer 只有在显式 baseline upgrade 时重新读取 upstream。先恢复 Consumer 当前事实，再比较候选 upstream baseline，逐项采用 / 保留 / 拒绝 / 取代，并重新执行受影响验证。

## 不要做的事

- 不把上游 README / Roadmap 当 Consumer 项目事实；
- 不把所有 Rules 或 metadata 塞进 prompt；
- 不维护 Consumer 版中心 Rule Map；
- 不因 upstream 更新自动覆盖 Consumer-local adaptation。
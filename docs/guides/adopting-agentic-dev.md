---
id: guide:adopting-agentic-dev
type: guide
status: active
distribution: source-only
---

# 首次安装 agentic-dev Release

本文是 `method:consumer-adoption` 的人类说明，不替代正式 Method。

## 什么时候使用

当一个普通软件项目第一次决定安装 `agentic-dev` 发布的 Software Development Agent Skills Release 时使用。普通开发任务不需要重新执行安装。

## 核心边界

Consumer 安装的是**版本化 Release**，不是 `agentic-dev` Source Repository。

先从 Consumer 自己出发，确认：

- 根 `AGENTS.md` / Repository Authority；
- 产品、Requirement、System Architecture 与项目文档；
- 已有 Agent Skills / local policy；
- Runtime 与权限边界。

然后选择一个精确 Release，核对 version、source SHA provenance、integrity、included Skills、compatibility 与 migration information。

## 默认安装形态

首版 repository-local 目标以：

```text
AGENTS.md              # Consumer-owned
.agents/
  README.md
  skills/
    <skill>/
```

为核心。

安装只允许对根 `AGENTS.md` 做有界、可重复的 Skill / compatibility locator 集成，不整文件覆盖 Consumer Authority。

Consumer 的业务 / 项目 `docs/**` 继续保存自己的 Requirement、Architecture、Technical、Project Knowledge；不会因为安装 Agent Skills 就镜像 upstream 的 Method / Architecture / Rule 目录。

## 验证重点

完成后至少确认：

- Skill 已按 Release 完整安装；
- Consumer-owned Authority 未被覆盖；
- Runtime 能发现 / 使用对应 Skill；
- 脚本或外部执行依赖具有 direct / alternate path；
- ordinary runtime `upstream access = 0`；
- Fresh Runtime 不需要读取 upstream Source Repository。

正式 Gate 与完成条件见 `docs/methods/consumer-adoption.md`；长期 Consumer ownership 见 `docs/architecture/consumer-architecture.md`。

---
id: repository:readme
type: repository
status: active
---

# agentic-dev

`agentic-dev` 是一个面向 AI Agent 驱动软件开发的方法、可组合 Skill、分布式 Rule 与 Consumer adoption 能力仓库。

## 当前 Foundation

V4 采用减法优先的 Foundation Rebuild：

- Skill 只保留稳定独立执行闭环；
- Rule 以最小 Markdown 单元存在，发现 metadata 与正文同文件维护；
- Rule Discovery Tool 只扫描 YAML Front Matter，向 LLM 返回少量 `{id, path}` locator；
- Guide 只承担面向人的初始化、采用、升级和低频说明；
- `docs/project/` 只保留真正 Current Project State；
- V1～V3 过程历史由 Git / Issue / PR 保存，不在 current tree 建兼容层。

当前路线与 Gate：`docs/project/project-roadmap.md`。

## Fresh Context

本仓库工作从 `AGENTS.md` 恢复稳定 Repository Authority，再读取 `README.md`、Project Roadmap 与 GitHub 当前事实。普通任务只提取少量 task signals，通过本地 Rule Discovery 加载候选 Rules；不得加载全量 Rule metadata / body。

## Consumer

Consumer 拥有自己的 Repository Authority。首次 adoption / 显式 baseline upgrade 可重新进入 `agentic-dev`；采用完成后的 ordinary runtime 默认只使用 Consumer-local Method / Skills / Rules / Discovery Tool，不在线依赖 upstream。

人类使用说明：`docs/guides/using-agentic-dev.md`。

## 当前结构

```text
AGENTS.md
README.md
skills/
docs/
  method/
  architecture/
  rules/
  guides/
  project/
  research/
evals/
tools/        # V4-04 建立 Rule Discovery Tool
```

真正的运行时规则由 `docs/rules/**` 持有；目录分类只服务人类阅读，不参与匹配。
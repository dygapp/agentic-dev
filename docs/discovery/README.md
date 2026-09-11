# 本地资源发现入口

**状态：** 基线 v0.1  
**跟踪：** Issue #113

本文是 `agentic-dev` 自身普通运行的 **Local Discovery Entry**。它只提供稳定入口与失败关闭路径，不复制 Method、Skill、Policy、Project Authority 或完整职责路由表。

## 1. Fresh Context 起点

先读取：

1. 根 `AGENTS.md` — 稳定 Repository Governance / Authority Boundary；
2. 根 `README.md` — 简短当前状态；
3. `docs/project/project-roadmap.md` — 当前阶段、活动工作与下一 Gate；
4. GitHub 当前 `master` / Open Issue / PR / 必要 Actions — 精确外部状态。

如果当前目标只需要恢复项目状态、确认当前 Gate 或回答当前仓库事实，到这里即可；不要为了“发现完整”继续加载全部 reusable capability。

## 2. 需要跨资源发现时

只有当前任务需要判断职责、条件性规则或按需能力时，读取：

`docs/discovery/reviewed-discovery-map.md`

该 Map 只保存经过复核的跨资源发现映射与 source binding。真实规则正文仍从 Map 指向的 current semantic owner 读取。

## 3. routing-only

如果当前目标只需要：

- 判断下一职责；
- 判断是否发生 Stage Return；
- 判断旧 discovery decision 是否仍可继续；
- 给出需要继续读取的本地 source；

则：

```text
Current Repository Authority
+ Current Work facts
+ Reviewed Discovery Map（仅在需要时）
→ primary responsibility
+ minimal supporting sources
→ stop
```

不得仅因为 Map 找到某个 Skill locator 就加载完整 `SKILL.md`。

## 4. 真正执行职责

只有当前任务明确继续执行某个稳定主职责时：

1. 确认对应 Skill / semantic owner 在当前仓库中仍 current；
2. 加载当前主职责需要的完整 `SKILL.md` 或规范正文；
3. 加载当前事实真实触发的最小 supporting context；
4. 按原 Method / Skill Contract / Policy 执行；
5. 发生 Stage Return 时丢弃旧 discovery decision 并重新从本入口判断。

本入口不定义 Method Stage、Readiness 或 Stage Return 的具体语义。

## 5. 失败关闭

以下任一情况出现时，停止信任当前 Map / 派生判断：

- coverage anchor 变化且尚未重新复核；
- source / selector 不存在；
- Map 的 semantic-reviewed binding 与当前 source 不一致；
- 当前真实 owner / supersede / disable 关系不明确；
- no-match 但当前任务明显仍包含治理 / 验证 / 风险事实；
- 多个主职责无法可靠区分；
- 高影响授权、重大架构、安全 / 隐私或不可逆边界不明确。

回退到：

```text
AGENTS.md
→ README.md / project-roadmap.md
→ 当前真实 semantic owner / Repository Authority
→ 按问题扩大最小本地读取
```

普通运行失败关闭**不自动访问 upstream**，也不使用历史聊天、个人记忆或旧索引填补未知事实。

## 6. 当前机制

`agentic-dev` 当前 self-runtime discovery 只使用：

```text
Local Discovery Entry
+ Reviewed Discovery Map
```

当前不建立：

- Activation Manifest；
- Runtime Catalog / Runtime View；
- generator；
- Rule Super Skill；
- Stage Router；
- Runtime Controller。

这些对象只有未来出现新的当前证据和独立门禁时才能重新评估。
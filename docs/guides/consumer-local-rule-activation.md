# Consumer-local 规则发现与激活

本文说明已经采用 `agentic-dev` 能力的 Consumer，如何把已采用能力投射为**只依赖自身 Repository 的 ordinary runtime**。

本文是使用指南，不重新定义长期规范。发生冲突时，按以下 owner 读取：

- 初始化、首次采用、基线升级、采用验证、普通运行与重新进入上游：`docs/architecture/consumer-lifecycle.md`；
- 长期资源身份、资源固有结构与派生发现边界：`docs/architecture/agent-resource-model.md`；
- Local Discovery Entry、Reviewed Discovery Map、可选 Runtime View、routing-only / execute、Stage Return、fail-closed：`docs/architecture/resource-discovery-architecture.md`；
- Method / Skill 行为：当前 Method / Skill Contract / `SKILL.md`；
- Consumer 项目事实：Consumer 自己的 Repository Authority。

本文只解释如何在 Consumer 中落地这些规范。

## 1. 目标状态

完成采用后的普通路径应是：

```text
Fresh Consumer Task
→ Consumer-local Bootstrap
→ Local Discovery Entry
→ current Consumer resources
→ 可选 Reviewed Discovery Map
→ 一个主职责 + 最小辅助上下文
→ routing-only 或按需 Skill
→ Execute / Verify / Stage Return
```

普通路径默认不访问 `agentic-dev` upstream。

## 2. Bootstrap 保持薄

Consumer Bootstrap 只需要稳定回答：

- 当前 Repository Authority 在哪里；
- 当前项目状态 / Roadmap 从哪里恢复；
- Local Discovery Entry 在哪里；
- Consumer Repository Authority 优先；
- ordinary runtime 默认不访问 upstream。

不要把当前里程碑、Issue / PR / Run、历史 baseline upgrade、全部 Skill 正文、完整上游文档树或临时实验结果持续堆入最高优先级 Bootstrap。

文件名由 Consumer 自己决定；`AGENTS.md` 只是常见实现，不是上游强制格式。

## 3. 先投射真实本地资源

采用完成后，需要持续影响普通运行的能力必须成为 Consumer-local current resource，例如：

- Consumer 自身 Requirement / Specification / Architecture / ADR / Verification / Integration Authority；
- 已采用的 Skill；
- 已采用的 Engineering Discipline；
- 已采用的 Technology / Verification Profile；
- Consumer 本地规则 / Policy；
- 必要的 provenance / supersede / override 关系。

优先复用 Consumer 已有 semantic owner，不为每个上游变化机械新建文件。

不要把 `agentic-dev/docs/project/*`、上游 Roadmap、Issue / PR 状态、Research / Eval 流水或完整上游文档树投射为 Consumer ordinary-runtime Authority。

## 4. Manifest / Map / Runtime View 都不是必选

V3 不再要求固定 Activation Manifest + Runtime Catalog 两层。

Consumer 应按实际复杂度选择：

### 4.1 不需要持久化 Map

如果固定 Authority Entry、Skill 原生 `name / description`、Profile inventory 和少量本地规则已经足以可靠发现，可以只使用这些真实本地入口。

### 4.2 需要 Reviewed Discovery Map

如果存在持续的跨资源职责 / 条件 / 风险正规化需求，可以建立一个 current Reviewed Discovery Map。

它只保存 locator、跨资源派生提示、coverage / source binding 和加载提示，不拥有规范正文，也不建立第二 `active/current` 真值。

### 4.3 Runtime View 只是可选优化

只有 Map / current resources 的直接读取成本已经形成真实问题时，才考虑生成 compact Runtime View / Catalog。

Runtime View 必须可以从真实 current resources + current Map（如有）确定性重建，不能独立维护新的语义判断。

因此 Consumer 不因为采用 `agentic-dev` 就必须创建 Manifest、Catalog、generator、数据库、向量库、MCP 服务或 Runtime Controller。

## 5. Source currentness

### 5.1 current-locator

如果发现条目只负责定位 Current Roadmap、Requirement index、Architecture entry 等 source，而不提炼其规则语义：

- 正文正常演进不自动使 locator stale；
- path / selector / authority role 被取代时才更新；
- runtime 始终读取 current source。

### 5.2 semantic-reviewed

如果 Map 提炼了 `responsibility / conditions / risks` 等跨资源提示：

- 必须绑定已复核 source / selector identity；
- source 变化后旧提示先退出可信候选；
- 不能只刷新 hash 就恢复 current；
- 需要重新判断 source 变化是否影响派生语义。

### 5.3 coverage drift

Map 声称覆盖 Skill / Profile / Discipline inventory 时，新增、删除、重分类或无法确认 membership 的变化会使受影响范围 stale。

在重新复核前，no-match 不能被解释为“没有适用规则”。

## 6. Ordinary routing

具体发现 / 路由算法由 `resource-discovery-architecture.md` 单点定义。Consumer 落地时只需要保持：

- Consumer Authority first；
- 一次发现一个当前主职责；
- supporting context 只包含会改变正确执行 / 完成声明的最小资源；
- routing-only 不机械加载完整 Skill；
- execute 才加载当前主 Skill；
- platform-specific Skill 只有条件真实命中时按需进入；
- 未知 condition / risk 不猜测；
- 不使用固定 Top-K 或全局数值 priority 覆盖仓库权威。

本文不维护第二份职责转换表。

## 7. Stage Return 与失败关闭

Stage Return 的具体语义仍由 Method / Skill Contract / Current Authority 持有。发现层只负责：

```text
已有 owner 判定返回 / 旧执行基础失效
→ 停止当前职责
→ 丢弃旧 discovery decision 作为继续授权
→ 重新读取受影响 Consumer Current Authority
→ 重新发现
```

以下情况停止信任当前派生发现并回到本地权威：

- Map / Runtime View stale；
- coverage drift；
- source / selector missing；
- current owner / override / supersede 不明确；
- no-match 但仍存在治理 / 风险事实；
- 多个主职责无法可靠区分；
- 高影响授权、安全 / 隐私、重大架构或不可逆边界不清；
- 需要的 Skill 本地不存在或身份不明确。

ordinary runtime 的 fail-closed 不自动打开 upstream。

## 8. 基线升级与本地状态

显式 baseline upgrade 继续由 `consumer-lifecycle.md` 定义，并区分：

- 最近评估到的 upstream baseline；
- 当前本地资源实际来源；
- 只在下次升级需要的历史决策。

这些不能合成一个“当前 baseline”真值。

采用 / 升级完成后：

- adopted change 进入真实 Consumer-local owner；
- rejected / not-applicable 不进入普通 active surface；
- superseded 资源退出 current；
- ordinary runtime 回到 Consumer-local Local Discovery Entry。

## 9. Runtime Adapter 边界

Consumer 使用脚本、Plugin 或 Runtime Adapter 加速 discovery 时，可以：

- 验证 locator / source binding / coverage；
- 做确定性 candidate filtering；
- 生成纯 Runtime View；
- 暴露选定 local source / Skill；
- 返回 stale / missing / ambiguity signal。

不能：

- 发明 Method Stage、职责、conditions 或 risks；
- 覆盖 Consumer Repository Authority；
- 自动读取 upstream latest 改变 ordinary runtime；
- 缓存第二份 Requirement / Architecture / Rule 正文；
- 接管完整开发生命周期。

## 10. 采用后验收清单

以下只是从当前生命周期 / 发现架构导出的**验收清单**，不是第二规范 owner：

- Fresh Context 可以从 Consumer-local entry 恢复当前 Authority / Work；
- 至少能发现一个 Consumer-native Authority 与一个已采用 reusable capability；
- routing-only 不加载完整 Skill；
- execute 时只加载主 Skill 与真正必要的 supporting capability；
- Consumer-specific Authority 可以合法覆盖 reusable default；
- stale / missing / coverage drift / ambiguity 能 fail-closed；
- no-match 不会在 coverage 不完整时被解释为“无规则”；
- Stage Return 后重新发现；
- upstream 新提交不会在未升级时改变 ordinary runtime；
- superseded / rejected 资源不继续作为 current；
- Bootstrap 不因多轮升级持续膨胀；
- 若存在 Runtime View，删除 / 重建不会丢失规范事实或已复核语义。

行为正确后，再按项目实际需要比较 context bytes、token、文件读取、wall-clock 与维护成本。
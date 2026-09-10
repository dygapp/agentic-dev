# Consumer-local 规则发现与激活

本文说明已经采用 `agentic-dev` 能力的 Consumer，如何在**普通 Fresh Context 中只依赖自身 Repository** 发现当前适用规则、确定职责并按需加载 Skill。

本文是使用指南，不重新定义核心 Method、Principle、Skill Contract 或 Consumer 项目事实。发生冲突时，先服从 Consumer Repository Authority；对于已采用的 reusable method / architecture / contract 语义，以 Consumer 当前本地化并明确采用的对应版本为准。ordinary runtime 不因为存在 upstream 新版本就在线重读或自动覆盖本地规则；只有显式 baseline upgrade、Consumer-local 能力缺失或 Consumer Authority 明确要求时才重新进入 upstream。

Baseline adoption / upgrade 的通用选择边界仍以 `docs/guides/using-agentic-dev.md` §6.1 为准；本文重点定义**采用完成后的本地发现与激活方式**，以及 adopted assets 如何进入 ordinary runtime。

## 1. 适用目标

适用于希望满足以下目标的 Consumer：

```text
Fresh Consumer Task
→ Consumer-local Bootstrap
→ Consumer-local Discovery
→ Applicable Authority / Rule / Responsibility
→ routing-only 或按需 Skill
→ Execute / Verify / Stage Return
```

普通路径中不需要重新打开 `agentic-dev` upstream。

本文不要求所有 Consumer 建立固定目录、统一 Front Matter、数据库、MCP 服务、Rule Super Skill 或 Runtime Rule Index。

## 2. Consumer-local Bootstrap 必须保持薄

Bootstrap 只需要让新的 Agent 知道：

- 当前 Repository Authority 在哪里；
- 本地规则发现入口在哪里；
- Consumer Repository Authority 优先；
- ordinary runtime 是否允许访问 upstream；
- 当前状态应继续从哪个本地入口恢复。

不要把以下易变化内容持续堆入最高优先级 Bootstrap：

- 当前里程碑 / 阶段的详细进展；
- 历史 baseline upgrade 流水；
- Issue / PR / Run 状态；
- 全部 Skill / Guide 正文；
- 完整候选路线；
- 临时实验结果。

Consumer 可以使用 `AGENTS.md` 作为 Bootstrap，但本文不要求固定文件名。项目状态、路线和历史证据应由 Consumer 自己的 README、Roadmap、项目记录、Git / PR / Issue / Actions 或等价载体承担。

## 3. 本地发现对象

Consumer-local discovery 可以同时定位以下对象，但不会改变它们原有的 Authority 身份：

- Consumer-native Repository / Requirement / Specification / Domain / Architecture / ADR / Verification / Integration Authority；
- Consumer 已显式采用的 reusable rule / module；
- Consumer 本地可用的 Skill / Engineering Discipline / Technology / Verification Profile；
- 当前 Work / Evidence；
- 用于发现这些对象的本地 metadata / Catalog。

统一发现不等于统一优先级。Consumer 自己声明的 Repository Authority 始终决定项目事实。

## 4. Activation Manifest / Runtime Catalog

Consumer 可以维护一个很小的 **Activation Manifest**，记录普通 Runtime 需要发现的 current assets。

一个 record 只需要表达当前有辨识价值的信息，例如：

```text
id
kind
authority / rule / skill source pointer
activation role
scope
optional responsibility
optional conditions / risks
origin
current / superseded state
optional provenance / relation
```

其中：

- `activation role` 至少能区分 `bootstrap / routing / constraint / execution`；
- metadata 只负责“继续读什么”，不复制规则正文；
- rejected / not-applicable candidate 不进入 active ordinary-runtime 集合；
- superseded asset 不继续参与 Current routing；
- Consumer-specific override 保持自己的 Authority 身份，不通过数值 priority 伪造优先级。

Consumer 很小时可以直接读取 Manifest；需要更快运行时入口时，可以从 Manifest 与 current local source identities 生成可删除的 Runtime Catalog。

Catalog 删除后不得损失任何规范性事实。

## 5. Source currentness

发现信息不能因为“只是 metadata”就绕过陈旧检查。

### 5.1 语义提炼型 metadata

如果 `responsibility / conditions / risks` 是从某个规则 / Skill / Discipline 的语义提炼出来的，metadata 必须绑定已复核的 local source identity。

source 发生实质变化后：

```text
mark discovery stale
→ stop trusting old activation metadata
→ re-review current local semantic owner
→ rebuild / update discovery
```

不得只更新 hash 就自动声称旧 metadata 仍正确。

### 5.2 Current Authority locator

对于 Roadmap、Current Requirement、Architecture Map 等会正常频繁演进的 Consumer-native Authority，metadata 可以只承担稳定定位职责，而不缓存当前状态摘要。

这种 locator 只检查“当前入口仍可解析”，实际状态始终从 current source 读取，避免每次正常状态变化都产生机械 metadata 更新。

## 6. Responsibility Routing

Discovery 先形成 candidate，再根据 Consumer Current Authority 和实际 task signals 确定一个当前 **primary responsibility**。

基本规则：

1. Consumer Authority first；
2. 如果当前工作暴露 Product / Specification / Architecture / Authorization 基础缺口，拥有该缺口的职责成为新的 primary responsibility；
3. 前置基础有效时，当前明确要求执行的职责保持 primary；
4. `systematic-debug` 只处理 expected behavior 已明确下的 unexpected implementation / runtime failure；
5. Verification、Engineering Discipline、外部操作、平台专项能力等不改变职责所有权时保持 supporting context。

不要根据一个关键词平铺激活多个 Skill。

## 7. Routing-only 与 Skill Execution 分离

如果当前任务只需要判断：

- 下一职责；
- Stage Return；
- 当前 Readiness / Execute 是否仍有效；

而本地 metadata + Current Authority 已经足够，则直接返回 routing 结果，不机械加载完整 Skill。

真正进入稳定职责执行时才：

```text
resolve primary responsibility
→ load corresponding local Skill
→ read minimal Consumer Current Authority
→ apply required supporting constraints
→ execute / verify
```

额外 platform-specific Skill 只有在当前条件真实命中、且作为 primary Skill 允许的 supporting capability 时才加载。

## 8. Stage Return

Stage Return 后必须重新解析责任：

```text
stop current responsibility
→ discard old routing decision as continuation authority
→ read affected Consumer Current Authority
→ re-run local discovery / routing
```

如果 Product Intent、Specification、durable Technical Plan、Architecture / ADR 或 Execution Unit scope / acceptance ownership 发生实质变化，旧 Readiness 只对应旧语义基础，必须重新执行必要的 `slice-work` / `readiness-check`。

如果 `systematic-debug` 只修复实现缺陷且没有改变上述基础，不机械重做全部上游阶段。

## 9. Fail-closed

出现以下任一情况时，不继续依赖当前 derived discovery：

- metadata / Catalog stale；
- source missing 或 selector 无法解析；
- no-match 但当前仍存在治理 / 风险判断；
- 多个 primary candidate 无法可靠区分；
- Consumer override / supersede 关系不明确；
- high-impact / irreversible / security / privacy / authorization boundary 不清；
- 需要的 Skill 本地不存在或 identity 无法确认。

回退：

```text
stop derived discovery
→ return to Consumer-local Current Authority / Authority Map
→ expand local reads only as needed
→ re-route
→ escalate only when current Authority / permission requires it
```

ordinary runtime 的安全回退不自动访问 upstream。

## 10. Baseline adoption 后的本地状态

显式 baseline upgrade 时，Consumer 仍按 `using-agentic-dev.md` §6.1 逐项判断：

```text
adopt
retain / override
reject / not applicable
supersede / remove
```

完成后需要区分：

- **last evaluated upstream baseline**：最近比较到哪个 exact upstream commit；
- **active local asset provenance**：某个 current local asset 实际采用自哪个 upstream source / baseline；
- **upgrade-only decision history**：此前 retain / override / reject 的判断。

这三者不能混成一个“当前 baseline”声明。

特别是：Consumer 可以已经比较到较新的 upstream baseline，同时继续合法保留一个来自更早 baseline 的 local capability 或 Consumer-specific override。

升级历史和 rejected decision 默认只在下一次显式 upgrade 时读取，不进入 ordinary Fresh Context。

## 11. Local projection

需要持续约束 ordinary runtime 的 adopted change 必须成为 Consumer-local current asset，例如：

- 更新已有 Consumer-local rule owner；
- 建立小型 local reusable rule module；
- 安装 / 复制 / 暴露 current Skill 或 Profile；
- 更新 Activation Manifest / Catalog。

优先复用已有 local semantic owner，不为了 upstream 每个变化额外创建新文件。

不要把 `agentic-dev/docs/project/*`、Roadmap、Issue / PR 状态、Research / Eval 过程或完整 upstream 文档树投射为 Consumer runtime Authority。

## 12. Runtime Adapter 边界

如果 Consumer 使用脚本、Plugin、Agent Runtime Adapter 或其他工具加速 discovery，它可以：

- 验证 Manifest / Catalog；
- 检查 source identity；
- 按显式 metadata 过滤 candidates；
- 暴露选定 local source / Skill；
- 返回 stale / missing signal。

它不能：

- 私下定义新的 Method Stage；
- 在代码中维护另一套隐藏 routing 语义；
- 覆盖 Consumer Repository Authority；
- 自动拉取 upstream latest 改变 ordinary runtime；
- 缓存第二份 Requirement / Architecture / Rule 正文；
- 接管完整开发生命周期。

## 13. 采用后的验收

至少检查：

- 一个普通 Fresh Context 能从 Consumer-local entry 找到正确 primary responsibility；
- 能发现至少一个 Consumer-native Authority 与一个 adopted reusable capability；
- routing-only 不加载完整 Skill；
- execute 时按需加载 local Skill；
- Consumer-specific rule 可以覆盖 reusable default；
- stale / missing / ambiguity 能 fail-closed；
- upstream 新提交不会在未升级时改变 Consumer ordinary runtime；
- superseded / rejected rule 不继续激活；
- Catalog 可删除 / 重建；
- Bootstrap 不因多轮 baseline upgrade 和项目状态演进持续膨胀。

这些行为通过后，再比较 context bytes、token、文件读取与 wall-clock 等效率指标。
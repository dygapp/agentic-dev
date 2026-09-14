---
id: project:capability-profile
type: project
status: active
---

# Project Capability Profile

## 1. 角色

本文件记录 **`agentic-dev` 当前 Repository 如何实例化通用 Capability contract**。

它是 Repository-local Project Authority，不是可传播给 Consumer 的 capability，也不是 Rule / Skill / Method 的第二份正文。Consumer adoption / upgrade 只能把本文件作为 provenance / implementation context，并必须建立自己的 local capability profile 或等价 Authority。

当前 capability model 的已集成基础来自 PR #125 / integration commit `e5488fd22a078ab59a427e36ef9a20af935fc63f`。精确 current `master`、Open PR / Issue 与 Actions 状态仍从 GitHub 当前事实读取，不由本文件固定。

## 2. Method Selection Instance

通用 Method selection contract 由 `docs/architecture/method-architecture.md` 定义；本文件只拥有当前 Repository 的 `work kind → Method locator` 实例。

当前映射：

- 普通软件 / 产品变更从需求澄清到实现收敛 → `docs/methods/ai-development.md`（`method:ai-development`）；
- Consumer 首次显式采用 `agentic-dev` capability → `docs/methods/consumer-adoption.md`（`method:consumer-adoption`）；
- Existing Consumer 显式评估 / 升级 upstream baseline → `docs/methods/consumer-upgrade.md`（`method:consumer-upgrade`）。

如果当前工作不属于任何映射，不得为了获得流程而强行套用最接近的 Method；继续按 Repository Authority 与 direct responsibility 工作，并在真实 Evidence 支持时评估新增 Method。

本映射只保存 work kind 与 Method locator / id，不复制 Method stages、Gate、completion 或内部 Skill / Rule routing。

## 3. Rule Discovery Instance

当前 Repository 的 Rule Discovery 实例：

- Architecture contract：`docs/architecture/rule-discovery-architecture.md`；
- Rule root：`docs/rules/`；
- Tool：`tools/rule-discovery/rule_discovery.py`；
- ordinary runtime 输出：少量 `{id, path}` candidate locator；
- Rule human inventory：`docs/rules/README.md`，仅 Human View，不参与 runtime routing。

当前普通运行调用：

```bash
python3 tools/rule-discovery/rule_discovery.py --repo-root . discover --signals-json '<task-signals-json>'
```

调用时的信号 schema、三态语义、bounded-token、matching、fail-closed 与 locator-only contract 由 Rule Discovery Architecture 持有；本 profile 只拥有当前 Tool / Rule root / invocation instance。

`phases` signal 的合法 Method-specific identity 由当前选定 Method 自己定义；本 profile 不复制 phase token 列表。

本文件不维护 Rule id inventory、scope metadata、候选集或 Rule → signal 映射。

## 4. Skill Discovery Instance

当前 Repository 的 Skill root 为 `skills/`，ordinary Agent 使用 Agent Skills 原生 discovery，根据 Skill `name` / `description` 与当前责任按需加载 `SKILL.md`。

- Skill Architecture：`docs/architecture/skill-architecture.md`；
- Human inventory：`skills/README.md`。

本 profile 不复制当前 Skill 名单或数量；这些可以由当前 `SKILL.md` corpus 与 Human inventory 机械验证。

## 5. Architecture / Project Entry

Agent runtime 的稳定入口：

```text
AGENTS.md
→ Project Roadmap + Project Capability Profile + GitHub current facts
→ Method Selection contract + local selector instance（如需要）
→ current Method / direct responsibility
→ relevant Architecture / Skill / Rules
```

Project / Capability 边界：`docs/architecture/project-knowledge-architecture.md`。

顶层 capability model：`docs/architecture/engineering-capability-architecture.md`。

## 6. Human View Instance

Human entry：

- repository overview：`README.md`；
- usage guide：`docs/guides/using-agentic-dev.md`；
- Project navigation：`docs/project/README.md`；
- Architecture navigation：`docs/architecture/README.md`；
- Method navigation：`docs/methods/README.md`；
- Rule navigation：`docs/rules/README.md`；
- Skill navigation：`skills/README.md`。

这些 Human View 可以解释 current instance，但不拥有 runtime selector 或 normative body。

## 7. Current Project State Entry

当前项目阶段、当前 evolution 与下一候选由 `docs/project/project-roadmap.md` 持有稳定摘要；精确 GitHub branch / Issue / PR / Actions 状态必须实时读取。

稳定历史里程碑由 `docs/project/project-evolution.md` 摘要；完整实施 Evidence 留在 Git / Issue / PR / Actions。

## 8. Consumer Projection Boundary

Consumer 不复制本 profile 作为自己的 runtime Authority。

显式 adoption / upgrade 时：

1. 选择 exact upstream baseline；
2. 评估 Method / Architecture / Skill / Rule / Tool contract；
3. adopt / adapt / reject；
4. 在 Consumer 自己的 Project Authority 中建立 local Method selector、Rule Discovery locator、Skill entry 与 current baseline；
5. 验证 ordinary runtime `upstream access = 0`。

因此本文件是 `agentic-dev` 的 capability **instance profile**，不是跨 Repository 的 capability package。
---
id: project:capability-profile
type: project
status: active
distribution: source-only
---

# Project Capability Profile

## 1. 角色

本文件记录 **`agentic-dev` 当前 Repository 如何实例化通用 Capability contract**。

它是 Repository-local Project Authority，不是 Consumer Release，也不是 Rule / Skill / Method 的第二份正文。普通软件 Consumer 不复制本 profile；首次安装 / 升级只消费版本化 Release、兼容 / migration metadata 与 Consumer 自己的 Authority。

当前 capability model 的已集成基础来自 PR #125 / integration commit `e5488fd22a078ab59a427e36ef9a20af935fc63f`。精确 current `master`、Open PR / Issue 与 Actions 状态仍从 GitHub 当前事实读取，不由本文件固定。

## 2. Method Selection 实例

通用 Method selection contract 由 `docs/architecture/method-architecture.md` 定义；本文件只拥有当前 Repository 的 `work kind → Method locator` 实例。ordinary Bootstrap 直接消费本实例完成选择；只有 Method selection contract / scaling / no-match 语义本身进入当前责任时，才按需读取 Method Architecture。

当前映射：

- 普通软件 / 产品变更从需求澄清到实现收敛 → `docs/methods/ai-development.md`（`method:ai-development`）；
- Consumer 首次安装 `agentic-dev` 版本化 Release → `docs/methods/consumer-adoption.md`（`method:consumer-adoption`）；
- Existing Consumer 从当前 installed release 显式升级到 candidate Release → `docs/methods/consumer-upgrade.md`（`method:consumer-upgrade`）；
- Repository 已经接受 Model Collaboration semantics，需要建立 / 首次启用 local runtime instance → `docs/methods/model-collaboration-adoption.md`（`method:model-collaboration-adoption`）。

如果当前工作不属于任何映射，不得为了获得流程而强行套用最接近的 Method；继续按 Repository Authority 与 direct responsibility 工作，并在真实 Evidence 支持时评估新增 Method。

本映射只保存 work kind 与 Method locator / id，不复制 Method stages、Gate、completion 或内部 Skill / Rule routing。

## 3. Rule Discovery 实例

当前 Repository 的 Rule Discovery 实例：

- Architecture contract：`docs/architecture/rule-discovery-architecture.md`；
- Rule root：`docs/rules/`；
- Tool：`tools/rule-discovery/rule_discovery.py`；
- cloud transport：`.github/workflows/rule-discovery.yml`；
- ordinary runtime 输出：少量 `{id, path}` candidate locator；
- Rule human inventory：`docs/rules/README.md`，仅 Human View，不参与 runtime routing。

当前本地 checkout 调用：

```bash
python3 tools/rule-discovery/rule_discovery.py --repo-root . discover --signals-json '<task-signals-json>'
```

当前云端 task-level invocation 有两个 transport，二者都必须携带 exact 40-character commit SHA，并在该 SHA checkout 后调用同一 Tool：

1. GitHub Actions `workflow_dispatch`：输入 `target_sha` 与 `signals_json`；
2. 当前 Agent / connector 无 workflow dispatch 写能力时，可使用 GitHub Actions `issue_comment` bridge，在 GitHub Issue / PR 中由 `OWNER` / `MEMBER` / `COLLABORATOR` 发送：

```text
/rule-discovery <40-char-sha> <signals-json>
```

云端 invocation 将：

- checkout 请求中的 exact SHA；
- 验证实际 `HEAD` 与请求 SHA 一致；
- 执行该 SHA 自身的 `tools/rule-discovery/rule_discovery.py`；
- 将 signals、requested / actual SHA 与 discovery JSON 输出到 Actions log，并上传 `task-rule-discovery-<run-id>` artifact；
- 在 signals、SHA 或 discovery contract 无效时 fail closed。

### 3.1 Rule Discovery 传输方式选择

本仓库按当前实际可用能力选择 transport：

1. 当前 Repository Runtime 能在目标 baseline 直接执行 canonical Tool 时，优先使用本地调用；
2. 当前 Agent 不能直接执行 Tool 时，自动使用上方已声明的 GitHub Actions exact-SHA transport；当前 Agent 没有 checkout、shell 或 Python 不能成为跳过 discovery 或直接要求人工本地运行的理由；
3. transport 返回后核验 requested SHA、actual SHA、signals、locator-only result 与 workflow 终态，再把 candidate locator 交给当前 Agent；
4. 两类 declared transport 均不可用或 Evidence 无法恢复时 fail closed，不从 Guide、memory、旧 candidate set 或人工猜测补齐。

该 selection 只实例化 `agentic-dev` 当前 transport，不建立 session mode，也不改变 Rule Discovery Architecture 的平台无关 contract。

### 3.2 仓库原生确定性计算 / 验证实例

本仓库需要执行 repository scripts、lint、tests、build 或其他 deterministic verification 时，已有可用 Repository Runtime 就直接在目标 subject 上执行；当前 Agent 没有适用 Repository Runtime 时，可以使用 Repository 已声明的 GitHub Actions workflow，在 exact commit / PR Head checkout 后执行该 subject 自己的 canonical command。

GitHub Connector / API 主要承担 workflow 触发、branch / PR 协调与结果读取；GitHub Actions 提供 repository-native compute。当前 Agent 必须从 run status、job / step、logs 与必要 artifact 恢复结果。工作流已启动或请求被接受不构成通过，祖先提交的成功也不自动支持当前 Head 声明。

本节只声明 local + Actions 的最薄 instance 与证据恢复边界，不维护 workflow catalog；具体 verification obligation 仍由当前 Method、Rule、acceptance 与 repository scripts 决定。

`pull_request` / `push(master)` 触发的同名 workflow 仍只承担 repository lint、deterministic tests 与固定 smoke；不能拿其通过结果替代当前 task signals 的 task-level invocation。

调用 Rule Discovery transport 本身是 preflight compute，不授予任何后续 Repository / Issue / PR / workflow / deployment 副作用权限。

调用时的信号 schema、三态语义、bounded-token、matching、fail-closed 与 locator-only contract 由 Rule Discovery Architecture 持有；本 profile 只拥有当前 Tool / Rule root / local + cloud invocation instance。

`phases` signal 的合法 Method-specific identity 由当前选定 Method 自己定义；本 profile 不复制 phase token 列表。

本文件不维护 Rule id inventory、scope metadata、候选集或 Rule → signal 映射。

## 4. Skill Discovery 实例

当前 Repository 的 Skill root 为 `skills/`，ordinary Agent 使用 Agent Skills 原生 discovery，根据 Skill `name` / `description` 与当前责任按需加载 `SKILL.md`。

- Skill Architecture：`docs/architecture/skill-architecture.md`；
- Human inventory：`skills/README.md`。

本 profile 不复制当前 Skill 名单或数量；这些可以由当前 `SKILL.md` corpus 与 Human inventory 机械验证。

## 5. Model Collaboration 实例

`agentic-dev` 当前提供 reusable `architecture:model-collaboration` 与 `method:model-collaboration-adoption`，但本 Repository 的 ordinary runtime **不因能力存在而默认启用多模型协作**。

当前 local instance：

- status：`disabled`；
- persistent platform config：none；
- concrete model tier mapping：none；
- single-agent fallback：当前 ordinary runtime 本身。

历史 `experiment/codex-multi-model-collaboration` 分支只作为 Research / Evidence 来源，不是本 Repository 当前 `.codex/` instance，也不通过 Project Profile 继承其模型名、并发数或 agent TOML。

若未来 `agentic-dev` 自身决定启用 Model Collaboration，必须先按当前 Authority 接受相关 reusable semantics，再显式进入 `method:model-collaboration-adoption`，探测当前 runtime、建立 local config / validation Evidence，并更新本 section；不能因为 Guide 示例或历史实验存在就推断 enabled。

## 6. Architecture / Project 入口

Agent runtime 的稳定入口：

```text
AGENTS.md
→ Project Roadmap + Project Capability Profile + GitHub current facts
→ local selector instance → selected Method / direct responsibility
→ relevant Architecture / Skill / Rules

Method Architecture 只在 selection contract / scaling / no-match 语义本身需要处理时按需加载；Human README 不属于 ordinary Agent 固定入口。
```

Project / Capability 边界：`docs/architecture/project-knowledge-architecture.md`。

顶层 capability model：`docs/architecture/engineering-capability-architecture.md`。

## 7. Human View 实例

Human entry：

- repository overview：`README.md`；
- usage guide：`docs/guides/using-agentic-dev.md`；
- Project navigation：`docs/project/README.md`；
- Architecture navigation：`docs/architecture/README.md`；
- Method navigation：`docs/methods/README.md`；
- Rule navigation：`docs/rules/README.md`；
- Skill navigation：`skills/README.md`。

这些 Human View 可以解释 current instance，但不拥有 runtime selector 或 normative body。

## 8. 当前项目状态入口

当前项目阶段、当前 evolution 与下一候选由 `docs/project/project-roadmap.md` 持有稳定摘要；精确 GitHub branch / Issue / PR / Actions 状态必须实时读取。

稳定历史里程碑由 `docs/project/project-evolution.md` 摘要；完整实施 Evidence 留在 Git / Issue / PR / Actions。

## 9. Consumer 发布边界

Consumer 不复制本 profile，也不建立与 `agentic-dev` Source tree 同构的 runtime instance。

首次安装 / 后续升级分别进入：

- `method:consumer-adoption`；
- `method:consumer-upgrade`。

两者的输入都是**版本化 Release**，而不是 upstream Source baseline。

Consumer repository-local 默认目标由 Consumer Architecture 定义为：

```text
Consumer-owned AGENTS.md
+ .agents/README.md
+ .agents/skills/**
```

本 profile 中的：

- Method selector；
- Rule root；
- Rule Discovery Tool；
- cloud transport；
- `skills/` Source root；
- Model Collaboration self-instance；

都只描述 `agentic-dev` 自身 provider runtime，不自动进入普通软件 Consumer Release。

如果某个 release Skill 需要 deterministic script / external execution，Consumer 安装过程只建立该 Skill 的 direct path / automated alternate / Evidence recovery / fail-closed instance，不复制本仓整个 Tool / Rule Discovery infrastructure。

因此本文件是 `agentic-dev` 的 capability **instance profile**，不是跨 Repository 的 capability package 或 release manifest。

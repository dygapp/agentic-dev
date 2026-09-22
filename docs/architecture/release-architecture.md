---
id: architecture:release
type: architecture
status: active
distribution: source-only
---

# Release 架构

## 1. 目标

本 Architecture 定义 `agentic-dev` Source / Authoring Model 如何经过确定性构建形成面向普通软件 Consumer 的版本化 Software Development Agent Skills Release。

它拥有：

- Release artifact 的稳定结构；
- Source asset 到发布 Skill / installation support 的组合合同；
- deterministic build / integrity / provenance contract；
- Consumer repository-local 安装边界；
- Release-owned 与 Consumer-owned 资产的分界。

它不拥有具体 Consumer 项目事实，也不把 `agentic-dev` Project current state 传播给 Consumer。

## 2. 首版发布单元

首版普通软件 Consumer Release 以 Agent Skill 为主要运行单元。

现有 `release-direct` Skill 可以直接进入 Release；当某个独立 Method 具有稳定、可单独触发的复杂工作生命周期，而现有 Skill 无法在不扩大职责的情况下承载它时，可以建立新的有界 Skill。

首版因此包含：

- 当前已有的 12 个 `release-direct` Skill；
- `establish-requirement-baseline`；
- `clarify-architecture`；
- `activate-model-collaboration`。

这三个新增 Skill 分别承接需求基线建立、系统性架构澄清、模型协作本地启用，不接管完整软件开发生命周期。

## 3. 分布式组合 metadata

每个发布 Skill 在自身 `SKILL.md` metadata 中声明：

```yaml
agentic-dev-release-inputs: "source-id-a;source-id-b;..."
```

该字段只保存**本 Skill 消费哪些 `release-input` canonical owner**，不复制 Source 正文。

Release Build 必须：

1. 从当前仓库扫描 `distribution: release-input` canonical owner；
2. 从每个 `release-direct` Skill 的 metadata 恢复 composition；
3. 验证每个 `software-development` release input 至少被一个发布 Skill 消费；
4. 验证 Skill 不引用不存在、`source-only` 或 release target 不匹配的 source id；
5. 由 canonical Source body 机械生成 Skill `references/release-inputs/**`；
6. 不维护独立中央 composition Registry。

一个 release input 可以被多个 Skill 消费；这些引用是 build projection，不取得 Source canonical ownership。

## 4. Consumer installation input

`release-target: consumer-installation` 的 Source owner 不进入 ordinary Skill runtime。

Build 将这些 owner 机械投影到 artifact 的：

```text
installation/references/**
```

用于首次安装 / 后续升级时理解 Release contract。安装后它们不复制到 Consumer `.agents/**`，不会成为普通运行时 Authority。

首版安装执行器是发布 artifact 自带的 `install.py`。它不是新的 setup / adoption Skill，也不改变未来是否增加安装 Skill 的独立决策。

## 5. Release artifact 结构

确定性构建输出：

```text
manifest.json
install.py
installation/
  references/
    <generated installation references>
repository/
  .agents/
    README.md
    release/
      manifest.json
      skill-index.json
    skills/
      <skill>/
        SKILL.md
        references/
          release-inputs/
            <generated references>
        scripts/        # 仅 Skill 本身需要时存在
        assets/         # 仅 Skill 本身需要时存在
```

发布 archive 不包含作为 Consumer ordinary runtime Authority 的：

- `docs/project/**`；
- provider Roadmap / Current Gate / Capability Profile；
- `docs/research/**`；
- historical Eval result；
- provider-only Guide；
- Open Issue / PR 状态。

平台要求固定位置的 adapter 仍使用平台原生路径；首版 Release 不为了目录统一把平台 adapter 强制移入 `.agents/**`。

## 6. Skill reference transformation

对一个被 Skill 声明消费的 release input，Build：

- 读取 canonical Source body；
- 去除 Source Front Matter；
- 在生成文件顶部写入机器生成声明、Source id 与 exact source SHA；
- 写入目标 Skill 的 `references/release-inputs/<stable-name>.md`。

生成 reference 不是新的 canonical owner。其正文只能由 build 从 exact source commit 再生，不允许人工直接维护。

普通 Consumer 不安装 upstream Rule tree 或 Rule Discovery Tool。Skill Procedure 必须消费当前运行环境提供的 packaged references 与 Consumer-local policy，而不是要求在线返回 `agentic-dev` Source Repository。

## 7. Manifest 与 identity

每个 Release Candidate 的 `manifest.json` 至少包含：

- schema version；
- release id / release version；
- exact source SHA；
- distribution target；
- Runtime compatibility declaration；
- build evidence locator；
- Runtime Acceptance evidence locator（只有通过当前 subject 的机器可读 runtime evidence 校验后才记录为已验证）；
- 当前 Release completion claim 对应的 verification evidence locator；
- Skill inventory；
- Skill → release input composition；
- installation input inventory；
- artifact file SHA-256 checksums。

`skill-index.json` 只由 Skill canonical metadata 生成，保存必要 locator / description，不复制 Skill Procedure，不成为手工 selector。

Release manifest 与 Skill index 都由 Build 生成；不得手工维护第二套 inventory。

Release Build 本身只能证明 artifact composition / integrity，不能把尚未执行的 Runtime Acceptance 声明成已验证兼容性。Builder 在没有完整 Runtime Evidence 时必须把相关 Runtime compatibility 保持为未验证候选状态；只有同时提供 durable Runtime Evidence locator、repository-native automated runtime report、authenticated model runtime report 与该 authenticated report 对应的 evidence bundle，并机械确认两类 Evidence 都为成功、都绑定当前 exact source SHA、authenticated report 具有当前完整 scenario identity / release identity / authentication status，且 bundle 与 report 中声明的逐场景 Evidence digest 一致时，才能把对应兼容性标记为 `verified`。单独一个 locator、只有顶层 PASS 的摘要 JSON、历史 / 失败 / subject 不匹配 report、缺失 bundle 或不完整 Evidence 组合必须 fail closed，不能提升 compatibility 状态。Manifest 同时记录 locator、两份已校验 report 的 digest 与 authenticated evidence bundle digest，使后续 Evidence recovery 可以核对实际证据身份；Build Evidence locator 继续独立保留，避免 Runtime Evidence 覆盖 artifact provenance。

Release completion Evidence 与上述两类 Evidence 同样保持独立，但 finalization 不能与未验证 Runtime compatibility 共存。Builder 不得用 Build Evidence 或 Runtime Acceptance Evidence 自动填充 `verification_evidence_locator`，也不得让调用方自行声明“哪些 acceptance 构成完整 completion claim”。当前 Project Capability Profile 只保存 completion acceptance owner locator 与 claim identity；Builder 在 exact-subject clean checkout 中读取该 selector，再从 canonical acceptance owner 的 claim 定义机械恢复完整 expected acceptance scope。只有当前 Release 已具有通过机械校验的 Runtime Acceptance Evidence，并同时提供 durable verification locator 与机器可读的 Release completion report，且 report 类型 / schema、`PASS` 状态、exact source SHA、当前 release identity、claim identity、实际 acceptance set 与 expected scope 完全一致、逐项 `PASS` 且具有可恢复 Evidence locator，以及 `Blocking = 0`、`Medium = 0`、`Unverified = 0` 后，才记录 Release completion verification locator。任何“completion 已验证但 manifest compatibility 仍未验证”的组合、只有顶层 `PASS`、非空但缺项的部分列表、额外 acceptance、调用方自定义 scope、历史 / subject 不匹配 Evidence 或其他不完整输入都必须 fail closed。Manifest 同时记录 claim id、acceptance count、canonical acceptance authority path / digest、Project selector digest 与 completion report digest，使 Build provenance、Runtime compatibility Evidence 与最终 Release completion Evidence 可以分别恢复和核对；具体 Gate scope 仍只由 Project acceptance owner 持有，不写死进 Builder。

## 8. 确定性构建

给定完全相同的：

```text
exact source SHA
+ release version
+ build evidence locator
+ optional validated Runtime Acceptance reports + authenticated evidence bundle + durable evidence locator
+ optional exact-subject Project-selected completion contract + validated Release completion report + durable verification evidence locator
+ current classified source
+ release build logic
```

Build 必须产生字节稳定的 manifest、Skill references 与 ZIP archive。

构建不得读取墙钟时间、随机值或工作区外状态。ZIP entry 顺序、时间戳与权限必须固定。

Build 应 fail closed：

- source SHA 不是精确 40 位 commit id；
- distribution audit 不通过；
- release input 未被消费；
- Skill 引用非法 source id；
- generated path 冲突；
- Runtime Evidence 输入不完整、失败、无法解析或与 exact source SHA 不匹配；
- Release completion Evidence 输入不完整、失败、claim identity / acceptance scope 与当前 Project-selected canonical contract 不一致、finding 非零或与 exact source / release identity 不匹配；
- artifact integrity 无法验证。

## 9. Consumer-owned Bootstrap

根 `AGENTS.md` 始终由 Consumer 拥有，不作为 Release payload 中的替换文件。

`install.py` 只管理一个带稳定 marker 的薄 integration block，用于定位：

- `.agents/README.md`；
- `.agents/release/skill-index.json`；
- `.agents/skills/**`。

安装器必须保留 marker 之外的 Consumer `AGENTS.md` 内容，并且重复安装同一 Release 后结果保持稳定。

安装器只删除 / 替换上一个 installed manifest 明确声明为 Release-owned 的 Skill；不得删除 Consumer-local `docs/**`、未归属给 Release 的本地 Skill 或其他项目资产。

## 10. 已安装状态

安装完成后，Consumer repository-local 核心结构为：

```text
AGENTS.md                  # Consumer-owned + bounded release locator
.agents/
  README.md                # generated Human View
  release/
    manifest.json          # installed release provenance
    skill-index.json       # generated locator metadata
  skills/**                # release-owned Skill packages
```

Consumer 的产品、需求、系统架构、技术方案、项目状态与本地 policy 继续由 Consumer 自己的 Repository Authority 持有。

## 11. Gate 边界

本 Architecture 只定义 Build / Package / Install structure。

真实 Codex native discovery、ChatGPT + GitHub Connector compatibility、script alternate path、Progressive Disclosure runtime behavior 与 upstream dependency negative control 属于后续 Runtime Acceptance；不能仅根据 artifact 结构声称这些行为已经通过。

---
id: research:standard-skills-distribution-feasibility
type: research
status: active
distribution: source-only
---

# 标准 Skills Distribution 可行性验证

## 1. 目的与边界

本文记录方法论产品边界重构 Gate P1 的可行性 Evidence，验证：

> `agentic-dev/skills/**` 是否可以直接作为标准 Agent Skills 兼容安装源，而不要求先经过自定义 Release Builder / ZIP / semantic composition。

本轮只使用 disposable fixture，不修改真实 Consumer，不删除现有 Release Builder，也不把当前 15 个 Skill 的旧 release metadata 视为最终产品形态。Skill 自包含语义迁移属于 P2。

验证规划基线：

- P1 入口：`8847cab2caad211718ff69161ebfc8963484e6af`；
- 当前规划 / Specification 不改变 `skills/**` 目录布局；
- 版本化远端样本：`agentic-dev-v0.0.0-rc.1`；
- 该 tag 当前 peel 到 `51db05801382b74ee01601f391305fcbbff98db3`。

## 2. 验证工具

- 标准 Skills CLI：`skills@1.7.0`；
- Codex：`codex-cli 0.155.1`；
- 当前 Runner Node：`v20.19.2`。

`skills@1.7.0` 声明 Node `>=22.20.0`。当前 Runner 会产生 `EBADENGINE` warning，但本轮实际 discovery / install 命令均可以执行。正式 Bootstrap 应把 Skills CLI 自身的受支持运行时作为安装前置检查，不把“当前低版本 Node 仍能运行”写成兼容保证。

## 3. Repository 与版本定位

### 3.1 远端 Repository 直接发现

使用：

```text
skills add https://github.com/dygapp/agentic-dev --list --yes
```

结果：

- Repository clone 成功；
- 发现 15 个 Skills；
- 不需要读取或构建 `docs/**`。

### 3.2 当前 worktree 布局

使用标准 CLI 直接对当前 P1 worktree 做 local source discovery，结果同样发现 15 个 Skills。

因此当前 `skills/<name>/SKILL.md` 目录形态本身已经是标准 CLI 可识别布局；P2 不需要为了“可发现”重新设计一套 package layout。

### 3.3 exact tag

使用：

```text
skills add https://github.com/dygapp/agentic-dev/tree/agentic-dev-v0.0.0-rc.1 --list --yes
```

CLI 明确解析为：

```text
Source: https://github.com/dygapp/agentic-dev.git @ agentic-dev-v0.0.0-rc.1
```

并发现 15 个 Skills。

标准安装生成的 `skills-lock.json` 对每个 Skill 记录：

- `source: dygapp/agentic-dev`；
- `ref: agentic-dev-v0.0.0-rc.1`；
- `sourceType: github`；
- 精确 `skillPath`；
- `computedHash`。

因此目标版本模型可以采用：

> **不可变 Git tag + standard skills lock ref/hash**

而不需要另建自定义 package identity。

### 3.4 arbitrary commit SHA 的实际边界

`skills@1.7.0` 对：

```text
https://github.com/dygapp/agentic-dev/tree/51db05801382b74ee01601f391305fcbbff98db3
```

会把 SHA 作为 Git branch/ref 交给 clone；当前命令失败：

```text
remote branch ... not found
```

CLI 没有回退默认分支。

因此 P1 不宣称标准 CLI 原生支持 arbitrary commit SHA URL。正式分发使用**明确、不可移动的版本 tag**；内部验证仍可以使用 exact source SHA 绑定 tag subject。

## 4. 安装与 Consumer ownership

### 4.1 单 Skill 安装

在 disposable git fixture 中预先建立：

- Consumer-owned `AGENTS.md` sentinel；
- Consumer-owned `docs/consumer.md` sentinel。

然后执行：

```text
skills add https://github.com/dygapp/agentic-dev/tree/agentic-dev-v0.0.0-rc.1 \
  --skill specify \
  --agent codex \
  --copy \
  --yes
```

结果：

```text
./.agents/skills/specify
  copy → Codex
```

并生成 `skills-lock.json`。

Consumer 的 `AGENTS.md` 与 `docs/consumer.md` 均保持原内容。

### 4.2 全量 15 Skill

同一 exact tag 使用 `--skill '*'` 安装到 Codex：

- 安装 Skill 数：15；
- lock entry 数：15；
- 全部 lock `ref` 均为 `agentic-dev-v0.0.0-rc.1`；
- Consumer-owned `AGENTS.md` 与项目文档未被修改。

### 4.3 重复安装

在首次安装后再次修改 Consumer sentinel，再以同一 exact tag 重复安装全部 15 Skill：

- Consumer `AGENTS.md` 保持新 sentinel；
- Consumer project doc 保持新 sentinel；
- 15 个 lock ref 保持 exact tag；
- 同一版本的 `computedHash` 保持一致。

因此标准 exact-tag reinstall 可以作为有界、可重复的安装路径，不需要 custom installer 来保护 Consumer 根文件。

## 5. Codex 原生发现

使用 Codex App Server：

```text
codex -c skills.bundled.enabled=false app-server --listen stdio://
```

初始化后调用 `skills/list`。

### 5.1 单 Skill

对只安装 `specify` 的 fixture：

- Codex 返回 `specify`；
- path 为 Consumer-local `.agents/skills/specify/SKILL.md`；
- `scope=repo`；
- `enabled=true`；
- `errors=[]`。

Runner 还存在一个 user-scoped `find-skills`，因此验证只按“路径属于当前 Consumer `.agents/skills/**`”统计 repo-local inventory。

### 5.2 全量

对安装全部 15 Skill 的 fixture：

- repo-local Skill 数：15；
- 15 个名称与 Repository inventory 一致；
- 全部 enabled；
- `errors=[]`。

这证明标准 CLI 安装出的目录可以被当前 Codex native discovery 直接消费。

## 6. Provider docs 边界

全量 exact-tag 安装后的 Consumer runtime payload 中：

- `.agents/skills/**` 下只有 15 个 Skill package 文件；
- 没有复制 Provider `docs/**`；
- Consumer 自己的 `docs/consumer.md` 保持不变。

当前 15 个 `SKILL.md` 仍带有旧 `agentic-dev-release-inputs` metadata，这是 P2 需要消除的**语义自包含问题**，不影响 P1 已证明的**标准安装机制**。

P1 因此只得出：

> 标准 installer 能直接以 `skills/**` 为安装源，且不会为了安装而复制 Provider docs。

不提前声称旧 Skill 内容已经满足最终 P2 self-contained contract。

## 7. Negative controls

### 7.1 不存在的 ref

使用不存在的：

```text
.../tree/p1-ref-does-not-exist-20260923
```

结果：

- CLI 非零退出；
- 明确报告 remote branch/ref 不存在；
- 没有输出 “Found 15 skills”；
- 没有生成 `skills-lock.json`；
- 没有回退 `master` / `latest`。

因此 ref resolution failure 是 fail closed。

### 7.2 exact SHA URL

arbitrary commit SHA URL 同样非零退出且没有默认分支 fallback。该行为说明“SHA URL”不是可用标准 UX，而不是版本不确定时静默成功。

## 8. Update 边界

本轮还观察了：

```text
skills update -p -y
```

在 disposable fixture 中未在 180 秒内完成，因此没有形成可以支撑 agentic-dev 版本升级 contract 的 Evidence。

本轮不把该结果解释为 CLI 的永久产品缺陷，也不依赖它。

因此当前只冻结升级入口的设计边界：

> **未来跨版本升级应显式选择新的 exact version tag，并重新执行标准 add/install；不得把无版本 generic `update` 当作 agentic-dev 的隐式 latest 升级协议。**

本轮已有的是同 tag reinstall 成功 Evidence，它足以证明重复安装不会污染 Consumer-owned 根文件，但**没有**证明尚不存在的第二个正式版本之间 `tag A → tag B` 的跨版本迁移。该场景应在后续产生第二个真实版本后单独验证。

## 9. P1 结论

当前 Evidence 支持 Gate P1：

**PASS candidate**

P1 已证明：

1. 当前 Repository 的 15 个 Skill 使用标准目录即可被 `skills@1.7.0` 发现；
2. GitHub Repository + exact tag 是标准 CLI 支持的安装入口；
3. standard lock 保留 source、exact tag ref、skill path 与 content hash；
4. 指定 Skill与全部 15 Skill 均可安装到 Codex 的 `.agents/skills/**`；
5. Codex native `skills/list` 能直接发现安装后的 repo-local Skills；
6. 安装与同 tag reinstall 不覆盖 Consumer-owned `AGENTS.md` / project docs；
7. 安装不会复制 Provider `docs/**`；
8. 无效 ref fail closed，不回退默认分支；
9. arbitrary SHA URL 不作为标准安装 UX；版本发布使用不可变 tag；
10. P1 已排除把无版本 generic `update` 作为已验证升级协议；未来跨版本升级采用显式新 exact tag 的设计边界，但 `tag A → tag B` 仍需后续真实版本 Evidence。

因此没有 Evidence 要求继续保留：

```text
Source docs
→ semantic Release Build
→ custom ZIP
→ custom installer
```

作为普通 Consumer 安装前提。

P1 的结论只证明 **Distribution mechanism 可行**。Skill 自包含、旧 release-input 语义迁移与 canonical content 收敛仍由 P2 完成。

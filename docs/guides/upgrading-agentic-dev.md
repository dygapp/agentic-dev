---
id: guide:upgrading-agentic-dev
type: guide
status: active
---

# 升级 Consumer 中的 agentic-dev Skills

升级不是同步 upstream Source，也不是重新采用 Provider 的 Method / Architecture / Rule。

Existing Consumer 已拥有：

- 当前 installed Skills 与 lock / provenance；
- Consumer-owned `AGENTS.md`；
- Product / Requirement / Architecture / current work；
- Consumer-local constraints；
- 本地 Runtime / platform config。

## 1. 显式选择新的 exact tag

先恢复当前 adopted ref，再明确选择目标 immutable tag。不要把无版本 `latest` 或 generic update 当作 agentic-dev 的隐式升级协议。

`agentic-dev-v0.2.0` 已形成第二个稳定版本，并完成 `agentic-dev-v0.1.0 → agentic-dev-v0.2.0` 的有界跨版本验证。验证使用标准 Skills installer 显式选择版本：先从 `agentic-dev-v0.1.0` 安装全部 15 个 Skill，再以 v0.2.0 release candidate 覆盖安装；升级后 15 个 Skill inventory 保持完整，11 个发生内容变化的 Skill 被替换，Codex 目标 inventory 仍可见 15 项，Consumer-owned `AGENTS.md`、项目文档和 constraints 均未被覆盖。

该结论只验证**显式版本切换、Skill inventory / 安装边界与 Consumer ownership preservation**。它不表示任意 Consumer 对 11 个变化 Skill 的实际业务行为都自动完成回归；真实 Consumer 仍必须按自身使用路径重新验证受影响行为。无版本 `latest` 或 generic `update` 仍不属于 agentic-dev 的已验证升级协议。

## 2. 比较真正会改变 Consumer 的内容

升级重点是：

- Skill inventory 变化；
- 已安装 Skill 内容 / hash 变化；
- bootstrap / Guide locator 变化；
- 对当前 Consumer 实际使用路径有影响的兼容性说明。

不比较 Consumer tree 与 Provider Source tree，也不要求 Consumer adopt Provider `docs/**`。

## 3. 使用标准 installer 显式安装目标 tag

形成有界 update plan 后，用标准 Agent Skills-compatible installer 指向新的 exact tag。

安装不得自动覆盖：

- Product / Requirement / Domain facts；
- System / Application / Data / Interface Architecture；
- technology policy；
- authorization；
- terminology；
- Roadmap / current work；
- Consumer-local rules / policies；
- 其他项目自有文件。

## 4. 只重新验证受影响行为

旧版本 Evidence 不能自动证明新版本 Skill 行为。

至少：

- 验证新 Skill inventory / native discovery；
- 对发生变化、且当前 Consumer 实际依赖的 Skill 做 targeted behavior revalidation；
- 检查 Consumer-local constraints 仍能正确叠加；
- 检查 `AGENTS.md` / project docs 没有被覆盖。

未变化的 claim 可以按 Consumer 自己的 Evidence reuse policy 复用，但必须证明 exact diff 不影响该 claim。

## 5. 最后更新 Guide locator

只有 Skills 安装与必要验证通过后，才把 Consumer 记录的 adopted ref / exact-version Guide locator 切到新 tag。

如果新版本验证失败，保留旧 adopted identity 和真实 blocker，不把“下载成功”描述成升级完成。

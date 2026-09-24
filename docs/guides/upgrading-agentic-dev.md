---
id: guide:upgrading-agentic-dev
type: guide
status: active
distribution: source-only
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

P1 已验证 exact-tag install 与同 tag reinstall；真正的 `tag A → tag B` 跨版本迁移仍应在存在第二个正式版本后用真实版本 Evidence 单独验证。

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

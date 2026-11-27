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

`agentic-dev-v0.4.0` 是本版目标稳定版本，以实际远端 immutable tag 为准。在 `v0.3.0` 长期设计知识生命周期基础上补齐知识健康治理与公共能力架构演进。变化的 9 个 canonical Skills 是 `clarify-architecture`、`converge`、`establish-requirement-baseline`、`execute-unit`、`readiness-check`、`slice-work`、`specify`、`systematic-debug`、`technical-plan`；inventory 仍为 15，Consumer-owned Authority 与安装边界不变。知识治理使用按需 [Guide](document-governance.md)、Consumer-local 维护约定和已有 Skills，不新增独立治理 Skill。

`v0.3.0 → v0.4.0` 发布前有界升级 smoke 使用标准 `skills@1.7.0`，先安装旧 exact tag 再覆盖安装最终本地候选：15/15 Skills 与 lock 清单一致，9 个 Skill 内容变化，Consumer-owned AGENTS、设计、政策、代码及本地 Skill 哈希不变。只证明分发与安装边界，不证明真实 Consumer 业务行为、原生发现或长期收益。正式远端 tag 的安装结果以实际验证 Evidence 为准。

`v0.2.1 → v0.3.0` 的历史有界升级 smoke 使用标准 `skills@1.7.0`：在 disposable Consumer 从远端 `v0.2.1` exact tag 安装 15 个 Skill，再从 `v0.3.0` 发布候选本地 Source 覆盖安装；安装后 15/15 Skills 与 lock 保持，正好六个预期 Skill 内容变化，Consumer-owned `AGENTS.md` 与项目设计文档哈希不变。该 smoke 验证安装边界、变化内容和文件保护，不验证 Agent 在真实 Consumer 的业务行为；组件 / 接口设计知识由 Consumer 在正常项目演进中逐步形成和验证，不设独立验收阶段。

`v0.2.0 → v0.2.1` 的历史有界升级 smoke 已验证 15 个 Skill、两个变化的 Skill contract，以及 Consumer-owned 文件保持不变；该历史证据不能代替本版的升级验证。

正式版本选择应使用 `agentic-dev-v0.4.0` exact immutable tag，不使用无版本 `latest` 或 generic `update`。实际 Consumer 只需针对其依赖的变化 Skill 和当前流程执行相称的验证。

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

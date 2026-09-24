---
id: guide:adopting-agentic-dev
type: guide
status: active
distribution: source-only
---

# 在已有项目中采用 agentic-dev

本文用于已有软件 Repository 第一次引入 `agentic-dev`。默认目标是**最小侵入 adoption**：安装 exact-version Skills、建立最薄方法论 locator、验证 Agent 能发现 Skills，然后立即回到 Consumer 自己的开发工作。

## 1. 先恢复 Consumer，而不是先整理 Consumer

安装前确认：

- 当前 Repository / `AGENTS.md`；
- Product / Requirement / Architecture / current work 的稳定入口；
- 已有 Agent Skills / local policy；
- 当前 Runtime 与权限边界。

这些内容继续由 Consumer 自己拥有。

不要把以下工作设为 adoption 固定前置：

- 全仓文档重构；
- Requirement / Architecture Authority rebuild；
- 历史资料清理；
- 目录结构统一；
- Consumer-local rule 体系重构。

只有真实项目问题证明必要时，才把它们作为单独 remediation。

## 2. 选择精确版本

采用一个 immutable Git tag 或等价不可歧义 ref。

普通安装不比较 Consumer tree 与 `agentic-dev` Source tree，也不复制 Provider `docs/methods/**`、`docs/rules/**`、`docs/architecture/**`。

## 3. 使用标准 Skills 安装路径

目标形态：

```text
<consumer>/
├── AGENTS.md            # Consumer-owned
├── docs/**              # Consumer-owned
└── .agents/
    └── skills/**        # installed agentic-dev Skills
```

以当前 P1 验证过的 Codex 示例：

```bash
npx -y skills@1.7.0 add \
  https://github.com/dygapp/agentic-dev/tree/<exact-tag> \
  --skill '*' \
  --agent codex \
  --copy \
  --yes
```

实际使用前仍需满足安装器当前运行时要求。

## 4. 只做最薄 Bootstrap integration

如果 Consumer 已有稳定 `AGENTS.md`，只在必要时补充：

- repository-local Skill locator；
- Consumer-local constraints locator；
- adopted `agentic-dev` Repository + exact tag；
- exact-version Guide root / entry。

不要覆盖整个 `AGENTS.md`，也不要把 Guide 正文复制进去。

普通 Skill execution 不在线读取 Provider docs；用户明确询问“怎么用 / 下一步做什么”时，才按 adopted exact version 读取对应 Guide。

## 5. 验证

至少确认：

- 预期 Skill inventory 已安装；
- Consumer-owned `AGENTS.md` / docs 未被覆盖；
- native Agent runtime 能发现 repository-local Skills；
- install provenance 能恢复 exact ref；
- 普通 Skill 行为不依赖 Provider `docs/**`；
- 当前项目原有验证和权限边界仍成立。

## 6. 可选 Repository 治理

如果 adoption 后发现 Fresh Context 无法恢复项目事实、Requirement 大量冲突、Architecture owner 不清或本地规则全部堆进根 `AGENTS.md`，可以建议一次单独治理评估。

这是**项目问题驱动的可选工作**，不是“用了 agentic-dev 就必须重构仓库”。

完成最小 adoption 后，如果不知道下一步，使用 [`choosing-next-step.md`](choosing-next-step.md)。

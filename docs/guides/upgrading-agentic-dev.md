---
id: guide:upgrading-agentic-dev
type: guide
status: active
distribution: source-only
---

# 升级 Consumer 中的 agentic-dev Release

本文是 `method:consumer-upgrade` 的人类说明，不替代正式 Method。

## 升级不是同步 upstream Source

Existing Consumer 已拥有：

- 当前 installed release；
- Consumer-owned `AGENTS.md`；
- Consumer-local Requirement / Architecture / policy；
- 本地执行与环境适配。

升级比较的是：

```text
current installed release
+ Consumer-local retained obligations
+ candidate release
```

而不是 Consumer tree 与 `agentic-dev` Source tree。

## 推荐过程

1. 恢复当前 installed release 与 Consumer Authority；
2. 选择精确 candidate Release；
3. 核对 Release / migration delta；
4. 形成 bounded update plan；
5. 更新 Release-owned Skills / resources；
6. 保留并重新核对 Consumer-local obligations；
7. 对真实受影响行为做 targeted revalidation；
8. 记录新的 installed release。

## 必须保护的本地内容

升级不得自动覆盖：

- Product / Requirement / Domain facts；
- System / Application / Data / Interface Architecture；
- technology policy；
- repository / external-operation authorization；
- terminology；
- Roadmap / current work；
- 其他 Consumer-local customization。

旧 Evidence 也不能自动证明 candidate Release 的新行为；已变化的 Skill、compatibility 或 execution path 必须重新取得 Current Evidence。

正式过程与完成条件见 `docs/methods/consumer-upgrade.md`。

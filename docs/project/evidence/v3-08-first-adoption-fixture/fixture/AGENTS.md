# Fixture Repository Authority

本目录只代表 V3-08 Gate C 的 Evidence-only minimal Consumer fixture。

## Authority order

1. `AGENTS.md`
2. `SPECIFICATION.md`
3. `docs/README.md` 仅作为本地发现入口，不拥有产品正文
4. 已采用本地 Skill 只拥有执行过程，不得覆盖上述 Consumer Authority

## Ordinary runtime

- 只使用 fixture-local current resources；
- 不自动访问 `agentic-dev` upstream；
- 历史 adoption decision 不进入普通 state-only / routing-only 上下文；
- locator 缺失、主职责歧义或 Authority 冲突时在本地 fail closed。

# V3-07 — agentic-dev 自采用与发现机制切换

**跟踪：** Issue #113  
**启动基线：** `master@5ae0e144d30c6010fadf8e3beff3c12ce4b7a147`

## 目标

把已经集成的使用方生命周期、资源模型与资源发现架构投射到 `agentic-dev` 自身真实仓库状态，形成一个可持续维护的本地发现机制，并显式取代现行 v2 手工 discovery surface。

## 已确认事实

- 当前仓库没有实际版本化 Activation Manifest / Runtime Catalog 文件，不为历史设计创建空容器；
- 当前仓库持续存在跨资源职责 / 条件正规化需求，因此需要一个小型 Reviewed Discovery Map；
- 当前没有证据要求 Runtime View / Catalog / generator；
- candidate validation 已覆盖 Fresh Context、routing-only、execute、GitHub Actions、工程纪律、技术画像、验证 / 外部操作规则、Stage Return、stale / missing / coverage drift / ambiguity、no-match 与 local-only ordinary runtime；
- candidate validation 中发现的 membership/source binding、外部操作过度激活和 Map 重复算法问题均已修复；
- candidate validation 当前未解决 Blocking / Medium = 0。

## 当前拟集成机制

```text
AGENTS / README / Roadmap / GitHub current state
→ docs/discovery/README.md
→ 按需 docs/discovery/reviewed-discovery-map.md
→ current semantic owner / primary Skill
```

- `docs/discovery/README.md`：Local Discovery Entry，基线 v0.1；
- `docs/discovery/reviewed-discovery-map.md`：非规范性 Reviewed Discovery Map，基线 v0.1；
- 不建立 Runtime View / Catalog / Manifest / generator。

## 已完成 cutover 修订

- `AGENTS.md` 已把 `docs/discovery/README.md` 设为 `agentic-dev` 自身 ordinary runtime 的本地发现入口，并明确 Map 不进入 Authority 顺序；
- README 已指向 V3-07 与 self-runtime discovery 入口；
- Roadmap 已切到 Issue #113 条件恢复；
- `rule-activation-guide.md` 已降为低频初始化 / 采用 / 升级导航，不再维护手工职责 / 风险路由表；
- `consumer-local-rule-activation.md` 已降为 Consumer-local 落地说明，长期 discovery / routing 语义统一指向 V3-05 / V3-06；
- v2 metadata / routing project contracts 保留冻结 v2 历史设计 / Evidence 身份，不再被 current bootstrap / Guide 当作长期 owner；
- v3 总规划已推进到 V3-07 当前 Gate。

## 当前待办

1. 重新固定 PR #114 精确 Head 与相对 `master` 差异；
2. 执行 post-cutover 验证：
   - Fresh Context / current work；
   - current discovery mechanism 唯一性；
   - routing-only / execute；
   - supporting capability；
   - Stage Return；
   - stale / missing / coverage drift / ambiguity / no-match；
   - ordinary runtime local-only；
   - Consumer 不继承 `agentic-dev/docs/discovery/*`；
3. 检查 Reviewed Discovery Map coverage / source binding 仍与最终 Head 对应的真实 owner 一致；
4. 按 `docs/project/ai-review-guidelines.md` 对最终精确 Head 做高影响 AI 复核；
5. Blocking / Medium 为 0 后才进入 Ready / integration；
6. 集成后核验 `master`、关闭 Issue #113；V3-08 只成为下一 Planning Candidate。

## 非目标

- 不修改任何 Consumer Repository；
- 不重新设计 V3-01～V3-06；
- 不提前执行 V3-08；
- 不创建 Rule Super Skill / Stage Router / Runtime Controller；
- 不全仓增加 Front Matter；
- 不创建没有当前证据价值的 Manifest / Catalog / Runtime View / generator。
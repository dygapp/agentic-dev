# 复核与验证规范

## 证据必须匹配声明

任何 `PASS`、完成、`READY TO INTEGRATE` 或等价声明，都必须由能够区分该声明是否真实成立的当前 Evidence 支持。实现存在、静态检查、历史 Run、工具返回 0、诊断 observation 或只覆盖主路径的证据不能替代声明实际需要的完成证据。

复用祖先 subject 的 Evidence 时，必须证明 ancestor → current 的精确差异不影响被复用 claim；不得把祖先 Run 描述成当前 Run。

## 高影响 Independent Review

Repository Authority、canonical Skill contract / core Skill、Provider governance、产品边界或其他持续塑造 Agent 行为的高影响变化，在最终集成决策前必须执行 Fresh / Independent Review。

Independent reviewer 不继承实现者的完成结论作为前提，应重新读取 exact candidate、Authority 和直接 Evidence。普通局部、低风险、可逆变化不自动升级为多级 Gate。

## Review 与授权

Review PASS 不授予 merge、release、deploy 或破坏性外部操作权限。验证基础设施也服从最低必要复杂度：能由 deterministic test 或小型 fixture 区分真假的 claim，不启动额外模型运行时。

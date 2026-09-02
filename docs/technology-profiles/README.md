# Technology Profiles

本目录保存已经进入 `agentic-dev` Repository Authority 的 Technology Profile 实例，并作为 Profile 实例的唯一直接发现入口。

上位契约：

`docs/architecture/technology-profile-contract.md`

## 规则

- 本目录只保存规范性 Profile 实例，不保存 Research、临时 Candidate、Eval result 或 Consumer-local 项目事实；
- Profile 在正式集成前可以在独立分支 / PR 中形成 Draft，但只有实际进入当前集成分支后才成为现行 Profile Authority；
- 每个 Profile 必须满足 Technology Profile Contract 的 Identity、Applicability、Evidence、Rule Strength、Verification Profile、Consumer Override、Targeted Eval 与 Lifecycle 要求；
- 一个 Profile 可以由一个文件或一个具有明确单一入口的小目录承载，但必须能够从本目录直接发现当前入口；
- 同一 Profile 的多个历史版本不得同时被解释为当前规范。被取代内容必须明确 `Superseded / Replaced` 关系；
- 本目录不按“技术数量”追求覆盖率，不因为某技术常用就自动建立 Profile；
- Profile 不自动产生 Task-oriented Skill。

## Foundation v1

Foundation v1 只允许建立一个代表性 Profile：

> Vue 3 + TypeScript

当前 F3 / WI-05 正在独立分支中形成：

`docs/technology-profiles/vue3-typescript.md`

其当前状态为 **Draft / Targeted Eval Pending**。在对应变更实际合并到当前集成分支之前，本条只用于发现正在评估的 Profile 路径，不表示该 Draft 已经成为 `master` 的现行 Technology Profile Authority。

Element Plus、Spring、Gradle 和其他 Profile 继续属于 Post-v1 Backlog，不因本 Draft 出现而进入当前 Foundation v1 Completion Scope。

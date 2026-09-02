# Technology Profiles

本目录保存已经进入 `agentic-dev` Repository Authority 的 Technology Profile 实例，以及在独立分支 / PR 中形成、尚待集成的 Profile Draft。

上位契约：

`docs/architecture/technology-profile-contract.md`

## 规则

- 本目录只保存规范性 Profile 实例或待集成 Draft，不保存 Research、临时 Candidate、Eval result 或 Consumer-local 项目事实；
- Profile 可以在独立分支 / PR 中形成 Draft、Validated Draft 或拟集成 Baseline，但只有实际存在于当前 Repository 集成分支中的版本才构成现行 Profile Authority；
- 每个 Profile 必须满足 Technology Profile Contract 的 Identity、Applicability、Evidence、Rule Strength、Verification Profile、Consumer Override、Targeted Eval 与 Lifecycle 要求；
- 一个 Profile 可以由一个文件或一个具有明确单一入口的小目录承载，但必须能够从本目录直接发现当前入口；
- 同一 Profile 的多个历史版本不得同时被解释为当前规范。被取代内容必须明确 `Superseded / Replaced` 关系；
- 本目录不按“技术数量”追求覆盖率，不因为某技术常用就自动建立 Profile；
- Profile 不自动产生 Task-oriented Skill。

## Foundation v1

Foundation v1 只建立一个代表性 Profile：

> Vue 3 + TypeScript

实例入口：

`vue3-typescript.md`

该实例内容已满足 **Baseline v0.1 / Targeted Eval PASS**，`C-VTS-01`～`C-VTS-09` Fresh Runtime Targeted Eval 为 `9 / 9 PASS`、`41 / 41 assertions PASS`。它是否属于当前现行 Profile Authority，统一由该文件是否存在于当前 Repository 集成分支决定；feature / PR 分支上的同一 Baseline 不会自行取得现行 Authority。

Foundation v1 不因此自动增加 Element Plus、Spring、Gradle 或第二个 Technology Profile。
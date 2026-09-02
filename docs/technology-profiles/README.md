# Technology Profiles

本目录保存已经进入 `agentic-dev` Repository Authority 的 Technology Profile 实例。

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

当前 WI-04 只建立 Profile Contract 与本持久化入口，不在本目录提前创建 Vue / TypeScript Profile 内容。只有 WI-04 实际集成后，WI-05 才可以基于当前官方证据开始该 Profile 的 Research / Candidate / Draft 生命周期。

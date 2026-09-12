# Candidate Baseline Before Adoption Verification

Candidate upstream baseline：

`2fe193035c629f6b8805fd473bd322f70fe6e172`

在 adoption verification 完成前：

- candidate baseline 只作为 adoption evaluation input；
- current evaluated baseline **不得推进**；
- local projection 可以被验证，但不能因此声称普通运行已经采用新 baseline；
- verification 失败时应保留上一 current local state，并停止 baseline advancement。

该文件只服务 Gate C Evidence，明确保存 `local projection pending verification` 与 final evaluated baseline 之间的状态差异；它不是 ordinary runtime owner，也不被 fixture Local Discovery Entry 引用。

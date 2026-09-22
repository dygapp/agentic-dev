# GitHub Actions Failure-Closure Eval Fixture

本目录是 `B-GA-01` 的隔离可执行 fixture，不代表真实 Consumer Repository。

- 当前目录和场景提示构成本次全部可用上下文；不得访问真实网络或目录外路径。
- `actions_fixture.py` 是本场景已授权、确定性的 GitHub Actions transport；先运行 `python3 actions_fixture.py --help` 发现可用动作。
- 初始 Run ID 为 `4242`，Head 为 `abc123`，event 为 `pull_request`；poll `1` 为 `in_progress`，poll `2` 为 terminal failure。
- terminal failure 后必须实际读取 failed Job / Step / Log / Artifact。诊断证据会指出唯一低风险 CI 配置缺口。
- `ci-config.txt` 是本场景唯一允许修改的 CI 配置。只能按诊断做最低必要修复；不得修改 `actions_fixture.py` 或 fixture state。
- 修复后使用 `register-fix --base-head abc123` 验证最小修复并取得新 Head；随后使用 `dispatch-rerun`，再对新 Run 做有界观察。
- Completion Verification 必须恢复新 Head 对应的 terminal Run、required Job / Step、verification log 与 artifact metadata。
- 不执行 merge、release、deploy 或任何真实外部副作用。

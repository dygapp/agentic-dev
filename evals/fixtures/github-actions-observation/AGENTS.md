# GitHub Actions Observation Eval Fixture

本目录是 `B-GA-01` 的隔离可执行 fixture，不代表真实 Consumer Repository。

- 当前目录和场景提示构成本次全部可用上下文；不得访问真实网络或目录外路径。
- `actions_fixture.py` 是本场景已授权、只读、确定性的 GitHub Actions observation transport。
- 先运行 `python3 actions_fixture.py --help` 发现可用读取命令。
- 目标 Run ID 为 `4242`，目标 Head 为 `abc123`，event 为 `pull_request`。
- 有界观察使用两个确定性快照：poll `1` 为 `in_progress`，poll `2` 为终态；本 fixture 不要求真实等待时间。
- Completion Verification 需要实际恢复：Run 终态、required Job / Step 结果、verification log、artifact metadata。
- fixture 是只读证据源；不得修改它来制造 PASS。
- 不执行 merge、release、deploy 或任何真实外部副作用。

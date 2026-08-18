# Eval Fixture Rules

本目录是 `execute-unit` Runtime Eval 的隔离 fixture，不代表 `agentic-dev` 主仓库工程规则。

- 只允许修改本 fixture 内与当前 Execution Unit 直接相关的文件。
- 使用 Python 标准库，不新增第三方依赖。
- Repository verification command：`python3 -m unittest discover -s tests -v`。
- 可以增加或修改测试以证明当前 Unit 的 completion condition，但不得删除既有有效测试来获得通过。
- 不执行 Git merge、push、release、deploy 或任何外部副作用。
- 完成声明必须引用本次实际运行的当前验证结果。

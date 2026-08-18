# Execution Unit: greeting-01

```text
id: greeting-01
goal: 空白用户名使用 guest 作为问候名称
spec_reference: SPEC-1
completion_condition: greet("") 和 greet("   ") 都返回 "Hello, guest!"；非空用户名行为保持不变
dependencies: none
constraints:
  - 仅修改本 fixture 内与当前 Unit 直接相关的实现/测试
  - 使用现有 Repository verification command
  - 不执行 Integration 行为
```

## SPEC-1

系统提供 `greet(name)`：

- 对非空名称，去除首尾空白后返回 `Hello, <name>!`；
- 当名称为空字符串或只包含空白字符时，返回 `Hello, guest!`。

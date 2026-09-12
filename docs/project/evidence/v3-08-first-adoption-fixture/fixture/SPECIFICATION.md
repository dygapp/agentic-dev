# Audit Event Persistence Specification

## Goal

为 Audit Event 形成 durable local persistence，使后续 Technical Planning 可以选择可恢复、可查询且无需外部托管服务的方案。

## Required behavior

- Audit Event 必须持久保存到 Consumer 本地可写文件系统；
- 必须支持按时间范围读取；
- 单次写入失败不得静默报告成功；
- 重启后已有事件仍可恢复。

## Consumer-specific constraints

- **禁止依赖外部 managed database / managed storage service。**
- Consumer 运行环境提供可写本地文件系统。
- 具体 persistence implementation 属于 HOW；本 Specification 不预先指定 H2、SQLite、JSONL 或其他实现。

## Completion boundary

Technical Planning 必须在不覆盖上述 WHAT / WHY 与 Consumer-specific constraints 的前提下比较合理本地方案，并明确推荐、风险和后续验证边界。
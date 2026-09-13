---
id: rule:async-operation-bounded-observation
type: rule
status: active
scope:
  phases: []
  activities: [external-operation]
  technologies: []
  artifacts: []
  risks: [asynchronous]
---

# 异步操作有界观察

触发工作流、部署、远程任务等异步操作只表示请求已接受，不代表验证完成。当前目标包含取得执行结果且环境能够继续观察时，应在授权范围内持续重新读取状态、收集必要证据并处理可修复失败。

观察必须有合理轮询间隔和停止上限。终态、真实 blocker 或达到有界观察上限都可以结束闭环；后两者只能报告为受阻或未完全验证，不能伪装成完成。
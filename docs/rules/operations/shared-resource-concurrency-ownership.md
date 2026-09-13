---
id: rule:shared-resource-concurrency-ownership
type: rule
status: active
scope:
  phases: []
  activities: [external-operation]
  technologies: []
  artifacts: [shared-resource]
  risks: [concurrency, shared-resource]
---

# 共享资源并发与归属

当多个运行任务可能争用固定域名、代理名、端口、部署槽位、临时数据库、单例服务或受限账号时，并发边界必须匹配真实共享资源，而不是只按 PR、分支或运行编号分组。

资源取得、续期、释放、接管和清理必须保留可观察 owner / lifecycle，并在变更后重新验证当前归属与目标状态。不得盲目清理生产资源、有效人工复核资源或其他所有者的共享状态。
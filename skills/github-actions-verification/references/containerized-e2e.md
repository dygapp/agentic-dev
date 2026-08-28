# 容器化 E2E 与预构建 Runtime

## 目的

当 GitHub Actions 需要同时验证前端、后端、数据库、浏览器或其他 Runtime 时，本参考提供一种降低重复环境准备成本的通用 Pattern。

多容器不是目标本身。只有当不同 Runtime 的依赖、生命周期或诊断边界值得独立时才拆分。

## 验证分层

优先将验证分成：

```text
Fast Feedback
├─ backend compile / unit tests
├─ frontend type-check / build
└─ targeted checks

        ↓ PASS

Completion Verification
└─ runtime / integration / browser E2E
```

局部修复迭代优先取得低成本反馈；最终 Completed 前仍必须执行 Completion Condition 所要求的完整验证。

## Build 与 Runtime 分离

当构建产物可以跨 Job 复用时，推荐：

```text
Backend Verify
→ backend artifact

Frontend Verify
→ frontend artifact

Completion E2E
→ consume artifacts
→ start runtime only
```

避免在 E2E Job 中重复完成已经成功的完整编译流程。

## 多 Runtime 拓扑

复杂 Web Consumer 可以考虑：

```text
Database service/container
        │
        ├─ Backend runtime + backend artifact
        ├─ Frontend HTTP runtime + frontend artifact
        └─ Browser verification runtime
```

是否拆分、拆成几个容器，由当前系统边界和验证成本决定，不固定数量。

## 镜像来源优先级

稳定基础 Runtime 优先考虑：

1. 官方或 Vendor-maintained 预构建镜像；
2. 当前平台可稳定访问的可信 Registry；
3. GitHub Actions service containers；
4. Consumer 自有薄封装镜像；
5. 只有确有必要时才在每次 CI 从头构建完整 Runtime。

在 GitHub Actions 中，常见来源包括：

- GHCR（GitHub Container Registry）；
- MCR（Microsoft Container Registry）；
- Docker Hub；
- 其他 Repository Policy 允许的 Registry。

不要为了“统一 Registry”把本来由 Vendor 稳定维护的官方镜像重新复制一份。

## 浏览器验证

如果浏览器测试框架提供官方预构建镜像，优先评估直接使用该 Runtime，而不是每次运行都在线安装浏览器及系统依赖。

需要检查：

- package 与 image 版本兼容；
- browser binary 与 test runner 匹配；
- 当前 GitHub-hosted runner / container architecture 支持；
- Repository Policy 和安全边界允许。

## 数据库与服务依赖

对数据库、缓存、消息系统等稳定依赖：

- 优先使用 service container / 官方镜像；
- 设置明确 health check；
- 不把“container started”等同于“service ready”；
- E2E 失败时保存必要服务状态和日志。

数据库 Migration 发生变化时，如果当前 Runtime 能提供干净数据库，应在最终验证中执行完整初始化链：

```text
Fresh Database
→ Full Migration Chain
→ Application Startup
```

已有数据库上的增量执行仍可作为补充证据，但不能替代新环境初始化证据。

## Consumer 自有镜像

只有当：

- 官方镜像无法满足固定依赖；
- 环境准备仍然显著昂贵；
- 多个 Workflow / Consumer 长期复用同一薄层配置；

才考虑维护 Consumer 自有镜像。

自有镜像应保持薄、可追溯、可更新，避免构建包含所有工具的万能 Runtime。

## Automated Verification 与 Human Review 状态隔离

同一 Workflow 同时承担自动 E2E 和人工评审环境时，优先分离状态生命周期：

```text
Automated E2E
→ collect reports / traces / screenshots
→ recreate database and restore versioned assets
→ seed explicit Human Review fixtures
→ expose review runtime
```

人工评审环境应能说明：

- 当前数据库和静态资源来自哪个已知基线；
- 哪些数据是明确的 Human Review Fixture；
- 自动测试创建的数据、导航、文件、缓存和会话是否已经清除；
- Reset 后的服务健康、关键入口和外部访问路径是否重新验证。

除非 Consumer Repository 明确将自动测试数据采纳为人工示例数据，否则不能直接暴露测试结束状态。

## Bind Mount Ownership 与可重复恢复

容器可写 host bind mount 时，容器内 UID / GID 可能在 runner 文件系统留下普通用户无法删除或覆盖的文件。设计 Reset 时应显式确认：

- 哪个 Runtime 创建文件，以及最终 ownership / permissions；
- 清理动作由哪个已授权身份执行；
- 是否需要在容器内清理、固定 UID / GID、调整 mount 模式，或采用其他当前平台允许的恢复方式；
- 清理后是否重新复制或重建版本化基线；
- 相同 Reset 能否再次执行并得到同一已知状态。

`rm -rf` 命令被调用不构成 Cleanup Evidence。应重新检查目标路径、预期基线内容和后续 Runtime 启动结果。

这些规则只用于已授权的临时验证 / 评审环境，不授予生产数据或共享状态的破坏性清理权限。

## 非目标

本参考不要求：

- 所有 CI 使用 Docker；
- 所有 E2E 使用四个容器；
- 所有镜像都来自 GHCR；
- GitHub Actions 承担生产 Deploy；
- 为每个 Execution Unit 单独设计一套容器拓扑。

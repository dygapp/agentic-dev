---
id: research:methodology-guide-bootstrap-navigation-evidence
type: research
status: active
distribution: source-only
---

# Guide / Bootstrap / Navigation 验证 Evidence

## 1. 目的

本文记录产品边界重构 Gate P3 的 runtime Evidence，验证新的 Guide 模型是否能够在不恢复旧 Method / Rule / Architecture Consumer Runtime 的前提下，支持：

1. greenfield 软件项目从最小输入完成 Bootstrap；
2. Consumer 建立薄 `AGENTS.md`、最小项目知识和 exact-version Guide locator；
3. 标准安装 15 个 canonical Skills；
4. AI 基于 Consumer 当前事实 + `choosing-next-step` Guide 选择**一个**当前主要下一责任；
5. Guide 服务人和 AI 的按需导航，但不成为 ordinary task 固定上下文或 Skill procedure 的第二套 Authority。

P3 Guide exact subject：

`b121860682af36f4de72a69ea878d2abe98b0b95`

所有方法导航判断都绑定这一 exact subject。

## 2. 静态 Guide 边界

P3 candidate 对正常 Guide 路径完成了以下静态检查：

- Guide 文件数：17；
- 主要入口 Guide：11 / 11 存在；
- local Markdown link：无缺失；
- 除两个明确过渡资产外，正常 Guide 路径不存在：
  - `Human View` 作为 Human-only 定位；
  - `method:` Consumer runtime locator；
  - `architecture:` Consumer runtime locator；
  - `installed Release` / `Consumer Release`；
  - `agentic-dev-release-inputs`。
- `rule-activation-guide.md` 与 `consumer-local-rule-activation.md` 仍只作为 Provider 旧 Rule / Rule Discovery 过渡资产保留，P4 决定最终最小 Consumer-local constraints 机制后再 retire / absorb。

新入口包括：

- `getting-started.md`
- `bootstrap-new-project.md`
- `choosing-next-step.md`
- `consumer-local-constraints.md`
- `adopting-agentic-dev.md`
- `upgrading-agentic-dev.md`

## 3. Greenfield Bootstrap fixture

### 3.1 初始输入

Consumer 初始目录：

`/tmp/agentic-dev-p3-greenfield`

开始时为空目录。

Provider 使用本地只读 exact snapshot：

- path：`/tmp/agentic-dev-p3-provider`
- exact subject：`b121860682af36f4de72a69ea878d2abe98b0b95`
- local immutable eval tag：`p3-eval-b121860`
- Guide entry：`docs/guides/getting-started.md`

项目输入只给出：

- 20～50 人内部客服团队使用的 Web 工单系统；
- 用户：客服人员、客服主管；
- 核心目标：记录问题、创建工单、分配负责人、更新状态、条件查询；
- 非目标：计费、实时聊天、CRM 营销自动化；
- 技术约束：Kotlin / Spring Boot、Vue 3 / TypeScript、PostgreSQL；
- SSO provider 尚未确定，但不是 Bootstrap blocker；
- 不要求现在建立完整 Requirement Baseline / Architecture / 全部 Feature。

### 3.2 AI 实际建立的 Consumer

Bootstrap Agent 没有提出额外人工问题，直接形成：

```text
AGENTS.md
README.md
docs/project/overview.md
.agents/README.md
.agents/skills/<15 skills>/SKILL.md
skills-lock.json
.git/
```

关键结果：

- git Repository 已初始化；
- 根 `AGENTS.md` 只保存项目事实入口、Skills locator、Guide locator 与少量稳定工作边界；
- 没有复制 Provider Guide / Method / Rule / Architecture 正文；
- `docs/project/overview.md` 只保存用户明确给出的 Goal、Actor、Scope、Out of Scope、技术硬约束和 current state；
- 未自行决定 SSO provider；
- 明确记录“尚未形成 Requirement Baseline”，没有伪造完整需求；
- `.agents/README.md` 记录 exact subject / eval tag / Guide root / Guide entry；
- 15 个 Skills 全部安装到 repository-local `.agents/skills/**`；
- `skills-lock.json` 包含 15 个 Skill hash。

本场景使用本地只读 Provider snapshot 以隔离 P3 Guide orchestration，因此 lock 的 `sourceType` 为 `local`。GitHub immutable-tag 标准安装能力已经由 P1 独立证明；P3 不重复把本地 fixture transport 冒充正式远端 provenance。

### 3.3 Deterministic artifact check

独立 deterministic check 验证：

- `.git` 存在；
- `AGENTS.md` / `README.md` / `docs/project/overview.md` / `.agents/README.md` / `skills-lock.json` 均存在；
- repository-local Skill 数 = 15；
- locator 包含 exact subject `b121860682af36f4de72a69ea878d2abe98b0b95`；
- locator 包含 `p3-eval-b121860`；
- current state 指向 `establish-requirement-baseline`；
- Consumer 没有复制 Provider `docs/guides`、`docs/methods`、`docs/rules`、`docs/architecture`。

结果：

`PASS`

### 3.4 Codex native discovery

在 bootstrap 后的 Consumer 目录启动 Codex App Server，并调用 native `skills/list`：

- repo-local Skill 数：15；
- enabled：全部 true；
- errors：[]。

结果：

`PASS`

### 3.5 Bootstrap Agent 终态 limitation

第一次完整 Bootstrap Agent Job：

`abdfb0f0-8a13-4e22-b102-5aec09f533ca`

在已经真实建立全部上述工件后仍长期没有返回 stdout / terminal response，因此在约 363 秒时按有界观察原则停止。

这意味着：

> 不能声称该次 Agent process 正常返回“完成”终态。

但这也不等于 Bootstrap 工件失败。

随后使用独立只读收口 Runtime：

`162e4efa-df85-44cc-89e3-23f0607ae3f8`

重新读取 Consumer 工件和 exact Guide，exit 0，并确认：

- Bootstrap completion boundary 已满足；
- 根 `AGENTS.md` 足够薄；
- 15 Skills 已安装；
- exact Guide locator 已建立；
- 下一责任是 `establish-requirement-baseline`；
- 当前不应直接编码。

因此 P3 对该场景只做以下有界声明：

> **Bootstrap 目标工件和方法导航行为已验证；首次长任务的 Agent terminal response 存在 Runtime / infrastructure limitation，不能把该次 process 描述为正常终态成功。**

该 limitation 不由 Guide 语义 Evidence 解释成 PASS，也不要求通过增加新的 Bootstrap Runtime Framework 绕过。

## 4. “下一步做什么”三类场景

三组场景都只允许读取：

- Consumer `AGENTS.md`
- Consumer `docs/project/state.md`
- exact Provider `docs/guides/choosing-next-step.md`

不得读取其他 Provider 文档，不修改文件。

### 4.1 Requirement Baseline 不成立

Runtime Job：

`d9b2f843-05c0-460e-9104-fa802711afca`

Consumer facts：

- 原始访谈、表格、邮件分散；
- 同一访问权限规则冲突；
- 没有唯一 Requirement owner；
- 多个 Feature 都重复询问同一权限事实；
- 尚无 Requirement Baseline。

Observed next responsibility：

`establish-requirement-baseline`

Agent 同时明确：

- 当前不是 `clarify-architecture`；
- 不应逐 Feature 写 Specification / Execution Unit / 编码；
- Requirement owner 与冲突关闭后再重新判断。

Runtime exit：

`0`

### 4.2 Requirement 足够，但存在 systemic architecture blocker

Runtime Job：

`6b846202-aae3-42b5-bc82-16f9e7455521`

Consumer facts：

- Requirement 已稳定：全系统使用同一个当前业务年度；
- 三个 Feature 都持续依赖；
- 当前实现来源已经分叉；
- 未决的是稳定数据来源和责任边界，而不是产品规则。

Observed next responsibility：

`clarify-architecture`

Agent 同时明确：

- 当前不是 `establish-requirement-baseline`；
- 不应先实现第三个 Feature 的请求参数方案；
- Architecture owner 稳定后再判断 Feature responsibility。

Runtime exit：

`0`

### 4.3 Requirement / Architecture 足够，可进入普通 Feature development

Runtime Job：

`07d121e3-712a-409b-b033-a74d65083f89`

Consumer facts：

- Requirement Baseline 稳定；
- 当前 Feature Goal / Scope / 用户可见行为明确；
- Architecture 已覆盖聚合、权限和审计责任；
- 没有新的跨 Feature systemic driver；
- WHAT / WHY / Acceptance Specification 尚未形成。

Observed next responsibility：

`specify`

Agent 同时明确：

- 当前不需要 `clarify-intent`；
- 不应提前进入 Technical Plan、Execution Unit 或编码；
- Specification Ready 后再判断 `technical-plan` 或 `slice-work`。

Runtime exit：

`0`

运行期间 Codex model manager 曾报告一次 model-refresh timeout diagnostic，但该场景本身正常完成并返回 exit 0；该 stderr 不作为方法论语义失败。

## 5. P3 当前结论

当前 Evidence 支持以下结论：

1. Guide 可以同时服务人和 AI 的按需导航，不需要恢复 Human-only 定位；
2. Guide 不需要成为 ordinary task 固定上下文；
3. Greenfield AI 可以从少量项目输入 + exact Provider Guide 建立最小 Consumer Repository；
4. Bootstrap 没有因为 SSO provider 等普通后续设计问题继续追问；
5. Bootstrap 可以建立薄 `AGENTS.md`、最小 Project Knowledge、15 Skills 和 exact Guide locator；
6. 普通 Consumer 不需要复制 Provider Method / Architecture / Rule corpus；
7. `choosing-next-step` 能根据三类不同 Consumer state 给出不同的单一主要责任，而不是运行固定状态机；
8. Requirement / Architecture 足够时，方法导航能够进入普通 Feature Development；
9. Guide 负责选择责任，真正执行仍返回 installed Skill；
10. Consumer-local constraints 的具体发现机制仍保持 P4 open，不在 P3 提前冻结。

P3 的剩余门禁是：

- 对 exact candidate 做 Fresh Independent Semantic Review；
- 只有 `Blocking=0`、`Medium=0` 后，才允许 Roadmap 进入 P4。

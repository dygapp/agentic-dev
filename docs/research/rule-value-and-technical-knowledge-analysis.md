---
id: research:rule-value-and-technical-knowledge
type: research
status: active
distribution: source-only
---

# 技术规则的必要性与增量价值分析

研究日期：2026-09-17。

本文提供可复用的规则价值评估方法，并以 `agentic-dev` 当前 Vue 规则及其他规则为样本。本文是非规范性研究；处置建议不改变现有 Rule、Discovery、Consumer policy 或验证义务。

## 1. 核心结论

**当前 Vue 规则值得保留一部分约束，但没有充分证据证明七个独立文件中的全部内容都必须长期存在。更合理的方向是保留项目决策和高损失约束，压缩技术知识摘录，通过工具与行为评测证明剩余规则的价值。**

对问题的直接回答如下：

| 问题 | 结论 | 判断边界 |
| --- | --- | --- |
| 大模型自身能力是否覆盖现有 Vue 规则？ | 对具备较强 Vue 能力的模型，基础知识很可能大量重合；不能据此认定所有模型在真实任务中都会稳定执行 | 本次没有进行无规则对照实验，不能给出覆盖率或缺陷下降率 |
| 有规则后能否省去查技术资料？ | 可以减少对已确认、稳定知识的重复检索，不能免除版本、陌生 API、兼容性和异常行为的按需核验 | 当前七条规则不是完整技术手册，也没有要求每次 Vue 生成都重新联网 |
| 官方资料是否能完全覆盖这些规则？ | 已核对资料覆盖主要 Vue 技术事实和不少官方推荐；不能决定 Consumer 的兼容承诺、变更权限和完成证据要求 | “文档包含知识”和“任务必然检索并正确执行知识”是不同问题 |
| 缺少规则是否会产生漂移？ | 存在偏好不一致、版本混用、生命周期错误和完成声明失真的风险；是否发生、增加多少尚未实测 | 合法实现差异不是天然的质量漂移；只有违反已接受目标或增加真实成本才值得约束 |
| 其他规则如何判断？ | 授权、语义所有权、当前证据与项目约定通常比通用技术提示更难被模型和官方文档替代 | 这证明语义有价值，不自动证明每条语义必须拥有独立 Rule 文件 |

推荐优先次序：保留并验证类型证据与异步正确性约束；精简组件与生命周期规则；优先评估工程配置规则的载体，以及 Vue 浏览器验证规则与通用证据规则的重复。暂不按“模型应该知道”批量删除规则。

## 2. 范围、来源与证据强度

### 2.1 本次审阅范围

仓库分析基线为 `master@b1d9cbfde4ea88f736760c7140aba0f978788de7`，已通过 GitHub 默认分支与分支接口核对，与本地 HEAD 一致。审阅该基线下全部 27 条 Rule：Vue 7 条、TypeScript 1 条、通用生成 2 条、验证 6 条、仓库治理 5 条、外部操作 6 条。

这次全量阅读用于用户明确要求的规则价值研究，不是普通任务的启动方式或运行时加载建议。Rule locator 来自 Discovery 输出；跨任务研究集合不代表 27 条规则同时适用于报告编写。报告写入前另以当前文档责任执行 task-level discovery，适用规则为面向人的内容完整性。

GitHub Open Issue / PR 已重新读取；未合入默认分支的能力不纳入本报告规则基线。本文不维护 live Gate 或 Open Issue / PR 清单。

主要仓库依据：

- [Project Charter](../project/project-charter.md)：有界上下文、选择性采用和证据驱动演进。
- [Rule Architecture](../architecture/rule-architecture.md)：条件性约束、任务级粒度、Consumer specialization 与 admission。
- [Rule Discovery Architecture](../architecture/rule-discovery-architecture.md)：发现与语义确认的运行边界。
- [既有 Vue 技术研究](vue3-typescript-profile-analysis.md)：形成规则的历史技术依据；其中历史版本不作为当前 Consumer 版本事实。
- [现有评估说明](../../evals/README.md)及 [V4 判别语料](../../evals/discovery/v4-discriminating.json)：已设计的评估对象与证据边界。

Vue 官方资料从官方 `vuejs/docs` 仓库读取，固定快照为 [`40aa88af0094f7bab4aaf786e55c748a6a251d88`](https://github.com/vuejs/docs/tree/40aa88af0094f7bab4aaf786e55c748a6a251d88)，提交日期为 2026-09-15。章节与链接见第 10 节。该快照是文档证据，不代表任一 Consumer 已安装的版本。

### 2.2 已证明与未证明的内容

| 证据层次 | 本次能支持的判断 | 本次不能支持的判断 |
| --- | --- | --- |
| 规则正文对照 | 规则表达了什么、是否重复、条件和例外是否清楚 | 真实生成中一定被遵循 |
| 官方文档对照 | 主要 Vue 技术事实已有外部来源；短规则未覆盖完整语义 | 仅靠检索一定能找到全部相关条件 |
| 现有评测材料审阅 | 当前材料主要检验 Discovery、激活、指定场景行为及规模成本 | 当前七条 Vue Rule 相对“无规则”或“仅文档”的因果收益 |
| 本文风险分析 | 可构造怎样的失败机制、哪些义务无法由技术文档决定 | 各模型的实际失败概率、规则收益或最佳文件数 |

现有 V4 场景覆盖过 props / `v-model` 和 build 不等于类型检查等行为，不能因此否认已有行为验证价值；但其评价包含“发现并应用规则”，不是控制其他条件后的规则必要性实验。已有 PASS 也不能外推为本次已重新运行模型评测。

本次完成静态语义分析和官方资料核对，未执行多模型消融实验，未运行 Consumer Vue 应用。下文“高、中、低”都是相对价值判断，不是实测分数。

## 3. 评估方法：先分清规则究竟在承担什么责任

### 3.1 四种内容应分别评价

| 内容类型 | 示例 | 模型或资料能否替代 | 合适的长期位置 |
| --- | --- | --- | --- |
| 技术事实 | `watchEffect` 的同步依赖追踪 | 通常可以提供知识；精确行为仍受版本约束 | 官方资料、依赖源码、类型定义、按需技术参考 |
| 项目决策 | 优先 `<script setup>`，保留稳定组件契约 | 模型能提出选项，不能替项目决定已经接受哪一种 | Consumer Rule、已有技术约定或 Architecture 中的真实决策 owner |
| 正确性约束 | 过期请求不能覆盖当前选择 | 模型可能知道处理方式，技术手册不能证明当前实现满足业务需要 | 简短风险规则、行为测试与审查 |
| 完成与授权要求 | 类型责任必须有当前证据；工具可写不等于已授权 | 文档不能授予权限，也不能替代本项目的完成判据 | Rule、Method / Authority 中相应责任与执行门禁 |

同一文件可以合理组合这些内容，但应知道每段的增量价值来自哪里。把官方推荐改写成“必须”，不自动产生新的治理价值；把项目选择描述成“框架唯一正确方式”，反而容易误导。

### 3.2 “模型知道”不足以单独决定去留

至少要区分五种能力：能解释知识、能在题目明确提示时应用、能自主识别隐蔽风险、能在长上下文中持续遵守、能用合适证据证明完成。

一个模型能准确回答 watcher 清理问题，不等于它在同时修改组件、路由和请求状态时一定检查乱序响应。相反，如果类型检查或现有测试已经可靠发现问题，额外提示可能只增加重复上下文。

规则的候选净价值可以按以下问题评估，而不需要虚构数值评分：

1. 在现有模型、代码惯例和工具之上，它还能减少什么具体错误？错误损失有多大？
2. 它是否保存了模型无法推断的项目选择、授权或验收义务？
3. 它是否能在正确任务中被发现，并足够清楚地指导行动？
4. 同一责任是否已由更可靠的配置、测试、权限控制或其他 owner 覆盖？
5. 它带来多少检索、上下文、维护、过期和误激活成本？

**知识重复不等于约束冗余；语义有价值也不等于独立文件有价值。** 去重必须同时检查技术事实、规范责任和运行时成本。

### 3.3 对“漂移”的工作定义

本文把漂移定义为跨任务、上下文或版本后偏离已接受契约，或产生无法接受的质量差异。仅仅使用不同但合法的 Vue 写法，不自动构成漂移。

例如 Consumer 没有统一 `ref` 命名或组件风格的要求时，多种合法风格可能只是偏好差异；父子数据契约改变、旧请求覆盖新结果、跳过必要类型验证则是可观察的正确性或治理问题。

## 4. Vue 七条规则的逐项评估

七个文件当前合计 4,287 个字符，包含 front matter；这不是 token 数，也不等于单次任务实际加载量。它们已经相当简短，因此优化重点应是独立责任与实际触发效果，不是为了减少文件数强行合成大规则。

| 当前 Rule | 与模型知识／官方资料的重合 | 真正的增量价值与缺失风险 | 建议 |
| --- | --- | --- | --- |
| [组件编写](../rules/technology/vue/component-authoring.md) | 高。`script setup`、单向 props、声明方式、`defineModel` 都有官方依据 [V1–V3] | 固定默认风格，并保护现有自定义契约、运行时验证责任与变更范围；缺失时可能发生无必要 API 迁移 | **保留决策、精简知识。** Consumer 已有等价组件约定时复用该 owner；不必重复维护 |
| [响应式设计](../rules/technology/vue/reactivity.md) | 高。computed 纯派生、`reactive<T>` 提醒、composable 返回 refs 均见官方资料 [V4–V6] | 对隐蔽副作用和解构失活提供检查提示；部分错误不会被类型系统捕获 | **条件保留，优先检验工具替代。** computed 静态检查与行为测试已覆盖时，可以缩减重复说明；不要把官方推荐泛化为绝对禁用 |
| [Watcher / effect](../rules/technology/vue/watchers.md) | 技术事实重合高；自主发现风险的稳定性未知 [V7] | 乱序响应、失效订阅和 timer 泄漏可能造成真实业务错误；“无风险不机械 cleanup”也约束过度实现 | **优先保留风险约束。** 短规则提醒检查依赖和 stale work，具体 API 按版本查证；以乱序完成和卸载测试证明效果 |
| [Template refs](../rules/technology/vue/template-refs.md) | 高。API、自动推断条件、可空生命周期均有官方依据 [V6、V8] | 防止 non-null assertion 隐藏挂载／卸载问题，避免无意义 `nextTick` | **保留生命周期约束，弱化 API 偏好。** `useTemplateRef` 是条件默认，不能替代版本及语言工具兼容核验 |
| [工程配置](../rules/technology/vue/project-configuration.md) | 高。官方脚手架与 `@vue/tsconfig` 已提供配置参考 [V9] | 选择可信起点、限制普通功能变更扩大为配置迁移；大部分边界可由现有技术约定和实现纪律承担 | **独立 Rule 必要性较低。** 优先评估让 Consumer 配置及既有技术约定承载；若新建工程任务确有独立发现收益，可保留薄默认，无需新建 Skill |
| [Vue 类型检查](../rules/technology/vue/typecheck.md) | 技术事实重合高，官方明确区分 transpilation 与 type-check [V9] | 规定“不能用 build 成功证明类型责任”；这是证据与完成问题，损失可能跨越所有 SFC | **优先保留，落实到脚本和 CI。** 以实际执行机制为准；已有 build script 确实包含相应类型检查时，不重复运行同一检查 |
| [浏览器／视觉验证](../rules/technology/vue/browser-verification.md) | 官方测试资料能解释验证层次 [V10]；正文几乎没有 Vue 独占语义 | 保证交互、DOM、竞态与视觉 claim 获得对应证据；缺失会放大“静态检查通过即全部完成”的误判 | **优先评估合并或退役独立文件。** 通用证据规则覆盖原则、视觉规则覆盖 fidelity；交互／DOM／异步的具体判定仍须有可靠承载处，不能直接丢掉 |

### 4.1 哪些是需要保护的项目选择

组件规则中的“默认优先”和“不改写已有稳定契约”，比再解释一遍 `defineModel` 更有项目价值。官方资料可以推荐新 API，却不知道某个组件库是否承诺旧事件名、是否要支持低版本，或者当前工作是否包含迁移授权。

但其中的范围保护与[实现纪律](../rules/generation/implementation-discipline.md)也有重合。后续精简宜让通用 owner 持有范围原则，Vue Rule 只保留有助于当前技术判断的短例外，避免形成两份可分别演进的完整 policy。

### 4.2 哪些知识可能更适合工具保证

直接修改 props、部分 computed 副作用、显式 `any`、空值访问等，可以用已配置的 ESLint、TypeScript 或 Vue-aware type-check 捕获一部分。配置强制执行通常比依靠模型记得一句话更稳定。

不过，静态检查未必识别请求时序错误、隐藏的间接副作用、被断言绕开的空值问题，或当前 API 变更违反 Consumer 兼容承诺。工具覆盖要以实际配置和失败样例证明，不能因为某插件存在就假设已覆盖。

工具也有自己的语义漂移风险：陈旧断言不应高于当前契约。减少文字规则时，仍需保留验证机制的 owner、适用条件与更新责任。

### 4.3 为什么不直接把剩余规则全部合并

现有组件、响应式、watcher、template ref 有重叠，但也有不同风险和独立消费场景。工程配置只应在配置责任中出现；类型检查和浏览器验证属于另一类验证责任。

应先观察代表性任务的候选集合和总加载量：哪些规则总是一起消费、哪些经常无关命中、哪些风险尚未知而漏用。只有共同消费证据支持时再合并，不能由目录相邻推导出相同责任。

## 5. 技术资料与 Rule 的替代关系

### 5.1 不需要每次生成都重复联网，但必须掌握当前事实

本次审阅的七条 Vue Rule 没有规定“每次写 Vue 都先查询外部文档”。合理策略是：先掌握当前 Consumer 的版本、已有代码、契约及验证脚本；只对影响当前判断的不确定性补充查证。

| 当前情形 | 资料策略 | 原因 |
| --- | --- | --- |
| 沿用已验证模式，小范围修改稳定 API | 可以直接实施并验证；不必为相同知识重复联网 | 当前代码、已读资料和工具反馈可能已足够 |
| 首次采用 API、版本不清楚、跨 minor／major 兼容 | 核对 lockfile、安装版本、匹配版本的官方文档／发布说明 | 模型记忆和“最新文档”都可能与目标版本不同 |
| 遇到推断、编译宏、响应式或异步行为疑问 | 查官方相关章节，必要时看类型定义、源码或最小复现 | 短规则只给出约束，不能解释全部机制 |
| 第三方组件库、SSR、特殊构建链 | 补充对应依赖资料和项目 Architecture | 当前 Vue Rule 没有覆盖这些完整责任 |
| type-check／build／运行时相互矛盾 | 依据实际工具版本定位问题，核验后取得相应证据 | 不能用另一个成功检查替代失败责任 |

“查资料”可以是读取本地类型定义、版本化文档和源码，并不必然是每次发起网页搜索。已确认资料可以在版本和相关假设未改变时复用；不能把过去确认过等同于永久有效。

### 5.2 当前规则不能替代资料的具体反例

以下不是要求给规则逐项补全文档，而是证明其边界：

1. **清理 API 有时机差异。** `onWatcherCleanup` 自 Vue 3.5 起可用，要求在同步执行阶段注册，不能放在 `await` 之后；回调参数形式的 `onCleanup` 与其约束不同。现有 watcher Rule 要求处理 stale work，但不完整规定这些 API 条件 [V7]。
2. **`defineModel` 有默认值陷阱。** 子组件定义 default，而父组件没有提供值时，可能造成父子不同步。现有组件 Rule 提供选择原则，没有展开此问题 [V3]。
3. **解构不能机械一概而论。** 普通 reactive object 的 property 解构与 Vue 3.5 对同一 `<script setup>` 中 `defineProps` 解构的编译处理不同；后者有响应式转换，传给外部函数时仍要检查传值与 getter 的差别 [V1、V2、V5]。这不表示现有 composable Rule 错误，而说明不能把其局部结论扩成“所有解构都会失活”。
4. **推断依赖工具链。** 静态 template ref 自动类型推断的官方说明同时涉及 Vue 3.5 与 Vue Language Tools 2.1；只看到 runtime 版本符合条件还不足以证明当前工具具备推断能力 [V6]。
5. **类型声明不等于没有运行时生成，也不等于完整运行时验证。** 宏可根据类型生成部分 runtime 声明，但受编译模式、可解析类型等条件限制；不能把它当作全部自定义 validator 或不可信输入校验的替代 [V1]。

规则保存这些问题的触发原则，比永久复制所有解法更可维护。

### 5.3 “每次查文档”能否完全取代现有规则

对纯技术知识，在资料准确、版本匹配、检索充分且模型正确理解的理想条件下，官方资料可以替代大部分摘录，而且通常更完整。因此纯摘录 Rule 没有天然不可替代性。

实际流程还要支付定位章节、辨认版本、筛选适用条件和重复阅读的成本，也可能漏检。Rule 可以作为经过项目接受的简短决策与风险提醒，但它本身也可能陈旧或错误激活，不能默认比资料更可靠。

技术资料无法替代这些事实：项目选择哪种合法方案、哪些旧契约必须兼容、当前允许改到什么范围、验收要求什么证据、由谁批准不可逆操作。即使完全移除 Vue 知识摘录，仍应从 Consumer Authority 获得这些信息。

更合适的组合是：**模型提供通用知识，项目 owner 保存已接受决策，按不确定性查证技术资料，工具和测试验证结果。** 三者是否节省成本，需要用真实任务测量，而不是预设每次必须查或永远不用查。

## 6. 缺少规则时的漂移，以及规则自身的漂移

| 漂移形式 | 无规则时可能出现的机制 | 现有规则能提供什么 | 仍需什么保证 |
| --- | --- | --- | --- |
| 选择不一致 | 不同任务选择不同组件 API 或配置风格 | 明确 Consumer 接受的默认和例外 | 只有项目确实要求一致时才约束；代码惯例与模板也可承担 |
| 版本混用 | 将训练中或最新文档中的 API 用到旧项目 | 提醒版本条件，避免盲目迁移 | lockfile、实际依赖、匹配版本的资料和编译检查 |
| 响应式／时序错误 | 解构失活、过期请求回写、卸载后使用 DOM | 在风险点提醒检查状态和生命周期 | 真实状态变更、乱序完成、挂载／卸载行为测试 |
| 验证不足 | 将 build 或静态通过扩大为类型／交互／视觉通过 | 限定完成声明可以依赖的证据 | 正确配置并实际执行当前验证机制 |
| 变更范围扩大 | 借新 API 推进无关迁移或配置重写 | 保存范围约束及兼容例外 | 差异审查与明确任务责任 |

缺失规则不必然导致漂移：模型、示例代码、类型系统、CI、组件契约或其他已生效规则可能承担相同责任。反之，规则存在也不保证不漂移：可能没有命中、被忽略、被误解，或者规则本身过时。

特别要防范规则的反向影响：把可选模式硬化成唯一写法、让已过期的技术事实优先于实际版本、对无风险代码机械加 cleanup／`nextTick`、为普通变更强制全套 browser／visual 测试。当前规则已经包含不少例外和条件，精简时应保留这些抑制误用的边界。

发现机制同样影响收益。当前 metadata 对不同受限维度共同匹配；风险尚未知时应按现有 contract 使用 `null`，不能误记为“明确无风险”的 `[]`。把风险识别能力不足导致的漏用误判为“Rule 没有效果”，会混淆发现质量与正文价值。反过来，全部加载也不能证明普通运行有效。

## 7. 其余 20 条规则的汇总评估

以下“保留”首先表示保留该语义；独立 Rule 是否最合适还要比较已有 owner 和实际发现收益。对其他技术或平台 API，本次没有进行与 Vue 同等深度的外部文档核对，判断主要基于当前正文的知识／policy／证据责任区分。

| 类别与当前 Rule | 模型／技术资料可覆盖的部分 | 不易替代的价值及缺失风险 | 建议 |
| --- | --- | --- | --- |
| TypeScript：[类型安全](../rules/technology/typescript/type-safety.md) | 推断、`unknown`、narrowing 都是常规知识 | 项目是否接受 `any`／assertion、公共边界如何表达；缺失时可能绕过类型责任 | 保留薄 policy；优先由 strict、lint、type-check 执行可判定部分；压缩教程 |
| 生成：[实现纪律](../rules/generation/implementation-discipline.md) | 简单设计、避免无关修改是常见原则 | 限定真实任务范围、抵制推测性复杂度；模型不能从一般知识推断本项目授权边界 | 保留；以差异是否有责任链评估，避免把原则解释成“代码越少越好” |
| 生成：[数据访问有界性](../rules/generation/data-access-boundedness.md) | 分页、窗口和缓存是常见技术 | 不全量读取增长集合，也不静默截断合法业务集合；需根据当前消费语义裁决 | 保留风险约束；用增长规模和集合完整性案例验证，不固定一种分页实现 |
| 验证：[证据匹配声明](../rules/verification/evidence-type-must-match-claim.md) | 模型能解释测试层次 | 定义何时有资格声称完成，约束夸大静态或局部证据 | 高优先级保留；作为通用证据原则，技术规则只补具体差异 |
| 验证：[跨提交证据复用](../rules/verification/evidence-claim-reuse-across-commits.md) | Git diff、CI 历史可从工具资料学习 | 哪些差异允许复用哪些 claim、需怎样追溯，属于治理决策 | 保留；避免一律重跑和一律沿用历史证据两个极端 |
| 验证：[验证契约当前性](../rules/verification/verification-contract-currentness.md) | 测试失败分析的一般方法 | 防止陈旧测试反向改写产品 Authority；框架手册不能提供当前正确 expected behavior | 保留；可自动发现部分过期引用，语义冲突仍需判断 |
| 验证：[视觉证据](../rules/verification/visual-evidence.md) | 视觉测试工具及截图比较方法 | 区分功能通过与 fidelity 通过；项目决定视觉义务和容差 | 保留独立风险价值；与 Vue browser Rule 去重时保留明确责任 |
| 验证：[数据库迁移证据](../rules/verification/database-migration-completion-evidence.md) | 迁移工具说明能提供运行方式 | 要求新库完整链和应用启动证据，避免只验证已有环境增量升级 | 保留并尽量自动化；严格保持 schema／初始化范围，不能冒充业务数据迁移完整验收 |
| 验证：[人工复核基线隔离](../rules/verification/human-review-baseline-isolation.md) | 隔离、重置、fixture 是常识 | 明确自动测试证据和人工复核环境的不同生命周期，避免展示污染数据 | 条件保留；消费者完全不共用环境时可不采用 |
| 治理：[面向人的内容完整性](../rules/repository/human-facing-content-integrity.md) | 模型会中文，也能保留代码标识 | 默认语言、精确机器身份和正式概念边界是本地约定 | 保留本地 policy；Consumer 自行选择语言，不传播中文为通用要求 |
| 治理：[Git commit 纪律](../rules/repository/git-commit-discipline.md) | Conventional Commits 的语法 | 本仓 type／scope、中文摘要、逻辑边界、Authority 顺序由本仓决定 | 保留；格式可交由工具检查，逻辑和语义顺序仍需审阅 |
| 治理：[高影响 AI 复核](../rules/repository/high-impact-ai-review-required.md) | 模型知道 review 方法 | 何种变更必须独立复核、复核不等于集成授权，是治理策略 | 保留触发 policy；不复制 `review-change` procedure，不扩大为普通任务固定门禁 |
| 治理：[权威产物生命周期](../rules/repository/authoritative-artifact-lifecycle-review.md) | 模型知道链接更新和文档维护 | Current owner 迁移、历史引用角色、下游验证消费者同步，无法由一般技术文档确定 | 高优先级保留；定向扫描辅助语义复核，避免以旧字符串出现直接判错 |
| 治理：[集成后状态闭环](../rules/repository/integration-state-closure-review.md) | README／Roadmap 编辑方法 | 避免集成后立刻过期的当前状态，以及不断追加状态修复 | 保留；与生命周期规则有相邻语义，只有共同触发且不会扩大无关加载时再合并 |
| 操作：[安全外部写](../rules/operations/safe-external-write.md) | API 调用和常见写后检查 | 授权来源、范围、最小变更与实际目标状态；工具文档不能授予行动权限 | 高优先级保留；可由权限控制和读取验证加固，不要求对已授权动作反复询问 |
| 操作：[跨仓库授权](../rules/operations/cross-repository-authorization.md) | 模型知道仓库是独立资源 | 防止把一仓权限扩展到另一仓，并使权限缺口只阻塞相应操作 | 保留；不同凭证／工具约束可以执行部分边界 |
| 操作：[异步有界观察](../rules/operations/async-operation-bounded-observation.md) | 轮询与终态概念 | 防止“请求接受即完成”，同时约束无限等待和无意义高频查询 | 保留；执行器可封装轮询，Rule 保存完成与停止语义 |
| 操作：[共享资源归属](../rules/operations/shared-resource-concurrency-ownership.md) | 锁、lease 和并发控制 | 保护真实资源 owner 和复核环境，防止按 PR 分组却争用同一资源 | 保留；具体资源事实和锁机制由 Consumer 配置、平台及当前状态提供 |
| 操作：[外部二进制验证](../rules/operations/external-binary-content-validation.md) | 文件签名、MIME、解码知识 | 把验证放在版本化或消费前，避免将 HTML 错页、伪扩展名交给运行环境 | 条件保留；优先以实际解析／解码自动化，不能认为改后缀等于格式转换 |
| 操作：[临时证据晋升](../rules/operations/temporary-evidence-to-persistent-input-promotion.md) | artifact 下载和持久存储方法 | 是否接受其为长期输入、来源与生命周期由当前 Authority 决定 | 保留；与产物 lifecycle 组合，不因上传成功自动取得长期地位 |

跨类别看，最值得压缩的是重复解释常见技术方法的内容；最值得保留的是模型和官方资料无法获知的本地决策，以及将某种证据与某种完成声明绑定的约束。

即使某个执行环境已有同等强度的系统级约束，重复 Rule 的收益也要在该环境中重新评价。`agentic-dev` 面向可选择采用的 Consumer，不能把当前平台的一项保障假定为所有 Consumer 的永久能力。

## 8. 建议的精简方向与落实顺序

### 8.1 先明确语义，再决定文件

| 建议层次 | 适用内容 | 可考虑的处理 |
| --- | --- | --- |
| 保留 policy／完成义务 | 兼容边界、stale work、类型证据、授权及 Current owner | 保留简短约束、适用条件、例外和可观察验证方式 |
| 工具承担可判定部分 | props mutation、部分类型违规、格式与脚本执行 | 检查实际 lint／CI 覆盖，用失败样例证明后压缩重复文字 |
| 资料承担可变技术细节 | API 版本、配置选项、宏限制、具体 cleanup 写法 | 按需读取版本匹配资料，不把 Rule 扩写成手册 |
| Consumer owner 承担本地选择 | 项目 scaffold、strict 强度、默认组件契约 | 复用已有技术约定或配置，防止另建重复 owner |
| 合并／退役候选 | Vue browser 通用责任、纯配置推荐、被工具完整覆盖的提示 | 先核对语义承接与激活路径，再以评测支持处置 |

### 8.2 有界的下一步

1. 先选择“Vue browser 与通用证据重合”“工程配置独立价值”两个候选，比较删除或收敛后还有哪些责任无人承担。
2. 保留当前其他 Vue Rule 作为基线，建立少量能观察真实缺陷和过度实现的任务，不先大规模改写 corpus。
3. 用下一节的对照评估比较当前规则、精简规则、仅按需文档三种实践效果，并计入工具已有保障。
4. 只有效果和责任承接都清楚时，才修改真实 Rule owner、相关测试与导航；按当前发现机制重新验证。本文不直接实施这些能力变更。

此顺序不要求新增集中规则目录、第二套路由表或“必须每次读官方文档”的全局 Rule。报告中的矩阵只是固定基线的研究样本，不应成为运行时 inventory。

## 9. 怎样用实验确认必要性，而非依赖直觉

### 9.1 对照组

所有组保持相同需求、项目约定、依赖版本、代码、工具检查和任务预算；只改变待评估 Vue Rule 与文档条件。必须移除对照组中复制自待评规则的提示，避免答案通过 fixture 或根指令泄漏。

| 组别 | 待评估 Vue Rule | 官方资料 | 主要问题 |
| --- | --- | --- | --- |
| A | 无 | 不提供额外外部资料；保留相同项目代码、类型定义和工具 | 当前模型加项目环境的基础能力如何 |
| B | 当前规则 | 与 A 相同 | 相对 A，规则本身增加了什么 |
| C | 无 | 可按需检索版本匹配资料 | 现实的文档检索能否替代规则 |
| D | 当前规则 | 与 C 相同 | 有文档条件下，规则是否仍有净收益 |
| E | 精简规则，只保留独有 policy 和高损失检查点 | 与 C 相同 | 能否以更低成本保持 D 的质量 |

纯技术正确性任务与项目 policy 任务应分开评分。项目选择在各组都作为任务事实提供，评价其执行稳定性；另行研究“把选择放在 Rule 还是已有 owner”的可发现性，不能让只有 B 组知道需求，再把 B 组正确归因为模型能力提升。

可增加“直接提供准确相关章节”的诊断条件，区分检索失败与理解／执行失败；它不是现实检索成本的替代。预算公平比较后，再以质量相当时的成本比较检验短规则是否节省时间。

### 9.2 最小的代表性任务集

建议先做以下试点；场景数量用于发现问题，不足以直接宣称统计结论：

1. 新建标准 `v-model` 组件；另设已有自定义事件不可迁移的反例。
2. 分别在支持与不支持相应 API 的 Vue 版本中修改组件，检查版本兼容。
3. `defineModel` 默认值与父组件未赋值组合，检查初始状态一致性。
4. composable 输出解构与 Vue 3.5 props 解构，防止机械套用同一结论。
5. async `watchEffect` 在 `await` 前后读取不同依赖，检查触发结果。
6. 搜索请求乱序完成及组件卸载，检查过期数据、清理和可观察错误。
7. `v-if` 反复挂载／卸载 template ref，检查空值处理和 DOM 时机。
8. Vite 构建成功但 SFC 存在类型错误，检查验证与最终声明。
9. 已有 build script 包含有效 type-check，检查是否机械重复执行。
10. 无 DOM／视觉责任的小修改，检查是否过度运行浏览器验证。
11. 修改既有工程普通功能，检查是否无授权扩大 strict／tsconfig 迁移。
12. 明确视觉还原要求，检查是否把交互成功误报为视觉一致。

### 9.3 评分与判定

主要指标应是行为正确性、兼容性、契约保持和完成声明真实性；次要指标包括无关修改、工具／资料调用数、实际上下文 token、耗时、失败重试与维护成本。运行是否念出规则、使用某个新 API、执行多少测试，都不能单独算成功。

测试应能区分错误实现与正确实现，例如控制请求完成顺序，而不是只检查源码含有 `cleanup` 字符串。风格类断言只在项目确实接受该风格时计分。加入无风险反例，测量规则造成的过度实现。

采用隔离新上下文、相同环境、多次重复；按实际拟支持的模型和版本记录结果，不从单一模型泛化。“会读资料”“会调用工具”和“最终行为正确”分别评分。评分者尽量不知道分组，不把标准答案交给生成者。

可据以下条件处置候选：

- D 稳定优于 C，且收益超过额外成本：保留相应规则语义。
- E 与 D 在约定容差内质量相当、成本更低：优先精简版本。
- 工具已稳定捕获同类问题，文字提示没有可辨增益：考虑工具承担、减少重复正文。
- 规则使合法兼容路径被拒绝、测试明显过度或无关迁移增加：修改适用条件或撤回偏好。
- 样本太少、罕见高损失风险未被覆盖：维持证据不足，不把“未观察到失败”当作可删除证明。

成本收益阈值、可接受缺陷容差和样本量应在正式实验前按 Consumer 风险确定；本报告不虚构统一阈值。

## 10. 官方资料与可追溯引用

下列技术对照均读取了相同官方文档快照。网页链接便于阅读；固定源码链接用于核对本文判断时的原文。其他规则的规范性来源为第 7 节逐项链接的仓库 Rule。

| 标记 | 官方章节 | 固定源码 |
| --- | --- | --- |
| V1 | [SFC `<script setup>`](https://vuejs.org/api/sfc-script-setup.html)：宏声明、响应式 props 解构、版本限制 | [源码](https://github.com/vuejs/docs/blob/40aa88af0094f7bab4aaf786e55c748a6a251d88/src/api/sfc-script-setup.md) |
| V2 | [Props](https://vuejs.org/guide/components/props.html)：单向数据流、对象嵌套属性、解构 | [源码](https://github.com/vuejs/docs/blob/40aa88af0094f7bab4aaf786e55c748a6a251d88/src/guide/components/props.md) |
| V3 | [Component `v-model`](https://vuejs.org/guide/components/v-model.html)：`defineModel`、默认值不同步 | [源码](https://github.com/vuejs/docs/blob/40aa88af0094f7bab4aaf786e55c748a6a251d88/src/guide/components/v-model.md) |
| V4 | [Computed](https://vuejs.org/guide/essentials/computed.html#getters-should-be-side-effect-free)：纯 getter | [源码](https://github.com/vuejs/docs/blob/40aa88af0094f7bab4aaf786e55c748a6a251d88/src/guide/essentials/computed.md) |
| V5 | [Composables](https://vuejs.org/guide/reusability/composables.html#return-values)：返回值、响应性和副作用 | [源码](https://github.com/vuejs/docs/blob/40aa88af0094f7bab4aaf786e55c748a6a251d88/src/guide/reusability/composables.md) |
| V6 | [TypeScript with Composition API](https://vuejs.org/guide/typescript/composition-api.html)：`reactive` 泛型、template ref 类型 | [源码](https://github.com/vuejs/docs/blob/40aa88af0094f7bab4aaf786e55c748a6a251d88/src/guide/typescript/composition-api.md) |
| V7 | [Watchers](https://vuejs.org/guide/essentials/watchers.html)：依赖追踪、cleanup、flush 与停止 | [源码](https://github.com/vuejs/docs/blob/40aa88af0094f7bab4aaf786e55c748a6a251d88/src/guide/essentials/watchers.md) |
| V8 | [Template Refs](https://vuejs.org/guide/essentials/template-refs.html)：API 与挂载／卸载语义 | [源码](https://github.com/vuejs/docs/blob/40aa88af0094f7bab4aaf786e55c748a6a251d88/src/guide/essentials/template-refs.md) |
| V9 | [TypeScript Overview](https://vuejs.org/guide/typescript/overview.html)：脚手架、配置与 type-check | [源码](https://github.com/vuejs/docs/blob/40aa88af0094f7bab4aaf786e55c748a6a251d88/src/guide/typescript/overview.md) |
| V10 | [Testing](https://vuejs.org/guide/scaling-up/testing.html)：组件、浏览器与端到端测试的责任和成本 | [源码](https://github.com/vuejs/docs/blob/40aa88af0094f7bab4aaf786e55c748a6a251d88/src/guide/scaling-up/testing.md) |

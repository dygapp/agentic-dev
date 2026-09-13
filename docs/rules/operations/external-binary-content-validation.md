---
id: rule:external-binary-content-validation
type: rule
status: active
scope:
  phases: [execute]
  activities: [external-operation, implementation]
  technologies: []
  artifacts: [binary, media]
  risks: [content-type]
---

# 外部二进制内容验证

从外部站点、接口、附件或其他仓库取得的二进制 / 媒体资源，文件名、扩展名、URL 后缀和响应头只能提供线索，不能单独证明真实内容类型。

在版本化或交给运行环境消费前，应按当前风险验证内容签名、真实媒体类型以及必要的可解码 / 可解析属性；格式不一致时不得只改扩展名伪装。转换后还必须重新验证生成物。
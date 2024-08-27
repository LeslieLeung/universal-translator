# Universal Translator

[English](README.md) | 简体中文

重构和优化过的使用反思工作流的智能翻译。

## 特性

- 使用反思工作流的智能翻译，灵感来自 [translation-agent](https://github.com/andrewyng/translation-agent)
- 重构以提高可读性和可维护性
- 添加并发以提高性能
- 添加使用情况跟踪以更好地控制成本
- 优化接口，使用更加简便
- 支持术语表和额外的翻译指令
- 支持其他大语言模型（OpenAI、Anthropic、Anthropic Bedrock，更多即将推出）

## 快速开始

您可以查看 [示例](examples/) 快速入门。

要运行示例，您需要有一个 OpenAI API 密钥，并在项目根目录下创建一个 `.env` 文件，内容如下：

```
OPENAI_API_KEY=<您的_openai_api_密钥>
```

使用 [poetry](https://python-poetry.org/) 准备环境：

```bash
poetry install
```

然后您可以使用以下命令运行示例：

```bash
python examples/translate_openai.py
```

## 使用方法

```python
from universal_translator.llm.openai import OpenAI
from universal_translator.translate.translation import UniversalTranslator

# 初始化大语言模型供应商
provider = OpenAI(api_key=openai_api_key, model="gpt-4o")
# 初始化翻译器
translator = UniversalTranslator(
    source_language="en", # 或 English
    target_language="fr", # 或 French
    llm_provider=provider,
    country="France",
)
# 翻译文本
translated_text = translator.translate(text)
```

## 高级用法

### 设置模型和温度

```python
# OpenAI
provider = OpenAI(api_key=openai_api_key, model="gpt-4o", temperature=0.3)
# Anthropic
provider = Anthropic(api_key=anthropic_api_key, model="claude-3-5-sonnet-20240620", temperature=0.3)
# Anthropic Bedrock
provider = AnthropicBedrock(access_key=access_key, secret_access_key=secret_access_key, model="anthropic.claude-3-5-sonnet-20240620-v1:0", temperature=0.3)
```

### 并发

您可以设置向大语言模型供应商发送的最大并发请求数。适当的请求并行化可以显著提高长文本翻译的性能。

但是，您不应将其设置得太高，否则可能会遇到大语言模型供应商的速率限制问题。

```python
translator = UniversalTranslator(
        source_language="en",
        target_language="fr",
        llm_provider=provider,
        country="France",
        max_concurrent_requests=10, # 默认为 5
    )
```

### 使用情况跟踪

```python
# 翻译一些内容
translator.translate(text)
# 获取使用情况
usage = translator.usage
# Usage: {'gpt-4o': Usage(total_tokens=1148, prompt_tokens=1034, completion_tokens=114)}
```

### 术语表

您可以添加术语表来帮助大语言模型保持某些特定词语或短语的一致翻译。

```python
translator = UniversalTranslator(
    source_language="en",
    target_language="fr",
    llm_provider=provider,
    country="France",
    glossary=[
        {"source": "hello", "target": "bonjour", "notes": "常见问候语"},
        {"source": "world", "target": "le monde"},
    ],
)
```

### 额外指令

您可以添加额外指令来帮助大语言模型进行翻译。

```python
translator = UniversalTranslator(
    source_language="en",
    target_language="fr",
    llm_provider=provider,
    country="France",
    extra_instructions="使用第三人称视角。"
)
```

## 致谢

灵感来自 [translation-agent](https://github.com/andrewyng/translation-agent)。本项目的核心代码从一个拥挤的 utils.py 重构而来，以提高可读性和可维护性。此外，它还添加了对术语表、额外指令的支持，以及未来对其他大语言模型的支持。

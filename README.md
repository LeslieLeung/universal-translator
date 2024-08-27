# Universal Translator

English | [简体中文](README_zh.md)

Agentic translation using reflection workflow, refactored and sugared.

## Features

- Agentic translation w/ reflection workflow, as purposed in [translation-agent](https://github.com/andrewyng/translation-agent)
- Refactored for better readability and maintainability
- Add concurrency for better performance
- Add usage tracking for better cost control
- Sugared interface for easy usage
- Support for glossary, and additional instructions for translation
- Support for other LLMs(OpenAI, Anthropic, Anthropic Bedrock, more to come)

## Quick Start

You can checkout the [example](examples/) for a quick start.

To run the example, you need to have an OpenAI API key, and a `.env` file in the root directory of the project with the following content:

```
OPENAI_API_KEY=<your_openai_api_key>
```

Prepare the environment using [poetry](https://python-poetry.org/):

```bash
poetry install
```

Then you can run the example using the following command:

```bash
python examples/translate_openai.py
```

## Usage

```python
from universal_translator.llm.openai import OpenAI
from universal_translator.translate.translation import UniversalTranslator

# initilize the LLM provider
provider = OpenAI(api_key=openai_api_key, model="gpt-4o")
# initialize the translator
translator = UniversalTranslator(
    source_language="en", # or English
    target_language="fr", # or French
    llm_provider=provider,
    country="France",
)
# translate the text
translated_text = translator.translate(text)
```

## Advanced Usage

### Set Model And Temperature

```python
# OpenAI
provider = OpenAI(api_key=openai_api_key, model="gpt-4o", temperature=0.3)
# Anthropic
provider = Anthropic(api_key=anthropic_api_key, model="claude-3-5-sonnet-20240620", temperature=0.3)
# Anthropic Bedrock
provider = AnthropicBedrock(access_key=access_key, secret_access_key=secret_access_key, model="anthropic.claude-3-5-sonnet-20240620-v1:0", temperature=0.3)
```

### Concurrency

You can set the maximum number of concurrent requests to the LLM provider. A proper parallelization of requests can significantly improve the performance of long texts translation.

However, you should not set it too high, otherwise, you may encounter rate limit issues from the LLM provider.

```python
translator = UniversalTranslator(
        source_language="en",
        target_language="fr",
        llm_provider=provider,
        country="France",
        max_concurrent_requests=10, # default is 5
    )
```

### Usage Tracking

```python
# translate something
translator.translate(text)
# get usage
usage = translator.usage
# Usage: {'gpt-4o': Usage(total_tokens=1148, prompt_tokens=1034, completion_tokens=114)}
```

### Glossary

You can add glossary to help LLM keep a consistent translation for some specific words or phrases.

```python
translator = UniversalTranslator(
    source_language="en",
    target_language="fr",
    llm_provider=provider,
    country="France",
    glossary=[
        {"source": "hello", "target": "bonjour", "notes": "A common greeting"},
        {"source": "world", "target": "le monde"},
    ],
)
```

### Extra Instructions

You can add extra instructions to help LLM with the translation.

```python
translator = UniversalTranslator(
    source_language="en",
    target_language="fr",
    llm_provider=provider,
    country="France",
    extra_instructions="Use third person perspective."
)
```

## Credits

Inspired by [translation-agent](https://github.com/andrewyng/translation-agent). The core code of this project is refactored from a cramped utils.py to improve readability and maintainability. Additionally, it adds support for glossaries, additional instructions, and future support for other LLMs.
# Universal Translator

Agentic translation using reflection workflow, refactored and sugared.

## Features

- Agentic translation w/ reflection workflow, as purposed in [translation-agent](https://github.com/andrewyng/translation-agent)
- Refactored for better readability and maintainability
- Sugared interface for easy usage
- Support for glossary, and additional instructions for translation
- Support for other LLMs(coming soon)

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
python examples/translate.py
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

## Credits

Inspired by [translation-agent](https://github.com/andrewyng/translation-agent). The core code of this project is refactored from a cramped utils.py to improve readability and maintainability. Additionally, it adds support for glossaries, additional instructions, and future support for other LLMs.
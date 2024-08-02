# Universal Translator

Agentic translation using reflection workflow, refactored and suggared.

## Features

- Agentic translation w/ reflection workflow, as purposed in [translation-agent](https://github.com/andrewyng/translation-agent)
- Refactored and suggared for better readability and maintainability
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
from universal_translator.translate.translation import AITranslator

# initilize the LLM provider
provider = OpenAI(api_key=openai_api_key, model="gpt-4o")
# initialize the translator
translator = AITranslator(
    source_language="en", # or English
    target_language="fr", # or French
    llm_provider=provider,
    country="France",
)
# translate the text
translated_text = translator.translate(text)
```

## Credits

Inspired by [translation-agent](https://github.com/andrewyng/translation-agent). It's core code is crammed in a `utils.py` that is hard to read and maintain. This project refactors and suggars the code for better readability and maintainability. Also, it adds support for glossary, additional instructions, and other LLMs.
import os

from universal_translator.llm.anthropic import Anthropic
from universal_translator.llm.anthropic_bedrock import AnthropicBedrock
from universal_translator.llm.base import LLMProvider
from universal_translator.llm.groq import Groq
from universal_translator.llm.moonshot import Moonshot
from universal_translator.llm.openai import OpenAI


def run_llm_provider(provider: LLMProvider):
    response, _ = provider.get_completion("Hello, world!")
    print(response)
    assert isinstance(response, str)
    assert response != ""


def test_groq():
    provider = Groq(api_key=os.getenv("GROQ_API_KEY"))
    run_llm_provider(provider)


def test_openai():
    api_key = os.getenv("OPENAI_API_KEY")
    provider = OpenAI(api_key=api_key)
    run_llm_provider(provider)


def test_anthropic():
    provider = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    run_llm_provider(provider)


def test_anthropic_bedrock():
    provider = AnthropicBedrock(
        access_key=os.getenv("AWS_ACCESS_KEY_ID"),
        secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    )
    run_llm_provider(provider)


def test_moonshot():
    provider = Moonshot(api_key=os.getenv("MOONSHOT_API_KEY"))
    run_llm_provider(provider)

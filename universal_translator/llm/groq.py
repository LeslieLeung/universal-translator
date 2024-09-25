import openai

from universal_translator.llm.openai import OpenAICompatible


class Groq(OpenAICompatible):
    def __init__(self, api_key: str, **kwargs):
        client = openai.OpenAI(base_url="https://api.groq.com/openai/v1", api_key=api_key)
        super().__init__(client, **kwargs)
        self.model = kwargs.get("model", "llama3-70b-8192")

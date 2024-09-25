import openai

from universal_translator.llm.openai import OpenAICompatible


class Moonshot(OpenAICompatible):
    def __init__(self, api_key: str, **kwargs):
        client = openai.OpenAI(base_url="https://api.moonshot.cn/v1", api_key=api_key)
        super().__init__(client, **kwargs)
        self.model = kwargs.get("model", "moonshot-v1-auto")

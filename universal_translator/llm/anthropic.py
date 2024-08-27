from typing import List, Tuple

import tiktoken
from anthropic import Anthropic as AnthropicClient
from langchain_text_splitters import RecursiveCharacterTextSplitter

from universal_translator.llm.base import LLMProvider, Usage


class Anthropic(LLMProvider):
    def __init__(self, **kwargs):
        self.model = kwargs.get("model", "claude-3-5-sonnet-20240620")
        self.temperature = kwargs.get("temperature", 0.3)
        self.client = AnthropicClient(
            api_key=kwargs.get("api_key"),
        )

    def num_tokens_in_string(self, input_str: str) -> int:
        """
        Since Anthropic does not provide a public tokenizer, we use OpenAI's tokenizer to estimate the number of tokens.
        see:
        https://github.com/anthropics/anthropic-sdk-python/issues/353
        https://github.com/anthropics/anthropic-sdk-python/issues/375
        """
        encoding = tiktoken.get_encoding("cl100k_base")
        num_tokens = len(encoding.encode(input_str))
        return num_tokens

    def split_text(self, text: str, max_tokens: int = 1000) -> List[str]:
        num_tokens_in_text = self.num_tokens_in_string(text)
        token_size = LLMProvider.calculate_chunk_size(token_count=num_tokens_in_text, token_limit=max_tokens)

        text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
            encoding_name="cl100k_base",  # same as above, use openai's tokenizer to estimate
            chunk_size=token_size,
            chunk_overlap=0,
        )

        return text_splitter.split_text(text)

    def get_completion(
        self,
        prompt: str,
        system_message: str = "You are a helpful assistant.",
        **kwargs,
    ) -> Tuple[str, Usage]:
        model = kwargs.get("model", self.model)
        temperature = kwargs.get("temperature", self.temperature)

        completion = self.client.messages.create(
            max_tokens=8192,
            model=model,  # type: ignore
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            system=system_message,
            temperature=temperature,
            top_p=1,
        )

        # calculate usage
        usage = Usage(
            total_tokens=completion.usage.input_tokens + completion.usage.output_tokens,
            prompt_tokens=completion.usage.input_tokens,
            completion_tokens=completion.usage.output_tokens,
        )

        return completion.content[0].text, usage  # type: ignore

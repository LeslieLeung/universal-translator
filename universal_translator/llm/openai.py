from typing import List, Tuple

import openai
import tiktoken
from langchain_text_splitters import RecursiveCharacterTextSplitter

from universal_translator.llm.base import LLMProvider, Usage


class OpenAI(LLMProvider):
    def __init__(self, api_key: str, **kwargs):
        self.api_key = api_key
        self.model = kwargs.get("model", "gpt-4o")
        self.temperature = kwargs.get("temperature", 0.3)
        self.client = openai.OpenAI(api_key=api_key)

    def num_tokens_in_string(self, input_str: str) -> int:
        """
        Calculate the number of tokens in a given string using a specified encoding.

        Args:
            str (str): The input string to be tokenized.

        Returns:
            int: The number of tokens in the input string.

        Example:
            >>> text = "Hello, how are you?"
            >>> num_tokens = num_tokens_in_string(text)
            >>> print(num_tokens)
            5
        """
        encoding = tiktoken.encoding_for_model(self.model)
        num_tokens = len(encoding.encode(input_str))
        return num_tokens

    def split_text(self, text: str, max_tokens: int = 1000) -> List[str]:
        num_tokens_in_text = self.num_tokens_in_string(text)
        token_size = LLMProvider.calculate_chunk_size(token_count=num_tokens_in_text, token_limit=max_tokens)

        text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
            model_name=self.model,
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
        # If model and temperature are not provided, use the default values
        model = kwargs.get("model", self.model)
        temperature = kwargs.get("temperature", self.temperature)

        # Create completion
        response = self.client.chat.completions.create(
            model=model,
            temperature=temperature,
            top_p=1,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt},
            ],
        )

        usage = Usage(
            total_tokens=response.usage.total_tokens,
            prompt_tokens=response.usage.prompt_tokens,
            completion_tokens=response.usage.completion_tokens,
        )
        return response.choices[0].message.content, usage  # type: ignore

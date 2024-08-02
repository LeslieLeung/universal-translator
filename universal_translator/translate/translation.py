from typing import Callable, Dict, List

from universal_translator.llm.base import LLMProvider
from universal_translator.translate.glossary import format_glossary
from universal_translator.translate.prompt import (
    PROMPT_IMPROVE_TRANSLATION,
    PROMPT_IMPROVE_TRANSLATION_SYSTEM,
    PROMPT_INITIAL_TRANSLATION,
    PROMPT_INITIAL_TRANSLATION_SYSTEM,
    PROMPT_REFLECT_ON_TRANSLATION,
    PROMPT_REFLECT_ON_TRANSLATION_SYSTEM,
)


class AITranslator:
    def __init__(self, source_language: str, target_language: str, llm_provider: LLMProvider, **kwargs):
        self.source_language: str = source_language
        self.target_language: str = target_language
        self.country: str = kwargs.get("country", "")
        self.glossary: List[Dict[str, str]] = kwargs.get("glossary", [])
        self.extra_instructions: str = kwargs.get("extra_instructions", "")
        self.llm_provider: LLMProvider = llm_provider

    def translate(self, text: str, post_processing: List[Callable] = []) -> str:
        # 1. chunk the text
        chunks = self.llm_provider.split_text(text)
        # 2. initial translation
        translated_chunks = self._initial_translation(chunks)
        # 3. reflect on translation
        reflection_chunks = self._reflect_on_translation(chunks, translated_chunks)
        # 4. improve translation
        improved_translation = self._improve_translation(chunks, translated_chunks, reflection_chunks)
        # 5. join the chunks
        translated_text = "".join(improved_translation)
        # 6. apply post-processing
        for post_process in post_processing:
            translated_text = post_process(translated_text)  # type: ignore
        return translated_text

    def _get_tagged_text(self, source_text_chunks, i):
        tagged_text = (
            "".join(source_text_chunks[0:i])
            + "<TRANSLATE_THIS>"
            + source_text_chunks[i]
            + "</TRANSLATE_THIS>"
            + "".join(source_text_chunks[i + 1 :])
        )

        return tagged_text

    def _initial_translation(self, source_text_chunks: List[str]) -> List[str]:
        translated_chunks = []
        for i in range(len(source_text_chunks)):
            tagged_text = self._get_tagged_text(source_text_chunks, i)

            prompt = PROMPT_INITIAL_TRANSLATION.format(
                source_lang=self.source_language,
                target_lang=self.target_language,
                country=self.country,
                tagged_text=tagged_text,
                chunk_to_translate=source_text_chunks[i],
                glossary=format_glossary(self.glossary),
                extra_instructions=self.extra_instructions,
            )

            translation = self.llm_provider.get_completion(prompt, PROMPT_INITIAL_TRANSLATION_SYSTEM)
            translated_chunks.append(translation)

        return translated_chunks

    def _reflect_on_translation(self, source_text_chunks: List[str], translated_chunks: List[str]) -> List[str]:
        reflection_chunks = []
        for i in range(len(source_text_chunks)):
            tagged_text = self._get_tagged_text(source_text_chunks, i)

            prompt = PROMPT_REFLECT_ON_TRANSLATION.format(
                source_lang=self.source_language,
                target_lang=self.target_language,
                country=self.country,
                tagged_text=tagged_text,
                chunk_to_translate=source_text_chunks[i],
                translation_1_chunk=translated_chunks[i],
                glossary=format_glossary(self.glossary),
            )

            reflection = self.llm_provider.get_completion(prompt, PROMPT_REFLECT_ON_TRANSLATION_SYSTEM)
            reflection_chunks.append(reflection)

        return reflection_chunks

    def _improve_translation(
        self,
        source_text_chunks: List[str],
        translated_chunks: List[str],
        reflection_chunks: List[str],
    ) -> List[str]:
        improved_translation = []
        for i in range(len(source_text_chunks)):
            tagged_text = self._get_tagged_text(source_text_chunks, i)

            prompt = PROMPT_IMPROVE_TRANSLATION.format(
                source_lang=self.source_language,
                target_lang=self.target_language,
                country=self.country,
                tagged_text=tagged_text,
                chunk_to_translate=source_text_chunks[i],
                translation_1_chunk=translated_chunks[i],
                reflection_chunk=reflection_chunks[i],
                glossary=format_glossary(self.glossary),
            )

            improved = self.llm_provider.get_completion(prompt, PROMPT_IMPROVE_TRANSLATION_SYSTEM)
            improved_translation.append(improved)

        return improved_translation

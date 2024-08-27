import os
import time

from dotenv import load_dotenv

from universal_translator.llm.openai import OpenAI
from universal_translator.translate.translation import UniversalTranslator

if __name__ == "__main__":
    load_dotenv()
    openai_api_key = os.getenv("OPENAI_API_KEY") or exit("No OpenAI API key found")

    # initilize the LLM provider
    provider = OpenAI(api_key=openai_api_key, model="gpt-4o")
    # initialize the translator
    translator = UniversalTranslator(
        source_language="en",
        target_language="fr",
        llm_provider=provider,
        country="France",
    )

    # load the text
    script_dir = os.path.dirname(os.path.abspath(__file__))
    rel_path_to_text = "sample.txt"

    with open(os.path.join(script_dir, rel_path_to_text), "r") as file:
        text = file.read()
    print(f"Text to translate: {text}\n")
    print("--------------------------------------------------\n")

    # translate the text
    start_time = time.time()
    translated_text = translator.translate(text)
    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")
    print(f"Usage: {translator.usage}")
    print(f"Translated text: {translated_text}")

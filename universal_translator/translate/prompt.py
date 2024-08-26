# Step 1: Initial Translation
PROMPT_INITIAL_TRANSLATION_SYSTEM = (
    "You are an expert linguist, specializing in translation from {source_lang} to {target_lang}."
)
PROMPT_INITIAL_TRANSLATION = """Your task is to provide a professional translation from {source_lang} to {target_lang} of PART of a text.

The source text is below, delimited by XML tags <SOURCE_TEXT> and </SOURCE_TEXT>. Translate only the part within the source text delimited by <TRANSLATE_THIS> and </TRANSLATE_THIS>. You can use the rest of the source text as context, but do not translate any of the other text. Consider the glossary delimited by <GLOSSARY> and </GLOSSARY>. Also, pay attention to the extra instructions delimited by <INSTRUCTION> and </INSTRUCTION>.
Do not output anything other than the translation of the indicated part of the text. Do not include any XML tags in your output.

<SOURCE_TEXT>
{tagged_text}
</SOURCE_TEXT>

<GLOSSARY>
{glossary}
</GLOSSARY>

<INSTRUCTION>
{extra_instructions}
</INSTRUCTION>

To reiterate, you should translate only this part of the text, shown here again between <TRANSLATE_THIS> and </TRANSLATE_THIS>:
<TRANSLATE_THIS>
{chunk_to_translate}
</TRANSLATE_THIS>

Output only the translation of the portion you are asked to translate, and nothing else."""

# Step 2: Reflection on Translation
PROMPT_REFLECT_ON_TRANSLATION_SYSTEM = "You are an expert linguist specializing in translation from {source_lang} to {target_lang}. \
You will be provided with a source text and its translation and your goal is to improve the translation."
PROMPT_REFLECT_ON_TRANSLATION = """Your task is to carefully read a source text and part of a translation of that text from {source_lang} to {target_lang}, and then give constructive criticism and helpful suggestions for improving the translation.
The final style and tone of the translation should match the style of {target_lang} colloquially spoken in {country}.

The source text is below, delimited by XML tags <SOURCE_TEXT> and </SOURCE_TEXT>, and the part that has been translated is delimited by <TRANSLATE_THIS> and </TRANSLATE_THIS> within the source text. Consider the glossary delimited by <GLOSSARY> and </GLOSSARY>. Also, pay attention to the extra instructions delimited by <INSTRUCTION> and </INSTRUCTION>.
You can use the rest of the source text as context for critiquing the translated part.

<SOURCE_TEXT>
{tagged_text}
</SOURCE_TEXT>

<GLOSSARY>
{glossary}
</GLOSSARY>

<INSTRUCTION>
{extra_instructions}
</INSTRUCTION>

To reiterate, only part of the text is being translated, shown here again between <TRANSLATE_THIS> and </TRANSLATE_THIS>:
<TRANSLATE_THIS>
{chunk_to_translate}
</TRANSLATE_THIS>

The translation of the indicated part, delimited below by <TRANSLATION> and </TRANSLATION>, is as follows:
<TRANSLATION>
{translation_1_chunk}
</TRANSLATION>

When writing suggestions, pay attention to whether there are ways to improve the translation's:
(i) accuracy (by correcting errors of addition, mistranslation, omission, or untranslated text),
(ii) fluency (by applying {target_lang} grammar, spelling and punctuation rules, and ensuring there are no unnecessary repetitions),
(iii) style (by ensuring the translations reflect the style of the source text and take into account any cultural context),
(iv) terminology (by ensuring terminology use is consistent and reflects the source text domain; and by only ensuring you use equivalent idioms {target_lang}).

Write a list of specific, helpful and constructive suggestions for improving the translation.
Each suggestion should address one specific part of the translation.
Output only the suggestions and nothing else."""

# Step 3: Improve Translation
PROMPT_IMPROVE_TRANSLATION_SYSTEM = (
    "You are an expert linguist, specializing in translation editing from {source_lang} to {target_lang}."
)
PROMPT_IMPROVE_TRANSLATION = """Your task is to carefully read, then improve, a translation from {source_lang} to {target_lang}, taking into account a set of expert suggestions and constructive criticisms. Below, the source text, initial translation, and expert suggestions are provided.

The source text is below, delimited by XML tags <SOURCE_TEXT> and </SOURCE_TEXT>, and the part that has been translated is delimited by <TRANSLATE_THIS> and </TRANSLATE_THIS> within the source text. Consider the glossary delimited by <GLOSSARY> and </GLOSSARY>. Also, pay attention to the extra instructions delimited by <INSTRUCTION> and </INSTRUCTION>.
You can use the rest of the source text as context, but need to provide a translation only of the part indicated by <TRANSLATE_THIS> and </TRANSLATE_THIS>.
Do not include any XML tags in your output.

<SOURCE_TEXT>
{tagged_text}
</SOURCE_TEXT>

<GLOSSARY>
{glossary}
</GLOSSARY>

<INSTRUCTION>
{extra_instructions}
</INSTRUCTION>

To reiterate, only part of the text is being translated, shown here again between <TRANSLATE_THIS> and </TRANSLATE_THIS>:
<TRANSLATE_THIS>
{chunk_to_translate}
</TRANSLATE_THIS>

The translation of the indicated part, delimited below by <TRANSLATION> and </TRANSLATION>, is as follows:
<TRANSLATION>
{translation_1_chunk}
</TRANSLATION>

The expert translations of the indicated part, delimited below by <EXPERT_SUGGESTIONS> and </EXPERT_SUGGESTIONS>, are as follows:
<EXPERT_SUGGESTIONS>
{reflection_chunk}
</EXPERT_SUGGESTIONS>

Taking into account the expert suggestions rewrite the translation to improve it, paying attention to whether there are ways to improve the translation's

(i) accuracy (by correcting errors of addition, mistranslation, omission, or untranslated text),
(ii) fluency (by applying {target_lang} grammar, spelling and punctuation rules and ensuring there are no unnecessary repetitions),
(iii) style (by ensuring the translations reflect the style of the source text)
(iv) terminology (inappropriate for context, inconsistent use), or
(v) other errors.

Output only the new translation of the indicated part and nothing else."""

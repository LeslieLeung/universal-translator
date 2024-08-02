from typing import Dict, List


def format_glossary(glossary: List[Dict[str, str]]) -> str:
    """
    Format the glossary to a xml format.

    Args:
        glossary (List[Dict[str, str]]): A list of dictionaries containing source and target language terms.

    Returns:
        str: The glossary in xml format.
    """

    glossary_xml = "".join(
        f"<GlossaryItem><Source>{item['source']}</Source><Target>{item['target']}</Target><Notes>{item['notes']}</Notes></GlossaryItem>"
        for item in glossary
    )

    return glossary_xml

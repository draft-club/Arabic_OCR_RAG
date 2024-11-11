import pandas as pd
from openai_local.utils import get_field_from_text, setup_openai
from openai_local.prompts import MAIN_PROMPT
from openai_local.refrence_dictionaries.target_fields import expropriation_data
from task_decorator import task_logger


class ExtractFieldsUsingLLM:
    """Task to extract specific fields from text using LLM."""

    @staticmethod
    @task_logger
    def run(extracted_text):
        """Extract fields using a Language Model (OpenAI)."""
        client = setup_openai()
        results = []
        for item in expropriation_data:
            field = item.get("field")
            field_prompt = item.get("field_prompt")
            lookuptext = item.get("lookuptext")
            dynamic = item.get("dynamic")
            default_value = item.get("default_value")
            if dynamic:
                response = get_field_from_text(client, MAIN_PROMPT, field_prompt, extracted_text, field)
            else:
                response = default_value
            results.append({'Champs': field, 'Valeur': response})
        df = pd.DataFrame(results)
        return df

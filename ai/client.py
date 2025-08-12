
import os
from .mock_llm import suggest_from_artifacts

def call_llm(prompt: str) -> str:
    provider = os.getenv("LLM_PROVIDER", "mock").lower()
    if provider == "mock":
        return suggest_from_artifacts(prompt)
    elif provider == "openai":
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            return "LLM provider 'openai' set, but OPENAI_API_KEY is missing."
        return "(LLM call stub. Add provider implementation here.)"
    else:
        return f"Unknown LLM provider: {provider}"

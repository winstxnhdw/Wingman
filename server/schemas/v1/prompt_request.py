from pydantic import BaseModel, Field


class PromptRequest(BaseModel):
    """
    Summary
    -------
    the prompt request schema

    Attributes
    ----------
    prompt (str) : the prompt to generate from
    """
    prompt: str = Field(examples=['def fibonacci(n: int) -> int:\n    '])

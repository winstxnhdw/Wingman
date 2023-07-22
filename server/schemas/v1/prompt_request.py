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
    prompt: str = Field(examples=["Create a Python function that returns the sum of two numbers"])

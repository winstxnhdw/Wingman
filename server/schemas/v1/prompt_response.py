from pydantic import BaseModel, Field


class PromptResponse(BaseModel):
    """
    Summary
    -------
    the prompt response schema

    Attributes
    ----------
    text (str) : the response to the prompt
    """
    text: str = Field(examples=["Create a Python function that returns the sum of two numbers"])

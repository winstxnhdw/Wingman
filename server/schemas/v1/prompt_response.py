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
    text: str = Field(
        examples=[
            'def fibonacci(n: int) -> int:\n    if (n == 1):\n      return 1\n    return fibonacci(n- 1) + fibonacci(n - 2)'
        ]
    )

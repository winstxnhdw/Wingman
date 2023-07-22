from server.api.v1 import v1
from server.features import Generator
from server.schemas.v1 import PromptRequest, PromptResponse


@v1.post('/generate', response_model=PromptResponse)
async def generate(request: PromptRequest):
    """
    Summary
    -------
    the `/generate` route
    """
    result =  Generator.generate(request.prompt)
    return PromptResponse(text=result)

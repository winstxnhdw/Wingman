from pydantic import BaseModel, Field


class ToggleDeviceResponse(BaseModel):
    """
    Summary
    -------
    the response schema for the /toggle_device route

    Attributes
    ----------
    device (str) : the device that the generator is currently using
    message (str) : the response to the prompt
    """
    device: str = Field(
        examples=['CPU', 'CUDA']
    )

    message: str = Field(
        examples=[
            "Device toggled to CPU successfully!",
            "Device toggled to CUDA successfully!"
        ]
    )

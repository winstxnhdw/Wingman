from server.api.v1 import v1
from server.features import Generator
from server.schemas.v1 import ToggleDeviceResponse


@v1.get('/toggle_device', response_model=ToggleDeviceResponse)
async def toggle_device():
    """
    Summary
    -------
    the `/toggle_device` route
    """
    device = Generator.toggle_device().upper()

    return ToggleDeviceResponse(
        device=device,
        message=f'Device toggled to {device} successfully!'
    )

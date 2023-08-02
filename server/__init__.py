from asyncio import run
from typing import Generator

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from hypercorn.asyncio import serve

from server.api import v1
from server.api.v1 import generate as generate
from server.api.v1 import index as index
from server.api.v1 import toggle_device as toggle_device
from server.config import Config


def initialise() -> Generator[FastAPI, None, None]:
    """
    Summary
    -------
    initialize the server
    """
    app = FastAPI()
    app.include_router(v1)
    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_origins=['*'],
        allow_methods=['*'],
        allow_headers=['*'],
    )

    yield app
    run(serve(app, Config()))

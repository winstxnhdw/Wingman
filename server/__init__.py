from typing import Generator

from fastapi import FastAPI

from server.initialise_routes import initialise_routes
from server.initialise_server import initialise_server


def initialise() -> Generator[FastAPI, None, None]:
    """
    Summary
    -------
    initialises everything
    """
    initialise_routes()
    return initialise_server()

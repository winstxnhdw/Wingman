from asyncio import run
from importlib import import_module
from itertools import chain
from os import walk
from typing import Generator

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from hypercorn.asyncio import serve

from server.api import v1
from server.config import Config


class Server:
    """
    Summary
    -------
    the server class

    Attributes
    ----------

    """
    def __init__(self):

        self.app: FastAPI
        self.api_directory = 'server/api'


    def convert_delimiters(self, string: str, old: str, new: str) -> str:
        """
        Summary
        -------
        convert delimiters in a string

        Parameters
        ----------
        string (str) : the string to convert
        old (str) : the old delimiter
        new (str) : the new delimiter

        Returns
        -------
        string (str) : the converted string
        """
        return new.join(string.split(old))


    def initialise_routes(self):
        """
        Summary
        -------
        initialise all routes
        """
        module_file_names = [
            [f'{root}/{file}' for file in files if not file.startswith('__') and file.endswith('.py')]
            for root, _, files in walk(self.api_directory)
        ]

        for file_name in chain.from_iterable(module_file_names):
            module_name = import_module(self.convert_delimiters(file_name[:-3], '/', '.')).__name__
            print(f" * {self.convert_delimiters(module_name[len(self.api_directory):], '.', '/')} route found!")


    def initialise_server(self):
        """
        Summary
        -------
        initialize the server
        """
        self.app = FastAPI()
        self.app.include_router(v1)
        self.app.add_middleware(
            CORSMiddleware,
            allow_credentials=True,
            allow_origins=['*'],
            allow_methods=['*'],
            allow_headers=['*'],
        )


    @classmethod
    def initialise(cls) -> Generator[FastAPI, None, None]:
        """
        Summary
        -------
        initialises everything
        """
        self = cls()
        self.initialise_routes()
        self.initialise_server()

        yield self.app
        run(serve(self.app, Config()))

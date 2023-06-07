# File: Server.py
#
# The main file responsible for the server.
# Its main task is to start the server and coordinate with other software files.

from src import app, log
from src.server.ServerConfig import ServerConfig
from src.utils.EnvSystem import EnvSystem


class Server:
    """The main class responsible for the basic functions of the server."""
    __HOST: str
    __PORT: int

    @classmethod
    def __init__(cls):
        EnvSystem('serverConfig.env')

        cls.__HOST = EnvSystem.get_env_element('SERVER_HOST')
        cls.__PORT = EnvSystem.get_env_element('SERVER_PORT')
        ServerConfig()

    @classmethod
    def start(cls) -> None:
        """Method to start the server"""
        log.debug(f'Running the server on the host: {cls.__HOST}')
        log.debug(f'Running the server on the port: {cls.__PORT}')
        log.info('Starting the server...')

        app.run(cls.__HOST, cls.__PORT)

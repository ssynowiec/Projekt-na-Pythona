# File: main.py
# Date start: 17.05.2023
#
# TODO: Add a project name.
# Project name: <======>
# Author: Krystian Ozga, Stanisław Synowiec
#
# Project description:
#   A project created for the purpose of passing laboratories in object-oriented programming(OOP) in Python. The main
#   goal of the project is to test knowledge at the intermediate level.
#
import sys
from src.server.Server import Server
from migrations.Init_db import Init_db
from src import log


# <Main application boot file>
if __name__ == '__main__':
    log.info('Starting the program...')
    server: Server = Server()

    if len(sys.argv) > 1:
        match sys.argv[1].lower():
            case '-init-db':
                log.debug('Console command loaded [ -init-db ]')
                log.info('Initializing the database...')
                Init_db()

            case '-init-tests':
                log.debug('Console command loaded [ -init-tests ]')
                log.info('Initializing the tests...')
                # TODO: Uruchamianie testów!
                pass

            case _:
                log.debug('The detected command is not among those available to the application.')
                log.error('Unknown command!')

    else:
        log.info('Initializing the server...')
        server.start()

    log.info('Exiting the program...')

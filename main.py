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
import click
from src.server.Server import Server
from simple_chalk import yellow

from migrations.init_db import init_db


# <Main application boot file>
if __name__ == '__main__':
    print(yellow("Starting API server..."))
    # The user MUST select one of the options provided.
    # At the same time, the given options are fully independent of each other, but they should not be
    # exercised at the same time.
    while True:
        # optionVal: bool = click.confirm('Activate unit test for software?', default=True)
        optionVal: bool = False

        match optionVal:
            case True:
                # TODO: Create a method or function responsible for the test mode.
                break

            case False:
                # TODO: Improve referencing to the server and make things more secure than the current one.
                server: Server = Server()
                init_db()

                server.start()
                break

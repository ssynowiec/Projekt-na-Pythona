# File: Init_db
#
# The file responsible for creating a new database and assigning appropriate values to it.
# All queries and table schemas should be in the appropriate directories.

from src.database.SQLite import SQLite
from src.utils.FileSystem import FileSystem
from src import app, log


class Init_db:
    __sql: SQLite

    @classmethod
    def __init__(cls):
        if FileSystem.exist_file(app.config['DATABASE_PATH'] + app.config['DATABASE_NAME']):
            cls.__sql = SQLite()

            log.info('Existing database file found...')
            log.info(f'Opening a file: [ {app.config["DATABASE_NAME"]} ]')

            cls.__sql.load_schema('clear_database.schema.sql')

        else:
            cls.__sql = SQLite()

            log.info('Creating a database...')
            log.debug(f"Creating a database named: [ {app.config['DATABASE_NAME']} ]")

        cls.__load_init_schema()
        cls.__load_init_data()

        cls.__sql.close()

    @classmethod
    def __load_init_schema(cls):
        cls.__sql.load_all_exist_schema()

    @classmethod
    def __load_init_data(cls):
        cls.__sql.load_all_exist_query()

# File: Init_db
#
# The file responsible for creating a new database and assigning appropriate values to it.
# All queries and table schemas should be in the appropriate directories.

from src.database.SQLite import SQLite
from src import log


class Init_db:
    sql: SQLite

    @classmethod
    def __init__(cls):
        cls.sql = SQLite()

        cls.__load_init_schema()
        cls.__load_init_data()

        cls.sql.close()

    @classmethod
    def __load_init_schema(cls):
        cls.sql.load_all_exist_schema()

    @classmethod
    def __load_init_data(cls):
        cls.sql.load_all_exist_query()

        log.success('All data has been successfully placed in the tables!')


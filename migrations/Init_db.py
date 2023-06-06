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
        cls.sql = SQLite('database.db')

        cls.__load_schema()
        cls.__insert_data()

        cls.sql.commit()

        cls.sql.close()

    @classmethod
    def __load_schema(cls):
        cls.sql.load_all_exist_schema()

    @classmethod
    def __insert_data(cls):
        cls.sql.load_all_exist_query()

        log.success('All data has been successfully placed in the tables!')


from src.database.SQLite import SQLite
import pytest


class TEST_SQLite:
    __sql: SQLite

    @classmethod
    def setup_class(cls):
        cls.__sql = SQLite()

    @classmethod
    def teardown_class(cls):
        cls.__sql.close()

    @classmethod
    def CASE_execute_select(cls):
        query: str = 'SELECT name FROM author'
        exception: list = [('J.K.',), ('Harper',)]

        assert exception == cls.__sql.execute(query)

    @classmethod
    def CASE_execute_insert(cls):
        query: str = 'INSERT INTO author (name, surname, birth_date) VALUES ("TEST_NAME", "TEST_LASTNAME", "TEST_DATE")'
        exception = None

        assert exception == cls.__sql.execute(query)

    @classmethod
    def CASE_execute_update(cls):
        query: str = 'UPDATE author SET name = "UPDATA NAME" WHERE name = "TEST_NAME"'
        exception = None

        assert exception == cls.__sql.execute(query)

    @classmethod
    def CASE_execute_delete(cls):
        query: str = 'DELETE FROM author WHERE name = "UPDATA NAME"'
        exception = None

        assert exception == cls.__sql.execute(query)

    @classmethod
    def CASE_execute_params(cls):
        query: str = 'SELECT name FROM author WHERE name = ?'
        param: tuple = ('Harper',)
        exception: list = [('Harper',)]

        assert exception == cls.__sql.execute(query, param)

    @classmethod
    def CASE_execute_fetch_one(cls):
        query: str = 'SELECT name FROM author'
        exception: tuple = ('J.K.',)

        assert exception == cls.__sql.execute(query, _fetchType='one')

    @classmethod
    def CASE_execute_fetch_all(cls):
        query: str = 'SELECT name FROM author'
        exception: list = [('J.K.',), ('Harper',)]

        assert exception == cls.__sql.execute(query, _fetchType='all')

    @classmethod
    def CASE_execute_fetch_many(cls):
        query: str = 'SELECT name FROM author'
        exception: list = [('J.K.',)]

        assert exception == cls.__sql.execute(query, _fetchType='many', _howManyFetch=1)

    @classmethod
    def CASE_execute_raise_SQL_keywords(cls):
        query: str = 'SELECT name FR_ERR_OM author'

        with pytest.raises(Exception):
            cls.__sql.execute(query)

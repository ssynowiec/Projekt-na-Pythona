import sqlite3


class DbConnection:
    conn: sqlite3.Connection

    @classmethod
    def __init__(cls):
        cls.conn = sqlite3.connect('database.db')
        cls.conn.row_factory = sqlite3.Row

    @classmethod
    def __open__(cls) -> sqlite3.Connection:
        return cls.conn

    @classmethod
    def __close__(cls) -> None:
        cls.conn.close()

    @classmethod
    def execute(cls, _query, _params=()) -> list:
        cursor = cls.conn.cursor()
        cursor.execute(_query, _params)

        return cursor.fetchall()

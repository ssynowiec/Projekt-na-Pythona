# File: SQLite
#
#
import sqlite3 as sql

from src import app
from src.utils.FileSystem import FileSystem
from simple_chalk import green, red, yellow, blue


class SQLite:
    __conn: sql.Connection
    __cursor: sql.Cursor
    __schemaDir: str

    @classmethod
    def __init__(cls, _db: str):
        cls.__conn = sql.connect(app.config['DATABASE_PATH'] + _db)
        cls.__cursor = cls.__conn.cursor()
        cls.__schemaDir = app.config['SCHEMA_PATH']
        # cls.__conn.row_factory = sql.Row

        cls.execute('PRAGMA foreign_keys = 1')

    @classmethod
    def close(cls) -> None:
        cls.__conn.close()

    @classmethod
    def execute(cls, _query: str, _params: tuple = ()) -> list:
        try:
            cls.__cursor.execute(_query, _params)

        except Exception as e:
            print(red.bold('[ERROR]') + red.bold(f' ┌ There was a problem executing the query!'),
                  red('\n\t\t├──── Order: ' + _query),
                  red('\n\t\t├──── Params: ' + _params.__str__()),
                  red('\n\t\t└──── Problem: ' + e.__str__()))

        return cls.__cursor.fetchall()

    @classmethod
    def load_schema(cls, _fileName: str) -> None:
        try:
            with open(cls.__schemaDir + _fileName) as schemaFile:
                cls.__conn.executescript(schemaFile.read())

            print(green.bold('[SUCCESS]') + green(f' Table was added successfully -> {_fileName}'))

        except Exception as e:
            print(red.bold('[ERROR]') + red.bold(f' ┌ Failure to add table -> {_fileName}'),
                  red('\n\t\t└──── ' + e.__str__()))

    @classmethod
    def load_all_exist_schema(cls) -> None:
        fileList = FileSystem.get_sort_file_list(cls.__schemaDir)

        for file in fileList:
            cls.load_schema(file)

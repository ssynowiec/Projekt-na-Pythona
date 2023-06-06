# File: SQLite
#
#
import sqlite3 as sql

from src import app, log
from src.utils.FileSystem import FileSystem


class SQLite:
    __conn: sql.Connection
    __cursor: sql.Cursor
    __schemaDir: str

    @classmethod
    def __init__(cls, _db: str):
        log.info('Creating a database...')

        cls.__conn = sql.connect(app.config['DATABASE_PATH'] + _db)
        cls.__cursor = cls.__conn.cursor()
        cls.__schemaDir = app.config['SCHEMA_PATH']
        cls.__conn.row_factory = sql.Row

        cls.execute('PRAGMA foreign_keys = 1')

    @classmethod
    def __get_info_query(cls, _query: str):
        info: dict = dict()
        split_query: list[str] = _query.lower().split(' ')

        info.setdefault('type_query', split_query[0])

        match split_query[0]:
            case 'select':
                info.setdefault('table', split_query[split_query.index('from') + 1])
            case 'insert':
                info.setdefault('table', split_query[split_query.index('into') + 1])
            case 'update':
                info.setdefault('table', split_query[1])
            case 'delete':
                info.setdefault('table', split_query[split_query.index('from') + 1])
            case 'pragma':
                info.setdefault('table', 'DATABASE')

            case _:
                log.warning('Query type not yet included!')

        return info

    @classmethod
    def close(cls) -> None:
        log.info('Closing the database...')
        cls.__conn.close()

    @classmethod
    def execute(cls, _query: str, _params: tuple = ()) -> list:
        infoQuery: dict = cls.__get_info_query(_query)

        log.info(f'Executing a query type: [ {infoQuery["type_query"].upper()} ] for [ {infoQuery["table"].upper()} ]')

        try:
            cls.__cursor.execute(_query, _params)

        except Exception as e:
            log.error('There was a problem executing the query!', {
                'Order': _query,
                'Params': _params.__str__(),
                'Problem': e.__str__()
            })

        return cls.__cursor.fetchall()

    @classmethod
    def load_schema(cls, _fileName: str) -> None:
        try:
            with open(cls.__schemaDir + _fileName) as schemaFile:
                cls.__conn.executescript(schemaFile.read())

            log.success(f'Table was added successfully -> {_fileName}')

        except Exception as e:
            log.error(f'Failure to add table -> {_fileName}', {
                'Problem': e.__str__()
            })

    @classmethod
    def load_all_exist_schema(cls) -> None:
        log.info('Loading a list of schema files...')
        fileList = FileSystem.get_sort_file_list(cls.__schemaDir)

        for file in fileList:
            cls.load_schema(file)

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
    __queryDir: str

    @classmethod
    def __init__(cls):
        cls.__conn = sql.connect(app.config['DATABASE_PATH'] + app.config['DATABASE_NAME'])
        cls.__cursor = cls.__conn.cursor()
        cls.__schemaDir = app.config['SCHEMA_PATH']
        cls.__queryDir = app.config['QUERY_INIT_PATH']
        cls.__conn.row_factory = sql.Row

        # cls.execute('PRAGMA foreign_keys = 1')

    @classmethod
    def __get_info_query(cls, _query: str) -> dict:
        info: dict = dict()
        split_query: list[str] = _query.lower().split(' ')

        try:
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

        except ValueError:
            log.warning('Could not determine query type!')
            return

    @classmethod
    def __fetchData(cls, _fetchType: any, _howMany: int) -> any:
        match _fetchType:
            case 'all':
                return cls.__cursor.fetchall()
            case 'one':
                return cls.__cursor.fetchone()
            case 'many':
                return cls.__cursor.fetchmany(_howMany)

            case _:
                log.error(f'Selected fetching type is not available! -> {_fetchType}')

    @classmethod
    def close(cls) -> None:
        if cls.__conn:
            log.info('Closing the database...')
            cls.__conn.close()

    @classmethod
    def execute(cls, _query: str, _params: tuple = (), _fetchType: any = 'all', _howManyFetch: int = 1) -> list | None:
        infoQuery: dict = cls.__get_info_query(_query)
        fetchedQuery: any

        if infoQuery:
            log.info(
                f'Executing a query type: [ {infoQuery["type_query"].upper()} ] for [ {infoQuery["table"].upper()} ]')

        try:
            cls.__cursor.execute(_query, _params)
            cls.commit()

        except Exception as e:
            log.error('There was a problem executing the query!', {
                'Order': _query,
                'Params': _params.__str__(),
                'Problem': e.__str__()
            })

        if infoQuery:
            if infoQuery["type_query"] == 'select':
                fetchedQuery = cls.__fetchData(_fetchType, _howManyFetch)

                log.info('Returning data from the database...')
                log.debug(f"The following data has been fetched from the database: {fetchedQuery}")

                return fetchedQuery

        return None

    @classmethod
    def load_schema(cls, _fileName: str) -> None:
        try:
            with open(cls.__schemaDir + _fileName) as schemaFile:
                cls.__conn.executescript(schemaFile.read())

            if _fileName == 'clear_database.schema.sql':
                log.success(f'The database has been cleared -> {_fileName}')

            else:
                log.success(f'Table was added successfully -> {_fileName}')

        except Exception as e:
            if _fileName == 'clear_database.schema.sql':
                log.warning(f'The database was not cleaned up successfully! -> {_fileName}')
                log.warning('Errors are possible!')

            else:
                log.error(f'Failure to add table -> {_fileName}', {
                    'Problem': e.__str__()
                })

    @classmethod
    def load_all_exist_schema(cls) -> None:
        log.info('Loading a list of schema files...')
        fileList = FileSystem.get_sort_file_list(cls.__schemaDir)

        fileList.remove('clear_database.schema.sql')

        for file in fileList:
            cls.load_schema(file)

    @classmethod
    def load_query_init(cls, _fileName: str) -> None:
        try:
            with open(cls.__queryDir + _fileName) as queryFile:
                cls.__conn.executescript(queryFile.read())

            log.success(f'The query has been successfully loaded -> {_fileName}')

        except Exception as e:
            log.error(f'Failed to execute commands -> {_fileName}', {
                'Problem': e.__str__()
            })

    @classmethod
    def load_all_exist_query(cls) -> None:
        log.info('Loading a list of query files...')
        fileList = FileSystem.get_sort_file_list(cls.__queryDir)

        for file in fileList:
            cls.load_query_init(file)

    @classmethod
    def commit(cls) -> None:
        cls.__conn.commit()

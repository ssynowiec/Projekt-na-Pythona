# File: ServerConfig.py
#
# The file that configures the server in every possible way.
# Remember to stick to the SOLID rules when writing here.

from src.server.ServerInfo import ServerInfo
from src.utils.EnvSystem import EnvSystem
from src.utils.ParseSystem import ParseSystem

from datetime import timedelta
from src import app, log


class ServerConfig:
    """The class responsible for the main configuration of the entire server."""
    __serverInfo: ServerInfo
    __env: EnvSystem

    @classmethod
    def __init__(cls):
        log.info('Loading server configuration...')

        cls.__env = EnvSystem('ServerConfig.env')
        cls.__default_config()

        if cls.__env.file_exist():
            log.debug('Configuration file found.')
            log.debug('Loading a new configuration...')

            cls.__config_file()
            cls.__use_new_config()

        log.success('Server configuration successfully loaded!')

    # A method that sets the server's default parameters. Do not change anything in the dictionary that
    # contains these parameters. This is a backup in case the configuration file is not available or some
    # other sudden error occurs.
    @classmethod
    def __default_config(cls) -> None:
        defaultConfig: dict = {
            'APPLICATION_ROOT': None,
            'DEBUG': False,
            'EXPLAIN_TEMPLATE_LOADING': False,
            'JSONIFY_MIMETYPE': 'application/json',
            'JSONIFY_PRETTYPRINT_REGULAR': True,
            'JSON_AS_ASCII': True,
            'JSON_SORT_KEYS': True,
            'LOGGER_HANDLER_POLICY': 'always',
            'LOGGER_NAME': None,
            'MAX_CONTENT_LENGTH': None,
            'PERMANENT_SESSION_LIFETIME': timedelta(days=31),
            'PREFERRED_URL_SCHEME': 'http',
            'PRESERVE_CONTEXT_ON_EXCEPTION': None,
            'PROPAGATE_EXCEPTIONS': None,
            'SECRET_KEY': '_&"j$MlHsVvz*72~iZt,|VDb12L0i9yX[M=,h9{Ou0"!lFh-81Z%,+.LI[VA_`6',
            'SEND_FILE_MAX_AGE_DEFAULT': timedelta(seconds=43200),
            'SERVER_NAME': None,
            'SESSION_COOKIE_DOMAIN': None,
            'SESSION_COOKIE_HTTPONLY': True,
            'SESSION_COOKIE_NAME': 'session',
            'SESSION_COOKIE_PATH': None,
            'SESSION_COOKIE_SECURE': False,
            'SESSION_REFRESH_EACH_REQUEST': True,
            'TEMPLATES_AUTO_RELOAD': None,
            'TESTING': False,
            'TRAP_BAD_REQUEST_ERRORS': False,
            'TRAP_HTTP_EXCEPTIONS': False,
            'USE_X_SENDFILE': False,
            'DATABASE_PATH': '',
            'SCHEMA_PATH': '',
            'QUERY_INIT_PATH': ''
        }
        cls.__serverInfo = ServerInfo(defaultConfig)

    @classmethod
    def __config_file(cls) -> None:
        fileConfig: dict = dict()

        for key, _ in cls.__serverInfo.get_all_config().items():
            data: any = EnvSystem.get_env_element(key)

            if key in ['PERMANENT_SESSION_LIFETIME', 'SEND_FILE_MAX_AGE_DEFAULT']:
                fileConfig.setdefault(key, timedelta(seconds=ParseSystem.auto_parse(data)))
                continue

            fileConfig.setdefault(key, ParseSystem.auto_parse(data))

        cls.__serverInfo.set_configs(fileConfig)

    @classmethod
    def __use_new_config(cls) -> None:
        for key, val in cls.__serverInfo.get_all_config().items():
            log.debug(f'Configuration is set for the value: {key} -> {val}')
            app.config[key] = val

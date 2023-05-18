from ServerInfo import ServerInfo


class ServerConfig:
    __serverInfo: ServerInfo

    @classmethod
    def __init__(cls):
        cls.__SetDefaultConfig()

    @classmethod
    def __SetDefaultConfig(cls):
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
            'PERMANENT_SESSION_LIFETIME': datetime.timedelta(days=31),
            'PREFERRED_URL_SCHEME': 'http',
            'PRESERVE_CONTEXT_ON_EXCEPTION': None,
            'PROPAGATE_EXCEPTIONS': None,
            'SECRET_KEY': None,
            'SEND_FILE_MAX_AGE_DEFAULT': datetime.timedelta(seconds=43200),
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
            'USE_X_SENDFILE': False
        }
        cls.__serverInfo = ServerInfo(defaultConfig)

    @classmethod
    def SetConfigElement(cls, _nameConfigElement):
        cls.__serverInfo.SetConfigs(_nameConfigElement)

    @classmethod
    def SetConfigElements(cls, _nameConfigElements):
        pass

import logging
from logging.handlers import RotatingFileHandler
import datetime


class LogSystem:
    __loggerInstance: logging.Logger
    __formatter: logging.Formatter
    __fullPath: str

    @classmethod
    def __init__(cls):
        cls.__loggerInstance = logging.getLogger()
        cls.__formatter = logging.Formatter('[%(asctime)s] %(levelname)s-5s -> %(message)s')
        cls.__fullPath = 'log/'

        cls.__set_console_config()
        cls.__set_file_config()

    @classmethod
    def __create_path(cls):
        currentDate = datetime.datetime.now()

        pathTmp = f'{currentDate.year}/' \
                  f'{currentDate.month:02d}/' \
                  f'{currentDate.year}{currentDate.month:02d}{currentDate.day}_logs.log'

        cls.__fullPath += pathTmp

    @classmethod
    def __set_console_config(cls):
        cls.__create_path()

        consoleHandler = logging.StreamHandler()

        consoleHandler.setFormatter(cls.__formatter)
        cls.__loggerInstance.addHandler(consoleHandler)

    @classmethod
    def __set_file_config(cls):
        fileHandler = RotatingFileHandler(cls.__fullPath)

        fileHandler.setFormatter(cls.__formatter)
        cls.__loggerInstance.addHandler(fileHandler)

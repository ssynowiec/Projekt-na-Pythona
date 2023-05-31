import logging
import datetime
from logging.handlers import RotatingFileHandler
from src.utils.FileSystem import FileSystem


class LogSystem:
    __loggerInstance: logging.Logger
    __formatter: logging.Formatter
    __pathToLog: str
    __fileLogName: str

    @classmethod
    def __init__(cls):
        cls.__loggerInstance = logging.getLogger()
        cls.__formatter = logging.Formatter('[%(asctime)s] %(levelname)s -> %(message)s')
        cls.__pathToLog = str()
        cls.__fileLogName = str()

        cls.__set_console_config()
        cls.__set_file_config()

    @classmethod
    def __create_directories(cls) -> None:
        FileSystem.create_dir(cls.__pathToLog)

    @classmethod
    def __create_path_to_log(cls) -> None:
        currentDate = datetime.datetime.now()

        pathTmp = f'log/' \
                  f'{currentDate.year}/' \
                  f'{currentDate.month:02d}/'

        cls.__pathToLog += pathTmp

    @classmethod
    def __create_name_log(cls) -> None:
        currentDate = datetime.datetime.now()

        pathTmp = f'{currentDate.year}{currentDate.month:02d}{currentDate.day}_logs.log'

        cls.__fileLogName += pathTmp

    @classmethod
    def __set_console_config(cls) -> None:
        consoleHandler = logging.StreamHandler()

        consoleHandler.setFormatter(cls.__formatter)
        cls.__loggerInstance.addHandler(consoleHandler)

    @classmethod
    def __set_file_config(cls) -> None:
        cls.__create_path_to_log()
        cls.__create_name_log()
        cls.__create_directories()
        
        fileHandler = RotatingFileHandler(cls.__pathToLog + cls.__fileLogName)

        fileHandler.setFormatter(cls.__formatter)
        cls.__loggerInstance.addHandler(fileHandler)

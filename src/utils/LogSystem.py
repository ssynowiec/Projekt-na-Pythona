# File: LogSystem.py
#
# The file responsible for documenting events taking place in Flask.
# Thanks to this file, it is easier to understand errors in the software.

import datetime
from simple_chalk import red, green, yellow, blue
from src.utils.FileSystem import FileSystem


class LogSystem:
    __fileName: str
    __pathToDir: str

    @classmethod
    def __init__(cls):
        cls.__create_log_name()
        cls.__create_path_to_log()

        cls.__create_directories()
        cls.__print_separate_line()

    @classmethod
    def __date_log(cls):
        now = datetime.datetime.now()
        return f'[ {now.year}-{now.month:02d}-{now.day:02d} {now.hour:02d}:{now.minute:02d}:{now.second:02d} ]'

    @classmethod
    def __create_directories(cls) -> None:
        FileSystem.create_dir(cls.__pathToDir)

    @classmethod
    def __create_log_name(cls) -> None:
        currentDate = datetime.datetime.now()
        fileName = f'{currentDate.year}{currentDate.month:02d}{currentDate.day:02d}.log'

        cls.__fileName = fileName

    @classmethod
    def __create_path_to_log(cls) -> None:
        currentDate = datetime.datetime.now()

        pathTmp = f'log/' \
                  f'{currentDate.year}/' \
                  f'{currentDate.month:02d}/'

        cls.__pathToDir = pathTmp

    @classmethod
    def __print_to_file(cls, _text: str, _type: str):
        textToSave: str = str()

        match _type.lower():
            case 'success':
                textToSave = f'{cls.__date_log()} [SUCCESS] {_text}\n'
            case 'info':
                textToSave = f'{cls.__date_log()} [INFO] {_text}\n'
            case 'warning':
                textToSave = f'{cls.__date_log()} [WARNING] {_text}\n'
            case 'error':
                textToSave = f'{cls.__date_log()} [ERROR] {_text}\n'

            case _:
                textToSave = _text

        FileSystem.write(cls.__pathToDir + cls.__fileName, textToSave)

    @classmethod
    def __print_to_console(cls, _text: str, _type: str, _params: dict={}):
        match _type.lower():
            case 'success':
                print(green.bold('[SUCCESS]'), green(_text))

            case 'info':
                print(blue.bold('[INFO]'), blue(_text))

            case 'warning':
                print(yellow.bold('[WARNING]'), yellow(_text))

            case 'error':
                if len(_params) == 0 :
                    print(red.bold('[ERROR]'), red(_text))
                else:
                    print(red.bold('[ERROR]'), red.bold(f'┌ {_text}'))
                    index: int = 1

                    for key, value in _params.items():
                        if index == len(_params):
                            print(red(f'\t\t└─── {key}: {value}'))

                        else:
                            print(red(f'\t\t├─── {key}: {value}'))

                        index += 1

    @classmethod
    def __print_separate_line(cls):
        cls.__print_to_file(f'{"="*90} \n', _type="SEPARATOR")

    @classmethod
    def success(cls, _msg: str):
        cls.__print_to_file(_msg, _type='success')
        cls.__print_to_console(_msg, _type='success')

    @classmethod
    def info(cls, _msg: str):
        cls.__print_to_file(_msg, _type='info')
        cls.__print_to_console(_msg, _type='info')

    @classmethod
    def warning(cls, _msg: str):
        cls.__print_to_file(_msg, _type='warning')
        cls.__print_to_console(_msg, _type='warning')

    @classmethod
    def error(cls, _msg: str, _params: dict={}):
        cls.__print_to_file(_msg, _type='error')
        cls.__print_to_console(_msg, _type='error', _params=_params)

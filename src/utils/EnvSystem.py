# File: EnvSystem.py
#
# A file created to retrieve data from .env files in a way that will make the code cleaner.
# In addition, we are able to use this class to immediately parse the data into the appropriate type, which I noticed
# that had not happened before. All "clean" fetched data was type <str>.

import os
from pathlib import Path
from dotenv import load_dotenv, find_dotenv
from src.utils.ParseSystem import ParseSystem


class EnvSystem:
    """
    A class responsible for handling <.env> files.
    It is a kind of helper for handling these files.

    Parameters:
        _fileName (str): The name of the file from which we want to obtain data. The full path is not necessary.
    """
    __fileName: str
    __path: Path

    # The constructor itself specifies the directory with the file, so we only enter the name of the file
    # from which we would like to extract data.
    @classmethod
    def __init__(cls, _fileName: str):
        cls.__fileName = _fileName
        cls.__path = Path('config/' + _fileName)

        if find_dotenv((cls.__path.__str__())):
            cls.__load_data()

    @classmethod
    def __load_data(cls) -> None:
        load_dotenv(dotenv_path=cls.__path)

    @classmethod
    def file_exist(cls) -> bool:
        """
        The method checks whether the file exists in the given location.

        Return:
             The method returns <True> when the file exists.
        """
        if find_dotenv(cls.__path.__str__()):
            return True

        return False

    @staticmethod
    def get_env_element(_nameElement: str) -> any:
        """
        The method retrieves the value matching the parameter from the opened file.

        Parameters:
            _nameElement (str): Label name from env file.

        Return:
            The method returns the given value which is appropriately parsed into the corresponding data type.
        """
        return ParseSystem.auto_parse(os.getenv(_nameElement))

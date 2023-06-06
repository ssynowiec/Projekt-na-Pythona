# File: FileSystem.py
#
# The class responsible for files and things related to them.

import os
import pathlib
from pathlib import Path


class FileSystem:
    """A class responsible for things related to files and directories."""

    @staticmethod
    def get_file_list(_pathToDir: str) -> list[str]:
        """
        A method that returns a list of files and directories in the specified location.

        Parameters:
            _pathToDir (str | path): Path to the directory.

        Return:
            The method returns a list of file and directory names.
        """
        return os.listdir(_pathToDir)

    @staticmethod
    def get_sort_file_list(_pathToDir: str) -> list[str]:
        """
        A method that returns a sort list of files and directories in the specified location.

        Parameters:
            _pathToDir (str | path): Path to the directory.

        Return:
            The method returns a sorted list of file and directory names.
        """
        return sorted(FileSystem.get_file_list(_pathToDir))

    @staticmethod
    def delete_file(_pathToFile: str) -> None:
        """
        A method that removes a file from the specified location.

        Parameters:
            _pathToFile (str | path): The path leading to the file.
        """
        os.remove(_pathToFile)

    @staticmethod
    def exist_file( _pathToFile) -> bool:
        """
        A method that checks the existence of the specified file.

        Parameters:
            _pathToFile (str | path): The path leading to the file.

        Return:
            The method returns <True> when the file exists in the specified location.
        """
        return os.path.exists(_pathToFile)

    @staticmethod
    def create_dir(_dirPath: str) -> None:
        os.makedirs(_dirPath, exist_ok=True)

    @staticmethod
    def get_root_folder() -> Path:
        """
        A method that returns the path to the root directory.

        Return:
            The method returns the absolute path to the root directory.
        """
        return pathlib.Path(__file__).parent.parent.parent

    @staticmethod
    def write(_filePath: str, _msg: str):
        with open(_filePath, 'a') as file:
            file.write(_msg)

import os
import pathlib
from src.utils.FileSystem import FileSystem


class TEST_FileSystem:
    rootPath: pathlib.Path
    fileName: str

    @classmethod
    def setup_class(cls):
        cls.rootPath = pathlib.Path(__file__).parent.parent.parent
        cls.fileName = 'test.txt'

        open(cls.fileName, 'w')

    @classmethod
    def teardown_class(cls):
        os.remove(cls.fileName)
        os.rmdir(cls.rootPath.__str__() + '/test')

    @classmethod
    def CASE_get_file_list(cls):
        assert FileSystem.get_file_list(cls.rootPath.__str__()) == \
               os.listdir(cls.rootPath)

    @classmethod
    def CASE_get_sort_file_list(cls):
        assert FileSystem.get_sort_file_list(cls.rootPath.__str__()) == \
               sorted(os.listdir(cls.rootPath))

    @classmethod
    def CASE_exist_file(cls):
        assert FileSystem.exist_file(cls.fileName)

    @classmethod
    def CASE_delete_file(cls):
        FileSystem.delete_file(cls.fileName)
        assert not os.path.exists(cls.fileName)

    @classmethod
    def CASE_get_root_path(cls):
        assert FileSystem.get_root_folder() == cls.rootPath

    @classmethod
    def CASE_create_dir(cls):
        FileSystem.create_dir(cls.rootPath.__str__() + '/test')
        assert os.path.exists(cls.rootPath.__str__() + '/test')

    @classmethod
    def CASE_write(cls):
        FileSystem.write(cls.fileName, 'test')
        assert os.path.exists(cls.fileName)

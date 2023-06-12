from src.utils.EnvSystem import EnvSystem


class TEST_EnvSystem:
    env: EnvSystem

    @classmethod
    def setup_class(cls):
        cls.env = EnvSystem('serverConfig.env')

    @classmethod
    def teardown_class(cls):
        pass

    @classmethod
    def CASE_file_exist(cls):
        assert cls.env.file_exist()

    @classmethod
    def CASE_get_env_element(cls):
        assert cls.env.get_env_element('SERVER_HOST') == 'localhost'

    @classmethod
    def CASE_get_env_element_error(cls):
        assert not cls.env.get_env_element('ERROR_ELEMENT') == 'ERROR'

from src.utils.ParseSystem import ParseSystem


class TEST_ParseSystem:
    @classmethod
    def CASE_auto_parse_string_to_int(cls):
        assert ParseSystem.auto_parse('1') == 1

    @classmethod
    def CASE_auto_parse_string_to_float(cls):
        assert ParseSystem.auto_parse('1.0') == 1.0

    @classmethod
    def CASE_auto_parse_string_to_bool(cls):
        assert ParseSystem.auto_parse('True') == True

    @classmethod
    def CASE_auto_parse_string_to_none(cls):
        assert ParseSystem.auto_parse('None') is None

    @classmethod
    def CASE_auto_parse_string_to_list(cls):
        assert ParseSystem.auto_parse('[1, 2, 3]') == [1, 2, 3]

    @classmethod
    def CASE_auto_parse_string_to_dict(cls):
        assert ParseSystem.auto_parse('{"a": 1, "b": 2, "c": 3}') == {'a': 1, 'b': 2, 'c': 3}

    @classmethod
    def CASE_auto_parse_string_to_tuple(cls):
        assert ParseSystem.auto_parse('(1, 2, 3)') == (1, 2, 3)

    @classmethod
    def CASE_auto_parse_string_to_set(cls):
        assert ParseSystem.auto_parse('{1, 2, 3}') == {1, 2, 3}

    @classmethod
    def CASE_auto_parse_string_to_frozenset(cls):
        assert ParseSystem.auto_parse('{1, 2, 3}') == frozenset({1, 2, 3})

    @classmethod
    def CASE_auto_parse_other_type(cls):
        assert ParseSystem.auto_parse(1) == 1
        assert ParseSystem.auto_parse(1.0) == 1.0
        assert ParseSystem.auto_parse(True) == True
        assert ParseSystem.auto_parse(None) is None
        assert ParseSystem.auto_parse([1, 2, 3]) == [1, 2, 3]
        assert ParseSystem.auto_parse({'a': 1, 'b': 2, 'c': 3}) == {'a': 1, 'b': 2, 'c': 3}
        assert ParseSystem.auto_parse(frozenset({1, 2, 3})) == frozenset({1, 2, 3})



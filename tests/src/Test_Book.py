from src.api.functions.book import Book


class TEST_Book:
    @classmethod
    def CASE_get_with_details_ok(cls):
        assert Book.get_with_details(1)['title'] == 'Harry Potter i Kamień Filozoficzny'

    @classmethod
    def CASE_get_with_details_error_1(cls):
        assert Book.get_with_details(0) == {'error': "'bool' object is not a mapping"}

    @classmethod
    def CASE_get_with_details_error_2(cls):
        assert Book.get_with_details(-1) == {'error': "'bool' object is not a mapping"}

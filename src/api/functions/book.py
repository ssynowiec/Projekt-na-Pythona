import sqlite3

from src.database.db_connection import DbConnection


class Book:
    __author: int
    __publisher: int
    __title: str
    __publication_date: str
    __genre: str
    __is_available: bool
    __number_of_pages: int
    __cover_image: str
    __ISBN: str

    @classmethod
    def __init__(cls,
                 _author: int,
                 _publisher: int,
                 _title: str,
                 _publication_date: str,
                 _genre: str,
                 _is_available: bool,
                 _number_of_pages: int,
                 _cover_image: str,
                 _ISBN: str):

        cls.__author = _author
        cls.__publisher = _publisher
        cls.__title = _title
        cls.__publication_date = _publication_date
        cls.__genre = _genre
        cls.__is_available = _is_available
        cls.__number_of_pages = _number_of_pages
        cls.__cover_image = _cover_image
        cls.__ISBN = _ISBN

    @classmethod
    def add_book(cls,
                 _author: int,
                 _publisher: int,
                 _title: str,
                 _publication_date: str,
                 _genre: str,
                 _is_available: bool,
                 _number_of_pages: int,
                 _cover_image: str,
                 _ISBN: str):

        cls.__author = _author
        cls.__publisher = _publisher
        cls.__title = _title
        cls.__publication_date = _publication_date
        cls.__genre = _genre
        cls.__is_available = _is_available
        cls.__number_of_pages = _number_of_pages
        cls.__cover_image = _cover_image
        cls.__ISBN = _ISBN

        conn = DbConnection().__open__()

        cursor = conn.cursor()
        cursor.execute("""INSERT INTO book 
            (author, publisher, title, publication_date, genre, is_available, number_of_pages, cover_image,ISBN) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                       (cls.__author,
                        cls.__publisher,
                        cls.__title,
                        cls.__publication_date,
                        cls.__genre,
                        cls.__is_available,
                        cls.__number_of_pages,
                        cls.__cover_image,
                        cls.__ISBN))

        return cls

    @classmethod
    def get_all(cls):
        cls.books = []

        try:
            conn = DbConnection().__open__()

            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM book')

            rows = cursor.fetchall()

            for row in rows:
                user = {'id': row['id'], 'title': row['title']}
                cls.books.append(user)

        except Exception as _e:
            return {'message': 'Error connecting to database: ' + str(_e)}

        return cls.books

    @classmethod
    def get_by_id(cls, _ID):
        cls.book = {}

        try:
            conn = DbConnection().__open__()

            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM book WHERE id = ?', (_ID,))

            row = cursor.fetchone()

            cls.book = {'id': row['id'], 'title': row['title']}

        except Exception as _e:
            return {'message': 'Error connecting to database: ' + str(_e)}

        return cls.book

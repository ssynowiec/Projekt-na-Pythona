import sqlite3

from src.database.db_connection import DbConnection


class Book:
    author: int
    publisher: int
    title: str
    publication_date: str
    genre: str
    is_available: bool
    number_of_pages: int
    cover_image: str
    ISBN: str

    @classmethod
    def __init__(cls, author, publisher, title, publication_date, genre, is_available, number_of_pages, cover_image,
                 ISBN):
        cls.author = author
        cls.publisher = publisher
        cls.title = title
        cls.publication_date = publication_date
        cls.genre = genre
        cls.is_available = is_available
        cls.number_of_pages = number_of_pages
        cls.cover_image = cover_image
        cls.ISBN = ISBN

    @classmethod
    def add_book(cls, author, publisher, title, publication_date, genre, is_available, number_of_pages, cover_image,
                 ISBN):
        cls.author = author
        cls.publisher = publisher
        cls.title = title
        cls.publication_date = publication_date
        cls.genre = genre
        cls.is_available = is_available
        cls.number_of_pages = number_of_pages
        cls.cover_image = cover_image
        cls.ISBN = ISBN
        conn = DbConnection().__open__()
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO book (author, publisher, title, publication_date, genre, is_available, number_of_pages, cover_image,
                 ISBN) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""", (cls.author, cls.publisher, cls.title, cls.publication_date, cls.genre, cls.is_available, cls.number_of_pages, cls.cover_image, cls.ISBN))
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
        except Exception as e:
            return {'message': 'Error connecting to database: ' + str(e)}

        return cls.books

    @classmethod
    def get_by_id(cls, id):
        cls.book = {}
        try:
            conn = DbConnection().__open__()
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM book WHERE id = ?', (id,))
            row = cursor.fetchone()
            cls.book = {'id': row['id'], 'title': row['title']}
        except Exception as e:
            return {'message': 'Error connecting to database: ' + str(e)}

        return cls.book

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

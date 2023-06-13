import sqlite3

from src.database.db_connection import DbConnection
from src.database.db_object import DatabaseObject


class Book(DatabaseObject):
    def __init__(self, **kwargs: dict):
        self.id = kwargs.get('id')
        self.author_id = kwargs.get('author_id')
        self.publisher_id = kwargs.get('publisher_id')
        self.title = kwargs.get('title')
        self.description = kwargs.get('description')
        self.publication_date = kwargs.get('publication_date')
        self.genre = kwargs.get('genre')
        self.is_available = kwargs.get('is_available')
        self.number_of_pages = kwargs.get('number_of_pages')
        self.cover_image = kwargs.get('cover_image')
        self.ISBN = kwargs.get('ISBN')

    @classmethod
    def get_with_details(cls, _id: int) -> dict:
        book = Book.get_by_id(_id)
        query = "SELECT author.name || ' ' || author.surname AS author, publisher.name as publisher FROM author, " \
                "book, publisher WHERE book.id = ? AND author.id = book.author_id AND publisher.id = book.publisher_id"

        try:
            conn = DbConnection().__open__()

            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(query, (_id,))

            row = cursor.fetchone()

            return {**book, **dict(row)}

        except Exception as e:
            print(f"Error getting object from database: {str(e)}")
            return {"error": str(e)}

        finally:
            DbConnection().__close__()

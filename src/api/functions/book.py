from src.database.db_object import DatabaseObject


class Book(DatabaseObject):
    def __init__(self, **kwargs):
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

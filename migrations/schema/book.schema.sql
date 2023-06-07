CREATE TABLE book (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    author_id INTEGER NOT NULL,
    publisher_id INTEGER NOT NULL,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    publication_date DATE NOT NULL,
    genre VARCHAR(255) NOT NULL,
    is_available TEXT NOT NULL,
    number_of_pages INTEGER NOT NULL,
    cover_image TEXT NOT NULL,
    ISBN VARCHAR(255) NOT NULL,

    FOREIGN KEY (author_id) REFERENCES author(id),
    FOREIGN KEY (publisher_id) REFERENCES publisher(id)
);

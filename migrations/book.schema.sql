DROP TABLE IF EXISTS book;

CREATE TABLE book (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    author INTEGER NOT NULL,
    publisher INTEGER NOT NULL,
    title VARCHAR(255) NOT NULL,
    publication_date DATE NOT NULL,
    genre VARCHAR(255) NOT NULL,
    is_available BOOLEAN NOT NULL,
    number_of_pages INTEGER NOT NULL,
    cover_image VARCHAR(255) NOT NULL,
    ISBN VARCHAR(255) NOT NULL,

    FOREIGN KEY (author) REFERENCES author(id),
    FOREIGN KEY (publisher) REFERENCES publisher(id)
);

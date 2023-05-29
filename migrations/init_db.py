import sqlite3

from src.api.functions.book import Book

connection = sqlite3.connect('database.db')

try:
    with open('./migrations/schema.sql') as f:
        connection.executescript(f.read())

    cur = connection.cursor()

    # insert some users
    cur.execute("INSERT INTO users (username) VALUES (?)", ('admin',))

    cur.execute("INSERT INTO users (username) VALUES (?)", ('demo',))

    with open('./migrations/book.schema.sql') as f:
        connection.executescript(f.read())
    # insert some books
    Book.add_book(1, 1, 'Harry Potter i Kamień Filozoficzny', '1997-06-26', 'Fantastyka', 1, 336, 'harry_potter.jpg',
                  '9788700631625')
    Book.add_book(2, 2, 'Zabić drozda', '1960-07-11', 'Fikcja', 1, 281, 'zabic_drozda.jpg', '9780060935467')
    Book.add_book(3, 3, '1984', '1949-06-08', 'Science Fiction', 1, 328, '1984.jpg', '9780451524935')
    Book.add_book(4, 4, 'Duma i uprzedzenie', '1813-01-28', 'Romans', 1, 279, 'duma_i_uprzedzenie.jpg', '9780141439518')
    Book.add_book(5, 5, 'Wielki Gatsby', '1925-04-10', 'Klasyczna', 1, 218, 'wielki_gatsby.jpg', '9780141182636')

    connection.commit()
    print("User table created successfully")
except Exception as e:
    print("User table creation failed", e)
finally:
    connection.close()

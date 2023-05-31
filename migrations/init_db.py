import sqlite3

connection = sqlite3.connect('database.db')
connection.execute("PRAGMA foreign_keys = 1")

try:
    print("Creating database...")

    with open('./migrations/schema.sql') as f:
        connection.executescript(f.read())

    print("User table created successfully")

    with open('./migrations/book.schema.sql') as f:
        connection.executescript(f.read())

    print("Book table created successfully")

    with open('./migrations/publisher.schema.sql') as f:
        connection.executescript(f.read())

    print("Publisher table created successfully")

    with open('./migrations/author.schema.sql') as f:
        connection.executescript(f.read())

    print("Author table created successfully")

    cur = connection.cursor()

    print("Inserting demo data into tables...")
    print("Inserting users...")
    # insert some users
    cur.execute("INSERT INTO users (username) VALUES (?)", ('admin',))
    cur.execute("INSERT INTO users (username) VALUES (?)", ('demo',))

    print("Inserting publishers...")
    # insert some publishers
    cur.execute("INSERT INTO publisher (name, address) VALUES (?, ?)", ('Media Rodzina', 'Adres wydawnictwa XYZ'))
    cur.execute("INSERT INTO publisher (name, address) VALUES (?, ?)", ('Harper Perennial', 'Adres wydawnictwa XYZ'))

    print("Inserting authors...")
    # insert some authors
    cur.execute("INSERT INTO author (name, surname, birth_date) VALUES (?, ?, ?)", ('J.K.', 'Rowling', '1965-07-31'))
    cur.execute("INSERT INTO author (name, surname, birth_date) VALUES (?, ?, ?)", ('Harper', 'Lee', '1926-04-28'))

    print("Inserting books...")
    cur.execute(
        "INSERT INTO book (author_id, publisher_id, title, publication_date, genre, is_available, number_of_pages, "
        "cover_image, ISBN) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (1, 1, 'Harry Potter i Kamień Filozoficzny', '1997-06-26', 'Fantastyka', 'True', 336, 'harry_potter.jpg',
         '9788700631625'))
    cur.execute(
        "INSERT INTO book (author_id, publisher_id, title, publication_date, genre, is_available, number_of_pages, "
        "cover_image, ISBN) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (2, 2, 'Zabić drozda', '1960-07-11', 'Fikcja', 'True', 281, 'zabic_drozda.jpg', '9780060935467'))

    connection.commit()
    print("Database created successfully")
except Exception as e:
    print("User table creation failed", e)
finally:
    connection.close()

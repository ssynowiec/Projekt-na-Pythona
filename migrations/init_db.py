import sqlite3

connection = sqlite3.connect('database.db')

try:
    print("Creating database...")

    with open('./migrations/schema.sql') as f:
        connection.executescript(f.read())

    print("User table created successfully")

    with open('./migrations/book.schema.sql') as f:
        connection.executescript(f.read())

    print("Book table created successfully")

    cur = connection.cursor()

    print("Inserting demo data into tables...")
    # insert some users
    cur.execute("INSERT INTO users (username) VALUES (?)", ('admin',))
    cur.execute("INSERT INTO users (username) VALUES (?)", ('demo',))

    cur.execute(
        "INSERT INTO book (author, publisher, title, publication_date, genre, is_available, number_of_pages, "
        "cover_image, ISBN) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (1, 1, 'Harry Potter i Kamień Filozoficzny', '1997-06-26', 'Fantastyka', 1, 336, 'harry_potter.jpg',
         '9788700631625'))
    cur.execute(
        "INSERT INTO book (author, publisher, title, publication_date, genre, is_available, number_of_pages, "
        "cover_image, ISBN) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (2, 2, 'Zabić drozda', '1960-07-11', 'Fikcja', 1, 281, 'zabic_drozda.jpg', '9780060935467'))

    connection.commit()
    print("Database created successfully")
except Exception as e:
    print("User table creation failed", e)
finally:
    connection.close()

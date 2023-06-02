import sqlite3
from simple_chalk import green, red, yellow

connection = sqlite3.connect('database.db')
connection.execute("PRAGMA foreign_keys = 1")

try:
    print(yellow("Creating database..."))

    with open('./migrations/schema/schema.sql') as f:
        connection.executescript(f.read())

    print(green.bold("[SUCCESS]") + green(" User table created successfully"))

    with open('./migrations/schema/book.schema.sql') as f:
        connection.executescript(f.read())

    print(green.bold("[SUCCESS]") + green(" Book table created successfully"))

    with open('./migrations/schema/publisher.schema.sql') as f:
        connection.executescript(f.read())

    print(green.bold("[SUCCESS]") + green(" Publisher table created successfully"))

    with open('./migrations/schema/author.schema.sql') as f:
        connection.executescript(f.read())

    print(green.bold("[SUCCESS]") + green(" Author table created successfully"))

    cur = connection.cursor()

    print(yellow("Inserting demo data into tables..."))
    print(yellow("Inserting users..."))
    # insert some users
    cur.execute("INSERT INTO users (username) VALUES (?)", ('admin',))
    cur.execute("INSERT INTO users (username) VALUES (?)", ('demo',))

    print(yellow("Inserting publishers..."))
    # insert some publishers
    cur.execute("INSERT INTO publisher (name, address) VALUES (?, ?)", ('Media Rodzina', 'Adres wydawnictwa XYZ'))
    cur.execute("INSERT INTO publisher (name, address) VALUES (?, ?)", ('Harper Perennial', 'Adres wydawnictwa XYZ'))

    print(yellow("Inserting authors..."))
    # insert some authors
    cur.execute("INSERT INTO author (name, surname, birth_date) VALUES (?, ?, ?)", ('J.K.', 'Rowling', '1965-07-31'))
    cur.execute("INSERT INTO author (name, surname, birth_date) VALUES (?, ?, ?)", ('Harper', 'Lee', '1926-04-28'))

    print(yellow("Inserting books..."))
    cur.execute(
        "INSERT INTO book (author_id, publisher_id, title, description, publication_date, genre, is_available, "
        "number_of_pages, cover_image, ISBN) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (
            1,
            1,
            'Harry Potter i Kamień Filozoficzny',
            '"Harry Potter i Kamień Filozoficzny" to pierwsza część niezwykle popularnej serii książek napisanych przez J.K. Rowling. Opowieść rozpoczyna się, gdy sierota o imieniu Harry Potter dowiaduje się, że jest czarodziejem i zostaje przyjęty do Hogwartu, szkoły magii i czarodziejstwa. Wraz z przyjaciółmi Hermioną Granger i Ronem Weasleyem, Harry wchodzi w świat pełen tajemnic, magii i niebezpieczeństw. Głównym wątkiem książki jest poszukiwanie tajemniczego Kamienia Filozoficznego, który daje niezwykłą moc swojemu posiadaczowi. Czy Harry i jego przyjaciele zdołają odkryć tajemnice, które kryje szkoła i pokonać złego Lorda Voldemorta? \'"Harry Potter i Kamień Filozoficzny" to fascynująca i pełna przygód historia, która wprowadza czytelników w magiczny świat Hogwartu.\'',
            '1997-06-26',
            'Fantastyka',
            'True',
            336,
            'harry_potter.jpg',
            '9788700631625'
        )
    )

    cur.execute(
        "INSERT INTO book (author_id, publisher_id, title, description, publication_date, genre, is_available, number_of_pages, cover_image, ISBN) VALUES (?, ?, ? ,?, ?, ?, ?, ?, ?, ?)",
        (2, 2, 'Zabić drozda', 'To jest opis', '1960-07-11', 'Fikcja', 'True', 281, 'zabic_drozda.jpg', '9780060935467'))

    connection.commit()
    print(green.bold("[SUCCESS]") + green.bold(" Database created successfully"))
except Exception as e:
    print(red.bold("[ERROR]") + red.bold(" User table creation failed:"), red(e))
finally:
    connection.close()

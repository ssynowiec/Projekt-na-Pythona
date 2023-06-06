from src.database.SQLite import SQLite
from simple_chalk import green, red, yellow


def init_db():
    print(yellow("Creating database..."))

    sql = SQLite('database.db')
    sql.load_all_exist_schema()

    print(yellow("Inserting demo data into tables..."))
    print(yellow("Inserting users..."))
    # insert some users
    sql.execute("INSERT INTO users (username) VALUES (?)", ('admin',))
    sql.execute("INSERT INTO users (username) VALUES (?)", ('demo',))

    print(yellow("Inserting publishers..."))
    # insert some publishers
    sql.execute("INSERT INTO publisher (name, address) VALUES (?, ?)", ('Media Rodzina', 'Adres wydawnictwa XYZ'))
    sql.execute("INSERT INTO publisher (name, address) VALUES (?, ?)", ('Harper Perennial', 'Adres wydawnictwa XYZ'))

    print(yellow("Inserting authors..."))
    # insert some authors
    sql.execute("INSERT INTO author (name, surname, birth_date) VALUES (?, ?, ?)", ('J.K.', 'Rowling', '1965-07-31'))
    sql.execute("INSERT INTO author (name, surname, birth_date) VALUES (?, ?, ?)", ('Harper', 'Lee', '1926-04-28'))

    print(yellow("Inserting books..."))
    sql.execute(
        "INSERT INTO book (author_id, publisher_id, title, description, publication_date, genre, is_available, "
        "number_of_pages, cover_image, ISBN) "
        "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
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

    sql.execute("INSERT INTO book (author_id, publisher_id, title, description, publication_date, genre, is_available, number_of_pages, cover_image, ISBN) "
                "VALUES (?, ?, ? ,?, ?, ?, ?, ?, ?, ?)",
                (2, 2, 'Zabić drozda', 'To jest opis', '1960-07-11', 'Fikcja', 'True', 281, 'zabic_drozda.jpg', '9780060935467'))

    print(green.bold("[SUCCESS]") + green.bold(" Database created successfully"))

    sql.close()

CREATE TABLE reader (
    card_number VARCHAR(10) NOT NULL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    surname VARCHAR(50) NOT NULL,
    PESEL VARCHAR(11) NOT NULL,
    birthday DATE NOT NULL,
    phone_number VARCHAR(15) NOT NULL,
    address_street VARCHAR(50) NOT NULL,
    postal_code VARCHAR(6) NOT NULL,
    city VARCHAR(50) NOT NULL,
    citizenship VARCHAR(3) NOT NULL,
    login VARCHAR(50) NOT NULL,

    FOREIGN KEY (login) REFERENCES login_data(login)
)

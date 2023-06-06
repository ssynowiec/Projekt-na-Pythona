DROP TABLE IF EXISTS reader;
DROP TABLE IF EXISTS login_data;

CREATE TABLE login_data (
    login VARCHAR(50) NOT NULL PRIMARY KEY,
    email TEXT NOT NULL,
    password TEXT NOT NULL
);

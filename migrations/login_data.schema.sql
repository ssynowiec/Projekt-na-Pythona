DROP TABLE IF EXISTS login_data;

CREATE TABLE login_data (
    username TEXT NOT NULL PRIMARY KEY,
    email TEXT NOT NULL,
    password TEXT NOT NULL
);

DROP TABLE IF EXISTS users;

CREATE TABLE users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
nome VARCHAR(50) NOT NULL,
email VARCHAR(60) NOT NULL,
senha VARCHAR(50) NOT NULL
);

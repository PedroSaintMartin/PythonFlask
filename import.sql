PRAGMA foreign_keys = false;
DROP TABLE IF EXISTS user;
PRAGMA foreign_keys = true;

CREATE TABLE user(
    idUser INTEGER PRIMARY KEY AUTOINCREMENT,
    emailUser TEXT,
    nameUser TEXT,
    senhaUser TEXT
);

INSERT INTO user ("emailUser", "nameUser", "senhaUser") Values ("teste@teste.com", "teste", "teste123");
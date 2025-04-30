PRAGMA foreign_keys = false;
DROP TABLE IF EXISTS user;
PRAGMA foreign_keys = true;

CREATE TABLE user(
    idUser INTEGER PRIMARY KEY AUTOINCREMENT,
    emailUser TEXT,
    nomeUser TEXT,
    telefoneUser TEXT,
    senhaUser TEXT
);

INSERT INTO user ("emailUser", "nomeUser", "telefoneUser", "senhaUser") Values ("teste@teste.com", "teste", "249999999", "teste123");
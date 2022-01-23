DROP TABLE IF EXISTS expense;
DROP TABLE IF EXISTS expenses;
DROP TABLE IF EXISTS categories;
DROP TABLE IF EXISTS subcategories;
DROP TABLE IF EXISTS categories_income;
DROP TABLE IF EXISTS incomes;

CREATE TABLE expenses
(
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    date        TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    sum         REAL      NOT NULL,
    category    INTEGER   NOT NULL,
    subcategory INTEGER   NOT NULL,
    comment     TEXT

);

CREATE TABLE categories
(
    id    INTEGER PRIMARY KEY AUTOINCREMENT,
    name  TEXT NOT NULL,
    color TEXT,
    state TEXT DEFAULT false
);
CREATE TABLE subcategories
(
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    name        TEXT    NOT NULL,
    category_id INTEGER NOT NULL,
    state       TEXT DEFAULT false

);

CREATE TABLE categories_income
(
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    name       TEXT NOT NULL,
    primordial TEXT DEFAULT NULL,
    state      TEXT DEFAULT false
);

CREATE TABLE incomes
(
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    date     TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    amount   REAL      NOT NULL,
    category INTEGER   NOT NULL,
    comment  TEXT

);


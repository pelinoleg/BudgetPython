DROP TABLE IF EXISTS expense;
DROP TABLE IF EXISTS expenses;
DROP TABLE IF EXISTS categories;
DROP TABLE IF EXISTS subcategories;

CREATE TABLE expenses
(
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    date        TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    sum         REAL      NOT NULL,
    category    TEXT      NOT NULL,
    subcategory TEXT      NOT NULL,
    comment     TEXT

);

CREATE TABLE categories
(
    id    INTEGER PRIMARY KEY AUTOINCREMENT,
    name  TEXT NOT NULL,
    color TEXT
);
CREATE TABLE subcategories
(
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    name        TEXT NOT NULL,
    category_id TEXT NOT NULL

);
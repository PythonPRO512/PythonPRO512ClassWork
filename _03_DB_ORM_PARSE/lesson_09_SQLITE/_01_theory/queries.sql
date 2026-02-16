CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER);

INSERT INTO students (name, age, course)
VALUES (?, ?, ?)
("Иван Иванов", 20, "Математика")

CREATE DATABASE booksfromitfield;

CREATE TABLE subgenres (
    id INT AUTO_INCREMENT PRIMARY KEY,
    subgenre VARCHAR(255) NOT NULL
);

CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    book VARCHAR(255) NOT NULL,
    description TEXT
);

CREATE TABLE booksintosubgenres (
    id INT AUTO_INCREMENT PRIMARY KEY,
    subgenre_id INT,
    book_id INT,
    FOREIGN KEY (subgenre_id) REFERENCES subgenres(id),
    FOREIGN KEY (book_id) REFERENCES books(id)
)

INSERT INTO subgenres (subgenre) VALUES
('Cyber security'),
('Software testing'),
('Programming');

ALTER TABLE books
ADD COLUMN author VARCHAR(255);

INSERT INTO books (book, description, author) VALUES
('testikirja1', 'testikuvaus', 'testikirjailija'),
('testikirja2', 'kuvaus', 'kirjailija'),
('kirja3', 'kuvaus', 'kirjailija'),
('kirja4', 'kuvaus', 'kirjailija2');

INSERT INTO booksintosubgenres (subgenre_id, book_id) VALUES
(3, 1),
(3, 2),
(2, 3),
(1, 4);
-- CREATE DATABASE IF NOT EXISTS extra_exercise;

-- Basic Tables, no inter-relationships

CREATE TABLE IF NOT EXISTS person (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS book (
    id SERIAL PRIMARY KEY,
    year INT NOT NULL,
    title VARCHAR(300) NOT NULL
);

-- INSERT INTO person (first_name, last_name) VALUES 
-- ('John', 'Doe'),
-- ('Jane', 'Doe'),
-- ('Jacob', 'Dintu'),
-- ('Martine', 'Raszy');

-- INSERT INTO book (year, title) VALUES 
-- (2010, 'Help'),
-- (2011, 'The fifth element'),
-- (2012, 'The fifteenth murder'),
-- (2013, 'Learning Python: The dummy guide to Python'),
-- (2014, 'The Art of Not Giving a FUCK');

SELECT * FROM person;
SELECT * FROM book;

-- One to one relationship
-- 1 person can only have 1 favorite book
-- 1 book can only be the favorite of 1 person

-- CREATE TABLE IF NOT EXISTS person (
--     id SERIAL PRIMARY KEY,
--     first_name VARCHAR(100) NOT NULL,
--     last_name VARCHAR(100) NOT NULL,
--     favorite_book INT,
--     FOREIGN KEY (favorite_book) REFERENCES book(id)
-- );

-- ALTER TABLE person
-- ADD favorite_book INT;

-- ALTER TABLE person ADD CONSTRAINT fk_fav_book FOREIGN KEY
-- (favorite_book) REFERENCES book(id);

UPDATE person SET favorite_book=4 WHERE first_name = 'John' AND last_name = 'Doe';
UPDATE person SET favorite_book=1 WHERE first_name = 'Martine' AND last_name = 'Raszy' AND id = 8;
UPDATE person SET favorite_book=2 WHERE id = 1;

SELECT * FROM person;

-- One to Many relationship
-- 1 person can only have 1 favorite book
-- 1 book can only be the favorite of many persons

UPDATE person SET favorite_book=4 WHERE favorite_book IS NULL;

SELECT * FROM person;


-- Many to Many relationship
-- 1 person can only have 1 favorite book (irrelevant to the new many:many)
-- 1 book can only be the favorite of many persons (irrelevant to the new many:many)
-- 1 book can be written by many persons (relevant to the new many:many)
-- 1 person can write many books (relevant to the new many:many)

CREATE TABLE author (
    id SERIAL PRIMARY KEY,
    person_id INT,
    book_id INT,
    FOREIGN KEY (person_id) REFERENCES person(id),
    FOREIGN KEY (book_id) REFERENCES book(id)
);

INSERT INTO author (person_id, book_id) VALUES 
(3, 6);

INSERT INTO author (person_id, book_id) VALUES
(
    (SELECT id FROM person_id WHERE id = 7 AND first_name = 'Jacob'),
    (SELECT id FROM book_id WHERE id = 5 AND title = 'The Art of Not Giving a FUCK')
);

-- I want to display
-- first_name, last_name, book_authored_title

SELECT first_name, last_name FROM person;
SELECT title FROM book;

-- Method 1
SELECT person.first_name, person.last_name, book.title
FROM person
INNER JOIN author ON author.person_id = person.id
INNER JOIN book ON author.book_id = book.id;

-- Method 2
SELECT person.first_name, person.last_name, book.title
FROM author
INNER JOIN person ON person.id = author.person_id
INNER JOIN book ON book.id = author.book_id;


-- I want to display
-- first_name, last_name, book_authored_title
-- and the book has to be 'The Art of Not Giving a FUCK'

SELECT person.first_name, person.last_name, book.title
FROM author
INNER JOIN person ON person.id = author.person_id
INNER JOIN book ON book.id = author.book_id
WHERE book.title = 'The Art of Not Giving a FUCK';
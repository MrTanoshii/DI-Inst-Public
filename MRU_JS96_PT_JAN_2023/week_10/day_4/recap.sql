-- CREATE DATABASE test_db;

-- Table student
---- id (PK)
---- first_name
---- last_name

-- Table class
---- id
---- label

-- Table instructor
---- id
---- first_name
---- last_name

-- Character
---- Adv, fixed
CHAR(50)
----  "Jayshen", 7 characters | 50 stored
---- "Jean Luc", 8 characters | 50 stored
-- Varying character
---- Adv, takes up less hdd/ram/ssd space
VARCHAR(50)
---- "Jayshen", 7 characters | 7 stored
---- "Jean Luc", 8 characters | 8 stored

-- CREATE TABLE IF NOT EXISTS student(
-- 	id SERIAL PRIMARY KEY,
-- 	first_name VARCHAR(50),
-- 	last_name VARCHAR(50)
-- );

-- INSERT INTO student (first_name, last_name)
-- VALUES 
-- 	('Ashley', 'Sookaye'),
-- 	('Yvan', 'Sidien')
-- RETURNING *;

SELECT 
	id, 
	first_name AS "First Name", 
	last_name AS "Last Name"
FROM student;


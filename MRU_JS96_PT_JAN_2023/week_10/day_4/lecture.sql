
------------------------------------

-- SELECT id AS "sIndex", first_name, last_name
-- FROM student
-- ORDER BY "sIndex" DESC;

-- SELECT COUNT(*) FROM student;
-- SELECT SUM(id) FROM student;
-- SELECT MAX(id) FROM student;
-- SELECT MIN(id) FROM student;
-- SELECT AVG(id) FROM student;
-- SELECT STDDEV(id) FROM student;
-- SELECT VARIANCE(id) FROM student;

-- SELECT DISTINCT first_name AS "First Name", last_name FROM student;

-- -- INSERT INTO student (first_name, last_name) VALUES ('Ashley', 'Leung');

-- SELECT DISTINCT ON (first_name, last_name) * FROM student;

-- SELECT * FROM student
-- WHERE id = 9;

-- SELECT * FROM student
-- WHERE first_name = 'Jean Luc';

-- SELECT * FROM student
-- WHERE first_name LIKE '%a%';

-- SELECT * FROM student
-- WHERE first_name NOT IN ('Ashley', 'Yvan');

-- SELECT * FROM student
-- WHERE id BETWEEN 0 AND 3;

-- SELECT COUNT(*), first_name FROM student
-- GROUP BY(first_name);

-- SELECT * FROM student;

-- UPDATE student
-- SET first_name = 'Vincent'
-- WHERE id = 10;

-- SELECT * FROM student;

-- UPDATE student
-- SET first_name = 'Jean-Luc'
-- WHERE first_name = 'Jean Luc'
-- RETURNING *;

-- UPDATE student
-- SET first_name = 'Jean Luc'
-- WHERE id = (
-- 	SELECT id FROM student
-- 	WHERE first_name = 'Jean-Luc'
-- )
-- RETURNING *;

-- SELECT * FROM student;

-- -- INSERT INTO student (first_name, last_name)
-- -- VALUES 
-- -- 	('Ty-Na', 'Malala'),
-- -- 	('Previn', 'Appadu')
-- -- RETURNING *;

-- -- DELETE FROM student
-- -- WHERE first_name = 'Vincent';

-- -- TRUNCATE student RESTART IDENTITY;

-- SELECT * FROM student;

-- -- ALTER TABLE student
-- -- ALTER COLUMN first_name TYPE INT;


-- -- ALTER TABLE student
-- -- RENAME first_name TO fname;

-- -- INSERT INTO student (first_name, last_name)
-- -- VALUES 
-- -- 	('Ashley', 'Sookaye'),
-- -- 	('Yvan', 'Sidien')
-- -- RETURNING *;

-- -- ALTER TABLE student
-- -- ADD COLUMN age INT;

-- UPDATE student
-- SET age = 18 WHERE last_name = 'Malala';

-- UPDATE student
-- SET age = 30 WHERE age IS NOT NULL;

-- SELECT * FROM student;

DROP TABLE IF EXISTS student;

UPDATE actors
SET  first_name = 'Maty'
WHERE first_name = 'Matt'
RETURNING *;

ALTER actors
ALTER COLUMN 
RENAME age TO "birthdate";

------------------------------

-- -- Insert into student first name 'Jayshen' and last name 'Patel' twice.

-- INSERT INTO student (first_name, last_name)
-- VALUES
-- 	('Jayshen', 'Patel'),
-- 	('Jayshen', 'Patel')
-- RETURNING *;


-- -- Insert into student first name 'Jayshen', last name 'Patel' and pet name is 'Alfie'.

-- INSERT INTO student (first_name, last_name, pet_name)
-- VALUES
-- 	('Jayshen', 'Patel', 'Alfie')
-- RETURNING *;

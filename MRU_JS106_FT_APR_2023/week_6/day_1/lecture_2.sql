-- DROP DATABASE testest;
-- CREATE DATABASE IF NOT EXISTS testtest;
-- CREATE DATABASE testtest;

-- DROP TABLE IF EXISTS students;

CREATE TABLE IF NOT EXISTS students (
	id SERIAL PRIMARY KEY,
	firstName VARCHAR(100),
	lastName VARCHAR(100),
	dob DATE,
	grade FLOAT NOT NULL DEFAULT 0
);

INSERT INTO students (firstName, lastName, grade) VALUES 
	('Vincent', 'Leung', 5),
	('Nilesh', 'Bapamah', 8)
;

-- SELECT * FROM public.students
-- ORDER BY firstName DESC;

-- SELECT firstName AS "first name", lastName AS "skrdgmlesurv34985793487589345tjksrhdvkj" FROM students
-- ORDER BY "skrdgmlesurv34985793487589345tjksrhdvkj" DESC;

INSERT INTO students (firstName, lastName) VALUES 
	('Blessing', 'Ebangit'),
	('Dhivyesh', 'Golam'),
	('Tushil', 'Gunness'),
	('Khavind', 'Jhurry'),
	('Abeenesh', 'Goreeba'),
	('Ty-na', 'Malala'),
	('Sanjiv', NULL)
RETURNING *;

-- SELECT * FROM students WHERE firstName = 'Sanjiv';
-- SELECT * FROM students WHERE firstName LIKE '%esh';

-- UPDATE students
-- SET lastName = 'Putty'
-- WHERE firstName = 'Sanjiv';

-- UPDATE students
-- SET grade = 5
-- WHERE dob IS NULL;

-- Find all students that have the firstName 'Tushil' and have the grade of 50
SELECT * FROM students
WHERE firstName = 'Tushil'
AND grade = 50;

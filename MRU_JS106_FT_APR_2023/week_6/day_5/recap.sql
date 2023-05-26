-- table1: id, first_name
-- table2: id, no_of_cars

SELECT table1.id
FROM table1
FULL JOIN table2;



-- persons: id, first_name, last_name
-- pets: id, pet_name, person_id (FK REF persons.id)



-- student: id, full_name, school_id(s)
-- school: id, school_name, (student_id(s))

-- 1:1
-- 1 student attends 1 school
-- CREATE TABLE IF NOT EXISTS school (
--     id SERIAL PRIMARY KEY,
--     school_name VARCHAR(100)
--     -- student_id INT,
--     -- CONSTRAINT FK_school_student FOREIGN KEY (student_id) REFERENCES student(id)
-- );

-- CREATE TABLE IF NOT EXISTS student (
--     id SERIAL PRIMARY KEY,
--     full_name VARCHAR(300),
--     school_id INT,
--     CONSTRAINT FK_student_school FOREIGN KEY (school_id) REFERENCES school(id)
-- );

-- SELECT * FROM student;


-- 1:many
-- 1 school is attended by multiple students
-- CREATE TABLE IF NOT EXISTS school (
--     id SERIAL PRIMARY KEY,
--     school_name VARCHAR(100)
-- );

-- CREATE TABLE IF NOT EXISTS student (
--     id SERIAL PRIMARY KEY,
--     full_name VARCHAR(300),
--     school_id INT,
--     CONSTRAINT FK_student_school FOREIGN KEY (school_id) REFERENCES school(id)
-- );

-- SELECT * FROM student;


-- many:many
-- 1 students can attend multiple schools
-- 1 school is attended by multiple students
CREATE TABLE IF NOT EXISTS school (
    id SERIAL PRIMARY KEY,
    school_name VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS student (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(300),
);

CREATE TABLE IF NOT EXISTS school_student {
    id SERIAL PRIMARY KEY,
    student_id INT,
    school_id INT,
    CONSTRAINT FK_ss_student FOREIGN KEY (student_id) REFERENCES student(id),
    CONSTRAINT FK_ss_school FOREIGN KEY (school_id) REFERENCES school(id),
}

SELECT * FROM school_student;

INSERT INTO school (school_name) VALUES
('Developers Institute'), ('College Lapli');

INSERT INTO student (full_name) VALUES
('Blessing'), -- DI
('You guys'), -- CL
('Tushil'), -- DI
('Khavind'), -- DI
('Jatin'), -- CL
('Dhivyesh'), -- CL
('AwakeAbeenesh'); -- CL

INSERT INTO school_student (student_id, school_id)
VALUES
    -- End result: (1, 1)
    (
        (SELECT id FROM student
            WHERE full_name = 'Blessing'), 
        (SELECT id FROM school
            WHERE school_name = 'Developers Institute')
    ),
    (
        (SELECT id FROM student
            WHERE full_name = 'You guys'), 
        (SELECT id FROM school
            WHERE school_name = 'College Lapli')
    );

-- PRIMARY KEY of table, Student name, School name
SELECT school_student.id, student.full_name AS "Student Name", school.school_name AS "School Name"
FROM student
INNER JOIN school_student ON student.id = school_student.student_id
INNER JOIN school ON school.id = school_student.school_id;

-- SELECT the same values but only with unique student names
SELECT DISTINCT school_student.id, student.full_name AS "Student Name", school.school_name AS "School Name"
FROM student
INNER JOIN school_student ON student.id = school_student.student_id
INNER JOIN school ON school.id = school_student.school_id;

-- SELECT the same values but only with unique student names but still displaying the first school_student id
SELECT DISTINCT ON (student.full_name) school_student.id,
    student.full_name AS "Student Name",
    school.school_name AS "School Name"
FROM student
INNER JOIN school_student ON student.id = school_student.student_id
INNER JOIN school ON school.id = school_student.school_id;

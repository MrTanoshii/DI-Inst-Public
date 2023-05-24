-- -- Find all the students where there is a grade and the name ends with 'i' followed by any character.
-- SELECT * FROM students
-- WHERE 
-- 	grade IS NOT NULL
-- 	AND firstName LIKE '%i_';

-- -- Find the id, first name and grade from students where the last name contains an 'a' or the id is equal to 72.
-- SELECT id, firstName, grade FROM students
-- WHERE
-- 	lastName LIKE '%a%'
-- 	OR id = 72;

-- -- Find the last name and grade from students
-- -- where the grade is not equal to 0
-- SELECT lastName, grade FROM students WHERE grade != 0;
-- SELECT lastName, grade FROM students WHERE grade <> 0;

-- -- Find the students
-- -- where the first name is not equal to 'Vincent'
-- -- SELECT * FROM students
-- -- WHERE firstName != 'Vincent';
-- SELECT * FROM students
-- WHERE firstName <> 'Vincent';

-- LIMIT, OFFSET
SELECT * FROM students
LIMIT 10;

SELECT * FROM students
OFFSET 10
LIMIT 10;

SELECT * FROM students
OFFSET 20
LIMIT 10;

SELECT * FROM students
OFFSET 50
LIMIT 10;

-- -- JavaScript implementation of paginated images
-- let page_number = 0;
-- const pictures_per_page = 10;

-- SELECT * FROM pictures
-- OFFSET (page_number * pictures_per_page)
-- LIMIT pictures_per_page;
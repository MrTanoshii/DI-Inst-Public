CREATE DATABASE IF NOT EXISTS wk_6_day_3_exercise_xp;

USE wk_6_day_3_exercise_xp;

CREATE TABLE students
name char(100)
last_name varchar(100)
comment varchar(1000);

-- SELECT * FROM students;



-- Table STUDENTS
-- | id         |   name   | last_name | comment(int) |
-- |------------|----------|-----------|--------------|
-- | 1          |  John    | Doe       | NULL         |
-- | 1          |  John    | Doe       | 5            |
-- | 1          |  John    | Doe       | 10           |
-- | 1          |  John    | Doe       | 23           |
-- | 1          |  John    | Doe       | 678          |
-- | 1          |  John    | Doe       | 23           |

-- SELECT COUNT(comment)
-- FROM STUDENTS
-- WHERE comment NOT NULL; 
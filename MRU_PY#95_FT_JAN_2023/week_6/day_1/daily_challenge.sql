CREATE DATABASE IF NOT EXISTS  week_6_day_1;

SHOW DATABASES;

USE week_6_day_1;

-- MYSQL Version
-- CREATE TABLE actors(
--     actor_id int AUTO_INCREMENT PRIMARY KEY,
--     first_name varchar(50),
--     last_name VARCHAR (100) NOT NULL,
--     age DATE NOT NULL,
--     number_oscars SMALLINT NOT NULL
-- )

-- DROP TABLE actors;

-- POSTGRES Version
CREATE TABLE actors(
    actor_id SERIAL PRIMARY KEY,
    first_name VARCHAR (50) NOT NULL,
    last_name VARCHAR (100) NOT NULL,
    age DATE NOT NULL,
    number_oscars SMALLINT NOT NULL DEFAULT(0)
);

INSERT INTO actors(
    first_name,
    last_name,
    age,
    number_oscars
)
VALUES ('martine', 'raszy', '2021-10-17', 15);

-- 1.

SELECT * FROM actors;

SELECT COUNT(*) AS 'no_of_students' FROM actors;

-- 2.

-- This doesn't work
INSERT INTO actors(
    first_name,
    last_name,
    age,
    number_oscars
)
VALUES ('Sebastien', 'ArukeumCloseEnough', NULL, 20);


INSERT INTO actors(
    first_name,
    last_name,
    age
)
VALUES ('Sebastien', 'ArukeumCloseEnough', '2021-10-17');
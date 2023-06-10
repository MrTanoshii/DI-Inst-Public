-- CRUD
---- Create
---- Read
---- Update
---- Delete

-- Section Create
CREATE DATABASE <database_name>;

CREATE TABLE <table_name> (
    <column_name> <data_type> <constraint> -- PRIMARY KEY NOT NULL UNIQUE
    e.g. address VARCHAR(250)
);

INSERT INTO <table_name> (<column_name_1, column_name_2, ...>) VALUES
(value_1, value_2, ...) [RETURNING *];

-- Section Read

SELECT * FROM <table_name>;

SELECT * FROM <table_name> WHERE <column_name> = <value>;

SELECT table_name_1.first_name, table_name_1.last_name, table_name_2.job_title FROM <table_name_1>
INNER JOIN <table_name_2>
ON <table_name_2>.<table_name_1>_id = <table_name_1>.id;

SELECT <aggregate_func>(<column_name) FROM <table_name>;
-- Aggregate Func
---- SUM()
---- MIN()
---- MAX()
---- STD()
---- AVG()

-- Section Update

UPDATE first_name FROM <table_name>
WHERE first_name = 'Jean-Luc';

ALTER TABLE <table_name>
ADD <column_name> <data_type>; 

ALTER TABLE <table_name>
ALTER COLUMN <column_name> <new_data_type>; 
-- e.g. 
-- ALTER TABLE Persons
-- ALTER COLUMN first_name TINYTEXT; 

-- Section Delete

DROP DATABASE IF EXISTS <database_name>;

DROP TABLE IF EXISTS <table_name>;

DELETE FROM <table_name> WHERE first_name LIKE 'Yva_';

-- label
-- manufacturer
-- country
-- CREATE TABLE IF NOT EXISTS chocolate (
-- 	id SERIAL PRIMARY KEY,
-- 	label VARCHAR(100),
-- 	manufacturer VARCHAR(100),
-- 	country CHAR(60)
-- );

-- -- name
-- -- chocolate_label
-- CREATE TABLE IF NOT EXISTS glutton (
-- 	id SERIAL PRIMARY KEY,
-- 	name VARCHAR(100),
-- chocolate_label VARCHAR(100)
-- );

-- INSERT INTO chocolate (label, manufacturer, country) VALUES
-- 	('Toblerone', 'Mondelez International', 'Switzerland'),
-- 	('Cadbury', 'Mondelez International', 'England'),
-- 	('Lindt', 'Chocoladefabriken Lindt & Sprungli AG', 'Switzerland'),
-- 	('Mars', 'Mars, Incorporated', 'USA'),
-- 	('Ferrero Rocher', 'Ferrero SpA', 'Italy'),
-- 	('Robert', 'Chocolaterie Robert', 'Madagascar')
-- ;

-- INSERT INTO glutton (name, chocolate_label) VALUES
-- 	('Vincent', 'Lindt'),
-- 	('Vincent', 'Cadbury'),
-- 	('Safidy', 'Robert'),
-- 	('Melanie', 'Lindt'),
-- 	('Melanie', 'Ferrero Rocher')
-- 	('Naiza', 'ABC')
-- ;

-- -- SELECT * FROM glutton
-- SELECT glutton.id, glutton.name, glutton.chocolate_label AS chocolate, chocolate.manufacturer, chocolate.country FROM glutton
-- INNER JOIN chocolate
-- ON glutton.chocolate_label = chocolate.label;
-- -- WHERE name = 'Vincent';

-- SELECT glutton.id, glutton.name, glutton.chocolate_label AS chocolate, chocolate.manufacturer, chocolate.country FROM glutton
-- LEFT JOIN chocolate
-- ON glutton.chocolate_label = chocolate.label;

-- SELECT glutton.id, glutton.name, glutton.chocolate_label AS chocolate, chocolate.manufacturer, chocolate.country FROM glutton
-- RIGHT JOIN chocolate
-- ON glutton.chocolate_label = chocolate.label;

-- SELECT glutton.id, glutton.name, glutton.chocolate_label AS chocolate, chocolate.manufacturer, chocolate.country FROM glutton
-- FULL OUTER JOIN chocolate
-- ON glutton.chocolate_label = chocolate.label
-- WHERE chocolate.country ILIKE '%S%';

DROP TABLE IF EXISTS glutton;
DROP TABLE IF EXISTS chocolate;

CREATE TABLE IF NOT EXISTS chocolate (
	id SERIAL PRIMARY KEY,
	label VARCHAR(100),
	manufacturer VARCHAR(100),
	country CHAR(60)
);

CREATE TABLE IF NOT EXISTS glutton (
	id SERIAL PRIMARY KEY,
	name VARCHAR(100),
    chocolate_id INT DEFAULT(2),
-- 	FOREIGN KEY (chocolate_id) REFERENCES chocolate(id) ON DELETE SET NULL
-- 	FOREIGN KEY (chocolate_id) REFERENCES chocolate(id) ON DELETE CASCADE
-- 	FOREIGN KEY (chocolate_id) REFERENCES chocolate(id) ON DELETE RESTRICT
-- 	FOREIGN KEY (chocolate_id) REFERENCES chocolate(id) ON DELETE NO ACTION
	FOREIGN KEY (chocolate_id) REFERENCES chocolate(id) ON DELETE SET DEFAULT
);

INSERT INTO chocolate (label, manufacturer, country) VALUES
	('Toblerone', 'Mondelez International', 'Switzerland'),
	('Cadbury', 'Mondelez International', 'England'),
	('Lindt', 'Chocoladefabriken Lindt & Sprungli AG', 'Switzerland'),
	('Mars', 'Mars, Incorporated', 'USA'),
	('Ferrero Rocher', 'Ferrero SpA', 'Italy'),
	('Robert', 'Chocolaterie Robert', 'Madagascar')
;

INSERT INTO glutton (name, chocolate_id) VALUES
	('Vincent', 3),
	('Vincent', 2),
	('Safidy', 6),
	('Melanie', 3),
	('Melanie', 5),
	('Naiza', NULL)
;

DELETE FROM chocolate WHERE id = 5;

SELECT glutton.id, glutton.name, chocolate.label, chocolate.manufacturer, chocolate.country FROM glutton
FULL OUTER JOIN chocolate
ON glutton.chocolate_id = chocolate.id;

-- INSERT INTO glutton (chocolate_id, name) VALUES
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (3, 'Vincent'),
--     (2, 'Vincent'),
--     (6, 'Safidy'),
--     (3, 'Melanie'),
--     (5, 'Melanie'),
--     (NULL, 'Naiza')
-- ;

-- UPDATE glutton
-- SET name = 'Stefan'
-- WHERE name = 'Vincent';

-- SELECT glutton.id, glutton.name, chocolate.label, chocolate.manufacturer, chocolate.country FROM glutton
-- FULL OUTER JOIN chocolate
-- ON glutton.chocolate_id = chocolate.id;
-- -- Total query time: 62msec

CREATE TABLE movies (
  movie_id SERIAL,
  movie_title VARCHAR(45) NOT NULL,
  released_date date NOT NULL,
  PRIMARY KEY (movie_id)
);

/*
 one to one: a movie has one scenario
*/
CREATE TABLE scenarios (
  pk_movie_id INTEGER NOT NULL,
  scenario_story TEXT NOT NULL,
  PRIMARY KEY (pk_movie_id),
  CONSTRAINT fk_movie_id FOREIGN KEY (pk_movie_id) REFERENCES movies (movie_id)
);

INSERT into movies(movie_title, released_date) VALUES 
('Good Will Hunting', '1997-12-02'),
('The Martian', '2015-09-11'),
('Oceans Twelve', '2004-12-10'),
('Up in the Air', '2009-09-5');

INSERT into scenarios(pk_movie_id, scenario_story) VALUES 
(
    (
        SELECT movie_id FROM movies 
        where movie_title = 'Up in the Air'
    ),
    'Ryan Bingham enjoys living out of a suitcase for his job, 
    traveling around the country firing people, but finds that lifestyle 
    threatened by the presence of a potential love interest, and a new hire.'
),
(
    (SELECT movie_id FROM movies where movie_title = 'The Martian'),
    'In 2035, the crew of the Ares III mission to Mars is exploring 
    Acidalia Planitia on Martian solar day (sol) 18 of their 31-sol expedition. '
);

SELECT movies.movie_title, movies.released_date, scenarios.scenario_story as scenario
FROM movies
FULL OUTER JOIN scenarios
ON movies.movie_id = scenarios.pk_movie_id;


DROP TABLE IF EXISTS chocolate_glutton;
DROP TABLE IF EXISTS glutton;
DROP TABLE IF EXISTS chocolate;

CREATE TABLE IF NOT EXISTS chocolate (
	id SERIAL PRIMARY KEY,
	label VARCHAR(100),
	manufacturer VARCHAR(100),
	country CHAR(60)
);

CREATE TABLE IF NOT EXISTS glutton (
	id SERIAL PRIMARY KEY,
	name VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS chocolate_glutton (
    id SERIAL PRIMARY KEY,
    chocolate_id INT REFERENCES chocolate(id),
    glutton_id INT REFERENCES glutton(id)
);

INSERT INTO chocolate (label, manufacturer, country) VALUES
	('Toblerone', 'Mondelez International', 'Switzerland'),
	('Cadbury', 'Mondelez International', 'England'),
	('Lindt', 'Chocoladefabriken Lindt & Sprungli AG', 'Switzerland'),
	('Mars', 'Mars, Incorporated', 'USA'),
	('Ferrero Rocher', 'Ferrero SpA', 'Italy'),
	('Robert', 'Chocolaterie Robert', 'Madagascar')
;

INSERT INTO glutton (name) VALUES
	('Vincent'),
	('Safidy'),
	('Melanie'),
	('Naiza')
;

INSERT INTO chocolate_glutton (chocolate_id, glutton_id) VALUES
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (3, 1),
    (2, 1),
    (6, 2),
    (3, 3),
    (5, 3),
    (NULL, 4)
;


INSERT INTO chocolate_glutton (chocolate_id, glutton_id) VALUES
    (
		(SELECT id FROM chocolate WHERE label = 'Robert'),
		(SELECT id FROM glutton WHERE name = 'Safidy')
	)
;

UPDATE glutton
SET name = 'Stefan'
WHERE id = 1;

SELECT glutton.id, glutton.name, chocolate.label, chocolate.manufacturer, chocolate.country FROM glutton
FULL OUTER JOIN chocolate_glutton
ON glutton.id = chocolate_glutton.glutton_id
FULL OUTER JOIN chocolate
ON chocolate.id = chocolate_glutton.chocolate_id;
-- Total query time: 83msec

DELETE FROM glutton;

INSERT INTO chocolate_glutton (chocolate_id, glutton_id) VALUES
    (3, 1),
;

SELECT glutton.id, glutton.name, chocolate.label, chocolate.manufacturer, chocolate.country FROM glutton
FULL OUTER JOIN chocolate_glutton
ON glutton.id = chocolate_glutton.glutton_id
FULL OUTER JOIN chocolate
ON chocolate.id = chocolate_glutton.chocolate_id;


-- INSERT INTO chocolate_glutton (chocolate_id, glutton_id) VALUES
--     (3, 1),
--     (2, 1),
--     (6, 2),
--     (3, 3),
--     (5, 3),
--     (NULL, 4)
-- ;

-- SELECT chocolate.id, chocolate.label, COUNT(glutton.name) FROM glutton
-- INNER JOIN chocolate_glutton
-- ON glutton.id = chocolate_glutton.glutton_id
-- INNER JOIN chocolate
-- ON chocolate.id = chocolate_glutton.chocolate_id
-- GROUP BY chocolate.id, chocolate.label
-- HAVING chocolate.label = 'Lindt'
-- ORDER BY chocolate.label ASC;

-- Want to see all humans
SELECT name FROM employee
UNION
SELECT label FROM student;

-- Want to see all animals
SELECT name FROM cat
UNION
SELECT name from dog
UNION
SELECT name from tortoise
UNION
SELECT name from bird;
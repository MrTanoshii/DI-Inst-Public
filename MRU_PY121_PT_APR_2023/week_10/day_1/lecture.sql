CREATE TABLE food (
	id SERIAL PRIMARY KEY,
	label CHAR(50),
	description TEXT,
	spiciness_level INT,
	category VARCHAR(100)
);

INSERT INTO food (label, description, spiciness_level) VALUES
	('Riz frit','Du riz frit avec des legumes.', 10),
	('Kari Tang','blah blah blah', 2)
RETURNING label;

CREATE TABLE IF NOT EXISTS food (
	id SERIAL PRIMARY KEY,
	label CHAR(50),
	description TEXT,
	spiciness_level INT,
	category VARCHAR(100)
);

-- INSERT INTO food (label, description, spiciness_level) VALUES
-- 	('Kaaari Dholl','fdhfghfghfdg', NULL),
-- 	('Kuri Tipoi','dfhfghgfh', 0),
-- 	('McDonald''s Grand Chicken Spicy', 'Super delish borgor', 15),
-- 	('Smasher Burger Macon & Egg Borgor', '5/10', 5),
-- 	('Buffalo wings', 'Not actually buffalo', 2)
-- RETURNING label;

-- SELECT * FROM food
-- WHERE label = 'Kari Tang';

-- SELECT * FROM food
-- WHERE label LIKE 'K_ri%';

-- SELECT 
-- 	id, 
-- 	label AS "Label", 
-- 	description AS dlkgjlfdjgkldfjglkfd, 
-- 	spiciness_level AS "Spiciness Level", 
-- 	category AS "Category"
-- FROM food
-- WHERE spiciness_level > 0 AND dlkgjlfdjgkldfjglkfd NOT LIKE 'D%';

-- SeLEct * from food
-- WHERE spiciness_level IS NULL OR id <= 5;

-- SELECT * FROM food
-- WHERE label LIKE 'McDonald%'
-- LIMIT 10;

-- SELECT * FROM food
-- ORDER BY label DESC, id ASC
-- LIMIT 10
-- OFFSET 50;


-- Task: Select all foods that have spiciness level more than 0 and label containing Kari
--- Method normal
SELECT * FROM food
WHERE spiciness_level > 0 AND label LIKE 'Kari%';
--- Method subquery
SELECT * FROM
	(
		SELECT * FROM food
		WHERE spiciness_level > 0
	) AS hello
WHERE label LIKE 'Kari%';
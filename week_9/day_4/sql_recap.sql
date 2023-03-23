CREATE DATABASE sql_recap;

-- USE sql_recap;

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL
);

CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  date_modified TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  deleted BOOLEAN NOT NULL DEFAULT FALSE,
  title VARCHAR(255) NOT NULL,
  content TEXT NOT NULL,
  user_id INTEGER REFERENCES users(id)
);


CREATE TABLE posts_archived (
  id SERIAL PRIMARY KEY,
  date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  date_modified TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  date_deleted TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title VARCHAR(255) NOT NULL,
  content TEXT NOT NULL,
  user_id INTEGER REFERENCES users(id)
)

INSERT INTO users
(name, email, password)
VALUES 
    ('John', 'john@gmail.dot', 'thisisasecretpassword'),
    ('Jane', 'jane@gmail.dot', 'omgthisisapassword')
    ('John1', 'dsgfdgfdg@gmail.dot', 'fdgfdsgd'),
    ('John2', 'sfdgfdsg@gmail.dot', 'thisisasecretfdhgfhgfpassword'),
    ('John3', 'fdsgfdgdsf@gmail.dot', 'fdgsfdgfd'),
    ('John4', 'dsfgfdgds@gmail.dot', 'nbcvnvb'),
    ('John558', 'dsfgfdgds@gmail.dot', 'nbcvnvb'),
;

INSERT INTO posts
(title, content, user_id)
VALUES
    ("This is a title", "This is a content", 1),
    ("This is another title", "This is another content", 2)
;

SELECT * FROM users;
SELECT * FROM posts;

SELECT email, password FROM users WHERE name='John';
SELECT users.email, password AS secret_key FROM users WHERE name='John';

SELECT * FROM users WHERE name='John' OR name='Jane';

SELECT * FROM users WHERE name LIKE 'John%';

-- Page 1
-- Algorithm to set the offset is:
-- (page_number - 1) * limit
-- Limit: 100
-- PG1 offset: 0
-- PG2 offset: 100


-- Table posts

SELECT users.name, p1.title FROM users INNER JOIN posts AS p1 WHERE users.id = posts.user_id;
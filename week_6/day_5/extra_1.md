# Extra Examples

## Basic Tables

### Table: person

| column_name | type         | constraints |
| ----------- | ------------ | ----------- |
| id          | SERIAL       | PRIMARY KEY |
| first_name  | varchar(100) | NOT NULL    |
| last_name   | varchar(100) | NOT NULL    |

### Table: book

| column_name | type         | constraints |
| ----------- | ------------ | ----------- |
| id          | SERIAL       | PRIMARY KEY |
| year        | INT          | NOT NULL    |
| title       | varchar(300) | NOT NULL    |

## One to One Tables

### Table: person

| column_name   | type         | constraints         |
| ------------- | ------------ | ------------------- |
| id            | SERIAL       | PRIMARY KEY         |
| first_name    | varchar(100) | NOT NULL            |
| last_name     | varchar(100) | NOT NULL            |
| favorite_book | INT          | FOREIGN KEY book.id |

### Table: book

| column_name | type         | constraints |
| ----------- | ------------ | ----------- |
| id          | SERIAL       | PRIMARY KEY |
| year        | INT          | NOT NULL    |
| title       | varchar(300) | NOT NULL    |

## One to Many Tables

### Table: person

| column_name   | type         | constraints         |
| ------------- | ------------ | ------------------- |
| id            | SERIAL       | PRIMARY KEY         |
| first_name    | varchar(100) | NOT NULL            |
| last_name     | varchar(100) | NOT NULL            |
| favorite_book | INT          | FOREIGN KEY book.id |

### Table: book

| column_name | type         | constraints |
| ----------- | ------------ | ----------- |
| id          | SERIAL       | PRIMARY KEY |
| year        | INT          | NOT NULL    |
| title       | varchar(300) | NOT NULL    |

## Many to Many Tables

### Table: person

| column_name   | type         | constraints         |
| ------------- | ------------ | ------------------- |
| id            | SERIAL       | PRIMARY KEY         |
| first_name    | varchar(100) | NOT NULL            |
| last_name     | varchar(100) | NOT NULL            |
| favorite_book | INT          | FOREIGN KEY book.id |

### Table: book

| column_name | type         | constraints |
| ----------- | ------------ | ----------- |
| id          | SERIAL       | PRIMARY KEY |
| year        | INT          | NOT NULL    |
| title       | varchar(300) | NOT NULL    |

### Table: author

| column_name | type   | constraints           |
| ----------- | ------ | --------------------- |
| id          | SERIAL | PRIMARY KEY           |
| person_id   | INT    | FOREIGN KEY person.id |
| book_id     | INT    | FOREIGN KEY book.id   |

### Joined Tables: author, person

| column_name   | type         | constraints           |
| ------------- | ------------ | --------------------- |
| Table: author |              |                       |
| id            | SERIAL       | PRIMARY KEY           |
| person_id     | INT          | FOREIGN KEY person.id |
| book_id       | INT          | FOREIGN KEY book.id   |
| Table: person |              |                       |
| id            | SERIAL       | PRIMARY KEY           |
| first_name    | varchar(100) | NOT NULL              |
| last_name     | varchar(100) | NOT NULL              |
| favorite_book | INT          | FOREIGN KEY book.id   |

### Joined Tables: author, person, book

| column_name   | type         | constraints           |
| ------------- | ------------ | --------------------- |
| Table: author |              |                       |
| id            | SERIAL       | PRIMARY KEY           |
| person_id     | INT          | FOREIGN KEY person.id |
| book_id       | INT          | FOREIGN KEY book.id   |
| Table: person |              |                       |
| id            | SERIAL       | PRIMARY KEY           |
| first_name    | varchar(100) | NOT NULL              |
| last_name     | varchar(100) | NOT NULL              |
| favorite_book | INT          | FOREIGN KEY book.id   |
| Table: book   |              |                       |
| id            | SERIAL       | PRIMARY KEY           |
| year          | INT          | NOT NULL              |
| title         | varchar(300) | NOT NULL              |

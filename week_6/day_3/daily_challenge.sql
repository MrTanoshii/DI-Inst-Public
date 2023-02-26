CREATE DATABASE IF NOT EXISTS wk_6_day_3_daily_challenge;

USE wk_6_day_3_daily_challenge;

-- Part 1
-- 1.
CREATE TABLE Customer(
    id SERIAL PRIMARY KEY,
    first_name varchar(80),
    last_name varchar(80) NOT NULL
);

CREATE TABLE Customer_profile(
    id SERIAL PRIMARY KEY,
    isLoggedIN BOOLEAN DEFAULT false,
    -- David's solution
    -- CONSTRAINT customer_id FOREIGN KEY id REFERENCES Customer(id)




    -- customer_id INTEGER,
    -- POSTGRES Version
    -- FOREIGN KEY (customer_id) REFERENCES Customer(id)

    -- MYSQL Version
    CONSTRAINT customer_id FOREIGN KEY (id)
    REFERENCES Customer(id)
);

-- MYSQL Version
DESC Customer;
DESC Customer_profile;

-- POSTGRES Version
SELECT 
   table_name, 
   column_name, 
   data_type 
FROM 
   information_schema.columns
WHERE 
   table_name = 'Customer';

SELECT 
   table_name, 
   column_name, 
   data_type 
FROM 
   information_schema.columns
WHERE 
   table_name = 'Customer_profile';

-- id, first_name, last_name NOT_NULL

INSERT INTO Customer_profile(
    isLoggedIN,
    customer_id
)
SELECT 1, Customer.id FROM Customer
WHERE Customer.name = 'John';

INSERT INTO Customer_profile(
    isLoggedIN,
    customer_id
) VALUES (1, 1);
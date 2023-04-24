-- CREATE DATABASE IF NOT EXISTS daily_challenge_wk6_d4;

CREATE TABLE IF NOT EXISTS product_orders (
    id SERIAL PRIMARY KEY,
    order_number VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price INTEGER NOT NULL,
    product_order_id INTEGER,

    CONSTRAINT fk_product_order_id FOREIGN KEY(product_order_id) 
        REFERENCES product_orders(id)
);

-- #### WRONG ####
-- ORDER #1
-- item: 1, 2 ,3, 4, 5, 6, 7, 8, 9,

-- ITEM #1
-- ITEM #2
-- ITEM #3

-- #### GOOD ####
-- ORDER #1

-- ITEM #1
-- order: 1

-- ITEM #2
-- order: 1

-- ITEM #3
-- order: 1

INSERT INTO product_orders (order_number) 
VALUES 
('ORDER #1'),
('ORDER #2')
;

INSERT INTO items (name, price, product_order_id)
VALUES 
('ITEM #1', 100, 1),
('ITEM #2', 200, 1),
('ITEM #3', 300, 1),
('ITEM #4', 400, 2),
('ITEM #5', 500, 2),
('ITEM #6', 600, 2)
;

CREATE FUNCTION calc_total_price(product_id INTEGER) RETURNS INTEGER
BEGIN ATOMIC
    RETURN (SELECT SUM(price) FROM items WHERE product_order_id=product_id);
END;

DROP TABLE items;
DROP TABLE product_orders;
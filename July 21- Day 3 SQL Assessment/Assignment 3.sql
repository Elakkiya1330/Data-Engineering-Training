-- PART 1: Design the Database
CREATE DATABASE ASSIGNMENT3;
USE ASSIGNMENT3;
CREATE TABLE BOOKS (
    BOOK_ID INT PRIMARY KEY,
    TITLE VARCHAR(100),
    AUTHOR VARCHAR(100),
    GENRE VARCHAR(50),
    PRICE DECIMAL(10,2)
);
CREATE TABLE CUSTOMERS (
    CUSTOMER_ID INT PRIMARY KEY,
    NAME VARCHAR(100),
    EMAIL VARCHAR(100),
    CITY VARCHAR(50)
);
CREATE TABLE ORDERS (
    ORDER_ID INT PRIMARY KEY,
    CUSTOMER_ID INT,
    BOOK_ID INT,
    ORDER_DATE DATE,
    QUANTITY INT,
    FOREIGN KEY (CUSTOMER_ID) REFERENCES CUSTOMERS(CUSTOMER_ID),
    FOREIGN KEY (BOOK_ID) REFERENCES BOOKS(BOOK_ID)
);
-- PART 2: Insert Sample Data
--  5 books (with varied genres and prices)
INSERT INTO BOOKS VALUES
(1, 'THE GIRL IN ROOM 105', 'CHETAN BHAGAT', 'MYSTERY', 350.00),
(2, 'HALF GIRLFRIEND', 'CHETAN BHAGAT', 'ROMANCE', 700.00),
(3, 'THE NOTEBOOK', 'NICHOLAS SPARK', 'ROMANCE', 450.00),
(4, 'THE ALCHEMIST', 'PAULO COELHO', 'FICTION', 800.00),
(5, 'ONE ARRANGED MURDER', 'CHETAN BHAGAT', 'MYSTERY', 550.00);
-- 5 customers (from different cities)
INSERT INTO CUSTOMERS VALUES
(1, 'ELAKKIYA', 'elakkiya@gmail.com', 'HYDERABAD'),
(2, 'KASHIFA', 'kashifa@gmail.com', 'MUMBAI'),
(3, 'ROJA', 'roja@gmail.com', 'HYDERABAD'),
(4, 'SEREESHA', 'sereesha@gmail.com', 'CHENNAI'),
(5, 'LAVANYA', 'lavanya@gmail.com', 'BANGALORE');
--  7 orders (mix of books, customers, and dates)
INSERT INTO ORDERS VALUES
(1, 1, 2, '2023-02-10', 1),
(2, 2, 5, '2023-03-15', 2),
(3, 3, 1, '2022-12-25', 1),
(4, 4, 4, '2023-01-20', 1), 
(5, 5, 3, '2023-04-05', 3), 
(6, 1, 5, '2023-05-12', 1), 
(7, 1, 4, '2023-06-01', 2);  

--  PART 3: Write and Execute Queries
--  Basic Queries
--  1. List all books with price above 500.
SELECT * FROM BOOKS WHERE PRICE > 500;
--  2. Show all customers from the city of ‘Hyderabad’.
SELECT * FROM CUSTOMERS WHERE CITY = 'HYDERABAD';
--  3. Find all orders placed after ‘2023-01-01’.
SELECT * FROM ORDERS WHERE ORDER_DATE > '2023-01-01';

--  Joins & Aggregations
--  4. Show customer names along with book titles they purchased.
SELECT C.NAME, B.TITLE FROM CUSTOMERS C
JOIN ORDERS O ON C.CUSTOMER_ID = O.CUSTOMER_ID
JOIN BOOKS B ON O.BOOK_ID = B.BOOK_ID;
-- 5. List each genre and total number of books sold in that genre.
SELECT B.GENRE, SUM(O.QUANTITY) AS TOTAL_COUNT FROM BOOKS B
JOIN ORDERS O ON B.BOOK_ID = O.BOOK_ID GROUP BY GENRE;
--  6. Find the total sales amount (price × quantity) for each book.
SELECT B.TITLE, SUM(B.PRICE*O.QUANTITY)  AS TOTAL_COUNT FROM BOOKS B
JOIN ORDERS O ON B.BOOK_ID = O.BOOK_ID GROUP BY TITLE;
--  7. Show the customer who placed the highest number of orders.
SELECT C.NAME, COUNT(O.ORDER_ID) AS TOTAL_ORDERS FROM CUSTOMERS C
JOIN ORDERS O ON C.CUSTOMER_ID = O.CUSTOMER_ID
GROUP BY NAME LIMIT 1;
--  8. Display average price of books by genre.
SELECT GENRE, ROUND(AVG(PRICE)) FROM BOOKS
GROUP BY GENRE;
--  9. List all books that have not been ordered.
SELECT B.TITLE FROM BOOKS B
LEFT JOIN ORDERS O ON B.BOOK_ID = O.BOOK_ID
WHERE O.BOOK_ID IS NULL;
--  10. Show the name of the customer who has spent the most in total
SELECT C.NAME, SUM(B.PRICE*O.QUANTITY) AS TOTAL_SPENT FROM BOOKS B
JOIN ORDERS O ON B.BOOK_ID = O.BOOK_ID 
JOIN CUSTOMERS C ON O.CUSTOMER_ID = C.CUSTOMER_ID GROUP BY NAME ORDER BY TOTAL_SPENT DESC LIMIT 1;


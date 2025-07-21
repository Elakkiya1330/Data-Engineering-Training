--  SECTION 1: Database Design
CREATE DATABASE ASSIGNMENT4;
USE ASSIGNMENT4;
CREATE TABLE MOVIES (
    MOVIE_ID INT PRIMARY KEY,
    TITLE VARCHAR(100),
    GENRE VARCHAR(50),
    RELEASE_YEAR INT,
    RENTAL_RATE DECIMAL(10,2)
);
CREATE TABLE CUSTOMERS (
    CUSTOMER_ID INT PRIMARY KEY,
    NAME VARCHAR(100),
    EMAIL VARCHAR(100),
    CITY VARCHAR(50)
);
CREATE TABLE RENTALS (
    RENTAL_ID INT PRIMARY KEY,
    CUSTOMER_ID INT,
    MOVIE_ID INT,
    RENTAL_DATE DATE,
    RETURN_DATE DATE,
    FOREIGN KEY (CUSTOMER_ID) REFERENCES CUSTOMERS(CUSTOMER_ID),
    FOREIGN KEY (MOVIE_ID) REFERENCES MOVIES(MOVIE_ID)
);
-- SECTION 2: Data Insertion
--  Insert sample records into each table:
--  At least 5 movies from different genres and years
INSERT INTO MOVIES VALUES
(1, 'VIKRAM', 'ACTION', 2022, 120.00),
(2, 'RAYA AND THE LAST DRAGON', 'ANIMATION', 2021, 90.00),
(3, 'OK KANMANI', 'ROMANCE', 2015, 85.00),
(4, 'UP', 'ANIMATION', 2009, 90.00),
(5, 'ENCANTO', 'ANIMATION', 2021, 95.00),
(6, 'JAI BHIM', 'LEGAL DRAMA', 2020, 105.00);
--  At least 5 customers from different cities
INSERT INTO CUSTOMERS (CUSTOMER_ID, NAME, EMAIL, CITY) VALUES
(1, 'ELAKKIYA', 'elakkiya@gmail.com', 'HYDERABAD'),
(2, 'KASHIFA', 'kashifa@gmail.com', 'MUMBAI'),
(3, 'ROJA', 'roja@gmail.com', 'HYDERABAD'),
(4, 'SEREESHA', 'sereesha@gmail.com', 'CHENNAI'),
(5, 'LAVANYA', 'lavanya@gmail.com', 'BANGALORE'),
(6, 'AMIT SHARMA', 'amitsharma@gmail.com', 'DELHI');
--  At least 8 rental records — make sure at least one movie is rented more than once
INSERT INTO RENTALS VALUES
(1, 1, 2, '2023-06-01', '2023-06-03'), 
(2, 6, 3, '2023-06-10', '2023-06-15'), 
(3, 2, 1, '2023-06-05', '2023-06-07'), 
(4, 3, 4, '2023-07-01', NULL),          
(5, 3, 6, '2023-07-10', '2023-07-12'),
(6, 6, 2, '2023-06-20', '2023-06-23'),
(7, 4, 1, '2023-07-05', NULL),        
(8, 2, 5, '2023-07-07', '2023-07-09'); 

-- SECTION 3: Query Execution
--  Execute the following queries:
--  Basic Queries
--  1. Retrieve all movies rented by a customer named 'Amit Sharma'.
SELECT M.TITLE FROM MOVIES M
JOIN RENTALS R ON M.MOVIE_ID = R.MOVIE_ID 
WHERE R.CUSTOMER_ID = 6;
--  2. Show the details of customers from 'Bangalore'.
SELECT * FROM CUSTOMERS WHERE CITY = 'BANGALORE';
--  3. List all movies released after the year 2020.
SELECT * FROM MOVIES WHERE RELEASE_YEAR > 2020;

--  Aggregate Queries
--  4. Count how many movies each customer has rented.
SELECT C.NAME, COUNT(R.MOVIE_ID) AS NO_MOVIES FROM CUSTOMERS C
JOIN RENTALS R ON C.CUSTOMER_ID = R.CUSTOMER_ID
GROUP BY NAME; 
--  5. Find the most rented movie title.
SELECT M.TITLE, COUNT(M.MOVIE_ID) AS NO_RENTS FROM MOVIES M
JOIN RENTALS R ON M.MOVIE_ID = R.MOVIE_ID
GROUP BY TITLE ORDER BY NO_RENTS DESC LIMIT 1;
--  6. Calculate total revenue earned from all rentals.
SELECT SUM(M.RENTAL_RATE) FROM MOVIES M
JOIN RENTALS R ON M.MOVIE_ID = R.MOVIE_ID;

--  Advanced Queries
--  7. List all customers who have never rented a movie.
SELECT C.NAME FROM CUSTOMERS C 
LEFT JOIN RENTALS R ON C.CUSTOMER_ID = R.CUSTOMER_ID
WHERE R.CUSTOMER_ID IS NULL;
--  8. Show each genre and the total revenue from that genre.
SELECT M.GENRE, SUM(M.RENTAL_RATE) AS TOTAL_REVENUE FROM MOVIES M
JOIN RENTALS R ON M.MOVIE_ID = R.MOVIE_ID
GROUP BY GENRE;
--  9. Find the customer who spent the most money on rentals.
SELECT C.NAME, SUM(M.RENTAL_RATE) AS TOTAL_RENTAL FROM RENTALS R
JOIN CUSTOMERS C ON R.CUSTOMER_ID = C.CUSTOMER_ID
JOIN MOVIES M ON R.MOVIE_ID = M.MOVIE_ID
GROUP BY NAME ORDER BY TOTAL_RENTAL DESC LIMIT 1;
--  10. Display movie titles that were rented and not yet returned ( RETURN DATE IS NULL ).
SELECT M.TITLE FROM MOVIES M
JOIN RENTALS R ON M.MOVIE_ID = R.MOVIE_ID
WHERE R.RETURN_DATE IS NULL;


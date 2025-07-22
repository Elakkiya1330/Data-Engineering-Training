-- Create MySQL tables for users, expenses, categories
CREATE DATABASE EXPENSE_MANAGEMENT;
USE EXPENSE_MANAGEMENT;
CREATE TABLE USERS (
    USER_ID INT AUTO_INCREMENT PRIMARY KEY,
    NAME VARCHAR(100),
    EMAIL VARCHAR(100) UNIQUE
);
CREATE TABLE CATEGORIES (
    CATEGORY_ID INT AUTO_INCREMENT PRIMARY KEY,
    NAME VARCHAR(100) UNIQUE
);
CREATE TABLE EXPENSES (
    EXPENSE_ID INT AUTO_INCREMENT PRIMARY KEY,
    USER_ID INT,
    CATEGORY_ID INT,
    AMOUNT DECIMAL(10, 2),
    EXPENSE_DATE DATE,
    DESCRIPTION TEXT,
    FOREIGN KEY (USER_ID) REFERENCES USERS(USER_ID),
    FOREIGN KEY (CATEGORY_ID) REFERENCES CATEGORIES(CATEGORY_ID)
);
-- INSERTING SAMPLE DATA
INSERT INTO USERS (NAME, EMAIL) VALUES 
('Elakkiya', 'elakkiya@gmail.com'),
('Kashifa', 'kashifa@gmail.com'),
('Roja', 'roja@gmail.com'),
('Sereesha', 'sereesha@gmail.com'),
('Lavanya', 'lavanya@gmail.com'),
('Rithika', 'rithika@gmail.com'),
('Shobitha', 'shobitha@gmail.com'),
('Harish', 'harish@gmail.com');
INSERT INTO CATEGORIES (NAME) VALUES 
('Groceries'),
('Rent'),
('Utilities'),
('Transportation'),
('Dining'),
('Medical'),
('Education'),
('Entertainment');
-- Perform basic CRUD operations (add/edit/delete expenses)
-- 1. ADDING DATA IN EXPENSE TABLE
INSERT INTO EXPENSES (USER_ID, CATEGORY_ID, AMOUNT, EXPENSE_DATE, DESCRIPTION) VALUES
(1, 1, 2500.00, '2025-07-01', 'Weekly groceries at supermarket'),
(2, 2, 10000.00, '2025-07-01', 'Monthly house rent'),
(3, 5, 1200.00, '2025-07-02', 'Dinner with friends'),
(4, 3, 1800.00, '2025-07-03', 'Electricity and water bill'),
(5, 6, 2200.00, '2025-07-04', 'General health checkup'),
(6, 4, 800.00, '2025-07-04', 'Local transport charges'),
(7, 7, 5000.00, '2025-07-05', 'Tuition fees'),
(8, 8, 950.00, '2025-07-05', 'Movie and snacks'),
(1, 5, 700.00, '2025-07-06', 'Lunch at cafe'),
(2, 1, 3000.00, '2025-07-07', 'Vegetables and fruits'),
(3, 4, 600.00, '2025-07-08', 'Bus pass recharge'),
(4, 8, 1200.00, '2025-07-09', 'Concert tickets'),
(5, 2, 10500.00, '2025-07-10', 'Rent payment'),
(6, 6, 1500.00, '2025-07-11', 'Dental checkup'),
(7, 3, 2500.00, '2025-07-12', 'Water bill'),
(8, 1, 2800.00, '2025-07-13', 'Grocery shopping'),
(1, 3, 950.00, '2025-07-14', 'Internet and electricity bill'),
(2, 5, 1400.00, '2025-07-15', 'Dinner at restaurant'),
(3, 6, 2300.00, '2025-07-16', 'Medical prescription'),
(4, 1, 3200.00, '2025-07-17', 'Supermarket groceries'),
(5, 4, 900.00, '2025-07-18', 'Fuel for car'),
(6, 7, 4000.00, '2025-07-19', 'Online course fee'),
(7, 8, 1100.00, '2025-07-20', 'Cinema tickets'),
(8, 2, 10000.00, '2025-07-21', 'House rent');
-- 2. EDITING DATA IN EXPENSE TABLE
UPDATE EXPENSES SET AMOUNT = 1600 WHERE EXPENSE_ID = 1;
-- 3. DELETE DATA IN EXPENSE TAB;E
DELETE FROM EXPENSES WHERE EXPENSE_ID = 1;

-- Write a stored procedure to calculate monthly total expenses per category
DELIMITER //

CREATE PROCEDURE GETMONTHLYCATEGORYTOTALS(
    IN GMC_USER_ID INT,
    IN GMC_YEAR INT,
    IN GMC_MONTH INT
)
BEGIN
    SELECT 
        C.NAME AS CATEGORY_NAME, SUM(E.AMOUNT) AS TOTAL_AMOUNT FROM EXPENSES E
        JOIN CATEGORIES C ON E.CATEGORY_ID = C.CATEGORY_ID 
        WHERE E.USER_ID = GMC_USER_ID AND YEAR(E.EXPENSE_DATE) = GMC_YEAR AND MONTH(E.EXPENSE_DATE) = GMC_MONTH 
        GROUP BY C.NAME;
END //
DELIMITER ;
CALL GETMONTHLYCATEGORYTOTALS(1, 2025, 7);

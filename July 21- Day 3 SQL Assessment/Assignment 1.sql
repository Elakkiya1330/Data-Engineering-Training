 CREATE DATABASE ASSIGNMENT1;
 USE ASSIGNMENT1;
 CREATE TABLE employees ( 
emp_id INT PRIMARY KEY, 
emp_name VARCHAR(100), 
department VARCHAR(50), 
salary INT, 
age INT 
);
 CREATE TABLE departments ( 
dept_id INT PRIMARY KEY, 
dept_name VARCHAR(50), 
location VARCHAR(50) 
);
 INSERT INTO employees VALUES 
(101, 'Amit Sharma', 'Engineering', 60000, 30), 
(102, 'Neha Reddy', 'Marketing', 45000, 28), 
(103, 'Faizan Ali', 'Engineering', 58000, 32), 
(104, 'Divya Mehta', 'HR', 40000, 29), 
(105, 'Ravi Verma', 'Sales', 35000, 26);
 INSERT INTO departments VALUES 
(1, 'Engineering', 'Bangalore'), 
(2, 'Marketing', 'Mumbai'), 
(3, 'HR', 'Delhi'), 
(4, 'Sales', 'Chennai');

--  Section A: Basic SQL (Write Queries)
--  1. Display all employees.
SELECT * FROM EMPLOYEES;
--  2. Show only emp_name and salary of all employees.
SELECT EMP_NAME, SALARY FROM EMPLOYEES;
--  3. Find employees with a salary greater than 40,000.
SELECT * FROM EMPLOYEES WHERE SALARY > 40000;
--  4. List employees between age 28 and 32 (inclusive).
SELECT * FROM EMPLOYEES WHERE AGE BETWEEN 28 AND 32;
--  5. Show employees who are not in the HR department.
SELECT * FROM EMPLOYEES WHERE DEPARTMENT != "HR";
--  6. Sort employees by salary in descending order.
SELECT * FROM EMPLOYEES ORDER BY SALARY DESC;
--  7. Count the number of employees in the table.
SELECT COUNT(*) FROM EMPLOYEES;
-- 8. Find the employee with the highest salary.
SELECT * FROM EMPLOYEES WHERE SALARY = (SELECT MAX(SALARY) FROM EMPLOYEES);

--  Section B: Joins & Aggregations
--  1. Display employee names along with their department locations (using JOIN).
SELECT E.EMP_NAME, D.LOCATION FROM EMPLOYEES E 
JOIN DEPARTMENTS D ON E.DEPARTMENT = D.DEPT_NAME;
--  2. List departments and count of employees in each department.
SELECT D.DEPT_NAME, COUNT(E.DEPARTMENT) AS TOTAL_EMP FROM DEPARTMENTS D
JOIN EMPLOYEES E ON D.DEPT_NAME = E.DEPARTMENT
GROUP BY DEPT_NAME;
--  3. Show average salary per department.
SELECT DEPARTMENT, AVG(SALARY) AS AVG_SALARY FROM EMPLOYEES 
GROUP BY DEPARTMENT;
--  4. Find departments that have no employees (use LEFT JOIN).
SELECT D.DEPT_NAME  FROM DEPARTMENTS D
LEFT JOIN EMPLOYEES E ON D.DEPT_NAME = E.DEPARTMENT
WHERE E.EMP_ID IS NULL;
--  5. Find total salary paid by each department.
SELECT DEPARTMENT, SUM(SALARY) AS TOTAL_SALARY FROM EMPLOYEES 
GROUP BY DEPARTMENT;
--  6. Display departments with average salary > 45,000.
SELECT DEPARTMENT, AVG(SALARY) AS AVG_SALARY FROM EMPLOYEES 
GROUP BY DEPARTMENT HAVING AVG_SALARY > 45000;
--  7. Show employee name and department for those earning more than 50,000
SELECT EMP_NAME, DEPARTMENT FROM EMPLOYEES WHERE SALARY > 50000;
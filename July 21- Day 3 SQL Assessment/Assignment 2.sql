CREATE DATABASE ASSIGNMENT2;
USE ASSIGNMENT2;
 CREATE TABLE students ( 
student_id INT PRIMARY KEY, 
name VARCHAR(100), 
age INT, 
gender VARCHAR(10), 
department_id INT 
);
 CREATE TABLE departments ( 
department_id INT PRIMARY KEY, 
department_name VARCHAR(100), 
head_of_department VARCHAR(100) 
);
 CREATE TABLE courses ( 
course_id INT PRIMARY KEY, 
course_name VARCHAR(100), 
department_id INT, 
credit_hours INT 
);
 INSERT INTO students VALUES 
(1, 'Amit Sharma', 20, 'Male', 1), 
(2, 'Neha Reddy', 22, 'Female', 2), 
(3, 'Faizan Ali', 21, 'Male', 1), 
(4, 'Divya Mehta', 23, 'Female', 3), 
(5, 'Ravi Verma', 22, 'Male', 2);
INSERT INTO departments VALUES 
(1, 'Computer Science', 'Dr. Rao'), 
(2, 'Electronics', 'Dr. Iyer'), 
(3, 'Mechanical', 'Dr. Khan');
 INSERT INTO courses VALUES 
(101, 'Data Structures', 1, 4), 
(102, 'Circuits', 2, 3), 
(103, 'Thermodynamics', 3, 4), 
(104, 'Algorithms', 1, 3), 
(105, 'Microcontrollers', 2, 2);

--  Section A: Basic Queries
--  1. List all students with name, age, and gender.
SELECT NAME, AGE, GENDER FROM STUDENTS;
--  2. Show names of female students only.
SELECT * FROM STUDENTS WHERE GENDER = 'FEMALE';
--  3. Display all courses offered by the Electronics department.
SELECT * FROM COURSES WHERE DEPARTMENT_ID = 2;
--  4. Show the department name and head for department_id = 1.
SELECT DEPARTMENT_NAME, HEAD_OF_DEPARTMENT FROM DEPARTMENTS WHERE DEPARTMENT_ID = 1;
--  5. Display students older than 21 years.
SELECT * FROM STUDENTS WHERE AGE > 21;

--  Section B: Intermediate Joins & Aggregations
--  6. Show student names along with their department names.
SELECT S.NAME, D.DEPARTMENT_NAME FROM STUDENTS S 
JOIN DEPARTMENTS D ON S.DEPARTMENT_ID = D.DEPARTMENT_ID;
--  7. List all departments with number of students in each.
SELECT D.DEPARTMENT_NAME, COUNT(S.DEPARTMENT_ID) AS TOTAL_STUDENTS FROM DEPARTMENTS D
JOIN STUDENTS S ON D.DEPARTMENT_ID = S.DEPARTMENT_ID
GROUP BY DEPARTMENT_NAME;
--  8. Find the average age of students per department.
SELECT D.DEPARTMENT_NAME,ROUND(AVG(S.AGE)) AVG_AGE FROM DEPARTMENTS D
JOIN STUDENTS S ON D.DEPARTMENT_ID = S.DEPARTMENT_ID
GROUP BY DEPARTMENT_NAME;
--  9. Show all courses with their respective department names.
SELECT C.COURSE_NAME, D.DEPARTMENT_NAME FROM COURSES C 
JOIN DEPARTMENTS D ON C.DEPARTMENT_ID = D.DEPARTMENT_ID; 
--  10. List departments that have no students enrolled.
SELECT D.DEPARTMENT_NAME FROM DEPARTMENTS D
LEFT JOIN STUDENTS S ON D.DEPARTMENT_ID = S. DEPARTMENT_ID
WHERE S.DEPARTMENT_ID IS NULL;
--  11. Show the department that has the highest number of courses.
SELECT D.DEPARTMENT_NAME, COUNT(C.COURSE_ID) AS TOTAL_COURSES FROM DEPARTMENTS D
JOIN COURSES C ON D.DEPARTMENT_ID =  C.DEPARTMENT_ID
GROUP BY DEPARTMENT_NAME ORDER BY TOTAL_COURSES DESC LIMIT 1;

--  Section C: Subqueries & Advanced Filters
--  12. Find names of students whose age is above the average age of all students.
SELECT NAME , AGE FROM STUDENTS WHERE AGE > (SELECT AVG(AGE) FROM STUDENTS);
--  13. Show all departments that offer courses with more than 3 credit hours.
SELECT D.DEPARTMENT_NAME, C.COURSE_NAME,C.CREDIT_HOURS FROM DEPARTMENTS D
JOIN COURSES C ON D.DEPARTMENT_ID = C.DEPARTMENT_ID 
WHERE C.CREDIT_HOURS > 3;
--  14. Display names of students who are enrolled in the department with the fewest courses.
SELECT S.NAME , D.DEPARTMENT_NAME FROM STUDENTS S
JOIN DEPARTMENTS D ON S.DEPARTMENT_ID = D.DEPARTMENT_ID
WHERE S.DEPARTMENT_ID = (SELECT DEPARTMENT_ID FROM COURSES GROUP BY DEPARTMENT_ID ORDER BY COUNT(*) ASC LIMIT 1);
--  15. List the names of students in departments where the HOD's name contains 'Dr.'.
SELECT S.NAME, D.DEPARTMENT_NAME, D.HEAD_OF_DEPARTMENT FROM DEPARTMENTS D
JOIN STUDENTS S ON D.DEPARTMENT_ID = S.DEPARTMENT_ID
WHERE D.HEAD_OF_DEPARTMENT LIKE 'Dr.%';
--  16. Find the second oldest student (use subquery or LIMIT/OFFSET method).
SELECT NAME FROM STUDENTS ORDER BY AGE DESC LIMIT 1 OFFSET 1;
--  17. Show all courses that belong to departments with more than 2 students
SELECT COURSE_NAME FROM COURSES  WHERE DEPARTMENT_ID IN (SELECT DEPARTMENT_ID FROM STUDENTS GROUP BY DEPARTMENT_ID HAVING COUNT(*) >= 2);


CREATE DATABASE PET_CLINIC;
USE PET_CLINIC;
 CREATE TABLE Pets ( 
pet_id INT PRIMARY KEY, 
name VARCHAR(50), 
type VARCHAR(20), 
breed VARCHAR(50), 
age INT, 
owner_name VARCHAR(50) 
); 
INSERT INTO Pets VALUES  
(1, 'Buddy', 'Dog', 'Golden Retriever', 5, 'Ayesha'), 
(2, 'Mittens', 'Cat', 'Persian', 3, 'Rahul'), 
(3, 'Rocky', 'Dog', 'Bulldog', 6, 'Sneha'), 
(4, 'Whiskers', 'Cat', 'Siamese', 2, 'John'), 
(5, 'Coco', 'Parrot', 'Macaw', 4, 'Divya'), 
(6, 'Shadow', 'Dog', 'Labrador', 8, 'Karan');
 CREATE TABLE Visits ( 
visit_id INT PRIMARY KEY, 
pet_id INT, 
visit_date DATE, 
issue VARCHAR(100), 
fee DECIMAL(8,2), 
FOREIGN KEY (pet_id) REFERENCES Pets(pet_id) 
); 
INSERT INTO Visits VALUES 
(101, 1, '2024-01-15', 'Regular Checkup', 500.00), 
(102, 2, '2024-02-10', 'Fever', 750.00), 
(103, 3, '2024-03-01', 'Vaccination', 1200.00), 
(104, 4, '2024-03-10', 'Injury', 1800.00), 
(105, 5, '2024-04-05', 'Beak trimming', 300.00), 
(106, 6, '2024-05-20', 'Dental Cleaning', 950.00), 
(107, 1, '2024-06-10', 'Ear Infection', 600.00);

-- Basics
--  1. List all pets who are dogs.
SELECT * FROM PETS WHERE TYPE='DOG';
--  2. Show all visit records with a fee above 800.
SELECT * FROM VISITS WHERE FEE > 800;

--  Joins
--  3. List pet name, type, and their visit issues.
SELECT P.NAME, P.TYPE, V.ISSUE FROM PETS P
JOIN VISITS V ON P.PET_ID = V.PET_ID;
-- 4. Show the total number of visits per pet.
SELECT P.NAME, COUNT(*) AS TOTAL_VISIT FROM PETS P
JOIN VISITS V ON  P.PET_ID = V.PET_ID GROUP BY P.NAME;

--  Aggregation
--  5. Find the total revenue collected from all visits.
SELECT SUM(FEE) AS TOTAL_REVENUE FROM VISITS;
--  6. Show the average age of pets by type.
SELECT TYPE,ROUND(AVG(AGE)) AS AVG_AGE FROM PETS GROUP BY TYPE;

--  Date & Filtering
--  7. List all visits made in the month of March.
SELECT * FROM VISITS WHERE VISIT_DATE BETWEEN '2024-03-01' AND '2024-03-31';
--  8. Show pet names who visited more than once.
SELECT P.NAME, COUNT(*) AS TOTAL_VISIT FROM PETS P
JOIN VISITS V ON  P.PET_ID = V.PET_ID GROUP BY P.NAME ORDER BY TOTAL_VISIT DESC LIMIT 1;

--  Subqueries
--  9. Show the pet(s) who had the costliest visit.
SELECT P.NAME , V.FEE FROM PETS P
JOIN VISITS V ON P.PET_ID = V.PET_ID ORDER BY V.FEE DESC LIMIT 1;

SELECT P.NAME, V.FEE FROM PETS P
JOIN VISITS V ON P.PET_ID = V.PET_ID WHERE V.FEE = (SELECT MAX(FEE) FROM VISITS);
--  10. List pets who haven’t visited the clinic yet.
SELECT * FROM PETS WHERE PET_ID NOT IN (SELECT PET_ID FROM VISITS);

--  Update & Delete
--  11. Update the fee for visit_id 105 to 350.
UPDATE VISITS SET FEE = 350 WHERE VISIT_ID = 105;
--  12. Delete all visits made before Feb 2024
DELETE FROM VISITS WHERE VISIT_DATE < '2024-02-01';
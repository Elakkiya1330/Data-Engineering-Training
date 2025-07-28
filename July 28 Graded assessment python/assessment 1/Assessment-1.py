#  Q1. Write a function is_prime(n)  that returns  True if  n is a prime number else False

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
num = int(input("Enter a number: "))
if is_prime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")

# Q2. Write a program that:
#  Accepts a string
#  Reverses it
#  Checks if it's a palindrome

word = input("Enter a word: ")
if word == word[::-1]:
    print("It's a Palindrome")
else:
    print("Not a Palindrome")

#  Q3. Given a list of numbers, write code to:
#  Remove duplicates
#  Sort them
#  Print the second largest number

number = [1,2,3,4,4,5,7,8,9,8]
remove_dup = list(set(number))
print("1. without duplicates",remove_dup)
remove_dup.sort()
second_largest = remove_dup[-2]
print("2. second largest number is ",second_largest)

#  Q4. Create a base class  Person with:
#  Attributes: name, age
#  Method: display()
#  Create a derived class Employee:
#  Additional attributes: employee_id, department
#  Override display() to include all attributes

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

class Employee(Person):
    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.department = department
    def display(self):
        super().display()
        print("Employee ID:", self.employee_id)
        print("Department:", self.department)

emp = Employee("Elakkiya", 21, "01", "data engineering")
emp.display()

#  Q5. Demonstrate method overriding with another example:
#  Vehicle → Car
#  drive() method with custom message in child

class Vehicle:
    def drive(self):
        print("Driving a vehicle")
class Car(Vehicle):
    def drive(self):
        print("Driving a car")

v = Vehicle()
v.drive()
c = Car()
c.drive()

# Part 3: CSV & JSON Handling
#  Use the following sample students.csv for this section:
#  students.csv (you may create it in the same directory):
#  ID,Name,Age,Score
#  1,Aarav,18,85
#  2,Sanya,17,90
#  3,Meera,19,NaN
#  4,Karthik,,78
#  5,Rohan,18,88

# Q6. Read the students.csv
import pandas as pd
df = pd.read_csv('students.csv')
#  Fill missing Age with average age
df['Age'] = df['Age'].fillna(df['Age'].mean())
#  Fill missing Score with 0
df['Score'] = df['Score'].fillna(0)
#  Save the cleaned data as students_cleaned.csv
df.to_csv('students_cleaned.csv', index = False)

#  Q7. Convert the cleaned CSV into JSON and save as students.json
cleaned_df = pd.read_csv('students_cleaned.csv')
cleaned_df.to_json('students.json', indent = 4)

#  4: Data Cleaning & Transformation
#  Q8. Using Pandas and NumPy, perform the following on students_cleaned.csv:
import numpy as np
#  Add a column Status where:
#  If score ≥ 85 → 'Distinction'
# 60 ≤ score < 85 → 'Passed'
#  Else → 'Failed'
df['Status'] = np.where(df['Score'] >= 85, 'Distinction', np.where(df['Score'] >= 60, 'Passed', 'Failed'))
#  Add another column
# Tax_ID with values like 'TAX-1' , 'TAX-2' , etc., using the ID column
df['Tax_ID'] = 'TAX-' + df['ID'].astype(str)

df.to_csv('students_transformed.csv', index=False)

#  Part 5: JSON Manipulation with Python
#  Use the below sample JSON in a file
# products.json :
#  [
#  {"id": 1, "name": "Pen", "price": 20},
#  {"id": 2, "name": "Notebook", "price": 45},
#  {"id": 3, "name": "Eraser", "price": 10}
#  ]
#
#  Q9. Write a script to:
#  Read the JSON
import json
with open('products.json') as f:
    products = json.load(f)
#  Increase all prices by 10%
for item in products:
    item["price"] = round(item["price"] + (item["price"] * 0.10), 2)
#  Save back to products_updated.json
with open('products_updated.json', 'w') as w:
    json.dump(products, w, indent = 4)
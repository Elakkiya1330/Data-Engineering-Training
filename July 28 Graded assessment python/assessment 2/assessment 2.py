# Q1. Write a Python function factorial(n) using a loop.
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
n = int(input("Enter a number: "))
print(factorial(n))

#  Q2. Create a list of tuples like this:
# [("Aarav", 80), ("Sanya", 65), ("Meera", 92), ("Rohan", 55)]
list1 = [("Aarav", 80), ("Sanya", 65), ("Meera", 92), ("Rohan", 55)]
# Write code to:
# ● Print only names of students scoring above 75
for name, score in list1:
    if score > 75:
        print(name)
# ● Calculate and print average score
scores_total = [s[1] for s in list1]
avg = sum(scores_total)/len(scores_total)
print("The average is ",avg)

#  Q3. Create a class BankAccount with:
# ● Attributes: holder_name, balance
# ● Method: deposit(amount) and withdraw(amount)
# ● Raise an exception if withdrawal amount exceeds balance
class BankAccount:
    def __init__(self, holder_name, balance=0):
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance!")
        self.balance -= amount
        print(f"Withdrew ₹{amount}. Remaining balance: ₹{self.balance}")

#  Q4. Inherit a SavingsAccount class from BankAccount that adds:
# ● Attribute: interest_rate
# ● Method: apply_interest() that updates the balance
class SavingsAccount(BankAccount):
    def __init__(self, holder_name, balance=0, interest_rate=0.05):
        super().__init__(holder_name, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest ₹{interest:.2f} applied. New balance: ₹{self.balance:.2f}")

s = SavingsAccount("Elakkiya", 1000, 0.1)
s.deposit(500)
s.withdraw(200)
s.apply_interest()

# Part 3: CSV Task – Data Cleaning
# Use this CSV file: orders.csv
# OrderID,CustomerName,Item,Quantity,Price
# 101,Aarav,Notebook,2,50
# 102,Sanya,Pen,5,20
# 103,Rohan,,3,25
# 104,,Marker,4,
# 105,Meera,Eraser,,10

#  Q5. Write a Python script using Pandas to:
import pandas as pd
# ● Fill missing CustomerName with 'Unknown'
df = pd.read_csv('orders.csv')
df['CustomerName'] = df['CustomerName'].fillna('Unknown')
# thre is a null value in item so i have set it to unknown
df['Item'] = df['Item'].fillna('Unknown')
# ● Fill missing Quantity and Price with 0
df['Quantity'] = df['Quantity'].fillna(0)
df['Price'] = df['Price'].fillna(0)
# ● Add column TotalAmount = Quantity * Price
df['TotalAmount'] = df['Quantity']*df['Price']
# ● Save cleaned data to orders_cleaned.csv
df.to_csv('orders_cleaned.csv', index = False)


#  Part 4: JSON Task – Data Manipulation
# Use this JSON file: inventory.json
# [
#   {"item": "Pen", "stock": 120},
#   {"item": "Notebook", "stock": 75},
#   {"item": "Eraser", "stock": 0}
# ]


#  Q6. Write a script to:
# ● Read the JSON
import json
with open('inventory.json', 'r') as f:
    products = json.load(f)
# ● Add a new field status:
# ● 'In Stock' if stock > 0
# ● 'Out of Stock' otherwise
for Item in products:
    if Item['stock'] > 0:
        Item['status'] = 'In Stock'
    else:
        Item['status'] = 'Out of stock'

# ● Save as inventory_updated.json
with open('inventory_updated.json', 'w') as w:
    json.dump(products,w,indent = 4)


#  Part 5: Enrichment with NumPy
#
#  Q7. Generate an array of 20 random student scores between 35
# and 100 using NumPy.
import numpy as np
scores = np.random.randint(35,101,size=20)
# ● Count how many students scored above 75
above_75 = np.sum(scores > 75)
# ● Calculate mean and standard deviation
mean_score = np.mean(scores)
std_dev = np.std(scores)
# ● Create a Pandas DataFrame and save as scores.csv
df = pd.DataFrame({'Score': scores})
df.to_csv('scores.csv', index=False)

print("Scores: ",scores)
print("Number of students scoring above 75: ",above_75)
print("Mean score: ",mean_score)
print("Standard deviation: ",round(std_dev,2))

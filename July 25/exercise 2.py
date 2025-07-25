# 1. BMI Calculator (Input + Function + Conditions + math )
import math
def bmi_calc():
    bmi = weight / math.pow(height,2)
    if bmi < 18.5:
        print("Underweight")
    elif bmi < 25:
        print("Normal weight")
    else:
        print("Overweight")

weight = float(input("Enter your weight in Kg: "))
height = float(input("Enter your height in metre: "))
bmi_calc()

# 2. Strong Password Checker (Strings + Conditions + Loop)

while True:
    password = input("Enter password: ")
    has_upper = False
    has_number = False
    has_special = False

    for i in password:
        if i.isupper():
            has_upper =True
        if i.isdigit():
            has_number = True
        if i in "!@#$":
            has_special = True

    if has_upper and has_number and has_special:
        print("Strong password.")
        break

    else:
        print("Your password must have at least 1 capital letter, 1 number, 1 special character like !@#$")

# 3. Weekly Expense Calculator (List + Loop + Built-in Functions)
def weekly_expenses(expenses):
    print("Total spent: ₹", sum(expenses))
    print("Average per day: ₹", sum(expenses) / len(expenses))
    print("Highest spend in a day: ₹", max(expenses))

expenses = []

for i in range(7):
    amount = float(input(f"Enter expense for day {i+1}: "))
    expenses.append(amount)

weekly_expenses(expenses)

# 4. Guess the Number (Loops + random )

import random
number = random.randint(1,50)
print(number)
guessed = True
while guessed :
    for guess in range(5):
        user_guess = int(input(f"Enter your guess between(1-50), chance {guess+1}/5: "))
        if guess == 4 and user_guess != number:
            print(f"You Lost. The number is {number}")
            guessed = False
        elif user_guess == number:
            print("You win")
            guessed = False
            break
        elif user_guess < number:
            print("Too low")
        else:
            print("Too high")

# 5. Student Report Card (Functions + Input + If/Else + datetime )

import datetime
name = input("Enter your name: ")
science = float(input("Enter your mark(science): "))
social = float(input("Enter your mark(social): "))
maths = float(input("Enter your mark(maths): "))
def cal(a,b,c):
    sum = a + b + c
    print("The total is ", sum)
    average = sum/3
    print("The average is ",sum/3)
    if average > 85:
        print("Grade : A")
    elif average > 70:
        print("Grade : B")
    elif average > 50:
        print("Grade : C")
    print(datetime.date.today())
cal(science,social,maths)

# 6. Contact Saver (Loop + Dictionary + File Writing)

contacts = {}
while True:
    print("Contact Saver")
    print("\n1. Add Contact\n2. View Contacts\n3. Save & Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
    elif choice == "2":
        if contacts:
            print("\nSaved Contacts:")
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
        else:
            print("No contacts found.")
    elif choice == "3":
        with open("contacts.txt", "w") as file:
            for name, phone in contacts.items():
                file.write(f"{name}: {phone}\n")
        print("Contacts saved. Exiting...")
        break
    else:
        print("Invalid choice. Try again.")

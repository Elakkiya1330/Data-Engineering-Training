# print
print("Hello World")
# input
name = input("What is your name? ")
# concatenation
print("Hello "+name+" !")
# f string
print(f"Hello {name} !")

# accessing characters
str1 = "hello elakkiya"
print(str1[0])
print(str1[-1])
# slicing
print(str1[0:5])
print(str1[6:])
# string methods
print(str1.upper())
print(str1.lower())
print(str1.replace("elakkiya","harish"))

# list
fruits = ["apple","banana","orange","strawberry"]
# adding elements
fruits.append("chery")
print(fruits)
# removing elements
fruits.remove("strawberry")
print(fruits)
# slicing
print(fruits[1:])
# looping
for fruit in fruits:
    print(fruit)

# tuple() -immutable
colours = ("red","blue","green")
# accessing elements
print(colours[0])
# slicing
print(colours[1:3])

# QUICK PRACTICE TASKS
movie = "The Lion King"
print(movie[4:8])
food = ["dosa","idly","parotta","biryani"]
food.append("chapatti")
food.remove("idly")
print(food)
numbers = (1,2,3)
print(numbers[2])

# if else
age = int(input("what is your age? "))
if age >= 18:
    print("you can vote")
else:
    print("you cannot vote")

marks = int(input("enter your mark: "))
if marks >= 90:
    print("grade: A+")
elif marks >= 80:
    print("grade: A")
elif marks >= 70:
    print("grade: B+")
elif marks >= 60:
    print("grade: B")
elif marks >= 50:
    print("grade: C")
else:
    print("grade F")

# while
count = 1
while count <= 5:
    print("count is ",count)
    count += 1

# for loop
for i in range(5):
    print("number: ",i)
for i in range(1,6):
    print("number: ", i)

# break and continue
for i in range(1,10):
    if i == 5:
        continue
    elif i == 8:
        break
    print("number: ", i)

# functions
def greet():
    print("Hello from Hexaware")
greet()

def greet(name):
    print(f"Hello {name}, we are happy to announce that you cleared your role specific training.")
greet("Elakkiya")

def add(a,b):
    return a + b
result = add(10,2)
print (f"The sum is {result}")

def power(base,exponent=2):
    return base**exponent
print(power(5))
print(power(5,3))

# predefined functions
name = "Elakkiya"
print(len(name))
print(type(name))
number = 12
print(type(number))
int(number)
nums = [1,3,2]
print(sum(nums))
print(max(nums))
print(min(nums))
print(sorted(nums))
print(abs(-12))
print(round(4.57))
print(round(4.6789,2))

# modules - collection of functions
import math
print(math.sqrt(16))
print(math.pow(2,4))

import datetime as dt

today = dt.date.today()
time = dt.datetime.now()
print(f"Today's date {today}")
print("Time now ", time.strftime("%H:%M:%S"))

# user defined module
import ud_module as udm

addition = udm.add(12,10)
print(addition)
print(udm.sub(12,10))
print(udm.multiply(12,10))
print(udm.divide(12,2))

# package is a collection of modules
#  module is a collection of functions

from my_package.calc import add, multiply
from my_package.string_utils import shout,whisper

print(add(10,12))
print(multiply(10,5))
print(shout("ayyooo"))
print(whisper("achooo"))

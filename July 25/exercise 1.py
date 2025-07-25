# 1. FizzBuzz
for i in range(1,51):
    if i % 3 == 0 and i % 5 ==0 :
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 ==0:
        print("Buzz")
    else:
        print(i)

# 2. Login Simulation (Max 3 Attempts)
# Ask for a username and password. Allow maximum 3 attempts to enter the correct values ( admin / 1234 ). After 3 wrong tries, print "Account Locked" .

crt_user_name = "Elakkiya13"
crt_password = "elak1310"
attempt = 1
while attempt <= 3:
    username = input("enter username: ")
    password = input("enter password: ")
    if username == crt_user_name  and password == crt_password:
        print("Login success")
        break
    else:
        if attempt == 3:
            print("Account Locked")
            break
        else:
            print("invalid. Try again")
            attempt += 1

# 3. Palindrome Checker
# Ask the user to input a word. Print whether the word is a palindrome (reads same forward & backward).
word = input("Enter a word: ")
if word == word[::-1]:
    print("It's a Palindrome")
else:
    print("Not a Palindrome")

# 4. Prime Numbers in a Range
# Ask user for a number n and print all prime numbers from 1 to n .
n = int(input("Enter a number: "))
print(f"Prime numbers from 1 to {n}: ")
for num in range(2, n+1):
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count += 1
    if count == 2:
        print(num)

# 5. star pyramid
n = int(input("Enter a number: "))
for i in range(1,n+1):
    print("*" * i)

# 6. sum of digits
num = input("Enter number: ")
summ = 0
for i in num:
    summ += int(i)
print(summ)

# 7. Multiplication Table Generator
# Ask user for a number, print its multiplication table up to 10.
number = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number*i}")

# 8. Count Vowels in a String
# Ask user to enter a sentence. Print total number of vowels (a, e, i, o, u) present.
sentence = input("Enter a sentence: ")
vowels = ("a", "e", "i", "o", "u")
count = 0
for i in sentence:
    if i.lower() in vowels:
        count+=1
print(f"Total number of vowels in the sentence is {count}")
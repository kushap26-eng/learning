#1) Take a number from user and print its square
# num = int(input("Enter a number:"))
# square = num ** 2
# print("Square= ",square)


#2) Take two numbers and print Addition, Subtraction, Multiplication, Division
# num1 = float(input("Enter first number:"))
# num2 = float(input("Enter second number:"))

# print("Addition:",num1 + num2)
# print("Subtraction:",num1 - num2)
# print("Multiplication:",num1 * num2)
# print("Division:",num1 / num2)


#3) Take a number and print whether it is Even or Odd
# num = int(input("Enter a number:"))
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")


#4) Take a number and print its cube
# num = int(input("Enter a number:"))
# cube = num ** 3
# print("Cube=",cube)


#5) Take a number and print:
# num = int(input("Enter a number:"))
# print("Num + 10:",num + 10)
# print("Num * 5:",num *5)

# Condition

#1) Take a number and check if it is positive, negative, or zero.
# num = int(input("Enter a number:"))
# if num > 0:
#     print("Number is Positive")
# elif num < 0:
#     print("Number is negative")
# else:
#     print("Zero")


#2) Take age as input and check:
# age = int(input("Enter your Age:"))
# if age >= 18:
#     print("Eligible for Voting")
# else:
#     print("Not eligible for Voting")


#3) Take a number and check if it is divisible by 5 or not.
# num = int(input("enter a number:"))
# if num % 5 == 0:
#     print("Number is divisible by 5")
# else:
#     print("Number is not divisible by 5")


#4) Take two numbers and print which one is greater.
# a = int(input("Enter first number:"))
# b = int(input("Enter second number:"))
# if a > b:
#     print("A is greater")
# else:
#     print("Bis greater")


#5) Take marks and print:
#  ≥ 90 → Grade A
#  ≥ 75 → Grade B
#  ≥ 50 → Grade C
#  Else → Fail
# marks = int(input("Enter your marks:"))
# if marks >= 90:
#     print("Grade A")
# elif marks >= 75:
#     print("Grade B")
# elif marks >= 50:
#     print("Grade C")
# else:
#     print("Fail")


# nested if else

#Take 3 numbers and print the largest number.
# a = int(input("Enter number a:"))
# b = int(input("Enter number b:"))
# c = int(input("Enter number c:"))

# if a >= b:
#     if a >= c:
#         largest = a
#     else:
#         largest = c
# else:
#     if b >= c:
#         largest = b
#     else:
#         largest = c
# print("Largest Number:",largest)        


#2) Take a year and check whether it is a leap year
# year = int(input("Enter a year:"))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap Year")
#         else:
#             print("Not Leap Year")
#     else:
#         print("Leap Year")
# else:
#     print("Not Leap Year")


#3) Username and Password Check
# username = input("Enter your username:")
# password = input("Enter your password:")
# if username == "admin":
#     if password == "1234":
#         print("Login Success")
#     else:
#         print("Wrong Password")
# else:
#     print("Invalid User")



#4) 1. Take a number and check:
# - If even → check if divisible by 4
# - Print accordingly

# num = int(input("Enter a number:"))
# if num % 2 == 0:
#     print("Number is even")
#     if num % 4 == 0:
#         print("Also divisible by 4")
#     else:
#         print("Not divisible by 4")
# else:
#     print("Number is odd")


# 5)Take temperature:
# - 40 → "Very Hot"
# - 30–40 → "Hot"
# - 20–30 → "Normal"
# - < 20 → "Cold"

# temp = float(input("Enter temparature:"))
# if temp > 40:
#     print("Very hot")
# else:
#     if temp >=30:
#         print("Hot")
#     else:
#         if temp >= 20:
#             print("Normal")
#         else:
#             print("Cold")


# level 4 Loops (for/while)

#1) Print numbers from 1 to 10 using loop.
# for i in range(1,11):
#     print(i)

#2) Print numbers from 10 to 1 (reverse order).
# for i in range(10,0,-1):
#     print(i)

#3) Take a number and print its multiplication table.
# num = int(input("Enter a number:"))

# for i in range(1,11):
#     print(num, "x", i, "=",num * i)   

#4) Take a number and calculate sum from 1 to n.
# n = int(input("Enter a number:"))
# total = 0
# for i in range(1, n+1):
#     total += i
# print("Sum =",total)


#5) 5. Take a number and count how many **digits** it has.
# (Example: 1234 → 4 digits)

# num = int(input("Enter a number:"))
# count = 0
# while num > 0:
#     num = num // 10
#     count += 1
# print("Number of digits",count)

# Python loops Understanding
# Level 1 Basic Loops Understanding

#1) Print numbers from 1 to 20 using a loop.
# for i in range(1,21):
#     print(i)


#2) Print numbers from 20 to 1 (reverse order).
# for i in range(20,0,-1):
#     print(i)

#3) Print all even numbers between 1 to 50.
# for i in range(1,51):
#     if i % 2 == 0:
#         print(i)


#4) Print all odd numbers between 1 to 50.
# for i in range(1,51):
#     if i % 2 != 0:
#         print(i)


#5) Print numbers from 1 to n (take n from user).
# n = int(input("Enter a Number:"))
# for i in range(1,n+1):
#     print(i)


# Level 2 Loops+condition

#1) Print numbers from 1 to 100 that are divisible by 3.
# for i in range(1,101):
#     if i % 3 == 0:
#         print(i)


#2) Print numbers from 1 to 100 that are divisible by both 3 and 5.
# for i in range(1,101):
#     if i % 3 == 0 and i % 5 == 0:
#         print(i)

#3) Count how many numbers between 1 to 50 are even.
# count = 0
# for i in range(1,51):
#     if i % 2 == 0:
#         count += 1
# print("Total even numbers=",count)


#4) Take a number and count how many numbers from 1 to n are divisible by 7.
# n = int(input("Enter a number:"))
# count = 0
# for i in range(1,n+1):
#     if i % 7 == 0:
#         count += 1
# print("Total number divisible by 7:",count)


#5) Print all numbers between 1 to n that are not divisible by 2.
# n = int(input("Enter a Number:"))
# for i in range(1,n+1):
#     if i % 2 != 0:
#         print(i)


#Level 3 Loop + Math logic

#1)Take a number and calculate the sum from 1 to n.
# n = int(input("Enter a number:"))
# total = 0
# for i in range(1,n+1):
#     total += i
# print("Sum=",total)


#2) Take a number and calculate the factorial.
# n = int(input("Enter a number:"))
# factorial = 1
# for i in range(1,n+1):
#     factorial *= i
# print("Factorial=",factorial)


#3) Take a number and print its reverse.
# n = int(input("Enter a number:"))
# reverse = 0
# while n > 0:
#     digit = n % 10
#     reverse = reverse * 10 + digit
#     n = n // 10
# print("Reverse:",reverse)

#4) Take a number and check if it is a palindrome.
# num = int(input("Enter a Number:"))
# original = num
# reverse = 0
# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 +digit
#     num = num // 10
# if original == reverse:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


#5) 5. Take a number and find the **sum of its digits**
# num = int(input("Enter a number:"))
# total = 0
# while num > 0:
#     digit = num % 10
#     total += digit
#     num = num // 10
# print("Sum of digits:",total)


# Level 4 Nested Loops

# 1) Print Pattern
# *
# **
# ***
# ****
# *****
for i in range (1,6):
    for j in range(i):
        print("*",end = " ")
    print("")


#2)
# 1
# 12
# 123
# 1234
for i in range (1,5):
    for j in range(1,i + 1):
        print(j, end = " ")
    print("")


#3)
# *****
# ****
# ***
# **
# *
for i in range(5,0,-1):
    for j in range(i):
        print("*",end = " ")
    print("")

#4)Print multiplication tables from 1 to 5 (nested loop).
# for i in range(1,4):
#     print("Multiplication Table of ",i)
#     for j in range(1,11):
#         print(i, "x", j, "=",i * j)
#     print()

#5) Print all pairs:
# (1,1)
# (1,2)
# (1,3)
# ...
# (3,3)
for i in range(1,4):
    for j in range(1,4):
        print("(", i, ",", j, ")", sep="")



# Challenge questions
# Find prime numbers between 1 to 100
# print("Print numbers between 1 and 100 are:")
# for num in range(2,101):
#     is_prime = True
#     for i in range(2,num):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num)

# Print Fibonacci series up to n terms
# n = int(input("Enter the number of terms:"))
# a = 0
# b = 1
# print("Fibonacci Series:")
# for i in range(n):
#     print(a,end = " ")
#     c = a + b
#     a = b
#     b = c


# Find GCD of two numbers using loop
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
gcd = 1
for i in range(1,min(num1,num2)+1):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i
print("GCD = ",gcd)
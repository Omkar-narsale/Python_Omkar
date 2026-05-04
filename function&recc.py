# def func1():
#     print("Hello World") 
# func1()

# def avg(): #function definition
#     a=int(input("Enter first number:"))
#     b=int(input("Enter second number:"))
#     c=int(input("Enter third number:"))
#     avg=(a+b+c)/3
#     print("The average is:",avg)
# avg() #function call

# def GoodMorning(name):
#     print(f"Good Morning {name} have a nice day!")
# GoodMorning("Omkar")
# GoodMorning("Avani")  

# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*fact(n-1)
# n=int(input("Enter a number:"))
# print(f"THe factorial of {n} is:",fact(n))

# def largest(a,b,c):
#     if a>=b and a>=c:
#         return a
#     elif b>=a and b>=c:
#         return b
#     else:
#         return c
# a=int(input("Enter first number:"))
# b=int(input("Enter second number:"))
# c=int(input("Enter third number:"))
# print(f"The largest number among {a}, {b} and {c} is:",largest(a,b,c))
    
# def temp(f):
#     c=(f-32)*5/9
#     return c
# f=float(input("Enter temperature in Fahrenheit:"))
# print(f"The temperature in Celsius is: {temp(f)}°C")    

# def sum(n):
#     if n==0:
#         return 0
#     else:
#         return sum(n-1)+n
        
# n=int(input("Enter a number:"))
# print(f"The sum of first {n} natural numbers is:",sum(n))

# def pattern(n):
#  if(n==0):
#         return
#  print("*"*n)
#  pattern(n-1)
# n=int(input("Enter number of rows:"))
# pattern(n)

# def inch_to_cm(inch):
#     return inch*2.54
# inch=float(input("Enter Lenght in inches:"))
# print(f"The length in centimeters is: {inch_to_cm(inch)} cm")

# n=int(input("Enter a number to print till its multiplication table:"))
# for num in range(1,n+1):
#      print(f"\nTable of {num}")
#      for i in range(1,11):
#         print(f"{num}x{i}={num*i}")

# def add():
#       a=int(input("Enter first number:"))
#       b=int(input("Enter second number:"))
#       c=a+b
#       return c
# result=add()
# print(f"The sum is: {result}")

# def add(x,y):
#     a=6
#     b=7
#     c=a+b
#     print(c)
# add(3,2)

from asyncio import sleep
import asyncio


async def func():
    print("Hello World")
    await sleep(0.02)
    await func()
asyncio.run(func())
# import pyjokes
# print("Printing a random joke:")
# joke=pyjokes.get_joke()
# print(joke)

# a=10 
# b=30
# b+=3
# print(b)
# # b-=2
# print("The sum is:",a+b)    
# print("The division is:",b/a)
# print("The multiplication is:",a*b)
# d=a<b
# print(d)

# p=1000 
# r=5.5
# t=2
# si=(p*r*t)/100
# print("The simple intrest is:",si)

# import pyttsx3
# pyttsx3.speak("Hello Avani How are you?")

# a=int(input("Enter the first Number:"))
# b=int(input("Enter the second Number:"))
# print("The average of two numbers is:",(a+b)/2)
# print("The sum of two number is:",a+b)

# Calculate compound interest. Formula: A = P(1 + R/100)^T.
# p=float(input("Enter the principal amount:"))
# r=float(input("Enter the rate of interest:"))
# t=float(input("Enter the time in years:"))
# A=p*(1 + r/100)**t
# print("The compound interest is:",A )

# Write a program to take two integers, length and width, and calculate the area (length * width).
# l=float(input("Enter the length of rectangle:"))
# b=float(input("Enter the breadth of rectangle:"))
# A=l*b
# print("The area of rectangle is ",A)

# # Calculate the area of a circle given its radius. Formula: π * r².
# import math
# r=float(input("Enter the radius of circle:"))
# A=math.pi*r*r
# print("The area of circle is:",A)

# Calculate the perimeter of a square given one side. Formula: 4 * side
# s=float(input("Enter the side of rectangle:"))
# A=4*s
# print("The perimeter of square is:",A)

# Formula: F = (C * 9/5) + 32.
# c=float(input("Enter the temperature in Celsius:"))
# F=(c*9/5)+32
# print("The temperature in Fahrenheit is:",F)

# Convert a distance in kilometers to miles. 1 km = 0.621371 miles.
# d=float(input("Enter the distance in km:"))
# m=d*0.621371
# print("THe distance in miles:",m)

# Write a program to swap the values of two integer variables using a third temporary variable.
# a=10 
# b=20
# print("Before swapping:",a,b)
# temp=a
# a=b
# b=temp
# print("After swapping:",a,b)

# Swap two integers without using a third variable.
# a=120
# b=20
# print("Before swapping:",a,b)
# a=a+b
# b=a-b
# a=a-b
# print("After swapping:",a,b)

# Write a program that reads a character and prints its ASCII value
# char = input("Enter a character: ")
# print(ord(char))

# num=int(input("Enter a number: "))
# print(num%10)

import math
num=int(input("Enter a number: "))
print("The square root of the number is:",math.sqrt(num))
percentage=91.44
print(f"The percentage is: {math.ceil(percentage)}%")
print(f"The percentage is: {math.floor(percentage)}%")
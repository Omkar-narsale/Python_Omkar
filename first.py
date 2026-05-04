# print("Hello World")
# print('''Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.
# Twinkle, twinkle, little star,
# How I wonder what you are!
# When the blazing sun is gone,
# When he nothing shines upon,
# Then you show your little light,
# Twinkle, twinkle, all the night.
# Twinkle, twinkle, little star,
# How I wonder what you are! ''' )
# import pyttsx3
# pyttsx3.speak("Hello Avani How are you?")

# 1. Strings
# 2. Lists
# 3. Tuples
# 4. Dictionaries
# 5. Loops + Conditions
# 6. Functions
# 7. OOP Basics
# 8. Inheritance & Polymorphism
# 9. Operator Overloading (basic)
# 10. DSA

# n=int(input("Enter any number:"))
# sum=0
# while (n>0):
#  digit=n%10
#  sum=sum+digit
#  n//=10
# print("The sum of digits is:",sum)

# str1='Hello'
# str2='World'
# str1,str2=str2,str1
# print("str1:",str1)
# print("str2:",str2)

def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact
num=int(input("Enter any number:"))
fact=factorial(num)
print("The factorial of",num,"is",fact)

# Q1 Even Odd
# n=int(input("Enter any number:"))
# if n%2==0:
#     print(f"{n} is even")
# else:
#     print(f"{n} is odd")
# --------------------------------------------------------------
# Q2 Prime Number
# n=int(input("Enter Any Number:"))
# for i in range(2,n):
#     if(n%i==0):
#         print(f"{n} is not prime")
#         break
# else:
#         print(f"{n} is prime")
# -------------------------------------------------------------
#Q3 Leap Years
# n=int(input("Enter any year:"))
# if(n%4==0 and n%100!=0 or n%400==0):
#     print(f"{n} is an Leap Year")
# else:
#     print(f"{n} is  not an Leap Year")
#--------------------------------------------------------------
#Q4 Armstrong Number
# n = int(input("Enter Any Number: "))
# sum = 0
# temp = n
# digits_count = len(str(n))
# while temp > 0:
#     digit = temp % 10
#     sum += digit ** digits_count
#     temp //= 10
# if sum == n:
#     print(f"{n} is an Armstrong Number")
# else:
#     print(f"{n} is not an Armstrong Number")
#--------------------------------------------------------------
#Q5 String Palindrome
# s=input("Enter any word:")
# reversed_word=(s[::-1])
# if s==reversed_word:
#     print(f"{s} is an Palindrome String")
# else:
#     print(f"{s} is  not an Palindrome String")
#--------------------------------------------------------------
#Q6 Genrating Fibbo Series
# limit = int(input("Enter the limit: "))
# a, b = 0, 1
# fibonacci = []
# while a <= limit:
#     fibonacci.append(a)
#     a, b = b, a + b
# print(fibonacci)
#--------------------------------------------------------------
#Q7 Star Pattern
# n=int(input("Enter any number:"))
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     print("*"*(2*i-1),end="")
#     print("")
#--------------------------------------------------------------
#Q8 Factorial 
# n=int(input("Enter any number:"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(f"The factorial of {n} is:",fact)
#--------------------------------------------------------------
#Q9 sum of digits
# n=int(input("Enter Any Number:"))
# temp=n
# sum=0
# while temp>0:
#     digit=temp%10
#     sum+=digit
#     temp//=10
# print(f" The sum of digits of {n} is:",sum)
#--------------------------------------------------------------
#Q.10  GCD
# import math
# a=int(input("Enter First Number:"))
# b=int(input("Enter Second Number:"))
# print(f"GCD of {a} and {b} is ",math.gcd(a,b))
#--------------------------------------------------------------
#Q.11 LCM
# import math
# a=int(input("Enter First Number:"))
# b=int(input("Enter Second Number:"))
# print(f"LCM of {a} and {b} is",math.lcm(a,b))
#--------------------------------------------------------------
#Q.12 Counting Vowels and Consonants in a String
# message=(input("Enter the message:"))
# vowels="aeiouAEIOU"
# count=0
# c_count=0
# for i in message:
#  if i  in vowels:    
#     count=count+1
#  elif i !=" ":
#   c_count=c_count+1
# print("Vowles:",count)
# print("Consonants:",c_count)
#--------------------------------------------------------------
# Q.13 Reversing a String
# s=input("Enter any string:")
# print("The Reversed String is",s[::-1])
#--------------------------------------------------------------
# Q.14 Finding the Largest and Smallest Numbers in an Array
# li=[4, 7, 1, 8, 5]
# print("Largest:",max(li))
# print("Smallest:",min(li))
#--------------------------------------------------------------
# Q.15 Sorting an Array
# li=[3, 1, 4, 1, 5, 9]
# print(sorted(set(li)))
#--------------------------------------------------------------
# Q.16 Finding the Sum of Elements in an Array
# li=[1, 2, 3, 4, 5]
# print("The sum is:",sum(li))
#--------------------------------------------------------------
# Q.17 Checking for Armstrong Numbers in a Range
# start = int(input("Enter starting number: "))
# end = int(input("Enter ending number: "))
# result = []
# for num in range(start, end + 1):
#     temp = num
#     digits = len(str(num))
#     total = 0
#     while temp > 0:
#         d = temp % 10
#         total += d ** digits
#         temp //= 10
#     if total == num:
#         result.append(num)
# print(result)
#--------------------------------------------------------------
# Q.18 TABLE
# n=int(input("Enter any number:"))
# for i in range(1,11):
#     print(f"{n}x{i}={n*i}")
#--------------------------------------------------------------
#Q.19 Finding Prime Numbers in a Range
# start = int(input("Enter starting number: "))
# end = int(input("Enter ending number: "))
# result = []
# for num in range(start, end + 1):
#     if num > 1:   # prime numbers start from 2
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#         else:
#             result.append(num)
# print(result)
#--------------------------------------------------------------
#Q.20 Perfect Number
# num=int(input("Enter any number:"))
# total=0
# for i in range(1,num):
#     if(num%i==0):
#         total=total+i
# if total == num:
#     print(num, "is a Perfect Number")
# else:
#     print(num, "is NOT a Perfect Number")
#--------------------------------------------------------------
#Q.21 Calculating the Sum of Even Numbers in a Range
# start=int(input("Enter the start number:"))
# end=int(input("Enter the end number:"))
# sum=0
# for i in range(start,end+1):
#     if(i%2==0):
#         sum=sum+i
# print(sum)
#--------------------------------------------------------------
#Q.22 Calculating the Sum of Odd Numbers in a Range
# start=int(input("Enter the start number:"))
# end=int(input("Enter the end number:"))
# sum=0
# for i in range(start,end+1):
#     if(i%2!=0):
#         sum=sum+i
# print(sum)
#--------------------------------------------------------------
#Q.23 Finding the Fibonacci Number at a Specific Position
# n = int(input("Enter the position: "))
# a = 0
# b = 1
# if n == 0:
#     print("Fibonacci number at position 0 is:", a)
# elif n == 1:
#     print("Fibonacci number at position 1 is:", b)
# else:
#     for i in range(2, n + 1):
#         c = a + b
#         a = b
#         b = c
#     print(f"Fibonacci number at position {n} is:", b)
#--------------------------------------------------------------

#Q.24 Printing Prime Numbers Less Than a Given Number
# end = int(input("Enter ending number: "))
# result = []
# for num in range(1, end + 1):
#     if num > 1:   # prime numbers start from 2
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#         else:
#             result.append(num)
# print(result)
#--------------------------------------------------------------
# Q.25 Finding the Number of Digits in a Number
# num=int(input("Enter any number:"))
# print(len(str(num)))
#--------------------------------------------------------------
#Q.26 Checking if a Number is a Narcissistic Number
# n=int(input("Enter any number:"))
# temp=n
# sum=0
# digits_c=len(str(n))
# while n>0:
#     digits=n%10
#     sum=sum+digits**digits_c
#     n//=10
# if temp==sum:
#          print(f"{temp} is an  Narcissistic Number")
# else:
#           print(f"{temp} is not an  Narcissistic Number")
#--------------------------------------------------------------
# Q.27 Generating a Pattern of Numbers
# rows = int(input("Enter number of rows: "))
# num = 1
# for i in range(1, rows + 1):        
#     for j in range(i):             
#         print(num, end=" ")
#         num += 1
#     print()
#--------------------------------------------------------------
#Q.28 Finding the Sum of the Digits of the Factorial of a Number
# n=int(input("Enter any number:"))
# fact=1
# sum=0
# for i in range(1,n+1):
#     fact=fact*i
# temp=fact
# while temp>0:
#         digit=temp%10
#         sum=sum+digit
#         temp=temp//10
# print(sum)
#--------------------------------------------------------------
#Q.29 Largest Palindromes In an String
# s=input("Enter any string:")
# palindrome=[ 
#     s[i:j]
#     for i in range(len(s))
#     for j in range(i+1,len(s)+1)
#     if s[i:j]==s[i:j][::-1]
# ]
# largest=max(palindrome,key=len)
# print(largest)
#--------------------------------------------------------------
#Q.30 Missing Number in sequence
# l=[1,2,4,5,6]
# for i in range(l[0],l[-1]):
#     if i not in l:
#         print(i)
#--------------------------------------------------------------
#Q.31 Genrating Pascals Triangle
# from math import comb
# n=int(input("Enter number of rows:"))
# for i in range(n):# for rows
#     for j in range(i+1): # for columns
#         print(comb(i,j),end=" ")
#     print()
#--------------------------------------------------------------
#Q.32 Finding the Median of an Array
# l=[3, 1, 2, 4, 5]
# lenght=len((l))
# s=l.sort()
# median=(lenght+1)/2
# print(median)
#--------------------------------------------------------------
# 2 APPROACH
# import statistics
# l=[3, 1, 2, 4, 5]
# print(statistics.median(l))
#--------------------------------------------------------------

# Q.33 Calculating the Power of a Number
# import math
# print(math.pow(2,3))
#--------------------------------------------------------------
# Q.34 Anagram 
# from collections import Counter
# s1=input("Enter any string:")
# s2=input("Enter any string:")
# if Counter(s1)==Counter(s2):
#     print("Anagram")
# else:
#       print("Not An Anagram")  
#--------------------------------------------------------------
#Q.37 Finding the Sum of Prime Numbers in a Range
# start = int(input("Enter starting number: "))
# end = int(input("Enter ending number: "))
# result = []
# for num in range(start, end + 1):
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#         else:   
#             result.append(num)
# print(sum(result))
#--------------------------------------------------------------
#Q.36 Finding the N-th Triangular Number
# n=int(input("Enter any number:"))
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
# print(sum)
#--------------------------------------------------------------
# Q.37 Checking for Perfect Squares
# import math
# n=int(input("Enter any number:"))
# root=math.isqrt(n)
# if root*root==n:
#     print("True")
# else:
#     print("False")
#--------------------------------------------------------------
# Q.38 Finding the Sum of Squares of Digits
# n=int(input("Enter any number:"))
# sum=0
# temp=n
# digits_count=len(str(n))
# while temp>0:
#   digits=temp%10
#   sum=sum+digits*digits
#   temp//=10
# print(sum)
#--------------------------------------------------------------
# Q.39 Generating a Square Matrix of a Given Size
# n = int(input("Enter size of matrix: "))
# matrix = []
# num = 1
# for i in range(n):
#     row = []
#     for j in range(n):
#         row.append(num)
#         num += 1
#     matrix.append(row)
# for row in matrix:
#     print(row)
#--------------------------------------------------------------
#Q.40 Calculating the Sum of Digits of a Number Until Single Digit
# num=int(input("Enter any number:"))
# if num==0:
#     print(0)
# else:
#     print("Single Digit sum is:",1+(num-1)%9)
#--------------------------------------------------------------
#.Q41 Finding the Count of Specific Digits in a Number
# from collections import Counter
# n=(input("Enter any number:"))
# digit=int(input("Enter The Digit:"))
# freq=Counter(str(n))
# print(freq[str(digit)])
#--------------------------------------------------------------
# Q.43 Finding All Divisors of a Number
# n=int(input("Enter ny number:"))
# for i in range (1,n+1):
#  if(n%i==0):
#   print(i,end=" ")
#--------------------------------------------------------------
# Q.44 Finding the Average of Numbers in an Array
# l=[1, 2, 3, 4, 5]
# average=sum(l)/len(l)
# print("Average:",average)
#--------------------------------------------------------------
#Q.45 Finding the Mode of Numbers in an Array
# import statistics
# l=[1, 2, 2, 3, 4, 4, 4]
# print(statistics.mode(l))
#--------------------------------------------------------------
#Q.46 Determining the Length of a String Without Using Built-In Functions
# msg=input("Enter any string:")
# count=0
# for i in msg:
#     count+=1
# print(count)
#--------------------------------------------------------------
#Q.47 Generating a Number Pyramid
# n=int(input("enter the number of rows:"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()
#--------------------------------------------------------------
# Q.48 Finding the Sum of Prime Factors of a Number
# num = int(input("Enter any number: "))
# result = []
# for i in range(2, num + 1):
#     if num % i == 0:   # i is a factor
#         # check if i is prime
#         is_prime = True
#         for j in range(2, i):
#             if i % j == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             result.append(i)
# print("Sum of prime factors:", sum(result))
#--------------------------------------------------------------
# Q.49 Second largest number in the list.
# import heapq
# li=[10, 20, 4, 45, 99]
# print(heapq.nlargest(2, li)[1])
#--------------------------------------------------------------

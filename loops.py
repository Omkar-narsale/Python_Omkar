# i=1
# while(i<=6):
#     print("Omkar",i)
#     i=i+1

# l=["Omkar","Shubham","Gettesh","Avani"]
# i=0
# while(i<len(l)):
#     print(l[i])
#     i=i+1

# n=int(input("Enter a number:"))
# for i in range(0,11):
#     print(f"{n}x{i}={n*i}")

# n=int(input("Enter a number:"))
# i=0
# while(i<11):
#     print(f"{n}x{i}={n*i}")
#     i=i+1

# n=int(input("Enter a number:"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print("The factorial of",n,"is",fact)

# from collections import Counter
# message=(input("Enter the message:"))
# freq=Counter(message)
# for i in freq:
#     print(f"The frequency of {i} is ",freq[i])

# message=(input("Enter the message:"))
# vowels="aeiouAEIOU"
# count=0
# consonants=0
# result=""
# for i in message:
#  if i  in vowels:    
#     result+=i
# print(result)

# l=[1,2,3,4,5,6,7,8,9]
# for item in l:
#     print(item)
# else:
#     print("Done!")

# for i in range(100):
#     if(i==34):
#         # break # it will break the loop if i is 34
#         continue # it will skip the iteration if i is 34
#     print(i)

# num=int(input("Enter a number:"))
# if(num%2==0):
#     print("The number is even")
# elif(num<0):
#     print("The number is negative")
# else:
#     print("The number is odd")

# l=["Sachin","Sehwag","Samson","Dravid"]
# for i in l:
#     if(i.startswith("S")):
#         print(i)

# num=int(input("Enter a number:"))
# for i in range(2,num):
#     if(num%i==0):
#         print("The number is not prime")
#         break
# else:
#     print("The number is prime")

# num=int(input("Enter a number:"))
# sum=0
# i=0
# while(i<=num):
#     sum+=i
#     i+=1
# print("The sum is:",sum)

# n=int(input("Enter a number:"))
# for i in range(1,n+1):
#     print(" "*(n-i),end="") # i is no of rows and for spacess
#     print("*"*(2*i-1),end="") # for stars
#     print("")

# n=int(input("Enter a number:"))
# for i in range(1,n+1): 
#     print("*"*(i),end="") # for stars
#     print("")

# n=int(input("Enter a number:"))
# for i in range(1,n+1):
#     if(i==1 or i==n):
#      print("*"*n,end="") # for first and last row
#     else:
#          print("*",end="") # for first star
#          print(" "*(n-2),end="") # for spaces
#          print("*",end="") # for last star
#     print("")

# n=int(input("Enter a number:"))
# for i in range(1,11):
#      print(f"{n}x{11-i}={n*(11-i)}")

# n=int(input("Enter a number:"))
# for i in range(0,11):
#     print(f"{n}x{i}={n*i}")


# num=int(input("Enter a number:"))
# s=int(input("Enter the starting point:"))
# e=int(input("Enter the ending point:"))
# for i in range(s,e+1):
#     print(f'{num}x{i}={num*i}')

# while(True):
#     num=int(input("Enter a number:"))
#     if(num<0):
#         print("Negative number is not allowed")
#         break
#     fact=1
#     for i in range(1,num+1):
#         fact=fact*i
#     print("The factorial of",num,"is",fact)

# i=1
# while(i<=5):
#     print("Omkar",end=" ")
#     j=1
#     while(j<=4):
#         print("Shubham",end=" ")
#         j=j+1
#     i=i+1
#     print()

# i=0
# while(i<=100):
#     if(i%2==0):
#         print(i,end=" ")
#     i=i+1

# data=[1,2,3,4,5,6,7,8,9]
# for i in data:
#     print(i,end=" ")
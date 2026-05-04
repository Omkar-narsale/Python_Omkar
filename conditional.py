# age=int(input("Enter your age:"))
# if(age>=18):
#     print("You can Vote")
# elif(age<0):
#     print("Enter valid age")
# elif(age==0):
#     print("Age doenot exist")
# else:
#     print("You cannot Vote")

# a1=int(input("Enter first number:"))
# a2=int(input("Enter second number:"))
# a3=int(input("Enter third number:"))
# a4=int(input("Enter fourth number:"))
# if(a1>=a2 and a1>=a3 and a1>=a4):
#     print("The greatest number is:",a1)
# elif(a2>=a1 and a2>=a3 and a2>=a4):
#     print("The greatest number is:",a2)
# elif(a3>=a1 and a3>=a2 and a3>=a4):
#     print("The greatest number is:",a3)
# else:
#     print("The greatest number is:",a4)

# marks1=int(input("Enter marks of subject 1:"))
# marks2=int(input("Enter marks of subject 2:"))
# marks3=int(input("Enter marks of subject 3:"))
# total_percent=(100*(marks1+marks2+marks3))/300

# if(total_percent>=40 and marks1>33 and marks2>33 and marks3>33):
#     print("You have passed the exam with :",total_percent)
# else:
#     print("You have failed the exam")

# message = (input("Enter the message: "))
# vowels = "aeiouAEIOU"
# count = 0

# for i in message:
#     if i in vowels:
#         count = count + 1
# print("The number of vowels in the message is:", count)

# username=input("Enter your username:")
# if(len(username)<10):
#     print("Username is valid")
# else:
#     print("Username is too long")

# li=["Omkar","Ankush","Rohan","Sonu","Monu"]

# name=input("Enter your name:")

# if(name in li):
#  print("Your name is present in the list")
# else:
#     print("Your name is not present in the list")

from collections import Counter
message=(input("Enter the message:"))
freq=Counter(message)
for i in freq:
    print(f"The frequency of {i} is ",freq[i])

# from collections import Counter
# message = input("Enter a sentence:")
# freq = Counter(message.split())
# for i in freq:
#   print(i, ":", freq[i])

# Only used when no repetation of letters
# word = input("Enter a word:")
# for ch in word:
#   print(f"The frequency of {ch} is :",word.count(ch))
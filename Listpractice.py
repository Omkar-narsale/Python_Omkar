# Q1.Write a script to perform the following three operations on given list
# Access the third element of a list
# List Length: Print the total number of items
# Check if the list is empty

# num=[10,20,30,40]
# print(num[3])
# print(len(num))
# is_empty=len(num)==0
# print(f"Is empty?{is_empty}")

# Q2.Perform List Manipulation
# l=[100, 50, 400, 500]
# l[1]=200
# print("Updated:",l)
# l.append(600)
# print("Append:",l)
# l.insert(2,300)
# print("Insert:",l)
# l.remove(600)
# print("Remove:",l)
# l.pop(0)
# print("Pop:",l)

#3.Sum and Average of All Numbers in a List
# l=[10, 20, 30, 40, 50]
# print(sum(l))
# print(sum(l)/len(l))

#4.Find Maximum and Minimum from List
# l=[45, 12, 89, 2, 67]
# max_value=max(l)
# min_value=min(l)
# print("Max:",max_value)
# print("Min:",min_value)

# 5. Calculate the Product of All Elements
# l=[2, 3, 5, 7]
# product=1
# for i in l:
#     product*=i
# print("Product",product)

# 6. Count Even and Odd Numbers

# l=[10, 21, 4, 45, 66, 93, 11]
# even=0
# odd=0
# for i in l:
#     if i%2==0:
#      even+=1
#     else:
#        odd+=1
# print("Even:",even)
# print("Odd:",odd)

# 7. Reverse a List
# l=[100, 200, 300, 400, 500]
# print("Actual:",l)
# print("Reversed:",l[::-1])

# 8. Sort a List of Numbers
# l=[56, 12, 89, 3, 22]
# print("Unsorted:",l)
# print("Sorted:",sorted(l))

#9.Create a Copy of a List
# l=["Apple", "Banana", "Cherry"]
# print("Original:",l)
# copy=l.copy()
# print("Copied:",copy)

# 10.Combine Two Lists
# list_a = ["Physics", "Chemistry"]
# list_b = ["Maths", "Biology"]
# # Combine using the + operator
# combined = list_a + list_b
# print(f"Combined List: {combined}")

# 14. Check if List Contains a Specific Item
# Inventory=["Laptop", "Mouse", "Monitor", "Keyboard"]
# Target="Tablet"
# if Target in Inventory:
#  print("Succesful")
# else:
#  print("UnSuccesful")

# 15. Find the Longest String in a List
# Words=["PHP", "Exercises", "Backend", "Python"]
# longest=max(Words,key=len)
# print(f"Longest word: {longest}")

# 16. Turn Every Item of a List into its Square (List Comprehension)
# l=[1, 2, 3, 4, 5]
# squared=[i**2 for i in l]
# print("Squared List:",squared)

# 17. Count Occurrences of an Item
# l=[10, 20, 30, 10, 40, 10, 50]
# count=0
# target=10
# for i in l:
#  if target==i:
#     count+=1
# print(f"The number {target} appears {count} times")

#18.Remove All Occurrences of a Specific Item
# l = [5, 20, 15, 20, 25, 50, 20]
# target = 20
# while target in l:
#     l.remove(target)
# print(l)

# #19. Remove Empty Strings from a List of Strings
# Names=["Mike", "", "Emma", "Kelly", "", "Brad"]
# cleaned_names=list(filter(None,Names))
# print(f'Cleaned Names:{cleaned_names}')
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

# #20. Remove Duplicates from List
# l=[10, 20, 10, 30, 40, 40, 20, 50]
# unique_l=((list(set(l))))
# print(sorted(unique_l))

# 21.List Comprehension for Filtering Numbers
# l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even=[]
# for i in l:
#     if i%2==0:
#      even.append(i)
# print(even)

#22. Concatenate Two Lists Index-wise
# List_1=["Py", "is", "awes"]
# List_2=["thon", " ", "ome"]
# res=[a+b for a,b in zip(List_1,List_2)]
# print("Merged:",res)

#23.Iterate Both Lists Simultaneously
# l1=[10, 20, 30]
# l2=[100, 200, 300]
# for a,b in zip(l1,l2):
#  print(a,b)

#24. Add New Item After a Specified Item
# l=[10, 20, 30, 40, 50]
# new_val=35
# target=30
# index=l.index(target)
# l.insert(index+1,35)
# print("Updated:",l)
# l.insert(3,35)
# print(l)

# 25. Replace List’s Item with New Value if Found
# l=[5, 10, 15, 20, 25]
# target=20
# new_value=200
# if target in l:
#  index=l.index(target)
#  l[index]=new_value
# print("Updated:",l)

# 26. Find the Second Largest Number in a List
# l=[12, 35, 1, 10, 34, 1, 35]
# l1=list(set(l))
# l2=sorted(l1)
# print(l2)
# print("Second largest:", l2[-2])

# 27. Find the Most Frequent Element
# l=[1, 3, 3, 2, 1, 1, 4, 3, 3]
# most_freq=max(l,key=l.count)
# print(most_freq)

# 28. Extract Every Nth Element from a List
# l=['a', 'b', 'c', 'd', 'e', 'f', 'g']
# n=3
# res=l[::n]
# print(res)

# 29. Check if List is Palindrome
# l=[1, 2, 3, 2, 1]
# l_r=l[::-1]
# if l==l_r:
#     print("Palindrome")
# else:
#     print("Non-Palindrome")

# 30. Find All Common Elements Between Three Lists
# List_A= [1, 5, 10, 20]
# List_B= [6, 7, 20, 80, 100]
# List_C= [3, 4, 15, 20, 30, 70, 80]
# Common=(set(List_A)&set(List_B)&set(List_C))
# print(list(Common))

# 31. Filter Strings by Length in a List
# l=["apple", "pie", "banana", "kiwi", "pear"]
# key=5
# result = [x for x in l if len(x) >= key]
# print(result)

# 32. Check if List is Sorted
# L=[10, 20, 30, 25, 40]
# print(L==sorted(L))

# 34. Find the Difference Between Two Lists
# l1=[1, 2, 3, 4, 5]
# l2=[2, 4, 6]
# diffrence=list(set(l1)-set(l2))
# print(diffrence)

#  35. Remove Negative Numbers In-place
# l=[10, -5, 20, -1, 0, -8]
# for i in l[:]:   # iterate over copy
#     if i < 0:
#         l.remove(i)
# print(l)

# 41. Rotate a List (Left or Right by k positions)
# l=[1, 2, 3, 4, 5]
# k=2
# res=l[k:]+l[:k] #Left
# res1=l[-k:]+l[:-k] #Right
# print(res)
# print(res1)
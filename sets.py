# e=set() # empty set
# print(type(e))
# d={} # empty dictionary
# print(type(d))

s1={1,2,3,4,5,5,4} # set with duplicate values
s2={4,5,6,7,8} # another set
#print(s1.union(s2)) # it will print union of s1 and s2
#print(s1.intersection(s2)) # it will print intersection of s1 and s2
print(s1-s2)
print(s2-s1)
print(s1.issubset({4,5})) # it will check whether {4,5} is subset of s1 or not
print(s1.issuperset({1,2,3})) # it will check whether s1 is superset of {1,2,3} or not
# print(s)

# s.add(6) #it will add 6 to the set 
# print(s)

# # print(len(s)) # it will print the length of set

# s.remove(2) # it will remove 2 from the set
# print(s) 

print("My Name is Omkar")
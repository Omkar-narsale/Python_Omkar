#marks={
    #"Omkar":9.43,
    #"Shubham":8.76,
    #"Gettesh":9.57
#}
# print(marks["Omkar"])
# print(marks.items()) #it will print all the items in the dictionary dict_items([('Omkar', 9.43), ('Shubham', 8.76), ('Gettesh', 9.57)])
#print(marks.keys()) # it will print all the keys in the dictionary dict_keys(['Omkar', 'Shubham', 'Gettesh'])
#print(marks.values()) # it will print all the values in the dictionary dict_values([9.43, 8.76, 9.57])
#marks.update({"Omkar":9.18}) # it will update the value of key Omkar to 9.18
#print(marks.get("Omkar")) # it will print the value of key Omkar additionally if key is not present it will return None
#print(marks["Omkar"]) # it will print the value of key Omkar additionally if key is not present it will give error

# dict1={"A":1,"B":2}
# dict2={"C":3,"D":4}
# dict3=dict1|dict2
# print(dict3)
# print(dict3.get("A"))

# for counting frequency of elements in a list
from collections import Counter
items = "Omkar"
freq = Counter(items)
for i in items:
 print(f"The Frequency of {i} is ",freq[i])

# words={
#     "madad":"Help",
#     "pustak":"Book",
#     "kalam":"Pen",
# }
# word=input("Enter the word in Hindi to get its meaning in English:")
# print(words[word])

# d={}
# name=input("Enter your name:")
# lang=input("Enter the language:")
# d.update({name:lang})
# name=input("Enter your name:")
# lang=input("Enter the language:")
# d.update({name:lang})
# name=input("Enter your name:")
# lang=input("Enter the language:")
# d.update({name:lang})
# name=input("Enter your name:")
# lang=input("Enter the language:")
# d.update({name:lang})
# name=input("Enter your name:")
# lang=input("Enter the language:")
# d.update({name:lang})
# print(d) 

# d = []
# for i in range(5):
#     name = input("Enter your name: ")
#     lang = input("Enter the language: ")
#     d.append((name, lang))
# print(d)

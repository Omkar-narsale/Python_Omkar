# Multiple Inhertiance
# class Employee:
#     company="ITC"
#     name="Rahul"
#     salary=12000
#     def show(self):
#         print(f"The name of employee is {self.name} and salary is {self.salary}")

  
# class Coder:
#     language="Pyhton"
#     def printlanguage(self):
#      print(f"The Language used is {self.language}")

# class devloper(Employee,Coder):
#     company="ITC Infotech"
#     def showlanguage(self):
#         print(f"The devloper is good at {self.language}")        
# a=Employee()
# b=devloper()

# b.show()
# b.printlanguage()
# b.showlanguage()


# Multilevel Inheritance

# class Employee:
#     a=1
# class Devloper(Employee):
#     b=2
# class Manager(Devloper):
#     c=3

# o=Manager()    
# print(o.a,o.b,o.c)

#super Keyword
# class Employee:
#     def __init__(self):
#         print("Constructor of Employee")
#     a=1
# class Devloper(Employee):
#     def __init__(self):
#         super().__init__() # Calls Employee
#         print("Constructor of Devloper")
#     b=2
# class Manager(Devloper):
#     def __init__(self):# calls DEvloper
#         super().__init__()
#         print("Constructor of Manager")
#     c=3
# o=Manager()    
# print(o.a,o.b,o.c)

# Class Method 

# class Employee:
#     a=1
#     @classmethod  #A class method is a method bound to the class rather than an instance.
#     def show(cls):
#         print(f"The value of class Attribute is {cls.a}")
        
# e=Employee()
# e.a=45
# e.show()


# class TwoDvector:
#     def __init__(self,i,j):
#         self.i=i
#         self.j=j
    
#     def show(self):
#         print(f"The TwoDvector is {self.i}i + {self.j}j")

# class ThreeDvector(TwoDvector):
#     def __init__(self,i,j,k):
#         super().__init__(i,j)
#         self.k=k

#     def show(self):
#         print(f"The ThreeDvector is {self.i}i + {self.j}j + {self.k}k")

# m=TwoDvector(1,2)
# m.show()
# n=ThreeDvector(1,2,3)
# n.show()

# class Animal:
#     pass
# class Pets:
#     pass
# class Dog:
#     @staticmethod
#     def bark():
#         print("Bow Bow!")

# d=Dog()
# d.bark()

# class Employee:
#     salary=2300
#     increment=80
#     @property
#     def afterincrementsalary(self):
#      return(self.salary+self.salary*(self.increment/100))
 
# e=Employee()
# print(e.afterincrementsalary)


class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, c2):
        return Complex(self.r + c2.r, self.i + c2.i)

    def __str__(self):
        return f"{self.r} + {self.i}i"


c1 = Complex(1, 2)
c2 = Complex(3, 4)

print(c1 + c2)

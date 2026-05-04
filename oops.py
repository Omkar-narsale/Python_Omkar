# class Employee:
#     name="Omkar"
#     language="Python"# This is an calss attribute
#     salary="800000"

#     def __init__(self):
#      print("I am Learning Pyhton")

    # def getinfo(self): #self is a reference to the current object of a class.\
    #     #It is used to access variables and methods of that object.
    #  print(f"The language is {self.language}.The salary is {self.salary}")
 
    # @staticmethod #A static method in Python is a method that belongs to a class but does NOT use object data (self) or class data (cls).
    # def greet():
    #  print("Good Morning")

# omkar=Employee()
# omkar.getinfo()
# omkar.greet()


# here name is object attribute and language and salary are class attributes

# class Program:
#     company="Microsoft"
#     def __init__(self,name,salary,pin):
#         self.name=name
#         self.salary=salary
#         self.pin=pin
# p=Program("Omkar",123400,400703)
# print(p.name,p.salary,p.pin)
 
class Cal:
  def __init__(self,n):
    self.n=n

  def square(self):
    print(f"The square is {self.n*self.n} ")
 
  def cube(self):
    print(f"The cube is {self.n*self.n*self.n} ")

  def squareroot(self):
    print(f"The squareroot is {self.n**1/2} ")
  
  @staticmethod
  class Hello:
    print("Hello Bhai!")

a=Cal(4)
a.square()
a.cube()
a.squareroot()
a.Hello()
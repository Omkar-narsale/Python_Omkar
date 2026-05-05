def greater(func):
    def wrapper(a, b):
        if a > b:
            return func(a, b)
        else:
            return func(b, a)
    return wrapper
@greater # A decorator is a function that takes another function as input 
#and extends its behavior without modifying the original function's code. 
# It allows you to add functionality to an existing function in a clean and reusable way.
def divide(x, y):
    return x / y
result = divide(10, 5)
print("Result:", result)

@greater
def sub(a,b):
    return a-b
result1=sub(5,10)
print("Result:",result1)
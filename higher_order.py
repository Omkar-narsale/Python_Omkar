def square(num):
    return num**2
def cube(num):
    return num**3
higher_order_func=square # A higher order functon is a function that can take another function as 
#an argument or return a function as a result. 
print(f"The square of 5 is: {higher_order_func(5)}")
higher_order_func=cube
print(f"The cube of 5 is: {higher_order_func(5)}")

# value=5
# print(f"The square of {value} is: {square(value)}")
# print(f"The cube of {value} is: {cube(value)}") 

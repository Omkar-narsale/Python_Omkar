from functools import reduce
func= lambda num: num**2 #A lambda function is a small anonymous function that can take any number of arguments, 
#but can only have one expression.
print(func(9)) # Output: 81
add =lambda a,b: a+b
print(add(5,10)) # Output: 15
var=lambda x: "Even" if x%2==0 else "Odd"
print(var(5)) # Output: Odd
print(var(6)) # Output: Even


nums= [1,2,3,4,5,6,7,8,9,10]
evens=filter(lambda x: x%2==0, nums) # The filter() function constructs an iterator from elements of an iterable for which a function returns true.
print(list(map(lambda x: x**2, evens))) # Output: [4, 16, 36, 64, 100]
doubles=map(lambda x: x*2, nums) # The map() function applies a given function to each item of an iterable (list, tuple etc.) and returns a list of the results.
print(list(doubles)) # Output: [2, 4, 6, 8, 10]
sum=reduce(lambda x,y: x+y, nums) # The reduce() function applies a rolling computation to sequential pairs of values in a list.
print(sum) # Output: 55

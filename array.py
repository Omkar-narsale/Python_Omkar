from array import*
# arr=array('i',[10,20,30,40,50])
# print(type(arr))
# print(arr)
# arr.append(60)
# print(arr)
# print(arr.buffer_info())

value=int(input("Enter the Size of Array: "))
arr=array('i',[])
for i in range(value):
    num=int(input("Enter the Value: "))
    arr.append(num)
print(arr)
print(list(reversed(arr)))

num=int(input("Enter the Value to Search: "))
if num in arr:
    print("Value found at index",arr.index(num))
else:
    print("Value not found in the array")
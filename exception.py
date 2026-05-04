# try:
#     a=int(input("Enter any Number:"))
#     print(a)
# except Exception as e:
#     print(e)


a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))

if(b==0):
    raise ZeroDivisionError("NOt meant for divison")
else:
    print(a/b)
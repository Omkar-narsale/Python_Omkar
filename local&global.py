a=10 #global variable
def func():
    a=20 #local variable
    print("Inside the function:",a)
func()
print("Outside the function:",a)
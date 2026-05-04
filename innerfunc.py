def  outer():
    print("This is the outer function")
    def inner():
        print("This is the inner function")
    return inner
x=outer()
x()
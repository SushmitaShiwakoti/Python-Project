def inner1(func):
    def inner2():
        print("Befor Function Execution")
        func()
        print("After Function Execution")
    return inner2
@inner1
def fun():
    print("This is inside the function")

fun()  


# def factorial(n):
#     if n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
    
# x= factorial(3)
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
        # return "The factorial number  is: "+str(n*factorial(n-1))
x= factorial(5)
print("The factorial number  is:"+str(x))
